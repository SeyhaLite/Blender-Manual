#!/usr/bin/env python3
"""Generate ``manual/_data/upstream_labels.json``.

The Khmer manual is a *partial* translation. Upstream scatters ~5000 explicit
targets such as ``.. _bpy.ops.wm.save_mainfile:`` across the pages that
document each operator/property. Until those pages are translated, every
``:ref:`bpy.ops.wm.save_mainfile``` in the Khmer tree would be an unresolved
reference and would fail the ``-W`` build.

This script records, for every explicit target in the upstream tree, which
document defines it and what HTML fragment id docutils will give it. The
``km_xref_fallback`` Sphinx extension reads that map and rewrites the
unresolved reference into a link to the corresponding page of the official
English manual. As soon as a page is translated, its own local target wins
and the fallback stops firing — no source edits needed.

Usage:
    python3 tools/update_upstream_labels.py --upstream /path/to/upstream/manual
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys

from docutils.nodes import make_id

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(REPO, "manual", "_data", "upstream_labels.json")

# Explicit targets may be indented (inside list-table cells, admonitions, ...).
LABEL = re.compile(r"^\s*\.\.\s+_([^:\s][^:]*?):\s*(?:#.*)?$", re.M)

SKIP_DIRS = {".git", "build", "_build", "locale", "images"}


def collect(root: str):
    labels = {}
    dupes = []
    count = 0
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS)
        for name in sorted(filenames):
            if not name.endswith(".rst"):
                continue
            path = os.path.join(dirpath, name)
            count += 1
            docname = os.path.relpath(path, root)[:-4].replace(os.sep, "/")
            with open(path, encoding="utf-8") as handle:
                text = handle.read()
            for label in LABEL.findall(text):
                label = label.strip()
                if label in labels and labels[label] != docname:
                    dupes.append((label, labels[label], docname))
                    continue
                labels.setdefault(label, docname)
    return labels, dupes, count


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--upstream", required=True,
                        help="path to the upstream checkout's `manual/` directory")
    parser.add_argument("--commit", default="",
                        help="upstream commit sha, recorded in the output for provenance")
    args = parser.parse_args(argv)

    root = os.path.abspath(args.upstream)
    if not os.path.isdir(root):
        print("error: %s is not a directory" % root, file=sys.stderr)
        return 2

    labels, dupes, count = collect(root)

    # Compact encoding: intern the docnames, then map label -> index, and store
    # the pre-computed HTML fragment id only where it differs from the label.
    docs = sorted(set(labels.values()))
    doc_index = {d: i for i, d in enumerate(docs)}
    entries = {}
    for label, docname in sorted(labels.items()):
        frag = make_id(label)
        entries[label] = [doc_index[docname], frag]

    payload = {
        "source": "https://projects.blender.org/blender/blender-manual",
        "commit": args.commit,
        "rst_files": count,
        "docs": docs,
        "labels": entries,
    }

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, separators=(",", ":"), sort_keys=False)

    size = os.path.getsize(OUT)
    print("scanned %d .rst files" % count)
    print("labels    : %d (%d with a conflicting second definition ignored)"
          % (len(entries), len(dupes)))
    print("documents : %d" % len(docs))
    print("wrote %s (%.1f KB)" % (os.path.relpath(OUT, REPO), size / 1024.0))
    bpy = sum(1 for k in entries if k.startswith("bpy."))
    print("bpy.* labels: %d" % bpy)
    return 0


if __name__ == "__main__":
    sys.exit(main())

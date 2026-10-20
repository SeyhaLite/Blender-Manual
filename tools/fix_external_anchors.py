#!/usr/bin/env python3
"""Repair the #fragment of hand-written links into the English manual.

docutils derives an HTML ``id`` from an explicit target with
``docutils.nodes.make_id``, which lower-cases, turns *every* run of
non-alphanumeric characters (including ``_``) into a single ``-`` and strips
leading digits. Writing the label by hand therefore produces dead anchors:

    label                              hand-written (WRONG)      make_id (CORRECT)
    files-blend-relative_paths         #files-blend-relative_paths   #files-blend-relative-paths
    app_templates                      #app_templates                #app-templates
    3dview-fly-walk                    #3dview-fly-walk              #dview-fly-walk

This script finds every ``https://docs.blender.org/manual/en/<ver>/<doc>.html#frag``
link in the translated sources, recovers the original upstream label from
``manual/_data/upstream_labels.json`` and rewrites the fragment with
``make_id``. ``--check`` reports without writing.

Usage:
    python3 tools/fix_external_anchors.py --check
    python3 tools/fix_external_anchors.py --write
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import defaultdict

from docutils.nodes import make_id

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANUAL = os.path.join(REPO, "manual")
LABELS = os.path.join(MANUAL, "_data", "upstream_labels.json")

URL = re.compile(
    r"https://docs\.blender\.org/manual/en/([0-9.]+)/([A-Za-z0-9_./-]+?)\.html"
    r"(?:#([A-Za-z0-9_.\-]+))?")

SKIP = {"_data", "images"}


def load_labels():
    with open(LABELS, encoding="utf-8") as handle:
        payload = json.load(handle)
    docs = payload["docs"]
    # docname -> {naive_fragment: correct_fragment}
    table = defaultdict(dict)
    for label, entry in payload["labels"].items():
        docname, fragment = docs[entry[0]], entry[1]
        # how a human would most likely have typed this label by hand
        for naive in {label, label.replace(".", "-"), label.replace(".", "_"),
                      make_id(label.replace("_", "-"))}:
            table[docname].setdefault(naive, fragment)
    return table


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--check", action="store_true")
    group.add_argument("--write", action="store_true")
    args = parser.parse_args(argv)

    table = load_labels()
    fixed = unchanged = unverifiable = 0
    report = []

    for dirpath, dirnames, filenames in os.walk(MANUAL):
        dirnames[:] = [d for d in dirnames if d not in SKIP]
        for name in sorted(filenames):
            if not name.endswith(".rst"):
                continue
            path = os.path.join(dirpath, name)
            rel = os.path.relpath(path, MANUAL).replace(os.sep, "/")
            text = open(path, encoding="utf-8").read()
            original = text

            def repl(match: re.Match) -> str:
                nonlocal fixed, unchanged, unverifiable
                version, docname, fragment = match.group(1), match.group(2), match.group(3)
                base = "https://docs.blender.org/manual/en/%s/%s.html" % (version, docname)
                if not fragment:
                    unchanged += 1
                    return match.group(0)
                candidates = table.get(docname, {})
                correct = candidates.get(fragment)
                if correct is None:
                    # Maybe the fragment is already correct.
                    if fragment in set(candidates.values()):
                        unchanged += 1
                        return match.group(0)
                    unverifiable += 1
                    report.append("UNVERIFIED %s  %s#%s" % (rel, base, fragment))
                    return match.group(0)
                if correct == fragment:
                    unchanged += 1
                    return match.group(0)
                fixed += 1
                report.append("FIXED      %s  %s#%s  ->  #%s"
                              % (rel, base, fragment, correct))
                return base + "#" + correct

            text = URL.sub(repl, text)
            if text != original and args.write:
                open(path, "w", encoding="utf-8").write(text)

    for line in report:
        print(line)
    print("\n%d fixed, %d already correct, %d unverifiable"
          % (fixed, unchanged, unverifiable))
    if args.check and (fixed or unverifiable):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

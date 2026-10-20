#!/usr/bin/env python3
"""Normalise reStructuredText title adornments.

Khmer titles are much wider than their Latin originals, and docutils compares
adornment length against the *character count* of the title line. A title like::

    ##########
      តំបន់ (Areas)
    ##########

triggers ``WARNING: Title overline too short`` because the Khmer text has more
characters than the ten ``#`` above it.

This script grows every overline/underline so that it is at least as long as
its title, leaving transitions (``----`` surrounded by blank lines) and
over-long adornments untouched.

Usage:
    python3 tools/normalize_titles.py            # dry run, report only
    python3 tools/normalize_titles.py --write    # apply changes
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from typing import List

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANUAL = os.path.join(REPO, "manual")

# docutils treats any repeated non-alphanumeric printable character as an
# adornment. ``-`` needs care because it is also used for transitions.
ADORNMENT = re.compile(r"^([^\sA-Za-z0-9])\1+$")

SKIP_DIRS = {".git", "build", "_build"}

# Documents kept byte-identical to upstream must never be rewritten.
SKIP_FILES = {
    os.path.join("getting_started", "about", "history.rst"),
}


def is_adornment(line: str) -> bool:
    return bool(ADORNMENT.match(line.rstrip("\n")))


def is_blank(line: str) -> bool:
    return not line.strip()


def fix_file(path: str, write: bool) -> List[str]:
    with open(path, encoding="utf-8") as handle:
        text = handle.read()

    # Keep line endings stable; operate on a list of lines without the "\n".
    trailing_newline = text.endswith("\n")
    lines = text.split("\n")
    if trailing_newline:
        lines = lines[:-1]

    changes: List[str] = []
    n = len(lines)
    i = 0
    while i < n:
        line = lines[i]
        if is_adornment(line):
            char = line[0]
            # Case A: overline + title + underline
            if (i + 2 < n and is_adornment(lines[i + 2]) and lines[i + 2][0] == char
                    and not is_adornment(lines[i + 1]) and lines[i + 1].strip()):
                title = lines[i + 1]
                want = max(len(title), len(line), len(lines[i + 2]))
                if want != len(line) or want != len(lines[i + 2]):
                    changes.append(
                        "line %d: overline/underline %d/%d -> %d for %r"
                        % (i + 1, len(line), len(lines[i + 2]), want, title.strip()[:40]))
                    lines[i] = char * want
                    lines[i + 2] = char * want
                i += 3
                continue
            # Case B: title + underline (a transition has a blank line above)
            if (i > 0 and lines[i - 1].strip() and not is_adornment(lines[i - 1])
                    and (i + 1 >= n or is_blank(lines[i + 1]))):
                title = lines[i - 1]
                if len(line) < len(title):
                    changes.append(
                        "line %d: underline %d -> %d for %r"
                        % (i + 1, len(line), len(title), title.strip()[:40]))
                    lines[i] = char * len(title)
        i += 1

    if changes and write:
        new_text = "\n".join(lines)
        if trailing_newline:
            new_text += "\n"
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(new_text)

    return changes


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--write", action="store_true", help="apply the changes")
    args = parser.parse_args(argv)

    total = 0
    touched = 0
    for dirpath, dirnames, filenames in os.walk(MANUAL):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in sorted(filenames):
            if not name.endswith(".rst"):
                continue
            path = os.path.join(dirpath, name)
            if os.path.relpath(path, MANUAL) in SKIP_FILES:
                continue
            changes = fix_file(path, args.write)
            if changes:
                touched += 1
                total += len(changes)
                print(os.path.relpath(path, REPO))
                for change in changes:
                    print("   ", change)

    verb = "fixed" if args.write else "would fix"
    print("\n%s %d adornment(s) in %d file(s)." % (verb, total, touched))
    return 0


if __name__ == "__main__":
    sys.exit(main())

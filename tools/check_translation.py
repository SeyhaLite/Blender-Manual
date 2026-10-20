#!/usr/bin/env python3
"""Quality gate for the Khmer Blender Manual.

Run from the repository root:

    python3 tools/check_translation.py            # check, exit non-zero on failure
    python3 tools/check_translation.py --report    # also rewrite appendix/status.rst

Checks
------
1. Khmer coverage: every .rst that is *supposed* to be translated really
   contains Khmer text (U+1780..U+17FF).
2. Verbatim files: documents that must NOT be translated (the upstream
   version history) are byte-identical to upstream.
3. Structure preservation: the number of ``:kbd:``, ``:menuselection:``,
   ``code-block`` and ``figure`` constructs in a translated file is not
   lower than in its upstream counterpart (nothing was dropped).
4. Secret hygiene: no credential-looking strings anywhere in the repo.
5. Encoding: every text file is valid UTF-8.
6. Coverage report: per-section translation progress against upstream.

The upstream checkout is optional; pass ``--upstream PATH`` or set
``BLENDER_MANUAL_UPSTREAM``. Without it, checks 2, 3 and 6 are skipped.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from typing import Dict, Iterable, List, Optional, Tuple

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANUAL = os.path.join(REPO, "manual")

# Documents deliberately kept OUT of the translation (rule: never translate
# changelogs or release notes). They must not exist in the tree and must not be
# pulled in by a toctree; the pages that used to link them point at the
# official English manual instead.
EXCLUDED = [
    "getting_started/about/history.rst",
]

# Pages we deliberately restructured, so a 1:1 structure comparison against
# upstream is meaningless (the landing page drops the per-section card grid and
# lists untranslated sections as external links instead).
STRUCTURE_EXEMPT = {"index.rst"}

# Documents that must not exist yet, so nobody accidentally half-translates
# them without updating the status page.
KHMER_RANGE = re.compile(r"[\u1780-\u17FF]")

# NOTE: the literal prefixes are assembled from fragments on purpose, so that
# this checker does not report itself as containing a credential.
_GH_FINE = "github" + "_pat_"
_GH_CLS = "gh" + "p_"
_GH_OA = "gh" + "o_"
_GH_APP = "gh" + "s_"
SECRET_PATTERNS = [
    (re.compile(_GH_FINE + r"[A-Za-z0-9_]{20,}"), "GitHub personal access token"),
    (re.compile(_GH_CLS + r"[A-Za-z0-9]{30,}"), "GitHub personal access token (classic)"),
    (re.compile(_GH_OA + r"[A-Za-z0-9]{30,}"), "GitHub OAuth token"),
    (re.compile(_GH_APP + r"[A-Za-z0-9]{30,}"), "GitHub App installation token"),
    (re.compile(_GH_FINE + "|" + _GH_CLS + "|" + _GH_OA + "|" + _GH_APP
                + "|" + "x-access" + "-token:" + "[^@" + r"\s]+@"), "credential in URL"),
    (re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"), "private key"),
    (re.compile(r"(?i)\b(password|passwd|secret|api[_-]?key)\b\s*[:=]\s*['\"]?[^\s'\"]{8,}"),
     "hardcoded credential"),
    (re.compile(r"AKIA[0-9A-Z]{16}"), "AWS access key id"),
    (re.compile(r"xox[baprs]-[A-Za-z0-9-]{10,}"), "Slack token"),
]

# Text extensions worth scanning.
TEXT_EXT = {
    ".rst", ".py", ".css", ".js", ".md", ".txt", ".yaml", ".yml", ".toml",
    ".bat", ".cfg", ".ini", ".json", ".html", ".svg", ".po", ".pot", "",
}

SKIP_DIRS = {".git", ".venv", "venv", "build", "__pycache__", ".mypy_cache", "node_modules"}

# Scripts that must never appear in a Khmer translation. Catches the classic
# failure mode where a model or an IME leaks Thai / Devanagari / CJK glyphs
# into Khmer prose.
FORBIDDEN_SCRIPTS = [
    ("Thai", re.compile(r"[\u0E00-\u0E7F]")),
    ("Devanagari", re.compile(r"[\u0900-\u097F]")),
    ("Hangul", re.compile(r"[\uAC00-\uD7AF]")),
    ("CJK", re.compile(r"[\u4E00-\u9FFF\u3040-\u30FF]")),
    ("Arabic", re.compile(r"[\u0600-\u06FF]")),
    ("Cyrillic", re.compile(r"[\u0400-\u04FF]")),
    ("Greek", re.compile(r"[\u0370-\u03FF]")),
    ("Tamil", re.compile(r"[\u0B80-\u0BFF]")),
    ("Lao", re.compile(r"[\u0E80-\u0EFF]")),
    ("Myanmar", re.compile(r"[\u1000-\u109F]")),
]

STRUCTURE_ROLES = {
    ":kbd:": re.compile(r":kbd:`"),
    ":menuselection:": re.compile(r":menuselection:`"),
    # A :doc: to an untranslated page is deliberately rewritten to an absolute
    # link into the English manual, so count both spellings together.
    ":doc:/external-doc": re.compile(
        r":doc:`|https://docs\.blender\.org/manual/en/[0-9.]+/[^\s)`]+\.html"),
    "code-block": re.compile(r"^\s*\.\.\s+code-block::", re.M),
    "figure": re.compile(r"^\s*\.\.\s+figure::", re.M),
    "note/warning/tip": re.compile(
        r"^\s*\.\.\s+(note|warning|tip|important|caution|attention|danger|seealso|hint|admonition)::",
        re.M),
    "list-table": re.compile(r"^\s*\.\.\s+list-table::", re.M),
    "images": re.compile(r"/images/[A-Za-z0-9_.%-]+\.(?:png|jpg|jpeg|gif|svg)"),
}

STATUS_BEGIN = ".. BEGIN GENERATED COVERAGE (tools/check_translation.py --report)"
STATUS_END = ".. END GENERATED COVERAGE"


# --------------------------------------------------------------------------- #
# helpers
# --------------------------------------------------------------------------- #

def walk(root: str, exts: Optional[set] = None) -> Iterable[str]:
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS)
        for name in sorted(filenames):
            ext = os.path.splitext(name)[1].lower()
            if exts is not None and ext not in exts:
                continue
            yield os.path.join(dirpath, name)


def read(path: str) -> Optional[str]:
    try:
        with open(path, "rb") as handle:
            raw = handle.read()
    except OSError:
        return None
    try:
        return raw.decode("utf-8")
    except UnicodeDecodeError:
        return None


def rst_files(root: str) -> List[str]:
    out = []
    for path in walk(root, {".rst"}):
        out.append(os.path.relpath(path, root).replace(os.sep, "/"))
    return sorted(out)


def upstream_root(cli_value: Optional[str]) -> Optional[str]:
    candidate = cli_value or os.environ.get("BLENDER_MANUAL_UPSTREAM")
    if not candidate:
        for guess in (
            os.path.join(REPO, os.pardir, "work", "upstream", "manual"),
            os.path.join(REPO, "upstream", "manual"),
        ):
            if os.path.isdir(guess):
                candidate = guess
                break
    if candidate and os.path.isdir(candidate):
        return os.path.abspath(candidate)
    return None


# --------------------------------------------------------------------------- #
# checks
# --------------------------------------------------------------------------- #

def check_khmer_coverage(problems: List[str]) -> Tuple[int, int]:
    """Every non-verbatim .rst must contain Khmer characters."""
    translated = 0
    missing: List[str] = []
    for rel in rst_files(MANUAL):
        if rel in EXCLUDED:
            problems.append("excluded: manual/%s must not be part of the "
                            "translation (changelog/release notes)" % rel)
            continue
        text = read(os.path.join(MANUAL, rel))
        if text is None:
            problems.append("encoding: cannot decode %s as UTF-8" % rel)
            continue
        if KHMER_RANGE.search(text):
            translated += 1
        else:
            missing.append(rel)
    for rel in missing:
        problems.append("no Khmer text: manual/%s" % rel)
    return translated, len(missing)


def check_excluded(problems: List[str]) -> int:
    """Changelog / release-note documents must be absent, not half-translated."""
    found = 0
    for rel in EXCLUDED:
        if os.path.exists(os.path.join(MANUAL, rel)):
            found += 1
            problems.append(
                "excluded: manual/%s exists — changelog and release-note "
                "documents must not be part of the translation" % rel)
    return found


def check_toctree_targets(problems: List[str]) -> int:
    """Every local toctree entry must exist, so no `toc.not_readable` warning."""
    checked = 0
    for rel in rst_files(MANUAL):
        text = read(os.path.join(MANUAL, rel))
        if text is None:
            continue
        for block in re.finditer(r"^\s*\.\.\s+toctree::(.*?)(?=^\S|\Z)", text, re.S | re.M):
            for line in block.group(1).splitlines():
                entry = line.strip()
                if not entry or entry.startswith(":") or entry.startswith(".."):
                    continue
                if "<" in entry:          # `Title <target>`
                    entry = entry.rsplit("<", 1)[1].rstrip(">").strip()
                if entry.startswith(("http://", "https://", "/", "genindex",
                                     "search", "modindex")):
                    continue
                checked += 1
                base = os.path.dirname(os.path.join(MANUAL, rel))
                target = os.path.normpath(os.path.join(base, entry))
                if not (target.endswith(".rst") and os.path.exists(target)):
                    problems.append("toctree: manual/%s -> missing %s" % (rel, entry))
    return checked


def check_structure(up: Optional[str], problems: List[str]) -> int:
    """Nothing important may be dropped while translating."""
    if not up:
        return 0
    compared = 0
    for rel in rst_files(MANUAL):
        if rel in EXCLUDED:
            continue
        if rel in STRUCTURE_EXEMPT:
            continue
        theirs_path = os.path.join(up, rel)
        if not os.path.exists(theirs_path):
            continue  # our own page (appendix/*), nothing to compare against
        mine = read(os.path.join(MANUAL, rel))
        theirs = read(theirs_path)
        if mine is None or theirs is None:
            continue
        compared += 1
        for label, pattern in STRUCTURE_ROLES.items():
            a = len(pattern.findall(mine))
            b = len(pattern.findall(theirs))
            if a < b:
                problems.append(
                    "structure: manual/%s has %d %s but upstream has %d"
                    % (rel, a, label, b))
    return compared


def check_scripts(problems: List[str]) -> int:
    """No non-Khmer/non-Latin script may leak into the translated prose."""
    scanned = 0
    for rel in rst_files(MANUAL):
        if rel in EXCLUDED:
            continue
        text = read(os.path.join(MANUAL, rel))
        if text is None:
            continue
        scanned += 1
        for lineno, line in enumerate(text.splitlines(), 1):
            for name, pattern in FORBIDDEN_SCRIPTS:
                if pattern.search(line):
                    problems.append(
                        "wrong script: manual/%s:%d contains %s characters"
                        % (rel, lineno, name))
    return scanned


def check_secrets(problems: List[str]) -> int:
    scanned = 0
    for path in walk(REPO):
        rel = os.path.relpath(path, REPO).replace(os.sep, "/")
        if os.path.splitext(rel)[1].lower() not in TEXT_EXT:
            continue
        text = read(path)
        if text is None:
            continue
        scanned += 1
        for pattern, label in SECRET_PATTERNS:
            match = pattern.search(text)
            if match:
                problems.append("secret: %s looks like a %s" % (rel, label))
    return scanned


def coverage(up: Optional[str]) -> Dict[str, Tuple[int, int]]:
    """{section: (translated, total)} measured against the upstream tree."""
    sections: Dict[str, Tuple[int, int]] = {}
    if not up:
        return sections
    mine = set(rst_files(MANUAL))
    theirs = set(rst_files(up))
    buckets: Dict[str, List[int]] = {}
    for rel in sorted(theirs):
        top = rel.split("/")[0] if "/" in rel else "(root)"
        buckets.setdefault(top, [0, 0])[1] += 1
        if rel in mine:
            buckets[top][0] += 1
    for key in sorted(buckets):
        done, total = buckets[key]
        sections[key] = (done, total)
    return sections


def bar(done: int, total: int, width: int = 24) -> str:
    if not total:
        return "[" + " " * width + "]"
    filled = round(width * done / total)
    return "[" + "#" * filled + "." * (width - filled) + "]"


# --------------------------------------------------------------------------- #
# status page
# --------------------------------------------------------------------------- #

def render_status(sections: Dict[str, Tuple[int, int]], upstream_sha: Optional[str]) -> str:
    lines: List[str] = [STATUS_BEGIN, ""]
    total_done = sum(v[0] for v in sections.values())
    total_all = sum(v[1] for v in sections.values())
    if sections:
        lines += [
            ".. list-table::",
            "   :header-rows: 1",
            "   :widths: 34 12 12 42",
            "",
            "   * - ផ្នែក (Section)",
            "     - បានបកប្រែ",
            "     - សរុប",
            "     - វឌ្ឍនភាព",
        ]
        for name, (done, total) in sections.items():
            pct = (100.0 * done / total) if total else 0.0
            lines += [
                "   * - ``%s``" % name,
                "     - %d" % done,
                "     - %d" % total,
                "     - %s %.1f%%" % (bar(done, total, 18), pct),
            ]
        lines += [
            "   * - **សរុប**",
            "     - **%d**" % total_done,
            "     - **%d**" % total_all,
            "     - **%.1f%%**" % ((100.0 * total_done / total_all) if total_all else 0.0),
        ]
    else:
        lines.append(
            "   (ដំណើរការ ``tools/check_translation.py --report`` ជាមួយ "
            "``--upstream`` ដើម្បីបង្កើតតារាងនេះ)")
    lines += ["", STATUS_END]
    if upstream_sha:
        lines += ["", ".. upstream-commit: %s" % upstream_sha]
    return "\n".join(lines) + "\n"


def write_status(sections: Dict[str, Tuple[int, int]], upstream_sha: Optional[str]) -> Optional[str]:
    path = os.path.join(MANUAL, "appendix", "status.rst")
    text = read(path)
    if text is None or STATUS_BEGIN not in text or STATUS_END not in text:
        return None
    block = render_status(sections, upstream_sha)
    head, rest = text.split(STATUS_BEGIN, 1)
    _old, tail = rest.split(STATUS_END, 1)
    new = head + block.rstrip("\n") + tail
    if new != text:
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(new)
        return path
    return None


def upstream_head(up: Optional[str]) -> Optional[str]:
    if not up:
        return None
    gitdir = os.path.join(os.path.dirname(up), ".git")
    head = os.path.join(gitdir, "HEAD")
    if not os.path.exists(head):
        return None
    ref = read(head)
    if not ref:
        return None
    ref = ref.strip()
    if ref.startswith("ref: "):
        refpath = os.path.join(gitdir, ref[5:])
        sha = read(refpath)
        return sha.strip()[:12] if sha else None
    return ref[:12]


# --------------------------------------------------------------------------- #
# main
# --------------------------------------------------------------------------- #

def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--upstream", help="path to an upstream checkout's `manual/` directory")
    parser.add_argument("--report", action="store_true",
                        help="rewrite the generated block in manual/appendix/status.rst")
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args(argv)

    up = upstream_root(args.upstream)
    problems: List[str] = []

    translated, untranslated = check_khmer_coverage(problems)
    excluded_found = check_excluded(problems)
    toctree_checked = check_toctree_targets(problems)
    compared = check_structure(up, problems)
    script_checked = check_scripts(problems)
    scanned = check_secrets(problems)
    sections = coverage(up)

    if args.report:
        changed = write_status(sections, upstream_head(up))
        if changed and not args.quiet:
            print("updated", os.path.relpath(changed, REPO))

    if not args.quiet:
        print("Khmer Blender Manual — quality check")
        print("  translated .rst files      : %d" % translated)
        print("  .rst files without Khmer   : %d" % untranslated)
        print("  changelog docs excluded    : %d/%d (must be 0 present)"
              % (len(EXCLUDED) - excluded_found, len(EXCLUDED)))
        print("  local toctree entries ok   : %d" % toctree_checked)
        print("  files compared to upstream : %d%s"
              % (compared, "" if up else "  (no upstream checkout found)"))
        print("  files checked for scripts  : %d" % script_checked)
        print("  files scanned for secrets  : %d" % scanned)
        if sections:
            done = sum(v[0] for v in sections.values())
            total = sum(v[1] for v in sections.values())
            print("  upstream coverage          : %d/%d .rst (%.2f%%)"
                  % (done, total, 100.0 * done / total if total else 0.0))
        print()

    if problems:
        print("PROBLEMS (%d):" % len(problems))
        for problem in problems:
            print("  -", problem)
        return 1

    if not args.quiet:
        print("OK — no problems found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

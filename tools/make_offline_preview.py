#!/usr/bin/env python3
"""Build ONE self-contained offline HTML preview of the built documentation.

Everything is inlined so the result opens correctly with no network access and
no sibling files:

* every ``<link rel=stylesheet>`` becomes a ``<style>`` block
* every ``url(...)`` font reference inside those stylesheets becomes a base64
  data URI (only woff2 is kept for the icon font; the legacy eot/ttf/svg
  fallbacks are dropped to keep the file small)
* every ``<img src>`` becomes a base64 data URI
* every ``<script src>`` is inlined, so the light/dark/auto toggle still works
* local ``*.html`` links are neutralised to ``#`` (they cannot resolve inside a
  single-file preview); external https links are left intact

``--extra-article`` stitches the ``<article role="main">`` of other built pages
underneath the main one. No single page of the manual happens to contain every
element type, so this is how one preview file can show tables, ``:kbd:`` chips,
code blocks, admonitions, ``.. reference::`` boxes, the icon font and the
"EN" fallback badges together. It is a preview convenience only — it never
touches the manual sources.

Usage:
    make html
    python3 tools/make_offline_preview.py \
        --page interface/operators \
        --extra-article getting_started/installing/linux_windowing_environment \
        --extra-article interface/window_system/tabs_panels \
        --out ../preview.html
"""

from __future__ import annotations

import argparse
import base64
import mimetypes
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD = os.path.join(REPO, "build", "html")

MIME = {
    ".css": "text/css",
    ".js": "text/javascript",
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".gif": "image/gif",
    ".svg": "image/svg+xml",
    ".webp": "image/webp",
    ".woff": "font/woff",
    ".woff2": "font/woff2",
    ".ttf": "font/ttf",
    ".eot": "application/vnd.ms-fontobject",
    ".ico": "image/x-icon",
}

ICON_LEGACY_EXTS = {".eot", ".ttf", ".svg", ".woff"}


def data_uri(path: str):
    if not os.path.isfile(path):
        return None
    ext = os.path.splitext(path)[1].lower()
    mime = MIME.get(ext) or mimetypes.guess_type(path)[0] or "application/octet-stream"
    with open(path, "rb") as handle:
        blob = base64.b64encode(handle.read()).decode("ascii")
    return "data:%s;base64,%s" % (mime, blob)


def resolve(base_dir: str, href: str) -> str:
    """Resolve a relative asset reference against the page that contains it."""
    return os.path.normpath(os.path.join(base_dir, href.split("?")[0].split("#")[0]))


def inline_css_urls(css: str, base_dir: str, stats: dict) -> str:
    def repl(match: re.Match) -> str:
        raw = match.group(1).strip().strip("'\"")
        if not raw or raw.startswith(("data:", "http://", "https://", "//")):
            return match.group(0)
        target = resolve(base_dir, raw)
        ext = os.path.splitext(target)[1].lower()
        name = os.path.basename(target)
        if ext in ICON_LEGACY_EXTS and name.startswith("bl-icons"):
            return "url('')"          # keep woff2 only
        uri = data_uri(target)
        if not uri:
            return match.group(0)
        stats["font"] += 1
        return "url('%s')" % uri

    return re.sub(r"url\(([^)]*)\)", repl, css)


def inline_images(html: str, base_dir: str, stats: dict) -> str:
    def repl(match: re.Match) -> str:
        prefix, src, suffix = match.group(1), match.group(2), match.group(3)
        if src.startswith(("http://", "https://", "//", "data:")):
            return match.group(0)
        uri = data_uri(resolve(base_dir, src))
        if not uri:
            return match.group(0)
        stats["img"] += 1
        return "%s%s%s" % (prefix, uri, suffix)

    html = re.sub(r'(<img[^>]*\bsrc=")([^"]*)("[^>]*>)', repl, html)
    html = re.sub(r'(<link[^>]*\bhref=")([^"]*\.(?:png|ico|svg))("[^>]*>)', repl, html)
    return html


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--page", required=True,
                        help="docname of the built page, e.g. interface/operators")
    parser.add_argument("--out", required=True, help="output .html path")
    parser.add_argument("--build", default=BUILD)
    parser.add_argument("--extra-article", action="append", default=[],
                        help="docname whose <article> is appended to the preview "
                             "(repeatable)")
    args = parser.parse_args(argv)

    build = os.path.abspath(args.build)
    page_path = os.path.join(build, args.page + ".html")
    if not os.path.isfile(page_path):
        print("error: built page not found: %s" % page_path, file=sys.stderr)
        print("       run `make html` first", file=sys.stderr)
        return 2

    with open(page_path, encoding="utf-8") as handle:
        html = handle.read()

    page_dir = os.path.dirname(page_path)
    stats = {"css": 0, "js": 0, "img": 0, "font": 0, "stitched": 0}

    # -- stylesheets -------------------------------------------------------- #
    def link_repl(match: re.Match) -> str:
        href = match.group("href")
        if href.startswith(("http://", "https://", "//", "data:")):
            return match.group(0)
        path = resolve(page_dir, href)
        if not os.path.isfile(path):
            return "<!-- missing stylesheet %s -->" % href
        with open(path, encoding="utf-8") as handle:
            css = handle.read()
        stats["css"] += 1
        return "<style data-source=\"%s\">\n%s\n</style>" % (
            href, inline_css_urls(css, os.path.dirname(path), stats))

    html = re.sub(r'<link[^>]*rel="stylesheet"[^>]*href="(?P<href>[^"]*)"[^>]*/?>',
                  link_repl, html)
    html = re.sub(r'<link[^>]*href="(?P<href>[^"]*\.css[^"]*)"[^>]*/?>',
                  link_repl, html)

    # -- scripts ------------------------------------------------------------ #
    def script_repl(match: re.Match) -> str:
        src = match.group(1)
        if src.startswith(("http://", "https://", "//", "data:")):
            return match.group(0)
        path = resolve(page_dir, src)
        if not os.path.isfile(path):
            return "<!-- missing script %s -->" % src
        with open(path, encoding="utf-8") as handle:
            js = handle.read()
        stats["js"] += 1
        return "<script data-source=\"%s\">%s</script>" % (src, js)

    html = re.sub(r'<script[^>]*src="([^"]*)"[^>]*>\s*</script>', script_repl, html)

    # -- images of the main page ------------------------------------------- #
    html = inline_images(html, page_dir, stats)

    # -- stitch in extra articles ------------------------------------------- #
    # Inserted right after the first </article>, so iterate in reverse to
    # keep the final visual order equal to the CLI order.
    for extra in reversed(args.extra_article):
        extra_path = os.path.join(build, extra + ".html")
        if not os.path.isfile(extra_path):
            print("warning: extra page not found, skipped: %s" % extra, file=sys.stderr)
            continue
        with open(extra_path, encoding="utf-8") as handle:
            extra_html = handle.read()
        found = re.search(r'(<article[^>]*role="main"[^>]*>.*?</article>)',
                          extra_html, re.S)
        if not found:
            print("warning: no <article role=main> in %s, skipped" % extra,
                  file=sys.stderr)
            continue
        fragment = found.group(1)
        # Images inside the fragment are relative to *that* page's directory,
        # which is usually a different depth than the shell page.
        fragment = inline_images(fragment, os.path.dirname(extra_path), stats)
        divider = (
            '<hr style="margin:3rem 0;border:0;border-top:2px dashed '
            'var(--color-background-border)">'
            '<p style="font-size:.85rem;opacity:.75">Stitched in from '
            '<code>%s</code> for preview purposes.</p>' % extra)
        html = re.sub(r"</article>",
                      lambda m, d=divider, f=fragment: m.group(0) + d + f,
                      html, count=1)
        stats["stitched"] += 1

    # -- neutralise local navigation ---------------------------------------- #
    html = re.sub(r'\bhref="(?!https?:|//|#|mailto:|data:)([^"]*?\.html(?:#[^"]*)?)"',
                  r'href="#" title="offline preview — original target: \1"', html)

    banner = (
        '<div style="position:sticky;top:0;z-index:9999;background:#1f2933;color:#f2f5f8;'
        'font:13px/1.6 system-ui,sans-serif;padding:6px 14px;border-bottom:1px solid #3a414d">'
        'Offline preview — one self-contained file (all CSS, fonts, images and JS inlined). '
        'Local navigation is disabled; the light/dark/auto toggle works.'
        '</div>')
    html = html.replace("<body", banner + "<body", 1)

    out = os.path.abspath(args.out)
    if os.path.dirname(out):
        os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as handle:
        handle.write(html)

    print("wrote %s (%.1f KB)" % (out, os.path.getsize(out) / 1024.0))
    print("  inlined : %d stylesheet(s), %d script(s), %d image(s), %d font file(s)"
          % (stats["css"], stats["js"], stats["img"], stats["font"]))
    print("  stitched: %d extra article(s)" % stats["stitched"])

    leftover = re.findall(r'<link[^>]*rel="stylesheet"[^>]*>', html)
    leftover += re.findall(r'<script[^>]*\bsrc="[^"]*"', html)
    leftover += re.findall(r'<img[^>]*\bsrc="(?!data:)[^"]*"', html)
    if leftover:
        print("  WARNING: %d external asset reference(s) remain:" % len(leftover))
        for item in leftover[:5]:
            print("   ", item[:140])
        return 1
    print("  no external asset references remain")
    return 0


if __name__ == "__main__":
    sys.exit(main())

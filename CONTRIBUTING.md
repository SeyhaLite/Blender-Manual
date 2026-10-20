# Contributing to the Khmer Blender Manual

Thank you for your interest. The full, Khmer-language contributor guide —
including the complete terminology table and translation rules — lives at
[`manual/appendix/contributing.rst`](manual/appendix/contributing.rst) and is
published on the site. This file is the short English summary.

---

## License — read this first

| | |
|---|---|
| Source | [`blender/blender-manual`](https://projects.blender.org/blender/blender-manual), branch `blender-v5.2-release` |
| Content licence | [CC-BY-SA 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/) |
| Code licence (`build_files/extensions/*`, `tools/*`) | `GPL-2.0-or-later` |

By contributing you agree that your text is released under **CC-BY-SA 4.0** and
that you do **not** hold exclusive copyright over it. Others may edit your
translation to keep the manual consistent. See [`manual/copyright.rst`](manual/copyright.rst).

Never commit a token, password, API key or private key. `make check` scans for
them and fails the build if one is found.

---

## Ground rules

1. **Translate teaching content only.** Never translate or edit changelog,
   release-note or version-history documents. `getting_started/about/history.rst`
   is deliberately excluded from this repository for that reason.
2. **Keep technical names in English:** Python identifiers, `bpy.ops.*`,
   `bpy.types.*`, operator and property names, menu paths inside
   `:menuselection:`, keyboard shortcuts inside `:kbd:`, GUI labels inside
   `:guilabel:`, file extensions, shell commands and every code example.
   The Blender UI ships in English, so a Khmer reader must be able to match
   what the manual says to what they see on screen.
3. **Translate** headings, prose, figure captions, table headers and
   admonition titles.
4. **Never invent** a button, feature, menu or step that does not exist in
   Blender 5.2. Verify against the upstream `.rst`.
5. **Never drop** a warning, safety notice, note, example, code block or link.
   `tools/check_translation.py` compares those counts against upstream.
6. **No broken links.** See the cross-reference rules below.

### Terminology

Use the standard Khmer term for a given English term, every time. The canonical
list is the table in
[`manual/appendix/contributing.rst`](manual/appendix/contributing.rst) and
[`manual/glossary/index.rst`](manual/glossary/index.rst). If you introduce a new
term, add it to **both**.

At the first mention in a page, write the Khmer term with the English in
parentheses — «ផ្ទាំង (Panel)» — then use the Khmer term alone afterwards.

---

## Cross-references (the part that breaks builds)

Upstream uses `:doc:` and `:ref:` heavily. Because this is a *partial*
translation, most of those targets do not exist here yet, and `make html` runs
with `-W`, so any unresolved reference fails the build.

| Situation | What to write |
|---|---|
| Target is translated | Keep the role: `` :doc:`តំបន់ </interface/window_system/areas>` `` |
| `bpy.ops.*` / `bpy.types.*` | **Keep the `:ref:` unchanged.** The [`km_xref_fallback`](build_files/extensions/km_xref_fallback.py) extension resolves it against the English manual automatically. Once you translate the defining page, its local target wins and nothing needs editing. |
| Any other `:doc:`/`:ref:` to an untranslated page | Rewrite as an absolute link into the **pinned version**, not `latest`:<br>`` `Preferences <https://docs.blender.org/manual/en/5.2/editors/preferences/index.html>`__ `` |
| External website | Leave as-is |

To find where a label is defined upstream:

```sh
git clone --depth 1 --filter=blob:none --sparse \
    --branch blender-v5.2-release \
    https://projects.blender.org/blender/blender-manual.git ../upstream
cd ../upstream
git sparse-checkout init --no-cone
printf '%s\n' '/manual/**/*.rst' > .git/info/sparse-checkout
git read-tree -mu HEAD          # ~17 MB, .rst only, no images
grep -rn '^\s*\.\. _my-label:' manual/
```

#### Anchor fragments — do not hand-write them

The `#fragment` of a link into the English manual is **not** the upstream label.
docutils derives the HTML `id` with `docutils.nodes.make_id`, which lower-cases,
collapses *every* run of non-alphanumeric characters (including `_`) into one
`-`, and strips leading digits:

| upstream label | hand-written (dead) | `make_id` (correct) |
|---|---|---|
| `files-blend-relative_paths` | `#files-blend-relative_paths` | `#files-blend-relative-paths` |
| `app_templates` | `#app_templates` | `#app-templates` |
| `3dview-fly-walk` | `#3dview-fly-walk` | `#dview-fly-walk` |
| `bpy.ops.wm.save_mainfile` | `#bpy.ops.wm.save_mainfile` | `#bpy-ops-wm-save-mainfile` |

Always run the checker before committing; it rewrites them from the label map:

```sh
python3 tools/fix_external_anchors.py --check   # report
python3 tools/fix_external_anchors.py --write   # repair
make linkcheck                                   # must exit 0
```

`tools/make_offline_preview.py` and `tools/fix_external_anchors.py` both read the
same map, and `km_xref_fallback` computes fragments with `make_id`, so the
automatic links were always correct — only hand-written ones need this.

`manual/_data/upstream_labels.json` already contains the full
label → document map (5486 labels over 1565 documents) if you prefer to look it
up offline:

```sh
python3 -c "import json;d=json.load(open('manual/_data/upstream_labels.json'));\
v=d['labels']['bpy.ops.wm.save_mainfile'];print(d['docs'][v[0]]+'#'+v[1])"
```

---

## Workflow

```sh
make setup
# ...edit...
python3 tools/normalize_titles.py --write      # fix RST title adornment widths
python3 tools/fix_external_anchors.py --write  # repair English-manual #anchors
make html                                      # must exit 0, zero warnings
python3 tools/check_translation.py --report --upstream ../upstream/manual
make linkcheck                                 # needs network; must exit 0
```

`make linkcheck` exits 0 today: **159 working, 0 broken**. The `linkcheck_ignore`
list in `manual/conf.py` holds only URLs copied verbatim from upstream whose
sites answer a non-browser client with 400/403/429 (Reddit, Stack Exchange,
forum.htc.com, packages.debian.org, matrix.to SPA routes, …). Each is commented
with the reason. Do not add anything else to that list.

Then open a pull request.

### Khmer title adornments

docutils compares an RST title's adornment length against the title's *character
count*, and Khmer titles contain many combining marks, so an adornment copied
from the English original is almost always too short
(`WARNING: Title overline too short`). Run `tools/normalize_titles.py --write`;
it grows adornments and never touches transitions or the excluded changelog.

### Commit messages

Short, English, conventional-commit style, one logical change per commit:

```
docs(interface): translate window system areas and regions to Khmer

Mirrors upstream manual/interface/window_system/{areas,regions}.rst at
blender-v5.2-release (4a3be8f). Untranslated targets are linked to the
English manual; bpy.* refs stay as :ref: for km_xref_fallback.
```

Do not force-push or `reset --hard` a branch other people are using.

---

## Scope: what is left

Check the live table in [`manual/appendix/status.rst`](manual/appendix/status.rst)
for exact per-section numbers. The planned order is:

1. **Pass 2** — `interface/controls/**`, `interface/keymap/{blender_default,industry_compatible}`, full `glossary/`
2. **Pass 3** — `editors/**` (3D Viewport, navigation, Outliner, Properties, UV/Image)
3. **Pass 4** — `modeling/**` (mesh, curves, modifiers, Geometry Nodes)
4. **Pass 5** — `render/**`, `scene_layout/**` (materials, shaders, textures, lighting, cameras)
5. **Pass 6** — `animation/**`, `sculpt_paint/**`
6. **Pass 7** — `files/**` (import/export, data-blocks), `compositing/**`, `physics/**`,
   `video_editing/**`, `grease_pencil/**`, `movie_clip/**`, `addons/**`, `advanced/**`, `troubleshooting/**`

Small pull requests (1–5 files) are much easier to review than large ones.

---

## Known limitations

- **Search.** Sphinx has no Khmer search splitter. `html_search_language = "en"`
  keeps the build warning-free; space-delimited Khmer phrases are indexed as
  whole tokens, so sub-word search inside an unspaced Khmer run does not work.
- **Theme-toggle accessibility strings.** A few `aria-label` values
  ("Toggle Light / Dark / Auto color theme", "Toggle site navigation sidebar")
  are hard-coded English literals in furo's Jinja templates and are not
  reachable through gettext. Translating them would mean vendoring furo's
  `base.html`, which is fragile across theme upgrades, so they are left alone.
  All *visible* chrome is translated via `locale/km/LC_MESSAGES/sphinx.po`.
- **Sphinx version.** Upstream pins `sphinx==9.1.0`, which requires Python ≥ 3.12.
  This repository pins `sphinx==9.0.4` so local development on Python 3.11 and the
  Read the Docs build (Python 3.12) produce identical output.

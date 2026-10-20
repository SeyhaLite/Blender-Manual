# Blender Manual — ភាសាខ្មែរ (Khmer)

ការបកប្រែជាភាសាខ្មែរនៃ [Blender Manual](https://docs.blender.org/manual/en/latest/) ផ្លូវការ
សម្រាប់ **Blender 5.2 LTS**។

Khmer (ភាសាខ្មែរ) translation of the official Blender Manual, pinned to **Blender 5.2 LTS** —
the version served at `docs.blender.org/manual/en/latest/`.

---

## ⚠️ ស្ថានភាព / Status

**ការបកប្រែនេះមិនទាន់ពេញលេញទេ។**
This is a **partial** translation — it is *not* a complete Khmer Blender Manual.

| ផ្នែក / Section | ស្ថានភាព |
|---|---|
| `getting_started/**` (អំពី, ដំឡើង, កំណត់, ជំនួយ) | ✅ បកប្រែរួច — 15/16 ឯកសារ |
| `interface/window_system/**` (បង្អួច, តំបន់, តំបន់រង, ផ្ទាំង, របារ) | ✅ បកប្រែរួច — 9/9 ឯកសារ |
| `interface/` ផ្នែកខ្លះ (selecting, undo_redo, tool_system, operators, annotate_tool, keymap) | ✅ បកប្រែរួច — 7 ឯកសារ |
| `glossary/` (វចនានុក្រម) | ⚠️ ផ្នែកខ្លះ — ពាក្យស្នូលប៉ុណ្ណោះ |
| `interface/controls/**`, `editors/**`, `modeling/**`, `render/**`, `animation/**`, `sculpt_paint/**`, `files/**`, ផ្សេងៗទៀត | ❌ មិនទាន់បកប្រែ |

**ការគ្របដណ្ដប់សរុប / Overall upstream coverage: 35 / 2358 `.rst` files (1.48%)**

លេខទាំងនេះត្រូវបានគណនាដោយស្គ្រីប មិនមែនការប៉ាន់ស្មានទេ — សូមមើល
[`manual/appendix/status.rst`](manual/appendix/status.rst) និងដំណើរការ
`python3 tools/check_translation.py --report`។

ផ្នែកដែលមិនទាន់បានបកប្រែ ភ្ជាប់ទៅកាន់សៀវភៅណែនាំភាសាអង់គ្លេសផ្លូវការ
ហើយត្រូវបានសម្គាល់ដោយស្លាក <kbd>EN</kbd> នៅលើគេហទំព័រ។

---

## ប្រភព និងអាជ្ញាបណ្ណ / Provenance & License

| | |
|---|---|
| ប្រភពផ្លូវការ | [`blender/blender-manual`](https://projects.blender.org/blender/blender-manual) |
| សាខា / Branch | `blender-v5.2-release` |
| Commit | `4a3be8f9ed3b66b24913e0a0d491d3429a70ea08` |
| អាជ្ញាបណ្ណខ្លឹមសារ | [CC-BY-SA 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/) |
| អាជ្ញាបណ្ណកូដ | `GPL-2.0-or-later` |
| អ្នកនិពន្ធដើម | Blender Documentation Team |

កំណែបកប្រែនេះគឺជា **Adapted Material** ក្រោម CC-BY-SA 4.0 ហើយត្រូវបានចេញផ្សាយក្រោម
អាជ្ញាបណ្ណដូចគ្នា (ShareAlike)។ សូមមើល [`LICENSE`](LICENSE) និង
[`manual/copyright.rst`](manual/copyright.rst)។

ឯកសារ `getting_started/about/history.rst` (ប្រវត្តិកំណែ) **មិនត្រូវបានបកប្រែ និងមិនត្រូវបានរួមបញ្ចូល**
តាមគោលការណ៍គម្រោង — វាជាឯកសារកំណត់ត្រាការផ្លាស់ប្ដូរ (changelog)។

---

## ការដំណើរការជាមូលដ្ឋាន / Quick start

ត្រូវការ Python **3.11+**។

```sh
git clone https://github.com/SeyhaLite/Blender-Manual.git
cd Blender-Manual
make setup        # បង្កើត .venv និងដំឡើង requirements.txt
make html         # build ទៅ build/html  — បរាជ័យបើមាន warning ណាមួយ
```

Windows:

```bat
python -m venv .venv
.venv\Scripts\pip install -r requirements.txt
make.bat html
```

បើក `build/html/index.html`។

---

## មុខងារគេហទំព័រ / Site features

- **Light / Dark / Auto mode** — ប្ដូរបានតាមរយៈប៊ូតុងរបស់ furo នៅជ្រុងខាងលើស្ដាំ
  (គ្មាន JavaScript ផ្ទាល់ខ្លួន គ្មាន theme ផ្ទាល់ខ្លួន)។
- **Theme**: [furo](https://github.com/pradyunsg/furo) — theme ផ្លូវការដែល Blender Manual ប្រើ។
- **Sidebar navigation, search, on-page table of contents, responsive layout, copy-button លើ code block**។
- **ពុម្ពអក្សរខ្មែរ self-hosted**: Noto Sans Khmer (SIL OFL 1.1) — គ្មានការហៅទៅ Google Fonts
  ដូច្នេះគេហទំព័រដំណើរការបានទាំង offline។
- **Typography ខ្មែរ**: `line-height 1.85` ដើម្បីកុំឱ្យជើងអក្សរត្រូវកាត់, `lang="km"`,
  និងការបំបែកបន្ទាត់ត្រឹមត្រូវ។
- **ចំណុចប្រទាក់ Sphinx/furo ជាខ្មែរ**: admonition, ប៊ូតុង Next/Previous, ប្រអប់ស្វែងរក,
  theme toggle — តាមរយៈ [`locale/km/LC_MESSAGES/sphinx.po`](locale/km/LC_MESSAGES/sphinx.po)។

### កម្រិតគាំទ្រការស្វែងរក / Search limitation

Sphinx មិនមានភាសាស្វែងរកសម្រាប់ខ្មែរទេ។ `html_search_language` ត្រូវបានកំណត់ជា `"en"`
ដើម្បីកុំឱ្យមាន warning ពេល build។ លទ្ធផលគឺ៖ ពាក្យខ្មែរត្រូវបាន index ជា token ទាំងមូល
(បំបែកដោយដកឃ្លា) ដូច្នេះការស្វែងរកឃ្លាពេញលេញដំណើរការ ប៉ុន្តែការស្វែងរកពាក្យផ្នែក
ខាងក្នុងឃ្លាខ្មែរដែលគ្មានដកឃ្លា **មិនដំណើរការទេ**។

---

## រចនាសម្ព័ន្ធ / Layout

ផ្លូវឯកសារត្រូវនឹង upstream ១:១ ដើម្បីឱ្យការ sync និងលំហូរការងារ `.po` នាពេលអនាគតងាយស្រួល។

```
.readthedocs.yaml       # Read the Docs build config (fail_on_warning: true)
requirements.txt        # pinned dependencies
Makefile / make.bat     # build targets
LICENSE                 # CC-BY-SA 4.0 (ដូច upstream)
build_files/
├── extensions/         # reference.py, icons.py (vendored ពី upstream)
│                       # km_xref_fallback.py (របស់យើង)
└── theme/              # logo, favicon, CSS, ពុម្ពអក្សរខ្មែរ + bl-icons
locale/km/LC_MESSAGES/  # sphinx.po — Khmer UI strings
manual/                 # ← Sphinx source directory
├── conf.py
├── index.rst, copyright.rst
├── _data/upstream_labels.json   # label → docname map (generated)
├── appendix/           # contributing guide + translation status (របស់យើង)
├── getting_started/
├── glossary/
├── interface/
└── images/
tools/                  # quality + maintenance scripts
```

---

## របៀបដែលតំណភ្ជាប់ត្រូវបានដោះស្រាយ / How cross-references resolve

នេះជាបញ្ហាស្នូលនៃការបកប្រែដោយផ្នែក។ Upstream ប្រើ ``:doc:`` និង ``:ref:`` យ៉ាងច្រើន
រួមទាំង target `bpy.*` ចំនួន **4722** ដែលកំណត់នៅលើទំព័រដែលមិនទាន់បានបកប្រែ។

1. **គោលដៅស្ថិតក្នុងធានីបកប្រែ** → ដោះស្រាយធម្មតា (តំណខាងក្នុង)។
2. **``:ref:`bpy.ops.*``` / ``:ref:`bpy.types.*```** → ដោះស្រាយដោយ extension
   [`km_xref_fallback`](build_files/extensions/km_xref_fallback.py) ដែលអាន
   `manual/_data/upstream_labels.json` ហើយបង្កើតតំណទៅទំព័រភាសាអង់គ្លេសត្រឹមត្រូវ។
   **នៅពេលទំព័រមួយត្រូវបានបកប្រែ label ក្នុងស្រុករបស់វាមានអាទិភាពដោយស្វ័យប្រវត្តិ** —
   មិនចាំបាច់កែឯកសារដែលបានបកប្រែរួចទេ។
3. **``:doc:``/``:ref:`` ផ្សេងទៀតទៅទំព័រមិនទាន់បកប្រែ** → សរសេរជាតំណខាងក្រៅ
   ដោយផ្ទាល់ក្នុងឯកសារបកប្រែ (ចង្អុលទៅកំណែ `5.2` ជាក់លាក់ មិនមែន `latest`)។

តំណ fallback ទាំងអស់ទទួលបាន CSS class `km-fallback-en` ដែលបង្ហាញស្លាក
<kbd>EN</kbd> តូចមួយ។

---

## ពាក្យបញ្ជា / Commands

| ពាក្យបញ្ជា | ការពិពណ៌នា |
|---|---|
| `make setup` | បង្កើត `.venv` និងដំឡើង dependencies |
| `make html` | Build HTML ជាមួយ `-W --keep-going` (**warning = បរាជ័យ**) |
| `make html-quick` | Build ដោយមិនចាត់ទុក warning ជាកំហុស |
| `make livehtml` | Auto-rebuild នៅ `http://127.0.0.1:8000` |
| `make linkcheck` | ពិនិត្យតំណខាងក្រៅ |
| `make check` | ដំណើរការ `tools/check_translation.py` |
| `make anchors` | កែ `#fragment` នៃតំណទៅសៀវភៅណែនាំអង់គ្លេស |
| `make preview` | បង្កើតឯកសារ HTML offline តែមួយ (inline CSS/font/JS ទាំងអស់) |
| `make gettext` / `make update_po` | លំហូរការងារ gettext/`.po` សម្រាប់អនាគត |
| `make clean` | លុប `build/` |

### ការថែទាំ / Maintenance

```sh
# ធ្វើឱ្យ label map ទាន់សម័យ (ត្រូវការ upstream checkout)
python3 tools/update_upstream_labels.py --upstream ../upstream/manual --commit <sha>

# ពិនិត្យគុណភាព + ធ្វើឱ្យតារាងវឌ្ឍនភាពទាន់សម័យ
python3 tools/check_translation.py --report --upstream ../upstream/manual

# កែប្រវែងចំណងជើង RST (អក្សរខ្មែរវែងជាងអង់គ្លេស)
python3 tools/normalize_titles.py --write
```

`tools/fix_external_anchors.py` កែ `#fragment` នៃតំណភាសាអង់គ្លេសដោយស្វ័យប្រវត្តិ
ព្រោះ docutils បំលែង `_` → `-` ហើយដកលេខនៅដើម (ឧ. `app_templates` → `#app-templates`,
`3dview-fly-walk` → `#dview-fly-walk`)។

`tools/check_translation.py` ពិនិត្យ៖ គ្របដណ្ដប់អក្សរខ្មែរ, ឯកសារ changelog ដែលត្រូវបានដកចេញ,
ភាពត្រឹមត្រូវនៃ toctree, រចនាសម្ព័ន្ធ (`:kbd:`, `:menuselection:`, code block, figure, admonition,
រូបភាព) ធៀបនឹង upstream, អក្សរខុសប្រភេទ (ថៃ/CJK/…) ដែលលេចចូល, UTF-8, និង **ការលេចធ្លាយ credential**។

---

## ការចូលរួមចំណែក / Contributing

សូមអាន **[CONTRIBUTING.md](CONTRIBUTING.md)** (ជាភាសាអង់គ្លេស) និង
**[ការណែនាំសម្រាប់អ្នកចូលរួម](https://github.com/SeyhaLite/Blender-Manual/blob/main/manual/appendix/contributing.rst)**
(ជាភាសាខ្មែរ) សម្រាប់គោលការណ៍បកប្រែ តារាងពាក្យបច្ចេកទេស និងលំហូរការងារ។

---

## ការដាក់ពង្រាយ / Deployment

គេហទំព័រត្រូវបានកំណត់រចនាសម្ព័ន្ធសម្រាប់ [Read the Docs](https://app.readthedocs.org/)
តាមរយៈ [`.readthedocs.yaml`](.readthedocs.yaml):

```yaml
build:
  os: ubuntu-24.04
  tools:
    python: "3.12"
sphinx:
  configuration: manual/conf.py
  fail_on_warning: true     # quality gate
```

**ដើម្បីបញ្ចប់ការដាក់ពង្រាយ** អ្នកត្រូវ៖

1. ចូលទៅ https://app.readthedocs.org/ → *Import Project*
2. ជ្រើសរើស `SeyhaLite/Blender-Manual`
3. កំណត់ *Default branch* = `main`, *Configuration file* = `.readthedocs.yaml`
4. Trigger build ដំបូង

`html_baseurl` អានពី `READTHEDOCS_CANONICAL_URL` ដែល Read the Docs បញ្ចូលដោយស្វ័យប្រវត្តិ
ដូច្នេះមិនចាំបាច់កែអ្វីទេ។

---

## គោលការណ៍សំខាន់ៗ / Ground rules

គម្រោងនេះអនុវត្តតាមច្បាប់ខាងក្រោម (មើល `CONTRIBUTING.md` សម្រាប់ព័ត៌មានលម្អិត)៖

1. បកប្រែតែខ្លឹមសារបង្រៀន — **មិនបកប្រែ changelog / release notes**។
2. រក្សាឈ្មោះ API, Python identifier, operator, property, ឈ្មោះម៉ឺនុយ, ផ្លូវកាត់គ្រាប់ចុច
   ផ្នែកបន្ថែមឯកសារ និងឧទាហរណ៍កូដ **ដូចដើម**។
3. មិនបង្កើតមុខងារ ប៊ូតុង ឬជំហានដែលមិនមានក្នុង Blender ពិតប្រាកដ។
4. មិនលុបការព្រមាន សុវត្ថិភាព ចំណាំ ឧទាហរណ៍ ឬតំណភ្ជាប់។
5. រក្សាអាជ្ញាបណ្ណ និងការបញ្ជាក់ប្រភព។
6. មិនដាក់ credential ណាមួយក្នុង source, commit message ឬ Git history។

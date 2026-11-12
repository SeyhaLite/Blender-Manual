# Blender Manual — ភាសាខ្មែរ

ការបកប្រែជាភាសាខ្មែរនៃ [Blender Manual ផ្លូវការ](https://docs.blender.org/manual/en/5.2/) សម្រាប់ **Blender 5.2 LTS**។

This repository contains a **partial Khmer translation** of the official Blender Manual. It follows the upstream <code>blender-v5.2-release</code> branch and is not a complete translation.

> **ស្ថានភាព៖ កំពុងបកប្រែ។** ផ្នែកខ្លះនៃសៀវភៅណែនាំបានបកប្រែរួចហើយ។ ផ្នែកដែលមិនទាន់បកប្រែ ត្រូវបានភ្ជាប់ទៅសៀវភៅណែនាំភាសាអង់គ្លេសផ្លូវការ។

## មាតិកា

- [ស្ថានភាពការបកប្រែ](#ស្ថានភាពការបកប្រែ)
- [មុខងារសំខាន់ៗ](#មុខងារសំខាន់ៗ)
- [ប្រភព និងអាជ្ញាបណ្ណ](#ប្រភព-និងអាជ្ញាបណ្ណ)
- [ដំឡើង និង Build](#ដំឡើង-និង-build)
- [ពាក្យបញ្ជា](#ពាក្យបញ្ជា)
- [រចនាសម្ព័ន្ធ Repository](#រចនាសម្ព័ន្ធ-repository)
- [ការដោះស្រាយតំណយោង](#ការដោះស្រាយតំណយោង)
- [ការថែទាំ](#ការថែទាំ)
- [ការចូលរួមចំណែក](#ការចូលរួមចំណែក)
- [ការដាក់ពង្រាយ](#ការដាក់ពង្រាយ)
- [គោលការណ៍គម្រោង](#គោលការណ៍គម្រោង)

---

## ស្ថានភាពការបកប្រែ

**ការបកប្រែនេះមិនទាន់ពេញលេញទេ។** តារាងខាងក្រោមបង្ហាញចំនួនឯកសារ <code>.rst</code> ដែលមានក្នុង Repository ប្រៀបធៀបនឹងឯកសារសរុបនៅក្នុង Upstream៖

| ផ្នែក | ឯកសារមាន / សរុប | វឌ្ឍនភាព |
|---|---:|---:|
| <code>getting_started/</code> | 15 / 16 | 93.8% |
| <code>interface/</code> (រួមទាំង <code>window_system/</code>) | 17 / 58 | 29.3% |
| <code>glossary/</code> | 1 / 1 | មានឯកសារ ប៉ុន្តែមានតែពាក្យស្នូលប៉ុណ្ណោះ |
| ឯកសារកម្រិតដើម (<code>root</code>) | 2 / 3 | 66.7% |
| **សរុប** | **35 / 2,358** | **1.48%** |

**ចំណាំអំពីចំនួន៖** វាស់ចំនួនឯកសារ <code>.rst</code> ដែលមានក្នុង Repository ប៉ុណ្ណោះ។ វាមិនមែនជាការវាយតម្លៃថាអត្ថបទក្នុងឯកសារនីមួយៗបានបកប្រែពេញលេញ ឬមានគុណភាពល្អឥតខ្ចោះទេ។ សម្រាប់វឌ្ឍនភាពលម្អិតតាមផ្នែក សូមមើល [<code>manual/appendix/status.rst</code>](manual/appendix/status.rst)។ លេខទាំងនេះត្រូវបានបង្កើតដោយស្គ្រីប៖

~~~sh
python3 tools/check_translation.py --report --upstream ../upstream/manual
~~~

ផ្នែកដែលមិនទាន់បានបកប្រែ ត្រូវបានភ្ជាប់ទៅ [សៀវភៅណែនាំ Blender ជាភាសាអង់គ្លេស](https://docs.blender.org/manual/en/5.2/) និងសម្គាល់ដោយស្លាក <kbd>EN</kbd> នៅលើគេហទំព័រ។

## មុខងារសំខាន់ៗ

- **របៀបបង្ហាញ Light / Dark / Auto** តាមមុខងាររបស់ Furo។
- **ការរុករក និងស្វែងរក**៖ Sidebar navigation, search, Table of Contents និង layout ដែលសម្របតាមទំហំអេក្រង់។
- **ពុម្ពអក្សរខ្មែរ**៖ Noto Sans Khmer ដែលផ្ទុកនៅក្នុង Repository ដើម្បីកាត់បន្ថយការពឹងផ្អែកលើសេវាពុម្ពអក្សរខាងក្រៅ។
- **ការបង្ហាញអក្សរខ្មែរ**៖ កំណត់ line-height និងរបៀបបំបែកបន្ទាត់ ដើម្បីជួយឱ្យជើងអក្សរមិនត្រូវកាត់។
- **ចំណុចប្រទាក់ Sphinx ជាភាសាខ្មែរ** តាមរយៈ [<code>locale/km/LC_MESSAGES/sphinx.po</code>](locale/km/LC_MESSAGES/sphinx.po)។
- **តំណយោងទៅឯកសារដែលមិនទាន់បកប្រែ** អាចបញ្ជូនទៅកាន់ទំព័រភាសាអង់គ្លេសដែលត្រូវគ្នា។

### កម្រិតគាំទ្រការស្វែងរក

Sphinx មិនមានប្រព័ន្ធបំបែកពាក្យស្វែងរកជាភាសាខ្មែរដោយផ្ទាល់ទេ។ ដូច្នេះ <code>html_search_language</code> ត្រូវបានកំណត់ជា <code>en</code> ដើម្បីជៀសវាង Build Warning។

ពាក្យខ្មែរត្រូវបាន Index ជា token តាមដកឃ្លា។ ការស្វែងរកឃ្លាដែលបំបែកដោយដកឃ្លាអាចដំណើរការ ប៉ុន្តែការស្វែងរកតែផ្នែកខាងក្នុងនៃពាក្យ ឬឃ្លាខ្មែរដែលគ្មានដកឃ្លា មិនត្រូវបានគាំទ្រល្អទេ។

## ប្រភព និងអាជ្ញាបណ្ណ

| ព័ត៌មាន | តម្លៃ |
|---|---|
| ប្រភពផ្លូវការ | [blender/blender-manual](https://projects.blender.org/blender/blender-manual) |
| សាខា Upstream | <code>blender-v5.2-release</code> |
| Commit Upstream | <code>4a3be8f9ed3b66b24913e0a0d491d3429a70ea08</code> |
| អាជ្ញាបណ្ណខ្លឹមសារ | [CC-BY-SA 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/) |
| អាជ្ញាបណ្ណកូដ | <code>GPL-2.0-or-later</code> |
| អ្នកនិពន្ធប្រភពដើម | Blender Documentation Team |

ការបកប្រែនេះជា **Adapted Material** ក្រោម CC-BY-SA 4.0 ហើយត្រូវបានចេញផ្សាយក្រោមអាជ្ញាបណ្ណដូចគ្នា (ShareAlike)។ សូមអាន [<code>LICENSE</code>](LICENSE) និង [<code>manual/copyright.rst</code>](manual/copyright.rst)។

ឯកសារ <code>getting_started/about/history.rst</code> (ប្រវត្តិកំណែ) មិនត្រូវបានបកប្រែ និងមិនត្រូវបានរួមបញ្ចូលទេ ព្រោះវាជា Changelog មិនមែនជាខ្លឹមសារបង្រៀន។

## ដំឡើង និង Build

ត្រូវការ **Python 3.11 ឬខ្ពស់ជាងនេះ**។

### Linux / macOS

~~~sh
git clone https://github.com/SeyhaLite/Blender-Manual.git
cd Blender-Manual

make setup
make html
~~~

### Windows

បើក Command Prompt នៅក្នុងថត Repository៖

~~~bat
python -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
make.bat html
~~~

បើកឯកសារ <code>build/html/index.html</code> នៅក្នុង Browser ដើម្បីមើលលទ្ធផល។

**ចំណាំ៖** <code>make html</code> និង <code>make.bat html</code> ប្រើ <code>-W --keep-going</code>។ មានន័យថា Sphinx Warning ណាមួយនឹងធ្វើឱ្យ Build បរាជ័យ។ សម្រាប់ការសាកល្បងពេលកំពុងសរសេរ អាចប្រើ <code>make html-quick</code> ឬ <code>make.bat html-quick</code> ប៉ុន្តែមុនពេលបញ្ជូនការកែប្រែ ត្រូវដោះស្រាយ Warning ទាំងអស់។

## ពាក្យបញ្ជា

| ពាក្យបញ្ជា | មុខងារ |
|---|---|
| <code>make help</code> | បង្ហាញបញ្ជីពាក្យបញ្ជា |
| <code>make setup</code> | បង្កើត <code>.venv</code> និងដំឡើង Dependencies |
| <code>make html</code> | Build HTML ទៅ <code>build/html</code> ដោយចាត់ទុក Warning ជាកំហុស |
| <code>make html-quick</code> | Build HTML ដោយមិនចាត់ទុក Warning ជាកំហុស |
| <code>make livehtml</code> | បើក Auto-rebuild នៅ <code>http://127.0.0.1:8000</code> |
| <code>make linkcheck</code> | ពិនិត្យតំណភ្ជាប់ខាងក្រៅ; ត្រូវពិនិត្យលទ្ធផលដោយដៃ |
| <code>make check</code> | ពិនិត្យគុណភាពការបកប្រែ និងធ្វើបច្ចុប្បន្នភាពតារាងស្ថានភាព (ត្រូវការ Upstream checkout) |
| <code>make progress</code> | បង្ហាញវឌ្ឍនភាពការបកប្រែ |
| <code>make labels</code> | បង្កើតឡើងវិញនូវ Upstream label map |
| <code>make titles</code> | កែប្រវែងបន្ទាត់តុបតែងចំណងជើង RST ឱ្យសមនឹងអក្សរខ្មែរ |
| <code>make anchors</code> | កែ Fragment <code>#...</code> នៃតំណទៅសៀវភៅណែនាំអង់គ្លេស |
| <code>make preview</code> | បង្កើត HTML Offline តែមួយនៅ <code>../preview/blender-manual-km-preview.html</code> |
| <code>make gettext</code> / <code>make update_po</code> | ដំណើរការ Gettext និងធ្វើបច្ចុប្បន្នភាពឯកសារ <code>.po</code> |
| <code>make clean</code> | លុបថត <code>build/</code> |

## រចនាសម្ព័ន្ធ Repository

ផ្លូវឯកសារនៅក្នុង <code>manual/</code> ត្រូវបានរៀបចំឱ្យស្រដៀង Upstream ដើម្បីងាយស្រួល Sync និងគាំទ្រលំហូរការងារ <code>.po</code> នាពេលអនាគត។

~~~text
.readthedocs.yaml       # ការកំណត់ Build សម្រាប់ Read the Docs
requirements.txt        # កំណែ Dependencies ដែលបានកំណត់
Makefile / make.bat     # ពាក្យបញ្ជា Build និង Maintenance
LICENSE                 # CC-BY-SA 4.0
build_files/
├── extensions/         # Sphinx extensions និង Khmer cross-reference fallback
└── theme/              # Logo, favicon, CSS, ពុម្ពអក្សរខ្មែរ និង Blender icons
locale/km/LC_MESSAGES/  # sphinx.po — Khmer UI strings
manual/
├── conf.py             # Sphinx configuration
├── index.rst           # ទំព័រចាប់ផ្ដើមសៀវភៅណែនាំ
├── appendix/           # ស្ថានភាព និងការណែនាំសម្រាប់អ្នកចូលរួម
├── getting_started/    # ផ្នែកចាប់ផ្ដើមប្រើប្រាស់
├── glossary/           # វចនានុក្រមពាក្យបច្ចេកទេស
├── interface/          # ផ្នែកចំណុចប្រទាក់អ្នកប្រើ
└── images/             # រូបភាពសៀវភៅណែនាំ
tools/                  # ស្គ្រីបពិនិត្យគុណភាព និងថែទាំ
~~~

## ការដោះស្រាយតំណយោង

ដោយសារការបកប្រែមិនទាន់ពេញលេញ តំណ <code>:doc:</code> និង <code>:ref:</code> មួយចំនួននៅក្នុង Upstream ចង្អុលទៅទំព័រដែលមិនទាន់មានជាភាសាខ្មែរ។ គម្រោងប្រើ Extension <code>km_xref_fallback</code> ដើម្បីដោះស្រាយ៖

1. **គោលដៅមាននៅក្នុងឯកសារខ្មែរ**៖ ប្រើតំណខាងក្នុងធម្មតា។
2. **គោលដៅ <code>bpy.ops.*</code> និង <code>bpy.types.*</code>**៖ Extension [<code>km_xref_fallback.py</code>](build_files/extensions/km_xref_fallback.py) ប្រើ <code>manual/_data/upstream_labels.json</code> ដើម្បីបង្កើតតំណទៅទំព័រភាសាអង់គ្លេស។
3. **គោលដៅផ្សេងទៀតមិនទាន់បកប្រែ**៖ ប្រើតំណខាងក្រៅទៅកាន់សៀវភៅណែនាំភាសាអង់គ្លេសកំណែ 5.2។

តំណ Fallback ត្រូវបានកំណត់ CSS class <code>km-fallback-en</code> និងបង្ហាញស្លាក <code>EN</code> ដើម្បីឱ្យអ្នកអានដឹងថាកំពុងបើកទំព័រភាសាអង់គ្លេស។

## ការថែទាំ

ស្គ្រីបខាងក្រោមត្រូវការថត Upstream checkout នៅ <code>../upstream/manual</code> លើកលែងតែបានបញ្ជាក់ផ្លូវផ្សេង៖

~~~sh
# បង្កើត Upstream checkout ម្តង ប្រសិនបើមិនទាន់មាន
git clone --depth 1 --filter=blob:none --sparse \
  --branch blender-v5.2-release \
  https://projects.blender.org/blender/blender-manual.git ../upstream

# បង្កើត Upstream label map
python3 tools/update_upstream_labels.py \
  --upstream ../upstream/manual \
  --commit <upstream-commit-sha>

# ពិនិត្យគុណភាព និងធ្វើបច្ចុប្បន្នភាពតារាងវឌ្ឍនភាព
python3 tools/check_translation.py \
  --report --upstream ../upstream/manual

# កែប្រវែងចំណងជើង RST
python3 tools/normalize_titles.py --write

# កែ Fragment នៃតំណទៅឯកសារអង់គ្លេស
python3 tools/fix_external_anchors.py --write
~~~

<code>tools/check_translation.py</code> ពិនិត្យការគ្របដណ្ដប់អក្សរខ្មែរ ឯកសារ Changelog ដែលត្រូវដកចេញ ភាពត្រឹមត្រូវនៃ Toctree រចនាសម្ព័ន្ធសំខាន់ៗធៀបនឹង Upstream អក្សរមកពីប្រព័ន្ធអក្សរដែលមិនត្រូវការ UTF-8 និងការលេចធ្លាយ Credential។

## ការចូលរួមចំណែក

សូមអាន [<code>CONTRIBUTING.md</code>](CONTRIBUTING.md) និង [ការណែនាំសម្រាប់អ្នកចូលរួមជាភាសាខ្មែរ](manual/appendix/contributing.rst) មុនពេលកែប្រែ ឬបកប្រែឯកសារ។

គោលការណ៍ចម្បង៖

- ជ្រើសរើសឯកសារដែលមិនទាន់បកប្រែពី [តារាងស្ថានភាព](manual/appendix/status.rst)។
- រក្សាឈ្មោះ API, Python identifiers, operators, properties, menus, shortcuts និង code ដូចប្រភពដើម។
- រក្សារូបភាព ឧទាហរណ៍ ការព្រមាន ចំណាំ និងតំណយោងទាំងអស់។
- ប្រើពាក្យបច្ចេកទេសខ្មែរឱ្យស៊ីសង្វាក់គ្នាតាម [វចនានុក្រម](manual/glossary/index.rst)។
- ដំណើរការ <code>make html</code> និង <code>make check</code> មុនពេលបញ្ជូន Pull Request។

## ការដាក់ពង្រាយ

គម្រោងមានឯកសារកំណត់រចនាសម្ព័ន្ធសម្រាប់ [Read the Docs](https://app.readthedocs.org/) នៅ [<code>.readthedocs.yaml</code>](.readthedocs.yaml)៖

- Build environment: Ubuntu 24.04 និង Python 3.12។
- Sphinx configuration: <code>manual/conf.py</code>។
- Builder: HTML។
- Quality gate: <code>fail_on_warning: true</code>។
- PDF និង EPUB មិនទាន់បានកំណត់ឱ្យបង្កើតទេ (<code>formats: []</code>)។

ដើម្បីបោះពុម្ពគេហទំព័រ៖

1. ចូលទៅ [Read the Docs](https://app.readthedocs.org/)។
2. Import Repository <code>SeyhaLite/Blender-Manual</code> ប្រសិនបើមិនទាន់មាន Project។
3. កំណត់ Branch = <code>main</code> និង Configuration file = <code>.readthedocs.yaml</code>។
4. Trigger Build ហើយពិនិត្យថា Build ជោគជ័យ និងគ្មាន Warning។

តម្លៃ <code>html_baseurl</code> អានពី <code>READTHEDOCS_CANONICAL_URL</code> ដែល Read the Docs ផ្ដល់ឱ្យពេល Build។ សម្រាប់ Local Build វាប្រើ URL លំនាំដើមដែលកំណត់ក្នុង <code>manual/conf.py</code>។

## គោលការណ៍គម្រោង

1. បកប្រែខ្លឹមសារបង្រៀន មិនបកប្រែ Changelog និង Release Notes។
2. រក្សាឈ្មោះ API, Python identifier, operator, property, ឈ្មោះម៉ឺនុយ និងផ្លូវកាត់គ្រាប់ចុចដូចដើម។
3. មិនបង្កើតមុខងារ ប៊ូតុង ឬជំហានដែលមិនមានក្នុង Blender ពិតប្រាកដ។
4. មិនលុបការព្រមាន សុវត្ថិភាព ចំណាំ ឧទាហរណ៍ ឬតំណភ្ជាប់។
5. រក្សាអាជ្ញាបណ្ណ និងការបញ្ជាក់ប្រភពដើម។
6. មិនដាក់ Credential, password, API key ឬ token ក្នុង Source code, commit message ឬ Git history។

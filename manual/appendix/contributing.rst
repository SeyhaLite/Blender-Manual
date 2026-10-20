.. _appendix-contributing:

#####################################
  ការណែនាំសម្រាប់អ្នកចូលរួម
#####################################

អរគុណដែលអ្នកចង់ជួយបកប្រែសៀវភៅណែនាំ Blender ជាភាសាខ្មែរ!
ទំព័រនេះពន្យល់ពីរបៀបដំណើរការ គោលការណ៍បកប្រែ និងរបៀប build គេហទំព័រ។


ប្រភព និងអាជ្ញាបណ្ណ
===================

- ប្រភពផ្លូវការ៖ `blender-manual <https://projects.blender.org/blender/blender-manual>`__
  (សាខា ``blender-v5.2-release`` ដែលត្រូវនឹង `docs.blender.org/manual/en/latest/
  <https://docs.blender.org/manual/en/latest/>`__)
- អាជ្ញាបណ្ណខ្លឹមសារ៖ `CC-BY-SA 4.0 International <https://creativecommons.org/licenses/by-sa/4.0/>`__
- អាជ្ញាបណ្ណកូដ (extension, build script)៖ ``GPL-2.0-or-later``

ដោយសារអាជ្ញាបណ្ណជា **ShareAlike** រាល់ការបកប្រែត្រូវតែចេញផ្សាយក្រោមអាជ្ញាបណ្ណដូចគ្នា
ហើយត្រូវបញ្ជាក់ប្រភពដើម។ សូមមើល :doc:`/copyright` សម្រាប់ព័ត៌មានលម្អិត។

.. important::

   នៅពេលអ្នកចូលរួមចំណែក អ្នក **មិន** កាន់កប់សិទ្ធិអ្នកនិពន្ធដាច់មុខលើអត្ថបទរបស់អ្នកទេ។
   អ្នកដទៃអាចកែប្រែវាបាន ដើម្បីរក្សាភាពស៊ីសង្វាក់គ្នានៃសៀវភៅណែនាំ។


រចនាសម្ព័ន្ធ repository
========================

គម្រោងនេះប្រើរចនាសម្ព័ន្ធ **ដូច upstream ១:១** សម្រាប់ផ្លូវឯកសារ ដើម្បីឱ្យការ sync
និងការបំលែងទៅលំហូរការងារ ``.po`` នាពេលអនាគតអាចធ្វើបានងាយ៖

.. code-block:: text

   Blender-Manual/
   ├── .readthedocs.yaml      # ការកំណត់ build សម្រាប់ Read the Docs
   ├── requirements.txt       # ការ pin កំណែ dependency
   ├── Makefile / make.bat    # ពាក្យបញ្ជា build
   ├── LICENSE                # CC-BY-SA 4.0 (ដូច upstream)
   ├── build_files/
   │   ├── extensions/        # reference.py, icons.py (vendored ពី upstream)
   │   └── theme/             # logo, favicon, CSS, ពុម្ពអក្សរខ្មែរ
   ├── manual/                # ថតប្រភព Sphinx (source directory)
   │   ├── conf.py
   │   ├── index.rst
   │   ├── getting_started/
   │   ├── interface/
   │   ├── glossary/
   │   ├── appendix/
   │   └── images/            # រូបភាព (ដូចឈ្មោះ upstream)
   └── tools/
       └── check_translation.py


ការរៀបចំបរិស្ថាន
=================

ត្រូវការ Python 3.11 ឬខ្ពស់ជាង (សម្រាប់ ``sphinx==9.0.4``)។

.. code-block:: sh

   git clone https://github.com/SeyhaLite/Blender-Manual.git
   cd Blender-Manual
   make setup        # Windows: ដំឡើងដោយដៃ — មើលខាងក្រោម
   make html

លទ្ធផលស្ថិតនៅ ``build/html/index.html``។

លើ Windows៖

.. code-block:: bat

   python -m venv .venv
   .venv\Scripts\pip install -r requirements.txt
   make.bat html

.. note::

   ``make html`` ដំណើរការជាមួយ ``-W --keep-going`` ដែលមានន័យថា **warning ណាមួយ
   នឹងធ្វើឱ្យ build បរាជ័យ**។ នេះគឺជាគុណភាព gate របស់គម្រោង — សូមកុំបិទវា។
   បើអ្នកកំពុងសេចក្ដីព្រាង សូមប្រើ ``make html-quick``។


លំហូរការងារបកប្រែ
=================

1. ជ្រើសរើសឯកសារមួយពី :doc:`ស្ថានភាពការបកប្រែ <status>` ដែលនៅឡើយ។
2. ចាប់ផ្ដើមពីឯកសារ upstream ត្រង់ផ្លូវដូចគ្នា៖
   ``https://projects.blender.org/blender/blender-manual/src/branch/blender-v5.2-release/manual/<ផ្លូវ>``
3. បកប្រែតាមគោលការណ៍ខាងក្រោម រួចរក្សាទុកក្នុងផ្លូវដូចគ្នាក្នុង ``manual/``។
4. បើឯកសារយោងទៅកាន់ទំព័រដែលមិនទាន់បានបកប្រែ សូមបំលែងតំណទៅជាតំណខាងក្រៅ
   (មើលផ្នែក *តំណភ្ជាប់* ខាងក្រោម)។
5. ដំណើរការ ``make html`` រហូតដល់គ្មាន warning។
6. ដំណើរការ ``python3 tools/check_translation.py``។
7. ធ្វើ pull request ជាមួយ commit message ខ្លីច្បាស់។


គោលការណ៍បកប្រែ
===============

អ្វីដែលត្រូវរក្សាជាភាសាអង់គ្លេស
----------------------------------

**កុំបកប្រែ** ធាតុខាងក្រោម ព្រោះវាជាផ្នែកនៃកម្មវិធី ឬនឹងបំផ្លាញការដំណើរការ៖

- ឈ្មោះ API និង Python identifier ទាំងអស់ (``bpy.ops.mesh.primitive_cube_add``)
- ឈ្មោះ operator និង property
- ឈ្មោះម៉ឺនុយ និងផ្លូវម៉ឺនុយក្នុង ``:menuselection:`` (ឧ. ``File --> Defaults``)
  ព្រោះចំណុចប្រទាក់ Blender លំនាំដើមជាភាសាអង់គ្លេស
- ផ្លូវកាត់គ្រាប់ចុចក្នុង ``:kbd:`` (ឧ. ``Ctrl-Shift-A``, ``LMB``)
- ឈ្មោះឧបករណ៍ ផ្ទាំង និងប៊ូតុងដូចដែលបង្ហាញក្នុង UI (ឧ. :guilabel:`Add Modifier`)
- បន្សំកូដ ឧទាហរណ៍ command line និងបន្ទាត់ពាក្យបញ្ជា
- ផ្នែកបន្ថែមឯកសារ (``.blend``, ``.png``, ``.po``)
- ឈ្មោះម៉ាស៊ីន render (``Cycles``, ``EEVEE``) និងឈ្មោះផលិតផល

អ្វីដែលត្រូវបកប្រែ
--------------------

- ចំណងជើង និងអត្ថបទពន្យល់ទាំងអស់
- ចំណងជើងរូបភាព (figure caption)
- ចំណងជើង admonition (``.. note::`` → *ចំណាំ*)
- ឈ្មោះផ្នែកក្នុងតារាង និងបញ្ជី

របៀបសរសេរ
----------

1. **ប្រើពាក្យអង់គ្លេសក្នុងវង់ក្រចក** នៅការលើកឡើងដំបូង៖
   «ផ្ទាំង (Panel)» «តំបន់ (Area)»។ បន្ទាប់មកអាចប្រើតែពាក្យខ្មែរបាន។
2. **ប្រើពាក្យខ្មែរដូចគ្នា** សម្រាប់ពាក្យបច្ចេកទេសដូចគ្នា — សូមមើលតារាងពាក្យខាងក្រោម
   និង :doc:`/glossary/index`។
3. **សរសេរជាភាសាខ្មែរធម្មជាតិ** កុំបកប្រែតាមពាក្យម្ដងមួយៗ។
4. **រក្សាដកឃ្លា** រវាងពាក្យខ្មែរ និងពាក្យ/លេខអង់គ្លេស៖ «កំណែ 5.2 LTS»។
5. **រក្សារាល់ការព្រមាន សុវត្ថិភាព ចំណាំ និងឧទាហរណ៍** — កុំលុប ឬសង្ខេបវា។
6. **រក្សាប្រវែងបន្ទាត់** ប្រហែល ១២០ តួអក្សរ ដូច upstream (មិនចាំបាច់តឹងពេកទេ
   ព្រោះអក្សរខ្មែរមានទទឹងធំជាង)។


តារាងពាក្យបច្ចេកទេសស្តង់ដារ
-----------------------------

ប្រើពាក្យខ្មែរទាំងនេះជាប់លាប់។ បើត្រូវបន្ថែមពាក្យថ្មី សូមបន្ថែមទាំងក្នុងតារាងនេះ
ទាំងក្នុង :doc:`/glossary/index`។

.. list-table::
   :header-rows: 1
   :widths: 28 32 40

   * - អង់គ្លេស
     - ខ្មែរ
     - ចំណាំ
   * - add-on
     - កម្មវិធីបន្ថែម
     -
   * - animation
     - ចលនា
     -
   * - area
     - តំបន់
     - ផ្នែកនៃបង្អួច
   * - camera
     - កាមេរ៉ា
     -
   * - collection
     - ការប្រមូលផ្ដុំ
     -
   * - data-block
     - ប្លុកទិន្នន័យ
     - សរសេរដាច់ដោយសញ្ញា ``-``
   * - edge
     - ជ្រុង
     - នៃ mesh
   * - editor
     - កម្មវិធីកែសម្រួល
     -
   * - export
     - នាំចេញ
     -
   * - face
     - មុខ
     - នៃ mesh
   * - file
     - ឯកសារ
     -
   * - header
     - របារបញ្ជា
     -
   * - import
     - នាំចូល
     -
   * - interface
     - ចំណុចប្រទាក់
     -
   * - keymap
     - ផែនទីគ្រាប់ចុច
     -
   * - layer
     - ស្រទាប់
     -
   * - lighting
     - ការបំភ្លឺ
     -
   * - material
     - សម្ភារៈ
     -
   * - menu
     - ម៉ឺនុយ
     -
   * - mesh
     - mesh
     - រក្សាជាអង់គ្លេស ឬ «បណ្ដាញក្រឡា» ក្នុងបរិបទទូទៅ
   * - mode
     - របៀប
     - Object Mode = របៀបវត្ថុ
   * - modifier
     - modifier
     - រក្សាជាអង់គ្លេស — ជាឈ្មោះមុខងារជាក់លាក់
   * - node
     - ថ្នាំង
     -
   * - object
     - វត្ថុ
     -
   * - operator
     - ប្រតិបត្តិករ
     -
   * - panel
     - ផ្ទាំង
     -
   * - preferences
     - ចំណូលចិត្ត
     -
   * - property
     - លក្ខណសម្បត្តិ
     -
   * - region
     - តំបន់រង
     - ដើម្បីខុសពី area
   * - render
     - render / ការបង្កើតរូបភាព
     - រក្សា «render» ក្នុងបរិបទបច្ចេកទេស
   * - rigging
     - rigging / ការបង្កើតឆ្អឹង
     -
   * - scene
     - ឆាក
     -
   * - sculpting
     - ការឆ្លាក់
     -
   * - session
     - វគ្គ
     -
   * - settings
     - ការកំណត់
     -
   * - shader
     - shader
     - រក្សាជាអង់គ្លេស
   * - shortcut
     - ផ្លូវកាត់
     -
   * - status bar
     - របារស្ថានភាព
     -
   * - tab
     - ផ្ទាំងចុច
     - ខុសពី panel = ផ្ទាំង
   * - texture
     - វាយនភាព
     -
   * - toolbar
     - របារឧបករណ៍
     -
   * - tool
     - ឧបករណ៍
     -
   * - tooltip
     - ប្រអប់ព័ត៌មាន
     -
   * - topbar
     - របារកំពូល
     -
   * - undo / redo
     - មិនធ្វើវិញ / ធ្វើឡើងវិញ
     - រក្សា «(Undo)» ក្នុងវង់ក្រចកលើកទីមួយ
   * - UV editing
     - ការកែសម្រួល UV
     - រក្សា «UV»
   * - vertex
     - កំពូល
     -
   * - viewport
     - ផ្ទាំងមើល
     -
   * - window
     - បង្អួច
     -
   * - workspace
     - តំបន់ការងារ
     -


តំណភ្ជាប់
=========

ចំណុចសំខាន់បំផុតមួយនៃការបកប្រែដោយផ្នែក (partial translation) គឺ **កុំឱ្យមានតំណខូច**។

ឯកសារ upstream ប្រើ ``:doc:`` និង ``:ref:`` យ៉ាងច្រើន។ ដោយសារយើងបកប្រែតែមួយផ្នែក
តំណដែលចង្អុលទៅទំព័រមិនទាន់បកប្រែនឹងបង្ក warning ហើយធ្វើឱ្យ ``-W`` build បរាជ័យ។

គោលការណ៍៖

**គោលដៅស្ថិតក្នុងធានីបកប្រែ** → រក្សា role ដូចដើម

.. code-block:: rst

   សូមមើល :doc:`តំបន់ </interface/window_system/areas>`។

**គោលដៅមិនទាន់បានបកប្រែ** → បំលែងទៅជាតំណខាងក្រៅទៅកាន់សៀវភៅណែនាំអង់គ្លេស

.. code-block:: rst

   សូមមើល `Preferences <https://docs.blender.org/manual/en/5.2/editors/preferences/index.html>`__។

**តំណ ``bpy.*``** → រក្សាដូចដើម (ដោះស្រាយដោយ intersphinx ទៅ API docs)

.. code-block:: rst

   :ref:`bpy.ops.wm.save_mainfile`

**តំណ ``:ref:`` ទៅ label ខាងក្រៅ** → បំលែងទៅជាតំណខាងក្រៅដែលមាន ``#label``

.. code-block:: rst

   `Portable Installation <https://docs.blender.org/manual/en/5.2/advanced/blender_directory_layout.html#portable-installation>`__

ឯកសារ ``tools/xref_worksheet.py`` (ក្នុង branch អភិវឌ្ឍន៍) អាចបង្កើតបញ្ជីតំណទាំងនេះ
ដោយស្វ័យប្រវត្តិពីឯកសារ upstream។

.. tip::

   កុំភ្លេចថាតំណខាងក្រៅទាំងអស់គួរចង្អុលទៅកំណែ ``5.2`` ជាក់លាក់
   (មិនមែន ``latest``) ដើម្បីឱ្យខ្លឹមសារត្រូវនឹងអ្វីដែលបានបកប្រែ។


ការពិនិត្យគុណភាព
=================

មុនបើក pull request សូមដំណើរការ៖

.. code-block:: sh

   make html                                  # ត្រូវតែ exit 0 ដោយគ្មាន warning
   python3 tools/check_translation.py         # គ្របដណ្ដប់ខ្មែរ + អនាម័យឯកសារ
   make linkcheck                             # តំណខាងក្រៅ (ត្រូវការអ៊ីនធឺណិត)

ស្គ្រីប ``tools/check_translation.py`` ពិនិត្យ៖

- ថាឯកសារដែលគួរបកប្រែពិតជាមានអក្សរខ្មែរ
- ថាមិនមានសញ្ញាសម្ងាត់ (token, password, key) ក្នុងឯកសារណាមួយ
- ថា ``:kbd:``, ``:menuselection:``, ``:doc:`` និងប្លុកកូដនៅដដែលធៀបនឹង upstream
- ថាឯកសារ changelog (``about/history.rst``) មិនត្រូវបានកែប្រែ


អ្វីដែល **មិន** ត្រូវធ្វើ
============================

- កុំបកប្រែ ឬកែ ``manual/getting_started/about/history.rst`` — វាជាឯកសារកំណត់ត្រាការផ្លាស់ប្ដូរ
  (changelog) ហើយត្រូវរក្សាដូចដើម។
- កុំកែកូដប្រភពរបស់ Blender ដើម្បីបង្ខំឱ្យចំណុចប្រទាក់ប្រើភាសាខ្មែរ។
  ការបកប្រែ UI របស់ Blender គឺជាគម្រោងដាច់ដោយឡែក
  (`translate Blender's UI <https://docs.blender.org/manual/en/5.2/contribute/translate_blender.html>`__)។
- កុំបង្កើតប៊ូតុង មុខងារ ឬជំហានដែលមិនមានក្នុង Blender ពិត។
  ផ្ទៀងផ្ទាត់ជាមួយប្រភព upstream ជានិច្ច។
- កុំលុបការព្រមាន ចំណាំ ឧទាហរណ៍កូដ ឬតំណភ្ជាប់។
- កុំ commit token, password ឬ secret ណាមួយ។


Commit និង pull request
=======================

- Commit message ខ្លី ច្បាស់ និងជាភាសាអង់គ្លេស តាមទម្រង់ conventional commit៖

  .. code-block:: text

     docs(interface): translate window system areas and regions to Khmer

     Mirrors upstream manual/interface/window_system/{areas,regions}.rst
     at blender-v5.2-release. External links used for pages that are
     not translated yet.

- មួយ pull request គួរមានវិសាលភាពតូច (ឯកសារ ១–៥) ដើម្បីងាយពិនិត្យ។
- កុំ force push ឬ reset hard លើសាខាដែលអ្នកដទៃកំពុងប្រើ។

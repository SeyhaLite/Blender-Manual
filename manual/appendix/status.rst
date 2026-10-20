.. _appendix-status:

#####################################
  ស្ថានភាពការបកប្រែ
#####################################

ទំព័រនេះបង្ហាញពីវឌ្ឍនភាពពិតប្រាកដនៃការបកប្រែ។ លេខទាំងអស់ត្រូវបានគណនា
ដោយស្គ្រីប ``tools/check_translation.py`` ធៀបនឹងធានីប្រភពផ្លូវការ
(``blender-manual`` សាខា ``blender-v5.2-release``) — មិនមែនជាការប៉ាន់ស្មានទេ។

.. admonition:: សេចក្ដីសង្ខេប
   :class: warning

   **ការបកប្រែនេះមិនទាន់ពេញលេញទេ។** មានតែផ្នែក *ចាប់ផ្ដើមប្រើប្រាស់* និង
   ផ្នែកខ្លះនៃ *ចំណុចប្រទាក់អ្នកប្រើ* ប៉ុណ្ណោះដែលបានបញ្ចប់។
   សម្រាប់ផ្នែកផ្សេងទៀត សូមប្រើ
   `សៀវភៅណែនាំភាសាអង់គ្លេសផ្លូវការ <https://docs.blender.org/manual/en/5.2/index.html>`__។

.. list-table:: ព័ត៌មានសង្ខេប
   :header-rows: 0
   :widths: 35 65

   * - កំណែ Blender គោលដៅ
     - |BLENDER_VERSION_LABEL| (សាខា ``blender-v5.2-release``)
   * - ប្រភពផ្លូវការ
     - `projects.blender.org/blender/blender-manual
       <https://projects.blender.org/blender/blender-manual>`__
   * - ឯកសារបកប្រែសំខាន់ៗ (Pass 1)
     - ``getting_started/**`` និង ``interface/window_system/**`` រួមទាំង
       ``interface/index.rst``, ``selecting.rst``, ``undo_redo.rst``,
       ``tool_system.rst``, ``operators.rst``, ``tools_operators.rst``,
       ``annotate_tool.rst``, ``keymap/index.rst``
   * - ឯកសារដែលរក្សាដូចដើម
     - ``getting_started/about/history.rst`` — ជាឯកសារកំណត់ត្រាការផ្លាស់ប្ដូរ (changelog)
       ត្រូវបានរក្សាជាភាសាអង់គ្លេសដោយមិនកែប្រែ តាមគោលការណ៍គម្រោង
   * - អាជ្ញាបណ្ណ
     - CC-BY-SA 4.0 International (ដូចប្រភពដើម)


វឌ្ឍនភាពតាមផ្នែក
================

តារាងខាងក្រោមត្រូវបានបង្កើតដោយស្វ័យប្រវត្តិ។ ចំនួន «បានបកប្រែ» គឺជាចំនួនឯកសារ ``.rst``
ដែលមានវត្តមានក្នុងគម្រោងនេះ (មិនថាបានបកប្រែពេញលេញឬនៅឡើយ) ធៀបនឹងចំនួនឯកសារសរុប
ក្នុងធានី upstream។

.. BEGIN GENERATED COVERAGE (tools/check_translation.py --report)

.. list-table::
   :header-rows: 1
   :widths: 34 12 12 42

   * - ផ្នែក (Section)
     - បានបកប្រែ
     - សរុប
     - វឌ្ឍនភាព
   * - ``(root)``
     - 2
     - 3
     - [############......] 66.7%
   * - ``addons``
     - 0
     - 19
     - [..................] 0.0%
   * - ``advanced``
     - 0
     - 31
     - [..................] 0.0%
   * - ``animation``
     - 0
     - 124
     - [..................] 0.0%
   * - ``compositing``
     - 0
     - 212
     - [..................] 0.0%
   * - ``contribute``
     - 0
     - 26
     - [..................] 0.0%
   * - ``editors``
     - 0
     - 201
     - [..................] 0.0%
   * - ``files``
     - 0
     - 33
     - [..................] 0.0%
   * - ``getting_started``
     - 15
     - 16
     - [#################.] 93.8%
   * - ``glossary``
     - 1
     - 1
     - [##################] 100.0%
   * - ``grease_pencil``
     - 0
     - 118
     - [..................] 0.0%
   * - ``interface``
     - 17
     - 58
     - [#####.............] 29.3%
   * - ``modeling``
     - 0
     - 774
     - [..................] 0.0%
   * - ``movie_clip``
     - 0
     - 35
     - [..................] 0.0%
   * - ``physics``
     - 0
     - 120
     - [..................] 0.0%
   * - ``render``
     - 0
     - 303
     - [..................] 0.0%
   * - ``scene_layout``
     - 0
     - 64
     - [..................] 0.0%
   * - ``sculpt_paint``
     - 0
     - 129
     - [..................] 0.0%
   * - ``troubleshooting``
     - 0
     - 29
     - [..................] 0.0%
   * - ``video_editing``
     - 0
     - 62
     - [..................] 0.0%
   * - **សរុប**
     - **35**
     - **2358**
     - **1.5%**

.. END GENERATED COVERAGE

.. upstream-commit: 4a3be8f9ed3b

.. upstream-commit: 4a3be8f9ed3b

.. upstream-commit: 4a3be8f9ed3b

ដើម្បីធ្វើឱ្យតារាងនេះទាន់សម័យ សូមដំណើរការ (ត្រូវការ checkout នៃ upstream)៖

.. code-block:: sh

   git clone --depth 1 --filter=blob:none --sparse \
       --branch blender-v5.2-release \
       https://projects.blender.org/blender/blender-manual.git ../upstream
   cd ../upstream
   git sparse-checkout init --no-cone
   printf '%s\n' '/manual/**/*.rst' > .git/info/sparse-checkout
   git read-tree -mu HEAD
   cd -
   python3 tools/check_translation.py --report --upstream ../upstream/manual


ផែនការបន្ទាប់
==============

.. list-table::
   :header-rows: 1
   :widths: 12 40 48

   * - ដំណាក់កាល
     - ផ្នែក
     - ខ្លឹមសារ
   * - Pass 1 ✅
     - ``getting_started/**``, ``interface/window_system/**``,
       ``interface/{index,selecting,undo_redo,tool_system,operators,tools_operators,annotate_tool,keymap/index}``
     - ចាប់ផ្ដើមប្រើប្រាស់ ការដំឡើង ការកំណត់ ប្រព័ន្ធជំនួយ
       ប្រព័ន្ធបង្អួច តំបន់ និងតំបន់រង ការជ្រើសរើស Undo/Redo
       ប្រព័ន្ធឧបករណ៍ និង Operator
   * - Pass 2
     - ``interface/controls/**``, ``interface/keymap/{blender_default,industry_compatible}``,
       ``glossary/**``
     - ធាតុគ្រប់គ្រង (ប៊ូតុង ម៉ឺនុយ ផ្ទាំង តារាង) ប្រព័ន្ធ node
       តារាងផ្លូវកាត់គ្រាប់ចុចពេញលេញ និងវចនានុក្រមពេញលេញ
   * - Pass 3
     - ``editors/**``
     - 3D Viewport ការរុករក Outliner Properties Timeline UV/Image Editor
   * - Pass 4
     - ``modeling/**``
     - Mesh, Curve, Text ឧបករណ៍ម៉ូដែល Modifier និង Geometry Nodes
   * - Pass 5
     - ``render/**``, ``scene_layout/**``
     - សម្ភារៈ Shader វាយនភាព ពន្លឺ កាមេរ៉ា និងការ render
   * - Pass 6
     - ``animation/**``, ``sculpt_paint/**``
     - Animation, Rigging, Constraints, Shape Key និង Sculpting
   * - Pass 7
     - ``files/**``, ``compositing/**``, ``physics/**``,
       ``video_editing/**``, ``grease_pencil/**``, ``movie_clip/**``,
       ``addons/**``, ``advanced/**``, ``troubleshooting/**``
     - Import/Export data-block និងផ្នែកដែលនៅសល់


របៀបជួយ
========

សូមអាន :doc:`ការណែនាំសម្រាប់អ្នកចូលរួម <contributing>`។ ការចូលរួមចំណែកតូចមួយ
(ឧទាហរណ៍ បកប្រែឯកសារតែមួយ ឬកែពាក្យបច្ចេកទេសឱ្យស៊ីសង្វាក់គ្នា) ក៏មានតម្លៃដែរ។

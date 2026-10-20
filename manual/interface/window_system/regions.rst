.. _bpy.types.Region:
.. _ui-region:

###################################
  តំបន់រង (Regions)
###################################

Editor ទាំងអស់ក្នុង Blender ត្រូវបានបំបែកជាតំបន់រង (Regions)។
តំបន់រងអាចមានធាតុរចនាសម្ព័ន្ធតូចៗ ដូចជា
:doc:`ផ្ទាំងចុច និងផ្ទាំង (tabs and panels) </interface/window_system/tabs_panels>`
ដែលមានប៊ូតុង ធាតុគ្រប់គ្រង និង widget ស្ថិតនៅខាងក្នុង។

.. figure:: /images/interface_window-system_regions_3d-view.png

   តំបន់រងរបស់ 3D Viewport ដែលបង្ហាញ Sidebar និងផ្ទាំង Adjust Last Operation
   បន្ទាប់ពីបន្ថែម Cube មួយ។

   របារបញ្ជា Header (ពណ៌បៃតង) តំបន់រងចម្បង (ពណ៌លឿង) Toolbar (ពណ៌ខៀវ)
   Sidebar (ពណ៌ក្រហម) និងផ្ទាំង Adjust Last Operation (ពណ៌ផ្កាឈូក)។


.. _ui-region-window:

តំបន់រងចម្បង (Main Region)
============================

យ៉ាងហោចណាស់មានតំបន់រងមួយដែលបង្ហាញជានិច្ច។
វាត្រូវបានហៅថាតំបន់រងចម្បង (Main region) ហើយជាផ្នែកសំខាន់បំផុតរបស់ editor។

Editor នីមួយៗមានគោលបំណងជាក់លាក់ ដូច្នេះតំបន់រងចម្បង
និងភាពអាចរកបាននៃតំបន់រងបន្ថែម ខុសគ្នារវាង editor។
សូមមើលឯកសារជាក់លាក់អំពី editor នីមួយៗក្នុងជំពូក
`Editors <https://docs.blender.org/manual/en/5.2/editors/index.html>`__។


.. _bpy.types.Header:
.. _ui-region-header:

របារបញ្ជា (Header)
====================

Header គឺជាបន្ទះផ្ដេកតូចមួយ ដែលស្ថិតនៅផ្នែកខាងលើ ឬខាងក្រោមនៃតំបន់មួយ។
Editor ទាំងអស់មាន header ដែលដើរតួជាធុងផ្ទុកម៉ឺនុយ និងឧបករណ៍ដែលប្រើជាទូទៅ។
:ref:`ម៉ឺនុយ <bpy.types.UIPopupMenu>` និងប៊ូតុងនឹងផ្លាស់ប្ដូរទៅតាមប្រភេទ editor
វត្ថុដែលបានជ្រើសរើស និងរបៀប (mode)។

.. figure:: /images/editors_3dview_introduction_3d-view-header-object-mode.png

   Header របស់ 3D Viewport។


.. _bpy.ops.screen.header:

ម៉ឺនុយបរិបទ (Context Menu)
---------------------------

ចុច :kbd:`RMB` លើ header បង្ហាញម៉ឺនុយបរិបទដែលមានជម្រើសមួយចំនួន៖

Show Header
   ប្ដូរភាពមើលឃើញរបស់ header។
   ប្រសិនបើ header ត្រូវបានលាក់ វាអាចបង្ហាញឡើងវិញបានដោយចុច ឬអូស
   ព្រួញតូចដែលលេចឡើងនៅជ្រុងខាងលើ/ខាងក្រោមផ្នែកខាងស្ដាំរបស់ editor។
Show Tool Settings
   ប្ដូរភាពមើលឃើញរបស់ `ការកំណត់ឧបករណ៍ (Tool Settings)`_។
Show Menus
   ប្ដូរថាតើ :ref:`ម៉ឺនុយ <bpy.types.UIPopupMenu>` ត្រូវបានបង្រួម ឬអត់។

.. _bpy.ops.screen.region_flip:

Flip to Bottom/Top
   ប្ដូរថាតើ header ឬ Tool Settings បង្ហាញនៅផ្នែកខាងលើ ឬខាងក្រោមរបស់ editor។
Vertical/Horizontal Split
   បង្ហាញបន្ទាត់សូចនាករ ដែលអនុញ្ញាតឱ្យអ្នកជ្រើសរើសតំបន់ និងទីតាំងដែលត្រូវបំបែក។
   :kbd:`Tab` ប្ដូររវាងបញ្ឈរ/ផ្ដេក។
Maximize Area / Focus Mode
   សូមមើល :ref:`bpy.ops.screen.screen_full_area`។
Duplicate Area into New Window
   សូមមើល :ref:`bpy.ops.screen.area_dupli`។
Close Area
   បិទតំបន់នេះ ហើយជំនួសវាដោយការពង្រីកនៃតំបន់ជាប់គ្នា។


របារឧបករណ៍ (Toolbar)
======================

:ref:`Toolbar <ui-region-toolbar>` (នៅផ្នែកខាងឆ្វេងនៃតំបន់ editor)
មានសំណុំឧបករណ៍អន្តរកម្ម។ :kbd:`T` ប្ដូរភាពមើលឃើញរបស់ Toolbar។


.. _ui-region-tool-settings:

ការកំណត់ឧបករណ៍ (Tool Settings)
================================

បន្ទះផ្ដេកមួយនៅផ្នែកខាងលើ ឬខាងក្រោមរបស់ editor (ស្រដៀងនឹង header)
ដែលមានការកំណត់សម្រាប់ឧបករណ៍ដែលបានជ្រើសរើសបច្ចុប្បន្ន។ ដូចគ្នានឹង header
វាអាចត្រូវបានលាក់ និងផ្លាស់ទីតាមរយៈម៉ឺនុយបរិបទរបស់វា។


ការកែប្រតិបត្តិការចុងក្រោយ (Adjust Last Operation)
====================================================

:ref:`Adjust Last Operation <bpy.ops.screen.redo_last>` គឺជាតំបន់រងមួយដែលអនុញ្ញាតឱ្យ
កែតម្រូវ operator បន្ទាប់ពីដំណើរការវា។ ឧទាហរណ៍ ប្រសិនបើអ្នកទើបតែបន្ថែម cube មួយ
អ្នកអាចប្រើតំបន់រងនេះដើម្បីកែទំហំរបស់វា។


.. _ui-region-sidebar:

របារចំហៀង (Sidebar)
=====================

*Sidebar* (នៅផ្នែកខាងស្ដាំនៃតំបន់ editor)
មាន :ref:`ផ្ទាំង (Panels) <ui-panels>`
ដែលមានការកំណត់របស់វត្ថុខាងក្នុង editor និងរបស់ editor ខ្លួនឯង។
:kbd:`N` ប្ដូរភាពមើលឃើញរបស់ Sidebar។


.. _ui-region-footer:

របារបាត (Footer)
==================

Editor ខ្លះបង្ហាញរបារមួយ (នៅផ្នែកខាងលើ/ខាងក្រោមនៃតំបន់ editor)
ដែលបង្ហាញព័ត៌មានអំពីឧទាហរណ៍ ឧបករណ៍សកម្ម ឬ operator។

ក្នុង editor ចលនា (animation editor) របារបាតមានធាតុគ្រប់គ្រង និងជម្រើស
ដែលពាក់ព័ន្ធនឹងការចាក់ ការដាក់ keyframe, auto keyframing និងការដឹកជញ្ជូន (transport)។

ការកំណត់ទាំងនេះអនុញ្ញាតឱ្យអ្នក៖

- គ្រប់គ្រងពីរបៀបដែលចលនាត្រូវបានមើលជាមុន និងធ្វើសមកាលកម្មជាមួយសំឡេង។
- បញ្ចូល និងគ្រប់គ្រង keyframe តាមរយៈ keying set និង auto keying។
- រុករកតាមបណ្ដោយ timeline ដោយប្រើធាតុគ្រប់គ្រងការចាក់ និងការដឹកជញ្ជូន។
- កែតម្រូវជួរ frame និងមើលជាមុនផ្នែកជាក់លាក់នៃចលនា។

.. seealso::

   សម្រាប់ការពណ៌នាលម្អិតអំពីលក្ខណសម្បត្តិ និងធាតុគ្រប់គ្រងទាំងអស់
   ដែលជាទូទៅមាននៅក្នុងរបារបាត សូមមើលឯកសារ
   `Playback Controls <https://docs.blender.org/manual/en/5.2/animation/animation_editors.html#animation-editors-footer>`__។


ការរៀបចំ
========

ការរំកិល (Scrolling)
---------------------

តំបន់រងមួយអាចត្រូវបានរំកិលតាមបញ្ឈរ និង/ឬផ្ដេក ដោយអូសវាដោយ :kbd:`MMB`។
ប្រសិនបើតំបន់រងគ្មានកម្រិតពង្រីក (zoom level) វាក៏អាចរំកិលបានដោយប្រើ :kbd:`Wheel`
ខណៈពេលដែលកណ្ដុរស្ថិតនៅលើវា។

.. _interface_window-system_regions_scroll_range:

តំបន់រងខ្លះ ជាពិសេស timeline ចលនា មានរបាររំកិល (scrollbar)
ដែលមានចំណុចគ្រប់គ្រងបន្ថែម ដើម្បីកែតម្រូវជួរបញ្ឈរ ឬផ្ដេកនៃតំបន់រង។
របាររំកិលពិសេសទាំងនេះនឹងមាន widget បន្ថែមនៅចុងទាំងពីរ ដូចបានបង្ហាញក្នុងរូបភាពខាងក្រោម៖

.. figure:: /images/interface_window-system_regions_scrollbar_widget.png
   :align: center

   របាររំកិលជាមួយ widget ពង្រីក/បង្រួម។

នេះអាចប្រើដើម្បីពន្លាត ឬបង្រួមជួរ ដើម្បីបង្ហាញព័ត៌មានលម្អិតច្រើន ឬតិច
ក្នុងកន្លែងអេក្រង់ដែលមាន។ គ្រាន់តែអូសចំណុចមួយក្នុងចំណោមចំណុចទាំងនោះ
ដើម្បីបង្កើន ឬបន្ថយជួរដែលបង្ហាញ។
អ្នកក៏អាចកែតម្រូវទាំងជួរផ្ដេក និងបញ្ឈរយ៉ាងរហ័ស ដោយអូសក្នុង editor ដោយ :kbd:`Ctrl-MMB`។


.. _bpy.ops.screen.region_blend:

ការប្ដូរទំហំ និងការលាក់តំបន់រង
--------------------------------

ការប្ដូរទំហំតំបន់រងធ្វើឡើងដោយអូសព្រំដែនរបស់វា ដូចគ្នានឹង
:doc:`តំបន់ (Areas) </interface/window_system/areas>`។

ដើម្បីលាក់តំបន់រងមួយ សូមប្ដូរទំហំវាឱ្យតូចរហូតដល់អស់។
តំបន់រងដែលបានលាក់ ទុកសញ្ញាព្រួញតូចមួយ។
ចុច :kbd:`LMB` លើរូបតំណាងនេះ ដើម្បីឱ្យតំបន់រងលេចឡើងវិញ។

.. list-table:: ការលាក់ និងបង្ហាញ Sidebar។

   * - .. figure:: /images/interface_window-system_regions_sidebar-hide.png

     - .. figure:: /images/interface_window-system_regions_sidebar-show.png


.. _bpy.ops.screen.region_scale:

ការពង្រីក/បង្រួម (Scaling)
----------------------------

មាត្រដ្ឋាននៃតំបន់រងមួយចំនួន (ដូចជា Toolbar) អាចផ្លាស់ប្ដូរបានដោយអូសខាងក្នុងវា
ដោយ :kbd:`Ctrl-MMB` ឬប្រើ :kbd:`NumpadPlus` និង :kbd:`NumpadMinus`
ខណៈពេលដាក់ទ្រនិចកណ្ដុរលើវា។ ចុច :kbd:`Home` ដើម្បីកំណត់មាត្រដ្ឋានឡើងវិញទៅលំនាំដើម។


.. _ui-region-asset_shelf:

ធ្នើរទ្រព្យ (Asset Shelf)
===========================

.. figure:: /images/interface_window-system_regions_asset-shelf.png
   :align: center

   Asset Shelf របស់ 3D View ដែលបង្ហាញទ្រព្យសម្ភារៈ (material asset)។

ការស្វែងរក
-----------

ដើម្បីស្វែងរកទ្រព្យ (asset) សូមដាក់កណ្ដុររបស់អ្នកលើ Asset Shelf បន្ទាប់មកចុច Ctrl-F
ហើយវាយបញ្ចូលពាក្យស្វែងរក។ នេះនឹងត្រង pose ឱ្យត្រូវនឹងអ្វីដែលអ្នកបានវាយ។


ផ្ទាំងចុច (Tabs)
-----------------

.. figure:: /images/asset_shelf-tabs.png

   ការប្រើ catalog ជាផ្ទាំងចុច។

Catalog អាចត្រូវបានបង្ហាញជាផ្ទាំងចុចដាច់ដោយឡែក។ ផ្ទាំងចុចនីមួយៗនឹងបង្ហាញតែមាតិការបស់វា
និងមាតិការបស់កូនរបស់វា។ នេះធ្វើឱ្យវាងាយស្រួលក្នុងការត្រងទៅសំណុំទ្រព្យជាក់លាក់មួយ។


ជម្រើសបង្ហាញ
-------------

.. figure:: /images/asset_shelf-options.png

   ជម្រើសបង្ហាញដែលមានសម្រាប់ Asset Shelf។

វាអាចផ្លាស់ប្ដូរទំហំធាតុនៅលើធ្នើរ ដោយប្រើលក្ខណសម្បត្តិទំហំ (size property)។

ដោយបើកប្រអប់ធីក «Names» ឈ្មោះទ្រព្យនឹងបង្ហាញនៅលើធ្នើរ។
ជាជម្រើសផ្សេង ក៏អាចដាក់ទ្រនិចលើធាតុមួយដើម្បីបង្ហាញឈ្មោះរបស់វាបានដែរ។

តាមលំនាំដើម ធ្នើរមានកម្ពស់សម្រាប់តែជួរធាតុមួយប៉ុណ្ណោះ។
ដើម្បីអនុញ្ញាតឱ្យមានជួរច្រើន សូមអូសវានៅគែមខាងលើដើម្បីបង្កើនទំហំ។


ការត្រង (Filter)
-----------------

.. _bpy.types.PreferencesView.use_filter_brushes_by_tool:

By Active Tool
   បង្ហាញតែ brush ដែលអាចប្រើបានជាមួយឧបករណ៍សកម្មបច្ចុប្បន្ន នៅក្នុង Asset Shelf។

   .. note::

      តម្លៃនៃលក្ខណសម្បត្តិនេះត្រូវបានរក្សាទុកក្នុង
      `Preferences <https://docs.blender.org/manual/en/5.2/editors/preferences/index.html>`__
      ដែលអាចត្រូវការរក្សាទុកដោយដៃ ប្រសិនបើ *Auto-Save Preferences* ត្រូវបានបិទ។

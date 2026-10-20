.. _ui-tool_system:
.. _bpy.ops.wm.tool:

#############################################
  ប្រព័ន្ធឧបករណ៍ (Tool System)
#############################################

ឧបករណ៍ត្រូវបានចូលប្រើពី :ref:`របារឧបករណ៍ (Toolbar) <ui-region-toolbar>`។

នេះគឺជាការណែនាំទូទៅអំពីឧបករណ៍។ ឧបករណ៍នីមួយៗមានឯកសារផ្ទាល់ខ្លួនរបស់វា។

អាចមានឧបករណ៍សកម្មតែមួយប៉ុណ្ណោះក្នុងមួយ
:doc:`តំបន់ការងារ (Workspace) </interface/window_system/workspaces>` និង
`របៀប (mode) <https://docs.blender.org/manual/en/5.2/editors/3dview/modes.html>`__។
ឧបករណ៍នេះត្រូវបានចងចាំ៖ ប្រសិនបើអ្នកស្ថិតក្នុង Edit Mode ហើយបានជ្រើសរើសឧបករណ៍ Extrude
បន្ទាប់មកប្ដូរទៅ Object Mode (ដែលគ្មានឧបករណ៍ Extrude) ហើយត្រឡប់មក Edit Mode វិញ
ឧបករណ៍ Extrude នឹងនៅតែសកម្ម។

ឧបករណ៍ភាគច្រើនត្រូវបានគ្រប់គ្រងដោយប្រើតែ :kbd:`LMB` ទោះបីជាខ្លះមានគ្រាប់ចុចកែប្រែ (modifier key)
(បង្ហាញក្នុង :doc:`របារស្ថានភាព (Status Bar) </interface/window_system/status_bar>` ខណៈពេលប្រើឧបករណ៍)។
ទាំងអស់នេះអាចប្ដូរតាមបំណងបានក្នុង
`Keymap Preferences <https://docs.blender.org/manual/en/5.2/editors/preferences/keymap.html>`__។

ឧបករណ៍ខ្លះកំណត់ gizmo (ឧទាហរណ៍ *Shear* និង *Spin*) ដើម្បីជួយគ្រប់គ្រងវា។


.. _ui-region-toolbar:

របារឧបករណ៍ (Toolbar)
======================

.. reference::

   :Shortcut:  :kbd:`T`

.. figure:: /images/interface_tool-system_buttons-popup.png
   :align: right

   ក្រុមឧបករណ៍ដែលបានពង្រីក។

Toolbar មានប៊ូតុងសម្រាប់ឧបករណ៍ផ្សេងៗ។
ប៊ូតុងដែលមានត្រីកោណតូចនៅជ្រុងខាងក្រោមផ្នែកខាងស្ដាំ គឺជាក្រុមឧបករណ៍
ដែលអាចបើកបានដោយសង្កត់ :kbd:`LMB` លើវាមួយភ្លែត
(ឬអូស :kbd:`LMB` ដើម្បីបើកវាភ្លាមៗ)។

ការដាក់ទ្រនិចលើឧបករណ៍មួយក្នុងរយៈពេលខ្លី នឹងបង្ហាញឈ្មោះរបស់វា
ខណៈដែលការដាក់ទ្រនិចយូរជាងនឹងបង្ហាញប្រអប់ព័ត៌មានពេញលេញ។

ការប្ដូរទំហំ Toolbar តាមផ្ដេក នឹងបង្ហាញរូបតំណាងជាពីរជួរ។
ការពង្រីកវាបន្ថែមទៀត នឹងបង្ហាញរូបតំណាង និងអត្ថបទរបស់វា។


.. _bpy.ops.wm.toolbar:

Toolbar លោត (Pop-Up Toolbar)
=============================

.. reference::

   :Shortcut:  :kbd:`Shift-Spacebar`

ការចុច :kbd:`Shift-Spacebar` នឹងធ្វើឱ្យ toolbar តូចមួយលោតឡើងត្រង់ទ្រនិចរបស់អ្នក
ដើម្បីចូលប្រើបានរហ័ស។ ផ្លូវកាត់សម្រាប់ជ្រើសរើសឧបករណ៍ត្រូវបានបង្ហាញនៅផ្នែកខាងស្ដាំ។

ជាជម្រើស អ្នកអាចផ្គូផ្គងសកម្មភាពនេះទៅ :kbd:`Spacebar` ក្នុង Keymap Preferences។
បន្ទាប់មកអ្នកនឹងអាចប្រើ :kbd:`Spacebar` ដូចជាគ្រាប់ចុចកែប្រែ
(ស្រដៀងនឹងការសង្កត់ :kbd:`Ctrl` ឬ :kbd:`Shift`)។
ឧទាហរណ៍ អ្នកអាចចុច :kbd:`Spacebar T` សម្រាប់ Transform,
:kbd:`Spacebar D` សម្រាប់ Annotate, :kbd:`Spacebar M` សម្រាប់ Measure ជាដើម។
សូមមើល `Spacebar Action
<https://docs.blender.org/manual/en/5.2/editors/preferences/keymap.html#keymap-blender-default-spacebar-action>`__។


ជំនួយចិត្តរហ័ស (Quick Favorites)
==================================

.. reference::

   :Shortcut:  :kbd:`Q`

ម៉ឺនុយ Quick Favorites ប្រមូលឧបករណ៍ដែលអ្នកពេញចិត្ត។
ឧបករណ៍ ឬធាតុម៉ឺនុយណាមួយអាចត្រូវបានបន្ថែមទៅម៉ឺនុយលោតនេះ តាមរយៈម៉ឺនុយបរិបទរបស់វា។


ការប្ដូរឧបករណ៍
===============

ប្រសិនបើអ្នកបានបើក *Alt Click Tool Prompt* ក្នុង Keymap Preferences
ការចុច :kbd:`Alt` ខ្លីៗនឹងបង្ហាញការណែនាំឧបករណ៍ក្នុងរបារស្ថានភាព។
បន្ទាប់មកអ្នកអាចចុចគ្រាប់ចុចមួយដើម្បីជ្រើសរើសឧបករណ៍ដែលត្រូវគ្នា
ឬចុច :kbd:`Alt` ម្ដងទៀតដើម្បីបោះបង់ការណែនាំ។


.. _bpy.ops.wm.toolbar_fallback_pie:

ឧបករណ៍បម្រុង (Fallback Tool)
-------------------------------

ឧបករណ៍បម្រុងគឺជាឧបករណ៍ដែលត្រូវបានជ្រើសរើសតាមលំនាំដើម
(ដូច្នេះគឺជាឧបករណ៍នៅផ្នែកខាងលើនៃ Toolbar)។
អ្នកអាចផ្លាស់ប្ដូរវាដោយសង្កត់ :kbd:`LMB` លើប៊ូតុង toolbar ឬចុច :kbd:`Alt-W`
ដើម្បីទទួលបានម៉ឺនុយរង្វង់ (pie menu)។


ការជុំវិញឧបករណ៍ (Cycling Tools)
--------------------------------

ប្រសិនបើអ្នកភ្ជាប់គ្រាប់ចុចមួយទៅឧបករណ៍ដែលជាផ្នែកនៃក្រុមមួយ
អ្នកអាចបើកជម្រើស *Cycle* ក្នុងកម្មវិធីកែ keymap។
ការចុចជាបន្តបន្ទាប់នឹងជុំវិញឧបករណ៍ក្នុងក្រុមនោះ។

នេះត្រូវបានបើកតាមលំនាំដើមសម្រាប់ឧបករណ៍ជ្រើសរើសក្នុង 3D Viewport ឧទាហរណ៍៖
ការចុច :kbd:`W` នឹងជុំវិញរវាង Select Box, Select Circle ជាដើម។


លក្ខណសម្បត្តិ
=============

ឧបករណ៍អាចមានការកំណត់ផ្ទាល់ខ្លួន ដែលអាចរកបានពីកន្លែងជាច្រើន៖

- ផ្ទាំង :menuselection:`Tool --> Active Tool` ក្នុង Sidebar :kbd:`N`។
- ផ្ទាំងចុច *Active Tool* ក្នុង
  `Properties editor <https://docs.blender.org/manual/en/5.2/editors/properties_editor.html>`__។
- តំបន់រង *Tool Settings* នៅខាងក្រោមបញ្ជីតំបន់ (area header)។

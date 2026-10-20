#############################################
  ប្រតិបត្តិករ (Operators)
#############################################

ប្រតិបត្តិករ (Operator) ដំណើរការសកម្មភាពមួយភ្លាមៗនៅពេលដែលវាត្រូវបានបើក
ដែលធ្វើឱ្យវាខុសពីឧបករណ៍ (tool) ដែលត្រូវការការបញ្ចូលមួយចំនួន។
Operator អាចត្រូវបានចាប់ផ្ដើមពី
`ប៊ូតុង operator <https://docs.blender.org/manual/en/5.2/interface/controls/buttons/buttons.html#ui-operator-buttons>`__,
:ref:`bpy.types.UIPopupMenu` ឬ :ref:`bpy.ops.wm.search_menu`។
ឧទាហរណ៍នៃ operator រួមមាន ការបន្ថែមវត្ថុថ្មី ការលុបវា
ឬការកំណត់ការលាបពណ៌ (shading) របស់វាទៅជា smooth។


លក្ខណសម្បត្តិរបស់ Operator
===========================

Operator ភាគច្រើនមានលក្ខណសម្បត្តិ (property) ដែលអាចកែតម្រូវបាន ដើម្បីធ្វើឱ្យលទ្ធផលល្អិតល្អន់។
ដំបូងដំណើរការ operator (ដែលនឹងប្រើការកំណត់លំនាំដើមរបស់វា)
បន្ទាប់មកកែតម្រូវលក្ខណសម្បត្តិក្នុងតំបន់រង :ref:`bpy.ops.screen.redo_last`។


Operator បែប Modal
===================

Operator បែប modal មាននៅចន្លោះគោលគំនិតនៃ :doc:`ឧបករណ៍ (Tools) </interface/tool_system>`
និង operator ធម្មតា។ វាត្រូវការការបញ្ចូលអន្តរកម្មមួយចំនួន។

.. list-table::
   :align: left
   :width: 95%
   :widths: 20 80

   * - :kbd:`Esc`, :kbd:`RMB`
     - បោះបង់ operator បែប modal។
   * - :kbd:`Return`, :kbd:`LMB`
     - បញ្ជាក់សកម្មភាពរបស់ operator បែប modal។


Operator បែប Slider
--------------------

Operator បែប slider ត្រូវបានប្រើដើម្បីកែតម្រូវតម្លៃភាគរយដោយអន្តរកម្ម
នៅក្នុង :ref:`របារបញ្ជា (header) <ui-region-header>` របស់ editor។

អ្នកអាចកែតម្រូវភាគរយដោយអូស slider ទៅឆ្វេង ឬស្ដាំ។
នេះអាចធ្វើឱ្យគ្រើមជាង (ខ្ទាស់ជាចំនួនកើន ១០%) ដោយសង្កត់ :kbd:`Ctrl`
ហើយធ្វើឱ្យល្អិតជាងដោយសង្កត់ :kbd:`Shift`។
សម្រាប់ slider មួយចំនួន អ្នកអាចប្ដូរ «overshoot» ដោយ :kbd:`E` ដែលអនុញ្ញាតឱ្យអ្នក
ទៅហួសពីជួរ ០–១០០%។


ការស្វែងរក Operator
====================

.. _bpy.ops.wm.search_menu:

Menu Search
-----------

.. reference::

   :Mode:      គ្រប់របៀបទាំងអស់
   :Menu:      :menuselection:`Edit --> Menu Search`
   :Shortcut:  :kbd:`F3`

ផ្ទាំងលោត Menu Search អនុញ្ញាតឱ្យអ្នកស្វែងរក
:doc:`operator </interface/operators>` ជាក់លាក់មួយក្នុងចំណុចប្រទាក់ Blender ហើយដំណើរការវា។
ដំបូងបង្រួមបញ្ជីដោយវាយ (ផ្នែកខ្លះនៃ) ឈ្មោះរបស់ operator
បន្ទាប់មកអាចចុច operator ដោយ :kbd:`LMB` ឬរុករកទៅវាដោយ :kbd:`Down` និង :kbd:`Up`
ហើយបើកវាដោយ :kbd:`Return`។

ក្រៅពីឈ្មោះ operator ផ្ទាំងលោតក៏បង្ហាញម៉ឺនុយដែលវាស្ថិតនៅផងដែរ។

.. figure:: /images/interface_controls_templates_operator-search_pop-up.png
   :align: center

   ផ្ទាំងលោត Menu Search។

.. seealso::

   ជម្រើស `Spacebar Action
   <https://docs.blender.org/manual/en/5.2/editors/preferences/keymap.html#keymap-blender-default-spacebar-action>`__
   ក្នុង Preferences។


.. _bpy.ops.wm.search_operator:

Operator Search
---------------

.. reference::

   :Mode:      គ្រប់របៀបទាំងអស់
   :Menu:      :menuselection:`Edit --> Operator Search`

នៅពេលដែល :ref:`Developer Extras <bpy.types.PreferencesView.show_developer_ui>` ត្រូវបានបើក
Operator Search អាចចូលប្រើបានពីម៉ឺនុយ Edit នៅរបារកំពូល។
ម៉ឺនុយនេះស្វែងរក :doc:`operator </interface/operators>` ទាំងអស់ក្នុង Blender
ទោះបីជាវាមិនត្រូវបានបង្ហាញក្នុងម៉ឺនុយក៏ដោយ។
នេះមានប្រយោជន៍សម្រាប់អ្នកអភិវឌ្ឍន៍ Python សម្រាប់គោលបំណងសាកល្បង។
Blender ក៏អាចរួមបញ្ចូល operator កម្រិតខ្ពស់មួយចំនួន ដែលមិនត្រូវបានបង្ហាញក្នុងម៉ឺនុយ
ហើយអាចចូលប្រើបានតាមរយៈម៉ឺនុយស្វែងរកនេះប៉ុណ្ណោះ។

.. seealso::

   :ref:`User Preferences <bpy.types.Preferences.use_recent_searches>`
   មានជម្រើសដើម្បីផ្លាស់ប្ដូរពីរបៀបដែលលទ្ធផលស្វែងរកត្រូវបានដាក់ពិន្ទុ។

.. _bpy.ops.ed:

#############################################
  មិនធ្វើវិញ និងធ្វើឡើងវិញ (Undo & Redo)
#############################################

ឧបករណ៍ដែលបានរាយខាងក្រោមនឹងអនុញ្ញាតឱ្យអ្នកត្រឡប់សកម្មភាពដែលបានធ្វើដោយចៃដន្យ
ធ្វើសកម្មភាពចុងក្រោយរបស់អ្នកឡើងវិញ ឬអនុញ្ញាតឱ្យអ្នកជ្រើសរើសស្ដារទៅចំណុចជាក់លាក់មួយ
ដោយជ្រើសរើសពីបញ្ជីសកម្មភាពថ្មីៗដែល Blender បានកត់ត្រា។


.. _bpy.ops.ed.undo:

មិនធ្វើវិញ (Undo)
====================

.. reference::

   :Mode:      គ្រប់របៀបទាំងអស់
   :Menu:      :menuselection:`Edit --> Undo`
   :Shortcut:  :kbd:`Ctrl-Z`

ប្រសិនបើអ្នកចង់មិនធ្វើសកម្មភាពចុងក្រោយរបស់អ្នកវិញ គ្រាន់តែចុច :kbd:`Ctrl-Z`។

.. seealso::

   `Memory & Limits Preferences
   <https://docs.blender.org/manual/en/5.2/editors/preferences/system.html#prefs-system-memory-and-limits>`__
   ដើម្បីផ្លាស់ប្ដូរការកំណត់ Undo។


.. _bpy.ops.ed.redo:

ធ្វើឡើងវិញ (Redo)
=====================

.. reference::

   :Mode:      គ្រប់របៀបទាំងអស់
   :Menu:      :menuselection:`Edit --> Redo`
   :Shortcut:  :kbd:`Shift-Ctrl-Z`

ដើម្បីត្រឡប់សកម្មភាព Undo វិញ សូមចុច :kbd:`Shift-Ctrl-Z`។


.. _bpy.ops.screen.redo_last:

ការកែប្រតិបត្តិការចុងក្រោយ (Adjust Last Operation)
====================================================

.. reference::

   :Mode:      គ្រប់របៀបទាំងអស់
   :Menu:      :menuselection:`Edit --> Adjust Last Operation...`
   :Shortcut:  :kbd:`F9`

អ្នកអាចកែតម្រូវប៉ារ៉ាម៉ែត្ររបស់ :doc:`operator </interface/operators>` បន្ទាប់ពីដំណើរការវា។
ក្នុង editor ដែលគាំទ្រវា មានផ្ទាំង «head-up display» នៅជ្រុងខាងក្រោមផ្នែកឆ្វេង
ដោយផ្អែកលើប្រតិបត្តិការចុងក្រោយដែលបានធ្វើ។
ជាជម្រើស អ្នកអាចបង្កើតផ្ទាំងលោតដោយ :kbd:`F9` ដែលធ្វើរឿងដូចគ្នា។

ឧទាហរណ៍ ប្រសិនបើប្រតិបត្តិការចុងក្រោយរបស់អ្នកជាការបង្វិលក្នុង *Object Mode*
Blender នឹងបង្ហាញអ្នកនូវតម្លៃចុងក្រោយដែលបានផ្លាស់ប្ដូរសម្រាប់មុំ
(សូមមើលរូប :ref:`fig-interface-redo-last-object-mode` ខាងឆ្វេង)
ដែលអ្នកអាចផ្លាស់ប្ដូរសកម្មភាពរបស់អ្នកត្រឡប់ទាំងស្រុង ដោយវាយ :kbd:`Numpad0` ក្នុងប្រអប់ *Angle*។
មានជម្រើសមានប្រយោជន៍ផ្សេងទៀត ដោយផ្អែកលើ operator
ហើយអ្នកមិនអាចត្រឹមតែមិនធ្វើសកម្មភាពវិញបានទេ ប៉ុន្តែអាចផ្លាស់ប្ដូរវាទាំងស្រុង
ដោយប្រើជម្រើសដែលមាន។

ប្រសិនបើអ្នកស្ថិតក្នុង *Edit Mode*
Blender នឹងផ្លាស់ប្ដូរមាតិការបស់វាផងដែរ ដោយផ្អែកលើសកម្មភាពចុងក្រោយរបស់អ្នក។
ក្នុងឧទាហរណ៍ទីពីរ (ខាងស្ដាំ) ប្រតិបត្តិការចុងក្រោយគឺ Move ក្នុង Object Mode;
ប៉ុន្តែ *Scale* លើ Face ក្នុង Edit Mode ហើយដូចដែលអ្នកឃើញ
មាតិការបស់ *Adjust Last Operation* ខុសគ្នា ដោយសាររបៀប (Edit Mode)
(សូមមើលរូប :ref:`fig-interface-redo-last-edit-mode` ខាងស្ដាំ)។

.. list-table:: Adjust Last Operation។

   * - .. _fig-interface-redo-last-object-mode:

       .. figure:: /images/interface_undo-redo_redo-last-object-mode.png
          :width: 310px

          ការបង្វិល (Object Mode, ៦០ ដឺក្រេ)។

     - .. _fig-interface-redo-last-edit-mode:

       .. figure:: /images/interface_undo-redo_redo-last-edit-mode.png
          :width: 310px

          ការប្ដូរទំហំ (Edit Mode, ប្ដូរទំហំមុខ)។

.. tip::

   ប្រតិបត្តិការខ្លះផ្ដល់លទ្ធផលដែលមានប្រយោជន៍ជាពិសេស ដោយប្រើ *Adjust Last Operation*។
   ឧទាហរណ៍ ការបន្ថែម Circle ក្នុង 3D Viewport; ប្រសិនបើអ្នកបន្ថយ *Vertices* មកត្រឹមបី
   អ្នកនឹងទទួលបានត្រីកោណសម័ង្សដ៏ល្អឥតខ្ចោះ។

.. tip::

   តំបន់រង *Adjust Last Operation* អាចត្រូវបានលាក់ដោយ
   :menuselection:`View --> Adjust Last Operation`។


.. _bpy.ops.ed.undo_history:

ប្រវត្តិមិនធ្វើវិញ (Undo History)
===================================

.. reference::

   :Mode:      គ្រប់របៀបទាំងអស់
   :Menu:      :menuselection:`Edit --> Undo History`

.. figure:: /images/interface_undo-redo_undo-history-menu.png
   :align: right

   ម៉ឺនុយ Undo History។

ក៏មានប្រវត្តិ Undo នៃសកម្មភាពចុងក្រោយដែលបានធ្វើ ដែល Blender បានកត់ត្រាផងដែរ។

ផ្នែកខាងលើនៃបញ្ជីត្រូវនឹងសកម្មភាពថ្មីៗបំផុត។
រូបតំណាងចំណុចតូចមួយនៅក្បែរធាតុណាមួយ បញ្ជាក់ពីស្ថានភាពបច្ចុប្បន្ន។
ការត្រឡប់សកម្មភាពដោយប្រើមុខងារ *Undo History* នឹងនាំអ្នកត្រឡប់ទៅ
សកម្មភាពដែលអ្នកជ្រើសរើស។ ដូចគ្នានឹងរបៀបដែលអ្នកអាចប្ដូររវាងការថយក្រោយក្នុងពេលវេលា
ដោយ *Undo* ហើយបន្ទាប់មកទៅមុខដោយ *Redo*
អ្នកអាចលោតចុះឡើងលើបន្ទាត់ពេលវេលា Undo តាមដែលអ្នកចង់
ដរាបណាអ្នកមិនធ្វើការផ្លាស់ប្ដូរថ្មី។
នៅពេលអ្នកធ្វើការផ្លាស់ប្ដូរថ្មី ប្រវត្តិ Undo នឹងត្រូវបានកាត់ត្រឹមចំណុចនោះ។
ការជ្រើសរើសធាតុមួយក្នុងបញ្ជី នឹងនាំស្ថានភាពបច្ចុប្បន្នទៅទីតាំងនោះ។


.. _bpy.ops.screen.repeat_last:

ធ្វើចុងក្រោយឡើងវិញ (Repeat Last)
=====================================

.. reference::

   :Mode:      គ្រប់របៀបទាំងអស់
   :Panel:     :menuselection:`Edit --> Repeat Last`
   :Shortcut:  :kbd:`Shift-R`

មុខងារ Repeat Last នឹងធ្វើសកម្មភាពចុងក្រោយរបស់អ្នកឡើងវិញ នៅពេលអ្នកចុច :kbd:`Shift-R`។

ក្នុងរូបភាពឧទាហរណ៍ខាងក្រោម យើងបានចម្លង mesh *Monkey* មួយ ហើយផ្លាស់ទីវាបន្តិច។
ដោយប្រើ repeat :kbd:`Shift-R` *Monkey* ត្រូវបានចម្លង និងផ្លាស់ទីជាលើកទីពីរ។

.. list-table::

   * - .. figure:: /images/interface_undo-redo_repeat-last1.png

          Suzanne។

     - .. figure:: /images/interface_undo-redo_repeat-last2.png

          បន្ទាប់ពី :kbd:`Shift-D` ហើយផ្លាស់ទី។

     - .. figure:: /images/interface_undo-redo_repeat-last3.png

          បន្ទាប់ពី :kbd:`Shift-R`។


.. _bpy.ops.screen.repeat_history:

ប្រវត្តិធ្វើឡើងវិញ (Repeat History)
======================================

.. reference::

   :Mode:      គ្រប់របៀបទាំងអស់
   :Menu:      :menuselection:`Edit --> Repeat History...`

.. figure:: /images/interface_undo-redo_repeat-history-menu.png
   :align: right

   ម៉ឺនុយ Repeat History។

មុខងារ *Repeat History* នឹងបង្ហាញបញ្ជីសកម្មភាពដែលបានធ្វើឡើងវិញចុងក្រោយ
ហើយអ្នកអាចជ្រើសរើសសកម្មភាពដែលអ្នកចង់ធ្វើឡើងវិញ។
វាដំណើរការដូចគ្នានឹង Undo History ដែលបានពន្យល់ខាងលើ
ប៉ុន្តែបញ្ជីមានតែសកម្មភាពដែលបានធ្វើឡើងវិញប៉ុណ្ណោះ។

.. container:: lead

   .. clear

.. important::

   នៅពេលអ្នកបិទ Blender បញ្ជីសកម្មភាពអ្នកប្រើទាំងមូលនឹងបាត់បង់
   ទោះបីជាអ្នករក្សាទុកឯកសាររបស់អ្នកមុនពេលបិទក៏ដោយ។

.. seealso::

   ផ្នែកដោះស្រាយបញ្ហាអំពី
   `ការស្ដារការងារដែលបានបាត់បង់ <https://docs.blender.org/manual/en/5.2/troubleshooting/recover.html>`__។

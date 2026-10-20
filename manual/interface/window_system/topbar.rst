######################
  របារកំពូល (Topbar)
######################

ម៉ឺនុយ
=======

.. figure:: /images/interface_window-system_topbar_menus.png


.. _topbar-blender_menu:

ម៉ឺនុយ Blender
----------------

Splash Screen
   បើក :doc:`អេក្រង់ចាប់ផ្ដើម </interface/window_system/splash>`។

.. _bpy.ops.wm.splash_about:

About Blender
   បើកម៉ឺនុយដែលបង្ហាញព័ត៌មានខាងក្រោមអំពី Blender៖

   - **Version**៖ កំណែរបស់ Blender។
   - **Date**៖ កាលបរិច្ឆេទដែល Blender ត្រូវបាន compile។
   - **Hash**៖ Git Hash នៃ build។
     នេះអាចមានប្រយោជន៍ក្នុងការផ្ដល់ឱ្យបុគ្គលិកជំនួយ នៅពេលធ្វើរោគវិនិច្ឆ័យបញ្ហា។
   - **Branch**៖ ឈ្មោះសាខា (branch) ជាជម្រើស។
   - **Windowing Environment**៖ នៅលើ Linux នេះនឹងបង្ហាញ Wayland ឬ X11
     អាស្រ័យលើបរិស្ថានបង្អួចដែល Blender កំពុងដំណើរការ។

   - **Donate**៖ បើកគេហទំព័រ `Development Fund <https://fund.blender.org/>`__ របស់ Blender។
   - **What's New**៖ បើកកំណត់ត្រាការចេញផ្សាយចុងក្រោយ។
   - **Credits**៖ បើកទំព័រ `credits <https://www.blender.org/about/credits/>`__។
   - **License**៖ បើកទំព័រ `license <https://www.blender.org/about/license/>`__។
   - **Blender Store**៖ បើកគេហទំព័រ `Blender Store <https://store.blender.org/>`__។
   - **Blender Website**៖ បើកគេហទំព័រ `Blender <https://www.blender.org/>`__ ចម្បង។

Install Application Template
   ដំឡើង `application template
   <https://docs.blender.org/manual/en/5.2/advanced/app_templates.html#app-templates>`__ ថ្មី។


ម៉ឺនុយ File
-------------

ជម្រើសសម្រាប់គ្រប់គ្រងឯកសារគឺ៖

New :kbd:`Ctrl-N`
   សម្អាតឆាកបច្ចុប្បន្ន ហើយផ្ទុក application template ដែលបានជ្រើសរើស។
Open :kbd:`Ctrl-O`
   :ref:`បើក <bpy.ops.wm.open_mainfile>` ឯកសារ ``.blend``។
Open Recent :kbd:`Shift-Ctrl-O`
   បង្ហាញបញ្ជីឯកសារ ``.blend``
   `ដែលបានបើកថ្មីៗ <https://docs.blender.org/manual/en/5.2/files/blend/open_save.html#other-file-open-options>`__។
   ការដាក់ទ្រនិចលើធាតុនឹងបង្ហាញការមើលជាមុន និងព័ត៌មានអំពីឯកសារ ``.blend``។
   ជ្រើសរើសឈ្មោះឯកសារណាមួយក្នុងបញ្ជី ដើម្បីបើកឯកសារ ``.blend`` នោះ។

   Clear Recent Files List
      ដកធាតុចេញពីបញ្ជីឯកសារថ្មីៗ។
Revert
   បើកឯកសារបច្ចុប្បន្នឡើងវិញទៅកំណែដែលបានរក្សាទុកចុងក្រោយ។
Recover
   ជម្រើសដើម្បីស្ដារឯកសារ ``.blend`` ពីការបិទ Blender ដោយចៃដន្យ ឬការគាំង។ សូមមើល៖

   - :ref:`bpy.ops.wm.recover_last_session`
   - :ref:`bpy.ops.wm.recover_auto_save`

-----

Save :kbd:`Ctrl-S`
   :ref:`រក្សាទុក <bpy.ops.wm.save_mainfile>` ឯកសារ ``.blend`` បច្ចុប្បន្ន។
Save As... :kbd:`Shift-Ctrl-S`
   បើក File Browser ដើម្បីបញ្ជាក់ឈ្មោះឯកសារ និងទីតាំងសម្រាប់
   :ref:`រក្សាទុក <bpy.ops.wm.save_mainfile>`។
Save Copy...
   :ref:`រក្សាទុក <bpy.ops.wm.save_mainfile>` ច្បាប់ចម្លងនៃឯកសារបច្ចុប្បន្ន។
Save Incremental :kbd:`Ctrl-Alt-S`
   រក្សាទុកឯកសារ Blender បច្ចុប្បន្នដោយឈ្មោះដែលបង្កើនជាលេខ
   ដោយមិនសរសេរជាន់លើឯកសារដែលមានស្រាប់ទេ។

----

Link...
   ភ្ជាប់ទិន្នន័យពីឯកសារ ``.blend`` ខាងក្រៅ (បណ្ណាល័យ) មកឯកសារបច្ចុប្បន្ន។
   ការកែសម្រួលទិន្នន័យនោះអាចធ្វើបានតែនៅក្នុងបណ្ណាល័យខាងក្រៅប៉ុណ្ណោះ។
   *Link* និង *Append* ត្រូវបានប្រើដើម្បីផ្ទុកតែផ្នែកដែលបានជ្រើសរើសពីឯកសារផ្សេង។
   សូមមើល `Linked Libraries <https://docs.blender.org/manual/en/5.2/files/linked_libraries/index.html>`__។
Append...
   បន្ថែមទិន្នន័យពីឯកសារ ``.blend`` ខាងក្រៅមកឯកសារបច្ចុប្បន្ន។
   ទិន្នន័យថ្មីត្រូវបានចម្លងពីឯកសារខាងក្រៅ ហើយផ្ដាច់ការភ្ជាប់ពីវាទាំងស្រុង។
Data Previews
   ឧបករណ៍សម្រាប់គ្រប់គ្រង `ការមើលជាមុនរបស់ data-block
   <https://docs.blender.org/manual/en/5.2/files/blend/previews.html>`__។

-----

Import
   Blender អាចប្រើព័ត៌មានដែលរក្សាទុកក្នុងឯកសារទម្រង់ផ្សេងៗ
   ដែលបង្កើតដោយកម្មវិធីក្រាហ្វិកផ្សេងទៀត។
   សូមមើល `Import/Export <https://docs.blender.org/manual/en/5.2/files/import_export/index.html>`__។
Export
   ជាធម្មតាអ្នករក្សាទុកការងាររបស់អ្នកក្នុងឯកសារ ``.blend``
   ប៉ុន្តែអ្នកអាចនាំចេញការងារខ្លះ ឬទាំងអស់ ទៅទម្រង់ដែលកម្មវិធីក្រាហ្វិកផ្សេងអាចដំណើរការបាន។
   សូមមើល `Import/Export <https://docs.blender.org/manual/en/5.2/files/import_export/index.html>`__។

.. _bpy.ops.wm.collection_export_all:

Export All Collections
   ហៅ `exporter ដែលបានកំណត់
   <https://docs.blender.org/manual/en/5.2/scene_layout/collections/collections.html#collections-exporters>`__
   ទាំងអស់ សម្រាប់ collection ទាំងអស់។

-----

External Data
   ទិន្នន័យខាងក្រៅ ដូចជារូបភាព texture និងធនធានផ្សេងទៀត
   អាចរក្សាទុកខាងក្នុងឯកសារ ``.blend`` (packed) ឬជាឯកសារដាច់ដោយឡែក (unpacked)។
   Blender តាមដានធនធាន unpacked ទាំងអស់តាមរយៈផ្លូវសមេក (relative) ឬផ្លូវពេញ (absolute)។
   សូមមើល `pack ឬ unpack ទិន្នន័យខាងក្រៅ
   <https://docs.blender.org/manual/en/5.2/files/blend/packed_data.html#pack-unpack-data>`__។

   Automatically Pack Resources
      Pack ឯកសារខាងក្រៅទាំងអស់ដែលកំពុងប្រើ ចូលក្នុងឯកសារ ``.blend``
      ហើយ pack ឯកសារដែលបន្ថែមនៅពេលក្រោយដោយស្វ័យប្រវត្តិ។
      ការដកធីកជម្រើសនេះនឹងបញ្ឈប់តែការ pack ស្វ័យប្រវត្តិសម្រាប់ឯកសារថ្មី;
      វានឹងមិន unpack ឯកសារដែលមានស្រាប់ទេ។
   Pack Resources
      Pack ឯកសារខាងក្រៅទាំងអស់ដែលបានប្រើ ចូលក្នុងឯកសារ ``.blend``។
      បន្ទាប់ពីដំណើរការ operator នេះ និងរក្សាទុកឯកសារ ``.blend``
      ឯកសារខាងក្រៅនឹងលែងត្រូវបានប្រើទៀតហើយ — ការផ្លាស់ប្ដូរណាមួយក្នុងវា
      នឹងលែងបង្ហាញក្នុងឯកសារ ``.blend`` ហើយអ្នកអាចផ្លាស់ទី ឬលុបវាបានដោយសេរី។
   Unpack Resources
      នាំចេញឯកសារដែលបាន pack ពីមុន ត្រឡប់ទៅជាឯកសារខាងក្រៅវិញ។
      អ្នកអាចជ្រើសរើសថា ត្រូវប្រើឯកសារខាងក្រៅដែលមានស្រាប់ឡើងវិញ ឬសរសេរជាន់លើវា។
   Pack Linked Libraries
      Pack data-block ដែលបាន `ភ្ជាប់ (linked)
      <https://docs.blender.org/manual/en/5.2/files/linked_libraries/link_append.html>`__
      ពីឯកសារ ``.blend`` ខាងក្រៅ ចូលមកក្នុងឯកសារបច្ចុប្បន្ន។
   Unpack Linked Libraries
      នាំចេញ data-block ដែលបាន pack ពីមុន ត្រឡប់ទៅជាឯកសារ ``.blend`` ខាងក្រៅវិញ។
      ឯកសារ ``.blend`` ដែលមានស្រាប់នឹងត្រូវសរសេរជាន់លើ។
   Make Paths Relative
      ធ្វើឱ្យផ្លូវទាំងអស់ទៅឯកសារខាងក្រៅ
      `សមេក (relative) <https://docs.blender.org/manual/en/5.2/files/blend/open_save.html#files-blend-relative-paths>`__
      ធៀបនឹងឯកសារ ``.blend`` បច្ចុប្បន្ន។
   Make Paths Absolute
      ធ្វើឱ្យផ្លូវទាំងអស់ទៅឯកសារខាងក្រៅជាផ្លូវពេញ (absolute = ផ្លូវពេញពី root របស់ប្រព័ន្ធ)។
   Report Missing Files
      ជម្រើសនេះមានប្រយោជន៍ដើម្បីពិនិត្យថាតើមានតំណទៅឯកសារ unpacked ដែលលែងមានឬអត់។
      បន្ទាប់ពីជ្រើសរើសជម្រើសនេះ សារព្រមានមួយនឹងលេចឡើងក្នុងរបារបញ្ជារបស់ Info editor។
      ប្រសិនបើគ្មានការព្រមានបង្ហាញ នោះមានន័យថាគ្មានឯកសារខាងក្រៅបាត់ទេ។
   Find Missing Files
      ក្នុងករណីអ្នកមានតំណខូចក្នុងឯកសារ ``.blend`` នេះអាចជួយអ្នកកែបញ្ហា។
      File Browser នឹងលេចឡើង។ ជ្រើសរើសថតដែលចង់បាន (ឬឯកសារក្នុងថតនោះ)
      ហើយការស្វែងរកនឹងត្រូវបានធ្វើក្នុងវា ដោយឆ្លងកាត់ថតរងទាំងអស់។
      ឯកសារបាត់រាល់ឯកសារដែលរកឃើញ នឹងត្រូវបានស្ដារឡើងវិញ។
      ការស្ដារទាំងនោះនឹងធ្វើឡើងជាផ្លូវពេញ (absolute path)
      ដូច្នេះប្រសិនបើអ្នកចង់បានផ្លូវសមេក អ្នកត្រូវជ្រើសរើស *Make Paths Relative*។

      .. note::

         ឯកសារដែលបានស្ដារអាចត្រូវការផ្ទុកឡើងវិញ។ អ្នកអាចធ្វើវាម្ដងមួយៗ
         ឬអ្នកអាចរក្សាទុកឯកសារ ``.blend`` ហើយផ្ទុកវាឡើងវិញ
         ដើម្បីឱ្យឯកសារខាងក្រៅទាំងអស់ត្រូវបានផ្ទុកឡើងវិញក្នុងពេលតែមួយ។

Clean Up
   Purge Unused Data
      បើកផ្ទាំងសន្ទនាដើម្បីដក data-block ដែលមិនបានប្រើចេញពីឯកសារ ``.blend`` បច្ចុប្បន្ន
      ឬពី `ទិន្នន័យដែលបានភ្ជាប់ (Linked Data)
      <https://docs.blender.org/manual/en/5.2/files/linked_libraries/link_append.html>`__
      (មិនអាចមិនធ្វើវិញបានទេ)។
      សូមមើល :ref:`Outliner <bpy.ops.outliner.orphans_purge>` សម្រាប់ព័ត៌មានបន្ថែម។

   .. _bpy.ops.outliner.orphans_manage:

   Manage Unused Data
      បើកបង្អួចលោត (pop-up) របស់
      `Outliner <https://docs.blender.org/manual/en/5.2/editors/outliner/index.html>`__
      ក្នុង :ref:`របៀប Unused Data <bpy.types.SpaceOutliner.display_mode>` ដែលរាយ
      `data-block <https://docs.blender.org/manual/en/5.2/files/data_blocks.html>`__
      និងទិន្នន័យផ្សេងទៀតដែលមិនបានប្រើ និង/ឬនឹងបាត់បង់នៅពេលផ្ទុកឯកសារឡើងវិញ។
      វារួមបញ្ចូល data-block ដែលមានតែអ្នកប្រើក្លែង (fake user)។
      អ្នកអាចបន្ថែម/ដក Fake User ដោយចុចលើរូបតំណាងឆ្កាវ/ធីក នៅផ្នែកខាងស្ដាំរបស់ Outliner។

-----

.. _startup-file:

Defaults
   ម៉ឺនុយនេះគ្រប់គ្រងឯកសារចាប់ផ្ដើម (startup file) ដែលប្រើដើម្បីរក្សាទុកឆាកលំនាំដើម
   តំបន់ការងារ (workspace) និងចំណុចប្រទាក់ ដែលបង្ហាញនៅពេលបង្កើតឯកសារថ្មី។

   ដំបូងឡើយវាមាន `ឆាកចាប់ផ្ដើម
   <https://docs.blender.org/manual/en/5.2/editors/3dview/startup_scene.html>`__
   ដែលភ្ជាប់មកជាមួយ Blender។ នេះអាចត្រូវបានជំនួសដោយការរៀបចំផ្ទាល់ខ្លួនរបស់អ្នក។

   .. _bpy.ops.wm.save_homefile:

   Save Startup File
      រក្សាទុកឯកសារ ``.blend`` បច្ចុប្បន្នជាឯកសារចាប់ផ្ដើម។

   .. _bpy.ops.wm.read_factory_settings:

   Load Factory Settings
      ស្ដារឯកសារចាប់ផ្ដើម និងចំណូលចិត្តលំនាំដើមឡើងវិញ។

   នៅពេលដែល `application template
   <https://docs.blender.org/manual/en/5.2/advanced/app_templates.html>`__
   កំពុងត្រូវបានប្រើ operator ខាងក្រោមនឹងបង្ហាញ៖

   Load Factory Blender Settings
      ផ្ទុកការកំណត់លំនាំដើមទៅការកំណត់ Blender ដើម ដោយគ្មានការផ្លាស់ប្ដូរ
      ដែលបានធ្វើពី application template បច្ចុប្បន្ន។
   Load Factory (Application Template Name) Settings
      ផ្ទុកការកំណត់លំនាំដើមទៅ application template ដើម។

   .. seealso:: `Preferences
      <https://docs.blender.org/manual/en/5.2/editors/preferences/introduction.html#prefs-menu>`__។

-----

Quit :kbd:`Ctrl-Q`
   បិទ Blender។ ឆាកបច្ចុប្បន្នត្រូវបានរក្សាទុកទៅឯកសារឈ្មោះ «quit.blend»
   ក្នុងថតបណ្ដោះអាសន្នរបស់ Blender (ដែលអាចរកបានក្នុងផ្ទាំង «File Paths» នៃ
   `Preferences <https://docs.blender.org/manual/en/5.2/editors/preferences/file_paths.html>`__)។


ម៉ឺនុយ Edit
------------

Undo, Redo, Undo History
   សូមមើល :doc:`/interface/undo_redo`។
Adjust Last Operation, Repeat Last, Repeat History
   សូមមើល :doc:`/interface/undo_redo`។
Menu Search
   ស្វែងរកម៉ឺនុយដោយផ្អែកលើឈ្មោះរបស់វា។
Operator Search
   ដំណើរការ operator ដោយផ្អែកលើឈ្មោះរបស់វា
   (:ref:`Developer Extras <bpy.types.PreferencesView.show_developer_ui>` តែប៉ុណ្ណោះ)។
Rename Active Item
   ប្ដូរឈ្មោះវត្ថុសកម្ម ឬ node;
   សូមមើល `ឧបករណ៍ Rename
   <https://docs.blender.org/manual/en/5.2/files/blend/rename.html#tools-rename-active>`__
   សម្រាប់ព័ត៌មានបន្ថែម។
Batch Rename
   ប្ដូរឈ្មោះប្រភេទទិន្នន័យច្រើនក្នុងពេលតែមួយ;
   សូមមើល :ref:`ឧបករណ៍ Batch Rename <bpy.ops.wm.batch_rename>` សម្រាប់ព័ត៌មានបន្ថែម។

.. _bpy.types.ToolSettings.lock_object_mode:

Lock Object Modes
   រារាំងការជ្រើសរើសវត្ថុដែលស្ថិតក្នុងរបៀប (mode) ខុសពីរបៀបបច្ចុប្បន្ន។

   .. note::

      ជម្រើសនេះអាចទប់ស្កាត់ការផ្លាស់ប្ដូររបៀបដោយចៃដន្យ ឧទាហរណ៍នៅពេលអ្នក
      ព្យាយាមជ្រើសរើសឆ្អឹង (bone) ក្នុង Pose Mode ដើម្បីធ្វើចលនា ប៉ុន្តែបែរជា
      ចុចលើផ្នែកមួយនៃទិដ្ឋភាពខាងក្រោយ (ដែលជាធម្មតានឹងជ្រើសរើសផ្នែកនោះ
      និងប្ដូរទៅ Object Mode)។

      អ្នកប្រហែលជាចង់បិទ *Lock Object Modes* ឧទាហរណ៍នៅពេលធ្វើ weighting
      លើវត្ថុដែលបាន rig ឬនៅពេល sculpting/painting
      ដែលអ្នកចង់ប្ដូររវាងវត្ថុក្នុងរបៀបផ្សេងៗគ្នាដោយចេតនា។

Preferences :kbd:`Ctrl-Comma`
   បើកផ្ទាំង `Preferences <https://docs.blender.org/manual/en/5.2/editors/preferences/index.html>`__។


.. _topbar-render:

ម៉ឺនុយ Render
---------------

Render Image :kbd:`F12`
   Render ឆាកសកម្មនៅ frame បច្ចុប្បន្ន។
Render Animation :kbd:`Ctrl-F12`
   Render ចលនានៃឆាកសកម្ម។

   .. seealso::

      - `Rendering Animations <https://docs.blender.org/manual/en/5.2/render/output/animation.html>`__
        សម្រាប់ព័ត៌មានលម្អិត។
Render Sequencer Image :kbd:`Alt-F12`
   ប្រសិនបើមាន `ឆាក Sequencer
   <https://docs.blender.org/manual/en/5.2/video_editing/sequencer_scene.html>`__
   ដែលខុសពីឆាកសកម្ម សូម render ឆាកនោះវិញ។
Render Sequencer Animation :kbd:`Ctrl-Alt-F12`
   Render ចលនានៃ `ឆាក Sequencer
   <https://docs.blender.org/manual/en/5.2/video_editing/sequencer_scene.html>`__។

   .. note::
      ជម្រើស render របស់ sequencer ទាំងពីរ កំណត់ជម្រើស
      :ref:`Show Sequencer Scene <bpy.types.SpaceImageEditor.show_sequencer_scene>`
      ដោយស្វ័យប្រវត្តិ នៅក្នុង image editor ផ្នែក Render Result បន្ទាប់ពី render។

Render Audio
   លាយសំឡេងរបស់ឆាកទៅជាឯកសារសំឡេង។

   .. seealso::

      - `Rendering audio <https://docs.blender.org/manual/en/5.2/render/output/audio/introduction.html>`__
        សម្រាប់ព័ត៌មានលម្អិត។
View Render :kbd:`F11`
   បង្ហាញបង្អួច Render។ (ចុចម្ដងទៀតដើម្បីត្រឡប់ទៅបង្អួច Blender ចម្បង។)

.. _topbar-render-view_animation:

View Animation :kbd:`Ctrl-F11`
   ចាក់ចលនាដែលបាន render ក្នុងកម្មវិធីចាក់ដាច់ដោយឡែក។

   .. seealso::

      - :ref:`កម្មវិធីចាក់ចលនា <bpy.ops.render.play_rendered_anim>` សម្រាប់ព័ត៌មានលម្អិត។
      - :ref:`Preferences <bpy.types.PreferencesFilePaths.animation_player_preset>`
        សម្រាប់ជ្រើសរើសកម្មវិធីចាក់ចលនាខុសពីលំនាំដើម។
Lock Interface
   ចាក់សោចំណុចប្រទាក់ក្នុងអំឡុងពេល render ដើម្បីផ្ដល់អង្គចងចាំច្រើនជាងទៅកម្មវិធី render។


.. _topbar-window:

ម៉ឺនុយ Window
---------------

New Window
   បង្កើតបង្អួចថ្មីដោយចម្លងបង្អួចបច្ចុប្បន្ន។
New Main Window
   បង្កើតបង្អួចថ្មីដែលមានតំបន់ការងារ និងការជ្រើសរើសឆាកផ្ទាល់ខ្លួន។
Toggle Window Fullscreen
   ប្ដូរបង្អួចបច្ចុប្បន្នទៅ/ចេញពីអេក្រង់ពេញ។
Next Workspace
   ប្ដូរទៅតំបន់ការងារបន្ទាប់។
Previous Workspace
   ប្ដូរទៅតំបន់ការងារមុន។

.. _bpy.types.Screen.show_statusbar:

Show Status Bar
   ជ្រើសរើសថាតើ :doc:`របារស្ថានភាព (Status Bar) </interface/window_system/status_bar>`
   នៅបាតបង្អួច គួរបង្ហាញឬអត់។

.. _bpy.ops.screen.screenshot:

Save Screenshot
   ថតរូបភាពនៃបង្អួច Blender បច្ចុប្បន្ន។
   File Browser នឹងបើកឡើងដើម្បីជ្រើសរើសទីកន្លែងរក្សាទុករូបថតអេក្រង់។

.. _bpy.ops.screen.screenshot_area:

Save Screenshot (Editor)
   ថតរូបភាពនៃកម្មវិធីកែសម្រួល (Editor) ដែលបានជ្រើសរើស។
   ជ្រើសរើស Editor ដោយចុច :kbd:`LMB` ខាងក្នុងតំបន់របស់វា បន្ទាប់ពីដំណើរការ operator។
   File Browser នឹងបើកឡើងដើម្បីជ្រើសរើសទីកន្លែងរក្សាទុករូបថតអេក្រង់។


ម៉ឺនុយ Help
-------------

សូមមើល :ref:`help-menu`។


តំបន់ការងារ (Workspaces)
=========================

.. figure:: /images/interface_window-system_topbar_workspaces.png
   :align: center

សំណុំផ្ទាំងចុច (tab) នេះត្រូវបានប្រើដើម្បីប្ដូររវាង
:doc:`តំបន់ការងារ (Workspaces) </interface/window_system/workspaces>`
ដែលជាប់ទាក់ទងគ្នាជាការរៀបចំបង្អួចដែលបានកំណត់ជាមុន។


ឆាក និងស្រទាប់ (Scenes & Layers)
==================================

.. figure:: /images/interface_window-system_topbar_scenes-layers.png
   :align: center

`ម៉ឺនុយ data-block <https://docs.blender.org/manual/en/5.2/interface/controls/templates/data_block.html#ui-data-block>`__
ទាំងនេះត្រូវបានប្រើដើម្បីជ្រើសរើស
`ឆាក (Scene) <https://docs.blender.org/manual/en/5.2/scene_layout/scene/index.html>`__ និង
`ស្រទាប់ទិដ្ឋភាព (View Layer) <https://docs.blender.org/manual/en/5.2/render/layers/index.html>`__ បច្ចុប្បន្ន។

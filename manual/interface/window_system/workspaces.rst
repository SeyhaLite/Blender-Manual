.. _bpy.ops.workspace:
.. _bpy.types.Window.workspace:

###########################################
  តំបន់ការងារ (Workspaces)
###########################################

តំបន់ការងារ (Workspace) គឺជាការរៀបចំបង្អួចដែលបានកំណត់ជាមុន។
Workspace នីមួយៗមានសំណុំនៃ :doc:`តំបន់ (Areas) </interface/window_system/areas>`
ដែលផ្ទុក `កម្មវិធីកែសម្រួល (Editors) <https://docs.blender.org/manual/en/5.2/editors/index.html>`__
ហើយមានគោលដៅលើកិច្ចការជាក់លាក់មួយ ដូចជា modeling, animation ឬការសរសេរស្គ្រីប។
ជាធម្មតាអ្នកនឹងប្ដូររវាង Workspace ជាច្រើន ខណៈពេលធ្វើការលើគម្រោងមួយ។

.. figure:: /images/interface_window-system_workspaces_screen.png
   :align: center

   Workspace ស្ថិតនៅរបារកំពូល (Topbar)។


.. _workspaces-controls:

ការគ្រប់គ្រង
============

Tabs
   ចុចលើផ្ទាំងចុច (tab) ដើម្បីប្ដូររវាង workspace។
   ចុចទ្វេដងលើ tab ដើម្បីប្ដូរឈ្មោះ workspace។

.. _bpy.ops.workspace.add:

:bl-icon:`add` Add Workspace
   បន្ថែម workspace ថ្មីពីគំរូដែលបានកំណត់ជាមុន (ឧទាហរណ៍ *Modeling*, *Sculpting*, *Compositing*)។

.. rubric:: ម៉ឺនុយបរិបទ (Context Menu) :kbd:`RMB`

.. _bpy.ops.workspace.duplicate:

Duplicate
   បង្កើតច្បាប់ចម្លងនៃ workspace ដែលបានជ្រើសរើស រួមទាំងការរៀបចំអេក្រង់ និង editor របស់វា។

.. _bpy.ops.workspace.delete:

Delete
   លុប workspace ដែលបានជ្រើសរើស។ ប្រសិនបើវាជា workspace ចុងក្រោយ វាមិនអាចដកបានទេ។

.. _bpy.ops.workspace.reorder_to_front:
.. _bpy.ops.workspace.reorder_to_back:

Reorder to Front/Back
   ផ្លាស់ទី tab របស់ workspace ទៅទីតាំងដំបូង (ខាងមុខ) ឬចុងក្រោយ (ខាងក្រោយ) ក្នុងបញ្ជី tab។

.. _bpy.ops.screen.workspace_cycle:

Previous Workspace :kbd:`Ctrl-PageUp`
   បើក workspace ដែលនៅខាងឆ្វេងជាប់នឹង workspace បច្ចុប្បន្ន។

Next Workspace :kbd:`Ctrl-PageDown`
   បើក workspace ដែលនៅខាងស្ដាំជាប់នឹង workspace បច្ចុប្បន្ន។

.. _bpy.ops.workspace.delete_all_others:

Delete Other Workspaces
   ដក workspace ទាំងអស់ លើកលែងតែមួយដែលបានចុចប៊ូតុងស្ដាំ។


Workspace លំនាំដើម
===================

ការចាប់ផ្ដើមលំនាំដើមរបស់ Blender បង្ហាញ workspace «Layout» នៅក្នុងតំបន់ចម្បង។
Workspace នេះគឺជា workspace ទូទៅសម្រាប់មើលឆាករបស់អ្នកជាមុន
ហើយមាន Editor ខាងក្រោម៖

- `3D Viewport <https://docs.blender.org/manual/en/5.2/editors/3dview/introduction.html>`__
  នៅខាងលើផ្នែកឆ្វេង។
- `Outliner <https://docs.blender.org/manual/en/5.2/editors/outliner/introduction.html>`__
  នៅខាងលើផ្នែកខាងស្ដាំ។
- `Properties <https://docs.blender.org/manual/en/5.2/editors/properties_editor.html>`__
  នៅខាងក្រោមផ្នែកខាងស្ដាំ។
- `Timeline <https://docs.blender.org/manual/en/5.2/editors/timeline.html>`__
  នៅខាងក្រោមផ្នែកឆ្វេង។

.. figure:: /images/interface_window-system_workspaces_layout.png
   :align: center

   Workspace 'Layout' របស់ Blender ជាមួយ editor បួន។

   3D Viewport (ពណ៌លឿង), Outliner (ពណ៌បៃតង), Properties (ពណ៌ខៀវ) និង Timeline (ពណ៌ក្រហម)។

Blender ក៏មាន workspace ផ្សេងទៀតជាច្រើនដែលបានបន្ថែមតាមលំនាំដើម៖

:Modeling: សម្រាប់កែប្រែ geometry ដោយឧបករណ៍ modeling។
:Sculpting: សម្រាប់កែប្រែ mesh ដោយឧបករណ៍ sculpting។
:UV Editing: សម្រាប់ផ្គូផ្គងកូអរដោនេ texture រូបភាពទៅផ្ទៃ 3D។
:Texture Paint: សម្រាប់លាបពណ៌ texture រូបភាពក្នុង 3D Viewport។
:Shading: សម្រាប់បញ្ជាក់លក្ខណសម្បត្តិសម្ភារៈ (material) សម្រាប់ការ render។
:Animation: សម្រាប់ធ្វើឱ្យលក្ខណសម្បត្តិនៃវត្ថុអាស្រ័យលើពេលវេលា។
:Rendering: សម្រាប់មើល និងវិភាគលទ្ធផល render។
:Compositing: សម្រាប់ផ្សំ និងកែច្នៃក្រោយការ render នៃរូបភាព និងព័ត៌មាន render។
:Geometry Nodes: សម្រាប់ modeling បែប procedural ដោយប្រើ
   `Geometry Nodes <https://docs.blender.org/manual/en/5.2/modeling/geometry_nodes/index.html>`__។
:Scripting: សម្រាប់ធ្វើអន្តរកម្មជាមួយ Python API របស់ Blender និងសរសេរស្គ្រីប។


Workspace បន្ថែម
-----------------

Blender មាន Workspace បន្ថែមមួយចំនួនដែលអាចជ្រើសរើស នៅពេលបន្ថែម Workspace ថ្មី៖


.. rubric:: 2D Animation

:2D Animation: Workspace ទូទៅសម្រាប់ធ្វើការជាមួយ Grease Pencil។
:2D Full Canvas: ស្រដៀងនឹង «2D Animation» ប៉ុន្តែមាន canvas ធំជាង។


.. rubric:: VFX

:Masking: សម្រាប់បង្កើត mask 2D សម្រាប់ compositing ឬការកាត់តវីដេអូ។
:Motion Tracking: សម្រាប់គណនាចលនាកាមេរ៉ា និងធ្វើឱ្យវីដេអូមានស្ថិរភាព (stabilize)។


.. rubric:: Video Editing

:Video Editing: សម្រាប់តម្រៀបមេឌៀចូលគ្នាជាវីដេអូតែមួយ។


ការរក្សាទុក និងការសរសេរជាន់លើ
================================

Workspace ត្រូវបានរក្សាទុកក្នុងឯកសារ ``.blend``។
នៅពេលអ្នកបើកឯកសារមួយ ការបើក `Load UI
<https://docs.blender.org/manual/en/5.2/files/blend/open_save.html#file-load-ui>`__
ក្នុង File Browser បញ្ជាក់ថា Blender គួរប្រើការរៀបចំអេក្រង់របស់ឯកសារ
ជំនួសឱ្យការរៀបចំបច្ចុប្បន្ន។

សំណុំ Workspace ផ្ទាល់ខ្លួនអាចត្រូវបានរក្សាទុកជាផ្នែកមួយនៃ
:doc:`ការកំណត់លំនាំដើម </getting_started/configuration/defaults>`។


ការកំណត់ Workspace
====================

.. reference::

   :Editor:    `Properties Editor <https://docs.blender.org/manual/en/5.2/editors/properties_editor.html>`__
   :Panel:     :menuselection:`Tool tab --> Workspace`

.. _bpy.types.WorkSpace.use_pin_scene:

Pin Scene
   នៅពេលបើក workspace បច្ចុប្បន្ននឹងចងចាំឆាកដែលបានជ្រើសរើសបច្ចុប្បន្ន។
   បន្ទាប់មក រាល់ពេលអ្នកបើក workspace នោះ វានឹងប្ដូរត្រឡប់ទៅឆាកនោះដោយស្វ័យប្រវត្តិ។

.. _bpy.types.WorkSpace.object_mode:

Mode
   ប្ដូរទៅ `Mode <https://docs.blender.org/manual/en/5.2/editors/3dview/modes.html>`__ នេះ
   នៅពេលបើក workspace។

.. _bpy.types.WorkSpace.sequencer_scene:

Sequencer Scene
   ឆាកដែលមានការកាត់ត ដែលប្រើដោយកម្មវិធីកែសម្រួលលំដាប់វីដេអូ (video sequence editor)។
   សូមមើល `Sequencer Scene
   <https://docs.blender.org/manual/en/5.2/video_editing/sequencer_scene.html>`__។

.. _bpy.types.WorkSpace.use_scene_time_sync:

Sync Scene Time
   ធ្វើសមកាលកម្មឆាកសកម្ម និងពេលវេលា ដោយផ្អែកលើ :ref:`scene strip <bpy.types.SceneStrip>`
   បច្ចុប្បន្នក្នុងកម្មវិធីកែសម្រួលលំដាប់វីដេអូ។
   សូមមើល `Sequencer Scene
   <https://docs.blender.org/manual/en/5.2/video_editing/sequencer_scene.html>`__។

.. _bpy.ops.wm.owner_enable:
.. _bpy.ops.wm.owner_disable:
.. _bpy.types.WorkSpace.use_filter_by_owner:

Filter Add-ons
   កំណត់ថា `add-on <https://docs.blender.org/manual/en/5.2/addons/index.html>`__ ណាខ្លះ
   ត្រូវបានបើកក្នុង workspace សកម្ម។ នៅពេលមិនធីក add-on សកលនឹងត្រូវបានប្រើ។
   នៅពេលធីក អ្នកអាចបើក add-on នីមួយៗក្នុងបញ្ជីខាងក្រោម។

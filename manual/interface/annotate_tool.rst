.. _bpy.ops.gpencil.annotate:

#############################################
  ចំណារពន្យល់ (Annotations)
#############################################

ឧបករណ៍ចំណារពន្យល់ (annotation tool) មាននៅក្នុង editor ជាច្រើន។
វាអាចប្រើដើម្បីបន្ថែមកំណត់ចំណាំទៅលើឧទាហរណ៍ វត្ថុ 3D ឬការរៀបចំ node។
ព្រួញនៅក្នុងរូបថតអេក្រង់ខាងក្រោម គឺជាចំណារពន្យល់មួយ។

.. figure:: /images/interface_annotate-tool_node-editor.png
   :align: center

   ឧបករណ៍ Annotations នៅក្នុង node editor។


.. _tool-annotate:

ឧបករណ៍ចំណារពន្យល់
==================

ឧបករណ៍ចំណារពន្យល់អាចត្រូវបានបើកនៅក្នុង Toolbar ហើយមានឧបករណ៍រងខាងក្រោម៖

.. _tool-annotate-freehand:

Annotate
   គូសខ្សែដោយដៃសេរីក្នុងតំបន់ចម្បង។

.. _tool-annotate-line:

Annotate Line
   ចុចហើយអូសដើម្បីបង្កើតបន្ទាត់។
   ជាជម្រើស អ្នកអាចជ្រើសរើសរចនាបថព្រួញសម្រាប់ដើម និងចុងបន្ទាត់។

.. _tool-annotate-polygon:

Annotate Polygon
   ចុចច្រើនដងដើម្បីបង្កើតបន្ទាត់ភ្ជាប់គ្នាច្រើន បន្ទាប់មកចុច :kbd:`Return` ឬ :kbd:`Esc` ដើម្បីបញ្ជាក់។

.. _tool-annotate-eraser:

Annotate Eraser
   ចុចហើយអូសដើម្បីដកបន្ទាត់ចេញ។
   ឧបករណ៍លុបមានការកំណត់ *Radius* ដែលអាចរកបានក្នុង :menuselection:`Tool Settings`។


ការកំណត់ឧបករណ៍
================

ទូទៅ
------

Color
   កែតម្រូវពណ៌នៃខ្សែដែលមានស្រាប់ និងខ្សែថ្មី។

Annotation Layer
   ម៉ឺនុយលោតតូច ដែលបង្ហាញឈ្មោះស្រទាប់បច្ចុប្បន្ន ដើម្បីចូលប្រើ `ស្រទាប់ Annotation`_។

.. _bpy.types.ToolSettings.annotation_stroke_placement_view3d:
.. _bpy.types.ToolSettings.annotation_stroke_placement_view2d:

Placement
   កំណត់ថាចំណារពន្យល់ត្រូវបានគូសនៅឯណា។

   :3D Cursor:
      មានតែក្នុង 3D Viewport។ ចំណារពន្យល់ថ្មីក្លាយជាផ្នែកនៃឆាក 3D;
      វាត្រូវបានគូសលើប្លង់និម្មិតមួយដែលកាត់តាម
      `3D Cursor <https://docs.blender.org/manual/en/5.2/editors/3dview/3d_cursor.html>`__
      ហើយតម្រឹមទៅនឹងទិដ្ឋភាពរបស់អ្នក។
   :Surface:
      មានតែក្នុង 3D Viewport។ ចំណារពន្យល់ថ្មីក្លាយជាផ្នែកនៃឆាក 3D;
      វាត្រូវបានគូសលើផ្ទៃនៃវត្ថុដែលនៅក្រោមកណ្ដុរ។ ប្រសិនបើគ្មានផ្ទៃ
      អ្នកទទួលបានឥរិយាបថដូចគ្នានឹង *3D Cursor*។
   :Image:
      មានតែក្នុង editor 2D ដូចជា
      `Image Editor <https://docs.blender.org/manual/en/5.2/editors/image/introduction.html>`__។
      ចំណារពន្យល់ក្លាយជាផ្នែកនៃលំហ 2D មានន័យថាទីតាំង និងទំហំរបស់វាផ្លាស់ប្ដូរ
      នៅពេលអ្នករំកិល (pan) និងពង្រីក (zoom) ក្នុង editor។
   :View:
      ចំណារពន្យល់ថ្មីជា 2D ហើយជាប់នឹងអេក្រង់។ វារក្សាទីតាំង ការបង្វិល និងទំហំដដែល
      មិនថាអ្នករំកិល បង្វិល ឬពង្រីកក្នុង editor យ៉ាងណាក៏ដោយ។

.. _bpy.types.ToolSettings.use_annotation_stroke_endpoints:

Only End Points :guilabel:`Surface Placement`
   ប្រើតែផ្នែកដំបូង និងចុងក្រោយនៃខ្សែ សម្រាប់ការខ្ទាស់ (snapping)។

.. _bpy.types.ToolSettings.use_annotation_project_only_selected:

Project Onto Selected :guilabel:`Surface Placement`
   បញ្ចាំងខ្សែតែទៅលើវត្ថុដែលបានជ្រើសរើសប៉ុណ្ណោះ។

Stabilize Stroke
   ជួយបន្ថយការញ័រនៃខ្សែខណៈពេលគូស ដោយពន្យារ និងកែតម្រូវទីតាំងនៃចំណុច។

   Radius
      ចម្ងាយអប្បបរមាពីចំណុចចុងក្រោយ មុនពេលខ្សែបន្ត។
   Factor
      កត្តាភាពរលូន ដែលតម្លៃខ្ពស់ជាងផ្ដល់ខ្សែរលូនជាង
      ប៉ុន្តែអារម្មណ៍នៃការគូសហាក់ដូចជាអ្នកកំពុងទាញខ្សែ។


Annotate Line
-------------

Style Start, End
   ការតុបតែងដែលត្រូវប្រើនៅដើម ឬចុងនៃផ្នែកបន្ទាត់។
   នេះអាចប្រើឧទាហរណ៍ដើម្បីបង្កើតព្រួញ ដើម្បីចង្អុលបង្ហាញព័ត៌មានលម្អិតជាក់លាក់ក្នុងឆាក។


.. _bpy.types.AnnotationLayer:

ស្រទាប់ Annotation
===================

នៅពេលដែលឧបករណ៍ចំណារពន្យល់ត្រូវបានបើក ការកំណត់សម្រាប់គ្រប់គ្រងស្រទាប់ច្រើន
អាចរកបានក្នុងផ្ទាំង :menuselection:`Sidebar --> View --> Annotations`។

.. _bpy.types.AnnotationLayer.annotation_opacity:

Opacity
   កែតម្រូវភាពថ្លារបស់ខ្សែដែលមានស្រាប់ និងខ្សែថ្មី។

Thickness
   កែតម្រូវកម្រាស់របស់ខ្សែដែលមានស្រាប់ និងខ្សែថ្មី។


.. _bpy.types.AnnotationLayer.use_annotation_onion_skinning:

Onion Skin
----------

បង្ហាញរូបភាពខ្ទើយ (ghosted image) នៃខ្សែដែលបានគូសក្នុង frame មុន និងក្រោយ frame បច្ចុប្បន្ន។
Onion skinning ដំណើរការតែក្នុង 3D Viewport និង Sequencer។
សូមមើលឯកសារ Grease Pencil សម្រាប់ការពន្យល់អំពី
`Onion Skinning <https://docs.blender.org/manual/en/5.2/grease_pencil/properties/onion_skinning.html>`__។

.. _bpy.types.AnnotationLayer.annotation_onion_before_color:
.. _bpy.types.AnnotationLayer.annotation_onion_before_range:
.. _bpy.types.AnnotationLayer.annotation_onion_after_color:
.. _bpy.types.AnnotationLayer.annotation_onion_after_range:

Before/After
   ពណ៌ដែលត្រូវប្រើមុន និងក្រោយ frame បច្ចុប្បន្នលើ frame ខ្ទើយ។
   ចំនួនកំណត់ថាត្រូវបង្ហាញ frame ប៉ុន្មានមុន និងក្រោយ frame បច្ចុប្បន្ន។

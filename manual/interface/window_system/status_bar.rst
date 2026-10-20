#############################################
  របារស្ថានភាព (Status Bar)
#############################################

របារស្ថានភាព (Status Bar) ស្ថិតនៅបាតបង្អួច Blender ហើយបង្ហាញព័ត៌មានអាស្រ័យបរិបទ
ដូចជា ផ្លូវកាត់ក្ដារចុច សារ និងព័ត៌មានស្ថិតិ។
របារស្ថានភាពអាចត្រូវបានលាក់ ដោយបិទ *Show Status Bar* ក្នុងម៉ឺនុយ Window
ឬដោយអូសពីគែមខាងលើចុះក្រោម។

.. figure:: /images/interface_window-system_status-bar_ui.png

   របារស្ថានភាព។


ព័ត៌មាន Keymap
================

ផ្នែកខាងឆ្វេងនៃរបារស្ថានភាព បង្ហាញផ្លូវកាត់ប៊ូតុងកណ្ដុរ និង keymap នៃឧបករណ៍សកម្ម។
ក្នុង editor ដែលមាន Toolbar ការចុច :kbd:`Alt` (ឬ ``Option`` នៅលើ macOS)
បង្ហាញគ្រាប់ចុចក្ដៅ (hotkey) ដើម្បីប្ដូរទៅឧបករណ៍ដែលចង់បាន។

.. tip::

   មុខងារនេះអាចត្រូវបានបិទដោយចំណូលចិត្ត *Alt Click Tool Prompt*
   ក្នុង `Keymap Preferences <https://docs.blender.org/manual/en/5.2/editors/preferences/keymap.html>`__។

.. figure:: /images/interface_window-system_status-bar_ui-left.png
   :align: center


សារស្ថានភាព
=============

ផ្នែកកណ្ដាលនៃរបារស្ថានភាព បង្ហាញព័ត៌មានអំពីប្រតិបត្តិការដែលកំពុងដំណើរការ។

.. figure:: /images/interface_window-system_status-bar_ui-center.png
   :align: center

Running Task
   បង្ហាញវឌ្ឍនភាពនៃកិច្ចការដែលកំពុងដំណើរការ (ដូចជា render ឬ bake)។
   ការដាក់ទ្រនិចកណ្ដុរលើរបារវឌ្ឍនភាព នឹងបង្ហាញការប៉ាន់ប្រមាណពេលវេលា។
   កិច្ចការអាចត្រូវបានបញ្ឈប់ដោយចុចប៊ូតុងបោះបង់ (:bl-icon:`cancel`)។
Report Message
   សារព័ត៌មាន ឬការព្រមាន ដូចជាបន្ទាប់ពីរក្សាទុកឯកសារ។
   វាបាត់ទៅវិញបន្ទាប់ពីរយៈពេលខ្លី។
   ចុចលើវាដើម្បីបង្ហាញសារពេញលេញក្នុង
   `Info Editor <https://docs.blender.org/manual/en/5.2/editors/info_editor.html>`__។


ព័ត៌មានធនធាន
===============

ផ្នែកខាងស្ដាំនៃរបារស្ថានភាព បង្ហាញព័ត៌មានអំពី Blender instance។
ថាតើព័ត៌មានអ្វីខ្លះត្រូវបង្ហាញ អាចជ្រើសរើសបានដោយចុច :kbd:`RMB` លើរបារស្ថានភាព
ឬក្នុង `Preferences
<https://docs.blender.org/manual/en/5.2/editors/preferences/interface.html#prefs-interface-status-bar>`__។

.. figure:: /images/interface_window-system_status-bar_ui-right.png
   :align: center

Scene Statistics
   បង្ហាញព័ត៌មានអំពីទិន្នន័យក្នុងឆាកសកម្ម។

   - **Collection**៖ ឈ្មោះនៃ `Collection
     <https://docs.blender.org/manual/en/5.2/scene_layout/collections/index.html>`__ សកម្ម។
   - **Active Object**៖ ឈ្មោះនៃវត្ថុសកម្មដែលបានជ្រើសរើស។
   - **Geometry**៖ ព័ត៌មានអំពីឆាកបច្ចុប្បន្ន អាស្រ័យលើរបៀប (mode) និងប្រភេទវត្ថុ។
     នេះអាចជាចំនួន vertex, face, triangle ឬ bone។
   - **Objects**៖ ចំនួនវត្ថុដែលបានជ្រើសរើស និងចំនួនវត្ថុសរុប។

Scene Duration
   បង្ហាញរយៈពេលសរុបនៃការចាក់ ព្រមទាំងលេខ frame បច្ចុប្បន្ន និងចំនួន frame សរុប។
   ទម្រង់អត្ថបទរយៈពេលត្រូវបានកំណត់ដោយ
   :ref:`Timecode Style <bpy.types.PreferencesView.timecode_style>`។

System Memory
   បង្ហាញការប៉ាន់ប្រមាណនៃការប្រើប្រាស់ RAM របស់ Blender។
   ក្នុងស្ថានការណ៍ instance តែមួយលើម៉ាស៊ីនតែមួយ
   ការប៉ាន់ប្រមាណនេះផ្ដល់ការវាស់វែងធៀបនឹងដែនកំណត់ផ្នែករឹងរបស់ម៉ាស៊ីន។

Extensions Updates
   បង្ហាញចំនួន `extension <https://docs.blender.org/manual/en/5.2/advanced/extensions/index.html>`__
   ដែលមានការធ្វើបច្ចុប្បន្នភាព។

Blender Version
   បង្ហាញលេខកំណែរបស់ Blender ដែលកំពុងដំណើរការ។

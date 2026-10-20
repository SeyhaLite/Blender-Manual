##########################
  សេចក្ដីណែនាំ
##########################

ខាងក្រោមនេះគឺជាចំណូលចិត្ត (preferences) មួយចំនួន ដែលអ្នកប្រហែលជាចង់កំណត់ជាដំបូង។
សូមមើលផ្នែក `Preferences <https://docs.blender.org/manual/en/5.2/editors/preferences/index.html>`__
សម្រាប់បញ្ជីការកំណត់ទាំងអស់ដែលមាន។ ផ្លូវកាត់ :kbd:`Ctrl-Comma`
អាចប្រើដើម្បីបើកកម្មវិធីកែសម្រួល Preferences បានយ៉ាងរហ័ស។


.. _autosave-preferences:

ការរក្សាទុកចំណូលចិត្តដោយស្វ័យប្រវត្តិ (Auto-Save Preferences)
================================================================

តាមលំនាំដើម ការដំឡើង Blender ថ្មីត្រូវបានកំណត់ឱ្យរក្សាទុកការផ្លាស់ប្ដូរចំណូលចិត្ត
ដោយស្វ័យប្រវត្តិ ដូច្នេះអ្នកមិនបាត់បង់ការផ្លាស់ប្ដូរដែលបានធ្វើដោយចៃដន្យ។
ដើម្បីបិទឥរិយាបថនេះ សូមអនុវត្តតាមជំហានទាំងនេះ៖

1. បើកផ្ទាំង Preferences
2. ចុចលើម៉ឺនុយតូចនៅខាងឆ្វេងផ្នែកខាងក្រោម (បង្ហាញដោយបន្ទាត់ ៣)
3. ដកធីកប្រអប់នៅខាងក្បែរ «*Auto-Save Preferences*»
4. ចុចប៊ូតុង «*Save Preferences*» ដែលនឹងលេចឡើងនៅខាងឆ្វេងផ្នែកខាងក្រោមនៃផ្ទាំង។
   **កុំភ្លេចជំហាននេះ ព្រោះការផ្លាស់ប្ដូរនឹងមិនត្រូវបានរក្សាទុកទេបើមិនដូច្នោះ។**

ដើម្បីបើកការរក្សាទុកស្វ័យប្រវត្តិឡើងវិញ គ្រាន់តែអនុវត្តតាមជំហាន ១–៣ ខាងលើ
ហើយធីកប្រអប់នៅជំហានទី ៣។


ភាសា (Language)
================

បើក :menuselection:`Edit --> Preferences --> Interface --> Translation`
ហើយជ្រើសរើស *Language* និងអ្វីដែលត្រូវបកប្រែពី *Interface*, *Tooltips* និង *New Data*។

សូមមើល `Translation Preferences
<https://docs.blender.org/manual/en/5.2/editors/preferences/interface.html#prefs-interface-translation>`__
សម្រាប់ព័ត៌មានលម្អិត។

.. note::

   ចំណុចប្រទាក់របស់ Blender អាចបកប្រែដាច់ដោយឡែកពីសៀវភៅណែនាំនេះ។
   សូមមើល `Translate Blender's UI
   <https://docs.blender.org/manual/en/5.2/contribute/translate_blender.html>`__។
   សៀវភៅណែនាំនេះសន្មតថាអ្នកប្រើចំណុចប្រទាក់ជាភាសាអង់គ្លេស ដូច្នេះឈ្មោះម៉ឺនុយ
   និងប៊ូតុងទាំងអស់ត្រូវបានរក្សាជាភាសាអង់គ្លេស។


ការបញ្ចូល (Input)
==================

ប្រសិនបើអ្នកមានក្ដារចុចតូចដែលគ្មានផ្ទាំងលេខ (number pad) ដាច់ដោយឡែក សូមបើក
:menuselection:`Preferences --> Input --> Keyboard --> Emulate Numpad`។
នេះផ្ដល់ឱ្យអ្នកនូវផ្លូវកាត់ទិដ្ឋភាព 3D ដែលប្រើជាធម្មតានៅលើផ្ទាំងលេខ។

ប្រសិនបើអ្នកគ្មានប៊ូតុងកណ្ដុរកណ្ដាល អ្នកអាចបើក
:menuselection:`Preferences --> Input --> Mouse --> Emulate 3 Button Mouse`។
នេះអនុញ្ញាតឱ្យអ្នកសង្កត់គ្រាប់ចុច :kbd:`Alt` ឬ :kbd:`OSKey` ខណៈពេលអូសកណ្ដុរ ដើម្បីបង្វិល (orbit)។

សូមមើល :doc:`ការកំណត់ឧបករណ៍បញ្ចូល <hardware>` សម្រាប់ព័ត៌មានបន្ថែមអំពីជម្រើសទាំងនេះ
ហើយសូមមើល `Input Preferences
<https://docs.blender.org/manual/en/5.2/editors/preferences/input.html>`__
សម្រាប់ព័ត៌មានលម្អិតអំពីការកំណត់របស់វា។


ឯកសារ និងផ្លូវ (File and Paths)
=================================

នៅ :menuselection:`Preferences --> File Paths` អ្នកអាចកំណត់ជម្រើស
ដូចជា *Image Editor* (GIMP, Krita...) និង *Animation Player* ដែលត្រូវប្រើ។

`Temporary Files <https://docs.blender.org/manual/en/5.2/advanced/blender_directory_layout.html#temp-dir>`__
កំណត់ថាត្រូវរក្សាទុកឯកសារដូចជា render បណ្ដោះអាសន្ន និង auto-save នៅឯណា។

.. tip::

   សញ្ញា ``//`` នៅដើមផ្លូវនីមួយៗក្នុង Blender មានន័យថា ថតនៃឯកសារ ``.blend``
   ដែលកំពុងបើកបច្ចុប្បន្ន ដែលប្រើដើម្បីយោងទៅផ្លូវសមេក (relative path)។

សូមមើល `File Preferences
<https://docs.blender.org/manual/en/5.2/editors/preferences/file_paths.html>`__
សម្រាប់ព័ត៌មានលម្អិត។


ការរក្សាទុក និងផ្ទុក (Save & Load)
===================================

ប្រសិនបើអ្នកទុកចិត្តប្រភពនៃឯកសារ ``.blend`` របស់អ្នក អ្នកអាចបើក *Auto Run Python Scripts*។
ជម្រើសនេះមានបំណងការពារអ្នកពីស្គ្រីប Python ដែលមានគំនិតអាក្រក់នៅក្នុងឯកសារ ``.blend``
ដែលអ្នកទទួលបានពីអ្នកដទៃ។ អ្នកប្រើជាច្រើនបើកជម្រើសនេះ ព្រោះ rig កម្រិតខ្ពស់
ច្រើនតែប្រើស្គ្រីបមួយចំនួន។ **សូមប្រុងប្រយ័ត្ន ព្រោះនេះជាការកំណត់សកល
ហើយអាចអនុញ្ញាតឱ្យកូដ Python ដែលមានគំនិតអាក្រក់ពីប្រភពដែលមិនអាចទុកចិត្តបានដំណើរការ។**

សូមមើលចំណូលចិត្ត Save & Load
:ref:`bpy.types.PreferencesFilePaths.use_scripts_auto_execute`។

#############################################
  ការជ្រើសរើស (Selecting)
#############################################

តាមលំនាំដើម Blender ប្រើ :kbd:`LMB` ដើម្បីជ្រើសរើសធាតុ។
នេះអាចផ្លាស់ប្ដូរទៅ :kbd:`RMB` បានក្នុង
`Preferences <https://docs.blender.org/manual/en/5.2/editors/preferences/keymap.html>`__។

Blender មានឧបករណ៍ជ្រើសរើសជាច្រើន ដែលអាចប្រើបាននៅគ្រប់ editor។

.. note::

   Editor ខ្លះខុសពីផ្លូវកាត់ក្ដារចុចដែលបានបង្ហាញខាងក្រោម។ ឧទាហរណ៍ editor ភាគច្រើន
   ប្រើ :kbd:`Shift-LMB` ដើម្បីបន្ថែមធាតុតែមួយទៅការជ្រើសរើស ប៉ុន្តែ
   `Outliner <https://docs.blender.org/manual/en/5.2/editors/outliner/introduction.html>`__
   ប្រើ :kbd:`Ctrl-LMB`។ ស្រដៀងគ្នា editor ភាគច្រើនប្រើ :kbd:`Ctrl-RMB` សម្រាប់ធ្វើ *Lasso Select*
   ប៉ុន្តែ `node editor <https://docs.blender.org/manual/en/5.2/interface/controls/nodes/index.html>`__
   ប្រើ :kbd:`Ctrl-Alt-LMB`។

ឧបករណ៍ជ្រើសរើសភាគច្រើនមានពីរទម្រង់ ដែលទម្រង់មួយមាននៅក្នុង Toolbar
ហើយមួយទៀតនៅក្នុងម៉ឺនុយ *Select*។ ខណៈដែលឈ្មោះរបស់ទម្រង់ទាំងពីរស្ទើរតែដូចគ្នា
(ដូចជា *Select Box* នៅក្នុង Toolbar ធៀបនឹង *Box Select* នៅក្នុងម៉ឺនុយ)
របៀបដែលវាដំណើរការខុសគ្នាបន្តិច។ អ្នកប្រើថ្មីដែលមកពីកម្មវិធីផ្សេងទៀត
នឹងឃើញថាទម្រង់នៅក្នុង Toolbar គឺស្គាល់ច្បាស់ជាងគេ។


ឧបករណ៍ជ្រើសរើសក្នុង Toolbar
=============================

ឧបករណ៍ជ្រើសរើសទាំងអស់ក្នុង Toolbar មានឥរិយាបថដូចគ្នានៅពេលចុចធាតុមួយ៖ វាជ្រើសរើសធាតុនោះ
(ហើយបោះបង់ការជ្រើសរើសធាតុដែលបានជ្រើសពីមុន)។ ប្រសិនបើអ្នកសង្កត់ :kbd:`Shift` ខណៈពេលចុច
ធាតុនោះនឹងត្រូវបានបន្ថែមទៅការជ្រើសរើស (ប្រសិនបើវាមិនទាន់បានជ្រើស) ឬដកចេញពីការជ្រើសរើស
(ប្រសិនបើវាបានជ្រើសរួចហើយ)។

អ្វីដែលធ្វើឱ្យឧបករណ៍ទាំងនេះខុសគ្នា គឺអ្វីដែលកើតឡើងនៅពេលអ្នកអូស។


.. _tool-select-tweak:

Tweak
-----

.. reference::

   :Tool:      :menuselection:`Toolbar --> Tweak`
   :Shortcut:  :kbd:`W`

ការអូសធាតុមួយនឹងផ្លាស់ទីវា។


.. _tool-select-box:

Select Box
----------

.. reference::

   :Tool:      :menuselection:`Toolbar --> Select Box`
   :Shortcut:  :kbd:`W`

ការអូសនឹងបង្កើតចតុកោណកែងមួយ ហើយជ្រើសរើសធាតុទាំងអស់ដែលនៅក្នុងវាទាំងស្រុង ឬមួយផ្នែក
នៅពេលអ្នកលែង។ (ធាតុផ្សេងទៀតទាំងអស់នឹងត្រូវបានបោះបង់ការជ្រើសរើស។)

ការសង្កត់ :kbd:`Shift` ខណៈពេលអូស នឹងបន្ថែមធាតុទៅការជ្រើសរើស។
ការសង្កត់ :kbd:`Ctrl` នឹងដកវាចេញ។

ខណៈពេលអូស អ្នកអាចសង្កត់ :kbd:`Spacebar` បន្ថែម ដើម្បីផ្លាស់ទីចតុកោណកែងដោយកណ្ដុរ។

.. list-table:: ឧទាហរណ៍ Select Box (Edit Mode)។

   * - .. _fig-mesh-select-basics-start:

       .. figure:: /images/interface_selecting_border-select1.png
          :width: 200px

          ចាប់ផ្ដើម។

     - .. _fig-mesh-select-basics-selecting:

       .. figure:: /images/interface_selecting_border-select2.png
          :width: 200px

          កំពុងជ្រើសរើស vertex។

     - .. _fig-mesh-select-basics-complete:

       .. figure:: /images/interface_selecting_border-select3.png
          :width: 200px

          បញ្ចប់។


.. _tool-select-circle:

Select Circle
-------------

.. reference::

   :Tool:      :menuselection:`Toolbar --> Select Circle`
   :Shortcut:  :kbd:`W`

ការអូសនឹងជ្រើសរើសធាតុទាំងអស់ដែលរង្វង់បានកាត់។
ធាតុដែលអ្នកមិនបានកាត់ នឹងត្រូវបានបោះបង់ការជ្រើសរើស។

ការសង្កត់ :kbd:`Shift` ខណៈពេលអូស នឹងបន្ថែមធាតុទៅការជ្រើសរើស។
ការសង្កត់ :kbd:`Ctrl` នឹងដកវាចេញ។

អ្នកអាចផ្លាស់ប្ដូរកាំរបស់រង្វង់ក្នុងការកំណត់ឧបករណ៍ (ដែលអាចរកបាន
ក្នុងបញ្ជីតំបន់ (area header) ផ្ទាំងចុច *Tool* នៃ Sidebar :kbd:`N`
ឬផ្ទាំងចុច *Active Tool* នៃ
`Properties editor <https://docs.blender.org/manual/en/5.2/editors/properties_editor.html>`__)។

.. note::

   ក្នុង `Object Mode <https://docs.blender.org/manual/en/5.2/editors/3dview/modes.html>`__៖
   ខុសពី *Select Box* ដែលជ្រើសរើសវត្ថុភ្លាមៗនៅពេលដែលប្រអប់គ្របដណ្ដប់ផ្នែកណាមួយ
   នៃ geometry របស់វា *Select Circle* ជ្រើសរើសវត្ថុ តែនៅពេលដែលរង្វង់កាត់ចំណុចដើម (origin)
   របស់វាប៉ុណ្ណោះ។ ចំណុចដើមត្រូវបានបង្ហាញជាចំណុចពណ៌ទឹកក្រូចសម្រាប់វត្ថុដែលបានជ្រើស
   ប៉ុន្តែមើលមិនឃើញសម្រាប់វត្ថុដែលមិនបានជ្រើស លើកលែងតែ «Origins (All)» ត្រូវបានបើក
   ក្នុង `Overlays <https://docs.blender.org/manual/en/5.2/editors/3dview/display/overlays.html>`__។

   ភាពខុសគ្នានៃឥរិយាបថនេះ មិនអនុវត្តចំពោះរបៀបផ្សេងទៀតទេ
   (ដូចជា Edit Mode និង Pose Mode)។

.. list-table:: ឧទាហរណ៍ Select Circle (Edit Mode)។

   * - .. figure:: /images/interface_selecting_circle-select1.png
          :width: 320px

          ចាប់ផ្ដើម។

     - .. figure:: /images/interface_selecting_circle-select2.png
          :width: 320px

          កំពុងជ្រើសរើស vertex។

     - .. figure:: /images/interface_selecting_circle-select3.png
          :width: 320px

          បញ្ចប់។


.. _tool-select-lasso:

Select Lasso
------------

.. reference::

   :Tool:      :menuselection:`Toolbar --> Select Lasso`
   :Shortcut:  :kbd:`W`

ការអូសនឹងបង្កើតរូបរាងសេរី ហើយជ្រើសរើសធាតុទាំងអស់នៅក្នុងវា នៅពេលអ្នកលែង។
(ធាតុផ្សេងទៀតទាំងអស់នឹងត្រូវបានបោះបង់ការជ្រើសរើស។)

ការសង្កត់ :kbd:`Shift` ខណៈពេលអូស នឹងបន្ថែមធាតុទៅការជ្រើសរើស។
ការសង្កត់ :kbd:`Ctrl` នឹងដកវាចេញ។

ខណៈពេលអូស អ្នកអាចសង្កត់ :kbd:`Spacebar` បន្ថែម ដើម្បីផ្លាស់ទីរូបរាងដោយកណ្ដុរ។

.. note::

   *Select Lasso* មានឥរិយាបថដូចគ្នានឹង *Select Circle* គឺ
   វាមើលតែចំណុចដើម (origin) ប៉ុណ្ណោះក្នុង Object Mode។

.. list-table:: ឧទាហរណ៍ Select Lasso (Edit Mode)។

   * - .. figure:: /images/interface_selecting_lasso-select1.png
          :width: 200px

          ចាប់ផ្ដើម។

     - .. figure:: /images/interface_selecting_lasso-select2.png
          :width: 200px

          កំពុងជ្រើសរើស vertex។

     - .. figure:: /images/interface_selecting_lasso-select3.png
          :width: 200px

          បញ្ចប់។


របៀបជ្រើសរើស (Selection Modes)
--------------------------------

.. reference::

   :Tool:      Select Tools
   :Panel:     :menuselection:`Tool Settings --> Mode`

ឧបករណ៍ជ្រើសរើសនីមួយៗក្នុង Toolbar មានរបៀបមួយដើម្បីកំណត់
ពីរបៀបដែលវាធ្វើអន្តរកម្មជាមួយការជ្រើសរើសដែលមានស្រាប់។
ចំណាំថា មិនមែនឧបករណ៍ទាំងអស់គាំទ្ររបៀបទាំងអស់នេះទេ។

Set
   កំណត់ការជ្រើសរើសថ្មី (ការជ្រើសរើសមុនត្រូវបានបោះបង់)។ នេះគឺជាលំនាំដើម។
Extend
   បន្ថែមធាតុដែលបានជ្រើសថ្មីទៅការជ្រើសរើសដែលមានស្រាប់។
Subtract
   ដកធាតុដែលបានជ្រើសថ្មីចេញពីការជ្រើសរើសដែលមានស្រាប់។
Invert :kbd:`Ctrl-I`
   បញ្ច្រាសការជ្រើសរើស (ធាតុដែលមិនបានជ្រើសក្លាយជាបានជ្រើស ហើយផ្ទុយមកវិញ)។
Intersect
   ជ្រើសរើសធាតុដែលប្រសព្វជាមួយការជ្រើសរើសដែលមានស្រាប់។


ឧបករណ៍ជ្រើសរើសក្នុងម៉ឺនុយ
===========================

ឧបករណ៍ទាំងនេះគឺជាទម្រង់របស់ឧបករណ៍ដែលបានពណ៌នាពីមុន។
វាមាននៅក្នុងម៉ឺនុយជំនួសឱ្យ Toolbar ហើយដំណើរការខុសគ្នាបន្តិច។


.. _bpy.ops.*.select_box:

Box Select
----------

.. reference::

   :Menu:      :menuselection:`Select --> Box Select`
   :Shortcut:  :kbd:`B`

ដើម្បីប្រើឧបករណ៍នេះ ដំបូងអ្នកបើកធាតុម៉ឺនុយ ឬផ្លូវកាត់ក្ដារចុច
បន្ទាប់មកអូសប្រអប់ដូចធម្មតា។ ខុសពី *Select Box* ឥរិយាបថលំនាំដើមនៅទីនេះ
គឺបន្ថែមធាតុក្នុងប្រអប់ទៅការជ្រើសរើស។
(ធាតុខាងក្រៅប្រអប់មិនត្រូវបានបោះបង់ការជ្រើសរើសទេ។)

ដើម្បីដកធាតុក្នុងប្រអប់ចេញពីការជ្រើសរើស
សូមសង្កត់ :kbd:`Shift` ឬអូសដោយ :kbd:`MMB` វិញ។

ខណៈពេលអូស អ្នកអាចសង្កត់ :kbd:`Spacebar` បន្ថែម ដើម្បីផ្លាស់ទីប្រអប់ដោយកណ្ដុរ។


.. _bpy.ops.*.select_circle:

Circle Select
-------------

.. reference::

   :Menu:      :menuselection:`Select --> Circle Select`
   :Shortcut:  :kbd:`C`

ដើម្បីប្រើឧបករណ៍នេះ ដំបូងអ្នកបើកធាតុម៉ឺនុយ ឬផ្លូវកាត់ក្ដារចុច
បន្ទាប់មកអូសរង្វង់ដូចធម្មតា។ ខុសពី *Select Circle* ឥរិយាបថលំនាំដើមនៅទីនេះ
គឺបន្ថែមធាតុក្នុងរង្វង់ទៅការជ្រើសរើស។
(ធាតុខាងក្រៅរង្វង់មិនត្រូវបានបោះបង់ការជ្រើសរើសទេ។)

ដើម្បីដកធាតុក្នុងរង្វង់ចេញពីការជ្រើសរើស
សូមសង្កត់ :kbd:`Shift` ឬអូសដោយ :kbd:`MMB` វិញ។

អ្នកអាចផ្លាស់ប្ដូរកាំរបស់រង្វង់ដោយរំកិល :kbd:`Wheel`
ឬប្រើគ្រាប់ចុច :kbd:`NumpadPlus` និង :kbd:`NumpadMinus`។

បន្ទាប់ពីបានបើក *Circle Select* នៅតែសកម្ម៖ អ្នកអាចលែងប៊ូតុងកណ្ដុរ
ហើយចាប់ផ្ដើមអូសនៅកន្លែងផ្សេង ដោយមិនចាំបាច់ចុច :kbd:`C` ម្ដងទៀត។
ប៉ុន្តែក្នុងពេលជាមួយគ្នា វាទប់ស្កាត់ផ្នែកផ្សេងទៀតទាំងអស់របស់ Blender ខណៈដែលវាសកម្ម។
ដើម្បីបិទឧបករណ៍នេះវិញ សូមចុច :kbd:`RMB`, :kbd:`Return` ឬ :kbd:`Esc`។


.. _bpy.ops.*.select_lasso:

Lasso Select
------------

.. reference::

   :Menu:      :menuselection:`Select --> Lasso Select`
   :Shortcut:  :kbd:`Ctrl-RMB`

ដើម្បីប្រើឧបករណ៍នេះ ដំបូងអ្នកបើកធាតុម៉ឺនុយ ហើយអូសរូបរាងសេរី
ជុំវិញធាតុដែលអ្នកចង់ជ្រើសរើសដោយ :kbd:`LMB`។ ម៉ឺនុយអនុញ្ញាតឱ្យអ្នកជ្រើសរើស
ថាតើត្រូវកំណត់ (set) ពង្រីក (extend) ឬបន្ថយ (reduce) ការជ្រើសរើស។

ជាជម្រើស អ្នកអាចចាប់ផ្ដើមអូសភ្លាមៗដោយ :kbd:`Ctrl-RMB`។
ខុសពី *Select Lasso* ឥរិយាបថលំនាំដើមបន្ទាប់មក គឺបន្ថែមធាតុក្នុង lasso
ទៅការជ្រើសរើស។ (ធាតុខាងក្រៅ lasso មិនត្រូវបានបោះបង់ការជ្រើសរើសទេ។)

ដើម្បីដកធាតុក្នុង lasso ចេញពីការជ្រើសរើស
សូមអូសដោយ :kbd:`Shift-Ctrl-RMB` វិញ។

ខណៈពេលអូស អ្នកអាចសង្កត់ :kbd:`Spacebar` បន្ថែម ដើម្បីផ្លាស់ទី lasso ដោយកណ្ដុរ។

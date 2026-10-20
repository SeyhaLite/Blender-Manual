###################################################
  ការកំណត់ឧបករណ៍បញ្ចូល (Configuring Peripherals)
###################################################

អេក្រង់
========

អេក្រង់ Full HD (1920x1080) ឬខ្ពស់ជាងនេះ ត្រូវបានណែនាំ។
ការរៀបចំអេក្រង់ច្រើន (multi-monitor) ត្រូវបានគាំទ្រ ហើយតំបន់ការងារ (workspace)
អាចត្រូវបានកំណត់ឱ្យលាតសន្ធឹងលើអេក្រង់ច្រើន។

.. figure:: /images/getting-started_configuration_hardware_multi-monitor.jpg

   ឧទាហរណ៍នៃការគាំទ្រអេក្រង់ច្រើនរបស់ Blender។


ឧបករណ៍បញ្ចូល
==============

Blender គាំទ្រឧបករណ៍បញ្ចូលជាច្រើនប្រភេទ៖

- ក្ដារចុច (ណែនាំ៖ ក្ដារចុចដែលមានផ្ទាំងលេខ ប្លង់អង់គ្លេសដំណើរការល្អបំផុត)
- កណ្ដុរ (ណែនាំ៖ កណ្ដុរបីប៊ូតុងដែលមានកង់រំកិល)
- Graphic Tablet
- Touchpad
- ឧបករណ៍ NDOF (ហៅផងដែរថា *កណ្ដុរ 3D*)

.. note::

   ប្រសិនបើអ្នកគ្មានប៊ូតុងកណ្ដុរកណ្ដាល ឬផ្ទាំងលេខ អ្នកអាចក្លែងធ្វើវាក្នុង
   `Input Preferences <https://docs.blender.org/manual/en/5.2/editors/preferences/input.html>`__។
   ប៉ុន្តែសូមដឹងថា ការក្លែងធ្វើទាំងនេះអាចបណ្ដាលឱ្យបាត់បង់ផ្លូវកាត់គ្រាប់ចុចខ្លះ។
   នៅកន្លែងដែលអាចធ្វើបាន គេណែនាំឱ្យប្រើផ្នែករឹងដែលបានណែនាំ។


កណ្ដុរ
--------

អន្តរកម្មជាច្រើនរបស់ Blender ប្រើប៊ូតុងកណ្ដាល (ចុចកង់រំកិល) ឬប្រើកង់រំកិល។
នេះជាមូលហេតុដែលការណែនាំសម្រាប់កណ្ដុរគឺ កណ្ដុរពីរប៊ូតុងដែលមានកង់រំកិលបន្ថែម
ដែលដើរតួជាប៊ូតុងកណ្ដាល (ជាក់ស្ដែងគឺកណ្ដុរបីប៊ូតុង)។
នេះនឹងអនុញ្ញាតឱ្យមានលំហូរការងារប្រសិទ្ធភាពបំផុតនៅក្នុងម៉ូឌុលទាំងអស់របស់ Blender។

ការក្លែងធ្វើប៊ូតុងកណ្ដុរ
^^^^^^^^^^^^^^^^^^^^^^^^^^^

ប្រសិនបើអ្នកគ្មានកណ្ដុរបីប៊ូតុង អ្នកនឹងត្រូវក្លែងធ្វើវាដោយធីកជម្រើសនៅក្នុង
`Preferences <https://docs.blender.org/manual/en/5.2/editors/preferences/input.html>`__។

តារាងខាងក្រោមបង្ហាញបន្សំដែលបានប្រើ៖

.. list-table::
   :stub-columns: 1

   * - កណ្ដុរ ៣ ប៊ូតុង
     - :kbd:`LMB`
     - :kbd:`MMB`
     - :kbd:`RMB`
   * - កណ្ដុរ ២ ប៊ូតុង
     - :kbd:`LMB`
     - :kbd:`Alt-LMB`
     - :kbd:`RMB`


ក្ដារចុច
----------

អន្តរកម្មជាច្រើនរបស់ Blender ប្រើផ្ទាំងលេខរបស់ក្ដារចុច (numpad)។
នេះគឺជាសំណុំគ្រាប់ចុចលេខ ១០ បូកនឹងអនុគមន៍គណិតវិទ្យា ដែលលេចឡើងនៅផ្នែកខាងស្ដាំនៃ
`ក្ដារចុចទំហំពេញ ១០៤ គ្រាប់តាមបែបប្រពៃណី <https://en.wikipedia.org/wiki/Keyboard_layout#/media/File:Qwerty.svg>`__។
នេះនឹងអនុញ្ញាតឱ្យមានលំហូរការងារប្រសិទ្ធភាពបំផុតនៅក្នុងម៉ូឌុលទាំងអស់របស់ Blender។

ការក្លែងធ្វើផ្ទាំងលេខ (Numpad Emulation)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ប្រសិនបើអ្នកគ្មានផ្ទាំងលេខនៅខាងក្ដារចុចរបស់អ្នក អ្នកប្រហែលជាចង់ក្លែងធ្វើមួយ។
បន្ទាប់មកអ្នកអាចប្រើជួរលេខនៅផ្នែកខាងលើនៃក្ដារចុចជំនួសវិញ
ប៉ុន្តែនឹងលែងមានសិទ្ធិចូលប្រើមុខងារដើមរបស់គ្រាប់ចុចទាំងនោះ
(ដូចជាការប្ដូររវាងការជ្រើសរើស vertex/edge/face ក្នុង Edit Mode)។

.. seealso::

   អានបន្ថែមអំពី *Numpad Emulation* ក្នុង
   `Preferences <https://docs.blender.org/manual/en/5.2/editors/preferences/input.html>`__។


ក្ដារចុចដែលមិនមែនជាអង់គ្លេស
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ប្រសិនបើអ្នកប្រើក្ដារចុចដែលមានប្លង់មិនមែនអង់គ្លេស អ្នកនៅតែអាចទទួលបានអត្ថប្រយោជន៍
ពីការប្ដូរទៅប្លង់ UK ឬ US ខណៈពេលធ្វើការជាមួយ Blender។

.. note::

   អ្នកក៏អាចផ្លាស់ប្ដូរ keymap ពី
   `Preferences <https://docs.blender.org/manual/en/5.2/editors/preferences/input.html>`__ បានដែរ។
   ទោះជាយ៉ាងណា សៀវភៅណែនាំនេះសន្មតថាអ្នកកំពុងប្រើ keymap លំនាំដើម។


.. _hardware-touch:

អេក្រង់ប៉ះ (Touch Screens)
---------------------------

Blender មានការកំណត់ជាច្រើនដែលអាចបើកបាន ដើម្បីធ្វើឱ្យបទពិសោធន៍លើឧបករណ៍ប៉ះប្រសើរឡើង។
ជម្រើសទាំងនេះធ្វើឱ្យវាកាន់តែងាយស្រួលក្នុងការគ្រប់គ្រងតំបន់ (area) ម៉ឺនុយ
និងអន្តរកម្ម ដោយមិនពឹងផ្អែកលើការបញ្ចូលពីកណ្ដុរយ៉ាងជាក់លាក់។

- បើក :ref:`Show Handles <bpy.types.PreferencesView.show_area_handle>`
  ដើម្បីធ្វើឱ្យការប្ដូរទំហំ និងរៀបចំ :doc:`តំបន់ </interface/window_system/areas>` ឡើងវិញងាយស្រួល។
- បង្កើន :ref:`Border Width <bpy.types.PreferencesView.border_width>`
  ដើម្បីធ្វើឱ្យគែមតំបន់ងាយស្រួលជ្រើសរើសដោយម្រាមដៃ។


.. _hardware-tablet:

Graphic Tablet
--------------

Graphic tablet អាចប្រើដើម្បីផ្ដល់វិធីគ្រប់គ្រងទ្រនិចកណ្ដុរតាមបែបប្រពៃណីជាង ដោយប្រើប៊ិច។
នេះអាចជួយផ្ដល់បទពិសោធន៍ដែលស្គាល់ច្បាស់ជាង សម្រាប់សិល្បករដែលធ្លាប់លាបពណ៌ និងគូរ
ដោយឧបករណ៍ស្រដៀងគ្នា ព្រមទាំងផ្ដល់ការគ្រប់គ្រងបន្ថែម ដូចជាភាពរសើបចំពោះសម្ពាធ (pressure sensitivity)។

.. note::

   ប្រសិនបើអ្នកកំពុងប្រើ graphic tablet ជំនួសកណ្ដុរ ហើយភាពរសើបចំពោះសម្ពាធមិនដំណើរការត្រឹមត្រូវ
   សូមព្យាយាមដាក់ទ្រនិចកណ្ដុរក្នុងបង្អួច Blender បន្ទាប់មកផ្ដាច់/ភ្ជាប់ graphic tablet របស់អ្នកឡើងវិញ។
   នេះអាចជួយបាន។


.. _hardware-ndof:

Touchpad
--------

ការគ្រប់គ្រង touchpad មាននៅលើ Windows, macOS និង Linux ជាមួយ Wayland។
ប្រសិនបើអ្នកធ្វើការពីកុំព្យូទ័រយួរដៃដែលគ្មានកណ្ដុរ អ្នកអាចក្លែងធ្វើការគ្រប់គ្រង
ដោយប្រើកាយវិការ multi-touch ជាមួយ trackpad ពី
`Preferences <https://docs.blender.org/manual/en/5.2/editors/preferences/input.html>`__។

.. list-table:: កាយវិការ multi-touch ដែលគាំទ្រ
   :header-rows: 1

   * - កាយវិការ
     - លទ្ធផល
   * - Pan (រំកិល)
     - សង្កត់គ្រាប់ចុច :kbd:`Shift` ខណៈពេលអូសម្រាមដៃពីរលើ pad។
   * - Zoom (ពង្រីក/បង្រួម)
     - សង្កត់គ្រាប់ចុច :kbd:`Ctrl` ឬ :kbd:`OSKey` ខណៈពេលអូសម្រាមដៃពីរលើ pad។
   * - Orbit (បង្វិល)
     - អូសម្រាមដៃពីរលើ pad។
   * - ក្លែងធ្វើការចុចប៊ូតុងស្ដាំ
     - ប៉ះម្រាមដៃពីរលើ pad។

NDOF (កណ្ដុរ 3D)
------------------

កណ្ដុរ 3D ឬឧបករណ៍ :abbr:`NDOF (N-Degrees of Freedom)` គឺជាផ្នែករឹង
ដែលអ្នកអាចប្រើដើម្បីរុករកឆាកក្នុង Blender។ បច្ចុប្បន្នមានតែឧបករណ៍
ដែលផលិតដោយ 3Dconnexion ប៉ុណ្ណោះដែលត្រូវបានគាំទ្រ ដូចជា SpaceMouse™។
ឧបករណ៍ទាំងនេះអនុញ្ញាតឱ្យអ្នកស្វែងយល់ឆាក និងធ្វើឱ្យ
`ការរុករក Fly/Walk <https://docs.blender.org/manual/en/5.2/editors/3dview/navigate/walk_fly.html#dview-fly-walk>`__
ងាយស្រួលគ្រប់គ្រង។ ឧបករណ៍ NDOF អាចត្រូវបានកំណត់ក្នុង
`Preferences <https://docs.blender.org/manual/en/5.2/editors/preferences/input.html#editors-preferences-input-ndof>`__។
ការកំណត់ទាំងនេះក៏អាចចូលដំណើរការបានដោយផ្ទាល់ពី viewport
ដោយប្រើប៊ូតុង :kbd:`NDOFMenu` នៅលើឧបករណ៍ NDOF។

.. seealso::

   សូមមើល `Input Preference <https://docs.blender.org/manual/en/5.2/editors/preferences/input.html>`__
   សម្រាប់ព័ត៌មានបន្ថែមអំពីការកំណត់ឧបករណ៍បញ្ចូល។


.. _hardware-head-mounted-displays:

Head-Mounted Display (Virtual Reality)
======================================

:abbr:`HMD (Head-Mounted Display)` ធ្វើឱ្យវាអាចដាក់អ្នកប្រើក្នុងបរិស្ថាននិម្មិត
ដែលមានអន្តរកម្ម។ វាត្រូវបានពាក់នៅលើក្បាល ហើយតាមដានចលនាក្បាល
ដើម្បីបញ្ចាំងពិភពលោកដែលហាក់ដូចជាព័ទ្ធជុំវិញ ទៅលើអេក្រង់តូចៗនៅមុខភ្នែកអ្នកប្រើ។
ប្រសិនបើប្រព័ន្ធដំណើរការល្អ ពួកគេមានបទពិសោធន៍បរិស្ថាននិម្មិត
ដូចជាពួកគេពិតជានៅខាងក្នុងវា។


ប្រព័ន្ធដែលគាំទ្រ
------------------

ការគាំទ្រ virtual reality ក្នុង Blender ត្រូវបានអនុវត្តតាមរយៈស្តង់ដារ OpenXR ដែលមានច្រើនប្រព័ន្ធ។
ស្តង់ដារនេះថ្មី ដូច្នេះការគាំទ្រសម្រាប់វានៅតែមានកម្រិត។

.. list-table:: ប្រព័ន្ធឆបគ្នានឹង OpenXR។
   :header-rows: 1

   * - ប្រព័ន្ធ
     - ប្រព័ន្ធប្រតិបត្តិការ
     - ចំណាំ
   * - `HTC Vive Cosmos`_
     - Windows
     - `Developer Preview <https://forum.htc.com/topic/9046-vive-openxr-support-for-vive-cosmos/>`__
   * - `HTC Vive Focus 3`_
     - Windows
     - `Developer Preview <https://forum.htc.com/topic/9876-focus-3-openxr-support-status/page/3/>`__
   * - `Monado`_
     - GNU/Linux
     - *មិនទាន់* ត្រូវបានណែនាំសម្រាប់ការប្រើទូទៅទេ។
   * - `Meta (formerly Oculus)`_ (Rift និង Quest)
     - Windows
     - ត្រូវការ Oculus v31 Software Update។ Quest ត្រូវការ Oculus Link។
   * - `SteamVR`_
     - Windows, GNU/Linux
     - ត្រូវការ SteamVR 1.16 ឬខ្ពស់ជាង។
   * - `Varjo`_
     - Windows
     - --
   * - `Windows Mixed Reality`_
     - Windows
     - ត្រូវការ Windows 10 May 2019 Update (1903)។


ការចាប់ផ្ដើម
-------------

ផ្នែករងខាងក្រោមពណ៌នាពីរបៀបរៀបចំ HMD សម្រាប់ប្រើជាមួយ `ប្រព័ន្ធដែលគាំទ្រ`_។
ប្រសិនបើមិនបានធ្វើដូច្នេះទេ Blender នឹងរាយការណ៍កំហុសនៅពេលព្យាយាមចាប់ផ្ដើមវគ្គ virtual reality។


HTC Vive Cosmos
^^^^^^^^^^^^^^^

វេទិកាសម្រេចសម្រាប់ `HTC Vive Cosmos <https://www.vive.com/sea/product/#vive%20cosmos>`__
បច្ចុប្បន្នមានគោលដៅលើអ្នកអភិវឌ្ឍន៍ ហើយអាចខ្វះមុខងារដែលមានក្នុងវេទិកាផ្សេងទៀត។

- អនុវត្តតាមជំហានពី
  `Vive Developer Forums <https://forum.htc.com/topic/9046-vive-openxr-support-for-vive-cosmos/>`__។
- បើក `VR Scene Inspection add-on <https://docs.blender.org/manual/en/5.2/addons/vr_scene_inspection.html>`__
  ក្នុង Blender។


HTC Vive Focus 3
^^^^^^^^^^^^^^^^

វេទិកាសម្រេចសម្រាប់ `HTC Vive Focus 3 <https://www.vive.com/eu/product/vive-focus3/overview/>`__
បច្ចុប្បន្នមានគោលដៅលើអ្នកអភិវឌ្ឍន៍ ហើយអាចខ្វះមុខងារដែលមានក្នុងវេទិកាផ្សេងទៀត។

- អនុវត្តតាមជំហានពី
  `Vive Developer Forums <https://forum.htc.com/topic/9876-focus-3-openxr-support-status/page/3/>`__។
- បើក `VR Scene Inspection add-on <https://docs.blender.org/manual/en/5.2/addons/vr_scene_inspection.html>`__
  ក្នុង Blender។


Monado
^^^^^^

`Monado <https://monado.dev/>`__ គឺជាវេទិកា XR
:doc:`សេរី និងមានប្រភពបើកចំហ </getting_started/about/license>` សម្រាប់ Linux។
វាមិនទាន់រួចរាល់សម្រាប់ការប្រើប្រាស់ផលិតកម្មទេ ហើយគួរប្រើតែសម្រាប់គោលបំណងសាកល្បង។

- កញ្ចប់មានសម្រាប់ distribution ខាងក្រោម៖

  - Ubuntu (`Eoan, Focal <https://launchpad.net/~monado-xr/+archive/ubuntu/monado>`__)
  - Debian (`bullseye <https://packages.debian.org/bullseye/libopenxr1-monado>`__,
    `sid <https://packages.debian.org/sid/libopenxr1-monado>`__)

  សម្រាប់ប្រព័ន្ធផ្សេងទៀត វាត្រូវតែ compile ពីប្រភព ដែលក្នុងករណីនេះមិនត្រូវបានណែនាំ
  សម្រាប់អ្នកដែលមានបទពិសោធន៍តិចក្នុងការ compile កម្មវិធីទេ។
  ទោះជាយ៉ាងណា សូមអនុវត្តតាម
  `Getting Started Guides <https://gitlab.freedesktop.org/monado/monado/-/blob/main/README.md>`__
  របស់ Monado ដើម្បីធ្វើវា។
- បើក `VR Scene Inspection add-on <https://docs.blender.org/manual/en/5.2/addons/vr_scene_inspection.html>`__
  ក្នុង Blender។


Meta (formerly Oculus)
^^^^^^^^^^^^^^^^^^^^^^

`Meta (formerly Oculus) <https://www.meta.com/quest/>`__ ផ្ដល់ការគាំទ្រ OpenXR ពេញលេញ
ចាប់ពី Oculus v31 Software Update។

- ទាញយក និងដំឡើង `Oculus Rift/Oculus Link software <https://www.meta.com/quest/setup/>`__។
- កំណត់ Oculus ជា OpenXR runtime សកម្ម តាមរយៈផ្ទាំង *General* ក្នុងការកំណត់ Oculus App។

.. figure:: /images/getting-started_configuration_hardware_xr_runtime_oculus.jpg
   :scale: 50 %

- បើក `VR Scene Inspection add-on <https://docs.blender.org/manual/en/5.2/addons/vr_scene_inspection.html>`__
  ក្នុង Blender។

.. admonition:: ការគាំទ្រ Passthrough
   :class: note

   បច្ចុប្បន្ន ការគាំទ្រ passthrough លើ OpenXR ត្រូវបានបិទតាមលំនាំដើមក្នុងកម្មវិធី Quest Link
   ហើយត្រូវតែបើកដោយដៃក្នុងការកំណត់របស់វា ដើម្បីប្រើមុខងារនេះ។

   ដំណើរការនៃការ render passthrough ប្រែប្រួលទៅតាមគុណភាពនៃការតភ្ជាប់
   រវាង headset និងកុំព្យូទ័រ។ ដើម្បីលទ្ធផលល្អជាង គេណែនាំឱ្យភ្ជាប់ headset
   ដោយផ្ទាល់តាមរយៈ USB ទៅ PC ឬយ៉ាងហោចណាស់ភ្ជាប់កុំព្យូទ័រទៅបណ្ដាញមូលដ្ឋានតាម Ethernet។


SteamVR
^^^^^^^

`SteamVR <https://www.steamvr.com/en/>`__ ផ្ដល់ការគាំទ្រ OpenXR ពេញលេញចាប់ពី SteamVR 1.16។

- កំណត់ SteamVR ជា OpenXR runtime សកម្ម តាមរយៈផ្ទាំង *Developer* ក្នុងការកំណត់ SteamVR។

.. figure:: /images/getting-started_configuration_hardware_xr_runtime_steamvr.jpg
   :scale: 50 %

- បើក `VR Scene Inspection add-on <https://docs.blender.org/manual/en/5.2/addons/vr_scene_inspection.html>`__
  ក្នុង Blender។

.. note::

   SteamVR runtime ក៏អាចប្រើសម្រាប់ HMD របស់ HTC Vive Cosmos, Oculus
   និង Windows Mixed Reality ផងដែរ។


Varjo
^^^^^

`Varjo <https://varjo.com/>`__ រួមបញ្ចូលការគាំទ្រ OpenXR ពេញលេញ
ជាមួយកម្មវិធី Varjo Base ដែលចាំបាច់របស់វា។

- បើក `VR Scene Inspection add-on <https://docs.blender.org/manual/en/5.2/addons/vr_scene_inspection.html>`__
  ក្នុង Blender។


Windows Mixed Reality
^^^^^^^^^^^^^^^^^^^^^

`Windows Mixed Reality <https://www.microsoft.com/windows/windows-mixed-reality>`__
ផ្ដល់ការគាំទ្រ OpenXR ពេញលេញ។ ដើម្បីពិនិត្យថាតើ PC មួយបំពេញតម្រូវការ
ក្នុងការដំណើរការកម្មវិធីនេះឬអត់ Microsoft ផ្ដល់កម្មវិធី
`Windows Mixed Reality PC Check <https://www.microsoft.com/en-us/p/windows-mixed-reality-pc-check/9nzvl19n7cnc>`__។

- សូមប្រាកដថា Windows 10 May 2019 Update (1903) បានដំឡើងរួច។
- ប្រសិនបើប្រព័ន្ធបំពេញតម្រូវការទាំងអស់ Mixed Reality Portal គួរតែបានដំឡើងរួចហើយ។
  វាក៏មាននៅក្នុង `Microsoft Store <https://apps.microsoft.com/detail/9ng1h8b3zc7m>`__ ដែរ។
- បើក Mixed Reality Portal។ ចុចប៊ូតុងម៉ឺនុយ ``...`` នៅជ្រុងខាងឆ្វេងផ្នែកខាងក្រោម។
  ក្នុងម៉ឺនុយដែលវាបើក សូមជ្រើសរើស *Set up OpenXR*។
- បើក `VR Scene Inspection add-on <https://docs.blender.org/manual/en/5.2/addons/vr_scene_inspection.html>`__
  ក្នុង Blender។

.. note::

   ដើម្បីប្ដូរទៅ Windows Mixed Reality ពី OpenXR runtime ផ្សេង (ឧទាហរណ៍ SteamVR)
   សូមទាញយក OpenXR Developer Tools ពី
   `Microsoft Store <https://www.microsoft.com/en-us/p/openxr-developer-tools-for-windows-mixed-reality/9n5cvvl23qbt>`__
   ហើយកំណត់ Windows Mixed Reality ជា runtime សកម្ម។

.. figure:: /images/getting-started_configuration_hardware_xr_runtime_wmr.jpg
   :scale: 50 %

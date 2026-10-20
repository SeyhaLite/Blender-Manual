:orphan:

.. _linux-windowing-environment:

########################################################
  បរិស្ថានបង្អួចរបស់ Linux (Linux Windowing Environment)
########################################################

នៅលើ Linux Blender គាំទ្រទាំង X11 និង Wayland សម្រាប់ការចេញផ្សាយផ្លូវការ។

នៅពេលដែល Wayland ត្រូវបានរកឃើញ វាជាប្រព័ន្ធដែលត្រូវបានពេញចិត្ត បើមិនដូច្នោះទេ X11 នឹងត្រូវបានប្រើ។

.. hint::

   បរិស្ថានបង្អួចបច្ចុប្បន្នត្រូវបានរាយក្នុង
   :menuselection:`Topbar --> Blender --> About Blender`។


X11
===

នេះគឺជាបរិស្ថានបង្អួចដែលត្រូវបានប្រើយ៉ាងទូលំទូលាយបំផុតជាប្រវត្តិសាស្ត្រ
នៅលើប្រព័ន្ធ Linux និង Unix។

មិនមានផែនការក្នុងពេលឆាប់ៗនេះ ដើម្បីបោះបង់ ឬដកការគាំទ្រ X11 ចោលទេ។


Wayland
=======

ការគាំទ្រ Wayland គឺជាការបន្ថែមថ្មីជាង ដូច្នេះអាចមានការកំណត់រចនាសម្ព័ន្ធខ្លះ
ដែលមិនទាន់បានសាកល្បង។ សូម
`រាយការណ៍កំហុស <https://docs.blender.org/manual/en/5.2/troubleshooting/report_bug.html>`__
ប្រសិនបើអ្នកជួបបញ្ហា។

Blender ត្រូវបានសាកល្បងជាមួយ compositor ដែលផ្អែកលើ Gnome-Shell (mutter), KDE (plasma)
និង SWAY (wlroots)។


ការដោះស្រាយបញ្ហា
------------------

ទិន្នផល Wayland លម្អិតអាចជួយតាមដានបញ្ហា។ បើក Blender ពី
`បន្ទាត់ពាក្យបញ្ជា <https://docs.blender.org/manual/en/5.2/advanced/command_line/launch/linux.html>`__
ជាមួយអាគុយម៉ង់បន្ថែម៖

ការកត់ត្រា Wayland របស់ Blender
   .. code-block:: sh

      blender --log "ghost.wl.*" --log-level 2

ការកត់ត្រាដែលមានស្រាប់របស់ Wayland
   .. code-block:: sh

      WAYLAND_DEBUG=1 blender

បិទ Wayland (បង្ខំឱ្យប្រើ X11)
   .. code-block:: sh

      WAYLAND_DISPLAY="" blender


អថេរបរិស្ថាន (Environment Variables)
----------------------------------------

``XCURSOR_THEME``
   រូបរាងទ្រនិច (cursor theme) ដែលត្រូវប្រើ (ត្រូវតែយោងទៅរូបទ្រនិចដែលបានដំឡើងក្នុងម៉ាស៊ីន)។

``XCURSOR_SIZE``
   ទំហំទ្រនិច លំនាំដើមគឺ 28។ អ្នកប្រហែលជាចង់បង្កើនទំហំនៅលើអេក្រង់ Hi-DPI។


ដែនកំណត់ដែលបានដឹង
---------------------

Fractional Scaling របស់ Gnome Shell (មុនកំណែ 44)
   Gnome-Shell កំណែមុន 44 មិនគាំទ្រ fractional scaling ពេញលេញទេ។

   ការប្រើ fractional ក្រោម Gnome-Shell កំណែចាស់អាចបណ្ដាលឱ្យមានកំហុសបង្ហាញ
   ដូចជា `ទំហំទ្រនិចតូច <https://projects.blender.org/blender/blender/issues/105895>`__។

NVIDIA GPU
   បច្ចុប្បន្ន កម្មវិធីបញ្ជា (driver) របស់ NVIDIA មិនគាំទ្រពេញលេញនូវមុខងារ
   ដែល Wayland ត្រូវការទេ។ កំហុសក្រាហ្វិក និងការភ្លឹបភ្លែតៗ (flickering) គឺជាបញ្ហាទូទៅ។
   ក្នុងករណីខ្លះ អាចមាន `ការគាំងនៅពេលចាប់ផ្ដើម
   <https://projects.blender.org/blender/blender/issues/103999>`__។
   នេះមិនមែនជាបញ្ហាជាក់លាក់របស់ Blender ទេ ដូច្នេះអ្នកប្រើ NVIDIA
   ប្រហែលជាចង់ប្រើ X11 រហូតដល់ការគាំទ្ររបស់ driver ប្រសើរឡើង។

----


ការប្រៀបធៀបមុខងារ
==================

.. |tick|  unicode:: U+2713
.. |cross| unicode:: U+2717
.. |none|  unicode:: U+2014

.. list-table::
   :header-rows: 1
   :class: valign
   :widths: 30 5 5 60

   * - មុខងារ
     - X11
     - Wayland
     - ចំណាំ
   * - ការរំកិលរលូន (Smooth Scroll)
     - |cross|
     - |tick|
     - | ការរំកិលរលូនជាមួយ track-pad។
   * - កាយវិការ Multi-Touch
     - |cross|
     - |tick|
     - | ការគាំទ្រ track-pad និង tablet សម្រាប់
       | ការច្របាច់ដើម្បីពង្រីក (pinch to zoom) រំកិល និងបង្វិល។
   * - Cursor Warping ដែលអាចទុកចិត្តបាន
     - |cross| :sup:`*1`
     - |tick|
     - | Cursor warping ត្រូវបានប្រើខណៈពេលកែប្រែ (transform)
       | និងបង្វិល viewport ជាដើម។
   * - ការកំណត់ទីតាំងបង្អួច
     - |tick|
     - |cross| :sup:`*2`
     - | ចាំបាច់សម្រាប់ការអូសរវាងបង្អួច និង
       | ការស្ដារទីតាំងបង្អួចនៅពេលផ្ទុកឯកសារ។

មុខងារផ្សេងទៀតដែលប្រព័ន្ធទាំងពីរគាំទ្រ ដូចជា Hi-DPI, កណ្ដុរ 3D, ការបញ្ចូលពី tablet ជាដើម
ត្រូវបានទុកចោលពីបញ្ជីនេះ។

| :sup:`*1` ក្នុង X11 ចលនាទ្រនិចលឿនអាចចេញពីព្រំដែនបង្អួច ខណៈដែលទ្រនិចត្រូវបានចាប់យក
  (ឧទាហរណ៍ ក្នុងពេល transform)។
| :sup:`*2` Wayland មិនគាំទ្រការកំណត់ទីតាំងបង្អួចទេ ដោយសារវាជាការសម្រេចចិត្តផ្នែករចនា
  ដូច្នេះវាទំនងជាមិនត្រូវបានគាំទ្រទេ (សូមមើល issue សម្រាប់
  `ទីតាំង <https://projects.blender.org/blender/blender/issues/98928>`__)។

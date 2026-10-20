# Configuration file for the Khmer (ភាសាខ្មែរ) translation of the Blender Manual.
#
# Derived from the official Blender Manual ``manual/conf.py``
# (https://projects.blender.org/blender/blender-manual, branch ``blender-v5.2-release``).
# Content is licensed CC-BY-SA 4.0 International; see LICENSE and manual/copyright.rst.
#
# For a full list of options see:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join("..", "build_files", "extensions")))

# Sphinx errors out on single threaded builds, see upstream T86621.
sys.setrecursionlimit(2000)


def has_module(module_name):
    found = False
    try:
        __import__(module_name)
        found = True
    except ModuleNotFoundError as ex:
        if ex.name != module_name:
            raise ex
    return found


# -- Local Vars --------------------------------------------------------------

# Blender version this translation is pinned to.
# Must match the upstream branch the sources were taken from
# (``blender-v5.2-release`` == https://docs.blender.org/manual/en/latest/).
blender_version = "5.2"
blender_version_label = "5.2 LTS"

# Upstream revision the translation was synchronised against.
upstream_branch = "blender-v5.2-release"
upstream_commit = "4a3be8f9ed3b66b24913e0a0d491d3429a70ea08"
# Canonical English manual this translation refers back to for untranslated pages.
english_manual_url = "https://docs.blender.org/manual/en/{:s}".format(blender_version)

# Used by the km_xref_fallback extension.
km_english_manual_url = english_manual_url
km_upstream_labels = "_data/upstream_labels.json"

# -- Project information -----------------------------------------------------

project = "Blender {:s} Manual — ភាសាខ្មែរ".format(blender_version_label)
copyright = ": This page is licensed under a CC-BY-SA 4.0 Int. License"
author = "Blender Documentation Team / Khmer Translation Contributors"

version = blender_version
release = blender_version


# -- General configuration ---------------------------------------------------

extensions = [
    # Vendored from upstream, required by the translated pages.
    "icons",
    "reference",
    # Resolves :ref:`bpy.*` and :doc: targets that live on pages which are not
    # translated yet, by linking them to the official English manual.
    "km_xref_fallback",
    "sphinx.ext.mathjax",
    "sphinx.ext.todo",
]

# Provides a copy button next to code-blocks (nice to have but not essential).
if has_module("sphinx_copybutton"):
    extensions.append("sphinx_copybutton")
    copybutton_exclude = ".linenos, .gp, .go"

# Intersphinx performs online access, so make it opt-out for offline builds.
if not os.environ.get("NO_INTERSPHINX", "").strip("0"):
    extensions.append("sphinx.ext.intersphinx")

if "latex" in sys.argv:
    extensions.append("sphinx.ext.imgconverter")
    image_converter = "magick"

# A string of reStructuredText included at the end of every source file.
# Substitutions available on every page.
rst_epilog = """
.. |BLENDER_VERSION| replace:: {:s}
.. |BLENDER_VERSION_LABEL| replace:: {:s}
.. |KM_EN_MANUAL| replace:: {:s}
.. |TODO| replace:: ផ្នែកនេះមិនទាន់បានបកប្រែពេញលេញទេ។ សូមអានជាភាសាអង់គ្លេសនៅ |KM_EN_MANUAL| ឬជួយបកប្រែតាម :doc:`ការណែនាំសម្រាប់អ្នកចូលរួម </appendix/contributing>`.
""".format(blender_version, blender_version_label, english_manual_url)

needs_sphinx = "7.0"

highlight_language = "python3"

numfig = False
numfig_secnum_depth = 0

# Khmer has no ASCII-style quotation conventions and smart quotes mangle
# the ``“ ”`` pairs that upstream RST relies on, so keep the raw characters.
smartquotes = False

# Report every problem so `make html` stays a reliable quality gate.
keep_warnings = True


# -- Options for Internationalization ----------------------------------------

# The code for the language the docs are written in.
language = "km"

# Sphinx has no Khmer search splitter. Declaring "en" explicitly keeps the
# build warning-free; Khmer phrases separated by spaces are still indexed as
# whole tokens. See README.md → "កម្រិតគាំទ្រការស្វែងរក".
html_search_language = "en"

# Directories in which to search for additional message catalogs.
# Kept so a future gettext/.po workflow (``make gettext``) drops in unchanged.
locale_dirs = ["../locale/"]
gettext_compact = "blender_manual"
gettext_allow_fuzzy_translations = False


# -- Options for HTML output -------------------------------------------------

html_theme = "basic"
if has_module("furo"):
    html_theme = "furo"

html_theme_path = []
html_theme_options = {}

if html_theme == "furo":
    html_theme_options = {
        "source_edit_link": (
            "https://github.com/SeyhaLite/Blender-Manual/edit/main/manual/{filename}"
        ),
        # Furo ships a built-in light / dark / auto switcher
        # (sidebar/variant-selector.html below), which is what the project
        # brief asks for — no custom toggle script needed.
        "light_css_variables": {
            "color-brand-primary": "#265787",
            "color-brand-content": "#265787",
        },
        "dark_css_variables": {
            "color-brand-primary": "#7fa7cc",
            "color-brand-content": "#7fa7cc",
        },
        "navigation_with_keys": True,
        "top_of_page_button": "edit",
        "announcement": (
            "កំពុងបកប្រែ — ការបកប្រែភាសាខ្មែរនេះនៅមិនទាន់ពេញលេញទេ។ "
            "Work in progress: only part of the manual is translated yet."
        ),
    }

    html_sidebars = {
        "**": [
            "sidebar/brand.html",
            "sidebar/search.html",
            "sidebar/scroll-start.html",
            "sidebar/navigation.html",
            "sidebar/variant-selector.html",
            "sidebar/scroll-end.html",
        ]
    }

html_title = "Blender {:s} Manual — ខ្មែរ".format(blender_version_label)

# Read the Docs injects READTHEDOCS_CANONICAL_URL at build time; the fallback
# only matters for local builds.
html_baseurl = os.environ.get(
    "READTHEDOCS_CANONICAL_URL",
    "https://blender-manual-km.readthedocs.io/",
)

html_logo = "../build_files/theme/blender-logo.svg"
html_favicon = "../build_files/theme/favicon.png"

if html_theme == "furo":
    # Order matters: fonts first, then the upstream overrides, then the
    # Khmer-specific overrides last so they win the cascade.
    html_css_files = [
        "fonts/noto-sans-khmer.css",
        "fonts/bl-icons.css",
        "css/theme_overrides.css",
        "css/km_overrides.css",
    ]

html_static_path = ["../build_files/theme"]

html_last_updated_fmt = "%Y-%m-%d"

html_copy_source = False
html_show_sourcelink = False
html_use_opensearch = html_baseurl.rstrip("/")
html_show_copyright = True
html_show_sphinx = False
html_show_search_summary = True

# Do not advertise an EPUB/PDF that we do not publish yet.
html_extra_path = []


# -- Options for HTML help output --------------------------------------------

htmlhelp_basename = "BlenderManualKhmer"


# -- Options for LaTeX output ------------------------------------------------

latex_engine = "xelatex"
latex_documents = [
    (
        "index",
        "blender_manual_km.tex",
        "Blender User Manual (Khmer)",
        "Blender Community",
        "manual",
    ),
]
latex_show_urls = "no"
latex_elements = {
    "papersize": "a4paper",
    "pointsize": "10pt",
    "sphinxsetup": "hmargin=0.75in, vmargin=1in",
    "classoptions": ",openany,oneside",
}


# -- Options for intersphinx -------------------------------------------------

# ``:ref:`bpy.ops.*``` / ``:ref:`bpy.types.*``` cross-references used all over
# the manual are resolved against the official Python API documentation,
# exactly like upstream does. Without this, every such reference is an
# unresolved-label warning.
intersphinx_mapping = {
    "blender_api": (
        "https://docs.blender.org/api/{:s}/".format(blender_version),
        None,
    ),
}

# The API inventory is a few megabytes; be generous on slow CI runners.
intersphinx_timeout = 30

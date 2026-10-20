# -*- mode: gnumakefile; tab-width: 4; indent-tabs-mode: t; -*-
# vim: tabstop=4
#
# Build targets for the Khmer (ភាសាខ្មែរ) Blender Manual.
# Modelled on the upstream Makefile of
# https://projects.blender.org/blender/blender-manual

define HELP_TEXT
Targets
=======

- setup             create .venv and install requirements.txt.
- html (default)    build HTML into build/html, failing on ANY warning.
- html-quick        build HTML without -W (use while drafting).
- livehtml          auto-rebuild on change at http://127.0.0.1:8000.
- linkcheck         check external links.
- clean             remove build/.

Translation workflow
--------------------

- gettext           extract .pot catalogs into build/locale.
- update_po         refresh locale/km/LC_MESSAGES/*.po from the catalogs.
- progress          print translation progress and untranslated files.
- check             run tools/check_translation.py (Khmer coverage + hygiene).
- labels            regenerate manual/_data/upstream_labels.json (needs UPSTREAM).
- titles            normalise RST title adornment widths for Khmer.
- anchors           repair #fragments of links into the English manual.
- preview           build one self-contained offline HTML preview.

The maintenance targets need a checkout of the upstream manual; point UPSTREAM
at its `manual/` directory, e.g.

  make check labels UPSTREAM=../upstream/manual

Environment Variables
---------------------

- NO_INTERSPHINX    when non-zero, skip intersphinx (no network access).

endef
# HELP_TEXT (end)

# Use the virtual environment when it exists.
SPHINX_BIN_PATH := .venv/bin/
ifeq (,$(wildcard $(SPHINX_BIN_PATH)))
	SPHINX_BIN_PATH :=
endif

SPHINXBUILD   ?= $(SPHINX_BIN_PATH)sphinx-build
SPHINXINTL    ?= $(SPHINX_BIN_PATH)sphinx-intl
SOURCEDIR      = manual
BUILDDIR       = build
LOCALEDIR      = locale
LANG           = km
UPSTREAM       ?= ../upstream/manual

# Fail on warnings by default: this is the project's quality gate.
SPHINXWARNFLAGS ?= -W --keep-going

.DEFAULT_GOAL := html

.PHONY: help Makefile
help:
	@printf '%s\n' '$(HELP_TEXT)'

.PHONY: setup
setup:
	python3 -m venv .venv
	.venv/bin/pip install --upgrade pip
	.venv/bin/pip install -r requirements.txt

.PHONY: html
html:
	$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(SPHINXWARNFLAGS)

# Convenience: build without treating warnings as errors.
.PHONY: html-quick
html-quick:
	$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)

.PHONY: livehtml
livehtml:
	$(SPHINX_BIN_PATH)sphinx-autobuild -b html "$(SOURCEDIR)" "$(BUILDDIR)/html" \
		--host 127.0.0.1 --port 8000 $(SPHINXOPTS)

.PHONY: linkcheck
linkcheck:
	$(SPHINXBUILD) -M linkcheck "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) || true

.PHONY: clean
clean:
	rm -rf "$(BUILDDIR)"

# -- Translation workflow ----------------------------------------------------

.PHONY: gettext
gettext:
	$(SPHINXBUILD) -b gettext "$(SOURCEDIR)" "$(BUILDDIR)/locale" $(SPHINXOPTS)

.PHONY: update_po
update_po: gettext
	$(SPHINXINTL) update -p "$(BUILDDIR)/locale" -l $(LANG) -d "$(LOCALEDIR)"

.PHONY: progress
progress:
	$(SPHINXINTL) stat -d "$(LOCALEDIR)" -l $(LANG) || true
	@python3 tools/check_translation.py --report

.PHONY: check
check:
	@python3 tools/check_translation.py --report --upstream "$(UPSTREAM)"

.PHONY: labels
labels:
	@python3 tools/update_upstream_labels.py --upstream "$(UPSTREAM)" \
		--commit "$$(cd "$(UPSTREAM)/.." && git rev-parse HEAD)"

.PHONY: titles
titles:
	@python3 tools/normalize_titles.py --write

.PHONY: anchors
anchors:
	@python3 tools/fix_external_anchors.py --write

.PHONY: preview
preview: html
	@python3 tools/make_offline_preview.py \
		--page interface/operators \
		--extra-article getting_started/installing/linux_windowing_environment \
		--extra-article interface/window_system/tabs_panels \
		--extra-article getting_started/configuration/hardware \
		--out ../preview/blender-manual-km-preview.html

# Catch-all: route anything else to sphinx-build (e.g. `make epub`).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# SPDX-License-Identifier: GPL-2.0-or-later
#
# Cross-reference fallback for the partial Khmer translation.
#
# Problem
# -------
# The upstream Blender Manual scatters ~5500 explicit targets such as
# ``.. _bpy.ops.wm.save_mainfile:`` over the pages that document each operator
# and property.  A ``:ref:`` pointing at one of those targets resolves *inside
# the manual*, not through intersphinx (the Python API inventory only registers
# ``py:function`` / ``py:class`` / ``py:attribute`` objects, never
# ``std:label``).  In a partial translation those pages do not exist yet, so
# every such reference is unresolved and breaks a ``-W`` build.
#
# Solution
# --------
# ``tools/update_upstream_labels.py`` records which upstream document defines
# each target.  This extension reads that map on ``missing-reference`` and
# turns the unresolved reference into a link to the matching page of the
# official English manual.  As soon as a page is translated, its own local
# target takes precedence and the fallback stops firing for it - no edits to
# the already-translated pages are needed.
#
# The extension never invents a target: if a label is not in the map the
# reference is left unresolved so the normal Sphinx warning still appears.

from __future__ import annotations

import json
import os
from typing import Any, Dict, Optional

from docutils import nodes
from docutils.nodes import fully_normalize_name
from sphinx.application import Sphinx
from sphinx.environment import BuildEnvironment
from sphinx.util import logging

logger = logging.getLogger(__name__)

_CACHE: Dict[str, Any] = {"labels": {}, "docs": set(), "loaded_from": None}


def _load(app: Sphinx) -> None:
    path = app.config.km_upstream_labels
    if not path:
        return
    if not os.path.isabs(path):
        path = os.path.join(app.srcdir, path)
    if _CACHE["loaded_from"] == path:
        return
    try:
        with open(path, encoding="utf-8") as handle:
            payload = json.load(handle)
    except (OSError, ValueError) as exc:
        logger.warning("km_xref_fallback: cannot read %s (%s)", path, exc)
        return

    docs = list(payload.get("docs", []))
    labels: Dict[str, str] = {}
    for label, entry in payload.get("labels", {}).items():
        try:
            index, fragment = entry
            tail = "%s.html#%s" % (docs[index], fragment)
        except (TypeError, ValueError, IndexError):
            continue
        # Sphinx lowercases and whitespace-normalises the target of a ``:ref:``
        # before it reaches `missing-reference`, so index the map the same way
        # (this is what makes ``bpy.types.UIPopupMenu`` resolve).
        labels[fully_normalize_name(label)] = tail
        labels.setdefault(label, tail)

    _CACHE["labels"] = labels
    _CACHE["docs"] = set(docs)
    _CACHE["loaded_from"] = path
    logger.debug("km_xref_fallback: %d labels over %d documents", len(labels), len(docs))


def _external(base: str, tail: str, contnode: nodes.Element,
              css_class: str) -> nodes.reference:
    ref = nodes.reference("", "", contnode, refuri=base.rstrip("/") + "/" + tail,
                          internal=False)
    ref["classes"].append(css_class)
    return ref


def missing_reference(app: Sphinx, env: BuildEnvironment, node: nodes.Element,
                      contnode: nodes.Element) -> Optional[nodes.Element]:
    base = app.config.km_english_manual_url
    if not base or not _CACHE["labels"]:
        return None

    reftype = node.get("reftype")
    target = node.get("reftarget")
    if not target:
        return None

    # ``:doc:`` to a page that is not in the translated tree yet.
    if reftype == "doc":
        normalised = target[1:] if target.startswith("/") else target
        if normalised in _CACHE["docs"]:
            return _external(base, normalised + ".html", contnode, "km-fallback-en")
        return None

    # ``:ref:`` / ``:numref:`` to an upstream explicit target.
    if reftype in ("ref", "numref", "keyword", "option", "cmdoption", "envvar"):
        tail = _CACHE["labels"].get(target)
        if tail:
            return _external(base, tail, contnode, "km-fallback-en")

    return None


def setup(app: Sphinx) -> Dict[str, Any]:
    app.add_config_value("km_english_manual_url", "", "env")
    app.add_config_value("km_upstream_labels", "_data/upstream_labels.json", "env")
    app.connect("builder-inited", _load)
    app.connect("missing-reference", missing_reference, priority=400)

    return {
        "version": "1.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }

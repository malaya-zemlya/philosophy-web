"""
bookgen — build a printable encyclopedia (LaTeX -> PDF) from the philosophy web.

Modules, each owning one concern:
  config      paths, constants, and the BookOptions dataclass
  nodes       load web/ nodes and resolve a user selection into an ordered id list
  latex       LaTeX escaping and the portable Unicode map
  inline      inline markdown -> LaTeX, plus cross-reference (Ctx) resolution
  markdown    block-level markdown -> LaTeX (lists, paragraphs, sections, asides)
  templates   the LaTeX preamble / title page / front-matter strings
  document    assemble the whole document from the selected nodes
  compile     locate a LaTeX engine and run it
  cli         argument parsing and orchestration

The sibling top-level scripts (weblinks.py) are imported by name, so make sure the `scripts/`
directory is importable however bookgen is loaded.
"""
import os
import sys

# Allow `import weblinks` (a sibling top-level script) regardless of how bookgen was imported.
_SCRIPTS_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, _SCRIPTS_DIR)

"""Shared paths, constants, and the rendering-options dataclass."""
import os
import re
from dataclasses import dataclass
from typing import Optional

# repo root = .../scripts/bookgen/config.py -> up three
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
WEB = os.path.join(ROOT, "web")
OUTDIR = os.path.join(ROOT, "book")     # deliverables: encyclopedia.tex + encyclopedia.pdf
BUILDDIR = os.path.join(ROOT, "build")  # LaTeX intermediates (.aux/.log/.fls/…) live here

# Default selection for --all (and when nothing is specified): the content nodes that read as
# encyclopedia entries. Sources and character portfolios are excluded unless asked for by --type.
CONTENT_TYPES = ["concept", "claim", "argument", "question", "position"]

SKIP_FILES = {"INDEX.md", "README.md"}
FM_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)


@dataclass
class BookOptions:
    """Everything that shapes the typeset document (independent of which nodes are chosen)."""
    title: str = "An Encyclopedia of Philosophy"
    subtitle: str = "Distilled from the philosophy web"
    running_head: Optional[str] = None    # falls back to title
    columns: int = 2                       # 1 or 2
    sort: str = "title"                    # title | type | id
    font: str = "default"                  # text font preset: default | bookman | palatino | times | charter
    attribution: bool = True               # show the "after <Author>" etiquette line
    twoside: bool = False
    paper: str = "a4paper"
    margin: str = "2cm"

    @property
    def head(self) -> str:
        return self.running_head or self.title

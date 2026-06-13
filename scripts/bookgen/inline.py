"""Inline markdown -> LaTeX, plus cross-reference resolution.

`Ctx` turns a cited node id into an encyclopedia cross-reference, following the conventions of an
old general encyclopedia. A reference is labelled by the target's **headword** (its name in this
book, the word it is alphabetised under) set in small caps; a node with no headword falls back to
its full title, set in italics so that a sentence-length title does not shout in running text.
`render_inline` adds the classic *redirection*: when a reference stands alone inside parentheses
(a pointer rather than a noun woven into the sentence), the group is rewritten `(see HEADWORD)`.
It handles the span-level markdown the corpus uses — code, links, `[[id]]` shorthand, `**bold**`,
`*italic*` — being careful to escape only genuine text, never the LaTeX it generates.
"""
import re
from typing import Dict, Optional, Set, Tuple

import weblinks  # sibling top-level script: MDLINK_RE, WIKILINK_RE, node_id_from_target, slug_of

from .config import ROOT
from .latex import latex_escape

# A cross-reference is set in small caps when its label is a true headword: short and term-like,
# the classic look. These node types carry short, headword-style titles, so they get small caps
# even with no explicit `headword:`. claim/argument/question titles are full sentences, so without
# a headword they fall back to italics; an explicit `headword:` (any type) forces small caps.
SMALLCAPS_TYPES = {"concept", "position", "source", "character"}

# Inline math: `$ … $`, GitHub-style. The `$` must hug its content (no space just inside), which
# is what keeps a stray prose dollar (`$5 and $10`) from being read as math. `$$` is display math,
# handled at block level (markdown.py); the lookarounds here make sure this never bites into one.
INLINE_MATH_RE = re.compile(r"(?<!\$)\$(?!\$)(?=\S)([^$\n]+?)(?<=\S)\$")


class Ctx:
    """Per-entry rendering context: resolves a cited id into a (possibly linked) cross-reference."""

    def __init__(self, src_path: str, titles: Dict[str, str], kinds: Dict[str, str],
                 included: Set[str], path_to_id: Dict[str, str],
                 has_headword: Optional[Set[str]] = None):
        self.src_path = src_path        # the citing node's file (links are relative to it)
        self.titles = titles            # id -> display label (headword if any, else title)
        self.kinds = kinds              # id -> node type (helps choose small caps vs italics)
        self.included = included        # ids that have an entry in THIS volume (so, linkable)
        self.path_to_id = path_to_id    # relpath-from-root -> id
        self.has_headword = has_headword or set()  # ids carrying an explicit `headword:`

    def _ref(self, nid: str, display: str, force_sc: bool = False) -> str:
        # Small caps for genuine headwords (explicit, a deliberate alias, or a term-like type);
        # italics for a fallen-back full-sentence title, which would shout in small caps.
        small = force_sc or nid in self.has_headword or self.kinds.get(nid) in SMALLCAPS_TYPES
        label = r"\%s{%s}" % ("textsc" if small else "emph", latex_escape(display))
        if nid in self.included:
            return r"\hyperref[entry:%s]{%s}" % (nid, label)
        return label

    def xref_id(self, nid: str, alias: Optional[str] = None) -> Tuple[str, bool]:
        # An explicit `[[id|alias]]` wins (it reads better inline than a long title) and is treated
        # as a headword-like label; otherwise default to the node's display name (headword or title).
        display = alias or self.titles.get(nid) or weblinks.slug_of(nid)
        return self._ref(nid, display, force_sc=alias is not None), True

    def xref_target(self, text: str, target: str) -> Tuple[str, bool]:
        nid = weblinks.node_id_from_target(target, self.src_path, ROOT, self.path_to_id)
        if not nid:
            return r"\emph{%s}" % latex_escape(text), False
        # A hand-written label (not the bare slug/id) is a deliberate alias -> honor it, the way
        # lint preserves custom link labels; a default slug/id label yields to the display name.
        custom = text not in (weblinks.slug_of(nid), nid)
        display = text if custom else (self.titles.get(nid) or weblinks.slug_of(nid))
        return self._ref(nid, display, force_sc=custom), True


def render_inline(text: str, ctx: Ctx) -> str:
    """Span-level markdown -> LaTeX: protect code/links, escape, apply emphasis, restore."""
    stash = []
    link_idx: Set[int] = set()   # stash slots holding a resolved cross-reference

    def keep(s: str, is_link: bool = False) -> str:
        stash.append(s)
        if is_link:
            link_idx.add(len(stash) - 1)
        return "\x00%d\x00" % (len(stash) - 1)

    # 1. protect spans that must not be escaped or touched by emphasis
    text = re.sub(r"`([^`]+)`", lambda m: keep(r"\texttt{%s}" % latex_escape(m.group(1))), text)
    # inline math: hand the LaTeX through verbatim — never escaped, never touched by emphasis
    text = INLINE_MATH_RE.sub(lambda m: keep("$%s$" % m.group(1)), text)

    def md(m):
        rendered, is_xref = ctx.xref_target(m.group(1), m.group(2))
        return keep(rendered, is_link=is_xref)
    text = weblinks.MDLINK_RE.sub(md, text)

    def wiki(m):
        alias = m.group(2)[1:].strip() if m.group(2) else None
        rendered, is_xref = ctx.xref_id(m.group(1), alias=alias)
        return keep(rendered, is_link=is_xref)
    text = weblinks.WIKILINK_RE.sub(wiki, text)

    # 1b. classic redirection: a parenthetical group that is *only* cross-references (a pointer,
    # not a term woven into the sentence) becomes "(see HEADWORD)" — one "see" for the whole group.
    def see(m):
        inner = m.group(1)
        idxs = [int(x) for x in re.findall(r"\x00(\d+)\x00", inner)]
        if not idxs or not all(i in link_idx for i in idxs):
            return m.group(0)            # contains a non-link span -> leave it alone
        if re.sub(r"[,\s]", "", re.sub(r"\x00\d+\x00", "", inner)):
            return m.group(0)            # links mixed with other prose -> a noun, not a pointer
        return "(see %s)" % inner
    text = re.sub(r"\(([^()]*)\)", see, text)

    # 2. escape the remaining plain text
    text = latex_escape(text)

    # 3. emphasis (asterisks pass through escaping untouched)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\\textbf{\1}", text)
    text = re.sub(r"\*([^*]+)\*", r"\\emph{\1}", text)

    # 4. restore protected spans
    return re.sub(r"\x00(\d+)\x00", lambda m: stash[int(m.group(1))], text)

"""Inline markdown -> LaTeX, plus cross-reference resolution.

`Ctx` knows how to turn a cited node id into an encyclopedia cross-reference: the target's title
in small caps, hyperlinked to its entry when that entry is in the same volume. `render_inline`
handles the span-level markdown the corpus uses — code, links, `[[id]]` shorthand, `**bold**`,
`*italic*` — being careful to escape only genuine text, never the LaTeX it generates.
"""
import re
from typing import Dict, Optional, Set

import weblinks  # sibling top-level script: MDLINK_RE, WIKILINK_RE, node_id_from_target, slug_of

from .config import ROOT
from .latex import latex_escape

# Term-like nodes have short, headword-style titles -> small caps (the classic cross-ref look).
# Proposition-like nodes (claim, argument) have full-sentence titles -> italics, which stay
# readable where small caps would shout a whole sentence in the running text.
SMALLCAPS_TYPES = {"concept", "position", "question", "source", "character"}


class Ctx:
    """Per-entry rendering context: resolves a cited id into a (possibly linked) cross-reference."""

    def __init__(self, src_path: str, titles: Dict[str, str], kinds: Dict[str, str],
                 included: Set[str], path_to_id: Dict[str, str]):
        self.src_path = src_path        # the citing node's file (links are relative to it)
        self.titles = titles            # id -> title, across the whole web
        self.kinds = kinds              # id -> node type (chooses small caps vs italics)
        self.included = included        # ids that have an entry in THIS volume (so, linkable)
        self.path_to_id = path_to_id    # relpath-from-root -> id

    def _styled(self, nid: str, text: str) -> str:
        cmd = "textsc" if self.kinds.get(nid) in SMALLCAPS_TYPES else "emph"
        return r"\%s{%s}" % (cmd, latex_escape(text))

    def xref_id(self, nid: str, fallback: Optional[str] = None) -> str:
        title = self.titles.get(nid)
        text = title if title else (fallback or weblinks.slug_of(nid))
        label = self._styled(nid, text)
        if nid in self.included:
            return r"\hyperref[entry:%s]{%s}" % (nid, label)
        return label

    def xref_target(self, text: str, target: str) -> str:
        nid = weblinks.node_id_from_target(target, self.src_path, ROOT, self.path_to_id)
        if nid:
            return self.xref_id(nid, fallback=text)
        return r"\emph{%s}" % latex_escape(text)


def render_inline(text: str, ctx: Ctx) -> str:
    """Span-level markdown -> LaTeX: protect code/links, escape, apply emphasis, restore."""
    stash = []

    def keep(s: str) -> str:
        stash.append(s)
        return "\x00%d\x00" % (len(stash) - 1)

    # 1. protect spans that must not be escaped or touched by emphasis
    text = re.sub(r"`([^`]+)`", lambda m: keep(r"\texttt{%s}" % latex_escape(m.group(1))), text)
    text = weblinks.MDLINK_RE.sub(lambda m: keep(ctx.xref_target(m.group(1), m.group(2))), text)

    def wiki(m):
        alias = m.group(2)[1:].strip() if m.group(2) else None
        return keep(ctx.xref_id(m.group(1), fallback=alias))
    text = weblinks.WIKILINK_RE.sub(wiki, text)

    # 2. escape the remaining plain text
    text = latex_escape(text)

    # 3. emphasis (asterisks pass through escaping untouched)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\\textbf{\1}", text)
    text = re.sub(r"\*([^*]+)\*", r"\\emph{\1}", text)

    # 4. restore protected spans
    return re.sub(r"\x00(\d+)\x00", lambda m: stash[int(m.group(1))], text)

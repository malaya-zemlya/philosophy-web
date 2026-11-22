r"""The chaptered layout: the book as thematic chapters rather than one A–Z run.

Structure (driven by the hand-edited `book/chapters/*.md`, see `scripts/chapters.py`):

- front matter: title page, Symbols, a Contents page listing **chapters only**, then any
  `kind: front` chapters (the book introduction, a reading guide);
- main matter: each `kind: body` chapter as a numbered chapter — its introduction full width, then
  its entries in the file's hand-made order, two columns; a claim listed under an argument (or
  position) prints as a compact sub-entry right after its parent, labelled with its role;
- appendices: the `kind: back` chapters, plus "Unsorted entries" for any selected node that no
  chapter places (so nothing silently disappears);
- back matter: Sources, then an alphabetical **Index** of every entry and sub-entry with its page.

Only selected nodes print: a chapter keeps its order but skips unselected entries, a nested claim
whose parent is unselected is promoted to a top-level entry, and a body chapter left with no
entries is dropped.
"""
from typing import Dict, List, Optional, Tuple

import chapters as chapterlib  # sibling top-level script: load_chapters, nesting roles

from .config import BookOptions
from .document import (_collect_cited_sources, _glyph, _sources_section, alpha_title,
                       document_head, entry_lines, render_setup)
from .inline import Ctx
from .latex import latex_escape
from .markdown import render_body
from .nodes import Node


def _as_list(v):
    if v is None:
        return []
    return v if isinstance(v, list) else [v]


def _role(child: str, parent: Optional[Node], parent_fm: Dict) -> str:
    """How a nested claim relates to its parent, for its etiquette line."""
    if parent is None:
        return ""
    prem = _as_list(parent_fm.get("premise"))
    if child in prem:
        return "premise %d" % (prem.index(child) + 1) if len(prem) > 1 else "premise"
    if child in _as_list(parent_fm.get("concludes")):
        return "conclusion"
    if child in _as_list(parent_fm.get("commits_to")):
        return "commitment"
    if child in _as_list(parent_fm.get("rejects")):
        return "rejected"
    return ""


def _chapter_node(ch) -> Node:
    """A chapter as a pseudo-node, so its introduction renders (and cites sources) like a body."""
    return Node(id=ch.id, type="chapter", title=ch.title, author=None, status="asserted",
                body=ch.body, path=str(ch.path))


def _intro_is_placeholder(body: str) -> bool:
    return not body.strip() or body.strip().upper().startswith("TODO")


def build_chaptered(ids: List[str], nodes: Dict[str, Node], opts: BookOptions) -> str:
    chs, errors = chapterlib.load_chapters()
    if errors:
        raise SystemExit("chapter files have errors (run `make lint`):\n  " + "\n  ".join(errors))
    web_fm = chapterlib.load_web()
    titles, kinds, has_headword, path_to_id, included = render_setup(ids, nodes)

    # --- what prints where ------------------------------------------------------------------
    plan: List[Tuple[object, List[Tuple[str, List[str]]]]] = []   # (chapter, [(top, [kids])])
    placed = set()
    for ch in chs:
        rows = []
        for top, kids in ch.entries:
            kids_in = [k for k in kids if k in included]
            if top in included:
                rows.append((top, kids_in))
            else:                      # parent not selected: its selected claims stand alone
                rows += [(k, []) for k in kids_in]
            placed.update([top] + kids)
        if rows or (ch.kind != "body" and not _intro_is_placeholder(ch.body)):
            plan.append((ch, rows))
    unsorted = sorted((i for i in ids if i not in placed),
                      key=lambda i: alpha_title(nodes[i].display))

    printed = [x for _, rows in plan for top, kids in rows for x in [top] + kids] + unsorted
    chapter_nodes = {ch.id: _chapter_node(ch) for ch, _ in plan}
    all_nodes = dict(nodes, **chapter_nodes)
    cited = _collect_cited_sources(printed + list(chapter_nodes), all_nodes, path_to_id)

    parts, subst = document_head(opts, len(printed), {nodes[i].type for i in printed})
    parts.append(r"\booktoc")

    def ctx_for(path) -> Ctx:
        return Ctx(str(path), titles, kinds, included, path_to_id, has_headword, cited)

    def emit_chapter(ch, rows, star: bool = False) -> List[str]:
        out = [r"\bookchapter{%s}{%s}" % (latex_escape(ch.title), ch.id)]
        if not _intro_is_placeholder(ch.body):
            out += [r"\begin{chapterintro}", render_body(ch.body, ctx_for(ch.path)),
                    r"\end{chapterintro}"]
        if rows:
            out.append(r"\begin{multicols}{2}" if opts.columns == 2 else "")
            for top, kids in rows:
                out += entry_lines(top, nodes, opts, ctx_for(nodes[top].path))
                if kids:
                    label = "Its claims" if nodes[top].type == "argument" else "Its commitments"
                    out.append(r"\begin{subentries}{%s}" % label)
                    for k in kids:
                        out += entry_lines(k, nodes, opts, ctx_for(nodes[k].path),
                                           macro="subentryhead",
                                           role=_role(k, nodes[top], web_fm.get(top, {})))
                    out.append(r"\end{subentries}")
            out.append(r"\end{multicols}" if opts.columns == 2 else "")
        return out

    stage = "front"
    for ch, rows in plan:
        if ch.kind == "body" and stage == "front":
            parts.append(r"\mainmatter")
            stage = "body"
        if ch.kind == "back" and stage != "back":
            if stage == "front":
                parts.append(r"\mainmatter")
            parts.append(r"\appendix")
            stage = "back"
        parts += emit_chapter(ch, rows)

    if unsorted:
        if stage != "back":
            if stage == "front":
                parts.append(r"\mainmatter")
            parts.append(r"\appendix")
            stage = "back"
        stub = type("Stub", (), {"title": "Unsorted entries", "id": "chapter-unsorted",
                                 "body": "", "path": ""})
        parts += emit_chapter(stub, [(i, []) for i in unsorted])

    parts.append(r"\backmatter")
    parts += _sources_section(cited, nodes)
    parts += _index(printed, nodes)
    parts.append(r"\end{document}")
    return "\n".join(p for p in parts if p is not None) + "\n"


def _index(printed: List[str], nodes: Dict[str, Node]) -> List[str]:
    """The back-of-book index: every printed entry and sub-entry, A–Z, with its page."""
    out = [r"\bookindexband", r"\begin{bookindex}"]
    cur = None
    for nid in sorted(printed, key=lambda i: (alpha_title(nodes[i].display), i)):
        head = alpha_title(nodes[nid].display)
        ch = next((c for c in head if c.isalnum()), "#")
        letter = ch.upper() if ch.isalpha() else "#"
        if letter != cur:
            out.append(r"\indexletter{%s}" % letter)
            cur = letter
        out.append(r"\entryline{%s}{%s}{%s}" % (_glyph(nodes[nid]), nid,
                                                latex_escape(nodes[nid].display)))
    out.append(r"\end{bookindex}")
    return out

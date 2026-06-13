"""Assemble the full LaTeX document from the selected nodes.

Ordering and grouping (alphabetical by title, by type, or by id), the per-headword etiquette
line, the List of Entries, and the letter/column structure all live here. Markdown rendering is
delegated to `inline`/`markdown`; the LaTeX scaffolding to `templates`.
"""
import datetime
import re
from typing import Dict, List, Tuple

from .config import BookOptions
from .inline import Ctx, render_inline
from .latex import latex_escape, unicode_declarations
from .markdown import render_body
from .nodes import Node
from . import templates


def fill(template: str, mapping: Dict[str, str]) -> str:
    """Substitute `<<KEY>>` placeholders (LaTeX-safe; str.format would choke on braces)."""
    for key, value in mapping.items():
        template = template.replace(key, value)
    return template


def author_display(author) -> str:
    """The attribution shown in an entry's etiquette line, or '' to omit it."""
    if not author or author == "generic":
        return ""
    if author == "mishka":
        return "editorial"
    return "after " + author.replace("-", " ").replace("_", " ").title()


def etiquette(node: Node, show_author: bool) -> str:
    """The small italic line under a headword: type, non-default status, optional attribution."""
    bits = [node.type.capitalize()]
    if node.status not in ("asserted", None):
        bits.append(node.status)
    if show_author:
        a = author_display(node.author)
        if a:
            bits.append(a)
    return r" \,\textperiodcentered\, ".join(latex_escape(b) for b in bits)


# Leading articles are ignored when alphabetising ("The Chinese Room" files under C).
_ARTICLE_RE = re.compile(r"^(the|a|an)\s+", re.IGNORECASE)


def alpha_title(title: str) -> str:
    """A title's sort form: leading article dropped, casefolded."""
    return _ARTICLE_RE.sub("", title).casefold()


def group_key(node: Node, nid: str, sort: str) -> str:
    """The divider a node falls under: its type, or the first letter of its display name/id."""
    if sort == "type":
        return node.type.capitalize()
    head = nid if sort == "id" else _ARTICLE_RE.sub("", node.display)
    ch = next((c for c in head if c.isalnum()), "#")
    return ch.upper() if ch.isalpha() else "#"


def sort_key(node: Node, nid: str, sort: str) -> Tuple:
    if sort == "id":
        return (nid,)
    if sort == "type":
        return (node.type, alpha_title(node.display), nid)
    return (alpha_title(node.display), nid)


def _preamble_subst(opts: BookOptions, count: int, date: str) -> Dict[str, str]:
    return {
        "<<SIDES>>": "twoside" if opts.twoside else "oneside",
        "<<PAPER>>": opts.paper, "<<MARGIN>>": opts.margin,
        "<<UNICODE>>": unicode_declarations(),
        "<<COLSEPRULE>>": "0.4pt" if opts.columns == 2 else "0pt",
        "<<TITLE>>": latex_escape(opts.title),
        "<<SUBTITLE>>": latex_escape(opts.subtitle) if opts.subtitle else "",
        "<<RUNHEAD>>": latex_escape(opts.head),
        "<<DATE>>": date, "<<COUNT>>": str(count),
    }


def build_document(ids: List[str], nodes: Dict[str, Node], opts: BookOptions) -> str:
    """Render the chosen ids into a complete, compilable LaTeX document."""
    # cross-references display the target's headword when it has one, else its title
    titles = {nid: n.display for nid, n in nodes.items()}
    kinds = {nid: n.type for nid, n in nodes.items()}
    path_to_id = {n.relpath: nid for nid, n in nodes.items()}
    included = set(ids)
    ordered = sorted(ids, key=lambda nid: sort_key(nodes[nid], nid, opts.sort))
    date = datetime.date.today().strftime("%B %Y")
    subst = _preamble_subst(opts, len(ordered), date)

    parts: List[str] = [fill(templates.PREAMBLE, subst), r"\begin{document}",
                        fill(templates.TITLEPAGE, subst)]
    parts += _front_matter(ordered, nodes, subst)
    parts += _entries(ordered, nodes, opts, titles, kinds, included, path_to_id)
    parts.append(r"\end{document}")
    return "\n".join(parts) + "\n"


def _front_matter(ordered: List[str], nodes: Dict[str, Node],
                  subst: Dict[str, str]) -> List[str]:
    out = [fill(templates.FRONT, subst), r"\begin{listofentries}"]
    out += [r"\entryline{%s}{%s}" % (nid, latex_escape(nodes[nid].display)) for nid in ordered]
    out += [r"\end{listofentries}", r"\mainmatter"]
    return out


def _entries(ordered: List[str], nodes: Dict[str, Node], opts: BookOptions,
             titles, kinds, included, path_to_id) -> List[str]:
    out: List[str] = []
    cur_group = None
    in_cols = False

    def close_cols():
        nonlocal in_cols
        if in_cols:
            out.append(r"\end{multicols}")
            in_cols = False

    for nid in ordered:
        node = nodes[nid]
        g = group_key(node, nid, opts.sort)
        if g != cur_group:
            close_cols()
            out.append(r"\bookgroup{%s}" % latex_escape(g))
            cur_group = g
            if opts.columns == 2:
                out.append(r"\begin{multicols}{2}")
                in_cols = True
        ctx = Ctx(node.path, titles, kinds, included, path_to_id)
        subtitle = render_inline(node.subtitle, ctx) if node.subtitle else ""
        out.append(r"\entryhead{%s}{%s}{%s}{%s}{%s}" % (
            nid, render_inline(node.display, ctx), etiquette(node, opts.attribution),
            latex_escape(node.display), subtitle))
        out.append(render_body(node.body, ctx))
        out.append("")
    close_cols()
    return out

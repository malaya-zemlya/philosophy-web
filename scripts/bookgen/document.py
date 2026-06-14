"""Assemble the full LaTeX document from the selected nodes.

Ordering and grouping (alphabetical by title, by type, or by id), the per-headword etiquette
line, the List of Entries, and the letter/column structure all live here. Markdown rendering is
delegated to `inline`/`markdown`; the LaTeX scaffolding to `templates`.
"""
import datetime
import re
from typing import Dict, List, Set, Tuple

import weblinks

from .config import BookOptions, ROOT
from .inline import Ctx, render_inline, render_reference
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
# Leading punctuation is ignored too, so a title that opens with a quote or bracket
# (`The "real feel"…`) sorts under its first *letter*, where its letter band also puts it.
_LEAD_PUNCT_RE = re.compile(r"^[^0-9A-Za-z]+")


def alpha_title(title: str) -> str:
    """A title's sort form: leading punctuation and a leading article dropped, casefolded. This is
    the single source of truth for both the sort order and the letter band, so they cannot drift
    (a leading quote no longer sorts a `The "real feel"…` entry ahead of everything under A)."""
    t = _LEAD_PUNCT_RE.sub("", title)     # opening quote/bracket before the first word
    t = _ARTICLE_RE.sub("", t)            # leading article
    t = _LEAD_PUNCT_RE.sub("", t)         # punctuation sitting between the article and first word
    return t.casefold()


def group_key(node: Node, nid: str, sort: str) -> str:
    """The divider a node falls under: its type, or the first letter of its sort form / id."""
    if sort == "type":
        return node.type.capitalize()
    head = nid if sort == "id" else alpha_title(node.display)
    ch = next((c for c in head if c.isalnum()), "#")
    return ch.upper() if ch.isalpha() else "#"


def sort_key(node: Node, nid: str, sort: str) -> Tuple:
    if sort == "id":
        return (nid,)
    if sort == "type":
        return (node.type, alpha_title(node.display), nid)
    return (alpha_title(node.display), nid)


# --- back-matter Sources (bibliography) --------------------------------------------------------
_REF_LABEL_RE = re.compile(r"^\s*references?\s*:\s*(.*)$", re.IGNORECASE)
_BULLET_RE = re.compile(r"^[-*]\s+(.*)$")
# a new lowercase section label (`key passages:`, `note on lineage:`, …) ends the reference block;
# the `(?!https?:)` guard keeps a wrapped URL line (`https://…`) from looking like a label.
_NEW_LABEL_RE = re.compile(r"^(?!https?:)[a-z][\w ()/'\-]{0,40}:(\s|$)")


def source_references(body: str) -> List[str]:
    """Pull the citation line(s) out of a source node body: the `Reference:` / `References:` block
    (inline text after the label, plus following lines up to a blank line or the next section
    label; bullets split multiple works)."""
    lines = body.split("\n")
    out: List[str] = []
    i = 0
    while i < len(lines):
        m = _REF_LABEL_RE.match(lines[i])
        if not m:
            i += 1
            continue
        block = [m.group(1).strip()] if m.group(1).strip() else []
        j = i + 1
        while j < len(lines) and lines[j].strip():
            if not _BULLET_RE.match(lines[j]) and _NEW_LABEL_RE.match(lines[j]):
                break
            block.append(lines[j].strip())
            j += 1
        cur = None
        for bl in block:
            bm = _BULLET_RE.match(bl)
            if bm:
                if cur:
                    out.append(cur)
                cur = bm.group(1).strip()
            elif cur is None:
                cur = bl
            else:
                cur += " " + bl
        if cur:
            out.append(cur)
        i = j
    return out


def _collect_cited_sources(ordered: List[str], nodes: Dict[str, Node],
                           path_to_id: Dict[str, str]) -> Set[str]:
    """Every `source` node referenced (by `[[id]]` or rendered link) in the included entries."""
    cited: Set[str] = set()
    for nid in ordered:
        node = nodes[nid]
        for m in weblinks.WIKILINK_RE.finditer(node.body):
            t = m.group(1)
            if t in nodes and nodes[t].type == "source":
                cited.add(t)
        for m in weblinks.MDLINK_RE.finditer(node.body):
            t = weblinks.node_id_from_target(m.group(2), node.path, ROOT, path_to_id)
            if t and t in nodes and nodes[t].type == "source":
                cited.add(t)
    return cited


def _sources_section(cited: Set[str], nodes: Dict[str, Node]) -> List[str]:
    """Render the Sources back matter: every cited source's APA reference(s), alphabetised by the
    leading author. Each source is anchored `source:<id>` so in-text citations link to it."""
    if not cited:
        return []

    def key(sid: str) -> str:
        refs = source_references(nodes[sid].body)
        return (refs[0] if refs else nodes[sid].title).casefold()

    out = [r"\sourcesband", r"\begin{sourcelist}"]
    for sid in sorted(cited, key=key):
        refs = source_references(nodes[sid].body) or [nodes[sid].title]
        for k, ref in enumerate(refs):
            out.append(r"\sourceitem{%s}{%s}" % (sid if k == 0 else "", render_reference(ref)))
    out.append(r"\end{sourcelist}")
    return out


def _preamble_subst(opts: BookOptions, count: int, date: str) -> Dict[str, str]:
    font_pdftex, font_unicode = templates.FONTS.get(opts.font, templates.FONTS["default"])
    return {
        "<<SIDES>>": "twoside" if opts.twoside else "oneside",
        "<<PAPER>>": opts.paper, "<<MARGIN>>": opts.margin,
        "<<FONT_PDFTEX>>": font_pdftex, "<<FONT_UNICODE>>": font_unicode,
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
    has_headword = {nid for nid, n in nodes.items() if n.headword}
    path_to_id = {n.relpath: nid for nid, n in nodes.items()}
    included = set(ids)
    ordered = sorted(ids, key=lambda nid: sort_key(nodes[nid], nid, opts.sort))
    cited_sources = _collect_cited_sources(ordered, nodes, path_to_id)
    date = datetime.date.today().strftime("%B %Y")
    subst = _preamble_subst(opts, len(ordered), date)

    parts: List[str] = [fill(templates.PREAMBLE, subst), r"\begin{document}",
                        fill(templates.TITLEPAGE, subst)]
    parts += _front_matter(ordered, nodes, subst)
    parts += _entries(ordered, nodes, opts, titles, kinds, included, path_to_id, has_headword,
                      cited_sources)
    parts += _sources_section(cited_sources, nodes)
    parts.append(r"\end{document}")
    return "\n".join(parts) + "\n"


def _front_matter(ordered: List[str], nodes: Dict[str, Node],
                  subst: Dict[str, str]) -> List[str]:
    out = [fill(templates.FRONT, subst), r"\begin{listofentries}"]
    out += [r"\entryline{%s}{%s}" % (nid, latex_escape(nodes[nid].display)) for nid in ordered]
    out += [r"\end{listofentries}", r"\mainmatter"]
    return out


def _entries(ordered: List[str], nodes: Dict[str, Node], opts: BookOptions,
             titles, kinds, included, path_to_id, has_headword, sources) -> List[str]:
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
        ctx = Ctx(node.path, titles, kinds, included, path_to_id, has_headword, sources)
        subtitle = render_inline(node.subtitle, ctx) if node.subtitle else ""
        out.append(r"\entryhead{%s}{%s}{%s}{%s}{%s}" % (
            nid, render_inline(node.display, ctx), etiquette(node, opts.attribution),
            latex_escape(node.display), subtitle))
        out.append(render_body(node.body, ctx))
        out.append("")
    close_cols()
    return out

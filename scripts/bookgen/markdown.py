"""Block-level markdown -> LaTeX.

Handles the block grammar the node bodies use: paragraphs, bullet/numbered lists, and `###`
subheadings. Two subheadings are special-cased to match the encyclopedia style: `### In plain
terms` becomes a shaded aside, and `### See also` becomes a cross-reference list.
"""
import re
from typing import List, Optional, Tuple

from .inline import Ctx, render_inline

# a list item: bullet (-, *) or ordered (1. / 1)); captures the indent, marker, and text
_ITEM_RE = re.compile(r"^(\s*)([-*]|\d+[.)])\s+(.*)$")
# a level-3 heading line
_H3_RE = re.compile(r"^###\s+(.*)$", re.MULTILINE)


def render_blocks(md: str, ctx: Ctx) -> str:
    """A chunk of markdown with no `###` headings -> LaTeX paragraphs and lists."""
    out: List[str] = []
    lines = md.split("\n")
    i = 0
    while i < len(lines):
        if not lines[i].strip():
            i += 1
            continue
        if _ITEM_RE.match(lines[i]):
            block, i = _take_list(lines, i, ctx)
            out.append(block)
        else:
            para, i = _take_paragraph(lines, i, ctx)
            out.append(para)
    return "\n\n".join(out)


def _take_list(lines: List[str], i: int, ctx: Ctx) -> Tuple[str, int]:
    """Consume a run of list lines (marker lines start items; others continue the last)."""
    ordered = _ITEM_RE.match(lines[i]).group(2)[0].isdigit()
    items: List[str] = []
    while i < len(lines) and lines[i].strip():
        m = _ITEM_RE.match(lines[i])
        if m:
            items.append(m.group(3).strip())
        elif items:
            items[-1] += " " + lines[i].strip()
        i += 1
    env = "enumerate" if ordered else "itemize"
    body = "\n".join(r"  \item %s" % render_inline(it, ctx) for it in items)
    return "\\begin{%s}\n%s\n\\end{%s}" % (env, body, env), i


def _take_paragraph(lines: List[str], i: int, ctx: Ctx) -> Tuple[str, int]:
    para: List[str] = []
    while i < len(lines) and lines[i].strip() and not _ITEM_RE.match(lines[i]):
        para.append(lines[i].strip())
        i += 1
    return render_inline(" ".join(para), ctx), i


def split_sections(body: str) -> List[Tuple[Optional[str], str]]:
    """Split a node body on `### Heading` lines -> [(heading|None, chunk), ...]."""
    matches = list(_H3_RE.finditer(body))
    if not matches:
        return [(None, body)]
    sections: List[Tuple[Optional[str], str]] = []
    if body[: matches[0].start()].strip():
        sections.append((None, body[: matches[0].start()]))
    for j, m in enumerate(matches):
        end = matches[j + 1].start() if j + 1 < len(matches) else len(body)
        sections.append((m.group(1).strip(), body[m.end():end]))
    return sections


def render_see_also(chunk: str, ctx: Ctx) -> str:
    """The `### See also` list -> a styled cross-reference block (each item: a link + a gloss)."""
    rows = [r"  \item %s" % render_inline(m.group(3).strip(), ctx)
            for m in (_ITEM_RE.match(line) for line in chunk.split("\n")) if m]
    if not rows:
        return ""
    return "\\webheading{See also}\n\\begin{seealso}\n%s\n\\end{seealso}" % "\n".join(rows)


def render_body(body: str, ctx: Ctx) -> str:
    """A whole node body -> LaTeX, applying the special-cased sections."""
    parts: List[str] = []
    for heading, chunk in split_sections(body):
        if heading is None:
            parts.append(render_blocks(chunk, ctx))
        elif heading.lower() == "in plain terms":
            parts.append("\\begin{plainterms}\n%s\n\\end{plainterms}" % render_blocks(chunk, ctx))
        elif heading.lower() == "see also":
            parts.append(render_see_also(chunk, ctx))
        else:
            parts.append("\\webheading{%s}\n\n%s" % (
                render_inline(heading, ctx), render_blocks(chunk, ctx)))
    return "\n\n".join(p for p in parts if p.strip())

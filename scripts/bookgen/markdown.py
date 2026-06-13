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
# any ATX heading line (any level): captures the heading text. Top-level `### ` headings are
# peeled off by split_sections; this catches the rest (e.g. a `## Illustration` nested inside a
# section), which would otherwise fall through to the paragraph path and print its `#`s literally.
_HEADING_RE = re.compile(r"^#{1,6}\s+(.*)$")


def render_blocks(md: str, ctx: Ctx) -> str:
    """A chunk of markdown with no `###` headings -> LaTeX paragraphs and lists."""
    out: List[str] = []
    lines = md.split("\n")
    i = 0
    while i < len(lines):
        if not lines[i].strip():
            i += 1
            continue
        if lines[i].lstrip().startswith("$$"):
            block, i = _take_display_math(lines, i)
            out.append(block)
            continue
        hm = _HEADING_RE.match(lines[i])
        if hm:
            out.append(r"\webheading{%s}" % render_inline(hm.group(1).strip(), ctx))
            i += 1
        elif _ITEM_RE.match(lines[i]):
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


def _take_display_math(lines: List[str], i: int) -> Tuple[str, int]:
    """A `$$ … $$` display-math block (on one line or spanning several) -> a LaTeX display equation.

    The content between the `$$` fences is emitted verbatim (never escaped), so authors write
    ordinary LaTeX maths — fractions, subscripts, `aligned`, etc. — straight into the body.
    """
    first = lines[i].strip()
    rest = first[2:].strip()                      # whatever follows the opening `$$`
    parts: List[str] = []
    if rest.endswith("$$"):                        # opens and closes on the same line: $$ … $$
        parts.append(rest[:-2].strip())
        i += 1
    else:
        if rest:
            parts.append(rest)
        i += 1
        while i < len(lines):
            s = lines[i].strip()
            if s.endswith("$$"):
                if s[:-2].strip():
                    parts.append(s[:-2].strip())
                i += 1
                break
            parts.append(s)
            i += 1
    inner = "\n".join(p for p in parts if p)
    return "\\[\n%s\n\\]" % inner, i


def _take_paragraph(lines: List[str], i: int, ctx: Ctx) -> Tuple[str, int]:
    para: List[str] = []
    while (i < len(lines) and lines[i].strip()
           and not _ITEM_RE.match(lines[i]) and not _HEADING_RE.match(lines[i])
           and not lines[i].lstrip().startswith("$$")):
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
    """The `### See also` list -> a styled cross-reference block (each item: a link + a gloss).

    An item may wrap across several lines; a non-marker line continues the previous item (the same
    folding `_take_list` does), so a wrapped gloss is never truncated at the line break.
    """
    items: List[str] = []
    for line in chunk.split("\n"):
        m = _ITEM_RE.match(line)
        if m:
            items.append(m.group(3).strip())
        elif line.strip() and items:
            items[-1] += " " + line.strip()
    if not items:
        return ""
    rows = "\n".join(r"  \item %s" % render_inline(it, ctx) for it in items)
    return "\\webheading{See also}\n\\begin{seealso}\n%s\n\\end{seealso}" % rows


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

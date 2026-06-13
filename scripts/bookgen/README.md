# bookgen — the encyclopedia builder

Typesets a selection of `web/` nodes as a printable encyclopedia (LaTeX → PDF): the long-term
"personal encyclopedia of philosophy" the node bodies are written toward (see `schemas/_style.md`).
Run it through the launcher `scripts/book.py` or as `python -m bookgen`.

```sh
uv run --with pyyaml python scripts/book.py                 # all content nodes -> book/encyclopedia.{tex,pdf}
uv run --with pyyaml python scripts/book.py --style encyclopedia  # only finished (tagged) entries
uv run --with pyyaml python scripts/book.py --type concept  # only the concept entries
uv run --with pyyaml python scripts/book.py concept-chinese-room claim-substrate-independence
uv run --with pyyaml python scripts/book.py --columns 1 --no-pdf   # single column, .tex only
uv run --with pyyaml python scripts/book.py --font bookman   # set the text font (see below)
uv run --with pyyaml python scripts/book.py --help          # every option
```

`--font default|bookman|palatino|times|charter` (default `default` = Latin Modern) picks the text
face; all are libre fonts shipped with TeX Live / MacTeX, loaded by file under Unicode engines so
no system install is needed. Maths stays Computer Modern (only the few inline symbols), which pairs
cleanly with any of them. `bookman` (TeX Gyre Bonum) gives the classic old-encyclopedia look.

`--style encyclopedia|legacy|any` (default `any`) filters the bulk type/`--all` selection by each
node's `style:` conversion tag — the marker recording whether a body has been brought up to the
encyclopedia standard (`schemas/_style.md`). It never drops an explicitly-named id, so naming a
node always includes it. The `/build-encyclopedia` command defaults this to `encyclopedia`, so the
published book carries only finished entries.

## What it produces

- **Alphabetised entries**, two columns, with a thin column rule. Leading articles are ignored
  when filing (*The Chinese Room* sits under **C**).
- A **guide word** in the running head and a full-width **letter band** starting each letter.
- Each entry: a bold **headword**, a small italic etiquette line (type · status · `after <Author>`),
  then the node body.
- **Cross-references** follow old-encyclopedia convention. A reference is labelled by the target's
  **headword** (the word it is filed under) set in small caps; a node with no headword falls back
  to its full title in italics, so a sentence-length title does not shout in small caps. (Term-like
  types — concept, position, source, character — are small-capped even without an explicit headword,
  since their titles are already headword-like.) A reference standing alone inside parentheses is a
  *pointer*, so it is rewritten `(see HEADWORD)` (one "see" for a comma-run of them); a reference
  woven into the sentence as a noun keeps the bare small-caps/italic label. Each becomes a clickable
  hyperlink when the target is also an entry in the same volume.
- `### In plain terms` → a shaded aside; `### See also` → a styled cross-reference list.
- **Mathematics**: inline `$…$` and display `$$…$$` (its own line[s]) pass to LaTeX verbatim via
  `amsmath` — `\frac`, sub/superscripts, `aligned`, etc. The `$` must hug its content, so a prose
  dollar stays literal. Single Unicode symbols in prose (`∴ ∧ Φ Σ`) are mapped to maths by `latex.py`.
- Front matter: a clickable **List of Entries**; PDF bookmarks for letters and entries.

## Engines

Like `scripts/graph.py` with Graphviz `dot`, the PDF step is optional: the `.tex` is always
written, and a LaTeX engine is used only if found (PATH plus the usual TeX bin dirs, so a fresh
MacTeX works before a shell restart). Any engine works — the generated `.tex` maps every non-ASCII
glyph the corpus uses (em dashes, `∴ ∧ ¬ ⟹ ↦ Φ Σ ℛ`, subscripts, accents) to a portable LaTeX
form. `--engine auto` prefers `tectonic`, then `latexmk`, `xelatex`, `lualatex`, `pdflatex`.

Install one: `brew install --cask mactex-no-gui` · `apt-get install texlive-xetex
texlive-latex-extra` · or `tectonic` (self-contained, fetches packages on demand).

LaTeX intermediates (`.aux`, `.log`, `.fls`, `.fdb_latexmk`, `.xdv`, …) are written to a
top-level `build/` directory (git-ignored), so only the deliverables — `encyclopedia.tex` and
`encyclopedia.pdf` — land in `book/`.

## Module layout (one concern each)

| module | responsibility |
|--------|----------------|
| `config.py`    | paths, constants, and the `BookOptions` dataclass |
| `nodes.py`     | load `web/` nodes (`Node`); resolve a selection into an ordered id list |
| `latex.py`     | LaTeX escaping, smart quotes, the portable Unicode map |
| `inline.py`    | inline markdown → LaTeX; cross-reference resolution (`Ctx`) |
| `markdown.py`  | block markdown → LaTeX (lists, paragraphs, sections, special blocks) |
| `templates.py` | the LaTeX preamble / title page / front-matter strings |
| `document.py`  | ordering, grouping, etiquette — assemble the whole document |
| `compile.py`   | locate a LaTeX engine and run it |
| `cli.py`       | argument parsing and orchestration |

It reuses the sibling top-level `weblinks.py` for id↔path math and link resolution, so a cited
node is rendered the same way the linter renders it.

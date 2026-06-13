---
description: Regenerate the encyclopedia book (book/encyclopedia.tex + .pdf) from the web via scripts/book.py.
---
Rebuild the encyclopedia from the current web. Optional passthrough to `scripts/book.py`: **$ARGUMENTS**

`$ARGUMENTS` is forwarded verbatim to `scripts/book.py`. Empty = the whole book (all content
nodes). Otherwise it may be a node selection (ids / slugs / `.md` paths, `--type`, `--all`) and/or
formatting flags (`--columns`, `--title`, `--sort`, `--no-pdf`, …). See `scripts/bookgen/README.md`.

Steps:
1. **Refresh derived data first.** Run `uv run --with pyyaml python scripts/lint.py` so the
   `[[id]]` links and `web/INDEX.md` are current before typesetting.
2. **Build.** Run `uv run --with pyyaml python scripts/book.py $ARGUMENTS`. With no `--output`,
   it writes `book/encyclopedia.tex` and compiles `book/encyclopedia.pdf`; LaTeX intermediates go
   to the git-ignored `build/`. If no LaTeX engine is found, `book.py` still writes the `.tex` and
   says so — relay that and point me to install one (`mactex-no-gui` / `texlive-xetex` / tectonic).
3. **Report.** State the entry count, the output paths, and whether the PDF built. If I asked for
   a subset (a selection or `--no-pdf`), note that the default deliverables in `book/` were *not*
   overwritten only if a custom `--output` was supplied; otherwise they were.

Do not commit unless I ask. Note that `book/encyclopedia.{tex,pdf}` are tracked deliverables, so a
plain rebuild will show them as modified.

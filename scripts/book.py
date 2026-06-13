#!/usr/bin/env python3
"""
book.py — launcher for the encyclopedia builder.

Typesets a selection of web nodes as a printable encyclopedia (LaTeX -> PDF). The real work
lives in the `bookgen` package (one module per concern); this file is just the entry point so the
familiar `.venv/bin/python scripts/book.py …` invocation keeps working. `python -m bookgen` runs
the same thing.

    .venv/bin/python scripts/book.py                 # all content nodes -> book/encyclopedia.{tex,pdf}
    .venv/bin/python scripts/book.py --type concept  # only the concept entries
    .venv/bin/python scripts/book.py concept-chinese-room claim-substrate-independence
    .venv/bin/python scripts/book.py --columns 1 --no-pdf   # single column, emit .tex only

See bookgen/README.md for the package layout, and `--help` for every option.
"""
from bookgen.cli import main

if __name__ == "__main__":
    main()

# Makefile — deterministic, non-AI operations for the philosophy web.
#
# These are the recurring shell/Python commands the workflow uses (lint, build the encyclopedia,
# preview pages, locate nodes, report conversion progress). Run them directly instead of
# re-deriving the commands each time:  make help
#
# Python always goes through uv (project rule, CLAUDE.md "Running Python (uv only)"). The PDF/
# preview steps need a LaTeX engine and Ghostscript respectively; both degrade or no-op cleanly.

PY      := uv run --with pyyaml python
GS      := gs
PREVIEW := build/preview

# Overridable on the command line, e.g. `make book STYLE=any`, `make preview FROM=3 TO=4`.
STYLE ?= encyclopedia
# which entries `make book` includes: encyclopedia | legacy | any
FONT ?= default
# text font for `make book` / `make entry`: default | bookman | palatino | times | charter
DPI ?= 130
# resolution for `make preview` / `make entry` PNG renders
FROM ?= 1
# first page for `make preview`
TO ?= 9999
# last page for `make preview`
PDF ?= book/encyclopedia.pdf
# PDF that `make preview` renders

.DEFAULT_GOAL := help
.PHONY: help lint lint-check book book-all graph all preview entry progress find clean clean-preview

help:  ## list the available targets
	@grep -E '^[a-zA-Z0-9_-]+:.*## ' $(MAKEFILE_LIST) \
	  | sed -E 's/:.*## /\t/' | sort | awk -F'\t' '{printf "  make %-14s %s\n", $$1, $$2}'
	@echo
	@echo "  vars: STYLE=$(STYLE)  DPI=$(DPI)  FROM=$(FROM) TO=$(TO)  PDF=$(PDF)  ID=<node>  Q=<text>"

lint:  ## integrity check + render [[id]] links + regenerate web/INDEX.md
	$(PY) scripts/lint.py

lint-check:  ## report pending lint changes without writing (CI / pre-commit dry run)
	$(PY) scripts/lint.py --check

book: lint  ## build the encyclopedia -> book/encyclopedia.{tex,pdf}  (STYLE=…, FONT=…)
	$(PY) scripts/book.py --style $(STYLE) --font $(FONT)

book-all: lint  ## build the whole book including unconverted entries (STYLE=any, FONT=…)
	$(PY) scripts/book.py --style any --font $(FONT)

graph:  ## regenerate the Graphviz view -> graph/web.{dot,svg}  (needs the `dot` binary)
	$(PY) scripts/graph.py

all: book graph  ## build both deliverables: the encyclopedia (book) + the Graphviz view (graph)

preview:  ## render PDF pages to PNGs in build/preview  (PDF=, FROM=, TO=, DPI=)
	@mkdir -p $(PREVIEW)
	$(GS) -dNOPAUSE -dBATCH -sDEVICE=png16m -r$(DPI) -dFirstPage=$(FROM) -dLastPage=$(TO) \
	  -sOutputFile=$(PREVIEW)/p%03d.png $(PDF)
	@echo "wrote $(PREVIEW)/  (pages $(FROM)-$(TO) of $(PDF))"

entry: lint  ## typeset ONE node single-column and render it for eyeballing  (ID=<node-id-or-slug>)
	@test -n "$(ID)" || { echo 'usage: make entry ID=<node-id-or-slug>'; exit 2; }
	$(PY) scripts/book.py "$(ID)" --columns 1 --font $(FONT) --output book/_entry.tex
	@mkdir -p $(PREVIEW)
	$(GS) -dNOPAUSE -dBATCH -sDEVICE=png16m -r$(DPI) -sOutputFile=$(PREVIEW)/entry-%03d.png book/_entry.pdf
	@echo "wrote $(PREVIEW)/entry-*.png"

progress:  ## report encyclopedia-style vs legacy node counts
	@printf 'encyclopedia: %s\nlegacy:       %s\n' \
	  "$$(grep -rl '^style: encyclopedia' web/ | wc -l | tr -d ' ')" \
	  "$$(grep -rl '^style: legacy' web/ | wc -l | tr -d ' ')"

find:  ## locate node file(s) by id or slug  (Q=<text>)
	@test -n "$(Q)" || { echo 'usage: make find Q=<id-or-slug>'; exit 2; }
	@grep -rl -- "$(Q)" web/ || echo "no match for '$(Q)'"

clean-preview:  ## delete the PNG previews
	rm -rf $(PREVIEW)

clean: clean-preview  ## delete LaTeX intermediates (build/) and book scratch (book/_*); keep deliverables
	rm -rf build
	rm -f book/_*

# Philosophy Web — project rules

This repo is a **semantic web of philosophical objects** (concepts, claims, arguments,
questions, positions, sources) plus AI **characters** who debate into it. The web is the
durable substrate; treatises are later written *from* it.

## Two artifacts, never confused
- `transcripts/` — the **dialogue**: append-only, linear, full of rhetoric. Raw record of debates.
- `web/` — the **distilled graph**: atomic, deduplicated nodes that cross-reference each other.

Dialogue does **not** get dumped into `web/` verbatim. During a debate, a speaker emits
prose into the transcript AND creates/cites a small number of clean nodes in `web/`.
One utterance is not one node.

## Cardinal rules for writing nodes
1. **Read the schema, then grep, before you create.** Before creating OR editing a node of
   type `T`, read `schemas/T.md` (legal edges, required fields, invariants). Then search
   `web/` for an existing equivalent (`grep -ri "<key phrase>" web/`). If one exists, **cite
   it by id**; do not
   make a near-duplicate. If you create a new node, the body must state *why* it is distinct
   from the closest existing one.
2. **Edges are one-directional and reference nodes by `id`.** The *attacking/supporting/
   citing* node owns the edge. Never store the reverse ("supported-by", "attacked-by") —
   backlinks are **computed** by `scripts/lint.py`, never hand-maintained. The same goes for
   **prose**: cite another node with the `[[id]]` shorthand in bodies and transcripts; lint
   renders it into a clickable `[slug](relpath)` link (derived data — never hand-write the link).
   Only frontmatter edges carry bare ids.
3. **Provenance is mandatory.** Every node has an `author`. For content nodes (claim,
   concept, argument, question, position) the author is **never a character** — it is a real
   philosopher/scientist with an established association (e.g. `block`), `generic` for a
   well-known idea with no clear source, or `mishka` for ideas introduced while building this
   web. Only a `character` portfolio node is authored by its character id. This is what lets a
   treatise attribute ideas later.
4. **Atomic claims.** A claim is one truth-apt proposition. "Thought requires biology" and
   "consciousness requires carbon chemistry" are **different claims** — never collapse them.
5. **Never silently merge or reword another author's node.** Suspected duplicates go to
   `proposals/` for human review (`/reconcile`). Precision beats tidiness.
6. A body of a claim, argument, concept, position or question should be written from a neutral perspective, without mentioning a specific character. References to works of a real philosopher or scientist are ok. "Alvin claims X" is bad. Instead just use "X". What each character claims or thinks is a function of that character only and should be stored there.
7. Nodes authored by the user, but that really are from a well-known person (a philsopher, scientist, writer etc) should be attributed to that person. 
8. **Encyclopedia style** (full standard + worked example: `schemas/_style.md`). Concept,
   position, argument and question nodes are written as entries in a good general encyclopedia
   (Encyclopedia Britannica is the model) — the long-term goal is to collect them into a PDF, a
   personal encyclopedia of philosophy, so each entry must stand alone on a printed page. Lead
   with a plain-language definition, then expand into the fine points and nuances; be
   self-contained (links via `[[id]]` enrich, never required reading); stay approachable to an
   interested amateur without sacrificing precision; include a concrete example or canonical
   case wherever the subject allows; and write real prose with clean formatting (`###`
   subheadings for longer entries) — never `label: fragment` notes. The style never costs the
   web its cross-links: weave `[[id]]` links into the prose where they arise naturally, and
   close the entry with a `### See also` section (the very last section, after any
   `### In plain terms`) mapping the entry's related nodes — required for every related node
   the prose didn't absorb, allowed for the body's most important links, each with a clause
   saying how it relates. Claims stay atomic and short, but still read as prose. 
   
   Avoid em-dash constructions in prose (bad: "The four varieties are mutually compatible — a single case may exhibit several at
  once — but they spring from different sources and call for different remedies", better: "These four varieties can overlap in a single case, yet each has a distinct source and calls for a distinct remedy.")

   **Mathematics:** write formulas in LaTeX — inline between single dollars (`$x_i^2$`), display by
   fencing with `$$` on their own lines; content between the delimiters renders verbatim. A single
   symbol in prose can just be the Unicode glyph (`∴ ∧ Φ Σ`). Details + a worked fixture
   (`web/test/rendering-test.md`): `schemas/_style.md` ("Mathematics").
9. **Optional `### In plain terms` section.** When a content node (claim, concept, argument,
   question, position) is technical or jargon-heavy, end its body with a `### In plain terms`
   section: a short, self-contained explanation aimed at a casual visitor to the repo who has
   **no** philosophy training and **has not read the rest of the web**. It is strictly
   *additive* — it never overrides, softens, or replaces the precise prose above it, and it must
   not dilute the node's nuances. Write it to stand alone: avoid jargon, or unpack in a phrase any
   term you genuinely cannot avoid, and never lean on reading order — a casual reader may land here
   first. When the section refers to **another move in the web** (a reply it answers, an objection
   it rebuts, a case it sharpens), don't write "the previous reply": name that move in a few plain
   words *and* link it with `[[id]]`, so the gloss carries the gist and the link carries the full
   story. Keep such links to the genuinely-referenced moves; don't gratuitously link every concept.
   Add it only where it earns its keep — a node already
   readable by a layperson does not need one. Some nodes unavoidably require a specialized term or
   two; simplify as far as you can there without flattening the distinctions, rather than skipping
   the section. The heading is exactly `### In plain terms`; it follows the main prose, and only
   a `### See also` section (rule 8) may come after it. When in doubt about a node, ask.

## Where things live
- Per-type schemas (read before create/edit): `schemas/<type>.md`
- Body style standard (encyclopedia entries) + worked example: `schemas/_style.md`
- Argument patterns + their critical questions (optional `pattern:` on an argument): `patterns/`
  — a reference library, not web nodes. Citing a pattern names the move's standard attack surface;
  raise its critical questions when objecting. See `patterns/_README.md`.
- Node schema + write protocol: `.claude/skills/web-protocol/SKILL.md` (preloaded into debaters)
- Character personas (stable): `.claude/agents/<id>.md`
- Character positions (evolving): `web/characters/<id>.md` — a character reads this at the
  start of each turn; it is the character's memory between turns.
- Integrity check / backlink + index generation: `scripts/lint.py` (see below)
- Visual graph of the web (claims/arguments/concepts + relations): `scripts/graph.py` →
  `graph/web.svg`. Manual, on demand; needs the Graphviz `dot` binary (`brew install graphviz`).
  Not in the pre-commit hook. Regenerate after sizable web changes; see README "Building the graph".
- Printable encyclopedia (selected nodes → LaTeX → PDF): `scripts/book.py` (launcher) over the
  `scripts/bookgen/` package → `book/encyclopedia.{tex,pdf}`. Manual, on demand; the PDF step needs
  a LaTeX engine but degrades to `.tex` without one. See `scripts/bookgen/README.md`. This is the
  delivery vehicle for the encyclopedia style of rule 8 / `schemas/_style.md`.

## Make targets (use these for routine ops)
Recurring non-AI operations are captured in the `Makefile` — **prefer them over re-typing the
commands**: `make lint`, `make book` (build the encyclopedia; `STYLE=any` for everything),
`make entry ID=<node>` (typeset + render one node to `build/preview/`), `make preview`,
`make progress` (encyclopedia vs legacy counts), `make find Q=<text>`, `make clean`. `make help`
lists them. They wrap the scripts below; the Python still runs through uv.

## Running Python (uv only)
**Always run the project's Python through `uv`** — never a system `python`, and never call
`.venv/bin/python` directly. The canonical invocation pulls in dependencies on the fly:

```sh
uv run --with pyyaml python scripts/lint.py        # integrity check + regenerate web/INDEX.md
uv run --with pyyaml python scripts/book.py        # build the encyclopedia PDF (see below)
```

This needs no pre-created venv; `uv` resolves an interpreter and the listed deps per run. (If you
prefer a persisted environment, `uv venv` once then `uv pip install pyyaml` — but still launch via
`uv run`.) The only dependency is PyYAML; `book.py` additionally shells out to a LaTeX engine and
`graph.py` to Graphviz `dot`, both optional and both degrading gracefully when absent.

The linter rewrites `web/INDEX.md` (computed backlinks + answer lists), **renders the `[[id]]`
prose shorthand in node bodies and transcripts into clickable `[slug](relpath)` links** (and
refreshes existing ones), and prints any integrity issues; run it after every debate turn and
before committing. Because it rewrites bodies, treat the rendered links as generated output — edit
the `[[id]]` shorthand, not the link. `scripts/lint.py --check` reports pending changes without
writing (for CI / pre-commit dry runs). The id↔link machinery lives in `scripts/weblinks.py`.

## A character's turn (summary)
Read your persona → read `web/characters/<you>.md` → read the relevant slice of `web/` and
recent `transcripts/` → argue (prose to transcript) → cite/create nodes per the protocol →
update your own positions portfolio → return a short summary.

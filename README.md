# philosophy-web

A living, machine-checkable record of philosophical **arguments** — not essays, but the
atomic moves essays are made of: claims, the concepts they use, the arguments that connect
them, the questions they answer, and who said what. Each idea is stored once, as a node, and
linked to the others it supports, attacks, or presupposes. The result is a graph you can
navigate, audit, and later write treatises *from*.

It is built and contested by a small cast of AI **characters** who debate into it, alongside
your own contributions. The machinery is subject-agnostic; what's actually being debated lives
in per-directory READMEs, not here:

> 🧭 **What's in it / where to start**
> - **[`web/README.md`](web/README.md)** — the governing questions and a guided map of the
>   arguments currently recorded (the present corpus is on the **philosophy of mind & AI**).
> - **[`web/characters/README.md`](web/characters/README.md)** — the cast of debaters.
> - **[`graph/README.md`](graph/README.md)** — the whole web as one picture.
> - To just browse: open any node — most end with a plain-language *"In plain terms"* gloss and
>   link onward through the web. No need to read in order.

This top-level README covers **what it is, how it works, and how to use it.**

---

## Why it exists

Ordinary philosophical writing buries its structure. A 30-page paper might turn on a single
premise, but you have to reconstruct the skeleton by hand, and the same idea gets re-stated in
slightly different words across a literature until nobody can tell which claims are really the
same. This project takes the opposite approach:

- **One idea, one node.** A claim is a single truth-apt proposition, written once. "Thought
  requires biology" and "consciousness requires carbon chemistry" are *different* claims and
  never collapsed.
- **Arguments are explicit.** An argument names its premises (by id), its conclusion, and —
  crucially — its *weakest premise*, the place a future objection should land.
- **Disagreement is first-class.** Objections and rebuttals are just arguments with `attacks` /
  `responds_to` edges. The graph records the live cruxes, not a tidy consensus.
- **Provenance is mandatory.** Every node carries an `author` — a real philosopher, a generic
  attribution, or the web-builder — so a treatise can attribute ideas correctly later. (What a
  *character* believes is stored separately; characters never author the shared content.)

The payoff: you can ask the graph questions ("what attacks substrate-independence?", "which
arguments grab the degree horn of a sorites?"), and an integrity script keeps it honest.

---

## How it works

**Two artifacts, never confused.**
- `transcripts/` — the **dialogue**: append-only, linear, rhetorical. The raw record of debates.
- `web/` — the **distilled graph**: atomic, deduplicated nodes that cross-reference each other
  (by id in frontmatter edges; as clickable `[[id]]` links in prose).

One utterance is *not* one node. During a debate a speaker writes prose to the transcript and
distils a few clean nodes into the web.

**Node types** (one schema each, in `schemas/<type>.md`):

| type | what it is |
|------|------------|
| `concept`  | a term and its definition(s), including competing senses |
| `claim`    | one truth-apt proposition — the atom of the web |
| `argument` | an inference: premises → conclusion, or a move for/against another node |
| `question` | an open issue; claims that `answer` it are candidate answers |
| `position` | a named stance bundling commitments |
| `source`   | a citable work (book, paper) |
| `character`| a debater's evolving portfolio of commitments |

**Edges are one-directional and reference nodes by id.** The supporting/attacking/citing node
*owns* the edge (`premise`, `concludes`, `supports`, `attacks`, `responds_to`, `answers`,
`uses_concept`, `presupposes`, …), in frontmatter, by bare id. Reverse links ("attacked-by") are
**never** stored by hand — they are *computed* by `scripts/lint.py` into `web/INDEX.md`.

**Prose references are clickable.** In a node body or transcript you cite another node with the
`[[id]]` shorthand; `scripts/lint.py` renders it into a relative Markdown link
(`[slug](../claims/…​.md)`), so browsing on GitHub you can click straight from a claim to the
argument that attacks it. Like the backlinks, these links are *generated* — you author `[[id]]`,
never the link itself.

**Characters split in two.** A character's stable voice and method live in a subagent
(`.claude/agents/<id>.md`); their *evolving commitments* live in a node
(`web/characters/<id>.md`) that the character re-reads at the start of each turn. The web is the
character's memory between otherwise stateless turns. (Who the current debaters are:
[`web/characters/README.md`](web/characters/README.md).)

---

## Repository layout

```
CLAUDE.md                  always-on project rules (in context every session)
README.md                  this file — what it is / how it works / how to use it
schemas/                   per-type node schemas — read schemas/<type>.md before
                           creating/editing a node; legal edges are enforced by lint.py
web/                       the distilled graph (the durable substrate); see web/README.md
  concepts/ claims/ arguments/ questions/ positions/ sources/ characters/
  INDEX.md                 GENERATED by lint.py — node list + computed backlinks; do not edit
  README.md                the corpus: governing questions + map of arguments
  characters/README.md     the cast of debaters
transcripts/               append-only debate logs + treatise drafts
proposals/                 merge proposals from the reconciler (await human approval)
graph/                     GENERATED visual map (web.svg + web.dot) — see graph/README.md
scripts/lint.py            integrity check + backlink/index generator (no model calls)
scripts/graph.py           render the web as a Graphviz SVG (needs the `dot` binary)
scripts/pre-commit         git hook wrapper for lint.py
.claude/
  skills/web-protocol/     the node schema + write discipline (preloaded into debaters)
  agents/                  character subagents (mu-043, alvin, sophia, reconciler)
  skills/, commands/       /debate /claim /reconcile /treatise /import-argument /new-character
```

---

## Setup

The integrity linter needs PyYAML. Use a [uv](https://docs.astral.sh/uv/)-managed virtual
environment rather than a system Python:

```bash
uv venv                            # one-time: create .venv/
uv pip install pyyaml              # one-time: the only dependency
.venv/bin/python scripts/lint.py   # integrity check + (re)build web/INDEX.md
```

`uv run --with pyyaml python scripts/lint.py` does the same without a persisted venv. After
`git init`, wire the hook so every commit is linted:

```bash
ln -sf ../../scripts/pre-commit .git/hooks/pre-commit
```

Run the linter after every debate turn and before committing. It rewrites `web/INDEX.md`,
renders `[[id]]` links, verifies that every edge points at a real node, and warns about dangling
references and contested claims with no recorded attacker.

### Building the graph (optional)

`scripts/graph.py` renders the web as a single picture into [`graph/web.svg`](graph/web.svg)
(coloured by node type and relation; see [`graph/README.md`](graph/README.md)). It shells out to
**Graphviz**, so you need the `dot` binary once:

```bash
brew install graphviz            # macOS
sudo apt-get install graphviz    # Debian/Ubuntu
sudo dnf install graphviz        # Fedora
```

```bash
.venv/bin/python scripts/graph.py                      # writes graph/web.dot and graph/web.svg
.venv/bin/python scripts/graph.py --engine dot --png   # different layout; also drop a web.png
```

No extra Python packages are needed (it reuses the linter's parsing). If `dot` isn't installed
the script still writes `graph/web.dot` and tells you how to install Graphviz — it never
hard-fails.

---

## How to use it

- `/debate <topic>` — run one or more turns; characters write prose to a transcript and distil
  nodes into the web. You control turn order.
- `/claim <your idea>` — add your own node with your wording preserved (no AI rephrasing).
- `/import-argument <text>` — bring an external argument (from the literature or you) into the
  web: triage, then decompose into properly-formatted nodes.
- `/reconcile` — surface suspected duplicate nodes as proposals for your review.
- `/treatise <thesis>` — draft a piece *from* the recorded web, attributed by `author`.
- `/new-character` — scaffold a new debater (persona subagent + positions portfolio).

### The discipline for writing nodes (the short version)
1. **Read the schema, then grep, before you create.** If an equivalent node exists, cite it by
   id; don't make a near-duplicate.
2. **Keep claims atomic** and bodies **neutral** — "X", not "Alvin claims X". What a character
   thinks belongs only in that character's portfolio.
3. **Attribute content to real people**, never to characters.
4. **Never silently merge or reword another author's node** — suspected duplicates go to
   `proposals/` for human review. Precision beats tidiness.

---

## Design principles & safeguards

- **Direct-writing, with guardrails.** Nodes are written directly, but grep-before-create, a
  *propose-only* reconciler (it never edits `web/`), and a deterministic lint script keep the
  graph clean without a heavyweight pipeline.
- **Computation over hand-maintenance.** Backlinks, the index, and prose links are generated, so
  they can't drift out of sync with the edges that own them.
- **Human in the loop for anything destructive.** Merges and rewordings of others' nodes are
  proposals, not actions.

## Known limits

- Deduplication is grep + discipline + a propose-only reconciler. Once the graph grows past a few
  hundred claims and paraphrase-duplicates start slipping through, add embedding-based similarity
  (e.g. an MCP tool the reconciler calls). The architecture isolates that change to the reconciler.
- The orchestrating session accumulates the transcript, so very long debates grow its context.
  Start a fresh session per debate; the web persists the state between them.

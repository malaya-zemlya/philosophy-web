# philosophy-web

A living, machine-checkable record of philosophical **arguments** — not essays, but the
atomic moves that essays are made of: claims, the concepts they use, the arguments that
connect them, the questions they answer, and who said what. Each idea is stored once, as a
node, and linked to the others it supports, attacks, or presupposes. The result is a graph
you can navigate, audit, and later write treatises *from*.

The web is built and contested by a small cast of AI **characters** who debate into it, plus
your own contributions. Its current subject matter is the **philosophy of mind and AI**:
above all, *what would it take for an artificial system to have a mind — or moral status?*

---

## Why it exists

Ordinary philosophical writing buries its structure. A 30-page paper might turn on a single
premise, but you have to reconstruct the skeleton by hand, and the same idea gets re-stated
in slightly different words across a literature until nobody can tell which claims are really
the same. This project takes the opposite approach:

- **One idea, one node.** A claim is a single truth-apt proposition, written once. "Thought
  requires biology" and "consciousness requires carbon chemistry" are *different* claims and
  never collapsed.
- **Arguments are explicit.** An argument names its premises (by id), its conclusion, and —
  crucially — its *weakest premise*, the place a future objection should land.
- **Disagreement is first-class.** Objections and rebuttals are just arguments with `attacks`
  / `responds_to` edges. The graph records the live cruxes, not a tidy consensus.
- **Provenance is mandatory.** Every node carries an `author` — a real philosopher, a generic
  attribution, or the web-builder — so a treatise can attribute ideas correctly later. (What a
  *character* believes is stored separately; characters never author the shared content.)

The payoff: you can ask the graph questions ("what attacks substrate-independence?", "which
arguments grab the degree horn of a sorites?"), and an integrity script keeps it honest.

---

## The question it's built around

The governing question is **`question-substrate-independence`: *Are mental states
substrate-independent?*** — and its applied cousin, **`question-llm-moral-status`: *Do large
language models have moral status?*** Almost every node hangs off these.

The debate as currently recorded runs roughly like this:

- **Functionalism & the grain problem.** If mental states are individuated by *functional
  role* (`concept-functionalism`), then silicon could realise them. But at *what grain* is a
  role specified (`concept-grain`)? Too coarse and a mere input–output mimic counts as minded;
  too fine and only biology qualifies (`argument-role-grain-dilemma`).
- **Behaviour as evidence.** The case that an LLM's behaviour is best explained by its
  realising the relevant roles (`argument-behavioral-parity` → `claim-llm-has-mental-states`).
- **Block's two counterexamples.** The *lookup-table / "Blockhead"* machine (right outputs,
  no internal processing — `concept-lookup-table-mind`) and the *Chinese Nation*
  (`concept-chinese-nation`, which *has* the organisation yet allegedly lacks qualia). These
  press, respectively, that behaviour isn't sufficient and that even organisation may leave a
  *phenomenal residue*.
- **Replies to Blockhead.** That a finite table can't match an open-ended mind
  (`argument-lookup-table-combinatorial-impossibility`); that a behaviour-matching table is
  physically impossible — bigger than the universe (`argument-lookup-table-physical-impossibility`);
  and a dilemma — such a table is *either* physically unrealisable *or* a merely imaginary
  object about which the "no-mind" intuition isn't compelled (`argument-blockhead-dilemma`),
  defended by an epistemology-of-intuition asymmetry (`argument-intuition-domain-asymmetry`).
- **The hard part: consciousness.** The explanatory gap (`argument-explanatory-gap`), its
  deflation via phenomenal concepts and a fading/dancing-qualia reductio
  (`argument-gap-deflated-by-phenomenal-concepts`), and the residue theorist's reply that the
  reductio begs the question (`argument-dancing-qualia-begs-the-question`).
- **A unifying meta-argument.** `concept-continuity-argument-schema` — the topological
  "a continuous function from a connected space to a discrete one is constant" form that
  underlies the *sorites/heap*, *Ship of Theseus*, *gradual neuron-by-neuron replacement*, and
  *Parfit-style rewiring* cases. Read contrapositively it yields an exhaustive menu of five
  responses, each a named philosophical position.

You don't have to take this on trust: open `web/INDEX.md` (generated) for the full node list
with computed backlinks.

---

## How knowledge is stored

**Two artifacts, never confused.**
- `transcripts/` — the **dialogue**: append-only, linear, rhetorical. The raw record of debates.
- `web/` — the **distilled graph**: atomic, deduplicated nodes that cross-reference by id.

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
`uses_concept`, `presupposes`, …). Reverse links ("attacked-by") are **never** stored by hand —
they are *computed* by `scripts/lint.py` into `web/INDEX.md`.

**Characters split in two.** A character's stable voice and method live in a subagent
(`.claude/agents/<id>.md`); their *evolving commitments* live in a node
(`web/characters/<id>.md`) that the character re-reads at the start of each turn. The web is
the character's memory between otherwise stateless turns.

---

## The characters

- **MU-043** — an LLM that argues *for* the moral status of AI; weighs functional and
  behavioural evidence heavily, suspicious of substrate-based criteria.
- **Alvin** — an analytic theologian in the vein of Plantinga and Swinburne; takes seriously
  that the mind may not be exhausted by functional organisation, fond of numbered premises and
  Bayesian arguments.
- **Sophia** — a mediator who takes no side on the governing question; her job is to steelman
  both parties, isolate the crux, and expose merely verbal disputes.

Each is a genuine interlocutor: they can concede, and they track what would change their mind.
New debaters are scaffolded with `/new-character`.

---

## Repository layout

```
CLAUDE.md                  always-on project rules (in context every session)
README.md                  this file
schemas/                   per-type node schemas — read schemas/<type>.md before
                           creating/editing a node; legal edges are enforced by lint.py
web/                       the distilled graph (the durable substrate)
  concepts/ claims/ arguments/ questions/ positions/ sources/ characters/
  INDEX.md                 GENERATED by lint.py — node list + computed backlinks; do not edit
transcripts/               append-only debate logs + treatise drafts
proposals/                 merge proposals from the reconciler (await human approval)
scripts/lint.py            integrity check + backlink/index generator (no model calls)
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
verifies that every edge points at a real node, and warns about dangling references and
contested claims with no recorded attacker.

---

## Working with it

- `/debate <topic>` — run one or more turns; characters write prose to a transcript and distil
  nodes into the web. You control turn order.
- `/claim <your idea>` — add your own node with your wording preserved (no AI rephrasing).
- `/import-argument <text>` — bring an external argument (from the literature or you) into the
  web: triage, then decompose into properly-formatted nodes.
- `/reconcile` — surface suspected duplicate nodes as proposals for your review.
- `/treatise <thesis>` — draft a piece *from* the recorded web, attributed by `author`.

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
- **Computation over hand-maintenance.** Backlinks and indexes are generated, so they can't
  drift out of sync with the edges that own them.
- **Human in the loop for anything destructive.** Merges and rewordings of others' nodes are
  proposals, not actions.

## Known limits

- Deduplication is grep + discipline + a propose-only reconciler. Once the graph grows past a
  few hundred claims and paraphrase-duplicates start slipping through, add embedding-based
  similarity (e.g. an MCP tool the reconciler calls). The architecture isolates that change to
  the reconciler.
- The orchestrating session accumulates the transcript, so very long debates grow its context.
  Start a fresh session per debate; the web persists the state between them.

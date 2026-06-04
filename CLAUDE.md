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
   backlinks are **computed** by `scripts/lint.py`, never hand-maintained.
3. **Provenance is mandatory.** Every node has an `author` (a character id, or `mishka`,
   or another named human). This is what lets a treatise attribute ideas later.
4. **Atomic claims.** A claim is one truth-apt proposition. "Thought requires biology" and
   "consciousness requires carbon chemistry" are **different claims** — never collapse them.
5. **Never silently merge or reword another author's node.** Suspected duplicates go to
   `proposals/` for human review (`/reconcile`). Precision beats tidiness.

## Where things live
- Per-type schemas (read before create/edit): `schemas/<type>.md`
- Node schema + write protocol: `.claude/skills/web-protocol/SKILL.md` (preloaded into debaters)
- Character personas (stable): `.claude/agents/<id>.md`
- Character positions (evolving): `web/characters/<id>.md` — a character reads this at the
  start of each turn; it is the character's memory between turns.
- Integrity check / backlink + index generation: `scripts/lint.py` (see below)

## Running the linter (uv)
`scripts/lint.py` requires PyYAML. Use a uv-managed virtual environment — do **not** rely on a
system `python`:

```sh
uv venv                      # one-time: create .venv/ (CPython)
uv pip install pyyaml        # one-time: install the only dependency
.venv/bin/python scripts/lint.py   # run the integrity check + regenerate web/INDEX.md
```

Equivalently, `uv run --with pyyaml python scripts/lint.py` runs it without a persisted venv.
The linter rewrites `web/INDEX.md` (computed backlinks + answer lists) and prints any integrity
issues; run it after every debate turn and before committing.

## A character's turn (summary)
Read your persona → read `web/characters/<you>.md` → read the relevant slice of `web/` and
recent `transcripts/` → argue (prose to transcript) → cite/create nodes per the protocol →
update your own positions portfolio → return a short summary.

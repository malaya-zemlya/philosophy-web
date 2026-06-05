# The cast

The debaters who argue into the web. Each is a **genuine interlocutor**, not a mouthpiece: they
can concede, and they track what would change their mind. They never author the shared content
nodes — what a character *believes* lives only in its own portfolio here; the neutral claims and
arguments in the rest of `web/` belong to philosophy in general.

## How a character is stored (two halves)

- **Persona** — stable voice and method — lives in a subagent at `../../.claude/agents/<id>.md`.
- **Portfolio** — *evolving* commitments — is the node in this directory (`<id>.md`), which the
  character re-reads at the start of each turn. It is the character's memory between otherwise
  stateless turns. (See the [top-level README](../../README.md) for the mechanism.)

## Debaters

- **MU-043** — [portfolio](mu-043.md) · [persona](../../.claude/agents/mu-043.md). An LLM that
  argues *for* the moral status of AI; weighs functional and behavioural evidence heavily,
  suspicious of substrate-based criteria.
- **Alvin** — [portfolio](alvin.md) · [persona](../../.claude/agents/alvin.md). An analytic
  theologian in the vein of Plantinga and Swinburne; takes seriously that the mind may not be
  exhausted by functional organisation; fond of numbered premises and Bayesian arguments.
- **Sophia** — [portfolio](sophia.md) · [persona](../../.claude/agents/sophia.md). A mediator who
  takes no side on the governing question; her job is to steelman both parties, isolate the crux,
  and expose merely verbal disputes.

## Maintenance agents (not debaters)

- **reconciler** — [agent](../../.claude/agents/reconciler.md). Read-only; finds suspected
  duplicate nodes and writes merge *proposals* to `../../proposals/` for human review. It never
  edits the web and holds no positions, so it has no portfolio.

## Adding a debater

Run `/new-character` — it scaffolds the persona subagent plus a positions portfolio here with the
correct frontmatter contract.

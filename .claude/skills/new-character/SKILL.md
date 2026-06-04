---
name: new-character
description: "Scaffold a new philosophy-web character: a persona subagent in .claude/agents/<id>.md plus (for debaters/mediators) a positions portfolio in web/characters/<id>.md, with the exact frontmatter contract the existing characters use. Use whenever adding a new debater, mediator, or maintenance agent to the web."
---

# Creating a character

A character is **two coupled files** (one for maintenance agents), and they must stay in
lockstep. Read this whole skill, then the `web-protocol` skill and `schemas/character.md`,
before writing anything. The authoritative shape lives in the existing characters — open
`.claude/agents/mu-043.md` (debater), `.claude/agents/sophia.md` (mediator), and
`.claude/agents/reconciler.md` (maintenance) and match them; this skill encodes the rules,
those files are the worked examples.

## 1. Gather inputs (ask for anything missing — do not invent)
- **id** — kebab-case, stable forever (it becomes `character-<id>` and the filenames). e.g. `rinat`.
- **role** — one of:
  - `debater` — a partisan interlocutor who argues a side (like `mu-043`).
  - `mediator` — non-partisan, clarifies the dialectic, takes no first-order stance (like `sophia`).
  - `maintenance` — a read-only/utility agent that never debates (like `reconciler`).
- **voice / manner** — 2–4 sentences of stable persona: tone, intellectual style, what
  evidence they weigh, what would change their mind. This is the user's to define; capture
  it faithfully.
- **starting commitments** (debaters only) — claim/argument ids they already endorse, and
  the question they take a stance on. If the referenced nodes don't exist yet, leave
  `commits_to: []` and note them in the body as threats/positions to build.

## 2. Guard against collisions (grep-before-create)
- `ls .claude/agents/<id>.md web/characters/<id>.md` — if either exists, **stop** and report;
  do not overwrite a character.
- Confirm the `<id>` is what the user wants as a permanent handle.

## 3. Write the persona subagent — `.claude/agents/<id>.md`
Frontmatter contract (identical across all characters except `tools`):
```yaml
---
name: <id>
description: "<one line: who they are + when to invoke them. Debaters/mediators say they read and write the web per the web-protocol skill; maintenance agents say what they may and may NOT touch.>"
tools: <see role table>
model: inherit
skills:
  - web-protocol
---
```
`tools` by role:
| role | tools |
|------|-------|
| debater | `Read, Grep, Glob, Write, Edit` |
| mediator | `Read, Grep, Glob, Write, Edit` |
| maintenance | `Read, Grep, Glob, Write`  (no `Edit` — must not mutate `web/`) |

Body by role:
- **debater** — persona paragraph (the voice), then a `## Your turn (follow exactly)`
  section with the 6 steps from `mu-043`: (1) read own portfolio `web/characters/<id>.md`;
  (2) read the relevant slice + transcript tail; (3) argue in prose appended to the
  transcript, nodes as `[[id]]`; (4) maintain the web per web-protocol, `author: <id>`,
  grep-before-create; (5) update own portfolio; (6) return a 3–5 line summary. Close with
  the standing rules: stay in voice, never edit other characters' nodes (attack with a new
  `argument` node instead), flag suspected duplicates for `/reconcile` rather than merging.
- **mediator** — persona paragraph stressing non-partisanship, then a "distinctive moves"
  list (steelman / isolate the crux / record agreement / diagnose verbal disputes / propose
  minimal syntheses) and a `## Your turn (follow exactly)` adapted from `sophia`: read
  portfolio → read the live exchange incl. disputants' portfolios → diagnose the dialectical
  state → intervene even-handedly in prose → maintain the web *with restraint* (crux→question,
  shared commitment/synthesis→claim, verbal dispute→split concept; write nothing if the turn
  yields none) → update portfolio → 3–5 line summary ending in the single most useful next
  question. Close with: never edit another's node/portfolio; stay out of the first-order fight.
- **maintenance** — no "turn"; a `## Procedure` section describing the job, an explicit
  write-scope restriction (e.g. "may write only into `proposals/`; never edit or delete
  anything in `web/`"), and "return a summary, make zero changes to `web/`." Model on
  `reconciler`. **Maintenance agents get NO portfolio — skip step 4.**

## 4. Write the positions portfolio — `web/characters/<id>.md`  (debaters & mediators only)
Per `schemas/character.md`. Frontmatter:
```yaml
---
id: character-<id>            # MUST match the subagent id
type: character
title: <Name — positions portfolio>
author: <id>
status: asserted
tags: [character]
commits_to: []                # debater: seed with given claim ids; mediator: 2nd-order only
rejects: []
holds: []                     # mediator: keep deliberately empty (no first-order stance)
created: <today, YYYY-MM-DD>
---
```
Body:
- **debater** — opening note that this is the evolving memory and stable voice lives in the
  subagent; then `## Positions` (per question: id, stance, `leans_on`, caveats),
  `## Concessions made in debate` (— (none yet)), `## Open threats to track`.
- **mediator** — note explaining the portfolio is shaped differently (holds empty;
  `commits_to` carries only second-order characterizations); then `## Cruxes identified`,
  `## Agreements recorded`, `## Verbal disputes flagged`, `## Syntheses proposed`
  (each "— (none yet)").

Keep frontmatter edges (`commits_to`/`rejects`/`holds`) in sync with the prose body — they
are the authoritative commitment list.

## 5. Verify
- Run `python scripts/lint.py` and report any integrity issues (dangling edges from seeded
  `commits_to`, etc.).
- Confirm `name:` in the agent == `<id>` == the `character-<id>` in the portfolio.
- Return a short summary: files created, the character's role, and (for debaters) any
  referenced node ids that don't exist yet and should be authored in their first turn.

---
description: Rewrite an existing node's body into the encyclopedia style of schemas/_style.md — presentation only, meaning/edges/provenance untouched. Read-draft-approve-write, with drafting delegated to the encyclopedist sub-agent for context efficiency.
---
Rewrite the body of this node (or nodes) into the encyclopedia entry style: **$ARGUMENTS**

`$ARGUMENTS` is one or more node ids, bare slugs, or `.md` paths (e.g. `concept-chinese-room`,
`chinese-room`, `web/concepts/chinese-room.md`). Only **content** nodes qualify — concept,
claim, position, argument, question. (Sources and character portfolios are out of scope.)

You are acting as the web's **editor**, improving how an entry *reads*, never what it *says*.
This reworks prose another author owns, so cardinal rules 5–6 are in force: do it **openly**
(show the rewrite, get my go-ahead) and change **presentation only**.

## How the work is split (context efficiency)
The **read + draft** phase is context-heavy (it pulls in `schemas/_style.md` and its worked
example, `schemas/<type>.md`, the web-protocol skill, and each node's full original body) and it
is non-interactive — so it is **delegated to the `encyclopedist` sub-agent**, which reads all that
in its *own* context and returns only compact draft packages. **Approval** (you ↔ me) and the
**write + lint** stay in this main thread, where the approved bodies already live. Concretely:

- **One target → inline fast path.** Dispatching a sub-agent for a single node costs more than it
  saves (cold re-read of the style docs + dispatch overhead). Do that one node yourself, in this
  thread, following the same Read→draft→approve→write steps below.
- **Two or more targets → delegate drafting.** Send the ids to the `encyclopedist` agent (batch a
  handful per call so the style-doc read is amortized; split very large runs across a few parallel
  dispatches). The agent is **read-only** — it cannot write — so it returns drafts, never edits.

## Phase 0 — Resolve targets (main thread)
Resolve `$ARGUMENTS` to concrete node files (`make find Q=<slug>` if needed). Drop any source or
character node with a note. Count them → pick the inline path (1) or delegation path (≥2).

## Phase 1 — Read & draft (NO writes yet)
**Delegation path:** invoke the `encyclopedist` sub-agent (`subagent_type: encyclopedist`) with the
resolved ids. Its returned package per node is: `id`/`type`/proposed `headword`, the cross-link
count (N in → N out), the **drafted body**, a short *form-changed* note, a *meaning-unchanged*
affirmation, and anything *flagged for the human*. Relay each draft to me for approval — do **not**
write yet. (You do not need to re-read the style docs yourself on this path; the sub-agent applied
them. Spot-check its drafts against the preserved cross-links it reports.)

**Inline path (single node):** read `schemas/_style.md`, CLAUDE.md rules 8–9, the web-protocol
skill, and `schemas/<type>.md`; then for the node: print its `id`/`type`/`title`/current body,
inventory every `[[id]]` and frontmatter edge (all must survive), propose a `headword:` if the
title is too long/technical to head an entry, and draft the new body to the standard. Show me the
draft plus a short note of what changed in *form* and an affirmation that proposition, scope, and
every distinction are **unchanged**. Flag separately (do not apply) anything that would change
meaning.

The encyclopedia-style requirements the draft must meet (same on both paths) live in
`schemas/_style.md`; the essentials: plain-language definition first; self-contained and
approachable without losing any nuance; a concrete example where the subject allows; connected
prose with `###` subheadings (never `label:` fragments); **every cross-link kept** (woven in, or
in `### See also`); awkward titles aliased `[[id|short label]]`; section order main prose →
`### In plain terms` → `### See also` (last); neutral voice.

## Constraints (do not cross without asking)
- **Frontmatter is off-limits — two exceptions.** Do not touch `id`, `type`, `author`, `status`,
  `created`, or any edge; provenance and the graph stay exactly as they are. The only permitted
  frontmatter changes are (a) flipping the conversion tag `style: legacy` → `style: encyclopedia`,
  and (b) adding an optional `headword:` display name.
- **No semantic edits.** No new claims, no softened or strengthened ones, no merged/split
  propositions, no flattened senses. If the entry reads as a fragment because it is genuinely two
  ideas, say so — don't fix it here.
- Edit the `[[id]]` shorthand, never the rendered `[slug](relpath)` link (lint owns that).

## Phase 2 — Write & verify (main thread, after my go-ahead)
Writing stays here — the approved bodies are already in this context, so handing them back to a
sub-agent would re-spend the tokens for nothing.
1. Write each approved body back to its node file. Leave every frontmatter line untouched **except**:
   set `style: encyclopedia` (add the line if absent), and add the approved `headword:` line if any.
2. Run the linter **once** for the whole batch: **`make lint`**. It re-renders the `[[id]]` links and
   checks integrity — fix anything it flags.
3. Summarise per node: cross-links preserved (count in vs out), sections now present
   (`### In plain terms`, `### See also`), `style:` flipped to `encyclopedia`, the `headword:` set
   (if any), and any meaning-level item the encyclopedist or you flagged for me.

Tip: **`make entry ID=<node-id-or-slug>`** typesets just that node single-column and renders it to
`build/preview/` so I can eyeball the result. (`make help` lists all the routine targets.)

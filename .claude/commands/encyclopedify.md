---
description: Rewrite an existing node's body into the encyclopedia style of schemas/_style.md — presentation only, meaning/edges/provenance untouched. Read-draft-approve-write.
---
Rewrite the body of this node (or nodes) into the encyclopedia entry style: **$ARGUMENTS**

`$ARGUMENTS` is one or more node ids, bare slugs, or `.md` paths (e.g. `concept-chinese-room`,
`chinese-room`, `web/concepts/chinese-room.md`). Only **content** nodes qualify — concept,
claim, position, argument, question. (Sources and character portfolios are out of scope.)

You are acting as the web's **editor**, improving how an entry *reads*, never what it *says*.
This reworks prose another author owns, so cardinal rules 5–6 are in force: do it **openly**
(show the rewrite, get my go-ahead) and change **presentation only**. Read first:
`schemas/_style.md` (the standard + worked example), CLAUDE.md rule 8, the web-protocol skill,
and `schemas/<type>.md` for each node's type (cardinal rule 1: read the schema before editing).

## Phase 1 — Read & draft (NO writes yet)
For each target node:
1. **Resolve & read.** Find the node, print its `id`, `type`, `title`, and current body.
2. **Inventory what must be preserved.** List every `[[id]]` / rendered cross-link in the body
   and every frontmatter edge. These all survive the rewrite — none may be dropped.
3. **Draft the new body** to the standard in `schemas/_style.md`:
   - Lead with a one-to-three-sentence plain-language definition before any taxonomy or dispute.
   - Self-contained and approachable to an interested amateur, **without losing any distinction
     or nuance** the original drew. Introduce each term of art in *italics* and unpack it.
   - Include a concrete example or canonical case where the subject allows.
   - Real connected prose with `###` subheadings for longer entries — never `label: fragment`
     note style. A claim stays atomic and short, but still reads as prose.
   - **Keep every cross-link.** Weave each `[[id]]` into the prose where it arises naturally;
     any related node that finds no natural home goes in a `### See also` section.
   - **Alias awkward titles inline.** A cross-reference prints the target's *title*; when that
     title would read badly in the sentence — it begins with "The" (so "the [[concept-hard-problem]]"
     doubles to "the The hard problem…") or it is a long claim sentence — cite it with an alias,
     `[[id|short label]]`, so the prose reads naturally. The encyclopedia and lint both honor the
     alias. In `### See also`, plain `[[id]]` (full title) is usually right.
   - Section order at the end: main prose, then `### In plain terms` (keep the existing one;
     add one only if the entry is genuinely jargon-heavy), then `### See also` **last**.
   - **Neutral voice** (rule 6): no character names; real philosophers/sources are fine.
4. **Show me the proposed body** and a short note of what changed in *form* and an explicit
   confirmation that the proposition, scope, and every distinction are **unchanged**. Flag
   separately (do not apply) anything that would change meaning — e.g. a cross-reference the
   prose now wants that isn't yet a frontmatter edge, or wording you suspect is actually wrong.

## Constraints (do not cross without asking)
- **Frontmatter is off-limits — one exception.** Do not touch `id`, `type`, `author`, `status`,
  `created`, or any edge; provenance and the graph stay exactly as they are. The *only* permitted
  frontmatter change is flipping the conversion tag `style: legacy` → `style: encyclopedia` (see
  Phase 2). Never add a frontmatter edge.
- **No semantic edits.** No new claims, no softened or strengthened ones, no merged/split
  propositions, no flattened senses. If the entry reads as a fragment because it is genuinely
  two ideas, say so — don't fix it here.
- Edit the `[[id]]` shorthand, never the rendered `[slug](relpath)` link (lint owns that).

## Phase 2 — Write & verify (after my go-ahead)
5. Write the approved body back to the node file. Leave every frontmatter line untouched **except**
   set the conversion tag to `style: encyclopedia` (if the node lacks a `style:` line, add one).
6. Run the linter (uv only, per CLAUDE.md): `uv run --with pyyaml python scripts/lint.py`. It
   re-renders the `[[id]]` links and checks integrity — fix anything it flags.
7. Summarise per node: confirmed cross-links preserved (count in vs out), sections now present
   (`### In plain terms`, `### See also`), `style:` flipped to `encyclopedia`, and any
   meaning-level item you flagged for me.

Tip: after a batch, `uv run --with pyyaml python scripts/book.py <ids>` renders just those
entries so I can eyeball the typeset result.

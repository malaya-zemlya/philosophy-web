---
description: Import an external argument (from literature or the user) into the web — triage + quality-control gate, then decompose into properly-formatted claim/concept/argument nodes.
---
Import this external argument into the web: **$ARGUMENTS**

`$ARGUMENTS` may be a file path, a citation, a URL, or pasted prose. If it is only a
reference with no text, ask me for the text (or fetch it) — never reconstruct an argument
you have not actually read.

Act as the web's **librarian**, not as a debating character: you write the nodes here
yourself (this is not a character's turn). Follow the **web-protocol** skill throughout, and
read `schemas/<type>.md` before creating each node type. **Write nothing to `web/` until I
approve** (Phase 1 is read-only).

Formal or Bayesian arguments often carry notation: write it in LaTeX maths — inline `$…$`,
display `$$…$$` on its own line(s) — per `schemas/_style.md` ("Mathematics"). Keep premises and
conclusions as atomic claims even when their statement contains a formula.

## Phase 1 — Triage & quality control (READ-ONLY; report, then ask me)
1. **Reconstruct charitably.** Restate the argument in structured form: its single
   conclusion, each premise, and the inference form (deductive | abductive | analogy |
   inductive). Make suppressed premises explicit.
2. **Belonging check.** Does it bear on the web's governing questions (see `web/questions/`)?
   Flag plainly if the text is *not actually an argument*, is *off-topic*, or looks like the
   *wrong / garbled text* — this is the "user pasted the wrong thing" guard.
3. **Quality control.** Scan for obvious errors and fallacies — formal invalidity,
   equivocation, question-begging, non-sequitur, false dichotomy, undischarged suppressed
   premise, etc. Name the **weakest premise** explicitly.
4. **Verdict, then ask me per case.** Present (a) the reconstruction, (b) belongs? + why,
   (c) QC findings + weakest premise, (d) your recommended disposition. Then **ask me how to
   proceed** for this argument — one of: import as-is · import as `status: contested` with the
   flaw recorded in the body · revise wording first · reject. Do not assume a default.

## Phase 2 — Decompose & map (after my go-ahead; still no writes)
5. **Atomise.** Decompose into: the concept(s) it invokes, each premise as **one** truth-apt
   proposition, the conclusion as a claim, and the argument move(s) (an objection is an
   `argument` with `attacks`; a reply is one with `responds_to` — do not invent new types).
6. **Grep-before-create for every part.** `grep -ri "<key phrase>" web/`, read the closest
   hits, and decide cite-by-id vs create-new for each. Show me the cite-vs-create plan before
   writing. For each new node, prepare the `Distinct from [[<id>]] because …` line.
7. **Attribution.** If the argument is from literature: create or cite a `source` node
   (`author` = who added it, normally `mishka`; `title` = `Author — Work (year)`), and set the
   imported claim/argument nodes' `author` to the **cited philosopher** as a named human (e.g.
   `author: chalmers`). If it is my own argument: `author: mishka`. Never attribute another
   author's formulation to a character.

## Phase 3 — Write (dependency order, so edges always resolve)
8. Create nodes in this order: **concepts → premise claims → conclusion claim → argument
   node.** Schema invariant: every `premise` must already exist as a claim id before the
   argument references it. Keep claims atomic (no "and"/"or" joining two propositions). The
   argument body must state the inference form and name the weakest premise. **Set the
   argument's `pattern:` field** to the best-matching scheme in `patterns/` (read the candidate
   file and check the move fits its Form); omit it only if none genuinely fits. `pattern` is a
   reference into `patterns/`, not an edge. If the argument is an objection whose target cites a
   pattern, identify which **critical question** of that pattern it raises and name it in the
   body's first line. Edges are outgoing-only and reference ids (no backlinks — lint computes those);
   in body prose, cite other nodes with the `[[id]]` shorthand (lint renders the clickable link).
9. If a new node is close to an existing one and you are unsure they differ, create it **and**
   flag the pair for `/reconcile` — never silently merge or reword another author's node.

## Phase 4 — Verify & report
10. Run the linter (see CLAUDE.md): `.venv/bin/python scripts/lint.py` (or
    `uv run --with pyyaml python scripts/lint.py`). Fix any integrity issues it reports.
11. Summarise: the source node; which claims/concepts were created vs cited; the argument
    node and its `premise`/`concludes`/`attacks`/`responds_to`/`supports` edges; and any
    `/reconcile` flags raised.

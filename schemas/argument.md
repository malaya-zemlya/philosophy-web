# argument
An inference: premises to a conclusion, or a move for/against another node.
The only type that argues.

## Frontmatter (copy & fill)
```yaml
---
id: argument-<slug>                       # REQUIRED · stable
type: argument                            # REQUIRED
title: <short name of the move>           # REQUIRED
author: <real-philosopher | generic | mishka>  # REQUIRED · NEVER a character
status: asserted                          # asserted | contested | retracted | superseded
pattern: <pattern-id>                     # optional · argument pattern this move instantiates (see patterns/); NOT an edge
tags: []                                  # optional
created: YYYY-MM-DD                        # REQUIRED
# --- edges: MUST include at least ONE target edge below (concludes/supports/attacks/responds_to)
premise: []                               # -> claim(s) it rests on
concludes: claim-<slug>                   # -> the single claim it establishes
supports: []                              # -> claim | argument it bolsters
attacks: []                               # -> claim | argument it undercuts
responds_to: []                           # -> argument it replies to
uses_concept: []                          # -> concept   (optional)
presupposes: []                           # -> claim | concept (optional)
---
```
Illegal here (enforced): answers, commits_to, rejects, holds. An argument does not answer a
question — the claim it `concludes`/`supports` answers it.

## Body
- inference form: deductive | abductive | analogy | inductive
- numbered premises -> conclusion
- **weakest premise**: name it explicitly (this is where future attacks land)
- if jargon-heavy: end with an optional `### In plain terms` section — a self-contained,
  plain-language gloss for a casual visitor with no philosophy training and no knowledge of the
  rest of the web. Additive only (never overrides the precise prose above; no `[[id]]` links).
  See web-protocol "Optional `### In plain terms` section".

## Pattern & critical questions (optional but encouraged)
- Set `pattern:` to one of the `patterns/` ids (e.g. `cause-to-effect`) when the move fits a
  named scheme. This is a reference, **not** an edge — its value is a `patterns/` filename, not a
  node id, and the linter never treats it as a backlink.
- Declaring a pattern names the move's **attack surface**: the pattern's critical questions (CQs)
  are the standard ways it can fail. When *attacking* such an argument, open the attacking
  argument's body by naming the CQ you raise — e.g.
  `Raises thought-experiment CQ4 (bridge): the case refutes behaviourism, not organisational
  functionalism.` — and point the `attacks` edge at the premise/inference that CQ targets.
- An unraised CQ on a cited pattern is a standing invitation for the next turn; don't manufacture
  attacks outside the pattern's CQ list without saying why the standard ones don't apply.

## Invariants
- Premises are claim ids, not prose. If a premise isn't a claim node yet, create the claim first.
- An objection IS an argument with `attacks`; a rebuttal IS an argument with `responds_to`.
  Do not invent separate "objection"/"rebuttal" types.
- NEUTRAL. The argument belongs to philosophy in general; never name a character in the body
  ("the functionalist replies …", not "mu-043 replies …"). Real philosophers / `source` nodes
  are fine. `author` is never a character. Who deploys the move, and what would move them,
  lives only in `web/characters/<id>.md`.

## Pre-save checklist
- [ ] read this schema; grepped for a duplicate move
- [ ] has at least one of concludes/supports/attacks/responds_to (lint rejects otherwise)
- [ ] every premise is an existing claim id
- [ ] inference form + weakest premise stated in body
- [ ] `pattern:` set to the best-fitting `patterns/` scheme (or deliberately omitted because none fits)
- [ ] if attacking a target that cites a pattern, named the critical question raised in the body

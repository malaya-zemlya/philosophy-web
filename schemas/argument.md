# argument
An inference: premises to a conclusion, or a move for/against another node.
The only type that argues.

## Frontmatter (copy & fill)
```yaml
---
id: argument-<slug>                       # REQUIRED · stable
type: argument                            # REQUIRED
title: <short name of the move>           # REQUIRED
author: <character-id | mishka | name>    # REQUIRED
status: asserted                          # asserted | contested | retracted | superseded
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

## Invariants
- Premises are claim ids, not prose. If a premise isn't a claim node yet, create the claim first.
- An objection IS an argument with `attacks`; a rebuttal IS an argument with `responds_to`.
  Do not invent separate "objection"/"rebuttal" types.

## Pre-save checklist
- [ ] read this schema; grepped for a duplicate move
- [ ] has at least one of concludes/supports/attacks/responds_to (lint rejects otherwise)
- [ ] every premise is an existing claim id
- [ ] inference form + weakest premise stated in body

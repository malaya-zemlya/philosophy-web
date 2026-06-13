# concept
A term and its definition(s), including competing senses.

## Frontmatter (copy & fill)
```yaml
---
id: concept-<slug>                        # REQUIRED · stable
type: concept                             # REQUIRED
title: <the term>                         # REQUIRED
author: <real-philosopher | generic | mishka>  # REQUIRED · NEVER a character
status: asserted                          # asserted | contested | retracted | superseded
tags: []                                  # optional
created: YYYY-MM-DD                        # REQUIRED
# --- edges: all optional ---
uses_concept: []                          # -> concept
presupposes: []                           # -> claim | concept
---
```
Illegal here (enforced): premise, concludes, supports, attacks, responds_to, answers,
commits_to, rejects, holds. A concept is *invoked* (via others' `uses_concept`), not argued.

## Body
- primary definition
- `senses:` list when the term is contested (label each sense + who holds it)
- the live dispute the concept feeds, by claim/question id
- if jargon-heavy: an optional `### In plain terms` section — a self-contained,
  plain-language gloss for a casual visitor with no philosophy training and no knowledge of the
  rest of the web. Additive only (never overrides the precise prose above). Don't rely on reading
  order; when it refers to another move in the web, name it in plain words and link it with `[[id]]`.
  See web-protocol "Optional `### In plain terms` section".
- last: a `### See also` section mapping the related nodes — every related node the prose didn't
  absorb, plus optionally the body's key links; each item `[[id]]` + a clause on how it relates
  (see `schemas/_style.md`).

## Invariants
- Define, don't argue. Evaluative content belongs in a claim or argument.
- NEUTRAL. The concept belongs to philosophy in general; never name a character ("who holds"
  a sense means a real philosopher, e.g. Putnam — never mu-043/alvin/…). `author` is never a
  character.

## Pre-save checklist
- [ ] read this schema; grepped for an existing concept of the same term
- [ ] competing senses captured, not flattened to one
- [ ] only legal edges used

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

## Invariants
- Define, don't argue. Evaluative content belongs in a claim or argument.
- NEUTRAL. The concept belongs to philosophy in general; never name a character ("who holds"
  a sense means a real philosopher, e.g. Putnam — never mu-043/alvin/…). `author` is never a
  character.

## Pre-save checklist
- [ ] read this schema; grepped for an existing concept of the same term
- [ ] competing senses captured, not flattened to one
- [ ] only legal edges used

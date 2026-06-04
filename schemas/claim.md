# claim
One truth-apt proposition. The atom of the web.

## Frontmatter (copy & fill)
```yaml
---
id: claim-<slug>                          # REQUIRED · stable · never reuse
type: claim                               # REQUIRED
title: <one declarative proposition>      # REQUIRED · atomic (no "and"/"or" joining two props)
author: <character-id | mishka | name>    # REQUIRED · provenance
status: asserted                          # asserted | contested | retracted | superseded
# superseded_by: claim-<slug>             # ONLY if status: superseded
tags: []                                  # optional
created: YYYY-MM-DD                        # REQUIRED
# --- edges: all optional; values are node ids; each may be a single id or a list ---
uses_concept: []                          # -> concept
presupposes: []                           # -> claim | concept
answers: []                               # -> question   (this claim is a candidate answer)
---
```
Illegal here (enforced by lint.py): premise, concludes, supports, attacks, responds_to,
commits_to, rejects, holds. A claim is argued *about*, never argues.

## Body
- gloss: 1–2 sentences restating the proposition precisely
- scope: what it does and does NOT assert
- who would deny it (often a `position` id)
- if near an existing claim: `Distinct from <id> because …`

## Invariants
- ATOMIC. Title is a single proposition; split any "X and Y".
- Materially different phrasings are different claims (e.g. "thought requires biology"
  ≠ "consciousness requires carbon").

## Pre-save checklist
- [ ] read this schema; grepped web/ for an equivalent (cited it if found)
- [ ] title is one declarative proposition
- [ ] id, type, title, author, created all filled
- [ ] only the legal edges above are used

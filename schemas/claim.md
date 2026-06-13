# claim
One truth-apt proposition. The atom of the web.

## Frontmatter (copy & fill)
```yaml
---
id: claim-<slug>                          # REQUIRED · stable · never reuse
type: claim                               # REQUIRED
title: <one declarative proposition>      # REQUIRED · atomic (no "and"/"or" joining two props)
headword: <short display name>            # optional · encyclopedia entry headword; `title` becomes the subtitle
author: <real-philosopher | generic | mishka>  # REQUIRED · provenance · NEVER a character
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
- who would deny it (often a `position`, cited in prose as `[[position-...]]`)
- if near an existing claim: `Distinct from [[<id>]] because …`
- if jargon-heavy: end with an optional `### In plain terms` section — a self-contained,
  plain-language gloss for a casual visitor with no philosophy training and no knowledge of the
  rest of the web. Additive only (never overrides the precise prose above). Don't rely on reading
  order; when it refers to another move in the web, name it in plain words and link it with `[[id]]`.
  See web-protocol "Optional `### In plain terms` section".

## Invariants
- ATOMIC. Title is a single proposition; split any "X and Y".
- Materially different phrasings are different claims (e.g. "thought requires biology"
  ≠ "consciousness requires carbon").
- NEUTRAL. The proposition belongs to philosophy in general; never name a character in the
  title or body ("the functionalist holds X", not "mu-043 holds X"). Real philosophers and
  `source` nodes are fine. `author` is a real philosopher / `generic` / `mishka`, never a
  character — what a character thinks lives in `web/characters/<id>.md`.

## Pre-save checklist
- [ ] read this schema; grepped web/ for an equivalent (cited it if found)
- [ ] title is one declarative proposition
- [ ] id, type, title, author, created all filled
- [ ] only the legal edges above are used

# question
An IBIS *issue* — an organizing node that candidate answers point at.

## Frontmatter (copy & fill)
```yaml
---
id: question-<slug>                       # REQUIRED · stable
type: question                            # REQUIRED
title: <the issue, phrased as a question?> # REQUIRED · interrogative
author: <real-philosopher | generic | mishka>  # REQUIRED · NEVER a character
status: asserted                          # asserted | contested | retracted | superseded
tags: []                                  # optional
created: YYYY-MM-DD                        # REQUIRED
# --- edges: edge-poor by design; uses_concept is the ONLY legal edge ---
uses_concept: []                          # -> concept
---
```
Illegal here (enforced): everything except uses_concept.

## Body
- precise statement of the issue and key terms
- sub-issues that may deserve their own question nodes
- if jargon-heavy: end with an optional `### In plain terms` section — a self-contained,
  plain-language gloss for a casual visitor with no philosophy training and no knowledge of the
  rest of the web. Additive only (never overrides the precise prose above; no `[[id]]` links).
  See web-protocol "Optional `### In plain terms` section".

## Invariants
- Do NOT hand-list candidate answers. Answers are nodes carrying `answers: <this id>`;
  lint.py computes the list into web/INDEX.md.
- NEUTRAL. The issue belongs to philosophy in general; never frame it around a character.
  `author` is never a character.

## Pre-save checklist
- [ ] read this schema; title is interrogative
- [ ] no hand-maintained answer list in the body

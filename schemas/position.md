# position
A named, reusable view (e.g. proteocentrism), independent of any character.
Characters cite positions rather than restating them.

## Frontmatter (copy & fill)
```yaml
---
id: position-<slug>                       # REQUIRED · stable
type: position                            # REQUIRED
title: <name of the view>                 # REQUIRED
author: <character-id | mishka | name>    # REQUIRED
status: asserted                          # asserted | contested | retracted | superseded
tags: []                                  # optional
created: YYYY-MM-DD                        # REQUIRED
# --- edges: MUST include at least ONE of commits_to / rejects / answers ---
commits_to: []                            # -> claim(s) endorsed
rejects: []                               # -> claim(s) denied
answers: []                               # -> question(s) it takes a stance on
uses_concept: []                          # -> concept (optional)
presupposes: []                           # -> claim | concept (optional)
---
```
Illegal here (enforced): premise, concludes, supports, attacks, responds_to, holds.

## Body
- one-paragraph statement of the view
- what distinguishes it from neighbouring views

## Invariants
- A position is substrate for characters; it is not itself an arguer. Reasons FOR it live in
  `argument` nodes that `support` its committed claims.

## Pre-save checklist
- [ ] read this schema; commitments expressed as claim ids (create claims first if needed)
- [ ] has at least one of commits_to/rejects/answers (lint rejects otherwise)

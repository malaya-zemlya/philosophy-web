# character
A debater's evolving positions portfolio. Stable voice/method live in the subagent at
`.claude/agents/<id>.md`; THIS node is the character's memory between turns.

## Frontmatter (copy & fill)
```yaml
---
id: character-<id>                        # REQUIRED · <id> MUST match .claude/agents/<id>.md
type: character                           # REQUIRED
title: <Name — positions portfolio>       # REQUIRED
author: <character-id>                    # REQUIRED · usually the character's own id
status: asserted                          # asserted | contested | retracted | superseded
tags: [character]                         # optional
created: YYYY-MM-DD                        # REQUIRED
# --- edges: formal, greppable commitments (KEEP IN SYNC with the prose body) ---
commits_to: []                            # -> claim(s) the character endorses
rejects: []                               # -> claim(s) the character denies
holds: []                                 # -> position(s) the character adopts
uses_concept: []                          # -> concept (optional)
---
```
Illegal here (enforced): premise, concludes, supports, attacks, responds_to, answers,
presupposes.

## Body (reasoning memory — NOT edges)
- per-question portfolio: `question` id, stance, `leans_on` (argument/claim ids), caveats
- concessions made in debate
- open threats to track
The frontmatter edges are the authoritative commitment list; the body is annotation.

## Invariants
- `<id>` here must match a subagent id in `.claude/agents/`.
- Update this node at the END of every turn the character takes. If you concede a claim,
  remove it from `commits_to`.

## Pre-save checklist
- [ ] read this schema; frontmatter commits_to/rejects/holds reflect current stance
- [ ] body portfolio updated for this turn (stance, concessions, threats)

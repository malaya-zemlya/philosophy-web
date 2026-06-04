# source
A philosopher, text, or paper, for provenance and citation.

## Frontmatter (copy & fill)
```yaml
---
id: source-<slug>                         # REQUIRED · stable
type: source                              # REQUIRED
title: <Author — Work (year)>             # REQUIRED
author: <who-added-it>                    # REQUIRED · the NODE's author, NOT the cited work's author
status: asserted                          # asserted | contested | retracted | superseded
tags: []                                  # optional
created: YYYY-MM-DD                        # REQUIRED
# --- edges: NONE are legal for a source ---
---
```
A source is referenced by other nodes' bodies and by their `author` field, not via edges.

## Body
- relevance to this project (content vs. method/form)
- key passages with page refs

## Pre-save checklist
- [ ] read this schema; not duplicating an existing source
- [ ] node `author` (who added it) set, distinct from the cited work's author

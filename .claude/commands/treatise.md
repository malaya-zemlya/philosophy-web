---
description: Draft a philosophical post/treatise/dispute from the recorded web.
---
Draft a piece on: **$ARGUMENTS**

Work FROM the web, not from memory:
1. Run `python scripts/lint.py` to refresh `web/INDEX.md` (backlinks) and render prose links.
2. Identify the governing `question-*` node and gather its candidate-answer nodes and their
   supporting/attacking arguments via backlinks.
3. Outline the dialectic: positions, the arguments for each, the attacks and responses.
4. Draft prose. Attribute ideas by each node's `author` (so a claim first made by Rinat,
   or by me, is credited as such). Cite nodes as `[[id]]` so I can trace each move; since the
   draft lives under `transcripts/`, lint renders these into clickable links.
5. Flag gaps: any `status: contested` claim with no recorded response is a hole to fill by
   more debate before publishing.
Save the draft to `transcripts/treatise-<slug>.md` (a working artifact, not a web node).

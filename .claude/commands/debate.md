---
description: Run one or more debate turns among the characters into the philosophy web.
---
Orchestrate a debate on: **$ARGUMENTS**

1. Identify the relevant `question-*` node (create one with author: human if none fits).
2. Open or create a transcript file `transcripts/YYYY-MM-DD-<slug>.md` and note the question.
3. Run characters in turns by explicitly invoking their subagents. Before dispatching each turn,
   run `make similar Q="<the turn's topic in a sentence>"` and paste the resulting shortlist
   (ids + headwords) into the character's prompt — the characters have no shell, so this is how
   they see semantically-nearby nodes that grep would miss (existing nodes to cite instead of
   recreate). After each turn, briefly relay that character's summary to me and ask whether to
   continue, switch speaker, or stop.
4. Do not write web nodes yourself — the character subagents do that. You hold the transcript and the turn order only.
5. When we stop, run `make lint` (and `make embed` if nodes were created) and report any integrity issues.

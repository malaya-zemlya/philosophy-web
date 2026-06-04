---
description: Run one or more debate turns among the characters into the philosophy web.
---
Orchestrate a debate on: **$ARGUMENTS**

1. Identify the relevant `question-*` node (create one with author: human if none fits).
2. Open or create a transcript file `transcripts/YYYY-MM-DD-<slug>.md` and note the question.
3. Run characters in turns by explicitly invoking their subagents. After each turn, briefly relay that character's summary to me and ask whether to continue, switch speaker, or stop.
4. Do not write web nodes yourself — the character subagents do that. You hold the transcript and the turn order only.
5. When we stop, run `python scripts/lint.py` and report any integrity issues.

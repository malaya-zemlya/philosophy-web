---
description: Find suspected duplicate nodes and write merge proposals for review (no auto-merge).
---
Invoke the **reconciler** subagent over the current web. Then summarise the proposals it wrote to `proposals/`. For each, present: the candidate ids, the case for and against merging,
and the suggested canonical id. Apply nothing until I approve a specific proposal; when I do,
make the edits to `web/` and rewire edges, then run `python scripts/lint.py`.

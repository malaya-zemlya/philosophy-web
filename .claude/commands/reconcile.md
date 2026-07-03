---
description: Find suspected duplicate nodes and write merge proposals for review (no auto-merge).
---
First run `make dupes` (semantic near-duplicate pairs from the embedding cache) and paste the
resulting pairs into the reconciler's prompt — it has no shell, and the pairs are its primary
lead list (candidates, not verdicts: deliberate contrasts like reply/rejoinder pairs score high
too). Then invoke the **reconciler** subagent over the current web. Then summarise the proposals
it wrote to `proposals/`. For each, present: the candidate ids, the case for and against merging,
and the suggested canonical id. Apply nothing until I approve a specific proposal; when I do,
make the edits to `web/` and rewire edges, then run `make lint`.

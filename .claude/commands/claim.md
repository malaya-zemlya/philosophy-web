---
description: Add the user's own idea to the web as a node, verbatim in intent (no AI rephrasing).
---
I want to add this to the web, authored by me (human): **$ARGUMENTS**

Follow the web-protocol skill. Critically: capture MY formulation faithfully — do not soften,
generalise, or merge it into an existing node without asking. Steps:
1. Grep `web/` for the closest existing node and show it to me.
2. Tell me whether you think this is the same proposition or genuinely new, and why.
3. On my confirmation, either cite the existing id or create a new node with `author: human`, atomic, with correct edges. If new and close to an existing one, add the "Distinct from <id> because …" line.

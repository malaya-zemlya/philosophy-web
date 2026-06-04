# Schemas

One file per node type. **Before creating or editing a node, read `schemas/<type>.md`.**
Each file opens with a **`## Frontmatter (copy & fill)`** block — a complete YAML template
with every field for that type, annotated REQUIRED/optional, showing exactly which edges are
legal. Copy it, fill the placeholders, delete any edge lines you don't use.

Universal field meanings and the meaning of each edge also live in
`.claude/skills/web-protocol/SKILL.md`; these files give the *per-type delta*: the legal subset of edges, body structure, invariants, and a pre-save checklist.

The legal-edge subsets here are **enforced** by `scripts/lint.py` — if they disagree, the
lint matrix `LEGAL_EDGES` is authoritative; fix the doc to match.

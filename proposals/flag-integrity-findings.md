# Integrity flags (non-merge): atomicity, provenance, contested-without-attacker

Reviewed 2026-06-05. These are NOT merge proposals — they are the procedure's step-4 flags for
human attention. No changes were made to `web/`.

## 1. Contested claim with no attacking argument node
`scripts/lint.py` flags any `status: contested` claim that has no incoming `attacks` edge.

- **`claim-prudence-favors-flesh-criterion`** — marked `status: contested`, but no argument node
  carries `attacks: claim-prudence-favors-flesh-criterion`. Its contestation is described only in
  prose (the two "recorded limits": `claim-biology-currently-unforgeable` and
  `claim-forgeable-sign-unfit-as-criterion`, plus a pointer to `argument-access-symmetry-rebuttal`
  on unearned asymmetries). None of these is wired as a frontmatter `attacks` edge at this claim.

  **Suggested fix (for human):** either (a) demote to `status: asserted` if the contestation is
  considered merely latent, or (b) create/redirect an argument node that `attacks`
  `claim-prudence-favors-flesh-criterion` — the natural candidate is an argument built from
  `claim-forgeable-sign-unfit-as-criterion` (the contested bridge premise) or from
  `argument-access-symmetry-rebuttal` (unearned burden-of-proof asymmetry). Recommendation: (b),
  since the body clearly intends a live objection.

  All 7 other contested claims have a proper inbound `attacks` edge and are fine:
  `claim-self-explanation-gap-can-be-architectural` (← `argument-architectural-account-leaves-hard-problem`),
  `claim-lookup-table-combinatorially-inadequate` (← `argument-bounded-table-rejoinder`),
  `claim-llm-has-mental-states` (← `argument-lookup-table-objection`),
  `claim-causal-structure-fixes-decomposition` (← `argument-relevance-filter-regress`,
  `argument-counterfactuals-yield-non-triviality-not-uniqueness`),
  `claim-acquaintance-necessary-for-moral-status-warrant` (← `argument-access-symmetry-rebuttal`),
  `claim-access-grounds-moral-status-asymmetry` (← `argument-access-symmetry-rebuttal`),
  `claim-substrate-independence` (← several).

## 2. Non-atomic claims ("X and Y")
None found. No claim `title` joins two propositions with "and". Clear.

## 3. Nodes missing `author`
None found. All 113 nodes carry an `author`. Spot-checked content nodes for the protocol rule that
content-node authors are real philosophers / `generic` / `mishka` (never a character): the sampled
nodes comply (e.g. `mcginn`, `block`, `mishka`, `generic`); character ids appear only on the
`web/characters/*` portfolio nodes, as required.

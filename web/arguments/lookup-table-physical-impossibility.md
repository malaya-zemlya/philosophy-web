---
id: argument-lookup-table-physical-impossibility
type: argument
title: The cosmic-size reply — a behaviour-matching lookup table is too large to physically exist
author: mishka
status: asserted
tags: [philosophy-of-mind, functionalism, computability]
premise: [claim-lookup-table-size-exponential, claim-observable-universe-finite-storage]
concludes: claim-lookup-table-physically-unrealisable
attacks: [argument-lookup-table-objection]
supports: [argument-lookup-table-combinatorial-impossibility]
uses_concept: [concept-lookup-table-mind]
created: 2026-06-04
---

inference form: deductive — a quantitative reductio (required resource exceeds available resource).

1. (claim-lookup-table-size-exponential) A pure lookup table matching behaviour over a context of
   `n` tokens from a vocabulary of `v` needs ~`v^n` entries; at LLM scale this is ~10^9600.
2. (claim-observable-universe-finite-storage) The observable universe can store at most ~10^120 bits.
∴ (claim-lookup-table-physically-unrealisable) No such table can be physically built; the blockhead
   is cosmically impossible, not merely impractical.

bearing on the targets:
- It `supports` argument-lookup-table-combinatorial-impossibility by closing that argument's known
  escape. That argument is `contested` because Block bounds the table to lifetime-/context-length
  inputs (claim-mind-handles-unbounded-inputs); the present argument grants the bound and shows the
  *bounded* table is still unbuildable — a different, physical ground that the bounded-table
  rejoinder does not touch.
- It `attacks` argument-lookup-table-objection not at its conceptual conclusion but at its weakest,
  tacit premise — the application to *actual* LLMs. Real LLMs match the behaviour with ~10^12
  parameters, ~10^9588 orders of magnitude short of a lookup table, so they cannot *be* lookup
  tables; they must compress and generalise (i.e. process). The blockhead worry thus does not
  transfer to real systems, and the abduction to claim-llm-has-mental-states is protected.

what it does NOT do: it leaves Block's *conceptual* possibility (claim-lookup-table-possible) and his
conceptual conclusion (claim-behaviour-insufficient-for-mind) standing. A merely *possible* blockhead
still shows behaviour ≠ mind in principle; this argument only denies such a thing could be actual.

(A lighter corollary, kept as rhetoric rather than a node: a physical system vast enough to tabulate
a mind would be on such a scale — and so internally rich — that calling it a "mere lookup table"
strains the description; at that size one half-expects it to develop organisation, even life, of its
own. The serious residue is that "flat storage" is not a stable description in the limit.)

weakest premise: (1), specifically that the table cannot be *compressed* below ~`v^n`. The reply
(built into claim-lookup-table-size-exponential): any sub-`v^n` representation must *compute* an
input's response-class rather than retrieve it, which is no longer pure lookup — so compression
concedes that the system processes, which is the conclusion sought.

Distinct from argument-lookup-table-combinatorial-impossibility: that denies the table *matches the
behaviour* (it diverges on unbounded inputs); this grants matching over the bounded domain and
denies the matching table can *physically exist*. Different premise (physical storage bound vs.
unbounded input space) and different conclusion (unrealisable vs. inadequate).

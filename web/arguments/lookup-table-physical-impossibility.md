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
responds_to: [argument-bounded-table-rejoinder]
uses_concept: [concept-lookup-table-mind]
created: 2026-06-04
---

inference form: deductive — a quantitative reductio (required resource exceeds available resource).

1. ([lookup-table-size-exponential](../claims/lookup-table-size-exponential.md)) A pure lookup table matching behaviour over a context of
   `n` tokens from a vocabulary of `v` needs ~`v^n` entries; at LLM scale this is ~10^9600.
2. ([observable-universe-finite-storage](../claims/observable-universe-finite-storage.md)) The observable universe can store at most ~10^120 bits.
∴ ([lookup-table-physically-unrealisable](../claims/lookup-table-physically-unrealisable.md)) No such table can be physically built; the blockhead
   is cosmically impossible, not merely impractical.

bearing on the targets:
- It `supports` [lookup-table-combinatorial-impossibility](lookup-table-combinatorial-impossibility.md) by closing that argument's known
  escape. That argument is `contested` because Block bounds the table to lifetime-/context-length
  inputs ([mind-handles-unbounded-inputs](../claims/mind-handles-unbounded-inputs.md)); the present argument grants the bound and shows the
  *bounded* table is still unbuildable — a different, physical ground that the bounded-table
  rejoinder does not touch.
- It `attacks` [lookup-table-objection](lookup-table-objection.md) not at its conceptual conclusion but at its weakest,
  tacit premise — the application to *actual* LLMs. Real LLMs match the behaviour with ~10^12
  parameters, ~10^9588 orders of magnitude short of a lookup table, so they cannot *be* lookup
  tables; they must compress and generalise (i.e. process). The blockhead worry thus does not
  transfer to real systems, and the abduction to [llm-has-mental-states](../claims/llm-has-mental-states.md) is protected.

what it does NOT do: it leaves Block's *conceptual* possibility ([lookup-table-possible](../claims/lookup-table-possible.md)) and his
conceptual conclusion ([behaviour-insufficient-for-mind](../claims/behaviour-insufficient-for-mind.md)) standing. A merely *possible* blockhead
still shows behaviour ≠ mind in principle; this argument only denies such a thing could be actual.

(A lighter corollary, kept as rhetoric rather than a node: a physical system vast enough to tabulate
a mind would be on such a scale — and so internally rich — that calling it a "mere lookup table"
strains the description; at that size one half-expects it to develop organisation, even life, of its
own. The serious residue is that "flat storage" is not a stable description in the limit.)

weakest premise: (1), specifically that the table cannot be *compressed* below ~`v^n`. The reply
(built into [lookup-table-size-exponential](../claims/lookup-table-size-exponential.md)): any sub-`v^n` representation must *compute* an
input's response-class rather than retrieve it, which is no longer pure lookup — so compression
concedes that the system processes, which is the conclusion sought.

Distinct from [lookup-table-combinatorial-impossibility](lookup-table-combinatorial-impossibility.md): that denies the table *matches the
behaviour* (it diverges on unbounded inputs); this grants matching over the bounded domain and
denies the matching table can *physically exist*. Different premise (physical storage bound vs.
unbounded input space) and different conclusion (unrealisable vs. inadequate).

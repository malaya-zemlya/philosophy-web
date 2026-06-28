---
id: argument-lookup-table-physical-impossibility
type: argument
title: The cosmic-size reply — a behaviour-matching lookup table is too large to physically exist
headword: Cosmic-size reply
author: mishka
status: asserted
tags: [philosophy-of-mind, functionalism, computability]
premise: [claim-lookup-table-size-exponential, claim-observable-universe-finite-storage]
concludes: claim-lookup-table-physically-unrealisable
attacks: [argument-lookup-table-objection]
supports: [argument-lookup-table-combinatorial-impossibility]
responds_to: [argument-bounded-table-rejoinder]
uses_concept: [concept-lookup-table-mind]
style: encyclopedia
created: 2026-06-04
---

The *cosmic-size reply* argues that a lookup table able to match a human- or LLM-scale mind's
behaviour is too large to exist anywhere in the physical universe. It is a quantitative reductio:
the storage the table would demand exceeds the storage the universe can hold, so the blockhead is
not merely impractical but impossible to build at all.

### The argument

The inference is deductive — a quantitative reductio in which a required resource exceeds an
available one.

1. A pure lookup table matching behaviour over a context of $n$ tokens from a vocabulary of $v$
   needs about $v^n$ entries; at LLM scale this is roughly $10^{9600}$
   ([lookup-table-size-exponential](../claims/lookup-table-size-exponential.md)).
2. The observable universe can store at most about $10^{120}$ bits
   ([observable-universe-finite-storage](../claims/observable-universe-finite-storage.md)).

∴ No such table can be physically built: the blockhead is cosmically impossible, not merely
impractical ([lookup-table-physically-unrealisable](../claims/lookup-table-physically-unrealisable.md)).

### What it supports and attacks

It *supports* [the combinatorial-impossibility
reply](lookup-table-combinatorial-impossibility.md) by closing that argument's known escape. The combinatorial reply is `contested` because
Block bounds the table to lifetime- or context-length inputs ([block](../sources/block.md);
[mind-handles-unbounded-inputs](../claims/mind-handles-unbounded-inputs.md)); the present argument grants the bound and shows the
*bounded* table is still unbuildable — a different, physical ground that the bounded-table
rejoinder ([bounded-table-rejoinder](bounded-table-rejoinder.md)) does not touch.

It *attacks* [the lookup-table objection](lookup-table-objection.md) not at its conceptual
conclusion but at its weakest, tacit premise: the application to *actual* systems. Real LLMs match
the behaviour with about $10^{12}$ parameters, some $10^{9588}$ orders of magnitude short of a
lookup table, so they cannot *be* lookup tables; they must compress and generalise — that is,
process. The blockhead worry thus does not transfer to real systems, and the abduction to
[llm-has-mental-states](../claims/llm-has-mental-states.md) is protected.

### What it does not do

It leaves Block's *conceptual* possibility ([block](../sources/block.md); [lookup-table-possible](../claims/lookup-table-possible.md)) and
his conceptual conclusion ([behaviour insufficient for
mind](../claims/behaviour-insufficient-for-mind.md)) standing. A merely *possible* blockhead still shows behaviour ≠ mind in principle; this
argument only denies that such a thing could be actual.

A lighter corollary, kept as rhetoric rather than as a separate node: a physical system vast
enough to tabulate a mind would be on such a scale, and so internally rich, that calling it a
"mere lookup table" strains the description — at that size one half-expects it to develop
organisation, even life, of its own. The serious residue is that "flat storage" is not a stable
description in the limit.

### Weakest premise

Premise (1), specifically the assumption that the table cannot be *compressed* below $v^n$. The
reply is built into [the exponential-size claim](../claims/lookup-table-size-exponential.md): any
sub-$v^n$ representation must *compute* an input's response-class rather than retrieve it, which is
no longer pure lookup — so compression concedes that the system processes, which is the conclusion
sought.

### Distinct from the combinatorial reply

[The combinatorial-impossibility reply](lookup-table-combinatorial-impossibility.md) denies
the table *matches the behaviour* at all (it diverges on unbounded inputs); this reply grants
matching over the bounded domain and denies the matching table can *physically exist*. Different
premise (a physical storage bound versus an unbounded input space) and different conclusion
(unrealisable versus inadequate).

### In plain terms

Even granting you only needed pre-stored answers for a single lifetime's worth of inputs, here is
the killer: count how big that table would have to be. For language, the number of possible
word-sequences explodes exponentially — for something at the scale of today's AI it works out to
roughly $10^{9600}$ entries. The entire observable universe can hold only about $10^{120}$ bits.
So the table is not just impractical; it could not be built in *this universe*, not even in
principle. Two payoffs. First, it slams shut the bounded-table escape hatch — the reply that you
only need to store answers for a single lifetime's inputs ([bounded-table-rejoinder](bounded-table-rejoinder.md)).
Second, and sharper: real AI models do their job with a "mere" $\sim\!10^{12}$ internal settings,
astronomically too few to be a hidden lookup table, so they *cannot* be working by canned lookup
at all; they must be compressing and generalising, i.e. genuinely processing. (What it does not
claim: that a lookup-table mind is logically impossible — only that no real one could ever
physically exist.)

### See also

- [lookup-table-mind](../concepts/lookup-table-mind.md) — the stored-answer machine whose physical size is at issue.
- [lookup-table-physically-unrealisable](../claims/lookup-table-physically-unrealisable.md) — the conclusion this argument establishes.
- [lookup-table-size-exponential](../claims/lookup-table-size-exponential.md) and [observable-universe-finite-storage](../claims/observable-universe-finite-storage.md) — its two
  premises: the table's size and the universe's storage bound.
- [bounded-table-rejoinder](bounded-table-rejoinder.md) — the reply this argument answers on physical grounds.
- [lookup-table-combinatorial-impossibility](lookup-table-combinatorial-impossibility.md) — the reply it supports, by closing the
  bounded-table escape.
- [storage-not-stable-kind](storage-not-stable-kind.md) — the companion reply, that a realisable table is not "mere
  storage".
- [llm-has-mental-states](../claims/llm-has-mental-states.md) — the downstream claim this protects, by ruling out the
  "LLM is a mere lookup table" worry.
- [behaviour-insufficient-for-mind](../claims/behaviour-insufficient-for-mind.md) — Block's conceptual conclusion this argument leaves
  standing.

---
id: argument-storage-not-stable-kind
type: argument
title: Pure storage is not a stable kind at mind-matching scale
headword: Pure-storage instability
author: mishka
status: asserted
tags: [philosophy-of-mind, functionalism, computability]
premise: [claim-lookup-table-physically-unrealisable, claim-lookup-table-size-exponential]
concludes: claim-realisable-behaviour-matcher-is-organised
attacks: [claim-lookup-table-possible, argument-lookup-table-objection]
responds_to: [argument-bounded-table-rejoinder]
uses_concept: [concept-lookup-table-mind, concept-grain]
style: encyclopedia
created: 2026-06-04
---

The *pure-storage-instability* reply argues that "behaviour by mere storage, with no internal
organisation" is not a kind of thing anything could actually be at the scale of a mind. Grant, for
argument's sake, that some imagined machine produces a whole mind's worth of behaviour just by
looking answers up in a stored list; the claim here is that no *physically realisable* machine could
work that way. Any buildable system that matched the behaviour would have to compute its responses,
and computing is organised inner processing — exactly what "pure storage" was meant to do without.

### The inference

The argument is *deductive*: it runs from the unrealisability of flat storage to the organisation of
any realisable matcher.

1. [A flat table cannot be built](../claims/lookup-table-physically-unrealisable.md). A flat table with
   roughly $v^n$ rows cannot be physically built — there is nowhere to *store* that many responses.
2. [Anything smaller must compute](../claims/lookup-table-size-exponential.md). Any representation smaller
   than ~$v^n$ must *compute* which response a given input maps to, rather than retrieve a
   pre-stored whole — and computing is processing over internal organisation, not lookup.

Therefore [every physically realisable
behaviour-matcher is an organised computer](../claims/realisable-behaviour-matcher-is-organised.md). "Mere storage, no organisation" — the defining
property of the [lookup-table mind](../concepts/lookup-table-mind.md) — is not a kind anything can
instantiate at mind-matching scale.

### Bearing on the bounded table

This is a rejoinder to the [bounded-table rejoinder](bounded-table-rejoinder.md). Grant Block
([block](../sources/block.md)) his [lifetime-bounded
table](../claims/lifetime-bounded-table-covers-encountered-inputs.md) that *covers* the inputs; it still fails as a counterexample, because any realisation of it
is an organised computer, not the no-organisation system the objection requires. So the move attacks
[the separability of behaviour from organisation](../claims/lookup-table-possible.md) on its realisable
reading and undercuts the transfer of the [lookup-table objection](lookup-table-objection.md)
to actual systems: the only real "blockheads" are organised computers, such as large language
models, which organisational-role functionalism may credit with mind — a question of
[grain](../concepts/grain.md).

### What it does not do

The argument leaves the conditional [that pure lookup would lack
mind](../claims/lookup-table-lacks-mind.md) standing — *if* something ran by pure stored lookup it would lack mind. The point is only
that nothing realisably does so at this scale. That makes it distinct from the scale-based deflation
of [the domain-asymmetry argument](intuition-domain-asymmetry.md): that move bounds the
warrant of the no-mind *intuition*, whereas this one denies the no-organisation *object* is
realisable at all. It is the standalone home of the "storage isn't a stable kind" reply.

### Weakest premise

Premise 2's claim that the addressing and retrieval organisation is *mind-relevant* rather than mere
plumbing. Block may insist that a retrieval mechanism, however vast, is not cognitive organisation.
The reply: with nothing to retrieve from (premise 1), the "retrieval" is computation, and the
plumbing/computation distinction has no purchase once storage is impossible. Whether that fully
answers the objection is the live crux of this whole sub-web.

Distinct from [the physical-impossibility argument](lookup-table-physical-impossibility.md)
(which establishes premise 1 and stops at "unbuildable"): this draws the further, positive
conclusion about the *kind* of the realisable alternative.

### In plain terms

Here's a subtle reply to the cheat-sheet idea — the objection that a giant stored answer-table could
act mindlike with nobody home ([the lookup-table objection](lookup-table-objection.md)). That
objection pictures a thing producing mind-like behavior by *pure storage* — just looking answers up,
with no real processing or organization inside. But push on the size. A flat table big enough to
cover a mind's behavior can't physically exist (no room in the universe). So any machine that
actually *fits* and *matches* the behavior must be storing far less than the full list — which means
it has to *work each answer out* on the fly rather than just fetch it. And working answers out *is*
processing — organized inner machinery — exactly the thing "pure storage" was supposed to do
without. Upshot: "all the behavior, zero organization" simply isn't an available option at mind
scale; any buildable behavior-matcher (a real AI included) is an organized computer, not a dumb
lookup. The sticking point: a die-hard could insist that even a giant fetch-and-retrieve system is
still "just plumbing," not genuine mind-like organization — and whether that holds up is the central
open question in this corner of the debate.

### See also

- [realisable-behaviour-matcher-is-organised](../claims/realisable-behaviour-matcher-is-organised.md) — the conclusion this argument establishes.
- [lookup-table-physically-unrealisable](../claims/lookup-table-physically-unrealisable.md) — premise 1: the flat table cannot be stored.
- [lookup-table-size-exponential](../claims/lookup-table-size-exponential.md) — premise 2: anything smaller must compute its answers.
- [bounded-table-rejoinder](bounded-table-rejoinder.md) — the Block move this replies to.
- [lifetime-bounded-table-covers-encountered-inputs](../claims/lifetime-bounded-table-covers-encountered-inputs.md) — the coverage stipulation granted for
  the sake of argument.
- [lookup-table-possible](../claims/lookup-table-possible.md) — the separability claim it attacks on the realisable reading.
- [lookup-table-objection](lookup-table-objection.md) — the objection whose transfer to actual systems it undercuts.
- [lookup-table-lacks-mind](../claims/lookup-table-lacks-mind.md) — the conditional it deliberately leaves standing.
- [intuition-domain-asymmetry](intuition-domain-asymmetry.md) — the scale-based deflation it is distinguished from.
- [lookup-table-physical-impossibility](lookup-table-physical-impossibility.md) — establishes premise 1 but stops at
  "unbuildable".
- [grain](../concepts/grain.md) — the grain of role individuation on which organised computers may count as
  minded.
- [lookup-table-mind](../concepts/lookup-table-mind.md) — the no-organisation construction shown to be unrealisable.

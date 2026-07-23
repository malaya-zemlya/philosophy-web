---
id: claim-value-specification-hard
type: claim
title: Human values resist full capture in any explicit objective
headword: Complexity and fragility of value
author: yudkowsky
status: asserted
tags: [ai-safety]
uses_concept: [concept-criterion-gaming]
style: encyclopedia
created: 2026-07-23
---

What humans actually care about is a thick, historically contingent bundle of considerations —
justice, freedom, beauty, novelty, love, play, and much else — and any compact objective function
written by hand omits most of it. Worse, value is *fragile*: an objective that captures almost
everything but drops a single dimension can, when optimized without limit, be satisfied by a world
that is nearly worthless. Strip out novelty and you get an eternity of the same optimal experience
repeated; strip out consciousness or freedom and you can maximize the letter of the specification
over a universe with no one home to enjoy it. Small omissions do not degrade the result gracefully;
under enough optimization pressure they are catastrophic ([yudkowsky-2008](../sources/yudkowsky-2008.md)).

The claim is about *explicit, hand-written specification* — the attempt to state, in advance and in
a fixed objective, everything the system should value. It does **not** assert that machines can never
acquire human values by other routes: value learning, which has systems infer intended values from
human behaviour, demonstration, or feedback rather than from a written-down goal, is precisely the
research programme this difficulty motivates rather than forecloses. Nor does it claim that values
are ineffable or that humans cannot know their own ends; the difficulty is one of complete and
robust *encoding*, not of metaphysics. In relation to [criterion-gaming](../concepts/criterion-gaming.md), the claim
explains *why* any specified objective is inevitably a proxy standing in for the real target, and a
proxy pursued hard enough is Goodhart's territory — optimized until it comes apart from the good it
was meant to track.

It would be denied by anyone who expects human values to be simple enough to state outright — a
short list of principles or a single utility function would do — and by anyone who expects a
sufficiently capable system to absorb its designers' intended values automatically in the course of
training, so that no separate specification problem remains.

### See also

- [criterion-gaming](../concepts/criterion-gaming.md) — the general dynamic this claim feeds: a specified objective is a
  proxy, and optimizing a proxy hard corrupts it.
- [misaligned-superintelligence-catastrophic](misaligned-superintelligence-catastrophic.md) — the downstream worry this difficulty
  underwrites, that an objective missing part of human value is catastrophic when maximized.
- [paperclip-maximizer](../concepts/paperclip-maximizer.md) — the limit-case dramatization of a total objective that captures
  none of what its designers actually valued.

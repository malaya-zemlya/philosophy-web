---
id: argument-proportionality-thesis
type: argument
title: If increases in intelligence yield proportionate increases in design ability, self-improvement compounds into an explosion
headword: Proportionality argument
author: good
status: contested
pattern: cause-to-effect
tags: [ai-safety]
style: encyclopedia
created: 2026-07-23
concludes: claim-self-improvement-leads-to-explosion
uses_concept: [concept-intelligence-explosion]
---

The proportionality argument is the engine of I. J. Good's original conjecture ([good-1966](../sources/good-1966.md)),
here in the reconstruction David Chalmers gives it ([chalmers-2010](../sources/chalmers-2010.md)). Its claim is that if
each gain in a machine's intelligence buys a proportionate gain in that machine's ability to design
still more intelligence, then a machine that reaches the point of designing its own successors sets
off a self-amplifying climb — an [intelligence-explosion](../concepts/intelligence-explosion.md) that carries capability far past
the human level. The argument does not assert that such a machine will be built; it says that *if*
one is, and the returns to cognitive investment do not vanish, the cascade follows.

The inference form is a defeasible causal projection: from a causal generalisation about what a
gain in intelligence produces, together with the supposition that the process is set going, it
projects the downstream effect of iterating that generalisation. This is why the move instantiates
the *cause-to-effect* argument pattern — and, per that pattern, its critical questions map its
standard attack surface: is the causal generalisation true and strong, is some factor interfering,
is the link genuinely causal rather than correlational. Reconstructed as premises:

1. At some point an AI will be capable of designing AI more intelligent than itself — a "seed"
   system whose competence includes the very task of building minds.
2. *Proportionality*: each increment of intelligence brings a proportionate — that is, a
   non-vanishing — increment in the ability to design intelligence. A system one step smarter is
   correspondingly better at the task of making smarter systems.
3. Absent defeaters — resource ceilings, manufacturing limits, outside interference, a hard upper
   bound on possible intelligence — iterating the design step under premise 2 yields a
   self-amplifying sequence: each generation both more capable and faster at producing the next.

From these the conclusion follows defeasibly: a runaway cascade of ever-greater intelligence,
terminating far above the human level ([self-improvement-leads-to-explosion](../claims/self-improvement-leads-to-explosion.md)). The force of
the argument is entirely in the compounding — remove proportionality and the same seed system yields
at most a one-off improvement, not an explosion.

### Weakest premise

The weight rests on premise 2, proportionality. It is not a conceptual truth but an empirical
conjecture about the shape of the returns curve on cognitive investment: it assumes that the payoff
from getting smarter does not taper as one climbs. That is precisely where the standard objection
lands — [diminishing-returns-objection](diminishing-returns-objection.md) argues the returns diminish, so the curve bends
to a plateau rather than running away, and premise 2 fails. Premise 3 carries a subtler burden:
Chalmers himself catalogues the defeaters that could stall the climb — resource and energy limits,
structural obstacles, failures of motivation or correlation between successive systems, and the
possibility that intelligence has a low ceiling — so premise 3's "absent defeaters" clause is doing
real work, and each listed defeater is a way the projection can be blocked even if proportionality
holds locally.

### See also

- [diminishing-returns-objection](diminishing-returns-objection.md) — the standard objection, that returns on
  self-improvement diminish so proportionality fails; it attacks premise 2 directly.
- [self-improvement-leads-to-explosion](../claims/self-improvement-leads-to-explosion.md) — the claim this argument establishes: a
  design-capable AI cascades into runaway intelligence.
- [intelligence-explosion-self-limiting](../claims/intelligence-explosion-self-limiting.md) — the rival claim, that the cascade meets
  diminishing returns and levels off.
- [intelligence-explosion](../concepts/intelligence-explosion.md) — the runaway dynamic the argument's conclusion names, with
  Good's original statement and Chalmers's reconstruction.
- [superintelligence-feasibility](../questions/superintelligence-feasibility.md) — the prior question of whether superintelligence is
  reachable at all; this argument offers the explosion as one route to it.

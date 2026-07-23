---
id: argument-diminishing-returns-objection
type: argument
title: Returns on self-improvement diminish because problem difficulty scales and progress is bottlenecked outside the designer
headword: Diminishing-returns objection
author: chollet
status: asserted
tags: [ai-safety]
style: encyclopedia
created: 2026-07-23
attacks: [argument-proportionality-thesis, claim-self-improvement-leads-to-explosion]
supports: [claim-intelligence-explosion-self-limiting]
uses_concept: [concept-intelligence-explosion]
---

This objection raises the cause-to-effect pattern's **CQ1 (strength)** against the
[proportionality-thesis](proportionality-thesis.md): it denies that the causal generalisation at the heart of that
argument — each increment of intelligence buys a proportionate increment in design ability — is
true or strong enough to sustain the projection. It presses **CQ3 (interference)** in the same
breath: real bottlenecks outside the designer block extra intelligence from converting into extra
capability, so even a locally sound design step fails to compound. Where the proportionality
argument needs a non-vanishing return on cognitive investment, this objection argues the return
tapers, and the projected explosion never gets off the ground.

The inference form is a defeasible undercutting argument, drawn from François Chollet
([chollet-2017](../sources/chollet-2017.md)):

1. As a system's capability grows, the problems whose solution would improve it further grow harder
   at least as fast. Discovery has a low-hanging-fruit structure: the easy gains are taken first,
   and each further advance demands disproportionately more. The frontier recedes as you approach it.
2. Intelligence is *situational*, not a context-free scalar a mind can raise in isolation. Cognitive
   gains are bottlenecked by the data a system can gather, the interfaces through which it acts on
   the world, and the wall-clock time real-world experiments take to return results — none of which
   raw self-improvement accelerates. A mind cannot be spent faster than the world will answer.
3. Therefore the returns curve bends: self-improvement yields *sigmoidal* growth that rises and
   then levels off, not an unbounded runaway. The proportionality premise fails, and with it the
   projected [intelligence-explosion](../concepts/intelligence-explosion.md) ([intelligence-explosion-self-limiting](../claims/intelligence-explosion-self-limiting.md)).

The objection targets premise 2 of the proportionality argument at its root, and does not deny that
very capable AI is possible — only that its arrival would take the self-amplifying, spike-like form
the explosion thesis requires.

### Weakest premise

The vulnerable point is the empirical status of premises 1 and 2 — the claim that problem difficulty
scales with capability, and that the external bottlenecks are genuinely immovable. Both are
generalisations from present experience, and a sufficiently capable designer might partially
internalise the very bottlenecks the objection treats as fixed: improving its own data-efficiency so
it learns more from less, and running high-fidelity simulations in place of slow real-world
experiments. To that extent the wall the objection leans on may be lower than it looks. This is the
live rejoinder, and it is exactly the ground the proportionality thesis would contest — whether the
returns curve is bent by the world's structure, or only by contingent limits a smarter system could
engineer around.

### In plain terms

The explosion idea says that once an AI is smart enough to make a smarter AI, the process feeds on
itself and rockets past us. This objection says: not so fast. Two things get in the way. First, the
smarter you get, the harder the *remaining* problems are — the easy wins are used up early, so each
new step costs far more than the last. Second, being smart is not enough on its own: to actually
improve, a system needs data, needs to try things out in the real world, and has to wait for reality
to answer — and thinking faster does not make experiments finish faster. Put together, the growth
curve rises steeply and then flattens out (an S-shape), instead of shooting up forever. That flat
top is the [self-limiting](../claims/intelligence-explosion-self-limiting.md) view, against the
[proportionality argument](proportionality-thesis.md) that powers the explosion. The catch,
noted above: a clever enough system might learn to squeeze more out of less data and test ideas in
simulation, chipping away at exactly those roadblocks — so the debate stays open.

### See also

- [proportionality-thesis](proportionality-thesis.md) — the argument this objection attacks, whose proportionality
  premise it denies.
- [intelligence-explosion-self-limiting](../claims/intelligence-explosion-self-limiting.md) — the claim this objection supports: self-improvement
  meets diminishing returns and levels off.
- [self-improvement-leads-to-explosion](../claims/self-improvement-leads-to-explosion.md) — the opposing claim, that self-improvement compounds
  into runaway growth.
- [intelligence-explosion](../concepts/intelligence-explosion.md) — the runaway dynamic the objection argues is self-limiting.
- [superintelligence-feasibility](../questions/superintelligence-feasibility.md) — the prior question of whether superintelligence is
  reachable; this objection bears on whether the explosion is a viable route.

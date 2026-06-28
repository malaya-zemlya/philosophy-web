---
id: claim-complete-self-representation-impossible
type: claim
title: No finite system can losslessly represent its entire current state within itself
headword: Self-representation incompleteness
author: mishka
status: asserted
tags: [philosophy-of-mind, ai, computation]
uses_concept: [concept-introspective-gap-varieties]
style: encyclopedia
created: 2026-06-05
---

No finite system can hold, within its current state, a lossless representation of that entire current
state while keeping any capacity for other functions.

### Gloss

By a capacity or pigeonhole bound, a proper part cannot injectively encode the whole; the only escape
— the self-model occupying the *entire* state — leaves nothing to perceive, act, or even run the
read-out. Self-modelling is therefore necessarily lossy, partial, sequential (and so stale), or
externally instrumented. The formal derivation is [finite-self-model-incomplete](../arguments/finite-self-model-incomplete.md).

### Scope

The claim is about *complete, simultaneous, internal, lossless* self-access only. It does not forbid
partial or compressed self-models, sequential self-report over time, or external instrumentation; and
it is an *access* or capacity claim, silent on phenomenality
([access-vs-phenomenal-consciousness](../concepts/access-vs-phenomenal-consciousness.md)) — the same access/phenomenal divide the gap-varieties
turn on ([introspective-gap-varieties](../concepts/introspective-gap-varieties.md)). The Kleene recursion theorem and quines are no
counterexample: a program's *source* is a compressed static description emitted sequentially to an
external medium, not a lossless image of its own runtime state.

### Independent physical pedigree

A sharper, measurement-theoretic form is Breuer's self-measurement impossibility
([breuer-1995](../sources/breuer-1995.md)): no apparatus that is a *proper subsystem* of a system can distinguish all
that system's present states, for classical and quantum theories alike, deterministic or stochastic.

### Who would deny it

Someone who lets the self-model live outside the state (an external observer — which concedes the
point for the internal case), or who only ever needs *partial* access.

### Distinct from neighbours

Distinct from [lookup-table-physically-unrealisable](lookup-table-physically-unrealisable.md): kin in spirit (a representation of the
whole cannot fit), but that is a *cosmological size* bound on a behaviour-table, whereas this is a
*within-system pigeonhole* bound on representing one's own current state.

### In plain terms

A complete, exact copy of everything you are right now can't fit *inside* you, because the copy would
itself be one more thing that needs copying — and a finite system runs out of room. So any workable
self-model has to leave something out, blur something, or read itself out a piece at a time (by which
point the picture is already stale). It is strictly a limit on *reaching all your own current details
from inside*, not a claim that anything is spooky or missing from the world.

### See also

- [finite-self-model-incomplete](../arguments/finite-self-model-incomplete.md) — the capacity argument that establishes this claim.
- [access-vs-phenomenal-consciousness](../concepts/access-vs-phenomenal-consciousness.md) — marks this as an access result, silent on feeling.
- [lookup-table-physically-unrealisable](lookup-table-physically-unrealisable.md) — a kin "can't fit" bound, distinguished (size vs. self-reference).

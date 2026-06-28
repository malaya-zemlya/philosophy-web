---
id: argument-sorites-paradox
type: argument
title: The sorites paradox (the heap)
headword: Sorites paradox
author: eubulides
status: asserted
tags: [vagueness, sorites]
premise: [claim-sorites-tolerance]
attacks: claim-heap-predicate-sharp
uses_concept: [concept-continuity-argument-schema]
presupposes: []
style: encyclopedia
created: 2026-06-04
---

The *sorites paradox* — from the Greek *sōros*, "heap" — is the ancient puzzle of the vague
predicate. A million grains of sand make a heap. Removing one grain surely cannot turn a heap into a
non-heap. Yet if removal never matters, one can strip the pile away grain by grain down to a single
grain and still be forced to call it a heap, which is absurd. Something in the apparently flawless
reasoning must fail, but every step looks innocent. The argument is traditionally credited to
Eubulides of Miletus.

### The reasoning

The paradox has the form of a *reductio*: a chain of small, individually unobjectionable steps that
together yield a contradiction.

1. A heap of a million grains is a heap. (The base case — an uncontroversial stipulation.)
2. Removing a single grain from a heap always leaves a heap. ([the
   tolerance premise](../claims/sorites-tolerance.md) — formally, the verdict "heap" makes no jump across any one admissible step.)
3. Applying step 2 repeatedly, starting from step 1 and running down the connected chain of
   removals, eventually reaches a single grain — which is plainly not a heap. Contradiction.

∴ The naive picture of vagueness — that there is a precise, exact grain-count at which "heap" stops
applying ([a sharp heap boundary](../claims/heap-predicate-sharp.md)) — cannot stand: one cannot keep
bivalence, no sharp cutoff, tolerance, and a connected path of negligible steps all at once.

### A paradox, not a solution

The sorites is the paradigm instance of the [continuity-argument-schema](../concepts/continuity-argument-schema.md): the predicate is
modelled as a function from a space of cases ($X$ = grain-counts under one-grain removal) into a
space of verdicts ($Y$ = {heap, non-heap}). Run forward, it forces the schema's five-way disjunction
but does not, by itself, choose among the horns. Selecting one — a sharp-but-unknown cutoff, degrees
of heaphood, a truth-value gap, a single non-negligible step, or no real distinction at all — is the
work of the rival theories of vagueness, not of the paradox. The argument establishes only that one
horn must give.

### The weakest premise

Premise 2 is where the argument is most exposed. The *disconnection* response denies tolerance
outright: some single removal really does flip the verdict — for the epistemicist, at a precise but
unknowable boundary. The paradox's force against [a sharp boundary](../claims/heap-predicate-sharp.md) is
therefore exactly as strong as the tolerance premise is compelling.

### In plain terms

A million grains of sand is a heap. Take away one grain — still a heap. Surely removing a single
grain could never turn a heap into a non-heap. But keep going and you arrive at one lonely grain,
which is plainly *not* a heap. So where, exactly, did "heap" stop being true? Every step looked
harmless, yet the harmless steps somehow add up to a contradiction. That's the paradox. It doesn't
hand you the solution — it just proves something has to give: maybe there's a secret exact cutoff,
maybe "heap" is really a matter of degree, maybe somewhere in the middle there's no fact of the
matter, or maybe one of those "harmless" single grains wasn't so harmless after all. It's the
textbook example of the no-sharp-line pattern, and the same shape returns wherever you swap "grains
of sand" for "neurons replaced by chips" or "the planks of a ship."

### See also

- [continuity-argument-schema](../concepts/continuity-argument-schema.md) — the master template this is the paradigm instance of; it
  proves the five horns jointly exhaust the responses.
- [sorites-tolerance](../claims/sorites-tolerance.md) — the inductive premise (step 2) that does the damage.
- [heap-predicate-sharp](../claims/heap-predicate-sharp.md) — the naive sharp-boundary picture this argument refutes.

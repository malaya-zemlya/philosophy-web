---
id: argument-sorites-paradox
type: argument
title: The sorites paradox (the heap)
author: eubulides
status: asserted
tags: [vagueness, sorites]
premise: [claim-sorites-tolerance]
attacks: claim-heap-predicate-sharp
uses_concept: [concept-continuity-argument-schema]
presupposes: []
style: legacy
created: 2026-06-04
---

Form: reductio / paradox. The paradigm instance of [continuity-argument-schema](../concepts/continuity-argument-schema.md) — `X` =
grain-counts under one-grain removal, `Y` = {heap, non-heap}.

1. A heap of a million grains is a heap. (base case — uncontroversial stipulation)
2. Removing a single grain from a heap always leaves a heap. ([sorites-tolerance](../claims/sorites-tolerance.md) — the
   tolerance premise; formally, the heap-verdict makes no jump across one admissible step)
3. Iterating (2) from (1) along the connected chain of removals reaches a single grain — which is
   not a heap. Contradiction.
∴ The naive picture ([heap-predicate-sharp](../claims/heap-predicate-sharp.md)) cannot stand: one cannot keep bivalence,
   no-sharp-cutoff, tolerance, and a connected path of negligible steps all at once.

Which horn it takes: *none by itself.* The sorites is the schema run forward; it forces the
five-way disjunction of [continuity-argument-schema](../concepts/continuity-argument-schema.md) but does not select a horn. Choosing a
horn (sharp-but-unknown cutoff / degrees / truth-value gaps / a non-negligible step / no real
distinction) is what the rival theories of vagueness do — this argument only establishes that one
horn must give.

Weakest premise: (2). The disconnection-horn response denies tolerance outright (some single
removal does flip the verdict, e.g. the epistemicist's hidden boundary); the argument's force
against [heap-predicate-sharp](../claims/heap-predicate-sharp.md) is exactly as strong as tolerance is compelling.

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

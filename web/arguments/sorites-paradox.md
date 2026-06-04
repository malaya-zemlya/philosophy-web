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
created: 2026-06-04
---

Form: reductio / paradox. The paradigm instance of concept-continuity-argument-schema — `X` =
grain-counts under one-grain removal, `Y` = {heap, non-heap}.

1. A heap of a million grains is a heap. (base case — uncontroversial stipulation)
2. Removing a single grain from a heap always leaves a heap. (claim-sorites-tolerance — the
   tolerance premise; formally, the heap-verdict makes no jump across one admissible step)
3. Iterating (2) from (1) along the connected chain of removals reaches a single grain — which is
   not a heap. Contradiction.
∴ The naive picture (claim-heap-predicate-sharp) cannot stand: one cannot keep bivalence,
   no-sharp-cutoff, tolerance, and a connected path of negligible steps all at once.

Which horn it takes: *none by itself.* The sorites is the schema run forward; it forces the
five-way disjunction of concept-continuity-argument-schema but does not select a horn. Choosing a
horn (sharp-but-unknown cutoff / degrees / truth-value gaps / a non-negligible step / no real
distinction) is what the rival theories of vagueness do — this argument only establishes that one
horn must give.

Weakest premise: (2). The disconnection-horn response denies tolerance outright (some single
removal does flip the verdict, e.g. the epistemicist's hidden boundary); the argument's force
against claim-heap-predicate-sharp is exactly as strong as tolerance is compelling.

---
id: claim-sorites-tolerance
type: claim
title: Removing a single grain from a heap always leaves a heap
author: eubulides
status: asserted
tags: [vagueness, sorites]
created: 2026-06-04
---

gloss: the *tolerance* (inductive) premise of the sorites — the verdict "heap" is insensitive to
any single admissible small step; no one-grain removal can turn a heap into a non-heap.

scope: a claim about the *predicate's* insensitivity to a unit step, not about how many grains a
heap has. It is the premise that, conjoined with an uncontroversial base case (a large pile is a
heap), generates the paradox. Read formally it is a no-large-jumps / uniform-continuity constraint
on the heap-verdict over the one-grain-removal adjacency.

who would deny it: anyone taking the *disconnection* horn of [continuity-argument-schema](../concepts/continuity-argument-schema.md) —
the epistemicist (there is a precise but unknown grain at which one removal flips the verdict) and
anyone who holds some single step is, after all, not negligible.

Distinct from a base-case claim ("a million grains is a heap"): tolerance is the *step* premise, not
the *anchor*. Together they are inconsistent with the heap-verdict being sharp and bivalent —
which is the work of [sorites-paradox](../arguments/sorites-paradox.md).

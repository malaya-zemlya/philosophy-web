---
id: claim-sorites-tolerance
type: claim
title: Removing a single grain from a heap always leaves a heap
headword: Sorites tolerance
author: eubulides
status: asserted
tags: [vagueness, sorites]
style: encyclopedia
created: 2026-06-04
---

The *tolerance* premise of the sorites paradox: the verdict "heap" is insensitive to any single
admissible small step, so no one-grain removal can turn a heap into a non-heap. It is also called the
*inductive* premise, because it is what licenses iterating the small step along the whole chain.

This is a claim about the *predicate's* insensitivity to a unit step, not about how many grains a
heap contains. Conjoined with an uncontroversial base case — a large pile is a heap — it generates
the paradox. Read formally, it is a no-large-jumps or uniform-continuity constraint on the
heap-verdict across the one-grain-removal adjacency.

It is denied by anyone who takes the *disconnection* horn of the
[continuity-argument-schema](../concepts/continuity-argument-schema.md): the epistemicist, who holds that there is a precise but
unknown grain at which a single removal flips the verdict, and anyone else who maintains that some
single step is, after all, not negligible.

Distinct from a base-case claim ("a million grains is a heap"): tolerance is the *step* premise, not
the *anchor*. Taken together the two are inconsistent with the heap-verdict being both sharp and
bivalent — which is the work of the [sorites paradox](../arguments/sorites-paradox.md).

### In plain terms

The premise that does the damage in the heap paradox: take one grain off a heap and you've still got
a heap — no single grain removal could ever flip "heap" into "non-heap." It sounds obviously true.
But chain it from a big pile all the way down to a single grain and it leads straight to a
contradiction — which is why something about this innocent-looking step has to give.

### See also

- [continuity-argument-schema](../concepts/continuity-argument-schema.md) — the template whose tolerance/connectedness premise this
  supplies; denying it is the schema's disconnection horn.
- [sorites-paradox](../arguments/sorites-paradox.md) — the argument this premise drives.
- [heap-predicate-sharp](heap-predicate-sharp.md) — the sharp-boundary target the paradox refutes using this premise.

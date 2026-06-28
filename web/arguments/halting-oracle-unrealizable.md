---
id: argument-halting-oracle-unrealizable
type: argument
title: The halting oracle is coherent yet physically unrealizable
headword: Unrealizable halting oracle
author: mishka
status: asserted
tags: [computability, philosophy-of-mind, metaphysics]
premise: [claim-halting-problem-undecidable, claim-physical-church-turing-thesis]
concludes: claim-halting-oracle-coherent-but-unrealizable
uses_concept: [concept-halting-oracle]
style: encyclopedia
created: 2026-06-08
---

This argument shows that a single, well-understood mathematical object — the halting oracle — is
*coherent yet impossible to build*. It runs as a short deduction from two premises, one a
theorem and one a claim about physics.

### The inference

The form is *deductive*. It combines a result about computation with a thesis about what nature
can compute:

1. No Turing machine decides the halting problem ([halting-problem-undecidable](../claims/halting-problem-undecidable.md)). This is
   Turing's 1936 theorem, not an empirical conjecture.
2. Every physically realizable computation is Turing-computable
   ([the physical Church–Turing thesis](../claims/physical-church-turing-thesis.md)).

From these it follows that no physical device computes the halting function. Yet the halting
oracle is a *consistent, richly theorized* abstract object — the engine of the theory of relative
computability ([halting-oracle](../concepts/halting-oracle.md)). So the oracle is mathematically coherent but
physically unrealizable ([halting-oracle-coherent-but-unrealizable](../claims/halting-oracle-coherent-but-unrealizable.md)).

### The weakest premise

The soft spot is premise (2), the physical Church–Turing thesis. Unlike (1), which is a proven
theorem and not in play, (2) is a *contingent* claim about the physical world, and it is
contested. *Hypercomputation* proposals — Malament–Hogarth spacetimes, infinite-time Turing
machines — describe physical setups that would out-compute any Turing machine; and for brains
specifically, Penrose's appeal to non-computable physics ([consciousness-noncomputable](../claims/consciousness-noncomputable.md))
denies it outright. If (2) fails, the oracle might be physically realizable after all.

### What it does and does not claim

The conclusion is *physical* unrealizability, not metaphysical impossibility. The oracle remains
a coherent abstract object — there is a possible world containing one. That is deliberate: the
argument is aimed at the bridge from conceivability to *physical* realizability
([conceivability-not-sufficient-for-physical-realizability](../claims/conceivability-not-sufficient-for-physical-realizability.md)), not at the metaphysical
bridge from conceivability to possibility.

### In plain terms

Two steps. First, a theorem: no ordinary computer can solve the halting problem. Second, a bet about
physics: nature has no computer stronger than an ordinary one. Put them together and *nothing physical*
can solve halting — even though the "halting oracle" that would is a perfectly coherent, well-studied
mathematical idea. So it's coherent but unbuildable. The soft spot is the second step: if some exotic
physics could out-compute a normal computer (which is what Penrose's theory of mind actually needs),
the oracle might be buildable after all.

### See also

- [halting-problem-undecidable](../claims/halting-problem-undecidable.md) — premise (1); Turing's theorem.
- [physical-church-turing-thesis](../claims/physical-church-turing-thesis.md) — premise (2) and the argument's weakest link.
- [halting-oracle](../concepts/halting-oracle.md) — the object the argument is about.
- [halting-oracle-coherent-but-unrealizable](../claims/halting-oracle-coherent-but-unrealizable.md) — the conclusion.
- [conceivability-not-sufficient-for-physical-realizability](../claims/conceivability-not-sufficient-for-physical-realizability.md) — the broader lesson this
  case feeds.
- [consciousness-noncomputable](../claims/consciousness-noncomputable.md) — Penrose's denial of premise (2) for brains.

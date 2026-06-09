---
id: concept-halting-oracle
type: concept
title: The halting oracle (and uncomputability)
author: turing
status: asserted
tags: [computability, philosophy-of-mind, modality, metaphysics]
created: 2026-06-08
---

primary definition: the **halting problem** asks, of an arbitrary program and input, whether the
program eventually halts. Turing proved it **undecidable**: no Turing machine answers it for all cases
([turing-1936](../sources/turing-1936.md), by a diagonal argument). A **halting oracle** is a hypothetical black box
that *does* return the answer — posited as an *oracle* to define **relative computability** (what
becomes computable *given* the oracle). This is not a fringe fiction but the object of a whole rigorous
theory: oracle machines, **Turing degrees**, the arithmetical hierarchy.

the key feature that makes it useful here: the halting oracle is **precisely specified and consistently
theorized** — *positively* conceivable, not merely "no contradiction noticed" — yet provably *not
Turing-computable*. Whether it is *physically* realizable turns on the **physical Church–Turing thesis**
([physical-church-turing-thesis](../claims/physical-church-turing-thesis.md)); standard physics says no, while **hypercomputation**
proposals (Malament–Hogarth spacetimes; infinite-time Turing machines) dispute it.

the disputes it feeds:
- a clean, non-definitional case of *conceivable/coherent but physically unrealizable*
  ([halting-oracle-coherent-but-unrealizable](../claims/halting-oracle-coherent-but-unrealizable.md), [conceivability-not-sufficient-for-physical-realizability](../claims/conceivability-not-sufficient-for-physical-realizability.md))
  — sharper than the water=H₂O case because there is no "you mislabelled it" escape.
- the formal backbone of *internal-vs-external derivability* ([explanation-must-be-internally-traversable](../claims/explanation-must-be-internally-traversable.md)).
- a building block for **Gödelian anti-mechanism** about minds — Penrose holds the brain exploits
  *non-computable* physics ([consciousness-noncomputable](../claims/consciousness-noncomputable.md), [noncomputable-consciousness](../positions/noncomputable-consciousness.md)),
  i.e. denies the physical Church–Turing thesis for brains.

### In plain terms

There's a famous question — "will this program eventually stop, or run forever?" — and Turing proved
*no* computer program can answer it reliably for every case. A "halting oracle" is an imaginary gadget
that just *knows* the answer. The striking thing: mathematicians have built an entire, perfectly
consistent theory around such gadgets (what you *could* compute if you had one) — so it's a fully
coherent, precisely-defined idea — and yet it's provably impossible for any ordinary computer to be
one. That makes it a clean example of something you can rigorously *describe and reason about* but (on
standard physics) can never actually *build*.

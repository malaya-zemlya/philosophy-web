---
id: argument-unwarrantable-zombie-premise
type: argument
title: The unwarrantable premise — the zombie argument's conceivability premise cannot be cogently asserted
headword: Unwarrantable-premise objection
author: mishka
status: asserted
tags: [philosophy-of-mind, consciousness, modality, computability, self-reference]
premise: [claim-ideal-conceivability-is-apriori-consistency, claim-consistency-certification-is-oracle-hard, claim-cogency-requires-accessible-noncircular-warrant]
concludes: claim-zombie-premise-unwarrantable
attacks: [argument-zombie-conceivability]
uses_concept: [concept-halting-oracle, concept-philosophical-zombie, concept-dialectical-cogency]
presupposes: [claim-physical-church-turing-thesis]
style: encyclopedia
created: 2026-06-24
---

This objection opens a third front against the [zombie argument](zombie-conceivability.md),
orthogonal to the two the literature already works. It raises a *warrant*-level question that is distinct
from the [thought-experiment pattern](../../patterns/thought-experiment.md)'s standard *coherence* and
*bridge* critical questions: it grants that zombies may be ideally conceivable (coherence) **and** grants
that ideal conceivability entails possibility (bridge, [conceivability-entails-possibility](../claims/conceivability-entails-possibility.md)), and
attacks instead the conceiver's entitlement to assert the first premise at all. The charge is not that the
argument is unsound but that it is not **cogent** — it cannot rationally move the physicalist it targets.

### The argument

The inference is deductive, governed by a dialectical constraint on cogency.

1. ([cogency-requires-accessible-noncircular-warrant](../claims/cogency-requires-accessible-noncircular-warrant.md)) An argument moves its opponent only if its
   premises admit accessible, non-question-begging warrant.
2. ([ideal-conceivability-is-apriori-consistency](../claims/ideal-conceivability-is-apriori-consistency.md)) The first premise of the zombie argument —
   that $Z = P \wedge \neg C$ is ideally conceivable — is the consistency claim $\mathrm{Con}_a(Z)$.
3. ([consistency-certification-is-oracle-hard](../claims/consistency-certification-is-oracle-hard.md)) Reliably certifying the consistency of a scenario
   as rich as a complete physics is at least as hard as the halting problem, hence beyond any effective
   faculty.
4. *Trilemma on the mind* (below): every way of possessing a non-effective certifying faculty defeats the
   argument's purpose.

∴ The conceivability premise is unwarrantable by a computable reasoner, and warrantable by others only at a
disqualifying cost ([zombie-premise-unwarrantable](../claims/zombie-premise-unwarrantable.md)). So the zombie argument fails as a cogent a
priori proof — which is why this move `attacks` [zombie-conceivability](zombie-conceivability.md) without denying any of
its premises.

### The trilemma

Two yes/no questions partition the views exhaustively. **Is the mind physical?** If no — horn **D3** — the
reasoner has the faculty only because minds are not wholly physical, which *is* the anti-physicalist
conclusion: the warrant for premise (1) presupposes what the argument set out to prove (a transparent
breach of non-circularity). If yes, **does the physical Church–Turing thesis hold of the reasoning
substrate?** If yes — horn **D1** — the reasoner computes only Turing-computable functions, so by step 3
cannot possess the certifying faculty, and the premise is simply *unwarrantable* (the available surrogate
delivers only "no contradiction found so far," the prima facie notion the argument disavows). If no — horn
**D2** — the reasoner's own substrate is a hypercomputer: the Penrose-style
[noncomputable-consciousness](../positions/noncomputable-consciousness.md) ([penrose-1994](../sources/penrose-1994.md)). This horn is coherent and is not here
claimed false, but it is (i) a contested *empirical* thesis about the physics of cognition, unavailable to
an argument that advertises itself as a priori, and (ii) explicitly denied by the argument's principal
target, *computational* physicalism. It rescues the premise only by importing what the method forbids and
the opponent rejects.

### The weakest premise

The decisive load is not borne by the computability result but by **premise (1) together with the
warrant-trichotomy that backs step 4** — the claim that *every* warrant a computable reasoner could have
for $\mathrm{Con}_a(Z)$ is one of exactly three: finite failure-to-refute (only $\Sigma_1$ evidence, hence
prima facie and insufficient), a demonstrative consistency proof (which would *exhibit a model* of
$P \wedge \neg C$ — asserting, not conceiving, $\Diamond Z$, and so begging the question), or a positive
grasp of a zombie-world structure (likewise question-begging). A modal rationalist of a Williamson/Bealer
cast will press for a *fourth* source: a fallible-but-positive modal insight that is neither exhaustive
search nor model-construction. The objection answers that any *reliable* such insight collapses into D2 or
D3 (a faculty that reliably outruns proof-search computes a non-computable set, whatever it is called), so
the rationalist's only remaining option is a *fallible positive* warrant — and whether such a thing exists,
distinct from the disavowed prima facie notion, is the genuine open crux on which the objection ultimately
rests.

### A note on the apparatus

The recursion-theoretic machinery is sharp but heavier than the conclusion strictly needs. A single
sentence $\mathrm{Con}_a(Z)$ is trivially decidable in isolation, and isolated $\Pi_1$ truths *are* known
piecemeal by proof — so the global $\equiv_T \emptyset'$ result does not by itself forbid warrant for the
one scenario $Z$. What actually carries the objection is the epistemic point that *ideal* conceivability of
an arithmetic-rich scenario outruns the $\Sigma_1$ evidence finite inspection supplies, and that the only
stronger warrant is question-begging. The computability theorem furnishes the precise reason inspection can
never close that gap; the persuasive weight is dialectical. (A secondary technical caveat: a *complete*
$P$ is plausibly not recursively axiomatized, so the tidy Turing-*equivalence* overstates — but the
load-bearing lower bound, that certification is at least $\emptyset'$-hard, is only strengthened if $P$ is
non-r.e.)

### How it differs from its neighbours

- The **type-B** reply (a posteriori necessity) denies the bridge [conceivability-entails-possibility](../claims/conceivability-entails-possibility.md);
  this objection *grants* the bridge and reaches a type-B-friendly conclusion without the semantics of
  phenomenal concepts.
- **Dennett**'s line denies that zombies are conceivable at all (the coherence question); this grants
  conceivability-in-principle and attacks only the *warrant* to assert it.
- The **anti-zombie** symmetry cancels the conceiving with a mirror-image conceiving; this removes the
  faculty *both* conceivings would require, rather than balancing them.
- It is the computability-theoretic sibling of [halting-oracle-unrealizable](halting-oracle-unrealizable.md) and
  [mary-omniscience-unrealizable](mary-omniscience-unrealizable.md): where those deny a *physical realizer* to an idealized
  capacity (a halting oracle; an embedded total knower), this denies an *accessible warrant* to an
  idealized conceiving — the same oracle-unrealizability moral, turned from metaphysics to epistemology.

### In plain terms

The zombie argument starts: "a being physically just like us but with no inner experience is coherently
conceivable." This objection doesn't say that's false. It says no ordinary thinker can ever be *entitled*
to assert it. To be entitled, you'd have to certify that a complete physics-with-consciousness-subtracted
hides *no* contradiction anywhere — and certifying "no hidden contradiction, ever" in a setup rich enough
to describe computers is provably as hard as solving the halting problem, which no computer can do. So a
computable mind can only ever say "found none yet," which everyone agrees proves nothing. The escapes all
backfire: claim a magic non-computer faculty and either your brain runs on exotic physics no a priori
armchair argument may assume, or your mind isn't physical — which is just to assume the dualism the
argument was supposed to prove. Either way, the argument can't move a physicalist who reasons, as we do,
without an oracle.

### See also

- [zombie-conceivability](zombie-conceivability.md) — the target: this objection undercuts its cogency without denying a
  premise.
- [zombie-premise-unwarrantable](../claims/zombie-premise-unwarrantable.md) — the conclusion established.
- [cogency-requires-accessible-noncircular-warrant](../claims/cogency-requires-accessible-noncircular-warrant.md), [ideal-conceivability-is-apriori-consistency](../claims/ideal-conceivability-is-apriori-consistency.md),
  [consistency-certification-is-oracle-hard](../claims/consistency-certification-is-oracle-hard.md) — the three premises.
- [physical-church-turing-thesis](../claims/physical-church-turing-thesis.md) — the thesis whose holding (D1) or failing (D2) splits the trilemma.
- [noncomputable-consciousness](../positions/noncomputable-consciousness.md) / [penrose-1994](../sources/penrose-1994.md) — the D2 escape and its cost.
- [halting-oracle](../concepts/halting-oracle.md) — the formal backbone: the logically omniscient certifier is a halting oracle.
- [halting-oracle-unrealizable](halting-oracle-unrealizable.md), [mary-omniscience-unrealizable](mary-omniscience-unrealizable.md) — the sibling
  oracle-unrealizability arguments, of which this is the epistemic case.
- [conceivability-entails-possibility](../claims/conceivability-entails-possibility.md) — the bridge this objection conspicuously *grants*.

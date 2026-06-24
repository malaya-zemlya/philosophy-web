---
id: claim-consistency-certification-is-oracle-hard
type: claim
title: Reliably certifying the consistency of arithmetic-rich scenarios is at least as hard as the halting problem
headword: Consistency-certification is oracle-hard
author: mishka
status: asserted
tags: [computability, modality, philosophy-of-mind, metaphysics]
uses_concept: [concept-halting-oracle]
style: encyclopedia
created: 2026-06-24
---

Any method that *reliably* returns correct consistency-verdicts for theories rich enough to interpret
arithmetic thereby decides the halting problem, and so is not an effective (Turing-computable) procedure.
The hardness lives in the *method*, not in any single instance: a fixed sentence "$T$ is consistent" has a
determinate truth value that a trivial one-state machine could output; what is uncomputable is a procedure
that tracks consistency *across the class* without being told the answer.

The reduction is standard. Let $Q$ be Robinson arithmetic and, for a Turing machine $M$ and input $x$,
let $h_{M,x}$ be the $\Sigma_1$ sentence "$M$ halts on $x$." Consider
$$ T_{M,x} := Q \cup \{\neg h_{M,x}\}. $$
If $M$ halts on $x$ then $h_{M,x}$ is a true $\Sigma_1$ sentence, so $Q \vdash h_{M,x}$ and $T_{M,x}$ is
inconsistent; if $M$ does not halt then $\mathbb{N} \models T_{M,x}$ and it is consistent. Hence
$$ T_{M,x}\ \text{consistent} \iff M\ \text{does not halt on}\ x, $$
so a reliable consistency-tester decides the complement of the halting set, i.e. computes $\emptyset'$. For
*recursively axiomatized* theories "inconsistent" is $\Sigma_1$ (search for a proof of $\bot$), so
"consistent" is $\Pi_1$ and the verdict-function is $\Pi_1$-complete, $\equiv_T \emptyset'$. By Turing's
theorem ([turing-1936](../sources/turing-1936.md)) $\emptyset'$ is not computable, so no effective method reliably certifies
consistency here.

**What carries the weight.** The load-bearing direction is the *lower* bound — certification is at
**least** $\emptyset'$-hard — which needs only that the scenario interpret arithmetic. The matching upper
bound ($\Pi_1$, decidable relative to $\emptyset'$) assumes the theory is recursively axiomatized; a
genuinely *complete* physical description $P$ may not be, in which case certification is harder still, not
easier. Either way no effective method suffices. A faculty relabelled "rational insight" does not escape:
if it reliably outruns proof-search on these inputs it computes a non-computable set, and naming it insight
rather than computation does not lower its Turing degree.

**Scope.** A claim about the *complexity of a method*, neutral on whether minds possess non-effective
faculties — that is the further question handled by the trilemma of
[unwarrantable-zombie-premise](../arguments/unwarrantable-zombie-premise.md). It does not say any particular consistency fact is unknowable;
isolated facts are known piecemeal by proof.

Distinct from [halting-problem-undecidable](halting-problem-undecidable.md), which states the undecidability of one function: this
claim transports that result onto *consistency-* (hence ideal-conceivability-) certification over a class,
which is what links computability to the [conceivability](../concepts/philosophical-zombie.md) premise. It is
the engine behind the slogan that the logically omniscient sage — who knows at once every consequence of
what is given — simply *is* a halting oracle ([halting-oracle](../concepts/halting-oracle.md)).

### In plain terms

There is no general, mechanical way to certify that a rich theory is *free of hidden contradiction*. You
can always *catch* an inconsistency if one exists — just grind through proofs until a contradiction turns
up — but confirming there is *none*, across the board, would let you solve the halting problem, which
Turing proved no computer can. The trick is a dial that converts "machine $M$ runs forever" into "this
little theory is consistent," so a consistency-checker would secretly be a halting-checker. The upshot:
verifying that a scenario as rich as a complete physics is genuinely coherent is not the kind of thing a
finite, step-by-step reasoner can do — it needs an oracle no ordinary computer can be.

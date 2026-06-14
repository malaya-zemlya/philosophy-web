---
id: claim-halting-problem-undecidable
type: claim
title: No Turing machine decides the halting problem
headword: Halting problem undecidable
author: turing
status: asserted
tags: [computability, logic]
uses_concept: [concept-halting-oracle]
style: legacy
created: 2026-06-08
---

gloss: there is no Turing machine that, given an arbitrary program and input, always correctly outputs
whether the program halts. Proved by Turing (1936; [turing-1936](../sources/turing-1936.md)) via a diagonal argument: a
supposed halting-decider can be turned against itself to produce a contradiction.

scope: a *mathematical theorem* about Turing machines — a priori and certain. It says nothing, by
itself, about *physical* machines (that needs [physical-church-turing-thesis](physical-church-turing-thesis.md)) nor about
*oracles* (a halting oracle is *defined* to do exactly what no Turing machine can — see
[halting-oracle](../concepts/halting-oracle.md)).

who would deny it: essentially no one — it is a proved theorem. Disputes in this neighbourhood are
about its *interpretation and reach* (e.g. whether it bears on minds), not its truth.

Distinct from [physical-church-turing-thesis](physical-church-turing-thesis.md): that is the contingent bridge from
"Turing-uncomputable" to "physically unrealizable"; this is the pure computability fact.

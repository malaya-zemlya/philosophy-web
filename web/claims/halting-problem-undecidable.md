---
id: claim-halting-problem-undecidable
type: claim
title: No Turing machine decides the halting problem
headword: Undecidability of the halting problem
author: turing
status: asserted
tags: [computability, logic]
uses_concept: [concept-halting-oracle]
style: encyclopedia
created: 2026-06-08
---

There is no Turing machine that, given an arbitrary program and input, always correctly reports
whether that program eventually halts or runs forever. This is the *undecidability of the halting
problem*, proved by Alan Turing in 1936 ([turing-1936](../sources/turing-1936.md)). The proof is a *diagonal
argument*: assume a machine $H$ that decides halting for every program, then feed it a program built
to do the opposite of whatever $H$ predicts about that program's own behaviour, and $H$ is forced
into a contradiction. So no such $H$ exists.

This is a *mathematical theorem* about Turing machines — a priori and certain. By itself it says
nothing about *physical* machines (carrying it over to them requires the
[physical Church–Turing thesis](physical-church-turing-thesis.md)), and nothing about *oracles*:
a [halting oracle](../concepts/halting-oracle.md) is simply *defined* to do what no Turing machine can.

Essentially no one denies it; it is a proved result. The live disputes in this neighbourhood are
about its *interpretation and reach* — for instance whether it bears on the nature of minds — not
about its truth.

Distinct from [the physical Church–Turing thesis](physical-church-turing-thesis.md): that is the
contingent bridge from "Turing-uncomputable" to "physically unrealizable"; this is the pure
computability fact on the abstract side of that bridge.

### In plain terms

Some yes/no questions can't be answered by any computer program, however powerful. The classic
example: write a program that looks at *any* other program and reliably says whether it will
eventually finish or get stuck running forever. Turing proved in 1936 that no such universal checker
can exist. The trick is to imagine you had one, then build a program designed to do the opposite of
whatever the checker predicts about it — which makes the checker's answer wrong by construction.
Since the assumption leads to a contradiction, the checker can't exist.

### See also

- [halting-oracle](../concepts/halting-oracle.md) — the hypothetical device defined to decide halting, which this theorem
  says no Turing machine is.
- [physical-church-turing-thesis](physical-church-turing-thesis.md) — the bridge needed to extend this from abstract to
  physical machines.

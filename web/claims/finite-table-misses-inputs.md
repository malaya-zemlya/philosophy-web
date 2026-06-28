---
id: claim-finite-table-misses-inputs
type: claim
title: For any finite lookup table there are finite inputs outside its stored domain, to which it can only "respond" by ignoring the excess of the input
headword: Finite table misses inputs
author: mishka
status: asserted
tags: [philosophy-of-mind, functionalism, computability]
uses_concept: [concept-lookup-table-mind]
style: encyclopedia
created: 2026-06-04
---

A [lookup table](../concepts/lookup-table-mind.md) stores a finite set of input→output pairs, but the
space of possible finite inputs — token strings longer or more numerous than any the table
anticipates — has no upper bound. So for any finite table there exist finite inputs that are not
among its keys. On such an input the table has no appropriate stored response; at most it can emit
an output by *discarding the part of the input that exceeds its keys*, treating a longer or novel
input as one of the finitely many it already knows.

### Scope

This is a near-combinatorial point about *finite* stored maps against an unbounded input space. It
does not assert that minds are infinite, nor that no large table is practically adequate — only
that, for any fixed finite table, some inputs fall outside it. It is silent on whether those
uncovered inputs are ones a real, finite-lifetime mind would ever actually receive; that contested
bridge is [whether a mind handles unbounded inputs](mind-handles-unbounded-inputs.md). As stated
the claim is denied by essentially no one: the dispute lies not here but at the asymmetry premise —
whether a mind does better than the table on the uncovered inputs.

Distinct from [the claim that a finite table can match a mind's full
behavioural profile](lookup-table-possible.md): this is the combinatorial fact that motivates denying that one, identifying
the inputs on which a finite table must fall short.

### In plain terms

A stored answer-table only holds finitely many input→answer pairs, but the inputs you could throw at
it (ever-longer strings of words, say) never run out. So however big the table, there are always
inputs it has no entry for — and all it can do then is ignore the unfamiliar part and treat a
brand-new input as one it already knows. (This much is barely deniable; the real fight is over
whether those uncovered inputs are ones a real, finite-lifetime mind would ever actually meet.)

### See also

- [mind-handles-unbounded-inputs](mind-handles-unbounded-inputs.md) — the contested bridge: whether a mind actually outdoes
  the table on the uncovered inputs.
- [lookup-table-possible](lookup-table-possible.md) — the separability claim this combinatorial fact is marshalled
  against.
- [lookup-table-mind](../concepts/lookup-table-mind.md) — the finite stored map this claim describes the limits of.

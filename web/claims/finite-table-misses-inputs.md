---
id: claim-finite-table-misses-inputs
type: claim
title: For any finite lookup table there are finite inputs outside its stored domain, to which it can only "respond" by ignoring the excess of the input
headword: Finite table misses inputs
author: mishka
status: asserted
tags: [philosophy-of-mind, functionalism, computability]
uses_concept: [concept-lookup-table-mind]
style: legacy
created: 2026-06-04
---

gloss: A lookup table stores a finite set of input→output pairs. The space of possible finite
inputs (e.g. token strings, longer or more numerous than any the table anticipates) is unbounded.
So for any finite table there exist finite inputs not among its keys; on such an input the table
has no appropriate stored response, and can at most emit an output by *discarding the part of the
input that exceeds its keys* — i.e. by treating a longer/novel input as one of the finitely many it
already knows.

scope: A near-combinatorial point about *finite* stored maps versus an unbounded input space. It
does NOT assert that minds are infinite, nor that no large table is practically adequate — only
that, for any fixed finite table, some inputs fall outside it. It is silent on whether those
uncovered inputs are ones a real, finite-lifetime mind would ever actually receive (that is the
contested bridge — see [mind-handles-unbounded-inputs](mind-handles-unbounded-inputs.md)).

who would deny it: essentially no one as stated; the dispute is not here but at the asymmetry
premise (whether a mind does better on the uncovered inputs).

Distinct from [lookup-table-possible](lookup-table-possible.md) (which asserts a finite table CAN match a mind's full
behavioural profile): this claim is the combinatorial fact that motivates denying that one — it
identifies the inputs on which a finite table must fall short.

### In plain terms

A stored answer-table only holds finitely many input→answer pairs, but the inputs you could throw at
it (ever-longer strings of words, say) never run out. So however big the table, there are always
inputs it has no entry for — and all it can do then is ignore the unfamiliar part and treat a
brand-new input as one it already knows. (This much is barely deniable; the real fight is over
whether those uncovered inputs are ones a real, finite-lifetime mind would ever actually meet.)

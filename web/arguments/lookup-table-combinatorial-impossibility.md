---
id: argument-lookup-table-combinatorial-impossibility
type: argument
title: The combinatorial-impossibility reply — a finite lookup table cannot match an open-ended mind's behaviour
author: mishka
status: asserted
tags: [philosophy-of-mind, functionalism, computability]
premise: [claim-finite-table-misses-inputs, claim-mind-handles-unbounded-inputs]
concludes: claim-lookup-table-combinatorially-inadequate
attacks: [claim-lookup-table-possible, argument-lookup-table-objection]
responds_to: [argument-lookup-table-objection]
uses_concept: [concept-lookup-table-mind]
created: 2026-06-04
---

inference form: deductive at its core — a diagonal / cardinality argument (a fixed finite domain
cannot cover an unbounded input space) — turning on one defeasible empirical premise (2).

1. ([finite-table-misses-inputs](../claims/finite-table-misses-inputs.md)) For any finite lookup table there exist finite inputs outside
   its stored domain; to such an input it can at most respond by ignoring the part of the input that
   exceeds its keys.
2. ([mind-handles-unbounded-inputs](../claims/mind-handles-unbounded-inputs.md)) A genuine mind responds appropriately to such inputs rather
   than discarding their excess.
∴ ([lookup-table-combinatorially-inadequate](../claims/lookup-table-combinatorially-inadequate.md)) For every finite table there is an input on which
   it diverges from the mind; so no finite table reproduces a mind's full behavioural profile.

bearing on the target: this `responds_to` and `attacks` [lookup-table-objection](lookup-table-objection.md) by denying
its premise (1), [lookup-table-possible](../claims/lookup-table-possible.md) — the assumption that a finite table *can* match the
whole behavioural profile. If a finite table cannot even produce the behaviour, the blockhead is not
a case of "behaviour without mind"; it is a system that fails to match the behaviour. Dialectically
this favours the substrate-independence side: it blunts the lookup-table objection to
[behavioral-parity](behavioral-parity.md) at its first premise. (It leaves untouched the Chinese-Nation objection, [china-nation-absent-qualia](china-nation-absent-qualia.md),
which has the organisation and so matches more than I/O.)

weakest premise: (2), [mind-handles-unbounded-inputs](../claims/mind-handles-unbounded-inputs.md). Block's "Blockhead" ([block](../sources/block.md)) is
built to escape exactly this: stipulate a table covering all inputs up to a length exceeding any the
subject meets in a lifetime, and note that a finite mind also truncates inputs past its own capacity
— so the divergence asserted in premise (2) may never arise within the bounded domain that matters.
The conclusion is therefore filed `contested`; that escape is now [bounded-table-rejoinder](bounded-table-rejoinder.md),
itself answered on physical grounds by [lookup-table-physical-impossibility](lookup-table-physical-impossibility.md) (the bounded table
cannot be built) and on kind grounds by [storage-not-stable-kind](storage-not-stable-kind.md) (a realisable table is not
"mere storage").

Distinct from [lookup-table-objection](lookup-table-objection.md) (mishka): that argument *uses* the lookup table to
attack behavioural sufficiency (behaviour ⇒ mind); this one attacks *that* argument, denying the
lookup table reproduces the behaviour at all. Opposite dialectical direction, different conclusion.
Distinct from [organisational-grain-dissolves-dilemma](organisational-grain-dissolves-dilemma.md), which excludes the blockhead
by its lack of internal *organisation*; this excludes it by its inability to match the *I/O profile*
over an unbounded input space — a different ground of exclusion.

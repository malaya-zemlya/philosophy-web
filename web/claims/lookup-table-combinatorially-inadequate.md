---
id: claim-lookup-table-combinatorially-inadequate
type: claim
title: No finite lookup table can reproduce the full behavioural profile of a genuine mind
headword: Combinatorially inadequate table
author: mishka
status: contested
tags: [philosophy-of-mind, functionalism, computability]
uses_concept: [concept-lookup-table-mind]
style: encyclopedia
created: 2026-06-04
---

A *finite lookup table* — a fixed list pairing each anticipated input with a stored response —
cannot match everything a real mind does. Because any such table omits some possible inputs while
a mind still answers those inputs sensibly, for every finite table there is an input on which the
two diverge. The table is therefore *combinatorially* inadequate, not merely impractically large:
its shortfall is one of range, not size.

The reasoning rests on two facts. Any finite table misses some inputs
([finite-table-misses-inputs](finite-table-misses-inputs.md)), and a genuine mind responds appropriately to those very
inputs rather than discarding their excess ([mind-handles-unbounded-inputs](mind-handles-unbounded-inputs.md)). Hence no
finite table reproduces a mind's *full* behavioural profile.

### Scope

The claim concerns *pure finite lookup* only. It does not deny that some other, non-table system
might match a mind, nor that a table could match a mind over a bounded fragment of its inputs —
only that finite lookup cannot match the whole open-ended profile. It is effectively the negation
of [the claim that a finite table can reproduce the profile](lookup-table-possible.md).

### Why it is contested

The disputed step is the second supporting claim, [mind-handles-unbounded-inputs](mind-handles-unbounded-inputs.md). On
Block's lifetime-bounded construction ([block](../sources/block.md)) the table need only cover inputs up to a
length the subject will actually receive, and a finite mind would itself truncate longer inputs —
so the asserted divergence may never arise in the domain that matters. The attacking move is
[the bounded-table rejoinder](../arguments/bounded-table-rejoinder.md) ([block](../sources/block.md)); this claim's
`contested` status records that dispute. The bounded table is in turn answered by
[the cosmic-size reply](../arguments/lookup-table-physical-impossibility.md) (it cannot be built) and by
[storage-not-stable-kind](../arguments/storage-not-stable-kind.md) (a realisable table is not "mere storage").

A defender of Blockhead, that is, of pure input–output functionalism, would deny the claim. Note,
though, that it *helps* organisational-role functionalism: if a lookup table cannot even match
behaviour, then [the lookup-table objection](../arguments/lookup-table-objection.md) fails at its first
premise.

It should be distinguished from [lookup-table-lacks-mind](lookup-table-lacks-mind.md), which grants the table the
behaviour but denies it a mind; the present, stronger and prior claim denies the table even has
the behaviour.

### In plain terms

No finite stored answer-table, however enormous, can match everything a real mind does — because a
mind handles an open-ended stream of fresh inputs, and any finite table eventually hits one it has
no entry for, at which point the two part ways. So the cheat-sheet is not merely impractically
big; it cannot reproduce the *whole* range of a mind's behaviour at all. (Disputed: maybe you only
ever need to cover the inputs of a single lifetime — the bounded-table reply,
[bounded-table-rejoinder](../arguments/bounded-table-rejoinder.md).)

### See also

- [lookup-table-mind](../concepts/lookup-table-mind.md) — the stored-answer machine this claim says falls short.
- [lookup-table-possible](lookup-table-possible.md) — the claim this one is effectively the negation of.
- [finite-table-misses-inputs](finite-table-misses-inputs.md) and [mind-handles-unbounded-inputs](mind-handles-unbounded-inputs.md) — the two facts
  the verdict rests on.
- [lookup-table-lacks-mind](lookup-table-lacks-mind.md) — the weaker sibling, granting behaviour but denying mind.
- [bounded-table-rejoinder](../arguments/bounded-table-rejoinder.md) — Block's reply at the contested premise.

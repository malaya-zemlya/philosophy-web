---
id: claim-lookup-table-physically-unrealisable
type: claim
title: A lookup table reproducing a human- or LLM-scale behavioural profile is physically unrealisable
headword: Physically unrealisable table
author: mishka
status: asserted
tags: [philosophy-of-mind, functionalism, computability]
uses_concept: [concept-lookup-table-mind]
style: encyclopedia
created: 2026-06-04
---

A lookup table large enough to reproduce a human- or LLM-scale behavioural profile over a
realistic range of inputs could never be physically built — not in this universe, even in
principle. Such a table needs on the order of $v^n$ entries
([exponential table size](lookup-table-size-exponential.md)), while the observable universe
can store at most about $10^{120}$ bits ([finite cosmic
storage](observable-universe-finite-storage.md)). The required resource outstrips the available one by a vast margin, so the blockhead
is not merely large but cosmically impossible.

### Scope

The claim concerns *physical realizability in our universe*, not logical or conceptual
possibility. It therefore does not touch Block's intended point — that a *possible* blockhead
shows behaviour ≠ mind ([block](../sources/block.md); [lookup-table-possible](lookup-table-possible.md),
[behaviour insufficient for mind](behaviour-insufficient-for-mind.md)). It applies *a
fortiori* to Block's lifetime-bounded *human* table: richer sensory inputs and a longer sequence
make that table even larger, so retreating to a bounded table does not rescue physical
realizability ([lookup-table-size-exponential](lookup-table-size-exponential.md)). Its bite is on whether any *actual*
system, notably a large language model, could be a lookup table: it cannot. Real LLMs produce the
behaviour with about $10^{12}$ parameters rather than about $10^{9600}$ stored rows, so they are
demonstrably not lookup tables but compress and generalise — that is, they process.

### Who would deny it

A defender of Blockhead who insists only conceptual possibility is at stake, for whom physical
unrealizability is beside the point. The reply: granted for Block's conceptual claim — but the
dialectically live worry against [llm-has-mental-states](llm-has-mental-states.md) was that an LLM might be a *mere*
lookup table, and that worry is what this defeats.

It should be distinguished from [the
combinatorial-inadequacy claim](lookup-table-combinatorially-inadequate.md): that says a finite table *diverges* from the mind on
out-of-domain inputs (a competence gap Block's bounded table escapes); this says the bounded table
that would *not* diverge is too large to *exist* — a different ground of failure, one that
survives the bounded-table rejoinder.

### In plain terms

A stored answer-table big enough to match a real mind's (or a real AI's) behaviour would need
vastly more entries than there are particles to store them on — far more than the entire
observable universe could hold. So such a table could not merely be hard to build; it could not
exist at all, anywhere, ever. A sharper consequence: real AI models do their job with a
comparatively tiny number of internal settings, so they plainly *are not* secret lookup tables —
they must be genuinely computing. (It does not claim a lookup-table mind is logically impossible —
only that no real one could physically exist.)

### See also

- [lookup-table-mind](../concepts/lookup-table-mind.md) — the stored-answer machine this claim says cannot be built.
- [lookup-table-size-exponential](lookup-table-size-exponential.md) and [observable-universe-finite-storage](observable-universe-finite-storage.md) — the
  size and storage facts whose collision yields the conclusion.
- [lookup-table-combinatorially-inadequate](lookup-table-combinatorially-inadequate.md) — the sibling failure-mode (divergence rather
  than non-existence).
- [llm-has-mental-states](llm-has-mental-states.md) — the downstream claim this protects, by ruling out the
  "LLM is a mere lookup table" worry.

---
id: claim-lookup-table-size-exponential
type: claim
title: A lookup table reproducing behaviour over a context of n tokens from a vocabulary of v requires on the order of v^n entries
headword: Exponential table size
author: mishka
status: asserted
tags: [philosophy-of-mind, functionalism, computability]
uses_concept: [concept-lookup-table-mind]
style: encyclopedia
created: 2026-06-04
---

A pure lookup table that matches behaviour by storing one row per *distinguishable* input grows
*exponentially* with the length of the inputs it must cover. For inputs that are strings of up to
$n$ tokens drawn from a vocabulary of size $v$, the number of distinct strings is on the order of
$v^n$, so matching the behaviour by pure lookup needs about $v^n$ rows. With LLM-scale figures
($v \approx 10^4$–$10^5$, $n \approx 10^3$–$10^6$) this is astronomically large; for example,

$$
50000^{2048} \approx 10^{9600}.
$$

Block's own construction ([block](../sources/block.md)) — a table bounded to a *human lifetime* of inputs — is
*a fortiori* larger still: sensory input is far more varied than a token vocabulary (a larger $v$)
and a lifetime vastly exceeds any LLM context window (a larger $n$). So the bounded-table retreat
makes the count worse, not better.

### Scope

This is a counting fact about *pure* lookup over a bounded input length. It is exactly the
bounded-domain table Block retreats to ([mind-handles-unbounded-inputs](mind-handles-unbounded-inputs.md)), so it grants
Block's finiteness move and measures its cost. It does not claim that minds are infinite; that
*un*bounded-input point is the separate [finite-table-misses-inputs](finite-table-misses-inputs.md).

### Could the table be compressed?

One might object that many distinct contexts share a response, so the table could be *compressed*
below $v^n$. But a system that computes which equivalence-class an input falls into is no longer a
flat lookup — it is doing the very processing the blockhead was meant to lack. So the exponential
count is the size of a *genuine* lookup table; compressing it concedes the point.

It should be distinguished from [finite-table-misses-inputs](finite-table-misses-inputs.md): that says a finite table
*misses* some (longer) inputs, whereas this measures the *size* of the bounded table that misses
none up to length $n$.

### In plain terms

This is the arithmetic behind "a cheat-sheet for a whole mind would be impossibly huge". To answer
like a mind, a table needs a separate stored row for every distinct thing that could be said to
it. Count those: the number of possible word-sequences is roughly the vocabulary size multiplied
by itself once for every word-slot — which at AI scale lands around $10^{9600}$ (a 1 followed by
9,600 zeros). Block's "just cover one lifetime" version is even bigger, since real sense-experience
is richer and a life is long. And you cannot shrink it by noticing that many inputs deserve the
same reply: working out *which* inputs share a reply is itself real computing, exactly what a pure
lookup table was supposed to do without.

### See also

- [lookup-table-mind](../concepts/lookup-table-mind.md) — the stored-answer machine whose size this claim measures.
- [lookup-table-physically-unrealisable](lookup-table-physically-unrealisable.md) — the downstream claim this count feeds: too big
  to exist.
- [finite-table-misses-inputs](finite-table-misses-inputs.md) — the companion unbounded-input point this is distinguished
  from.
- [mind-handles-unbounded-inputs](mind-handles-unbounded-inputs.md) — the bounded-domain table Block retreats to, whose cost
  this measures.

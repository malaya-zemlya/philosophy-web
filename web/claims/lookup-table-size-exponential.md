---
id: claim-lookup-table-size-exponential
type: claim
title: A lookup table reproducing behaviour over a context of n tokens from a vocabulary of v requires on the order of v^n entries
author: mishka
status: asserted
tags: [philosophy-of-mind, functionalism, computability]
uses_concept: [concept-lookup-table-mind]
created: 2026-06-04
---

gloss: a flat query→answer table must store one row per *distinguishable* input. For inputs that are
strings of up to `n` tokens drawn from a vocabulary of size `v`, the number of distinct strings is
on the order of `v^n`; matching the behaviour by pure lookup therefore needs ~`v^n` rows. With
LLM-scale figures (`v` ≈ 10^4–10^5, `n` ≈ 10^3–10^6) this is astronomically large, e.g.
`50000^2048 ≈ 10^9600`. Block's own construction — a table bounded to a *human lifetime* of inputs —
is a fortiori larger still: sensory input is far more varied than a token vocabulary (larger `v`)
and a lifetime vastly exceeds any LLM context window (larger `n`). So the bounded-table retreat makes
the count worse, not better.

scope: a counting fact about *pure* lookup over a bounded input length. It is exactly the
bounded-domain table Block retreats to ([mind-handles-unbounded-inputs](mind-handles-unbounded-inputs.md)), so it grants Block's
finiteness move and measures its cost. It does NOT claim minds are infinite (cf.
[finite-table-misses-inputs](finite-table-misses-inputs.md), which is the *un*bounded-input point).

who would deny it: one might object that many distinct contexts share a response, so the table could
be *compressed* below `v^n`. But a system that computes which equivalence-class an input falls into
is no longer a flat lookup — it is doing the very processing the blockhead was meant to lack. So the
exponential count is the size of a *genuine* lookup table; compressing it concedes the point.

Distinct from [finite-table-misses-inputs](finite-table-misses-inputs.md): that says a finite table *misses* some (longer)
inputs; this measures the *size* of the bounded table that misses none up to length `n`.

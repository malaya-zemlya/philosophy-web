---
id: claim-first-token-update-is-relational
type: claim
title: The token-specific part of a language model's update on first encountering a token is wholly relational
headword: Relational first-token update
author: mishka
status: asserted
tags: [ai, philosophy-of-mind, machine-learning]
uses_concept: [concept-llmary]
style: encyclopedia
created: 2026-11-20
---

When a language model trained by next-token prediction meets a token for the first time, what it
learns that is specific to that token consists of exactly two things: *in what context the token
occurs*, and *what follows when the token is in context*. Both are relations to other tokens. No
part of the update concerns the token taken by itself.

### The mechanics

A token that appears at some position in the training stream plays two roles at once. It is first
the *target* the model must predict from everything that came before it. The prediction error at that
position adjusts the token's output representation (its row in the output layer) toward the internal
state the preceding text put the model in, so the model learns what sort of text leads up to the
token. The token then sits *in the context* for every later prediction, and the errors on the tokens
that follow flow back into its input embedding, so the model learns what difference its presence
makes to what comes next. In models whose input and output embeddings are tied, both lessons are
written into one and the same vector.

Before the encounter, that vector was an essentially arbitrary initialisation. Afterwards it has a
place among the model's expectations, defined by the token's typical antecedents and consequents.

### Scope

The claim is about the *token-specific* parameters. The rest of the network also changes on the same
step, but those changes are shared with every other token and so are not what the model learns about
this one. The claim is a description of how gradient-based training works. It says nothing, by
itself, about human experience; carrying it over to Mary the colour scientist is the separate step
taken in [llmary-relational-diagnosis](../arguments/llmary-relational-diagnosis.md).

### In plain terms

When an AI language model sees a word-piece for the very first time, it picks up two things about it:
what kind of text tends to come *before* it, and what tends to come *after* it. That is all it learns
about that particular word-piece. Its "knowledge" of the token is entirely a matter of how the token
fits in with other tokens.

---
id: claim-description-cannot-confer-token-production
type: claim
title: Description alone cannot give a language model the ability to produce a token it has never encountered
headword: Unproducible described token
author: mishka
status: asserted
tags: [ai, machine-learning, philosophy-of-mind]
uses_concept: [concept-llmary, concept-zero-shot-few-shot-learning]
created: 2026-11-22
style: encyclopedia
---

However much a language model has read about a token, it cannot come to *output* that token
unprompted unless the token itself has occurred in its training. A model emits a token when its
internal state lines up with that token's row in the output layer, and that row is pulled toward the
states that precede the token only when the token is an actual prediction target. Text that merely
mentions the token never makes it one. The softmax in fact pushes the row of every token that is not
the target slightly *down* at each training step, so a never-seen token's row is trained only toward
improbability.

The claim is limited in two ways. It concerns unprompted production. When the token is present in
the context, a model may still *copy* it, because copying draws on the input side rather than the
untrained output row. It also leaves recognition open, which description can partly supply
([description-binds-token-only-relationally](description-binds-token-only-relationally.md)).

In the terms of [zero-shot-few-shot-learning](../concepts/zero-shot-few-shot-learning.md), the claim holds in both regimes. Training on
descriptions never trains the token's output row, and a description given in a prompt at inference time
cannot train anything at all, since inference leaves the weights fixed.

The resulting asymmetry, that description can support recognising the token in context but not
producing it, parallels the abilities David Lewis took Mary the colour scientist to gain on release
([lewis-1988](../sources/lewis-1988.md)). Description could let Mary recognise red by its context, as when she is not
fooled by a blue banana ([dennett-1991](../sources/dennett-1991.md)), but not imagine red.

### In plain terms

An AI can read everything about a word-piece without ever being able to say it on its own. The part of
the AI that "speaks" a word-piece is trained only by actually seeing that word-piece used, never by
reading about it. It is like knowing a great deal about a song you have never heard: you might
recognise it if someone played it, but you could not hum it.

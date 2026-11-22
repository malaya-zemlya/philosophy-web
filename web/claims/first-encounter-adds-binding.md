---
id: claim-first-encounter-adds-binding
type: claim
title: What a language model's first encounter with a token adds beyond any description is the binding of the token's relational role to the token's own representation
headword: Binding gained on first encounter
author: mishka
status: asserted
tags: [ai, machine-learning, philosophy-of-mind]
uses_concept: [concept-llmary, concept-zero-shot-few-shot-learning]
created: 2026-11-22
style: encyclopedia
---

When a language model that has read everything about a token finally processes the token itself, the
new element is not a further relational fact, since every such fact could have been described in
advance. It is that the token's own embedding and output row come to *carry* its relational role. Before
the encounter, what the model knows about the token sits in other parameters and can be linked to the
token only on the spot, through context. Afterwards the role is written into the token's own
representation, so the model can recognise the token anywhere and produce it unprompted.

The encounter in question is a training-time one, the one-shot case of training-time learning
distinguished in [zero-shot-few-shot-learning](../concepts/zero-shot-few-shot-learning.md). An encounter at inference time would not
produce the binding: a fixed model meeting the token in its prompt can relate it to its neighbours on
the spot, but its weights do not change, so nothing is written into the token's own representation and
the gain is lost with the prompt.

The claim refines [first-token-update-is-relational](first-token-update-is-relational.md) rather than contradicting it. That claim
says *what* the token-specific update contains; this one says what is new about it, given that its
content was already describable. It is distinct from [mary-gains-relational-placement](mary-gains-relational-placement.md), which
concerns Mary rather than the model, and it is reached in [llmary-binding](../arguments/llmary-binding.md).

### In plain terms

Everything an AI could learn about a new word-piece by meeting it could also, in principle, be told to
it in advance. What meeting it actually adds is that the knowledge gets filed *under the word-piece
itself*, instead of being something the AI has to work out from the surrounding text each time.

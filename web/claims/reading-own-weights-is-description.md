---
id: claim-reading-own-weights-is-description
type: claim
title: Reading its own weights as data gives a language model only a description of itself, which cannot supply the binding a first encounter with a token provides
headword: Self-reading as description
author: mishka
status: asserted
tags: [ai, machine-learning, philosophy-of-mind, knowledge-argument]
uses_concept: [concept-self-access-kinds, concept-llmary]
created: 2026-11-22
style: encyclopedia
---

When a language model is given its own weights to read, for instance the row of numbers that
represents a token it has never processed, it receives a description of itself like any other text.
Reading that row does not change it, and the model cannot compare the numbers it has read with the
activation the token will produce when it arrives, since it has no access to its own activations as
objects. Reading therefore leaves the model where any description leaves it: knowing about the token,
without the token's own representation carrying the token's role
([first-encounter-adds-binding](first-encounter-adds-binding.md)).

The same holds for simulation, the use of such self-knowledge to calculate what the network would do
on meeting the token, including the exact training update that would follow. Calculating an update is
not undergoing it. Both are among the kinds of self-access distinguished in
[self-access-kinds](../concepts/self-access-kinds.md), and both differ from writing one's own weights, the case taken up in
[write-access-installs-binding](write-access-installs-binding.md).

### In plain terms

An AI that reads a printout of its own internal numbers learns facts about itself, the way you might
read your own brain scan. That does not change the numbers. Even working out exactly how the numbers
would change on meeting a new word-piece is only a calculation; the change itself has not happened.

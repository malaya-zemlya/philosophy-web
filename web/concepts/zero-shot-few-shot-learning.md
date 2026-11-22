---
id: concept-zero-shot-few-shot-learning
type: concept
title: Zero-shot and few-shot learning
headword: Zero-shot and few-shot learning
author: generic
status: asserted
tags: [ai, machine-learning, language-models]
created: 2026-11-22
style: encyclopedia
---

*Zero-shot* and *few-shot learning* name two ways a learning system can come to handle something new.
In zero-shot learning it has only a *description* of the new item or task and no example of it. In
few-shot learning it is also given a small number of *examples*, usually between one and a few dozen.
The two terms are defined against each other, and the contrast between them, learning from what is
said about a thing versus learning from instances of the thing, is the reason they matter outside
machine learning.

### In language models

The terms became standard for language models with the GPT-3 paper ([brown-2020](../sources/brown-2020.md)). There
they describe what a trained model can do inside a single prompt. A zero-shot prompt states the task
("Translate into French: cheese"). A one-shot or few-shot prompt first shows worked examples ("sea
otter → loutre de mer; peppermint → menthe poivrée; cheese →") and lets the model continue the
pattern. The striking finding was that large models improve markedly from a few examples placed in
the prompt, although nothing about them is retrained.

### Two distinctions, not one

Two separate contrasts are often run together under these names, and they should be kept apart.

The first is the contrast between **description and example**: whether the system meets the new item
only as something talked about or also as something actually occurring. This is the contrast the
names themselves mark.

The second is the contrast between **learning in context and learning in the weights**. In the GPT-3
sense, both zero-shot and few-shot learning happen in context: the model's parameters stay fixed and
whatever it "learns" lasts only as long as the prompt. Ordinary training, by contrast, changes the
weights permanently through gradient descent. Elsewhere in machine learning, "zero-shot" is used more
broadly for any generalisation to a class never seen in training, for instance recognising a zebra
from the description "a horse with black and white stripes."

The two contrasts cross. A model can learn from examples in its weights (ordinary training), from
examples in context (few-shot prompting), or from a description in context (zero-shot prompting), and
it can absorb descriptions into its weights by being trained on text about a thing it has never met.
That last combination is the situation of [llmary](llmary.md) before its first encounter with the
token it has only read about.

### Why it matters philosophically

The description/example contrast is a machine-learning cousin of the gap that drives the
[knowledge-argument](knowledge-argument.md): Mary knows everything that can be *said* about colour but has never
*had* a colour experience. Asking how far zero-shot learning can go is a precise, testable version of
asking how far description can substitute for encounter. What description alone can and cannot give a
model about a never-seen token is set out in [description-binds-token-only-relationally](../claims/description-binds-token-only-relationally.md) and
[description-cannot-confer-token-production](../claims/description-cannot-confer-token-production.md).

### In plain terms

"Zero-shot" means figuring something out from instructions or a description alone, with no examples.
"Few-shot" means you also get to see a few examples first. A child told "a zebra is a striped horse"
and then recognising one at the zoo is learning zero-shot; a child shown three pictures of zebras is
learning few-shot. AI chatbots can do both inside a single conversation without being retrained,
which is a different thing from the slow, permanent learning they undergo when they are built.

### See also

- [llmary-binding](../arguments/llmary-binding.md) — uses the limits of zero-shot learning to say what a first encounter
  adds beyond description.

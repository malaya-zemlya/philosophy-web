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

### Two distinctions, four regimes

Two separate contrasts are often run together under these names, and they should be kept apart.

The first is the contrast between **description and example**: whether the system meets the new item
only as something talked about or also as something actually occurring. This is the contrast the
names themselves mark.

The second is the contrast between **learning at training time and learning at inference time**.
Training changes the model's weights through gradient descent, and what is learned persists. Inference
leaves the weights fixed: whatever the model "learns" from its prompt is carried in its internal
activations and lasts only as long as the prompt does. The GPT-3 sense of the terms is the
inference-time one. Elsewhere in machine learning, "zero-shot" more often means a training-time
achievement: generalising to a class absent from the training data, as in recognising a zebra from the
description "a horse with black and white stripes."

The two contrasts cross, giving four regimes:

- **Training-time zero-shot**: the model is trained on text *about* an item it never meets, so that
  what it knows of the item is stored in parameters shared with everything else. This is the
  situation of [llmary](llmary.md) before its first encounter with the token it has only read about.
- **Training-time few-shot**: the item itself occurs in the training data a handful of times, and
  each occurrence adjusts the weights, including the item's own parameters. LLMary's first encounter
  is the one-shot case.
- **Inference-time zero-shot**: a fixed model is told about an item or task in its prompt and must
  act on the description at once.
- **Inference-time few-shot**: a fixed model is shown examples in its prompt and continues the
  pattern.

### Different mechanisms, different dynamics

All four regimes are of interest, but they need not work the same way, and a result established for
one should not be assumed to carry over to another. The differences are of three kinds.

*Mechanism.* Training-time learning is gradient descent: each example nudges the weights in the
direction that would have reduced the error on it. Inference-time learning is carried out by the
fixed network itself, chiefly by attention, which lets later positions read from and copy patterns
found at earlier ones. Whether, and how closely, this in-context process imitates gradient descent is
an open research question.

*Dynamics.* At training time a single example usually moves the weights only a little, so rare items
tend to be learned poorly and many exposures may be needed. In context, one or two examples can be
enough for the model to pick up a pattern, but the gain vanishes with the prompt and is bounded by
the length of the context window.

*What can be reached.* Training can change any parameter, including an item's own embedding. Inference
can only use the representations the network already has. A token whose embedding was never trained
remains, during inference, an essentially untrained vector, so in-context learning can attach meaning
to it only through its position among other tokens, never by improving the vector itself.

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

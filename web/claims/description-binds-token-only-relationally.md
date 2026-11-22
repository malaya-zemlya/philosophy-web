---
id: claim-description-binds-token-only-relationally
type: claim
title: A description can attach a language model's knowledge to a never-seen token only through relational cues present in the context, not through the token's intrinsic properties
headword: Relational binding of described tokens
author: mishka
status: asserted
tags: [ai, machine-learning, philosophy-of-mind]
uses_concept: [concept-llmary, concept-zero-shot-few-shot-learning]
created: 2026-11-22
style: encyclopedia
---

A language model that has only read about a token it has never processed can apply what it read to
that token, when it finally appears, only if the description picks the token out by its *relations*
to the surrounding text, and only when that surrounding text is actually present. A description of the
token's *intrinsic* features cannot be used to identify it at all.

The reason is that a model never sees token numbers. It sees each input token only as that token's
embedding vector, and a never-seen token's vector is an essentially untrained initialisation, which
nothing in a description can reach. A relational description works because it can be checked against
the context. If the model has read that "the new token appears after three *Shazam*s in a row," then on
meeting "Shazam Shazam Shazam X" it can infer that X is the token described. An intrinsic description
such as "it is token number 123" or "its embedding is [0.12, −0.40, …]" gives the model nothing to
check, because it cannot compare its own input vector with numbers written out as text.

The limit shows most clearly with several unknown tokens. With a single one, the model might pick it
out by elimination, since untrained embeddings are anomalous: the glitch tokens found in GPT models
cluster near the centre of the embedding space ([rumbelow-watkins-2023](../sources/rumbelow-watkins-2023.md)). Several untrained
tokens, however, look nearly alike from the inside. They can be told apart only when each occurs in a
context its description distinctively specifies. Outside such a context, each is anonymous.

The claim concerns identification by description, not production; that description cannot make a
model *emit* such a token is the separate [description-cannot-confer-token-production](description-cannot-confer-token-production.md). It
complements [first-token-update-is-relational](first-token-update-is-relational.md), which says what the encounter itself teaches.

The claim spans two of the regimes distinguished in [zero-shot-few-shot-learning](../concepts/zero-shot-few-shot-learning.md). The
description is absorbed at training time, as training-time zero-shot learning, while the identification
happens at inference time, in context, when the token finally appears in a prompt. The same limit holds
when the description itself is given in the prompt rather than in training, because either way the
token's own vector carries nothing the description could latch onto.

### In plain terms

An AI that has only read about a word-piece it has never actually seen can recognise it later only by
where it shows up, as in "it comes right after Shazam, Shazam, Shazam." Being told the word-piece's
catalogue number is useless, because the AI never sees catalogue numbers. And if several never-seen
word-pieces turn up, it cannot tell which is which unless each appears in the spot its description
promised.

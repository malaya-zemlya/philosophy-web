---
id: claim-surprise-predictable-yet-undergone
type: claim
title: Knowing in advance how great its surprise on first encountering an item will be does not prevent a learner from undergoing that surprise
headword: Predicted surprise
author: mishka
status: asserted
tags: [ai, machine-learning, philosophy-of-mind, knowledge-argument]
uses_concept: [concept-llmary, concept-self-access-kinds]
created: 2026-11-22
style: encyclopedia
---

Knowing that one will be surprised, and exactly how, does not stop the surprise from happening. A
language model that knows all about a token it has never processed can calculate how improbable it
will find the token when it first arrives, and hence how large its prediction error will be, and it
can calculate the direction in which its token-specific weights will then move. When the token arrives
it still assigns it almost no probability, still incurs that error, and still undergoes that update.

The two facts sit in different places. The model's knowledge of the coming surprise is held in its
shared parameters or in its context, as a description. The surprise itself is the prediction error of
its output representation of the token, and that representation is computed without consulting what
the model knows about it. The prediction cannot be fed into the very representation whose failure it
predicts, unless the model can write that representation directly
([write-access-installs-binding](write-access-installs-binding.md)). A familiar human analogue is the startle at a loud noise one
knows is coming, which knowledge reduces but does not abolish.

The claim settles a question George Graham and Terence Horgan leave open. They concede that their
version of Mary, "Mary Mary", could predict in advance that she would be surprised on release, but they
allow in a footnote that "auto-prediction of epistemic states like surprise" might present "logical
problems insofar as Mary Mary cannot both know that she will be surprised in a certain way and be
surprised in that way" ([graham-horgan-2000](../sources/graham-horgan-2000.md), p. 85 n. 7). The language-model case shows that
no such problem arises when the knowledge and the surprise are carried by different parts of one
system.

### In plain terms

An AI can know ahead of time that a new word-piece will catch it off guard, and by how much, and still
be caught off guard when it arrives. The knowing happens in one part of the system and the being
surprised in another, and the first cannot reach the second. It is a bit like knowing a balloon is
about to pop and jumping anyway.

---
id: argument-llmary-binding
type: argument
title: Because relational knowledge of a token is describable yet description can neither identify the token outside its context nor make it producible, what LLMary's first encounter adds is binding
headword: LLMary binding argument
author: mishka
status: asserted
pattern: best-explanation
tags: [philosophy-of-mind, consciousness, ai, thought-experiment]
premise: [claim-first-token-update-is-relational, claim-description-binds-token-only-relationally, claim-description-cannot-confer-token-production]
concludes: claim-first-encounter-adds-binding
responds_to: [argument-llmary-relational-diagnosis]
uses_concept: [concept-llmary, concept-zero-shot-few-shot-learning, concept-knowledge-argument]
created: 2026-11-22
style: encyclopedia
---

This argument presses a question that the [llmary-relational-diagnosis](llmary-relational-diagnosis.md) leaves open. If the
whole of what a language model learns on first meeting a token is relational, and relational facts
can be stated in words, then a sufficiently detailed description should have delivered the same
knowledge in advance. In the terms of [zero-shot-few-shot-learning](../concepts/zero-shot-few-shot-learning.md), training-time zero-shot
learning from description should match training-time learning from examples. The argument answers
that it does not, and locates the difference precisely. Both the description and the encounter it
concerns happen at training time; inference-time learning, which leaves the weights fixed, works by a
different mechanism and is not what the argument is about.

### The argument

The inference form is inference to the best explanation.

1. The token-specific part of a model's update on first encountering a token is wholly relational
   ([first-token-update-is-relational](../claims/first-token-update-is-relational.md)).
2. A description can attach the model's knowledge to a never-seen token only through relational cues
   present in the context, not through the token's intrinsic properties
   ([description-binds-token-only-relationally](../claims/description-binds-token-only-relationally.md)).
3. Description alone cannot give a model the ability to produce a token it has never encountered
   ([description-cannot-confer-token-production](../claims/description-cannot-confer-token-production.md)).
4. Therefore the best explanation of what the first encounter adds, given that its content was
   describable, is the binding of the token's relational role to the token's own representation
   ([first-encounter-adds-binding](../claims/first-encounter-adds-binding.md)).

Premises 2 and 3 show that a model taught only by description falls short in two definite ways. It can
apply its knowledge only where the context lets it locate the token, and it cannot produce the token at
all. The encounter removes both shortfalls at once, and premise 1 says it does so without supplying
any non-relational content. What remains to explain the change is a matter of *where* the relational
knowledge is stored, not of what it is.

### Bearing on Mary

Carried over by the same analogy the relational diagnosis uses, the result splits Mary's gain into
content and binding. Mary already knows, in her black-and-white room, everything relational about
red. What release adds is that her own colour state comes to carry that role, so that she can recognise
red in any setting and imagine it at will. The split matches the abilities Lewis attributes to her
([ability-hypothesis](ability-hypothesis.md); [lewis-1988](../sources/lewis-1988.md)), and it explains why recognising red by its context, as in Dennett's
blue-banana case ([dennett-1991](../sources/dennett-1991.md)), comes easier than imagining it.

The binding has the character of a demonstrative ("*this* is the one that follows three *Shazam*s"),
which brings the result close to the view that Mary acquires a new phenomenal concept of an old fact
([old-fact-new-guise](old-fact-new-guise.md)). The two agree that the novelty lies in how the knowledge is held,
not in a new fact. They differ in that the binding account offers a mechanism, the training of the
item's own representation, where the phenomenal-concept view posits a special kind of concept.

### The weakest premise

Premise 2 is the most exposed. It holds for current architectures, in which a model has no access to
its own token indices, but a model could be built that exposes them, and such a model might use an
intrinsic description to pick out a token it had never processed. The defender can reply that this
would only move the binding to a different place: the model would still need the index to be linked
to its own internal representation, which is again something description supplies only through the
encounter. The argument also inherits the critical question of every inference to the best
explanation, whether a rival explanation of the encounter's effect, such as a non-relational residue,
explains it as well.

### In plain terms

There is an earlier argument that an AI meeting a new word-piece learns only how it fits with other
word-pieces ([llmary-relational-diagnosis](llmary-relational-diagnosis.md)). This raises an objection: anything of that kind
could have been told to the AI in advance. This argument replies that being told falls short in two
ways. The AI can recognise the word-piece only when the surroundings give it away, and it can never say
the word-piece itself. Actually meeting the word-piece fixes both, by filing the knowledge under the
word-piece itself. Applied to Mary, this suggests she knew all the facts about red already and what
she gained on seeing it was having them attached to her own experience.

### See also

- [llmary](../concepts/llmary.md) — the thought experiment this argument extends.
- [llmary-token-encounter](llmary-token-encounter.md) — the neutral counterexample to the knowledge argument's
  inference, on which both LLMary arguments build.

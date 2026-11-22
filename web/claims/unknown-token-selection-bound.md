---
id: claim-unknown-token-selection-bound
type: claim
title: When several never-seen tokens are indistinguishable to a language model, description alone lets it at best split its prediction evenly among them, so its first-encounter surprise exceeds by at least log k what selecting the right token would allow
headword: Selection bound for unknown tokens
author: mishka
status: asserted
tags: [ai, machine-learning, philosophy-of-mind, knowledge-argument]
uses_concept: [concept-llmary, concept-zero-shot-few-shot-learning]
created: 2026-11-22
style: encyclopedia
---

Suppose a language model has *k* tokens in its vocabulary that it has never processed, and it has read
that one of them, token 123, follows a certain phrase. From the description it can work out what role
token 123 will play, and so what its representation *should* become once training on it takes place.
What it cannot work out is *which* of its untrained output rows belongs to token 123, because it bets on
next tokens only through those rows and they are alike to it. Each began as random noise, and training
on text that never contains them has pushed them all down in the same direction. Nothing in training on
descriptions ever rewards putting probability on row 123 rather than on another untrained row.

The best the model can then do is to give the class of unknown tokens whatever probability *p* the
description warrants and spread it evenly, so that token 123 receives at most *p*/*k*. Measured as
prediction error in nats, its surprise when the token arrives is then at least

$$-\log \frac{p}{k} = -\log p + \log k ,$$

larger by log *k* than it would be if the model could select the right token. The model can compute
this bound in advance, which sharpens [surprise-predictable-yet-undergone](surprise-predictable-yet-undergone.md), and no further
description can reduce it, since only selection can. With a single unknown token the problem
disappears, because putting probability on "the unknown token" then puts it on the right one; the case
of several shows the selection problem that elimination otherwise hides. Selection is the output-side
counterpart of the recognition problem in [description-binds-token-only-relationally](description-binds-token-only-relationally.md): one asks
which incoming vector is the token, the other which row to bet on.

The case has a limited analogue in Mary the colour scientist. A token's row is arbitrary, bearing no
structural relation to the token's role, whereas a human colour system is in large part innately
structured, so that where red will fall may be fixed in advance. To that extent Mary faces less of a
selection problem than the model does; how much less depends on which parts of her colour pathway are
fixed before experience ([mary-gain-depends-on-prewiring](mary-gain-depends-on-prewiring.md)).

### In plain terms

Imagine an AI with several word-pieces it has never seen, which all look the same to it. It has read
that one particular one will come after a certain phrase, and it even knows what that word-piece will
come to mean. But when the phrase appears it cannot tell which of the look-alike word-pieces to expect,
so the best it can do is spread its bet evenly across all of them. That guarantees a certain amount of
surprise, which it can calculate in advance and cannot reduce by reading anything more.

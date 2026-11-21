---
id: argument-llmary-relational-diagnosis
type: argument
title: LLMary's first-token update is wholly relational, so by analogy Mary's gain on first seeing red is wholly relational
headword: LLMary relational diagnosis
author: mishka
status: asserted
pattern: analogy
tags: [philosophy-of-mind, consciousness, ai, thought-experiment]
premise: [claim-first-token-update-is-relational, claim-mary-analogous-to-llmary]
concludes: claim-mary-gains-relational-placement
uses_concept: [concept-llmary, concept-knowledge-argument]
style: encyclopedia
created: 2026-11-20
---

This argument uses the [llmary](../concepts/llmary.md) thought experiment to give a *positive* answer to what
Mary the colour scientist gains on release. Where [llmary-token-encounter](llmary-token-encounter.md) only shows that
a complete-knowledge-yet-gain case can be wholly physical, this argument goes further and says what
the gain consists of. It reads the answer off the mechanics of language-model training, then carries
it over to Mary by analogy.

### The argument

The inference form is analogy.

1. The token-specific part of a language model's update on first encountering a token is wholly
   relational: the model learns in what context the token occurs and what follows when it is in
   context ([first-token-update-is-relational](../claims/first-token-update-is-relational.md)).
2. Mary's first sight of red is relevantly analogous to a language model's first encounter with a
   token ([mary-analogous-to-llmary](../claims/mary-analogous-to-llmary.md)).
3. Therefore what Mary gains on first seeing red is wholly relational knowledge of where the
   experience sits among her expectations: what brings it on and what it leads to
   ([mary-gains-relational-placement](../claims/mary-gains-relational-placement.md)).

The respects of similarity on which premise 2 rests are three. Both subjects have complete
descriptive knowledge beforehand. Neither has had the item itself occur in its own processing. Both
adjust their internal states when it finally does occur.

### Why the first premise is secure

Premise 1 is not a speculation about machines but a description of how next-token training works. A
first-seen token is the prediction target for the text before it, which shapes its output
representation, and it is part of the context for the text after it, which shapes its input
embedding. Nothing else in the update is specific to the token. The model's whole grasp of the token
is therefore its place among its neighbours.

### The weakest premise

Premise 2 is the weakest, and the analogy pattern's disanalogy question lands squarely on it. The
phenomenal realist points to one difference that matters: Mary undergoes an experience with a felt
character, while the model undergoes nothing it is like anything to undergo. If that difference is
real, Mary's gain may include acquaintance with the intrinsic character of red
([mary-gains-acquaintance](../claims/mary-gains-acquaintance.md)), something with no counterpart in the model's update.

The defender of the analogy can reply that the burden runs the other way. Everything Mary can *do*
with her new knowledge, from recognising red to predicting how orange will look, is accounted for by
its relational placement. An intrinsic residue that makes no difference to anything she expects or
does is a residue with no observable role, and positing it is the very point the knowledge argument
was meant to establish rather than assume. Whether this reply succeeds is the hard problem in
miniature.

### Relation to neighbouring moves

The conclusion is close to the [ability-hypothesis](ability-hypothesis.md): recognising, imagining and
remembering are just the context-and-consequence dispositions the relational reading describes. The
two differ in commitment. The ability hypothesis classifies the gain as non-factual know-how, while
the relational reading is neutral on that classification and supplies instead a mechanism for how the
gain arises. It also differs from [old-fact-new-guise](old-fact-new-guise.md), which locates the novelty in a new
mode of presentation of an old fact rather than in new relations the state enters into.

### In plain terms

An AI language model meeting a word-piece for the first time learns exactly two things about it: what
tends to come before it, and what tends to come after it. The argument says Mary seeing red for the
first time is the same kind of event, so she too learns exactly two things: what situations bring on
the experience of red, and what that experience leads to in her mind. That would explain why no book
could teach her, since the learning *is* her own mind adjusting to the experience actually happening.
The weak spot is the comparison itself: critics say Mary *feels* something when she sees red and the
AI feels nothing, so the two cases may differ in the one way that counts.

### See also

- [what-does-mary-learn](../questions/what-does-mary-learn.md) — the question this argument answers, through its conclusion.
- [knowledge-argument](../concepts/knowledge-argument.md) — Jackson's original thought experiment about Mary.

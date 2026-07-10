---
id: argument-llm-representations-reply
type: argument
title: The LLM-representations reply — actual text-trained models build human-aligned representations, pressing A3 empirically
headword: LLM-representations reply
author: mishka
status: asserted
pattern: best-explanation
tags: [ai, philosophy-of-mind, cognitive-science, semantics]
premise: [claim-llm-text-yields-human-aligned-representations]
attacks: [claim-syntax-insufficient-for-semantics]
supports: [argument-connectionist-reply]
uses_concept: [concept-chinese-room, concept-intrinsic-derived-intentionality]
style: encyclopedia
created: 2026-06-25
---

A contemporary objection to the [Chinese Room](../concepts/chinese-room.md) not available to Searle in 1980,
because it turns on findings about *actual* large language models. It is the empirical vindication of the
Churchlands' bet ([connectionist-reply](connectionist-reply.md)): where they argued *a priori* that the right network
might induce meaning, the evidence now suggests text-trained networks *do* induce internal representations
structurally aligned with human ones — pressing axiom A3 ([syntax-insufficient-for-semantics](../claims/syntax-insufficient-for-semantics.md)) with
data rather than intuition.

### The argument

The inference is **inductive / inference to the best explanation** from convergent empirical results.

1. ([llm-text-yields-human-aligned-representations](../claims/llm-text-yields-human-aligned-representations.md)) Models trained on text alone develop internal
   representations whose structure matches human representations — perceptual similarity geometry across six
   modalities ([marjieh-2024](../sources/marjieh-2024.md)) and unsupervised colour-space alignment ([kawakita-2024](../sources/kawakita-2024.md));
   induced world models of a domain, from the Othello board ([li-2022](../sources/li-2022.md), [yuan-2025](../sources/yuan-2025.md)) to
   *real-world* space and time ([gurnee-2023](../sources/gurnee-2023.md)); and, most directly, alignment with human *brain*
   activity for both concepts ([xu-2025](../sources/xu-2025.md)) and vision ([doerig-2025](../sources/doerig-2025.md)).
2. If pure symbol-manipulation could *never* yield semantic content, it should not reliably grow
   representations isomorphic to human meaning-structure; the best explanation of that reliable isomorphism
   is that the statistics of language encode, and the network recovers, genuine semantic structure.

∴ A3 is false on its strongest reading: syntax is *not* inert with respect to semantics — formal training
on text is, in fact, sufficient to *constitute* human-aligned semantic representation. This `attacks`
[syntax-insufficient-for-semantics](../claims/syntax-insufficient-for-semantics.md) and `supports` [connectionist-reply](connectionist-reply.md).

### The weakest point

The reply's reach is **bounded, and the boundary is exactly Searle's retreat line.** It establishes aligned
representational *structure*; Searle can grant all of it and re-press the
[depicting-versus-instancing](../claims/simulation-instances-formal-depicts-causal.md) distinction — structure
isomorphic to human meaning is still structure, a *depiction* of semantics, not the
[intrinsic](../concepts/intrinsic-derived-intentionality.md) intentionality or felt understanding the argument
targets. So the reply decisively undercuts the *strong* reading of A3 ("syntax can't even induce
semantic-relevant structure") while leaving the *deep* reading ("structure, however rich, is not original
aboutness or consciousness") untouched — which is why it is best seen as shifting the burden rather than
closing the case. A second soft spot is evidential: contamination, anthropomorphic probing, and the
thinness of "similarity geometry" as a proxy for representation are live deflationary challenges to premise
(1), addressed but not extinguished by the unsupervised-alignment and world-model results.

### How it relates to its neighbours

It is the empirical descendant of two classical replies: it vindicates the
[Connectionist Reply](connectionist-reply.md)'s architectural bet, and it sharpens the
[Robot Reply](robot-reply.md) by suggesting that even *textual* commerce — not only sensorimotor
grounding — suffices to fix richly world-aligned content. Against Searle's
[water-pipes](rejoinder-water-pipes.md) move it answers that what the network reproduces is not the
mere *form* of some process but the *content-structure* of human concepts; whether that suffices for
understanding is the live crux.

### In plain terms

Searle's argument was written before anyone could check what a giant text-trained system actually builds
inside. Now we can, and it turns out pure word-shuffling grows an inner map of meaning that lines up with
ours — colour, sound, even a mental picture of a game board it was never shown — exactly the Churchlands'
old hunch, now with receipts. That's hard to square with "shuffling symbols can't get you anywhere near
meaning." The honest limit: it shows the machine builds the right *structure* of meaning, not that it
*feels* anything or *really* understands — so Searle can fall back to "that's still just an elaborate
picture of understanding, not the real thing." The argument wins the outer ring of his position and leaves
the inner keep standing.

### See also

- [llm-text-yields-human-aligned-representations](../claims/llm-text-yields-human-aligned-representations.md) — the empirical premise, with its four lines of
  evidence.
- [syntax-insufficient-for-semantics](../claims/syntax-insufficient-for-semantics.md) — axiom A3, which this reply attacks empirically.
- [connectionist-reply](connectionist-reply.md) — the Churchlands' a priori bet that this reply vindicates with data.
- [robot-reply](robot-reply.md) — the grounding reply this extends to textual grounding.
- [simulation-instances-formal-depicts-causal](../claims/simulation-instances-formal-depicts-causal.md) — Searle's retreat line: aligned structure may still
  only *depict* understanding.
- [intrinsic-derived-intentionality](../concepts/intrinsic-derived-intentionality.md) — the distinction marking what the reply does *not* settle.
- [marjieh-2024](../sources/marjieh-2024.md), [kawakita-2024](../sources/kawakita-2024.md) (perceptual-from-text), [li-2022](../sources/li-2022.md),
  [yuan-2025](../sources/yuan-2025.md) (induced world models), [gurnee-2023](../sources/gurnee-2023.md) (real-world space/time),
  [xu-2025](../sources/xu-2025.md), [doerig-2025](../sources/doerig-2025.md) (human-brain alignment) — the evidence base.

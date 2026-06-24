---
id: concept-aoe2-circuits
type: concept
title: Age of Empires II circuits (a trained perceptron built in a videogame)
headword: Age of Empires II circuits
author: dewynter
status: asserted
tags: [philosophy-of-mind, consciousness, computation, thought-experiment]
style: encyclopedia
uses_concept: [concept-functionalism]
created: 2026-06-24
---

The *Age of Empires II circuits* are a working digital computer assembled inside the 1999 real-time
strategy videogame, devised by Adrian de Wynter ([dewynter-2026](../sources/dewynter-2026.md)). Goats walking along
rails of grass and bridge stand for the 0s and 1s of a signal; patches of ice meter their timing to
prevent race conditions; and from these pieces de Wynter builds a NAND gate — the single operation
from which all of Boolean logic can be assembled. On top of the gates he constructs, and then
*trains*, a one-bit perceptron, the elementary learning unit from which neural networks (and so
large language models) are built. A side-product of the construction is a proof that *Age of
Empires II* is **functionally complete** and **Turing-complete**: anything a computer can compute,
the game can be made to compute.

### What it is for

Unlike most demonstrations that a game is Turing-complete, the point here is philosophical. The
perceptron is the same computational object whether it runs on silicon, on paper, or on goats; de
Wynter uses the videogame implementation as a deliberately absurd substrate to pry computation apart
from its medium. The construction then becomes the engine of an argument about how we may and may not
ascribe human-like attributes to language models (see [aoe2-anthropomorphism](../arguments/aoe2-anthropomorphism.md)): if the
same trained network can live in *Age of Empires II*, then attributes read off an LLM's behaviour are
not unique to the LLM.

### Distinct from the Chinese Nation

The circuits are an implemented, trainable cousin of Block's [chinese-nation](chinese-nation.md), but they are
not the same move. The Chinese Nation is an *imagined* population realizing a mind's functional
organisation, wielded as an intuition pump for *absent qualia* — the suspicion that organisation
without the right substrate yields no experience. De Wynter's machine is *actually built and trained*,
and it is aimed not at the metaphysics of consciousness but at the **methodology of attribution**: he
draws no conclusion that the game lacks (or has) an inner life, and explicitly denies that AoE2 has
human-like attributes. The bite is epistemic, not phenomenal. It is also distinct from Block's
[lookup-table-mind](lookup-table-mind.md), which produces the right *outputs* with no inner processing; the
perceptron here does the genuine processing, learning included.

### In plain terms

Someone built a real, working computer inside the videogame *Age of Empires II* — using herds of
goats as the 1s and 0s and sheets of ice to keep them in step — and on top of it built and taught a
tiny artificial "brain cell" of the kind that large AIs are made from. The serious point hiding in
the joke: the exact same little learning machine that powers a chatbot can be made out of goats. So
when people say a chatbot "understands" or "has morality", you have to ask whether that is really in
the machine or just in how we read it — because you would never say the goats understand anything.
This is a cousin of the famous [chinese-nation](chinese-nation.md) thought experiment, but its punchline is
about how we *measure* such claims, not about whether the goats are secretly conscious.

### See also

- [aoe2-anthropomorphism](../arguments/aoe2-anthropomorphism.md) — the argument the construction powers: anthropomorphic
  attributes of LLMs are substrate-non-unique, so assuming them a priori is circular or uninformative.
- [chinese-nation](chinese-nation.md) — the imagined-population ancestor; aimed at absent qualia where this is
  aimed at the methodology of attribution.
- [lookup-table-mind](lookup-table-mind.md) — right outputs with no processing; the circuits, by contrast, do the
  real computation and learning.
- [functionalism](functionalism.md) — the multiple-realizability of computation the construction dramatizes.
- [dewynter-2026](../sources/dewynter-2026.md) — the note and paper where the circuits and the proof are presented.

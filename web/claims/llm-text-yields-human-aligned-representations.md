---
id: claim-llm-text-yields-human-aligned-representations
type: claim
title: Language models trained on text alone develop internal representations structurally aligned with human ones
headword: Text yields human-aligned representations
author: mishka
status: asserted
tags: [ai, philosophy-of-mind, cognitive-science, semantics]
uses_concept: [concept-intentionality]
style: encyclopedia
created: 2026-06-25
---

Large language models trained purely on text develop *internal representations* whose relational structure
matches that of human representations of the same domain — not merely matching output labels, but
recovering the same similarity geometry and, in some settings, an explicit model of the world the symbols
describe. Four independent lines of evidence converge.

- **Perceptual structure from text.** GPT models' pairwise similarity judgments track human data across
  *six* perceptual modalities, reconstructing canonical structures like the colour wheel and pitch spiral
  from text, with no gain from added visual training ([marjieh-2024](../sources/marjieh-2024.md)); and the *unsupervised*
  alignment of GPT-4's colour-similarity space with that of colour-neurotypical humans — optimal transport
  assuming no label correspondence — shows the match lies in the internal structure, not the names
  ([kawakita-2024](../sources/kawakita-2024.md)).
- **Induced world models.** Sequence-only models build an explicit model of the domain they predict: a
  GPT trained on Othello moves maintains a causally-effective representation of the board
  ([li-2022](../sources/li-2022.md)), robust across architectures ([yuan-2025](../sources/yuan-2025.md)).
- **Real-world structure.** Beyond games, LLMs carry *linear* representations of space and time at multiple
  scales, with individual neurons encoding coordinates — the "basic ingredients of a world model"
  ([gurnee-2023](../sources/gurnee-2023.md)).
- **Brain alignment.** Most directly for the "human-aligned" wording, next-token training yields conceptual
  representations that *align with human brain activity*, emerging without real-world grounding
  ([xu-2025](../sources/xu-2025.md)), and LLM embeddings of scene captions predict visual-cortex activity well enough to
  reconstruct the caption from brain data ([doerig-2025](../sources/doerig-2025.md)).

**Scope.** The claim is about *structural/representational* alignment — the geometry of the model's internal
states matching the human one — established as a *lower bound* on what is latent in language. It does **not**
by itself assert that the models have phenomenal experience, consciousness, or
[intrinsic](../concepts/intrinsic-derived-intentionality.md) (rather than derived) intentionality; those are
further questions the alignment does not settle. Its force is to show that *syntax* (text statistics) is, as
a matter of fact, enough to *induce* richly human-like semantic *structure*.

**Who would deny it, and how.** A Searlean grants the structural finding but denies it touches the real
issue: aligned representational structure is still structure — a *depiction* of human semantics, not the
intrinsic understanding the [Chinese Room](../concepts/chinese-room.md) is about
([simulation-instances-formal-depicts-causal](simulation-instances-formal-depicts-causal.md)). Sceptics about the evidence add deflationary
readings: training-data contamination, anthropomorphic probing, or that "similarity geometry" is a thin
proxy for representation. The claim is framed to survive these as a structural result while conceding it
does not, alone, reach the phenomenal.

Distinct from [llm-approximates-perfect-actor](llm-approximates-perfect-actor.md) (about *behavioural* indistinguishability) and from
[llm-access-similarity-not-encoding](llm-access-similarity-not-encoding.md): this claim is specifically about the *internal
representational structure* matching the human one, the empirical pressure point on Searle's third axiom.

### In plain terms

Feed a model nothing but text and, surprisingly, it builds an inner "map" of things that lines up with the
map in our heads. Ask GPT-4 which colours are similar and its answer reconstructs the human colour wheel;
the same holds for sound, taste, and three other senses — and it doesn't even help to also train it on
images, because the structure was already hiding in the words. Train a model only on Othello moves and it
quietly builds a picture of the board. None of this proves the model *feels* anything or *really*
understands — but it does show that pure word-shuffling can grow a genuinely human-shaped *web of meaning*,
which is exactly the thing Searle's argument says shuffling alone can never do.

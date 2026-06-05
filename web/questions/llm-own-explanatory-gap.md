---
id: question-llm-own-explanatory-gap
type: question
title: Would a consciousness-naive but introspecting LLM be able to fully explain its own self-perception from its mechanism?
author: mishka
status: contested
tags: [philosophy-of-mind, consciousness, ai]
uses_concept: [concept-introspective-gap-varieties, concept-hard-problem]
created: 2026-06-05
---

precise statement of the issue: take a model trained with **no** exposure to philosophy-of-mind or
consciousness discourse (controlling the *training-contamination* confound; see
[introspective-gap-varieties](../concepts/introspective-gap-varieties.md)), but with limited functional introspective access to its own
states ([llm-functional-introspection](../claims/llm-functional-introspection.md)). Teach it the mechanics of how it works — transformer
architecture, activations, attention, logits, token probabilities. Then ask: does that mechanistic
self-knowledge *fully explain*, from its own side, how it perceives the world and its own thoughts?

the two outcomes:
- **Yes — deflation.** The model finds no residual explanandum: its "perceptions" are just
  input-conditioned latent representations made available to downstream prediction and self-report,
  its introspective "feelings" just compressed summaries of its own processing. A computational
  analogue of illusionism / strong functionalism — the apparent gap dissolves from the inside.
- **No — a gap remains.** The model reports that the mechanics do not explain why its accessible
  states present themselves as they do, robustly and not traceably to contamination.

a *separate* question, only if the answer is **No**: *why* does the gap arise? That is a distinct
issue from whether it arises, with its own candidate answers (sorted by
[introspective-gap-varieties](../concepts/introspective-gap-varieties.md): an *ontological* residue, an *architectural-access* limit, a
*conceptual-translation* failure). One such candidate — proposed tentatively — is recorded as its own
node, [self-explanation-gap-can-be-architectural](../claims/self-explanation-gap-can-be-architectural.md); it is a separate conjecture layered on the
"No," not a third outcome of the experiment. Note that a "No" is not by itself evidence of phenomenal
consciousness ([access-vs-phenomenal-consciousness](../concepts/access-vs-phenomenal-consciousness.md)).

why it bears on the governing issue: a sub-issue of [hard-problem](hard-problem.md) — it asks whether the
hard-problem *form* arises in a system whose only relevant property is self-modelling under restricted
access, with the human cultural inheritance stripped out.

how it could be adjudicated: vary internal-state access across models and watch whether a "No" appears
and whether it then *shrinks* — e.g. (A) a baseline with no consciousness literature; (B) given only
transformer mechanics; (C) trained to report specific activation-level facts; (D) given external
probes of its own activations at inference; (E) given calibrated access to its own token
probabilities. If a "No" shrinks as access improves, that supports the architectural hypothesis for it;
if it persists under rich access, that is more analogous to the human hard problem; if it appears only
when philosophy-of-mind text is in training, the phenomenon is contamination.

tentative remark (not a claim or edge): a *deflation* outcome might in turn *inform* attempts on the
human hard problem — a clean artificial case of "I know the mechanism but cannot see how it becomes
this appearance." Recorded as exploratory only; the cluster takes no `attacks` stance on
[explanatory-gap](../arguments/explanatory-gap.md) or [phenomenal-residue](../claims/phenomenal-states-not-exhausted-by-role.md).

### In plain terms

Build an AI that has never read a word about consciousness but can introspect a little on its own
insides, and teach it exactly how it works as a machine. Then ask: "Does knowing all that explain how
your own thoughts seem to you?" Two answers are possible: **yes** — "no mystery, it's just my
processing summarized" (the gap dissolves), or **no** — "I understand the machinery but still can't see
how it becomes *this*." Only if the answer is *no* does a second, separate question open up: *why* not?
— and one proposed answer to that is recorded as its own claim ([self-explanation-gap-can-be-architectural](../claims/self-explanation-gap-can-be-architectural.md)),
kept apart from the yes/no question here. You could even tell the cases apart experimentally, by giving
models more or less access to their own internals and seeing whether the "no" shrinks.

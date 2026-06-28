---
id: argument-llmary-token-encounter
type: argument
title: LLMary — a model that has read all of AI but never seen token 123 updates on first encounter, yet the whole episode is physical, refuting the Knowledge Argument's conditional
headword: LLMary token encounter
author: mishka
status: asserted
tags: [philosophy-of-mind, consciousness, ai, thought-experiment]
pattern: thought-experiment
attacks: [argument-knowledge-argument]
responds_to: [argument-knowledge-argument]
uses_concept: [concept-llmary, concept-knowledge-argument, concept-access-vs-phenomenal-consciousness]
style: encyclopedia
created: 2026-06-11
---

This argument is a *counterexample* to the [knowledge argument](knowledge-argument.md), not a
theory of its own. It grants the famous Mary scenario its starting materials, then exhibits a case with
the very same structure whose outcome is uncontroversially physical, showing that the argument's
central inference does not go through. It raises the thought-experiment critical question of the
*bridge* — whether the case really licenses the conclusion drawn from it — and the move is deliberately
*negative* and *metalinguistic*: it shows the Mary inference cannot establish its conclusion, and says
nothing about whether physicalism is in fact true. Its inference form is exactly that: a counterexample
to a conditional, refuting an entailment while asserting no ontology of its own.

### The conditional the knowledge argument needs

Read the knowledge argument as resting on a conditional, *if X then not-Y*:

- *X* — a subject has *complete prior knowledge* of a phenomenon (every sayable, physical fact about
  it) yet undergoes a *genuine cognitive gain* on first *encountering* it; and
- *Y* — physicality: the gain is a wholly physical affair, with nothing non-physical involved.

The argument uses Frank Jackson's Mary as an instance of *X* and concludes *not-Y* — that the fact she
learns on first seeing red is non-physical ([jackson-1982](../sources/jackson-1982.md); see
[some truths about experience are not
physically deducible](../claims/some-truths-about-experience-not-physically-deducible.md)).

### LLMary as an actual instance of X *and* Y

The scenario [llmary](../concepts/llmary.md) is a language model that has read all of AI and arXiv — including its
own architecture, the whole tokenisation pipeline, and discussions that *mention* "Token #123" — but
has never had the actual word-piece for token 123 *used* in its input. It is an actual instance of *X
and Y* together.

*X holds.* LLMary already knows everything *sayable* about token 123, down to its own workings and the
token's index, embedding, and role — the analogue of [Mary knowing all
the physical facts](../claims/mary-knows-all-physical.md). The only gap is one of use versus mention: the token is mentioned exhaustively,
never used. Yet when the word-piece itself first flows through mid-training, the model genuinely updates
— its predicted probability for the token was near zero, so the cross-entropy loss is large and the
gradient step is large, a real and measurable gain on first encounter (the analogue of
[Mary learning something on release](../claims/mary-learns-on-release.md)).

*Y holds.* Every part of the episode is physical through and through: the prior knowledge is weights,
the gain is a weight change, and the trigger (token 123) is an integer, a one-hot vector, a voltage
pattern. There is nowhere for a non-physical fact to hide.

A single genuine case of *X and Y* contradicts *if X then not-Y* — applying the conditional by modus
ponens would yield *not-Y*, against the *Y* we have. So one such instance falsifies the conditional.
"Complete prior knowledge yet a gain on encounter" does *not* entail non-physicality; the knowledge
argument's inference is unsound as a general entailment. The parallel question — "does LLMary prove
that token 123 is non-physical?" — makes the failure vivid: obviously it does not.

### What this does and does not show

The argument does *not* establish *Y*: it is no argument that physicalism is true, nor that Mary's gain
is physical. Nor does it pick a positive diagnosis of what Mary gains; it is consistent with the
ability reading ([that Mary gains abilities, not facts](../claims/mary-gains-abilities-not-facts.md)), the
new-guise reading ([old fact, new guise](old-fact-new-guise.md)), and others, and commits to
none. Its entire content is the negative point that one cannot use the Mary argument to support
anti-physicalism, because the inference pattern it instantiates has a true-premise, false-conclusion
counterexample. That is why this node attacks the *argument*, not any ontological claim.

### The weakest premise, and the dilemma it forces

The weak point is whether LLMary instantiates the *same X*. The phenomenal realist resists by reading
*X* phenomenally and charging an equivocation on "gain" or "learns" — the standard charge that the case
begs the question:

- On an *access* reading of *X* — acquiring a new information-bearing state or disposition despite a
  complete description — LLMary plainly satisfies *X*, and the conditional dies.
- On a *phenomenal* reading of *X* — coming to know what the encounter is *like* despite complete
  physical knowledge — LLMary arguably fails *X*. It is a *zombie learner*: all
  [access](../concepts/access-vs-phenomenal-consciousness.md)-update, with nothing it is like to undergo it.
  So read, LLMary is not a counterexample but an irrelevant case.

This forces a dilemma rather than an outright refutation. Either *X* is the access kind, in which case
the conditional is false, as LLMary shows; or *X* is the phenomenal kind, in which case the knowledge
argument owes an independent reason that Mary's encounter delivers phenomenal *knowledge-that* — the
very point in dispute. Either way the argument cannot stand as written, and the standoff relocates to
whether there is a phenomenal residue over and above the access-update — that is, back to the hard
problem. The honest verdict is conditional: *if* Mary's *X* is LLMary's *X*, the entailment fails, and
the burden is on the realist to show that it is not, without leaning on the very intuition under test.

### Distinct from neighbouring moves

It is distinct from [RoboMary](mary-misimagined.md) ([dennett-2005](../sources/dennett-2005.md)), which attacks the
knowledge argument's *intuition* premise — a system with complete self-knowledge pre-computes the state
and meets red with *no* update, so Mary learns nothing. LLMary instead *grants* the update and attacks
the *conditional*: a case of *X and Y* is actual, so *if X then not-Y* is false. The two computational
variants pull on opposite premises. It is also distinct from the [ability
hypothesis](ability-hypothesis.md), which offers a *positive analysis* of what Mary gains (abilities, not facts); LLMary
offers no positive diagnosis at all — it is a neutral counterexample to the inference, compatible with
the ability hypothesis but not asserting it.

### In plain terms

Mary's famous argument has the shape of an **"if … then …"**: *if* you knew every physical fact about
colour and *still* learned something new the first time you saw red, *then* the world isn't fully
physical ([knowledge argument](knowledge-argument.md)).

**LLMary** is a real-style case that breaks that "if … then." It's an AI language model that has read
every AI textbook and all of arXiv. One word-piece — "token 123" — never showed up in its training,
though it knows everything *written* about it. Then it meets token 123 for the first time and clearly
*does* learn: it was caught off guard (it expected that token almost never), so its internal numbers get
a big correction. So here we have both halves at once: *knew everything sayable* **and** *still updated
on first contact* — yet the whole thing is obviously, boringly physical (just numbers changing because
of an input). Ask the Mary question of it — "so is token 123 non-physical?" — and the answer is plainly
no.

One real case where both halves hold **and** it's all physical is enough to break the "if … then." So
the Mary move can't, by itself, prove the world isn't physical. Note what this does *not* claim: it does
**not** prove the world *is* physical, and it doesn't say which story about Mary is right. It only takes
away one argument.

The catch: LLMary feels nothing — nobody's home enjoying token 123. So a defender says the word "learn"
is doing two jobs. LLMary "learns" only in the *information/skill* sense; Mary supposedly also gets the
*feeling* of red, and that felt part is what was allegedly left out. So LLMary cleanly shows the
information-update kind of learning is plain physics; whether there's an extra *felt* kind in Mary's
case is the original puzzle all over again (the [access
versus feeling](../concepts/access-vs-phenomenal-consciousness.md) split). A sharp jab at the argument's logic — not a proof about reality.

### See also

- [knowledge-argument](knowledge-argument.md) — the target: the inference this move exhibits a counterexample to.
- [llmary](../concepts/llmary.md) — the scenario in full, including the use/mention diagnosis it turns on.
- [mary-misimagined](mary-misimagined.md) — RoboMary; the sister computational variant that attacks the
  *intuition* premise instead of the conditional.
- [ability-hypothesis](ability-hypothesis.md) — a *positive* analysis of Mary's gain; compatible with this move but
  going further than it.
- [access-vs-phenomenal-consciousness](../concepts/access-vs-phenomenal-consciousness.md) — the distinction the realist's dilemma turns on:
  access-update versus felt residue.

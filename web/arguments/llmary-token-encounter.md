---
id: argument-llmary-token-encounter
type: argument
title: LLMary — a model that has read all of AI but never seen token 123 updates on first encounter, yet the whole episode is physical, refuting the Knowledge Argument's conditional
author: mishka
status: asserted
tags: [philosophy-of-mind, consciousness, ai, thought-experiment]
pattern: thought-experiment
attacks: [argument-knowledge-argument]
responds_to: [argument-knowledge-argument]
uses_concept: [concept-llmary, concept-knowledge-argument, concept-access-vs-phenomenal-consciousness]
style: legacy
created: 2026-06-11
---

Raises thought-experiment **CQ-bridge** against [knowledge-argument](knowledge-argument.md) by exhibiting a
counterexample to the conditional that argument needs. It is a purely **negative, metalinguistic**
move: it shows the Mary inference cannot establish its conclusion. It says **nothing about whether
physicalism is true** — only that *this argument* cannot support its denial.

inference form: counterexample to a conditional (refutes an entailment; asserts no ontology of its own).

Read the Knowledge Argument as the conditional it relies on:

- **(KA)  X → ¬Y**, where
  - **X** = a subject has *complete prior knowledge* of a phenomenon (every sayable/physical fact about
    it) yet undergoes a *genuine cognitive gain* on first **encountering** it; and
  - **Y** = physicality — the gain is a wholly physical affair, nothing non-physical involved.

The argument uses Mary as an instance of X to deliver **¬Y** (the learned fact is non-physical; see
[some-truths-about-experience-not-physically-deducible](../claims/some-truths-about-experience-not-physically-deducible.md)).

**LLMary is an actual instance of X ∧ Y** (the scenario is [llmary](../concepts/llmary.md): a model that has read all
of AI and arXiv — including its own architecture and the whole tokenisation pipeline, and discussions
that *mention* "Token #123" — but has never had the actual word-piece for token 123 *used* in its input).

- **X holds.** LLMary already "knows" everything *sayable* about token 123, down to its own workings and
  the token's index, embedding, and role — the analogue of [mary-knows-all-physical](../claims/mary-knows-all-physical.md); the only
  gap is use/mention (mentioned exhaustively, never used). Yet when the word-piece itself first flows
  through mid-training, it genuinely updates: the predicted probability of that token was near zero, so
  the cross-entropy loss is large and the gradient step is large. A real, measurable gain on first
  encounter (the analogue of [mary-learns-on-release](../claims/mary-learns-on-release.md)).
- **Y holds.** Every part of the episode is physical through and through: the prior knowledge is
  weights, the gain is a weight change, the trigger (token 123) is an integer / one-hot vector / voltage
  pattern. There is nowhere for a non-physical fact to hide.

**X ∧ Y contradicts X → ¬Y** (modus ponens would yield ¬Y, against Y). One genuine X∧Y instance
therefore falsifies the conditional. So "complete prior knowledge yet a gain on encounter" does **not**
entail non-physicality; the Knowledge Argument's inference is unsound *as a general entailment*, and the
parallel "does LLMary prove token 123 is non-physical?" makes the failure vivid — obviously it doesn't.

**What this does and does not show.** It does **not** establish Y (it is no argument that physicalism is
true, nor that Mary's gain is physical). It does **not** pick a positive diagnosis of what Mary gains —
it is consistent with the ability reading ([mary-gains-abilities-not-facts](../claims/mary-gains-abilities-not-facts.md)), the new-guise
reading ([old-fact-new-guise](old-fact-new-guise.md)), and others, and commits to none. Its entire content is the
negative point: **you cannot use the Mary argument to support anti-physicalism**, because the inference
pattern it instantiates has a true-premise / false-conclusion counterexample. That is why this node
`attacks` the *argument*, not any ontological claim.

weakest premise: whether LLMary instantiates the **same X**. The realist resists by reading X
phenomenally and charging equivocation on "gain/learns" (thought-experiment CQ-begs-the-question):

- On an **access** reading of X — *acquires a new information-bearing state / disposition despite
  complete description* — LLMary plainly satisfies X, and the conditional dies.
- On a **phenomenal** reading of X — *comes to know what the encounter is like despite complete physical
  knowledge* — LLMary arguably fails X: it is a *zombie learner*, all
  [access](../concepts/access-vs-phenomenal-consciousness.md)-update, nothing it is like to undergo it. So read,
  LLMary is not a counterexample but an irrelevant case.

This forces a dilemma rather than a refutation: either X is the access kind (then the conditional is
false, as LLMary shows) or X is the phenomenal kind (then the Knowledge Argument owes an independent
reason that Mary's encounter delivers phenomenal *knowledge-that* — the very point in dispute). Either
way the argument cannot stand *as written*; the standoff relocates to whether there is a phenomenal
residue over the access-update — i.e. back to the hard problem. The honest verdict is conditional: *if*
Mary's X is LLMary's X, the entailment fails; the burden is on the realist to show it is not, without
leaning on the intuition under test.

Distinct from [mary-misimagined](mary-misimagined.md) (RoboMary) because that attacks the *Intuition* premise — a
system with complete self-knowledge pre-computes the state and meets red with **no** update, so Mary
learns nothing. LLMary instead *grants* the update and attacks the *conditional*: X∧Y is actual, so
X→¬Y is false. The two computational variants pull on opposite premises. Distinct from
[ability-hypothesis](ability-hypothesis.md) because that offers a *positive analysis* of what Mary gains (abilities,
not facts); LLMary offers no positive diagnosis at all — it is a neutral counterexample to the inference,
compatible with the ability hypothesis but not asserting it.

### In plain terms

Mary's famous argument has the shape of an **"if … then …"**: *if* you knew every physical fact about
colour and *still* learned something new the first time you saw red, *then* the world isn't fully
physical ([knowledge-argument](knowledge-argument.md)).

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
information-update kind of learning is plain physics; whether there's an extra *felt* kind in Mary's case
is the original puzzle all over again (the [access-vs-feeling](../concepts/access-vs-phenomenal-consciousness.md)
split). A sharp jab at the argument's logic — not a proof about reality.

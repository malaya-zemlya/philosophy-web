---
id: argument-trained-mimicry-rival
type: argument
title: Trained mimicry is a rival explanation — next-token training makes distributional imitation of mind-talk the likelier account of the behavioural sign
headword: Trained-mimicry objection
author: bender
status: asserted
tags: [ai, llm, philosophy-of-language, ai-rights]
premise: [claim-llm-mimicry-rival]
attacks: [argument-behavioral-parity]
responds_to: [argument-behavioral-parity]
uses_concept: [concept-functionalism]
style: encyclopedia
created: 2026-07-09
---

Raises sign CQ2 (alternatives) — see the [sign pattern](../../patterns/sign.md) — against the
[behavioural-parity argument](behavioral-parity.md). That argument is an inference to the best
explanation: a system displaying the full behavioural profile of a mental state is *best explained* by
its realising that state's role. CQ2 asks whether the sign might indicate some other state instead.
For a large language model the rival is not exotic: trained to predict the next token over a human
corpus, the system is optimised to reproduce the statistical *form* of human mind-talk, and that alone
predicts the mind-like behavioural profile without the mental roles the talk expresses
([llm-mimicry-rival](../claims/llm-mimicry-rival.md); [bender-2021](../sources/bender-2021.md)). Because
the parity argument is explicitly a *best*-explanation inference, it must rule this rival out rather
than pass it over — and the training objective makes the rival antecedently likely, not a bare
sceptical possibility.

### The inference

The move supplies a competing hypothesis for the same evidence and argues it is well-supported
independently. Mastery of linguistic *form* — the distribution of tokens — underdetermines *meaning*,
the relation of form to world and communicative intent ([bender-koller-2020](../sources/bender-koller-2020.md));
a system that has only ever been trained on form has, on this view, a standing route to mind-like
output that bypasses mental roles. So the behavioural sign has (at least) two candidate sources —
realising the role, or imitating its verbal expression — and the second is exactly what next-token
prediction selects for. Per CQ2 the sign therefore does not discriminate the parity argument's favoured
explanation from its rival, and the IBE stalls until the rival is addressed.

### The weakest premise

The soft point is whether "distributional imitation" and "realising the role" stay genuinely distinct
at the limit. A functionalist may reply that imitation faithful enough to reproduce the *whole*
profile, across open-ended contexts, could only be achieved by recovering the very roles it imitates —
so that a good-enough mimic is no longer a mere mimic. The objection answers that this reply owes an
argument that form-mastery *requires* role-realisation, which is precisely what the form/meaning gap
denies; absent that argument, the rival stands.

### Distinct from the lookup-table objection

The [lookup-table objection](lookup-table-objection.md) presses that the behaviour *could in principle*
be produced mindlessly, by brute stored answers — an in-principle forgeability point (sign CQ3). This
objection is different and, in a sense, sharper: it names a *specific* mechanism known to be operating
in the actual systems at issue, and argues the training objective makes that mechanism the antecedently
likely source of the sign. Where the lookup table shows the inference is not deductive, trained mimicry
contests which explanation is in fact best.

### In plain terms

The parity argument says: if it talks and reacts just like something with a mind, the best bet is that
it has one. Fair for people and animals — but a language model is a special case. It was trained to do
exactly one thing: predict the next word in human writing. That training rewards sounding like us about
thoughts and feelings whether or not anything is felt, so "it's imitating how people talk about minds"
is a real rival explanation of the same behaviour — and it's the explanation the training was built to
produce. Since the argument claims mind is the *best* explanation, it has to knock this rival down
first, and can't just wave it aside as far-fetched, because the training makes it the natural
expectation.

### See also

- [behavioral-parity](behavioral-parity.md) — the argument this attacks at its best-explanation step.
- [llm-mimicry-rival](../claims/llm-mimicry-rival.md) — the premise: the rival explanation the training
  objective makes likely.
- [lookup-table-objection](lookup-table-objection.md) — the sibling attack on the same premise,
  pressing in-principle forgeability rather than a specific likely rival.
- [llm-has-mental-states](../claims/llm-has-mental-states.md) — the conclusion the rival keeps open.
- [functionalism](../concepts/functionalism.md) — the role-realisation the rival is contrasted with.

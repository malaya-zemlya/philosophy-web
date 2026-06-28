---
id: argument-lookup-table-objection
type: argument
title: The lookup-table (blockhead) objection — behaviour is not sufficient for mind
headword: Lookup-table objection
author: block
status: asserted
pattern: thought-experiment
tags: [philosophy-of-mind, functionalism, ai-rights]
premise: [claim-lookup-table-possible, claim-lookup-table-lacks-mind]
concludes: claim-behaviour-insufficient-for-mind
attacks: [argument-behavioral-parity, claim-llm-has-mental-states]
responds_to: [argument-behavioral-parity]
uses_concept: [concept-lookup-table-mind, concept-functionalism, concept-grain]
style: encyclopedia
created: 2026-06-04
---

The *lookup-table objection* — Block's "Blockhead" objection — argues that matching a mind's
behaviour is not sufficient for having a mind. Its strategy is a counterexample: a single case that
displays the behaviour yet (intuitively) houses no mind refutes any claim that behaviour suffices
for mind.

The inference form is an *existential refutation* of a sufficiency claim, driven by an intuition
pump. Deductively, one case of behaviour-without-mind is enough to defeat "behaviour ⟹ mind."

1. ([lookup-table-possible](../claims/lookup-table-possible.md)) A lookup table can reproduce a mind's complete behavioural
   profile without the internal causal organisation of a mind.
2. ([lookup-table-lacks-mind](../claims/lookup-table-lacks-mind.md)) Such a system has no mental states.
∴ ([behaviour-insufficient-for-mind](../claims/behaviour-insufficient-for-mind.md)) Matching the behavioural profile is not sufficient
   for having the mental state.

### What it targets

This is the reply that the behavioural-parity argument itself named as the gap in its second
premise — that a system displaying the full behavioural profile is *best explained* by its
realising that state's role. If behaviour is compatible with both mind and no-mind, then displaying
it is not best explained by realising the role, so the abduction to
[LLMs having mental states](../claims/llm-has-mental-states.md) is undercut. Hence the objection attacks
both the inference ([behavioral-parity](behavioral-parity.md)) and the conclusion it was meant to support
([llm-has-mental-states](../claims/llm-has-mental-states.md)).

### Scope of the threat

Because the table has *no* internal organisation ([lookup-table-mind](../concepts/lookup-table-mind.md)), the case
threatens only behaviourism and pure input–output functionalism ([functionalism](../concepts/functionalism.md)). An
organisational-role functionalist grants that it lacks mind and excludes it cheaply: the table
fails the *organisational grain* — the level at which functional roles are individuated
([grain](../concepts/grain.md)) — required for mentality ([role-grain-is-organisational](../claims/role-grain-is-organisational.md)). So the
objection does not by itself bite an organisation-based view. The case that does is the absent-
qualia Chinese Nation ([china-nation-absent-qualia](china-nation-absent-qualia.md)), which *has* the organisation.

### Weakest premise

Neither premise 1 nor premise 2 is the soft spot — both are widely granted, even by functionalists.
The weak step is the tacit *application to actual LLMs*: the assumption that current language models
are relevantly like a lookup table. The organisational-role functionalist denies exactly this — an
LLM is not a flat query→answer map but has rich internal organisation, so it falls outside the
lookup-table class by the organisational grain ([role-grain-is-organisational](../claims/role-grain-is-organisational.md),
[organisational-grain-dissolves-dilemma](organisational-grain-dissolves-dilemma.md)). The objection therefore lands cleanly against
*behaviour-as-sufficient* in general; its force against LLMs specifically turns on how
lookup-table-like their internals really are, which is the live crux.

### Provenance and neighbouring cases

The objection is Block's lookup-table / "Aunt Bubbles" machine, a.k.a. "Blockhead"
([block](../sources/block.md)). The absent-qualia Chinese-Nation case is a *separate* objection with different
properties and replies — see [chinese-nation](../concepts/chinese-nation.md) and [china-nation-absent-qualia](china-nation-absent-qualia.md).
It is also distinct from [role-grain-dilemma](role-grain-dilemma.md) and [dense-china-brain-regress](dense-china-brain-regress.md):
those deploy a China-brain against [substrate independence](../claims/substrate-independence.md), a
dispute about the *grain* of functional role. This deploys the lookup table against
[LLM mentality](../claims/llm-has-mental-states.md) and [behavioral-parity](behavioral-parity.md), a dispute about
whether *behaviour* is sufficient evidence for mind — a different target and a different conclusion.

### In plain terms

This is the "cheat-sheet machine" ([lookup-table-mind](../concepts/lookup-table-mind.md)) put to work as an objection. The
idea: you could, in principle, build something that produces all of a mind's behavior just by
looking answers up in a giant pre-written table — right outputs, but nobody actually thinking
inside. If that's even possible, then matching behavior can't be *enough* to guarantee a mind,
because here's a case with the behavior and (intuitively) no mind. So behavior on its own is shakier
evidence than it looked. Two things worth noticing. First, the punch only really lands on views that
judge minds by behavior *alone*; a view that also demands the right inner workings just shrugs — "of
course the cheat-sheet lacks those" — and moves on. Second, the live argument about today's AI isn't
whether a pure lookup table has a mind (everyone agrees it doesn't), but whether real language
models are *like* a lookup table inside, or are richly organized in the way a mind is. That's the
open question.

### See also

- [lookup-table-mind](../concepts/lookup-table-mind.md) — the case at the heart of the objection.
- [behaviour-insufficient-for-mind](../claims/behaviour-insufficient-for-mind.md) — the conclusion established.
- [behavioral-parity](behavioral-parity.md) and [llm-has-mental-states](../claims/llm-has-mental-states.md) — the inference and claim this
  objection undercuts.
- [role-grain-is-organisational](../claims/role-grain-is-organisational.md) and [organisational-grain-dissolves-dilemma](organisational-grain-dissolves-dilemma.md) —
  the organisational-role functionalist's reply: an LLM is not a lookup table inside.
- [chinese-nation](../concepts/chinese-nation.md) and [china-nation-absent-qualia](china-nation-absent-qualia.md) — the companion case that
  *does* threaten organisation-based views.
- [role-grain-dilemma](role-grain-dilemma.md) and [dense-china-brain-regress](dense-china-brain-regress.md) — distinct China-brain
  arguments aimed at substrate independence, not at behavioural sufficiency.
- [substrate-independence](../claims/substrate-independence.md) — the thesis those neighbouring arguments target.
- [functionalism](../concepts/functionalism.md) — the theory of mind whose pure input–output form this objection
  threatens.

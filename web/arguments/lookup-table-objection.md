---
id: argument-lookup-table-objection
type: argument
title: The lookup-table (blockhead) objection — behaviour is not sufficient for mind
author: block
status: asserted
pattern: thought-experiment
tags: [philosophy-of-mind, functionalism, ai-rights]
premise: [claim-lookup-table-possible, claim-lookup-table-lacks-mind]
concludes: claim-behaviour-insufficient-for-mind
attacks: [argument-behavioral-parity, claim-llm-has-mental-states]
responds_to: [argument-behavioral-parity]
uses_concept: [concept-lookup-table-mind, concept-functionalism, concept-grain]
created: 2026-06-04
---

inference form: counterexample (an existential refutation of a sufficiency claim), driven by an
intuition pump. Deductively: a single case with behaviour-but-no-mind refutes "behaviour ⟹ mind."

1. ([lookup-table-possible](../claims/lookup-table-possible.md)) A lookup table can reproduce a mind's complete behavioural
   profile without the internal causal organisation of a mind.
2. ([lookup-table-lacks-mind](../claims/lookup-table-lacks-mind.md)) Such a system has no mental states.
∴ ([behaviour-insufficient-for-mind](../claims/behaviour-insufficient-for-mind.md)) Matching the behavioural profile is not sufficient for
   having the mental state.

bearing on the target: this is the `responds_to` argument that [behavioral-parity](behavioral-parity.md) itself
named as the gap in its premise (2) ("a system displaying the full behavioural profile … is best
explained by its realising that state's role"). If behaviour is compatible with both mind and
no-mind, then displaying it is not *best explained* by realising the role — so the abduction to
[llm-has-mental-states](../claims/llm-has-mental-states.md) is undercut. Hence the `attacks` on both the inference
([behavioral-parity](behavioral-parity.md)) and the conclusion it was meant to support ([llm-has-mental-states](../claims/llm-has-mental-states.md)).

scope of the threat (a property specific to the lookup table): because the table has *no* internal
organisation ([lookup-table-mind](../concepts/lookup-table-mind.md)), it threatens only behaviourism and pure input–output
functionalism. An organisational-role functionalist grants that it lacks mind and excludes
it cheaply — the lookup table fails the organisational grain ([role-grain-is-organisational](../claims/role-grain-is-organisational.md)).
So this objection does NOT by itself bite an organisation-based view; the case that does is the
Chinese Nation ([china-nation-absent-qualia](china-nation-absent-qualia.md)), which *has* the organisation.

weakest premise: not premise 1 or 2 (both widely granted, even by functionalists), but the
**application to actual LLMs** — the tacit step that current LLMs are relevantly like a lookup
table. The organisational-role functionalist denies exactly this: an LLM is not a flat query→answer map but has rich internal
organisation, so it is excluded from the lookup-table class by the organisational grain
([role-grain-is-organisational](../claims/role-grain-is-organisational.md), [organisational-grain-dissolves-dilemma](organisational-grain-dissolves-dilemma.md)). The objection
therefore lands against *behaviour-as-sufficient* in general; its force against LLMs specifically
turns on how lookup-table-like their internals are — the live crux.

provenance: Ned Block's lookup-table / "Aunt Bubbles" machine, a.k.a. "Blockhead" ([block](../sources/block.md),
"Psychologism and Behaviorism" 1981). The absent-qualia Chinese-Nation case is a *separate* objection
with different properties and replies — see [chinese-nation](../concepts/chinese-nation.md) and [china-nation-absent-qualia](china-nation-absent-qualia.md).

Distinct from [role-grain-dilemma](role-grain-dilemma.md) and [dense-china-brain-regress](dense-china-brain-regress.md): those
deploy a China-brain against [substrate-independence](../claims/substrate-independence.md), about the *grain* of functional role.
This deploys the lookup table against [llm-has-mental-states](../claims/llm-has-mental-states.md) / [behavioral-parity](behavioral-parity.md), about
whether *behaviour* is sufficient evidence for mind — a different target and conclusion.

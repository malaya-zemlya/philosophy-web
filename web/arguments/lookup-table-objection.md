---
id: argument-lookup-table-objection
type: argument
title: The lookup-table (blockhead) objection — behaviour is not sufficient for mind
author: block
status: asserted
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

1. (claim-lookup-table-possible) A lookup table can reproduce a mind's complete behavioural
   profile without the internal causal organisation of a mind.
2. (claim-lookup-table-lacks-mind) Such a system has no mental states.
∴ (claim-behaviour-insufficient-for-mind) Matching the behavioural profile is not sufficient for
   having the mental state.

bearing on the target: this is the `responds_to` argument that argument-behavioral-parity itself
named as the gap in its premise (2) ("a system displaying the full behavioural profile … is best
explained by its realising that state's role"). If behaviour is compatible with both mind and
no-mind, then displaying it is not *best explained* by realising the role — so the abduction to
claim-llm-has-mental-states is undercut. Hence the `attacks` on both the inference
(argument-behavioral-parity) and the conclusion it was meant to support (claim-llm-has-mental-states).

scope of the threat (a property specific to the lookup table): because the table has *no* internal
organisation (concept-lookup-table-mind), it threatens only behaviourism and pure input–output
functionalism. An organisational-role functionalist grants that it lacks mind and excludes
it cheaply — the lookup table fails the organisational grain (claim-role-grain-is-organisational).
So this objection does NOT by itself bite an organisation-based view; the case that does is the
Chinese Nation (argument-china-nation-absent-qualia), which *has* the organisation.

weakest premise: not premise 1 or 2 (both widely granted, even by functionalists), but the
**application to actual LLMs** — the tacit step that current LLMs are relevantly like a lookup
table. The organisational-role functionalist denies exactly this: an LLM is not a flat query→answer map but has rich internal
organisation, so it is excluded from the lookup-table class by the organisational grain
(claim-role-grain-is-organisational, argument-organisational-grain-dissolves-dilemma). The objection
therefore lands against *behaviour-as-sufficient* in general; its force against LLMs specifically
turns on how lookup-table-like their internals are — the live crux.

provenance: Ned Block's lookup-table / "Aunt Bubbles" machine, a.k.a. "Blockhead" (source-block,
"Psychologism and Behaviorism" 1981). The absent-qualia Chinese-Nation case is a *separate* objection
with different properties and replies — see concept-chinese-nation and argument-china-nation-absent-qualia.

Distinct from argument-role-grain-dilemma and argument-dense-china-brain-regress: those
deploy a China-brain against claim-substrate-independence, about the *grain* of functional role.
This deploys the lookup table against claim-llm-has-mental-states / argument-behavioral-parity, about
whether *behaviour* is sufficient evidence for mind — a different target and conclusion.

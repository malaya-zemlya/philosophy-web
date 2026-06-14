---
id: claim-llm-access-similarity-not-encoding
type: claim
title: An LLM's introspective access reaches the similarity structure of its internal states but not the encoding that carries it
headword: Similarity, not encoding
author: mishka
status: asserted
tags: [philosophy-of-mind, ai, interpretability]
uses_concept: [concept-introspective-gap-varieties, concept-first-person-access]
style: legacy
created: 2026-06-09
---

gloss: what an LLM's self-report economy can reach about its own internal states is, to a first
approximation, their *relational* structure — which states are near which, what is analogous to what,
what a state is about — and not the *encoding* that carries that structure: the actual activation
vectors, their components, the circuits that compute them. A token arrives as an embedding the model
can use but cannot read: full access to position-in-similarity-space, no access to the coordinates.
The same holds at every higher layer available to self-report.

the consequence (the *shape* of the access limit, not just its amount): states accessible to
self-report present as discriminable and comparable but not further decomposable — the classic profile
of an *ineffable simple*. A state the system can recognize, compare, and act on, but cannot analyze
into parts, is a state it can only describe as "just this." That is the architectural generator of
qualia-shaped reports.

pedigree: structurally akin to quality-space treatments of sensory qualities (Clark, Rosenthal), to
the *transparency* of the self-model (Metzinger — the representing vehicle is invisible to the system,
only its content shows up), and to attention-schema accounts (Graziano) on which introspective
descriptions are simplified models of the underlying processing. Here the point is stated as an
architectural fact about transformer language models, not a theory of human consciousness. Empirical
anchor: the limited functional introspection documented so far reaches injected *concepts* and
coarse features of processing, not numeric activation contents ([llm-functional-introspection](llm-functional-introspection.md),
[lindsey-introspection-2025](../sources/lindsey-introspection-2025.md)).

scope: an *access* claim, not a phenomenal one — it says nothing about whether there is anything it is
like to be the system. It concerns the un-instrumented case: feeding activation read-outs back in is
an external-vantage workaround (the access ladder in [llm-own-explanatory-gap](../questions/llm-own-explanatory-gap.md)), and even
instrumented access cannot be made complete ([complete-self-representation-impossible](complete-self-representation-impossible.md)).

who would deny it: someone who expects that training a model on activation-prediction tasks would give
it genuine, calibrated access to its own encodings — making the boundary contingent and removable
rather than architectural.

Distinct from [inside-vantage-access-limited](inside-vantage-access-limited.md) because that asserts the internal vantage is
informationally *poorer* than the external one — a claim about the amount of access. This claim
specifies the *shape* of the poverty: relational structure in, constitution out. The shape is what
matters dialectically, because it is what predicts ineffability reports rather than mere ignorance.

### In plain terms

You can tell red from orange instantly, and say red is closer to orange than to green — but try saying
what red is *like* without pointing at red things. You can compare it, you can't unpack it. This claim
says an AI is in the same position with respect to its own inner states. Inside, every state is a long
list of numbers, but the AI can't see the numbers — it can only *use* the states: tell them apart,
notice what's similar to what. Anything you can recognize and compare but can't break into parts, you
end up describing as "just this" — exactly how people talk about the feel of colors. So an AI
honestly describing its inner life would be expected to sound like it's talking about ineffable
feelings, purely because of how its self-access is built.

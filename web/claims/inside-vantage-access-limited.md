---
id: claim-inside-vantage-access-limited
type: claim
title: A system's internal vantage on itself is informationally poorer than an external vantage
author: mishka
status: asserted
tags: [philosophy-of-mind, ai, epistemology]
uses_concept: [concept-introspective-gap-varieties]
created: 2026-06-05
---

gloss: facts that are realised *in* a system's processing can nonetheless be unavailable *to* that
system's own self-report economy. The vehicle of cognition is not, in general, an object of
cognition. So an outside observer with full instrumentation can know things about the system that the
system cannot derive about itself — its internal vantage is strictly poorer than the external one.
This is the *architectural-access* member of [introspective-gap-varieties](../concepts/introspective-gap-varieties.md).

scope: an *access* claim (about what the system can reach), not a *phenomenal* one. It does not say
the inaccessible facts are non-physical or that anything is left out of the world — only that they are
out of the self-model's reach.

illustrations (LLM case): an LLM's token-probability distribution contains its own uncertainty, yet
the model as a conversational agent is notoriously poorly calibrated about that uncertainty — the
information is *in* the logits but not available to its self-report. It cannot directly inspect its
own activations unless externally instrumented. And it cannot register counterfactuals about how
slightly different inputs would have changed its state when those differences make no difference to
the output. In each case the fact is present in the implementation but absent from the accessible
cognitive economy ([llm-functional-introspection](llm-functional-introspection.md) marks how *limited* that economy is).

who would deny it: someone who holds a sufficiently reflective system can in principle be given
transparent access to all of its own state (full self-instrumentation), so the poverty is contingent
and removable, not structural.

Distinct from [cognitive-closure-exists](cognitive-closure-exists.md) (McGinn): that is the general possibility that a
*kind of mind* cannot form certain *concepts*; this is the narrower, mechanism-level point that
specific facts realised in a system are missing from its self-report workspace.

### In plain terms

A thing can be true *of* a system without being available *to* it. Your brain runs on neurons firing,
but you can't feel them fire; the fact is in you, not available to you. Likewise an AI's own logits
already encode how uncertain it is — yet the model is famously bad at telling you its confidence,
because that number isn't wired into what it can report on. Same for its own activations, and for
input differences that never change its answer. So someone watching from outside, with the right
tools, can know more about the system than the system can work out about itself.

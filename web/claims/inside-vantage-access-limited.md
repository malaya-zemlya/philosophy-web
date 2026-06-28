---
id: claim-inside-vantage-access-limited
type: claim
title: A system's internal vantage on itself is informationally poorer than an external vantage
headword: Limited inside vantage
author: mishka
status: asserted
tags: [philosophy-of-mind, ai, epistemology]
uses_concept: [concept-introspective-gap-varieties]
style: encyclopedia
created: 2026-06-05
---

Facts realised *in* a system's processing can be unavailable *to* that system's own self-report. The
vehicle of cognition is not, in general, an object of cognition, so an outside observer with full
instrumentation can know things about the system that the system cannot derive about itself: its
internal vantage is strictly poorer than the external one. This is the *architectural-access* member of
the [introspective-gap-varieties](../concepts/introspective-gap-varieties.md).

### Scope

An *access* claim (about what the system can reach), not a *phenomenal* one. It does not say the
inaccessible facts are non-physical or that anything is left out of the world — only that they are out
of the self-model's reach.

### Illustrations

In the language-model case the gap is concrete. A model's token-probability distribution contains its
own uncertainty, yet the model as a conversational agent is notoriously poorly calibrated about that
uncertainty — the information is *in* the logits but not available to its self-report. It cannot
directly inspect its own activations unless externally instrumented. And it cannot register
counterfactuals about how slightly different inputs would have changed its state when those differences
make no difference to the output. In each case the fact is present in the implementation but absent
from the accessible cognitive economy ([llm-functional-introspection](llm-functional-introspection.md) marks how limited that
economy is).

### Who would deny it

Someone who holds that a sufficiently reflective system can in principle be given transparent access to
all of its own state (full self-instrumentation), so the poverty is contingent and removable rather
than structural.

### Distinct from neighbours

Distinct from [cognitive-closure-exists](cognitive-closure-exists.md) (McGinn, [mcginn-1989](../sources/mcginn-1989.md)): that is the general
possibility that a *kind of mind* cannot form certain *concepts*; this is the narrower,
mechanism-level point that specific facts realised in a system are missing from its self-report
workspace.

### In plain terms

A thing can be true *of* a system without being available *to* it. Your brain runs on neurons firing,
but you can't feel them fire; the fact is in you, not available to you. Likewise an AI's own logits
already encode how uncertain it is — yet the model is famously bad at telling you its confidence,
because that number isn't wired into what it can report on. Same for its own activations, and for
input differences that never change its answer. So someone watching from outside, with the right
tools, can know more about the system than the system can work out about itself.

### See also

- [introspective-gap-varieties](../concepts/introspective-gap-varieties.md) — the catalogue; this is the architectural-access member.
- [llm-functional-introspection](llm-functional-introspection.md) — how limited the actual self-report economy is.
- [full-self-access-achievable](full-self-access-achievable.md) — the optimist denial that the poverty is structural.
- [cognitive-closure-exists](cognitive-closure-exists.md) — McGinn's concept-closure, distinguished from this access point.

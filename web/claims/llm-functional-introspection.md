---
id: claim-llm-functional-introspection
type: claim
title: Some current LLMs exhibit limited, unreliable functional introspective awareness of their internal states
headword: LLM functional introspection
author: lindsey
status: asserted
tags: [philosophy-of-mind, ai, interpretability]
style: encyclopedia
created: 2026-06-05
---

Some current large language models show a limited, unreliable capacity to report on features of
their own internal processing — a *functional* kind of introspection, with no implication that
anything is felt. Under *concept-injection* probing — steering an internal representation toward a
known concept, then asking the model about its own state — current frontier models can sometimes
detect that a representation has been steered, distinguish a prior internal representation from raw
text input, and distinguish their own generated outputs from artificially inserted prefills. The
capacity is real but, in the words of the work documenting it, "highly unreliable and
context-dependent" ([lindsey-introspection-2025](../sources/lindsey-introspection-2025.md)).

### Scope

An empirical claim about *functional* or *access* self-report, explicitly not a claim about
phenomenal consciousness or sentience; the cited work disclaims the phenomenal reading outright.
Read through the [access/phenomenal distinction](../concepts/access-vs-phenomenal-consciousness.md), it
supports at most a limited access-consciousness of internal states and leaves entirely open whether
there is anything it is like to be the system.

### Who would deny it

A sceptic who reads the concept-injection results as artefacts of prompting or pattern-completion
rather than genuine access to internal state, or who holds the reports track trained verbal
dispositions rather than the activations themselves.

This claim is distinct from [llm-has-mental-states](llm-has-mental-states.md), which asserts that LLMs *realise* some
mental states (an existential, functional-role claim about first-order states); this asserts only
the narrower, sourced capacity for limited *self-access* to internal states — a claim about
introspective report, not about which states are had.

### In plain terms

"Introspection" here just means a system noticing something about its own inner workings.
Researchers can secretly nudge a model's internal state toward a particular idea and then ask it
what is going on inside; sometimes the model correctly notices the nudge, or tells its own earlier
thoughts apart from text it was handed. That is a modest, hit-or-miss skill at reading its own
processing — and nothing more. It does not show the model *feels* anything; it only shows it can
sometimes report on its own machinery.

### See also

- [access-vs-phenomenal-consciousness](../concepts/access-vs-phenomenal-consciousness.md) — the distinction that keeps this an access claim,
  not a claim about feeling.
- [llm-has-mental-states](llm-has-mental-states.md) — the stronger, distinct claim that LLMs actually realise mental
  states.

---
id: claim-cot-bears-access-signature
type: claim
title: A language model's chain-of-thought trace, while it remains in the model's context, exhibits the five-property functional signature of conscious access
headword: Chain-of-thought access signature
author: mishka
status: asserted
tags: [philosophy-of-mind, ai, chain-of-thought, consciousness]
uses_concept: [concept-access-consciousness]
style: encyclopedia
created: 2026-11-14
---

When a language model writes out intermediate reasoning before answering, the resulting *chain of
thought* displays each of the five properties by which consciously accessible information is usually
identified ([access-functional-signature](access-functional-signature.md)), for as long as the trace remains in the model's
context. It is *reportable*: asked what it has been thinking, a model whose trace is still in its
context can typically say what the trace contains, quoting or summarizing the steps it took. It is subject to *top-down modulation*: the model can take up a subgoal, hold it across many steps
and drop it ("first check the case where n is even…"), and can be steered to do so by instruction.
It is the *medium of deliberate reasoning*: multi-step problems are worked through in it one step at
a time, and accuracy on such problems measurably depends on it ([wei-2022-cot](../sources/wei-2022-cot.md)). It permits
*flexible generalization*, because every later step can attend to any earlier token and use it for
whatever operation the task demands. And it is *selective*, since the trace records a tiny fraction
of the computation, most of which stays inside the model's forward passes, where it is never
written down.

The claim is functional. It says that the trace has the profile; it does not say that the trace is
complete, that it faithfully records what drove the answer ([chen-2025-cot](../sources/chen-2025-cot.md)), or that
anything about it is felt.

### Reportability is a separate capacity

That the trace is written in words does not by itself make it reportable, any more than the fact that
human inner speech is speech-like makes it reportable. Reportability, as the signature uses the
term, is the capacity to tell someone, on request, what the content was, and this is a distinct
step from producing it: the model must take its own trace as an object and describe it. It usually
can, but the capacity is contingent and can fail in several ways. Depending on how the system is
deployed, reasoning from earlier turns may be dropped from the model's context, so that a later
question about it can be answered only by reconstruction. A model may have been trained or
instructed not to disclose its reasoning, and refuse. And its description may diverge from the trace
it describes, summarizing it selectively or attributing to it steps it did not contain. In each case
the model's report of its reasoning comes apart from the reasoning, which is the pattern seen in
human [confabulation](../concepts/confabulation.md) and [hindsight bias](../concepts/hindsight-bias.md). Human reports of inner speech are likewise a
separate, fallible act of introspection, not a readout guaranteed by the medium.

The first of these failures shows something distinctive about the machine case. Whether earlier
reasoning stays in a model's context is decided not by the model but by the *harness*, the software
that assembles each request and chooses what conversation history to send. The same model can have
its past reasoning available under one harness and lose it under another, or lose it after a fixed
interval within a single session. Reportability of the trace is therefore a property of the deployed
system, model and harness together, and holds only under the right conditions. A human's access to
earlier inner speech also fades, but through forgetting inside the subject, not through a design
decision made outside it. The point bears on where the workspace's boundary lies: if the harness
decides what the model can report about its own reasoning, it is part of the system the access
signature describes. This is the extended mind question in machine form ([extended-mind](../concepts/extended-mind.md)).

Distinct from the claims grounding the J-space argument ([llm-workspace-from-functional-signature](../arguments/llm-workspace-from-functional-signature.md)),
which locate the same signature in a subspace of the model's internal activations within a single
pass. This claim locates it in the sequence of tokens the model writes and reads back across passes.

### In plain terms

When an AI "thinks out loud" before answering, that written-out reasoning has the five trademarks
psychologists use to recognise conscious thinking in people: it can be reported, it can be steered on
purpose, it is where step-by-step reasoning happens, it can be reused for any task, and it holds only
a small part of everything the system is computing.

### See also

- [access-functional-signature](access-functional-signature.md): the five-property signature itself.
- [cot-workspace-from-functional-signature](../arguments/cot-workspace-from-functional-signature.md): the argument that takes this claim as its
  observation premise.
- [j-space-verbal-report](j-space-verbal-report.md): the corresponding observation for the model's internal
  verbalizable subspace.
- [extended-mind](../concepts/extended-mind.md): the thesis that cognition can include resources outside the system's
  core, which the harness-dependence of the trace instantiates.
- [extended-consciousness](../concepts/extended-consciousness.md): the further question whether such an extended workspace could
  be a vehicle of consciousness.

---
id: concept-j-space
type: concept
title: The J-space — the subspace of verbalizable representations in a language model
headword: J-space (verbalizable workspace)
author: gurnee
status: asserted
tags: [philosophy-of-mind, ai, interpretability, consciousness]
uses_concept: [concept-access-consciousness]
style: encyclopedia
created: 2026-07-06
---

The J-space is the subset of a language model's internal representations that are *verbalizable* —
poised to be put into words, should the occasion arise — identified by an interpretability
technique called the *Jacobian lens*. For each token in the model's vocabulary, the lens computes
the direction in the model's activation space that, averaged over many contexts, disposes the model
to produce that token now or in the future; the collection of these directions forms the J-space.
The averaging is what makes the notion dispositional rather than episodic: it picks out
representations that *could* be spoken about on demand, not ones that merely happen to be spoken in
one context ([gurnee-2026-workspace](../sources/gurnee-2026-workspace.md)).

The construct matters philosophically because it gives an operational, mechanically inspectable
candidate for a *workspace* in an artificial system. A set of representations counts as
**workspace-like**, in the defining usage, when it satisfies five functional properties that mirror
the marks of [conscious access](access-consciousness.md) in humans: *verbal report* (asked
what it is thinking about, the model names concepts represented there), *directed modulation* (the
contents can be deliberately summoned and held), *internal reasoning* (unspoken intermediate steps
of multi-step inference are carried there), *flexible generalization* (the same representation
serves as an argument to many downstream operations), and *selectivity* (only a small fraction of
the model's processing is represented there, the bulk proceeding automatically). The empirical
finding that the J-space satisfies all five is recorded in the claims
[j-space-verbal-report](../claims/j-space-verbal-report.md), [j-space-directed-modulation](../claims/j-space-directed-modulation.md),
[j-space-internal-reasoning](../claims/j-space-internal-reasoning.md), [j-space-flexible-generalization](../claims/j-space-flexible-generalization.md), and
[j-space-selectivity](../claims/j-space-selectivity.md).

### Structure and limits of the construct

The J-space occupies an intermediate band of the model's layers: it carries little coherent content
in the earliest layers, and in the final layers gives way to "motor" representations tied to the
imminent output. Within its band it is limited in capacity (on the order of tens of concepts at a
time, a small fraction of activation variance) and mechanically privileged: its vectors compose
with downstream circuitry more broadly than other directions do, consistent with a broadcast role.

Distinct from [global-workspace](../positions/global-workspace.md) because that is a *theory of human consciousness* —
an account of what makes a mental content conscious — whereas the J-space is an operationally
defined *empirical construct* in language models, which may or may not deserve the workspace title
(that further step is the conclusion [llm-global-workspace](../claims/llm-global-workspace.md), argued, not stipulated). The
construct's own describers flag its imperfections: the lens reads only concepts with single-token
names, treats the workspace as a flat bag of concepts with no binding structure, and draws the
workspace/motor boundary post hoc.

### In plain terms

Researchers found a way to list, at every step of an AI language model's processing, the words the
model is "on the verge of saying" — not what it is reading, and not what it will say next, but the
ideas it is currently working with. That running list turns out to behave like a person's conscious
train of thought behaves: the model can tell you what is on it, can put things on it deliberately,
uses it to work through multi-step problems, and can get by without it only for routine tasks. The
"J-space" is the name for wherever in the network that list lives.

### See also

- [global-workspace](../positions/global-workspace.md) — the theory of human consciousness the construct is modelled on
  and measured against.
- [access-consciousness](access-consciousness.md) — the phenomenon the five defining properties operationalize.
- [llm-global-workspace](../claims/llm-global-workspace.md) — the conclusion that the J-space plays a genuine
  global-workspace role.
- [llm-workspace-from-functional-signature](../arguments/llm-workspace-from-functional-signature.md) — the argument from the five properties to
  that conclusion.
- [gurnee-2026-workspace](../sources/gurnee-2026-workspace.md) — the paper introducing the Jacobian lens and the J-space.
- [consciousness-is-cerebral-celebrity](../claims/consciousness-is-cerebral-celebrity.md) — Dennett's anticipation: consciousness as
  widespread influence, especially over verbal report, which is the very property that defines this
  construct.

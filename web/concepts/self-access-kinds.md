---
id: concept-self-access-kinds
type: concept
title: Kinds of self-access in a learning system
headword: Kinds of self-access
author: mishka
status: asserted
tags: [philosophy-of-mind, ai, knowledge-argument, introspection]
uses_concept: [concept-llmary, concept-knowledge-argument]
created: 2026-11-22
style: encyclopedia
---

A learning system can stand in several different relations to its own inner workings, and they are
easily run together under phrases like "knowing oneself completely." Four are worth separating:
*reading* one's own parameters as data, *introspecting* one's own current states, *simulating* oneself,
and *writing* one's own parameters. The distinctions matter most in thought experiments about
complete knowledge, such as Mary the colour scientist ([knowledge-argument](knowledge-argument.md)) and its
computational variant [llmary](llmary.md), because a verdict reached under one kind of self-access is
often silently carried over to another.

### Reading

A system *reads* itself when a description of its own parameters is presented to it as ordinary
input: a file of its weights placed in a language model's context, or papers about its architecture
in its training data. This is knowledge *about* oneself in the third person. A language model has no
other way to read its weights, because the weights do its processing and are never its object. Reading
is also limited by size, since a system cannot hold a complete copy of itself among its own contents
([complete-self-representation-impossible](../claims/complete-self-representation-impossible.md)); it can read only slices, such as the single row
of numbers that represents one token.

### Introspecting

A system *introspects* when it can register its own current internal states, for instance noticing
which activation an input has produced. Introspection is what would let a description of an inner
state be matched against the state itself. Present language models show at most a limited and
unreliable capacity of this kind, detecting some concepts deliberately injected into their
activations ([lindsey-introspection-2025](../sources/lindsey-introspection-2025.md); see [ai-introspection](../questions/ai-introspection.md)).

### Simulating

A system *simulates* itself when it uses its self-knowledge to work out what it would do or undergo in
some situation, without being in that situation. A language model that knows its own architecture and
weights could in principle calculate what its network would compute on meeting a new token, and even
the training update that would follow. Paul Churchland's suggestion that a neuroscientifically trained
Mary might imagine a cortical state "even in advance", as a musician can construct an unheard chord in
imagination, is a human version ([churchland-1985](../sources/churchland-1985.md)), and so, in a weaker form, is David Hume's
missing shade of blue, an idea of a colour never seen that the imagination supplies from the shades on
either side ([hume-treatise](../sources/hume-treatise.md), 1.1.1.10).

### Writing

A system *writes* itself when it can change its own parameters directly, putting itself into a state
that would ordinarily be produced only by some experience or training. Daniel Dennett's RoboMary is
the canonical case: a robot whose colour system is locked computes, with her self-model, the state she
would have entered on seeing a red tomato, and then makes "all the necessary adjustment and puts
herself into" that state, so that "there are no surprises for her" when she finally sees colour
([dennett-2005](../sources/dennett-2005.md)). His Swamp Mary, whose brain a lightning bolt rearranges into the same
state, reaches the result by accident rather than by work.

### Why the distinctions matter

The first three are all forms of knowing; only the fourth changes what the system is. Simulation in
particular can predict a change in full detail without producing it, since working out an update is
not undergoing it. Several disputes about Mary turn on which of the four the thought experiment
grants. Jackson's Mary, confined to her room, has reading and perhaps simulation; RoboMary has writing
as well. What follows for each of these regimes is set out in [llmary-predicted-surprise](../arguments/llmary-predicted-surprise.md).

### In plain terms

There are four different ways a mind or a machine might "know itself." It might *read* a description
of itself, as you might read your own medical file. It might *notice* what is going on inside it right
now. It might *imagine* or calculate how it would react to something, the way you might predict your
reaction to bad news. Or it might *rewire* itself directly, which humans cannot do but a robot might.
Only rewiring actually changes you. The other three, however detailed, leave you as you were.

### See also

- [mary-misimagined](../arguments/mary-misimagined.md) — the RoboMary argument that a system with complete self-knowledge
  would learn nothing on release; it assumes the writing kind of self-access.
- [full-self-access-achievable](../claims/full-self-access-achievable.md) — the claim that complete internal self-access is achievable,
  a thesis about introspection in the sense above.

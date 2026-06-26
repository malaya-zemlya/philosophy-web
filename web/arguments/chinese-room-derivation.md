---
id: argument-chinese-room-derivation
type: argument
title: The Chinese Room as a derivation from axioms — syntax is not sufficient for minds
headword: Chinese room derivation
author: searle
status: asserted
tags: [philosophy-of-mind, ai, functionalism]
premise: [claim-programs-are-syntactic, claim-minds-have-semantics, claim-syntax-insufficient-for-semantics, claim-brains-cause-minds]
concludes: claim-programs-not-sufficient-for-minds
attacks: [claim-substrate-independence]
uses_concept: [concept-chinese-room, concept-strong-weak-ai, concept-intentionality]
style: encyclopedia
created: 2026-06-25
---

This is the *formal* version of the [Chinese Room](../concepts/chinese-room.md) argument — the "derivation from
axioms" Searle gave in 1990 ([searle-1990](../sources/searle-1990.md)). Where the
[intuition-pump version](chinese-room.md) runs the thought experiment and reads a verdict off it,
this version distils the same point into a short deductive argument, so that the dispute can be located on a
single premise rather than on an intuition about a story.

### The argument

The inference is **deductive** (Searle calls it a "derivation").

1. ([programs-are-syntactic](../claims/programs-are-syntactic.md)) Programs are formal, or syntactic — defined over symbol shapes, not
   meanings. *(A1)*
2. ([minds-have-semantics](../claims/minds-have-semantics.md)) Minds have mental contents — semantics, genuine
   [aboutness](../concepts/intentionality.md). *(A2)*
3. ([syntax-insufficient-for-semantics](../claims/syntax-insufficient-for-semantics.md)) Syntax is neither constitutive of nor sufficient for
   semantics. *(A3)*

∴ ([programs-not-sufficient-for-minds](../claims/programs-not-sufficient-for-minds.md)) Implementing a program is neither constitutive of nor
sufficient for a mind *(C1)* — the denial of strong AI ([strong-weak-ai](../concepts/strong-weak-ai.md)). This `attacks`
[substrate-independence](../claims/substrate-independence.md) at its sufficiency direction: realising the right program does not deliver
the semantic side of mind.

A fourth axiom extends the result to the positive case:

4. ([brains-cause-minds](../claims/brains-cause-minds.md)) Brains cause minds through their specific causal powers. *(A4)*

∴ Any mind-producing system needs causal powers at least equivalent to brains' (C2); program-implementation
alone does not guarantee them (C3); so brains do not produce minds *by* running programs (C4) — the seed of
[biological-naturalism](../positions/biological-naturalism.md).

### The weakest premise

The whole weight rests on **A3** ([syntax-insufficient-for-semantics](../claims/syntax-insufficient-for-semantics.md)), and its status is the
crux. The standard charge is that A3 is **not an independent axiom but a restatement of the conclusion**:
the only support Searle offers for "syntax is not sufficient for semantics" is the Chinese Room thought
experiment, whose moral *is* C1 applied to the AI case — so the deductive form lends rigor without adding
*independent* force, and a functionalist who rejects C1 rejects A3 for the very same reason. Every standard
objection is, at bottom, a denial of A3: the [Systems](systems-reply.md),
[Robot](robot-reply.md), [Brain Simulator](brain-simulator-reply.md),
[Other Minds](other-minds-reply.md), [Connectionist](connectionist-reply.md), and
[Many Mansions](many-mansions-reply.md) replies each contend that syntax *plus something* (a whole
system, causal grounding, neural simulation, parallel architecture) does suffice after all. A secondary
soft spot is **A2**: eliminativists about content deny minds have the intrinsic semantics the contrast
needs ([intrinsic-derived-intentionality](../concepts/intrinsic-derived-intentionality.md)).

A1 is near-definitional and not in play; A4 is contested only on whether the mind-making feature is
biological causal power or abstract organisation.

### Relation to the intuition-pump version

This node and [chinese-room](chinese-room.md) are two presentations of one argument, kept distinct because they
have different *forms* and *attack surfaces*: the intuition-pump version is a
[thought-experiment](../../patterns/thought-experiment.md) counterexample, vulnerable at its bridge and
scope (the Systems and Robot replies as *critical questions*); this version is a deductive syllogism,
vulnerable at the truth and independence of A3. The replies in this cluster attack the derivation; many of
them apply, mutatis mutandis, to the thought-experiment version too.

### In plain terms

Searle's argument, stripped to a syllogism: (1) computer programs are just rules about symbol *shapes*; (2)
real minds actually *mean* things; (3) you can't get meaning out of shape-shuffling alone — so (conclusion)
running a program can't be enough to make a mind. Add (4) "brains make minds by their actual biology," and
you get the further moral that thinking isn't *running code* at all. The argument is airtight *if* step (3)
is true — and that's exactly the step everyone fights over. Critics say step (3) is just the conclusion in
disguise, and that syntax plus the right extra ingredient (the whole system, a body, simulated neurons)
*does* yield understanding.

### See also

- [programs-not-sufficient-for-minds](../claims/programs-not-sufficient-for-minds.md) — the conclusion (C1); the denial of strong AI.
- [syntax-insufficient-for-semantics](../claims/syntax-insufficient-for-semantics.md) — the load-bearing, contested axiom A3.
- [programs-are-syntactic](../claims/programs-are-syntactic.md), [minds-have-semantics](../claims/minds-have-semantics.md), [brains-cause-minds](../claims/brains-cause-minds.md) — the other
  axioms.
- [chinese-room](chinese-room.md) — the intuition-pump presentation of the same argument.
- [systems-reply](systems-reply.md), [robot-reply](robot-reply.md), [brain-simulator-reply](brain-simulator-reply.md),
  [other-minds-reply](other-minds-reply.md), [connectionist-reply](connectionist-reply.md), [many-mansions-reply](many-mansions-reply.md) — the
  standard objections, each a denial of A3.
- [luminous-room](luminous-room.md) — the Churchlands' meta-objection that the intuition supporting A3 is itself
  unreliable.
- [biological-naturalism](../positions/biological-naturalism.md) — Searle's positive view, grown from A4.
- [substrate-independence](../claims/substrate-independence.md) — the thesis the derivation attacks.

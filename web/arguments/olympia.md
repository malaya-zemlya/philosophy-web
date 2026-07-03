---
id: argument-olympia
type: argument
title: Maudlin's Olympia argument against computationalism about consciousness
headword: Olympia argument
author: maudlin
status: asserted
pattern: thought-experiment
tags: [philosophy-of-mind, consciousness, computation, functionalism]
premise: [claim-implementation-requires-counterfactual-structure]
attacks: [claim-substrate-independence]
uses_concept: [concept-functionalism]
style: encyclopedia
created: 2026-06-29
---

Tim Maudlin's *Olympia* argument ([maudlin-1989](../sources/maudlin-1989.md)) aims to show that no computational theory of
*phenomenal consciousness* can be correct. (Olympia is the lifelike automaton of E. T. A. Hoffmann's *The
Sandman*.) Rather than appeal to the intuition that the "wrong stuff" cannot think — a move Maudlin
explicitly disowns — it argues that three independently attractive theses form an *inconsistent triad*, so
that a computationalist about consciousness must abandon one of them. The target is the computational
construal of [the substrate-independence thesis](../claims/substrate-independence.md); it leaves
non-computational physical theories of consciousness untouched.

### The inconsistent triad

- *Sufficiency.* Running the right program suffices for the conscious state: any system that performs the
  computation π (on input *r*) thereby supports the phenomenal state φ.
- *Necessity.* Being a genuine computer running a *nontrivial* program is necessary for φ — a system that
  merely runs through a sequence of states without the right computational structure is not conscious.
- *Supervenience* (Maudlin's principle). Two systems engaged in precisely the same physical activity
  through a time support the same modes of consciousness. Equivalently: introducing an inert object that
  has no causal interaction with a system can neither create nor destroy its phenomenal states, because an
  occurrent experience is wholly realised in the activity going on during it.

Maudlin builds a single machine that makes these three collide.

### The machine: Klara and Olympia

Start with *Klara*, a genuine computer running the conscious-making program π. Klara may be built of
anything — Maudlin imagines a clockwork so vast it would fill the solar system; her tape is a row of water
troughs, each full or empty for one bit. Record the exact run Klara performs on the particular input *r*
that (by hypothesis) produces the conscious state φ, and reorder the troughs into the sequence that run
visits.

Now build *Olympia*. She is nothing but an **armature** that travels along the reordered troughs,
filling and emptying each one to reproduce, step for step, the recorded run. Fed *r*, Olympia's physically
active events are identical to Klara's. But the bare armature, blindly replaying one fixed sequence,
computes only a *trivial constant function*; it has none of the counterfactual structure π requires. So by
*Necessity*, the bare armature is not conscious.

To supply the missing counterfactual structure — *without adding any activity to the actual run* — Maudlin
fits each trough with a latched **float**, set to the water level that trough has at that step of the
recorded run, and chains the floats to **N + 2 further copies of Klara, each frozen ("blocked") in one of
π's machine states by a small block of wood jamming its gears**. Were the input ever to differ from *r*,
the relevant float would move, release its block, and that copy of Klara would wake up and take over the
computation (shutting the armature down). With this apparatus Olympia genuinely *implements* π: across the
whole space of possible inputs her states stand in exactly the dispositional relations π demands
([implementation-requires-counterfactual-structure](../claims/implementation-requires-counterfactual-structure.md)). Yet on the actual run *r* not one float
moves, not one blocked Klara stirs, and the chains hang slack: the entire added "clockwork universe" sits
physically inert.

### The bind

- By *Sufficiency*, Olympia-with-machinery — which really does implement π on *r* — is conscious, enjoying φ.
- By *Necessity*, the bare armature alone — a trivial constant function — is not conscious.
- But the bare armature and Olympia-with-machinery have *identical actual physical activity*: the added
  machinery never acts. By *Supervenience* they must be alike in consciousness.

The three verdicts cannot all stand. Whether φ is present turns, for the computationalist, on counterfactual
structure that is carried entirely by *physically inert* parts — and Maudlin's supervenience principle says
inert, causally disconnected parts cannot make that difference. So consciousness cannot derive from
computational structure; an acceptable computational theory of consciousness is not possible.

### The movie analogy

Maudlin's image: Olympia creates the illusion of being Klara-in-action the way a film creates motion from
still frames. Each frozen copy of Klara is a single frame — an inert object holding one captured moment of
her operation — and the armature's passage briefly "lights up" each frame's dispositional structure in
sequence, as a projector's lamp animates a strip of stills. "The problem with computationalism is that it
does not contain the conceptual resources to distinguish the flickering illusion from reality."

### Weakest premise

The supervenience principle — that only *actually active*, causally engaged events, not standing
unexercised dispositions, can make a difference to experience. The computationalist's natural escape is to
reject it: counterfactual dispositions are categorical physical facts present throughout the run, so the
bare armature and Olympia-with-machinery are *not* doing "the same thing" after all. Maudlin presses this
with cases in which counterfactual structure varies while actual activity plainly does not:

- *The pinball illustration* (due to Kevin Kelly): set a ball rolling through a board of pins; remove pins
  it never touches on that path. The trajectory, the energy transfers, the physicist's explanation are all
  unchanged — only the counterfactuals (what would have happened on a different push) differ.
- *Argument by addition.* Fit each blocked Klara with a *second* block that never touches anything but
  would jam the gears if the first block were removed. The counterfactuals now fail, so by computationalism
  Olympia is no longer conscious — though nothing physically active has changed.
- *Argument by subtraction.* Let the float-chains slowly rust until they would snap rather than unblock a
  machine. At some unmarked instant the counterfactual support lapses and, by computationalism, the
  toothache winks out — with no physical event to mark the passage.

The cost of rejecting supervenience, Maudlin adds, is steep: the very same intuition powers the standard
*pro*-computationalist thought experiment of gradually replacing neurons with silicon ("why should it
matter whether the impulse runs on a neuron or on a wire?"). A computationalist who lets an untouched,
inert block decide presence or absence of experience forfeits the intuition that made substrate-neutrality
attractive in the first place.

### Scope and conclusion

The argument is aimed at *occurrent* conscious states — datable events such as a sensation — but Maudlin
extends the construction to intelligence and linguistic understanding: shift the blocks a few centimetres
and Olympia "solves the problem stupidly," or produces the words without the understanding. He reaches, by
a consistency argument, the very conclusion John Searle sought by other means — that having a mind is *not
merely a matter of instantiating a program* — while rejecting Searle's "fancy instantiation" route through
the wrong-stuff intuition. Olympia does not show that minds must be "wet and squishy": a silicon or even a
hydraulic brain might, for all the argument says, be conscious. It shows only that consciousness cannot
supervene on *computational* structure, so "some other level beside the computational must be sought" — the
counterfactuals that constitute a program must be carried by the system's actual causal activity, not by
inert scaffolding.

### In plain terms

Imagine a computer running a program that (suppose) makes it conscious. Film the exact physical steps it
takes on one particular run, then build a dumb machine — Olympia — that just *replays* those steps, like a
player piano reproducing a recording. On that run Olympia physically does the very same things the computer
did. But Olympia can't cope with any *different* input, so computer scientists say she isn't really
*running the program* — running a program means being set up to respond correctly to all the inputs you
*might* get, not just the one you did.

So bolt on extra machines that *would* kick in and do the right thing if the input were different — but
that, on this actual input, just sit there, frozen, never moving. Now Olympia counts as running the
program, yet literally nothing that actually happens has changed; the add-ons are dead weight on this run.
Here's the squeeze. Did adding silent, never-used machines switch consciousness *on*? That seems crazy —
how could whether anyone's home depend on gadgets that never do anything? (Maudlin sharpens it: rust
through the cables connecting them and consciousness would supposedly blink out at some moment nothing
physical marks.) But if those idle machines *didn't* switch consciousness on, then "running the program"
was never what made the computer conscious to begin with. Either way, the idea that consciousness just *is*
running the right computation is in trouble. Maudlin's picture: Olympia is a *movie* of a mind — a strip of
frozen frames briefly lit up one after another — and computationalism can't tell the flickering movie from
the real thing.

### See also

- [substrate-independence](../claims/substrate-independence.md) — the computational sufficiency thesis this argument attacks (in its
  computational construal).
- [implementation-requires-counterfactual-structure](../claims/implementation-requires-counterfactual-structure.md) — the counterfactual account of
  implementation Olympia exploits and turns into a liability.
- [functionalism](../concepts/functionalism.md) — the broader view computationalism is a species of.
- [decomposition-indeterminacy](decomposition-indeterminacy.md) — a companion pressure on whether "which computation a physical
  system runs" is objective enough to ground a mind.
- [chinese-room](chinese-room.md) — the other classic anti-computationalist thought experiment; Maudlin reaches
  its conclusion (a program is not enough for a mind) but rejects its wrong-stuff route, arguing instead
  from the supervenience of consciousness on actual physical activity.

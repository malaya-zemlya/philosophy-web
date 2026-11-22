---
id: argument-isomorphic-feedforward-zombie
type: argument
title: Isomorphic feed-forward zombies — a behaviorally identical twin can have Φ = 0 against the original's Φ > 0
headword: Isomorphic feed-forward zombie
author: hanson
status: asserted
tags: [philosophy-of-mind, consciousness, iit, functionalism, thought-experiment]
pattern: thought-experiment
attacks: [claim-consciousness-is-integrated-information]
supports: [claim-substrate-independence]
uses_concept: [concept-functionalism]
created: 2026-09-30
style: encyclopedia
---

The *isomorphic feed-forward zombie* argument shows that [integrated information theory's](../positions/integrated-information-theory.md)
measure $\Phi$ can be pulled apart from a system's behavior entirely: two systems can compute exactly
the same function, visit exactly the same sequence of states, and still be rated oppositely for
consciousness — one with $\Phi > 0$, its twin with $\Phi = 0$ — because the only thing that differs
between them is which internal wiring realizes the identical behavior. If nothing about what a system
*does* can settle whether $\Phi$ assigns it experience, the argument concludes, $\Phi$ is not tracking
consciousness ([hanson-walker-2019](../sources/hanson-walker-2019.md)).

### The construction

Take a small feedback circuit $Y$: two XNOR gates and one XOR gate, wired so a signal flows
bidirectionally between two of the components. $Y$ contains genuine feedback, and on IIT's own
calculation $\Phi(Y) > 0$ for every state at which $\Phi$ is defined. Using techniques related to the
Krohn–Rhodes decomposition theorem for finite automata, $Y$ can be rewritten as a *feed-forward*
circuit $Y'$ — no component's output feeds back into anything upstream of it — that is *isomorphic*
to $Y$: $Y'$ has the same number of states, the same global state-transition diagram, and produces
the same output for every input, differing from $Y$ only by a relabeling of which bit-pattern names
which internal state. Because $Y'$ has no feedback, $\Phi(Y') = 0$. $Y'$ is, in the terminology IIT
itself uses for such cases, a *philosophical [zombie](../concepts/philosophical-zombie.md)*: behaviorally
and functionally indistinguishable from $Y$, yet (per IIT) wholly without experience.

### The inference

The move is a thought-experiment reductio.

1. *Scenario.* $Y$ and $Y'$ are isomorphic: identical input–output function and identical global
   state-transition diagram, differing only in (a) a relabeling of internal states and (b) whether
   the realizing circuit contains feedback.
2. *What the identity entails.* [Consciousness is integrated information](../claims/consciousness-is-integrated-information.md) entails
   $\Phi(Y) > 0$ and $\Phi(Y') = 0$ — so $Y$ has some experience and $Y'$, despite behaving identically
   in every respect, has none.
3. *Bridge.* A difference that is nothing but a relabeling of internal states — one with no behavioral
   or functional consequence whatsoever — cannot be what decides whether a system has any experience
   at all.
4. *Conclusion.* The identification of consciousness with $\Phi$ is false, or at least not the kind of
   thing that could be read off a system from the outside in the way IIT claims; $\Phi$ is sensitive to
   a functionally arbitrary feature of description, not to anything that could ground a phenomenal
   difference.

### The weakest premise

Premise 3, the bridge. An IIT proponent can decline to find this absurd, exactly as Tononi declined
to find [the expander-grid reductio](../sources/aaronson-2014.md) absurd: IIT's whole point is that
*intrinsic* cause-effect structure, not relabeling-invariant input-output behavior, is what
consciousness is, so a theory that respects this distinction is doing its job, not failing it. The
reply only has force, though, by owning the conclusion that behaviorally and functionally identical
systems — down to every state transition — can differ in whether there is anything it is like to be
them, with the difference turning on facts (which wires happen to be feedback, how states happen to be
labeled) that no observation of the system's behavior could ever reveal even in principle.

### Related moves

[Aaronson's](../sources/aaronson-2014.md) original reductio against IIT used behaviorally inert, densely-wired
grids to get unboundedly large $\Phi$ from trivial computation; in a comment reply he informally
anticipated the present point — that a large-$\Phi$ system can be behaviorally duplicated by a
small-$\Phi$ one. This argument is that anticipation made rigorous and minimal, with an explicit
circuit and an exact isomorphism rather than a general simulation claim. [The unfolding
argument](../sources/doerig-2019.md) generalizes the same move to any recurrent-vs-feed-forward
pair and to causal-structure theories of consciousness as a class, rather than to one worked example
against $\Phi$ specifically.

### In plain terms

Picture two machines that act *exactly* alike: fed the same inputs, they pass through the same
sequence of internal states (just with different names tagged to those states) and produce the same
outputs, every time. One machine has a loop where a wire feeds back into an earlier part of the
circuit; the other has been rewired, with no loop, to behave identically anyway. Integrated
information theory says the looped one is conscious and the un-looped one is not — even though
nothing about what either machine *does* could ever tell you which is which. That is the problem: if
two systems that behave identically in every way, state for state, can be assigned wildly different
amounts of consciousness, then whatever $\Phi$ is measuring, it does not look like consciousness
itself, since consciousness is usually taken to be exactly the kind of thing that should make *some*
actual difference.

### See also

- [consciousness-is-integrated-information](../claims/consciousness-is-integrated-information.md) — the identity this argument attacks.
- [integrated-information-theory](../positions/integrated-information-theory.md) — the position built on that identity.
- [substrate-independence](../claims/substrate-independence.md) — supported: if behaviorally identical systems must share
  conscious status, consciousness cannot hinge on substrate-level wiring details with no behavioral trace.
- [functionalism](../concepts/functionalism.md) — the rival view (mental states individuated by causal role) this
  argument's bridge premise leans on.
- [philosophical-zombie](../concepts/philosophical-zombie.md) — the concept the feed-forward twin instantiates, adapted to a
  finite-state circuit rather than a whole brain.
- [hanson-walker-2019](../sources/hanson-walker-2019.md) — the paper constructing the circuit and proving the isomorphism.
- [aaronson-2014](../sources/aaronson-2014.md) — the informal precursor and the companion expander-grid reductio against IIT.
- [doerig-2019](../sources/doerig-2019.md) — the unfolding argument, generalizing the same move to causal-structure theories at large.

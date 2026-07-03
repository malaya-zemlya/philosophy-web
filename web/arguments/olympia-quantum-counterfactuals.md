---
id: argument-olympia-quantum-counterfactuals
type: argument
title: The quantum counterfactuals objection — unexercised possibilities have physical effects, and quantum runs have no trace to unroll
headword: Quantum counterfactuals objection
author: mishka
status: asserted
tags: [philosophy-of-mind, consciousness, computation, functionalism, quantum-mechanics]
attacks: [argument-olympia]
responds_to: [argument-olympia-trace-specialization]
supports: [claim-substrate-independence]
style: encyclopedia
created: 2026-07-02
---

The *quantum counterfactuals objection* attacks the deepest premise of Maudlin's
[olympia](olympia.md) — the supervenience principle, on which only *actually exercised* activity can
matter to experience and causally untouched machinery cannot — by pointing out that this principle
is classical physics elevated to metaphysics. In quantum mechanics, unexercised possibilities have
measurable effects on actual outcomes; there are laboratory experiments in which a computer's
output is obtained on runs where the computer, in the standard sense, never ran. The objection has
two prongs. The first denies that "two systems engaged in precisely the same physical activity" is
a physically fundamental classification, undercutting the supervenience premise directly. The
second observes that the Klara→Olympia construction consumes a classically recorded execution
trace, and a quantum-coherent computation *has* none — so against a computationalism whose programs
exploit quantum interference, Olympia cannot even be built. In the vocabulary of the
thought-experiment pattern, the objection raises **CQ1 (coherence)** — the scenario's description
smuggles in classical assumptions that our physics falsifies — and **CQ6 (scope)**: at most the
argument touches classically traceable computation in the classical limit, a nomologically
parochial result rather than the advertised conceptual impossibility.

The move runs:

1. The supervenience premise rests on a classical picture of causation: what happens is a single
   definite history, and structure that history never touches is causally idle. Maudlin's pinball
   illustration — remove the pins the ball never hits and nothing about the actual run changes —
   states the picture exactly.
2. Quantum mechanics falsifies the picture. Which paths are *open* affects where a single particle
   lands even when it "takes" only one; an interferometer can detect a live bomb via a photon that
   never interacts with it, the bomb's unexercised disposition shifting the observed statistics
   (Elitzur & Vaidman, [1993](../sources/elitzur-vaidman-1993.md)); and the output of a quantum computer
   can be extracted from runs on which the computer did not run — *counterfactual computation*,
   theorized by Mitchison and Jozsa ([2001](../sources/mitchison-jozsa-2001.md)) and realized in the
   laboratory by Hosten and colleagues ([2006](../sources/hosten-2006.md)).
3. So systems differing only in never-triggered machinery are *not*, at the fundamental level,
   "engaged in precisely the same physical activity": the machinery is part of the total physical
   configuration, and physical law permits such differences to matter to what actually happens.
4. Independently: the Klara→Olympia transformation presupposes that the conscious-making run has a
   classically recordable trace — which cell, which value, at every step. A quantum-coherent run
   has no such trace: recording each step's value is a measurement that destroys the interference
   the computation exploits, and copying the state instead is barred by the no-cloning theorem
   (Wootters & Zurek, [1982](../sources/wootters-zurek-1982.md)).

∴ The trilemma fails twice over against a physically literate computationalism: its supervenience
premise is at best a classical approximation, not a principle fit to constrain theories of
consciousness; and its central construction cannot be mounted at all against computation that
exploits coherence. What survives is at most a contingent claim about the classical limit.

### Counterfactuals with causal teeth

The pinball illustration is the supervenience premise's whole evidential base, and quantum
mechanics reverses its verdict at the scale where physics is fundamental. Shrink the pinball to a
photon and the board to an interferometer, and removing pins the ball "never touches" *changes
where it lands*: interference depends on the whole configuration of open paths, not on the one path
a classical eye would say was taken. The Elitzur–Vaidman bomb tester
([1993](../sources/elitzur-vaidman-1993.md)) sharpens this into a working instrument: a photon sent
through an interferometer can reveal the presence of a live bomb — one that any interaction would
detonate — *without* the interaction occurring. The bomb never fires; its mere capacity to absorb
is what destroys the interference and shows up in the detectors. Mitchison and Jozsa
([2001](../sources/mitchison-jozsa-2001.md)) generalized the trick from bombs to computers, and Hosten
and colleagues ([2006](../sources/hosten-2006.md)) performed it: a quantum search yields its answer on
runs in which, by the experiment's own bookkeeping, the computer did not run. "What would have
happened but didn't" is, in our physics, a working part of what does happen.

Deutsch has pressed the general moral for decades: interference phenomena reveal the causal
relevance of unactualized histories ([1997](../sources/deutsch-1997.md)), and constructor theory
([2013](../sources/deutsch-2013.md)) proposes outright that fundamental physics be *formulated* in
counterfactuals — which transformations are possible and impossible — with the actual as a
derivative special case. One need not buy the whole program to take the lesson: a metaphysical
principle that quarantines counterfactuals from causal relevance is not neutral bookkeeping; it is
a substantive physical thesis, and apparently a false one.

### The supervenience premise reconsidered

Maudlin needs the claim that the bare armature and Olympia-with-machinery are "engaged in precisely
the same physical activity", so that whatever differs between them is causally idle. At the
fundamental level this is simply not so: the blocked Klaras, floats, and chains are part of the
total configuration, and the system's physical evolution — its Hamiltonian, its space of
interfering histories — differs with their presence. Restate the supervenience principle in honest
quantum terms ("two systems with the same physical state and evolution support the same
experience") and it no longer classifies the two machines as duplicates, so it can no longer force
the contradiction. Retreat to a coarse-grained reading ("the same *classical* activity") and the
premise ceases to be an evident metaphysical truth and becomes a choice of description — exactly
the point in dispute, since the computationalist holds that dispositional structure is part of what
a system is physically doing. The rhetorically strongest moves of the paper fare worst here: the
"argument by subtraction" insists that as the chains rust through, counterfactual support lapses
"with no physical event to mark the passage" — but there is *always* a physical difference as a
chain rusts; what there fails to be is a classical, macroscopic event. And Maudlin's own closing
demand — that the counterfactuals constituting a program be "carried by the system's actual causal
activity, not by inert scaffolding" — is one quantum mechanics happily grants: dispositions *are*
carried by actual, categorical physical structure. That was the reply the pinball was built to
kill, and the pinball does not survive quantization.

### No trace to unroll

The second prong turns on the reconstruction in [olympia-trace-specialization](olympia-trace-specialization.md). Its
*Effectiveness* corollary — Olympia is computable from the program and input alone — holds because
a classical run is *measurement-transparent*: it can be watched, logged, and replayed without being
changed. Quantum computation is defined by the failure of exactly this property. Its power comes
from interference among computational paths, which exists only so long as no record exists —
anywhere — of which path was taken; logging each step's value is a measurement that collapses the
run, and the no-cloning theorem (Wootters & Zurek, [1982](../sources/wootters-zurek-1982.md)) forecloses
the workaround of copying the machine's state for later replay. A quantum Klara therefore has no
trace log Λ, and without Λ there is no reordered tape, no float presets, no placement of blocked
copies: *the Klara→Olympia transformation is a classical-only operation*. Since Deutsch
([1985](../sources/deutsch-1985.md)) it has been a commonplace that the theory of computation is a branch
of physics — what counts as running a program is fixed by physical law, not a priori. Maudlin's
argument quantifies over "any machine running the conscious-making program π" but its construction
silently assumes π's runs are classically recordable; a computationalism whose programs exploit
coherence sits outside the argument's reach from the first page.

### The weakest premise

The objection's exposure is **decoherence**. Olympia's blocked copies are warm, macroscopic
clockwork; the interference terms their presence contributes to the armature's run are suppressed
beyond any physical relevance, and the classical description of the machine is for every practical
purpose exact. A defender of Maudlin will say the supervenience premise was never meant as
fundamental law, only as a truth about the quasiclassical domain where Olympia (and every brain)
lives — and a coarse-grained principle is all the trilemma needs, provided the systems it compares
really are decohered. The first prong must then show that this retreat to coarse-graining begs the
question rather than merely idealizes, and that a principle demoted from metaphysical necessity to
excellent approximation can no longer bear the argument's modal weight ("*no* computational theory
of consciousness *can* be correct"). The second prong has the mirror exposure: if the
conscious-making program is effectively classical — as most computationalists themselves hold about
brains — then its trace *is* recordable, Olympia is buildable against it, and the prong protects
only a computationalism prepared to wager, with Penrose ([1994](../sources/penrose-1994.md)), that
consciousness exploits quantum coherence — a wager most computationalists refuse. The honest net
effect is a demotion, not a refutation: Maudlin's conclusion shrinks from a conceptual impossibility
to a contingent claim about classically traceable computation in the classical limit — while the
argument's presentation, and its claim to constrain *any* possible computational theory, trade on
the stronger reading.

### In plain terms

Quantum physics contains a genuine surprise about "what didn't happen": it can leave fingerprints
on what did. There is a famous scheme — the bomb tester ([1993](../sources/elitzur-vaidman-1993.md)) —
in which a single particle of light reveals that a bomb is live *without touching it*: the bomb
never goes off, nothing hits it, and yet the pattern at the detectors is different because the bomb
*would have* absorbed the light. Physicists have even run a computer this way, reading off the
answer from rounds in which the computer never ran ([2006](../sources/hosten-2006.md)). Now recall what
Maudlin's machine ([olympia](olympia.md)) is built on: the claim that standby machinery which never
does anything obviously cannot matter to what the system experiences. Physics itself says that
principle is not a deep law — in our world, machinery that never fires can still shape what
happens. And there is a second, separate problem: Maudlin's whole recipe starts by *filming* the
computer's run, step by step, so as to replay it. A quantum computation cannot be filmed — peeking
at each step destroys it, and physics forbids photocopying its state ([1982](../sources/wootters-zurek-1982.md)).
So if a mind's program used quantum effects, the replay machine could never be built in the first
place. The fine print: for big, warm machinery — and probably for brains — these quantum effects
are absurdly tiny, so the objection doesn't show Maudlin's machine misfires in practice. It shows
his key principle is a rule of thumb about medium-sized objects, not a law of nature — and an
argument claiming to rule out every possible computational theory of mind needs a law, not a rule
of thumb.

### See also

- [olympia](olympia.md) — the thought experiment attacked; the objection lands on its supervenience
  premise and on the scope of its conclusion.
- [olympia-trace-specialization](olympia-trace-specialization.md) — the formal reconstruction whose *Effectiveness*
  corollary the second prong bounds to classical, measurement-transparent computation.
- [olympia-recording-objection](olympia-recording-objection.md) — the companion objection: it grants the classical
  setting and relocates the experience to the recording run, where this objection denies the
  setting's physics; the two can be run together.
- [substrate-independence](../claims/substrate-independence.md) — the thesis defended; quantum mechanics, far from threatening
  it, supplies the categorical physical basis for dispositional structure.
- [implementation-requires-counterfactual-structure](../claims/implementation-requires-counterfactual-structure.md) — the account of implementation whose
  counterfactuals quantum physics renders categorical and causally active rather than inert.

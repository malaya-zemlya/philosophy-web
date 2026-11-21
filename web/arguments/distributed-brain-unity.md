---
id: argument-distributed-brain-unity
type: argument
title: A brain is a slow, massively parallel distributed system, and in such systems global consistency must be engineered, so phenomenal unity is a costly achievement rather than a default
headword: Distributed-brain argument
author: mishka
status: asserted
pattern: analogy
tags: [philosophy-of-mind, consciousness, unity, distributed-systems, neuroscience]
premise: [claim-brain-parallel-slow-signalling, claim-distributed-consistency-is-costly]
concludes: claim-phenomenal-unity-is-engineered
attacks: [claim-unity-thesis]
supports: [claim-unity-harder-with-less-myelination, claim-subject-unity-graded-by-integration]
uses_concept: [concept-unity-of-consciousness, concept-postdiction, concept-binding-problem]
style: encyclopedia
created: 2026-11-21
---

This argument asks what it would take for a brain to have a unified experience at a moment, given
how a brain is built. Its answer is that a brain is a distributed system of the kind computer
scientists know well, and in such systems a single consistent state of the whole is never free. It
has to be engineered, at a cost, and it fails when the system is under strain. If that is right,
the unity of consciousness cannot be a default or necessary feature of experience. It is an
achievement of a well-functioning brain.

### The argument

The inference form is analogy, from distributed computing systems to the brain.

1. The brain is a massively parallel network whose signals travel slowly relative to the timescale
   of experience ([brain-parallel-slow-signalling](../claims/brain-parallel-slow-signalling.md)).
2. In a distributed system with significant signal delays, a globally consistent state does not
   arise by default but must be engineered at a cost
   ([distributed-consistency-is-costly](../claims/distributed-consistency-is-costly.md)).
3. A phenomenally unified moment of experience requires something like a globally consistent state
   of the brain: the contents being experienced together must be brought into one integrated state.
4. Therefore phenomenal unity is not a default feature of a brain but a costly engineered
   achievement, which holds only while the brain functions well
   ([phenomenal-unity-is-engineered](../claims/phenomenal-unity-is-engineered.md)).

The conclusion directly contradicts the [unity-thesis](../claims/unity-thesis.md), which says that a subject's
simultaneous experiences are *necessarily* unified. A unity that depends on good functioning can
fail, so it cannot be necessary.

### The analogy in detail

The model case is Google's Spanner database, which gives globally consistent transactions across
data centres on different continents ([corbett-2012](../sources/corbett-2012.md)). It manages this only by engineering
a bound on how far apart its clocks can be, using GPS receivers and atomic clocks, and then making
each transaction wait out that uncertainty before committing. Consistency is bought with hardware
and latency. In the general case, separate processes have no shared "now" at all, only a partial
order of events, unless a protocol constructs one ([lamport-1978](../sources/lamport-1978.md)).

The analogy maps onto the brain at several points:

- **Paying in latency.** The brain seems to pay something like Spanner's price. In
  [postdiction](../concepts/postdiction.md), what a person experiences at one moment depends on input arriving up to a
  tenth of a second later, as if the brain withheld an integrated version until late data had come
  in. This resembles a commit-wait.
- **Partition.** The CAP theorem states that when a network is cut, a system must give up either
  consistency or availability ([gilbert-lynch-2002](../sources/gilbert-lynch-2002.md)). Cutting the corpus callosum, the main
  link between the hemispheres, is literally a partition, and engineers call the corresponding
  failure "split-brain". Split-brain patients behave as if their brains keep availability (both
  hemispheres go on acting) and give up consistency (a single unified view).
- **Degraded links.** A system with slower or noisier links has to settle for weaker consistency,
  with subsystems acting on different versions of the world. Fatigue is a plausible case. In
  sleep-deprived but behaviourally awake rats, small patches of cortex go briefly offline in a
  sleep-like way, more often the longer the animal has been awake ([vyazovskiy-2011](../sources/vyazovskiy-2011.md)). This
  matches the first-person report that in fatigue, anxiety or severe ADHD, experience presents as
  interacting sub-processes with no orchestrating centre ([degraded-states-orchestratorless](../claims/degraded-states-orchestratorless.md)).

### Consequences

If unity is engineered, it should come in degrees, cost effort and fail under load, which supports
the view that subject unity is graded by integration
([subject-unity-graded-by-integration](../claims/subject-unity-graded-by-integration.md)). It also yields a developmental prediction. Myelin
is what makes long-range signals fast, and myelination continues into early adulthood, so unity
should be harder to achieve in less myelinated brains
([unity-harder-with-less-myelination](../claims/unity-harder-with-less-myelination.md)).

### The weakest premise

Premise 3 is the weakest, and the analogy pattern's relevance question lands on it: is phenomenal
unity the kind of thing that needs global consistency? Two replies press it.

The first is that "engineered" does not mean "absent". On global workspace theory, a content becomes
conscious only when it is broadcast across the brain. Then everything conscious is, by that very
fact, integrated, and unity holds for conscious contents even though the integrating is costly.
On this reply the argument shows only that *fewer* contents are conscious in a tired brain, not that
the conscious ones fall apart. The argument then depends on whether there is phenomenal experience
outside the integrated core. Ned Block's thesis that phenomenal consciousness *overflows* access
says that there is ([block-2007](../sources/block-2007.md)). If he is right, a strained brain can have experienced
but unintegrated content, which is real disunity.

The second reply is that the brain may not need consistency of Spanner's strength. Daniel Dennett
and Marcel Kinsbourne argued that the brain never settles the true order of events at all. It
*represents* timing without *synchronising* the processes that carry the representations
([dennett-kinsbourne-1992](../sources/dennett-kinsbourne-1992.md); see [time-represented-vs-time-of-representing](../concepts/time-represented-vs-time-of-representing.md)).
That supports the argument's claim that there is no global snapshot. It also lets the defender of
unity say that experience can *seem* unified at far less cost than actual synchronisation would
require.

### In plain terms

The brain is not one processor with one clock. It is a huge network of processes running in parallel
and passing messages that take a noticeable fraction of a second to arrive. Engineers who build
systems like that, such as global databases spread across continents, know that getting all the parts
to agree on what is happening *right now* never comes for free. Google's Spanner database manages it
only with atomic clocks and deliberate waiting. The argument says the same must be true of the brain:
if your experience at a moment feels like one whole, that is because your brain is doing expensive
work to make it so, and that work can fail when you are exhausted, stressed, or your brain's wiring
is slower. So the unity of experience is not guaranteed. It is something a healthy brain achieves.

### See also

- [unity-of-consciousness](../concepts/unity-of-consciousness.md) — the kinds of unity at issue, and the clinical cases usually
  used to test the unity thesis.
- [binding-problem](../concepts/binding-problem.md) — the narrower problem of how separately processed features are joined
  into one perceived object.

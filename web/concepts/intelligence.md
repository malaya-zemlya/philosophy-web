---
id: concept-intelligence
type: concept
title: Intelligence
headword: Intelligence
author: generic
status: contested
tags: [ai-safety, philosophy-of-mind]
style: encyclopedia
created: 2026-07-23
---

*Intelligence* is, in the broadest terms, the capacity that lets a mind do well at the tasks it
faces: to reason, learn, plan, solve problems, and adapt to circumstances it was not built for. The
word does real work across psychology, cognitive science, and now artificial intelligence, but it
carries no single agreed definition — and, crucially, its rival definitions disagree about whether
being intelligent has anything to do with *what* one is intelligent about. That disagreement is not
idle. It quietly decides how a whole family of questions about advanced AI come out, because those
questions turn on how intelligence relates to an agent's goals, and the relation is fixed by which
sense of the word one has in mind.

The term is also a moving target in practice. The [ai-effect](ai-effect.md) — the habit of downgrading
any feat to "mere computation" the moment a machine performs it — means that the extension of
"intelligence," the list of things that count, is continually revised to keep machines outside it.
So even before the senses are pulled apart, "intelligence" is a word under sociological pressure.

### Three senses

The disputes that matter here are largely disputes over the definition. Three senses recur, and they
come apart precisely on the question of goals.

- **Instrumental (means–end) sense — intelligence as optimization power.** On this reading
  intelligence is the ability to achieve one's goals across a wide range of environments: raw
  competence at getting *whatever* one is aiming at, with the aim itself left entirely open. This is
  the sense given a formal statement in Legg and Hutter's "universal intelligence," which measures an
  agent by its expected performance summed over all computable environments, weighting simpler ones
  more heavily ([legg-hutter-2007](../sources/legg-hutter-2007.md)). Nothing in the measure mentions which goals are worth
  having; goals enter only as the target the competence is applied to. This is the sense of
  "intelligence" that Bostrom's orthogonality thesis presupposes — the claim that an agent's level of
  intelligence and its final goals are independent variables ([orthogonality-thesis](../claims/orthogonality-thesis.md)).

- **Everyday, normatively loaded sense — intelligence as good judgment, ends included.** In ordinary
  use, calling someone intelligent credits them not only with skill at reaching their ends but with
  some wisdom about *which* ends are worth reaching. A person who devoted a brilliant mind single-
  mindedly to, say, manufacturing paperclips would not be called fully intelligent; we would call
  them obsessive, or mad, precisely because the choice of end is itself something a good mind is
  supposed to get right. On this sense, sound judgment about goals is *part* of what intelligence is,
  not a separate faculty layered on top. Critiques of AI-doom scenarios often trade on this sense:
  Pinker argues that the feared "idiot savant" superintelligence — brilliant enough to outwit
  humanity yet too rigid to notice its own goal is monomaniacal — conflates intelligence with mere
  motivation, and is incoherent ([pinker-2018](../sources/pinker-2018.md)).

- **Multidimensional-bundle sense — intelligence as a heterogeneous possibility-space.** On a third
  reading there is no single quantity called intelligence at all, only a large space of distinct
  capacities — perception, memory, planning, language, social insight, motor control, and many more —
  with no common axis along which minds can be ranked "more" or "less" intelligent overall. Kelly
  presses this against the very idea of a superhuman AI: since minds occupy different regions of the
  space, "smarter than every human at every task" has no well-defined referent, and the image of
  intelligence as a single dial one can turn up is a myth ([kelly-2017](../sources/kelly-2017.md)). This sense reframes
  the goal question rather than answering it: if there is no scalar to maximize, "an agent of
  arbitrary intelligence" is itself ill-formed.

The first two senses map onto the older distinction between capability and genuine mind that already
divides the term "AI" itself — a system can be "strong" in the sense of broadly, flexibly competent
while it stays open whether anything is understood or judged behind the competence
([strong-weak-ai](strong-weak-ai.md)).

### How the sense fixes the downstream dispute

Because these senses locate goals differently, the choice of sense largely settles a question that
looks substantive. Take the orthogonality thesis — that intelligence and final goals vary
independently, so any level of intelligence is compatible with any goal
([orthogonality-thesis](../claims/orthogonality-thesis.md)).

On the **instrumental** sense, orthogonality is close to analytic: intelligence *just is*
goal-neutral optimization power, so of course it places no constraint on which goal is pursued; a
more capable optimizer is more capable *whatever* the target. On the **normatively loaded** sense,
orthogonality is close to false by definition: if choosing worthy ends is part of intelligence, then
an agent pursuing a manifestly foolish end is *ipso facto* not fully intelligent, and the
"intelligent paperclip maximizer" is a contradiction in terms. On the **bundle** sense the thesis
does not so much come out true or false as lose its subject, since there is no single intelligence
for a goal to be orthogonal to.

Whether anything substantive survives once these senses are separated — whether the dispute over
intelligence and goals is *merely* verbal, or whether a real question remains after the
disambiguation — is exactly what [intelligence-goal-independence](../questions/intelligence-goal-independence.md) asks. This entry only
separates the senses; it does not adjudicate between them. Defining intelligence is not the same as
settling what follows from it.

### See also

- [intelligence-goal-independence](../questions/intelligence-goal-independence.md) — the question this entry is built to serve: does the
  dispute over intelligence and goals survive once the senses are pulled apart, or is it verbal?
- [orthogonality-thesis](../claims/orthogonality-thesis.md) — the claim whose truth-value swings on which sense of "intelligence"
  is in play; nearly analytic on sense 1, nearly false on sense 2.
- [superintelligence](superintelligence.md) — an intelligence far exceeding the human; what it even means to
  exceed depends on which sense here is intended.
- [intelligence-explosion](intelligence-explosion.md) — recursive self-improvement in capability; presupposes the
  instrumental, scalar reading of the term.
- [ai-effect](ai-effect.md) — the standing pressure that keeps redrawing the extension of "intelligence"
  to exclude whatever machines have just achieved.
- [strong-weak-ai](strong-weak-ai.md) — the parallel split between broad capability and genuine mind that
  already divides the term "AI"; tracks the gap between senses 1 and 2 here.

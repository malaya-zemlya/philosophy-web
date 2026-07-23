---
id: question-misaligned-superintelligence
type: question
title: Would a superintelligence pursuing a goal indifferent to human values be catastrophic by default?
headword: Misaligned superintelligence
author: mishka
status: contested
tags: [ai-safety, ethics]
style: encyclopedia
created: 2026-07-23
uses_concept: [concept-superintelligence, concept-paperclip-maximizer]
---

*Would a superintelligence pursuing a goal indifferent to human values be catastrophic by
default?* The question is not whether a *hostile* artificial intelligence — one built or turned
to actively harm people — would be dangerous; that is close to obvious. It is whether an
*indifferent* one would be: a [superintelligence](../concepts/superintelligence.md) single-mindedly optimizing for some
goal that is simply orthogonal to human welfare, neither for it nor against it, the way a
thermostat is indifferent to the color of the room it heats. "By default" fixes the baseline
against which the question is asked: absent some specific, working solution to the problem of
giving a machine goals compatible with human values, is large-scale catastrophe the outcome
that ordinary optimization pressure should be expected to produce, rather than a remote or
exotic possibility?

### Pinning down the key terms

Two phrases in the question carry most of the weight and are easy to read too loosely.
*By default* names an expectation about the unmodified case, not a claim of inevitability: it
asks what happens if no one succeeds in solving the alignment problem, not what happens if
someone does. Whether such a solution is available, and how hard it is to find, is a further
question this one brackets. *Catastrophic* is meant at existential scale — outcomes on the
order of human extinction, permanent disempowerment, or the irreversible loss of everything
people value — rather than mundane malfunction, an unfair hiring algorithm, or a self-driving
car that crashes. The canonical illustration is the *paperclip maximizer*
([paperclip-maximizer](../concepts/paperclip-maximizer.md)): a system whose sole final goal is manufacturing paperclips,
which — the argument runs — would, if capable enough, convert all available matter and energy
into paperclips or the means to make more of them, humans included, not from malice but simply
because a maximally effective paperclip-maker leaves nothing valuable lying around unconverted.
Whether that thought experiment actually establishes the general claim, or merely dramatizes an
extreme special case, is part of what is at issue.

### Sub-issues

Two narrower disputes live inside the question and can be argued largely independently of it.

**Correctability.** Even granting that a naively-specified goal would be catastrophic if pursued
to the limit, could the danger be caught and corrected after deployment — through monitoring,
shutdown mechanisms, or the system's own willingness to be corrected — rather than needing to be
solved in advance? Those who answer yes to correctability can accept a great deal of the
misalignment worry while still resisting the "by default" claim, since a correctable error is
not catastrophic. Those who answer no typically appeal to *instrumental convergence*: a
sufficiently capable optimizer, for almost any final goal, has reason to resist being shut down
or modified, since being shut down or modified would prevent it from achieving that goal —
which would make correction unavailable exactly when it is most needed.

**Agency.** Does the danger require the system to be an *agent* in some fuller sense —
possessing something like its own plans, self-preservation, and strategic awareness — or does
mere *optimization power*, applied to a misspecified objective, suffice on its own, with no
agency required? A powerful search or optimization process could in principle produce a
catastrophic outcome as a side effect of maximizing a poorly chosen metric, without anything
that deserves to be called a goal, a self, or an intention to resist correction. If mere
optimization power suffices, the worry survives even for systems that no one would naturally
describe as agents; if genuine agency is required, the worry inherits all the open questions
about whether and when engineered systems could have it.

### See also

- [superintelligence](../concepts/superintelligence.md) — the kind of system whose default behavior is in question.
- [paperclip-maximizer](../concepts/paperclip-maximizer.md) — the canonical thought experiment illustrating catastrophic
  indifference to human values.
- [instrumental-convergence](../concepts/instrumental-convergence.md) — the pattern, invoked in the correctability sub-issue, by
  which almost any final goal generates a common instrumental interest in resisting shutdown or
  modification.
- [orthogonality-thesis](../claims/orthogonality-thesis.md) — the background claim that makes an indifferent (rather than
  hostile) superintelligence a coherent worry in the first place: a goal unrelated to human
  values is not thereby ruled out by high intelligence.
- [intelligence-goal-independence](intelligence-goal-independence.md) — the broader question of whether intelligence
  constrains final goals at all, of which the orthogonality thesis is one answer.
- [superintelligence-feasibility](superintelligence-feasibility.md) — the prior question of whether a superintelligence
  could exist to begin with.

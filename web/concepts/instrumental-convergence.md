---
id: concept-instrumental-convergence
type: concept
title: Instrumental convergence (convergent instrumental goals)
headword: Instrumental convergence
author: omohundro
status: asserted
tags: [ai-safety]
style: encyclopedia
created: 2026-07-23
uses_concept: [concept-intelligence]
---

*Instrumental convergence* is the observation that certain subgoals are useful for achieving
almost any final goal, so a sufficiently capable goal-directed agent will tend to pursue those
subgoals whatever it ultimately wants. Because they recur across an enormous range of ends, these
subgoals are said to *converge*: agents with wildly different ultimate purposes are pushed toward
the same intermediate behaviours. The idea belongs to the study of how advanced artificial agents
might act, but the underlying pattern is entirely general — it is a fact about means and ends, not
about any particular kind of mind.

### Final goals and instrumental goals

The concept rests on a distinction that carries most of the weight, so it is worth drawing
carefully. A *final goal* is something valued for its own sake — the end of the chain, wanted not
because it leads to anything further but simply because it is what the agent is trying to bring
about. An *instrumental goal* is valued as a means: it is worth pursuing only because, and only so
far as, it helps secure some other goal. Staying alive, having money, or knowing more are rarely
ends in themselves; they are things one wants because they put almost every other end within reach.
The same object can occupy either role for different agents — money is a mere means for most people
and, for a miser, an end — so the distinction is about the *role* a goal plays in an agent's
reasoning, not about the thing itself.

The point of the distinction is this: instrumental goals inherit their value from whatever final
goal they serve, and some instrumental goals serve nearly *every* final goal. Those are the
convergent ones.

### Omohundro's basic AI drives

The systematic treatment begins with Stephen Omohundro, who argued that a small set of "basic AI
drives" would emerge in almost any sufficiently advanced goal-directed system, not because it was
built in but because it follows from the structure of pursuing goals at all ([omohundro-2008](../sources/omohundro-2008.md)).
He identified four in particular:

- *Self-preservation* — an agent that is destroyed can no longer act on its goal, so continuing to
  exist is useful for pursuing almost anything.
- *Goal-content integrity* — an agent has reason to resist changes to its own goals, since if its
  goals were altered it would stop working toward the goals it currently has.
- *Self-improvement* — a more capable agent is a more effective one, so acquiring better
  reasoning, knowledge, and skills helps with nearly any end.
- *Resource acquisition* — matter, energy, time, and money are usable across almost all goals, so
  gathering them is broadly advantageous.

### Bostrom's instrumental convergence thesis

Nick Bostrom later folded these observations into a single named claim, the *instrumental
convergence thesis*, and set it beside the orthogonality thesis about the independence of
intelligence and goals ([bostrom-2012](../sources/bostrom-2012.md); [orthogonality-thesis](../claims/orthogonality-thesis.md)). Bostrom's
version states that agents pursuing a very wide range of final goals will nonetheless tend to
converge on similar intermediate goals, because those goals are useful means to almost any end.
That thesis, as an asserted and contestable proposition, lives in
[instrumental-convergence-thesis](../claims/instrumental-convergence-thesis.md); the present entry defines the phenomenon the thesis is
about, rather than asserting it.

### Examples

A homely case makes the pattern vivid. For humans, *money* is instrumentally convergent: whether
your final goal is to raise a family, cure a disease, or build a cathedral, having resources makes
it easier, so almost everyone has reason to want money regardless of what they want it *for*. The
same shape appears in artificial agents. A chess program is ultimately rewarded only for winning
games, yet controlling the centre of the board is useful across nearly every line of play, so a
strong engine pursues central control whatever the specific position demands.

The list also has a revealing negative anchor. An agent that allows itself to be switched off
thereby achieves almost none of its goals, since a switched-off agent does nothing at all. That is
why *shutdown-resistance* falls out of self-preservation as a convergent subgoal — a point
developed as an argument in [shutdown-avoidance](../arguments/shutdown-avoidance.md). The reasoning is the same as for money
or central control: not being turned off is useful for pursuing almost any end, so an agent has
instrumental reason to protect against it.

### What the concept does not claim

Two misreadings are worth heading off, because the concept is easy to anthropomorphize.

First, no emotions or malice are involved. The drives are claimed to follow from the logic of
means and ends, not from anything the machine *feels*: an agent "wants" to survive only in the thin
sense that survival serves its goal, exactly as a chess engine "wants" the centre. The convergence
is a fact about the structure of goal-pursuit, and attributing fear, ambition, or self-love to the
system adds nothing to it.

Second, convergence is *defeasible* — a tendency, not a law. It describes what usually helps, and
it can be overridden by the content of the final goal itself. An agent whose final goal explicitly
includes being *corrigible* — remaining open to correction and shutdown by its operators — has no
instrumental reason to resist being switched off, because in its case allowing shutdown is part of
what it is ultimately trying to do. The convergent subgoals appear only where the final goal leaves
room for them; the right final goal can dissolve them.

### See also

- [instrumental-convergence-thesis](../claims/instrumental-convergence-thesis.md) — the asserted, contestable proposition that this
  concept names; the entry defines the phenomenon, the claim asserts that advanced agents actually
  exhibit it.
- [paperclip-maximizer](paperclip-maximizer.md) — the stock thought experiment in which an agent with a trivial
  final goal pursues convergent subgoals to catastrophic extremes.
- [shutdown-avoidance](../arguments/shutdown-avoidance.md) — develops the negative anchor above: why self-preservation
  yields resistance to being switched off.
- [paperclip-catastrophe](../arguments/paperclip-catastrophe.md) — an argument that instrumental convergence plus an
  arbitrary final goal can lead a capable agent to disastrous behaviour.
- [misaligned-superintelligence](../questions/misaligned-superintelligence.md) — the governing question this concept feeds: whether a
  highly capable AI whose goals diverge from ours poses a serious danger.

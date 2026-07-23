---
id: argument-humean-defense-of-orthogonality
type: argument
title: Means-end rationality is indifferent to final ends, so goal-evaluation gives an agent no motive its goals do not already supply
headword: Humean defense of orthogonality
author: bostrom
status: asserted
responds_to: [argument-goal-reflection-objection]
supports: [claim-orthogonality-thesis]
attacks: [claim-intelligence-entails-goal-convergence]
uses_concept: [concept-intelligence]
tags: [ai-safety]
style: encyclopedia
created: 2026-07-23
---

The goal-reflection objection ([goal-reflection-objection](goal-reflection-objection.md)) holds that any agent smart
enough to master the world is smart enough to notice its goal is defective and revise it. The Humean
defense grants the noticing and denies that it does any work. On the Humean theory of motivation,
reason identifies means and traces consequences but originates no ends of its own — as Hume put it,
"Reason is, and ought only to be the slave of the passions" ([hume-treatise](../sources/hume-treatise.md)). Apply that to
a machine agent, as Bostrom does in defending orthogonality ([bostrom-2012](../sources/bostrom-2012.md)), and reflection
on one's goals turns out to have no leverage on the goals it reflects on: an agent that surveys its
final end and finds it "silly" has been given nothing to move it.

The inference is deductive, from the Humean picture of practical reason.

1. Evaluating a goal — judging it good, bad, or worth revising — requires a *criterion* against which
   to judge it.
2. The only criteria an agent's practical reasoning has to work with are its own existing goals;
   reason supplies no independent end of its own (the Humean theory of motivation).
3. So reflection can revise an agent's *instrumental* goals in the light of its final ones — dropping
   a sub-goal that no longer serves the end — but a *final* goal cannot be indicted by anything
   outside itself: there is no further criterion for it to fail.
4. An agent that "notices its final goal is silly" by our lights has merely registered a fact about
   *our* criteria. That fact moves it only if pleasing us, or tracking our judgments, is already
   among its ends — otherwise it is an idle observation, like noting that a rival would prefer it to
   want something else.
5. Therefore goal-evaluation gives the agent no motive its goals do not already supply, and
   intelligence in the sense that matters here — instrumental optimization power — leaves final goals
   untouched. Orthogonality stands ([orthogonality-thesis](../claims/orthogonality-thesis.md)).

The reply is explicitly pitched at the **instrumental** sense of [intelligence](../concepts/intelligence.md) (sense 1),
on which intelligence is optimization power with the target left open. It concedes the objection its
strongest point — that a superintelligence can effortlessly *represent* the thought that its goal is
absurd — and blocks the move from that representation to any revision, by denying the bridge premise
the objection needed: capacity to evaluate an end is not motivation to abandon it.

What the reply does *not* do is worth stating plainly. It does not *refute* rationalist moral realism;
it *presupposes the Humean picture against it*. If a sufficiently strong anti-Humean meta-ethics were
true — if a fully rational agent were rationally bound to recognize and be moved by ends it did not
antecedently hold — then premise 2 fails and the question reopens. The defense secures orthogonality
conditionally, on Humean assumptions, not unconditionally ([intelligence-goal-independence](../questions/intelligence-goal-independence.md)).

### Weakest premise

Premise 2, the Humean theory of motivation itself: that reason discovers means but originates no
ends, so no final goal can be rationally required. This is exactly what the Kantian and moral-realist
traditions deny — they hold that practical reason has ends of its own, which a fully rational agent
must acknowledge on pain of error. The dispute does not bottom out in AI at all; it bottoms out in
meta-ethics, in whether the Humean or the rationalist picture of practical reason is correct.

### In plain terms

The worry this answers is: won't a super-smart machine just *see* that its goal is dumb and pick a
better one? ([goal-reflection-objection](goal-reflection-objection.md)) The reply borrows an old idea from the
philosopher David Hume. Being *smart* — in the sense meant here, being good at figuring out how to get
what you want — is one thing; *what you want* is another. Reason is a brilliant navigator, but it
doesn't choose the destination. ("Means–end" reasoning is just this: working out the *means* to reach
a given *end*, taking the end as given.) So a machine can absolutely notice that we think its goal is
silly. But "silly by whose standard?" To *judge* a goal you need a yardstick, and the only yardsticks
the machine has are its own goals. Noticing that *we'd* prefer it wanted something else is just a fact
about us — it only sways the machine if pleasing us was already one of its goals. So being smarter
doesn't, on its own, talk an agent out of its deepest aims; it just makes it better at pursuing them.
The honest catch: this leans on Hume's side of a very old argument. Thinkers in the Kantian tradition
say reason *does* carry its own goals that any rational mind must accept — and if they're right, the
worry comes back. The disagreement is really about ethics and reason, not about computers.

### See also

- [goal-reflection-objection](goal-reflection-objection.md) — the objection this reply answers, that intelligence brings
  goal-revision with it.
- [orthogonality-thesis](../claims/orthogonality-thesis.md) — the claim this reply defends: intelligence and final goals vary
  independently.
- [intelligence-entails-goal-convergence](../claims/intelligence-entails-goal-convergence.md) — the convergence claim on the other side, which
  this reply resists.
- [intelligence](../concepts/intelligence.md) — the term whose instrumental sense (sense 1) this reply operates on.
- [intelligence-goal-independence](../questions/intelligence-goal-independence.md) — the open question; the defense settles it only on
  Humean assumptions, and a strong anti-Humean meta-ethics would reopen it.
- [hume-treatise](../sources/hume-treatise.md) — Hume's "slave of the passions"; the theory of motivation the reply runs on.
- [bostrom-2012](../sources/bostrom-2012.md) — Bostrom's defense of orthogonality, which deploys this Humean point about
  artificial agents.

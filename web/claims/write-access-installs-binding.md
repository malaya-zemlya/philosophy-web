---
id: claim-write-access-installs-binding
type: claim
title: A learner with write access to its own representations can install, without the encounter, the binding a first encounter would provide, so that the encounter then brings no surprise
headword: Self-installed binding
author: mishka
status: asserted
tags: [ai, philosophy-of-mind, knowledge-argument]
uses_concept: [concept-self-access-kinds, concept-llmary]
created: 2026-11-22
style: encyclopedia
---

A system that can change its own parameters directly can do for itself what a first encounter would
have done. A language model that has calculated the update it would undergo on first meeting a token
can, if it is able to write its own weights, apply that update in advance. Its representation of the
token then carries the token's role before the token ever arrives, and when it does arrive the model
predicts it well, so that there is no large error and nothing left to learn from it.

The idea is Daniel Dennett's. His Locked RoboMary, whose colour system is locked, computes with her
self-model the state she would have entered on seeing a red tomato and then puts herself into it, after
which "there are no surprises for her" ([dennett-2005](../sources/dennett-2005.md)). Dennett's own target is the
conclusion that Mary would learn nothing. The present claim states the mechanism that makes this
true for RoboMary, the self-installation of the binding described in
[first-encounter-adds-binding](first-encounter-adds-binding.md), and so limits it to learners that have write access.

The binding need not be installed in the very representation the encounter would have trained. A
model whose token row cannot be changed could instead train its other parameters to treat that
particular untrained vector as the token, which is the analogue of RoboMary working around her locked
colour system. Either way the installation is an act of writing, not of knowing, and it is the act
that the kinds of self-access in [self-access-kinds](../concepts/self-access-kinds.md) separate from reading and simulation.

### In plain terms

A robot that can rewire itself could set itself up in advance exactly as meeting something new would
have set it up. Then, when the new thing finally comes, it is not surprised at all, because it has
already made the change the encounter would have made. Knowing about the change is not enough; the
robot has to actually make it.

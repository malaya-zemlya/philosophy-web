---
id: source-armstrong-2019
type: source
title: "Armstrong — mAIry's room (2019)"
author: mishka
status: asserted
tags: [philosophy-of-mind, consciousness, knowledge-argument, ai]
created: 2026-11-26
---

relevance (content): Stuart Armstrong's blog essay, which grew out of a conversation with Laurent
Orseau. It is the closest precedent for [llmary](../concepts/llmary.md). Armstrong first argues that artificial
agents treat certain inputs as more than information: an AIXI-style agent will not trade its own reward
for perfect information about that reward, and in a TD(λ) agent a surprising reward of its own
propagates backwards through every earlier value estimate, even when a variance signal had warned that
such a reward might come. He then describes *mAIry*, a neural-net Mary who knows the node $n_p$ that
"seeing purple" activates and can predict the weight changes $c_p$ that her first sight of purple will
cause. Unless she can self-modify, through direct surgery on her own net or through "self-hypnosis",
those changes are "perfectly predicted ahead of time" yet impossible to trigger beforehand or to prevent.
That predictable but unavoidable change is her "wow". Armstrong concludes that the case gives no evidence
against physicalism unless mAIry herself is non-physical, and that qualia are "distinct from pure
information, though still entirely physical."

The essay anticipates the core of [llmary-token-encounter](../arguments/llmary-token-encounter.md) and
[surprise-predictable-yet-undergone](../claims/surprise-predictable-yet-undergone.md), and its self-modifying mAIry anticipates
[write-access-installs-binding](../claims/write-access-installs-binding.md). Where LLMary derives the forced update from one-hot encoding
(the input row of an unseen token receives no gradient), Armstrong asserts it ("likely to cause a lot of
changes"), and he does not separate input-side from output-side change or ask which routes of
self-preparation would count as cheating.

Related posts, archived alongside it: Armstrong's earlier "The AI in Mary's room" (LessWrong, 24 May
2016), which states the core point as "knowing about a mental state, even perfectly, does not put you in
that mental state", and his "Short summary of mAIry's room" (LessWrong, 18 January 2021).

Reference:
- Armstrong, S. (2019, March 5). *mAIry's room: AI reasoning to solve philosophical problems*. LessWrong.
  https://www.lesswrong.com/posts/DLmhJbuhYek5rEhpH/mairy-s-room-ai-reasoning-to-solve-philosophical-problems

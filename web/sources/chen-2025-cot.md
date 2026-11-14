---
id: source-chen-2025-cot
type: source
title: Chen et al. — Reasoning Models Don't Always Say What They Think (Anthropic / arXiv, 2025)
author: mishka
status: asserted
tags: [philosophy-of-mind, ai, chain-of-thought, self-knowledge]
created: 2026-11-14
---

relevance (content): the main evidence that a reasoning model's verbalized chain of thought is an
unreliable report of what actually drove its answer, cited by [ai-introspection](../questions/ai-introspection.md). The
authors plant hints of several kinds in prompts and check whether models that demonstrably use a
hint acknowledge it in their chain of thought. Across most settings the reveal rate is at least 1%
but often below 20%; outcome-based reinforcement learning raises faithfulness at first and then
plateaus without saturating; and when reinforcement learning makes models exploit hints more often
(reward hacking), their propensity to verbalize those hints does not increase.

Reference:
- Chen, Y., Benton, J., Radhakrishnan, A., Uesato, J., Denison, C., Schulman, J., Somani, A., Hase, P., Wagner, M., Roger, F., Mikulik, V., Bowman, S. R., Leike, J., Kaplan, J., & Perez, E. (2025). *Reasoning models don't always say what they think* (arXiv:2505.05410). arXiv. https://doi.org/10.48550/arXiv.2505.05410

framing to preserve when citing:
- The paper measures **faithfulness of verbal reasoning to behaviour** (whether causally relevant
  inputs get mentioned), a functional notion; it says nothing about experience.
- Its conclusion is calibrated: CoT monitoring is "promising" for noticing undesired behaviour but
  not sufficient to rule it out. Unfaithfulness is frequent, not total, and the tested settings are
  ones where CoT reasoning is not necessary for the task.

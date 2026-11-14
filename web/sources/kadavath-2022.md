---
id: source-kadavath-2022
type: source
title: "Kadavath et al. — Language Models (Mostly) Know What They Know (Anthropic / arXiv, 2022)"
author: mishka
status: asserted
tags: [philosophy-of-mind, ai, calibration, self-knowledge]
created: 2026-11-14
---

relevance (content): an early empirical study of whether language models can assess their own
knowledge, cited by [ai-introspection](../questions/ai-introspection.md). Large models are shown to be well calibrated on
multiple-choice and true/false questions when posed in the right format; they can then evaluate
their own proposed answers by estimating *P(True)*, the probability that a given answer is correct,
and can be trained to predict *P(IK)*, the probability that "I know" the answer to a question before
proposing one. P(IK) partly generalizes across tasks but is less well calibrated on new domains, and
it rises appropriately when relevant source material is placed in context.

Reference:
- Kadavath, S., Conerly, T., Askell, A., Henighan, T., Drain, D., Perez, E., Schiefer, N., Hatfield-Dodds, Z., DasSarma, N., Tran-Johnson, E., Johnston, S., El-Showk, S., Jones, A., Elhage, N., Hume, T., Chen, A., Bai, Y., Bowman, S., Fort, S., … Kaplan, J. (2022). *Language models (mostly) know what they know* (arXiv:2207.05221). arXiv. https://doi.org/10.48550/arXiv.2207.05221

framing to preserve when citing:
- The results concern **calibration and self-evaluation of outputs**, measured behaviourally from
  the model's probabilities and answers. They show reliable *knowledge about one's own knowledge* in
  a functional sense, not introspective access to internal states and not anything about experience.
- The "(mostly)" is meant: calibration depends on question format, and P(IK) generalizes imperfectly
  out of distribution.

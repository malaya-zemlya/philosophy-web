---
id: source-binder-2024
type: source
title: "Binder et al. — Looking Inward: Language Models Can Learn About Themselves by Introspection (ICLR 2025; arXiv 2024)"
author: mishka
status: asserted
tags: [philosophy-of-mind, ai, introspection, self-knowledge]
created: 2026-11-14
---

relevance (content): a behavioural test for privileged self-access in language models, cited by
[ai-introspection](../questions/ai-introspection.md). Introspection is operationalized as a model's acquiring knowledge of
itself that is not derivable from its training data: if model M1 can introspect, it should predict
its own behaviour in hypothetical scenarios better than a model M2 trained on M1's ground-truth
behaviour. Fine-tuned GPT-4, GPT-4o and Llama-3 models show this self-prediction advantage on simple
tasks, and keep predicting themselves accurately after their behaviour is deliberately changed by
further fine-tuning. The advantage fails on more complex tasks and on tasks requiring
out-of-distribution generalization.

Reference:
- Binder, F. J., Chua, J., Korbak, T., Sleight, H., Hughes, J., Long, R., Perez, E., Turpin, M., & Evans, O. (2025). Looking inward: Language models can learn about themselves by introspection. In *International Conference on Learning Representations (ICLR 2025)*. https://arxiv.org/abs/2410.13787

framing to preserve when citing:
- "Introspection" here is a **functional, behavioural** notion (privileged self-prediction); the
  paper does not claim the models have subjective experience, though it discusses relevance to
  questions of moral status.
- The evidence is limited to **simple, in-distribution tasks**; the authors report failure on
  harder ones.

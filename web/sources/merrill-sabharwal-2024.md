---
id: source-merrill-sabharwal-2024
type: source
title: Merrill & Sabharwal — The Expressive Power of Transformers with Chain of Thought (ICLR 2024)
author: mishka
status: asserted
tags: [ai, chain-of-thought, computational-complexity]
created: 2026-11-14
---

relevance (content): a formal result on why chain of thought helps. A transformer that must answer
in a single forward pass performs a bounded amount of sequential computation, whatever its width.
Letting it generate intermediate tokens and read them back adds genuine serial computation, and the
gain depends on how many steps it may take: a logarithmic number adds little, a linear number lets it
solve inherently sequential problems it otherwise cannot (such as recognizing all regular languages),
and a polynomial number makes it equivalent to polynomial-time computation. Grounds the mechanism
appealed to in [cot-illuminates-inner-speech](../claims/cot-illuminates-inner-speech.md) and the recurrence point in
[cot-workspace-from-functional-signature](../arguments/cot-workspace-from-functional-signature.md).

Reference:
- Merrill, W., & Sabharwal, A. (2024). The expressive power of transformers with chain of thought. In *The Twelfth International Conference on Learning Representations*. https://arxiv.org/abs/2310.07923

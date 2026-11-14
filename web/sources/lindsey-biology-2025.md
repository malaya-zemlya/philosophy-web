---
id: source-lindsey-biology-2025
type: source
title: Lindsey et al. — On the Biology of a Large Language Model (Anthropic / Transformer Circuits Thread, 2025)
author: mishka
status: asserted
tags: [philosophy-of-mind, ai, interpretability, self-knowledge]
created: 2026-11-14
---

relevance (content): the circuit-tracing evidence that a model's account of its own processing can
come apart from the processing itself, cited by [ai-introspection](../questions/ai-introspection.md). Using attribution
graphs on Claude 3.5 Haiku, the paper studies a model that correctly computes 36+59 = 95 through
parallel pathways (a rough estimate of the sum's magnitude combined with a precise computation of the
final digit), yet, when asked how it did it, describes the schoolbook carry-the-one algorithm. The
authors read this as a capability the model lacks "metacognitive" insight into: explanations and
internal methods are learned by different processes. A separate case study on entity recognition
finds a default "can't answer" circuit that is inhibited by features for known entities, so that the
model in effect tracks whether it knows something; some hallucinations are traced to a misfire of
this inhibition, when a familiar name suppresses refusal although the specific fact is unknown.

Reference:
- Lindsey, J., Gurnee, W., Ameisen, E., Chen, B., Pearce, A., Turner, N. L., Citro, C., Abrahams, D., Carter, S., Hosmer, B., Marcus, J., Sklar, M., Templeton, A., Bricken, T., McDougall, C., Cunningham, H., Henighan, T., Jermyn, A., Jones, A., … Batson, J. (2025, March 27). *On the biology of a large language model*. Transformer Circuits Thread. https://transformer-circuits.pub/2025/attribution-graphs/biology.html

framing to preserve when citing:
- The paper's "metacognitive" vocabulary is in scare quotes: it describes **functional mechanisms**
  (circuits that gate answering on familiarity), and makes no claim about awareness or experience.
- The arithmetic case shows that **one** self-explanation is confabulated relative to the mechanism;
  it does not show that all model self-reports are unreliable.
- The authors caution that the identified features and connections "capture only a part of the
  story"; attribution graphs give partial, model-specific explanations.

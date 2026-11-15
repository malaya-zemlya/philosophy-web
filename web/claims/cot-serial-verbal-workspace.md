---
id: claim-cot-serial-verbal-workspace
type: claim
title: A language model's chain of thought plays the functional role of a serial verbal workspace analogous to human inner speech
headword: Chain of thought as serial workspace
author: mishka
status: asserted
tags: [philosophy-of-mind, ai, chain-of-thought, consciousness, inner-speech]
uses_concept: [concept-access-consciousness, concept-j-space]
style: encyclopedia
created: 2026-11-14
---

The chain of thought a language model writes while reasoning functions as a *serial verbal
workspace*: a stream of language-formatted contents, produced one at a time, each of which is made
available to all subsequent processing and can be reported, steered and reasoned with. In this
respect it plays the part that inner speech plays in human thinking, the running verbal commentary
in which people rehearse, plan and work through problems step by step.

The claim is about functional role only. It is silent on whether anything is experienced, and it
does not say that the trace is the model's *only* workspace or that it faithfully records everything
that drives the model's answers. In particular it is compatible with the claim that the model also
has a global workspace *within* each forward pass ([llm-global-workspace](llm-global-workspace.md)). Because what stays in the model's context is fixed by the harness that runs it, the serial workspace is a property of the deployed system, model and harness together ([cot-bears-access-signature](cot-bears-access-signature.md)). Human access
consciousness is not confined to inner speech either: perceptual contents, images and wordless
intentions are accessible without being verbalized. The natural picture is of two levels, a fast
broadcast medium inside each pass and a slower serial stream built on top of it, which is close to
Daniel Dennett's description of the conscious stream as a "Joycean machine", a serial, language-like
virtual machine running on parallel hardware ([dennett-1991](../sources/dennett-1991.md)).

The claim would be denied by those who hold that a workspace must be an internal state of the system,
so that a written record the system reads back is at most a memory aid used by the real workspace,
and by recurrent-processing theorists who regard looping through output as no substitute for
recurrence within the processor itself.

### See also

- [cot-workspace-from-functional-signature](../arguments/cot-workspace-from-functional-signature.md): the argument that establishes this claim.
- [llm-global-workspace](llm-global-workspace.md): the complementary claim about the workspace inside each forward
  pass.
- [cot-illuminates-inner-speech](cot-illuminates-inner-speech.md): the further suggestion that the computational value of
  chain of thought explains why humans have inner speech.
- [global-workspace](../positions/global-workspace.md): the theory supplying the role description.
- [extended-consciousness](../concepts/extended-consciousness.md): the thesis that the basis of consciousness can extend beyond the
  processor, which a harness-dependent workspace puts to the test.
- [extended-cognition-not-extended-consciousness](extended-cognition-not-extended-consciousness.md): the claim that a workspace's extending
  beyond the model would not by itself make its contents conscious.

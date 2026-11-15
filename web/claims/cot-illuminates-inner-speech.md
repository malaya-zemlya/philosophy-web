---
id: claim-cot-illuminates-inner-speech
type: claim
title: The computational value of chain of thought in language models is evidence that human inner speech serves to add serial recurrence to otherwise parallel, bounded-depth processing
headword: Chain of thought and inner speech
author: mishka
status: asserted
tags: [philosophy-of-mind, ai, chain-of-thought, inner-speech, cognitive-science]
uses_concept: [concept-access-consciousness]
style: encyclopedia
created: 2026-11-14
---

Language models reason markedly better when they write out intermediate steps before answering
([wei-2022-cot](../sources/wei-2022-cot.md)), and there is a precise account of why. A transformer answering in a single
forward pass can carry out only a bounded amount of step-by-step computation, however large it is;
writing intermediate results as tokens and reading them back turns it into a serial, recurrent
machine that can solve problems it otherwise cannot ([merrill-sabharwal-2024](../sources/merrill-sabharwal-2024.md)). The claim
is that this case sheds light on why human beings think in inner speech. The brain, too, does most
of its work in massively parallel processes that settle quickly. Inner speech gives it a loop in
which an intermediate result is put into words, held, and fed back in as input to the next round of
processing, extending what a fast, parallel and relatively shallow system can do.

### Relation to existing accounts

The idea that language is a tool for thought, and not only for communication, is old. Lev Vygotsky
traced inner speech to children's self-directed speech, internalized as a means of regulating their
own activity ([vygotsky-1986](../sources/vygotsky-1986.md)). Alan Baddeley's *phonological loop* treats silent rehearsal
as a way of keeping material in working memory ([baddeley-1992](../sources/baddeley-1992.md)). Andy Clark argued that
words augment the computational powers of an associative brain much as pen and paper augment
arithmetic ([clark-1998](../sources/clark-1998.md)), and Daniel Dennett described the conscious stream as a serial
"Joycean machine" running on parallel neural hardware ([dennett-1991](../sources/dennett-1991.md)). What the
language-model case adds is a concrete, controllable system in which the benefit of a serial verbal
loop can be measured, together with a formal account of what the loop adds to the system's
computational power. It moves the question of what inner speech is *for* from introspective
plausibility toward a mechanism that can be specified and tested.

### Scope and limits

The claim concerns function: what inner speech does, which may help explain why it develops and
persists. It is not a claim about evolutionary history, and it is compatible with Vygotsky's view
that inner speech is acquired in childhood from social speech; a capacity can be culturally acquired
and still owe its value to the computational role described here. It also has to respect the human
evidence that inner speech *facilitates* working memory, planning and task-switching without being
*essential* to them. Blocking inner speech experimentally impairs such tasks without abolishing
them, and people differ greatly in how much inner speech they report
([alderson-day-fernyhough-2015](../sources/alderson-day-fernyhough-2015.md)). The claim therefore predicts that inner speech will matter
most for inherently sequential problems, those whose steps must be done in order, and least for
problems a parallel system can solve in a single pass. That parallels the formal result for
transformers.

The analogy has a weak point. Brains are recurrent throughout, unlike a single transformer pass, so
the bottleneck inner speech would relieve is not the same as the one chain of thought relieves. A
defender can reply that what matters is serial recurrence over *discrete, reusable* contents, a
specific kind of loop that ordinary neural recurrence need not supply, but the reply carries part of
the claim's weight.

### In plain terms

AI language models get much better at hard problems when they "think out loud" in writing first,
and computer scientists can prove why: writing down each step and reading it back lets the system do
step-by-step work it couldn't do in one go. The suggestion here is that this is also why people talk
to themselves silently. Your brain does a lot at once, quickly, but putting a half-finished thought
into words lets you hold it, look at it and build the next step on it. People can still think
without inner speech, but it seems to help most with problems that have to be done one step after
another.

### See also

- [cot-serial-verbal-workspace](cot-serial-verbal-workspace.md): the claim that chain of thought plays the role of a serial
  verbal workspace, which this claim turns back on the human case.
- [cot-workspace-from-functional-signature](../arguments/cot-workspace-from-functional-signature.md): the argument for treating chain of thought
  as a workspace.
- [jackendoff-1996](../sources/jackendoff-1996.md): Jackendoff's account of how language helps us think by giving
  unconscious conceptual structure a conscious verbal handle.
- [sep-inner-speech](../sources/sep-inner-speech.md): survey of the philosophy of inner speech and its proposed roles in
  thought.
- [extended-mind](../concepts/extended-mind.md): Clark's broader thesis, of which the idea that words augment
  computation is one strand.

---
id: argument-llmary-predicted-surprise
type: argument
title: Because a fully informed learner's first-encounter surprise varies with whether the binding is installed and not with what it knows, the surprise registers a missing binding rather than missing knowledge
headword: Predicted-surprise argument
author: mishka
status: asserted
pattern: best-explanation
tags: [philosophy-of-mind, consciousness, ai, thought-experiment, knowledge-argument]
premise: [claim-first-encounter-adds-binding, claim-reading-own-weights-is-description, claim-surprise-predictable-yet-undergone, claim-unknown-token-selection-bound, claim-write-access-installs-binding]
concludes: claim-surprise-registers-missing-binding
responds_to: [argument-knowledge-argument, argument-mary-misimagined]
uses_concept: [concept-llmary, concept-self-access-kinds, concept-knowledge-argument]
created: 2026-11-22
style: encyclopedia
---

Discussions of Mary the colour scientist commonly treat surprise on release as a sign of missing
knowledge. Frank Jackson writes that Mary "will not say 'ho, hum'", and takes this to show that she
learns something she did not know ([jackson-1986](../sources/jackson-1986.md), p. 291). Daniel Dennett runs the same link
the other way: a Mary who knew all the physical facts would have "already written down, in exquisite
detail" how colour would affect her, and so would not be "in the slightest surprised"
([dennett-1991](../sources/dennett-1991.md); [dennett-2005](../sources/dennett-2005.md)). George Graham and Terence Horgan concede that a
fully informed Mary could predict her own surprise, but call this "beside the point" and ask the
materialist to explain why that surprise is rationally appropriate rather than an error
([graham-horgan-2000](../sources/graham-horgan-2000.md), pp. 76–77). The [llmary](../concepts/llmary.md) thought experiment allows the link
between surprise and knowledge to be tested directly, by varying the learner's self-access while
holding its knowledge fixed.

### The argument

The inference form is inference to the best explanation.

1. What a model's first encounter with a token adds beyond any description is the binding of the
   token's relational role to its own representation ([first-encounter-adds-binding](../claims/first-encounter-adds-binding.md)).
2. Reading its own weights, or simulating itself with them, is a form of description and cannot by
   itself supply that binding ([reading-own-weights-is-description](../claims/reading-own-weights-is-description.md)).
3. A learner can know in advance the size and direction of its first-encounter surprise and still
   undergo it ([surprise-predictable-yet-undergone](../claims/surprise-predictable-yet-undergone.md)).
4. With several indistinguishable unknown tokens, description alone leaves a surprise of at least
   log *k* beyond what selecting the right token would allow, a bound the model can compute and cannot
   reduce ([unknown-token-selection-bound](../claims/unknown-token-selection-bound.md)).
5. A learner that can write its own representations can install the binding without the encounter,
   and then meets the item with no surprise ([write-access-installs-binding](../claims/write-access-installs-binding.md)).
6. Therefore the best explanation of a fully informed learner's first-encounter surprise is that it
   registers a missing binding rather than missing knowledge
   ([surprise-registers-missing-binding](../claims/surprise-registers-missing-binding.md)).

The structure is one of co-variation. Across premises 2 to 5 the learner's knowledge stays the same:
it knows everything sayable about the token, including the surprise it will suffer. What changes is
only its access to its own representations. Where it can read and simulate but not write, it is
surprised, predictably and to a computable degree. Where it can write, and uses that power to install
the binding, the surprise vanishes. Surprise therefore tracks the binding, not the knowledge, and the
hypothesis that it signals missing knowledge predicts a co-variation that does not occur.

### Bearing on Mary

Carried over to Mary, the result separates four cases that the literature runs together. Jackson's
Mary, who has descriptive knowledge but cannot rewire her colour system, is surprised. That is
correct, but the surprise shows that her colour representations needed adjusting, not that her
physical knowledge was incomplete. Dennett's RoboMary, who can rewire herself, is not surprised, which
is also correct, but because she has done by writing what the encounter would have done, not because
knowing more removes surprise. Graham and Horgan's Mary Mary can predict her surprise and still feel
it, and their footnoted worry that she "cannot both know that she will be surprised in a certain way
and be surprised in that way" ([graham-horgan-2000](../sources/graham-horgan-2000.md), p. 85 n. 7) dissolves once the
knowledge and the surprise are seen to be carried by different parts of one system. The surprise is
rationally appropriate in exactly the sense they ask for: it is an accurate signal, not an illusion.

How much the human case resembles the model's depends on how much of Mary's colour pathway is fixed
before experience. If all of it is, there is nothing for the encounter to install, and Mary's first
sight of red is like anyone else's; if some of it is shaped by experience, the encounter installs a
binding there ([mary-gain-depends-on-prewiring](../claims/mary-gain-depends-on-prewiring.md)).

### The weakest premise

The analogy behind the bearing on Mary is the weakest link, as it is for the other LLMary arguments
([mary-analogous-to-llmary](../claims/mary-analogous-to-llmary.md)). The phenomenal realist can grant everything about the model and
hold that Mary's surprise contains a further component, delight at a new phenomenal quality, that has
no counterpart in a prediction error. Graham and Horgan press exactly this, describing what surprises
Mary Mary as "the unanticipated experiential basis" of her new capacities. The argument's reply is that
such a component would have to make no difference to anything the surprise does or predicts, since
everything it does is accounted for by the missing binding, and positing it is the point at issue
rather than an independent datum.

Within the model case, premise 4 depends on the never-seen rows being genuinely indistinguishable to
the model. A model with introspective access to its own activations might break the symmetry, though
it would then be using a further kind of self-access ([self-access-kinds](../concepts/self-access-kinds.md)) and the conclusion
would still follow for every learner that lacks it.

### In plain terms

People often assume that if Mary is surprised when she first sees red, she must have been missing some
fact, and that if she knew every fact, she could not be surprised. The AI version of Mary
([llmary](../concepts/llmary.md)) shows this is wrong. An AI that knows everything about a new word-piece can still
be surprised when it meets it, and can even predict how surprised it will be. The only thing that
stops the surprise is the AI rewiring itself in advance, which is what Dennett's robot Mary does
([mary-misimagined](mary-misimagined.md)). So surprise does not show a gap in knowledge. It shows that the mind
had not yet been set up to handle the thing itself, which is something knowing more cannot fix.

### See also

- [llmary-binding](llmary-binding.md) — the argument that what the first encounter adds is binding, on which
  this one builds.
- [knowledge-argument](knowledge-argument.md) — Jackson's argument, whose use of Mary's surprise this argument
  contests.

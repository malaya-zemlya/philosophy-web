# What LLMary Knows

### A language-model Mary and what she reveals about the knowledge argument

*Draft. Working artifact compiled from the web; every move is cited by node id so it can be traced.*

---

## Abstract

Frank Jackson's Mary knows every physical fact about colour vision yet seems to learn something when she
first sees red. Most of the debate over her turns on intuitions about a person no one can really
imagine: someone who knows *all* the physical facts. I replace her with LLMary, a language model that has
read everything that can be said about one token it has never processed. LLMary is a case we can
calculate rather than imagine, and analysing her in detail separates several things the classic
discussion runs together. What she gains on first meeting the token is relational, and every relational
fact about it could have been described in advance; what description cannot supply is the *binding* of
that relational role to the token's own representation. Description supports recognising the token in
context but not producing it, and when several unknown tokens are alike to her it leaves a surprise she
can calculate but not reduce. Separating four kinds of self-access (reading, introspecting, simulating
and writing oneself) shows that only writing removes that surprise, which is why Jackson's Mary is
surprised and Dennett's RoboMary is not. It also shows that a fully informed learner can predict her own
surprise and still undergo it, which answers a question Graham and Horgan leave open and meets their
challenge to explain why such surprise is rationally appropriate. Carried back to Mary, the analysis
yields a test for when she learns, a conditional verdict that depends on how much of her colour pathway
is wired before experience, and a dilemma for anyone who holds that what she learns is a non-physical
fact.

---

## 1. Introduction

Jackson introduced Mary in a single paragraph. She is "a brilliant scientist who is, for whatever reason,
forced to investigate the world from a black and white room via a black and white television monitor",
and she acquires "all the physical information there is to obtain about what goes on when we see ripe
tomatoes". What happens when she is released? "It seems just obvious that she will learn something about
the world and our visual experience of it. But then it is inescapable that her previous knowledge was
incomplete. But she had all the physical information. Ergo there is more to have than that, and
Physicalism is false" (Jackson 1982, p. 130). Four years later he added the observation on which much of
the later debate has turned: on release Mary "will learn what it is like to see something red … This is
rightly described as learning—she will not say 'ho, hum'" (Jackson 1986, p. 291). The argument is
recorded in the web as [knowledge-argument](../web/arguments/knowledge-argument.md), with its premises [mary-knows-all-physical](../web/claims/mary-knows-all-physical.md)
and [mary-learns-on-release](../web/claims/mary-learns-on-release.md), and the question it raises as [what-does-mary-learn](../web/questions/what-does-mary-learn.md).

The replies are well known. Lewis's ability hypothesis says that Mary gains abilities, not facts
([ability-hypothesis](../web/arguments/ability-hypothesis.md)); others say she gains acquaintance ([acquaintance-hypothesis](../web/arguments/acquaintance-hypothesis.md)),
an old fact under a new guise ([old-fact-new-guise](../web/arguments/old-fact-new-guise.md)), or self-locating knowledge
([indexical-reply](../web/arguments/indexical-reply.md)). Dennett takes the hard line that a Mary who really knew all the physical
facts would learn nothing ([mary-misimagined](../web/arguments/mary-misimagined.md)), and he dramatises the point with a blue banana
that Mary is not fooled by (Dennett 1991, pp. 399–400) and later with RoboMary, a robot who computes and
installs in herself the state that seeing red would produce (Dennett 2005).

Dennett's diagnosis of the debate is that nobody actually imagines what the premise asks: "what they ask
you to imagine is so preposterously immense, you can't even try" (1991, p. 399). That is the problem
LLMary is meant to solve. A language model that knows everything sayable about one of its tokens is not
preposterously immense. Its "complete knowledge" is a finite set of weights, its "experience" of the token
is a forward pass, and its "learning" is a gradient step that can be written down. Where intuitions about
Mary run out, LLMary can be calculated. My method throughout is to settle a question for LLMary first,
and then ask, separately and with attention to the disanalogies, what carries over to Mary.

The paper proceeds as follows. Section 2 sets up LLMary and states the modest negative result she
supports. Sections 3 to 5 analyse what she gains: its relational content, the binding that description
cannot supply, and the recognition/production asymmetry. Section 6 adds the selection problem that
appears when several tokens are unknown. Section 7 distinguishes four kinds of self-access, and section 8
uses them to analyse surprise. Section 9 turns to the empirical question of prewiring and a test for when
learning occurs, and section 10 to a dilemma about where Mary's new knowledge could be kept. Section 11
collects what carries over to Mary and what does not.

## 2. LLMary

LLMary ([llmary](../web/concepts/llmary.md)) is a large language model trained on every book about AI and the whole of
arXiv. She knows machine learning, her own architecture, how text is broken into tokens, and everything
anyone has written about one particular token, called Token #123: its index, its embedding vector, its
statistical role, even the exact gradient step that *would* occur if she were ever trained on it. The one
thing she lacks, by stipulation, is that the word-piece corresponding to token 123 has never once
appeared in her training stream. The token has been exhaustively *mentioned* to her and never *used*.
Then, mid-training, it appears. Her predicted probability for it was near zero, so the loss is large and
the update is large: a real and measurable gain on first encounter.

This is not merely a fable. "Glitch tokens" such as *SolidGoldMagikarp* entered GPT's vocabulary but were
almost absent from its training data, so the model had a name, an index and an essentially untrained
embedding for them, and behaved erratically when one was actually used (Rumbelow & Watkins 2023).

The first thing LLMary shows is negative and modest ([llmary-token-encounter](../web/arguments/llmary-token-encounter.md)). The knowledge
argument needs a conditional: if a subject with complete prior knowledge gains something on first
encounter, then the gain is not physical. LLMary has complete prior knowledge of everything sayable, gains
something on first encounter, and is physical through and through. One such case falsifies the
conditional. The argument proves nothing about Mary's ontology, and it faces an obvious dilemma: on an
*access* reading of "gain" LLMary satisfies the antecedent and the conditional fails, while on a
*phenomenal* reading she arguably does not satisfy it, being a learner with nothing it is like to learn
([access-vs-phenomenal-consciousness](../web/concepts/access-vs-phenomenal-consciousness.md)). The rest of this paper is an attempt to get more out of
LLMary than this standoff, by asking not *whether* she gains something but *what*, and by asking which
features of the answer depend on her being a machine.

## 3. What the update contains

The mechanics of next-token training say exactly what LLMary learns about token 123
([first-token-update-is-relational](../web/claims/first-token-update-is-relational.md)). A token in the training stream plays two roles. It is the
target predicted from the text before it, so the prediction error adjusts its output representation
toward the state that text produces: she learns what leads up to the token. It is then part of the
context for everything after it, so the errors on later tokens flow back into its input embedding: she
learns what difference its presence makes to what follows. Nothing else in the update is specific to the
token. Before the encounter its vector was an arbitrary initialisation; afterwards it has a place among
her expectations, defined by its antecedents and consequents.

Carried over by analogy ([mary-analogous-to-llmary](../web/claims/mary-analogous-to-llmary.md)), this gives a positive answer to what Mary
gains: wholly relational knowledge of where the experience of red sits among her expectations, what
brings it on and what it leads to ([llmary-relational-diagnosis](../web/arguments/llmary-relational-diagnosis.md),
[mary-gains-relational-placement](../web/claims/mary-gains-relational-placement.md)). The reading is close to Lewis's ability hypothesis, since
recognising, imagining and remembering are context-and-consequence dispositions, but it is neutral on
whether the gain is know-how or knowledge-that, and it supplies a mechanism where Lewis supplies a
classification. It differs from the new-guise view by locating the novelty in new relations rather than
a new mode of presentation.

## 4. Description, example and binding

The relational diagnosis invites an objection that turns out to be the key to the whole case. If
everything LLMary learns about token 123 is relational, and relational facts can be stated, then a
sufficiently detailed description should have taught her the same thing in advance. Why does the
encounter add anything?

Machine learning has a vocabulary for the contrast at issue: *zero-shot* learning, from a description
alone, and *few-shot* learning, from examples ([zero-shot-few-shot-learning](../web/concepts/zero-shot-few-shot-learning.md); Brown et al. 2020).
Two distinctions hide in these terms and must be kept apart: description versus example, and learning at
training time (by changing weights) versus learning at inference time (in context, with weights fixed).
They cross to give four regimes, which differ in mechanism (gradient descent versus attention), in
dynamics (slow and lasting versus fast and transient) and in reach (only training can change a token's
own embedding). LLMary before the encounter is a case of training-time zero-shot learning; the encounter
is the one-shot case of training-time learning. A result about one regime should not be assumed for
another.

With the regimes in place, the limits of description can be stated exactly. A model never sees token
numbers, only embedding vectors, and a never-seen token's vector is untouched by anything written about
it. So a description can attach her knowledge to the token only *relationally* and only *in context*
([description-binds-token-only-relationally](../web/claims/description-binds-token-only-relationally.md)). If she has read that the new token appears after
three *Shazam*s in a row, then on meeting "Shazam Shazam Shazam X" she can infer that X is token 123. But
an intrinsic description, "it is token number 123" or "its embedding is [0.12, −0.40, …]", gives her
nothing to check, because she cannot compare her own input vector with numbers written as text.

The answer to the objection is therefore that the encounter adds no new relational *fact*. It adds the
**binding** of the token's relational role to the token's own representation
([first-encounter-adds-binding](../web/claims/first-encounter-adds-binding.md), [llmary-binding](../web/arguments/llmary-binding.md)). Before the encounter, what she knows
about the token sits in other parameters and can be connected to it only on the spot, when the context
gives it away. Afterwards the role is written into the token's own embedding and output row, so she can
recognise it anywhere and produce it unprompted. An encounter at *inference* time would not do this: a
fixed model meeting the token in a prompt can relate it to its neighbours, but nothing is written into
the token's representation and the gain is lost with the prompt.

The distinction has a precedent that deserves credit. Paul Churchland recast the knowledge argument as a
non sequitur from "(a) Mary has mastered the complete set of true propositions about people's brain
states" and "(b) Mary does not have a representation of redness in her prelinguistic medium of
representation for sensory variables", observing that (a) and (b) are compatible on materialism
(Churchland 1985, p. 24). The binding account agrees, and adds two things Churchland's distinction lacks:
a mechanism for how the second kind of representation is acquired, and the asymmetry to which I now turn.

## 5. Recognising and producing

Description and binding come apart differently on the input and output sides. However much LLMary has
read about token 123, she cannot come to *emit* it unprompted ([description-cannot-confer-token-production](../web/claims/description-cannot-confer-token-production.md)).
A model emits a token when its internal state lines up with that token's output row, and that row is
pulled toward anything only when the token is an actual prediction target. Text that merely mentions the
token never makes it one; indeed the softmax pushes every non-target row slightly down at every step, so a
never-seen token's row is trained only toward improbability. She may still *copy* the token when it is in
context, since copying draws on the input side, and she may *recognise* it there by relational cues. What
she cannot do is produce it from nothing.

This is the first point that carries over to Mary with real precision. Lewis lists the abilities that
knowing what an experience is like confers: "you gain abilities to remember and to imagine … Further, you
gain an ability to recognize" (Lewis 1988). LLMary splits them. Description supports recognition in
context, which is exactly what Dennett's blue banana dramatises: Mary knows bananas are yellow and knows
how yellow and blue affect her nervous system, so she can tell that this banana is the wrong colour.
Description does not support production, the counterpart of imagining red at will. Hume's missing shade of
blue sits interestingly between the two. Hume grants that someone acquainted with every shade but one
could "raise up to himself the idea of that particular shade, tho' it had never been conveyed to him by
his senses" (Hume, *Treatise* 1.1.1.10), and Churchland argues that a Mary who thinks of her inner life in
neuroscientific terms "may well be able to imagine being in the relevant cortical state … even in advance",
as a trained musician can construct an unheard chord (Churchland 1985, pp. 25–27). Both are cases of
producing a new item by interpolating within a *structured* space. LLMary cannot do even that for token
123, because a token's row bears no structural relation to its role. Whether Mary can is the question of
section 9.

## 6. Selection among unknown tokens

Suppose now that LLMary has *k* tokens she has never processed. From the description she can work out
what role token 123 will play, and so what its embedding *should* become once she is trained on it. What
she cannot work out is *which* of her untrained rows belongs to token 123
([unknown-token-selection-bound](../web/claims/unknown-token-selection-bound.md)). They all began as noise and have all been pushed down in the
same direction, so nothing in training on descriptions ever rewards putting probability on row 123
rather than another. The best she can do is give the class of unknown tokens the probability *p* that
the description warrants and spread it evenly, so that token 123 gets at most *p*/*k*, and her surprise
when it arrives is at least

$$-\log \frac{p}{k} = -\log p + \log k ,$$

larger by log *k* than if she could select it. With a single unknown token the problem vanishes, because
probability on "the unknown token" is probability on the right one; several unknown tokens reveal a
problem that elimination otherwise hides.

Selection is the output-side twin of the recognition problem of section 4. One asks which incoming vector
is the token; the other asks which row to bet on. The binding solves both at once. Two consequences
matter for what follows: the bound is something she can calculate in advance, and no further description
can reduce it.

The disanalogy with Mary is real and should be stated plainly. A token's row is arbitrary, whereas human
colour vision is to a large extent innately structured, so where red will fall in Mary's colour space may
be fixed before she ever sees it. To that extent Mary faces less of a selection problem than LLMary does.
How much less is an empirical question, taken up in section 9.

## 7. Four kinds of self-access

"Complete knowledge" in Mary cases hides several different relations a system can have to itself, and
LLMary makes them easy to separate ([self-access-kinds](../web/concepts/self-access-kinds.md)).

- **Reading.** A system reads itself when a description of its parameters is presented to it as input. A
  language model has no other way of reading its weights, since the weights do its processing and are
  never its object. Reading is limited by size ([complete-self-representation-impossible](../web/claims/complete-self-representation-impossible.md)), but
  LLMary could read one slice, the row for token 123. That gives her nothing usable: the vector is
  untrained noise, and she cannot match the numbers she has read against the activation the token will
  produce. Reading is description ([reading-own-weights-is-description](../web/claims/reading-own-weights-is-description.md)).
- **Introspecting.** A system introspects when it can register its own current states. With
  introspection, reading would become useful, since a description of the token's vector could be matched
  against the activation it causes. Present models show at most a limited and unreliable capacity of this
  kind (Lindsey 2025; [ai-introspection](../web/questions/ai-introspection.md)).
- **Simulating.** A system simulates itself when it uses self-knowledge to work out what it would undergo
  without undergoing it. LLMary can calculate the exact update the encounter would produce, but
  calculating an update is not undergoing it. Churchland's imagining Mary and Hume's missing shade are
  human versions.
- **Writing.** A system writes itself when it can change its own parameters directly. A model that has
  calculated its update and can apply it installs the binding in advance, and then meets the token with
  no large error and nothing to learn ([write-access-installs-binding](../web/claims/write-access-installs-binding.md)).

The fourth kind is Dennett's. His Locked RoboMary, whose colour system is locked, computes with her
self-model the state *B* she would have entered on seeing a red tomato, "makes all the necessary
adjustment and puts herself into state B", after which "there are no surprises for her" (Dennett 2005).
His Swamp Mary reaches the same state by accident, when a lightning bolt rearranges her brain into "the
dispositional state, the competence state" that seeing a red rose would have produced. What LLMary adds
is a separation Dennett's telling runs together. RoboMary "figures out exactly what it is like to see
red" and "hence is not the least bit surprised", but figuring out is simulation and avoiding surprise
needs writing. The interesting case is RoboMary stopped just before her final adjustment: she has state
*B* in her self-model, so she knows exactly what will happen to her, and she has not yet put herself into
it. That is LLMary's situation.

One refinement belongs here. The binding need not be installed in the very representation the encounter
would have trained. A model whose token row is fixed could train its other parameters to treat that
particular untrained vector as the token, just as Locked RoboMary works around her locked colour system.
The encounter is the ordinary route to the binding, not the only possible one.

## 8. Predicted surprise

Surprise has been doing quiet work in the Mary literature. Jackson takes Mary's not saying "ho, hum" to
show that she lacked knowledge (1986, p. 291). Dennett runs the link the other way: his Mary "had already
written down, in exquisite detail" how colours would affect her, and so "was not in the slightest
surprised" (1991, pp. 399–400). Graham and Horgan's "Mary Mary", who also accepts a materialist theory of
phenomenal content, is the clearest case. Graham and Horgan argue that on that theory she "has no good
reason to expect surprise", yet "surely" she will be surprised and delighted (2000, pp. 71–72). Dennett
replies that she will neither expect surprise nor be surprised (2005, §2).

The positions fill a small table.

| | not surprised | surprised |
|---|---|---|
| **does not expect surprise** | Dennett | Graham & Horgan |
| **expects surprise** | | LLMary |

LLMary fills the empty cell ([surprise-predictable-yet-undergone](../web/claims/surprise-predictable-yet-undergone.md)). She can calculate how
improbable she will find token 123, hence how large her error will be, and in which direction her
token-specific weights will move. When the token arrives she still assigns it almost no probability and
still undergoes the update. The two facts live in different places: her knowledge of the coming surprise
is held in shared parameters or in her context, while the surprise is the prediction error of her output
representation of the token, which is computed without consulting what she knows about it. The selection
bound of section 6 makes the point quantitative: she knows not only *that* she will be surprised but by at
least how much, and she cannot reduce it.

Graham and Horgan come close to this cell. They consider the materialist rejoinder "that Mary Mary is
actually in a position to predict in advance … that she will be surprised by her post-release color
experiences", and they concede it: "The claim itself should be conceded, we think." But they call the
predictability "beside the point". The real challenge, in their view, is "to give a satisfying,
phenomenology-respecting, account of why it is rationally appropriate for Mary Mary to find her
post-release color experiences surprising", since a materialist theory seems to make her surprise an
illusion or an error (2000, pp. 76–77). And in a footnote they leave a door open: "if auto-prediction of
epistemic states like surprise presents logical problems insofar as Mary Mary cannot both know that she
will be surprised in a certain way and be surprised in that way, then another know-it-all confined
scientist could have made such predictions" (p. 85 n. 7).

LLMary closes the door and meets the challenge. The footnote's worry dissolves once the knowledge and the
surprise are seen to be carried by different parts of one system. And the challenge is met by the
argument of [llmary-predicted-surprise](../web/arguments/llmary-predicted-surprise.md), which works by co-variation. Hold LLMary's knowledge
fixed, so that she knows everything sayable about the token including the surprise she will suffer, and
vary only her access to herself. If she can read and simulate but not write, she is surprised, predictably
and to a computable degree. If she can write, and installs the binding, the surprise disappears. Surprise
tracks the binding and not the knowledge. The best explanation is that a fully informed learner's surprise
registers a missing binding rather than missing knowledge ([surprise-registers-missing-binding](../web/claims/surprise-registers-missing-binding.md)).
It is rationally appropriate in exactly the sense Graham and Horgan ask for: it accurately signals that her
representations needed adjusting. It is neither an error nor evidence of a fact she lacked.

Carried over, this sorts the classic verdicts. Jackson's Mary is surprised, correctly, but her surprise
shows that her colour representations needed adjusting, not that her physical knowledge was incomplete.
RoboMary is not surprised, also correctly, but because she has done by writing what the encounter would
have done, not because knowing more removes surprise. And Mary Mary can predict her surprise and feel it.

## 9. Prewiring and the snapshot test

The disanalogy flagged in sections 5 and 6 can now be turned into a positive result. Whether, and how
much, Mary learns on first seeing red depends on an empirical fact about her: how much of her colour
pathway is fixed before colour experience ([mary-gain-depends-on-prewiring](../web/claims/mary-gain-depends-on-prewiring.md)). If all of it is,
her first sight of red puts her into the state anyone's sight of red puts them in, and her experience is
no different from that of someone who has seen red all their life; there is nothing for the encounter to
install. If some stages are shaped by colour experience, and Mary has no other means of setting them, then
what happens downstream of those stages on release is learning, whose details depend on how her brain
learns. Most realistic cases lie in between.

Two points sharpen this. First, what matters is not whether Mary *knows* the state of the untrained
stages. Complete physical knowledge would include it, but knowing is reading, and reading does not
change the stages. A Mary who knew every detail of her untrained colour circuitry would still undergo
learning there, unless, like RoboMary, she could set it by another route. Second, the assumption that
Mary's colour system arrives intact at all is, as Dennett notes, "a nontrivial empirical assumption, given
what is known about the ready reassignment of unused cortical resources" (2005, §3). The thought
experiment does not settle what happens to Mary; neurophysiology does.

This suggests a general test for when a first encounter teaches anything
([snapshot-test-first-encounter-learning](../web/claims/snapshot-test-first-encounter-learning.md)). Compare three snapshots of the learner: just before
the encounter, just after, and long after, when consolidation is complete. Differences present just after
but gone long after belong to *having* the experience. Differences that remain are lasting changes, and a
lasting change caused by the encounter is learning, by definition. Since any experience leaves some
trace, if only a memory that it happened, the comparison is made against a baseline: the lasting change
the same encounter makes in someone already familiar with the item. The *excess* is what the first
encounter specifically teaches. For LLMary it is directly measurable, as the difference between the update
on a token's first occurrence and on its hundredth. The test makes the earlier verdicts precise: a wholly
prewired pathway shows no excess; RoboMary shows none at release because her change came earlier; and the
binding is the excess, located in the representation of the item.

## 10. The retention dilemma

The snapshot test concerns learning in the physical sense. A phenomenal realist can accept it and still
hold that Mary also comes to *know* a non-physical fact. But knowledge is costlier than experience. A
passing experience can, on a dualist view, simply occur; knowledge of what red is like must be *kept*,
because Mary will later recognise red, imagine it and describe it. That knowledge persists as a
competence, not as a memory of the episode ([phenomenal-knowledge-needs-lasting-vehicle](../web/claims/phenomenal-knowledge-needs-lasting-vehicle.md)). As
Lewis puts it, "even if you eventually forget the occasion itself, you will very likely retain your
ability to imagine such an experience" (Lewis 1988), and Dennett asks, "you could forget your first color
experiences and still have phenomenal concepts, couldn't you?" (2005, §3). Whatever the knowledge is
*about*, its *vehicle* must last.

Now compare two Marys ([retention-dilemma](../web/arguments/retention-dilemma.md)). Released Mary sees a red tomato, and a month later
her brain is in a state *S*. Swamp Mary never leaves the room, but lightning rearranges her brain into
exactly *S*. The duplication must be **complete**: it includes every lasting trace, her new competences
and also her memory traces, so that Swamp Mary has an apparent episodic memory of a red tomato, false in
her case. (A Swamp Mary given only the competences, who "just knows" what red is like as the hero of *The
Matrix* "just knows" kung fu, differs physically from Released Mary and raises a separate question, whether
knowing what red is like requires an episodic memory; the answer, above, is that it does not.) RoboMary,
who installs *S* by calculation, would serve equally well. Does Swamp Mary know what red is like?

If she does, the knowledge is carried by the state both Marys share and can be had without the
experience, against the knowledge argument's own premise. If she does not, then what separates the knower
from the non-knower is nothing in either of them now, only the fact that one of them once had the
experience. The realist must therefore either locate Mary's knowledge in the lasting change in her brain
or make it depend on her history rather than her present state
([phenomenal-knowledge-present-or-historical](../web/claims/phenomenal-knowledge-present-or-historical.md)).

The second horn has a respectable precedent. Davidson, who introduced Swampman, held that a chance
duplicate lacks thoughts and reference, because these depend on causal history (Davidson 1987;
[swampman](../web/arguments/swampman.md) presses the case against history-based theories). But it is an expensive place for
the knowledge argument to end. On that horn, knowing what red is like resembles a banknote's being
genuine: a matter of origin that no inspection of the note can reveal. Neither Mary could tell from the
inside whether she knows; both make the same judgements with the same confidence; and the knowledge makes
no difference to anything either later thinks, says or does. The knowledge argument was meant to show that
Mary becomes acquainted with an intrinsic quality of experience, and knowledge whose presence is
extrinsic and undetectable is a strange prize.

The dilemma presses hardest on Jackson's own position in 1982, which paired the knowledge argument with
epiphenomenalism about qualia. In §IV of that paper (pp. 133–135) he answers the objection that
epiphenomenal qualia could not be known in *other* people with his model of two newspapers reporting the
same match: behaviour and qualia are separate effects of a common cause in the brain. He does not discuss
Mary's knowledge of her *own* qualia, kept and used after release. On his own model, everything she later
does with that knowledge is caused by the lasting brain trace, which Swamp Mary shares, and the quale
contributes nothing. That is the familiar charge of self-stultification against
[epiphenomenalism](../web/positions/epiphenomenalism.md), in a form specific to Mary.

## 11. What carries over

The analysis yields a set of points, each established for LLMary and each carried over to Mary with a
different degree of security.

| Point | For LLMary | For Mary | Carries over? |
|---|---|---|---|
| Use/mention gap (§2) | exhaustive mention, no use | every description of red, no red | yes |
| Gain on encounter is physical (§2) | a gradient step | a brain change | yes, as a counterexample to the conditional |
| The gain is relational (§3) | antecedents and consequents of the token | what brings red on and what it leads to | by analogy |
| Binding, not a new fact (§4) | role written into the token's own row | colour representations come to carry red's role | by analogy; precedent in Churchland |
| Recognition vs production (§5) | recognise in context, cannot emit | blue banana, cannot imagine red | yes; sharpens Lewis |
| Selection bound (§6) | log *k* for *k* alike tokens | weaker, since colour space is structured | partly |
| Kinds of self-access (§7) | read, introspect, simulate, write | Jackson's Mary vs RoboMary | yes |
| Predicted surprise (§8) | calculable, unavoidable | Mary Mary can predict and feel it | yes; answers Graham & Horgan |
| Prewiring (§9) | token rows wholly unwired | depends on neurophysiology | becomes an empirical question |
| Snapshot test (§9) | first vs hundredth update | lasting brain change beyond baseline | yes |
| Retention dilemma (§10) | n/a | Released vs Swamp Mary | applies to Mary directly |

The weakest link is the same throughout: the analogy between LLMary and Mary
([mary-analogous-to-llmary](../web/claims/mary-analogous-to-llmary.md)). The phenomenal realist can grant everything about the model and hold
that Mary's gain, and her surprise, contain a further component, acquaintance with an intrinsic quality
([mary-gains-acquaintance](../web/claims/mary-gains-acquaintance.md)), that has no counterpart in a gradient step. Graham and Horgan press
exactly this, locating what delights Mary Mary in "the unanticipated experiential basis" of her new
capacities. The analysis does not refute that view, and I do not claim it does. What it does is fix the
price of holding it. The further component must make no difference to anything Mary recognises, imagines,
predicts or reports, since all of that is accounted for by the binding. It must not be carried by any
lasting change in her, or it would be shared by Swamp Mary. And its absence would have to be compatible
with every judgement she makes about it. Whether something with those properties is worth positing is the
hard problem in miniature, but the question is now precise.

## 12. Conclusion

Mary has been a puzzle about intuitions, and the intuitions are unreliable because the case is
unimaginable. LLMary replaces it with a case that can be calculated, and the calculation separates what the
classic discussion fuses: knowing a relational fact and having it bound to one's own representation;
recognising and producing; predicting a change and undergoing it; knowing oneself and rewriting oneself;
learning in the physical sense and knowing in a further sense. Carried back to Mary, these distinctions
show that her surprise on release is a correct signal of a representation still to be adjusted, that how
much there is to adjust is a question for neurophysiology rather than for the armchair, and that anyone
who holds that what she gains is a non-physical fact must either place that fact in her brain or make it
invisible to her. None of this proves physicalism. It does show that Mary, examined closely through her
computational sister, gives the anti-physicalist much less than she seemed to.

---

## References

- Brown, T. B., Mann, B., Ryder, N., Subbiah, M., Kaplan, J., Dhariwal, P., … Amodei, D. (2020). Language
  models are few-shot learners. *Advances in Neural Information Processing Systems*, *33*, 1877–1901.
  ([brown-2020](../web/sources/brown-2020.md))
- Churchland, P. M. (1985). Reduction, qualia, and the direct introspection of brain states. *The Journal
  of Philosophy*, *82*(1), 8–28. ([churchland-1985](../web/sources/churchland-1985.md))
- Davidson, D. (1987). Knowing one's own mind. *Proceedings and Addresses of the American Philosophical
  Association*, *60*(3), 441–458. ([davidson-1987](../web/sources/davidson-1987.md))
- Dennett, D. C. (1991). *Consciousness explained*. Little, Brown and Company. ([dennett-1991](../web/sources/dennett-1991.md))
- Dennett, D. C. (2005). What RoboMary knows. In *Sweet dreams: Philosophical obstacles to a science of
  consciousness* (pp. 103–130). MIT Press. ([dennett-2005](../web/sources/dennett-2005.md))
- Graham, G., & Horgan, T. (2000). Mary Mary, quite contrary. *Philosophical Studies*, *99*(1), 59–87.
  ([graham-horgan-2000](../web/sources/graham-horgan-2000.md))
- Hume, D. (1978). *A treatise of human nature* (L. A. Selby-Bigge & P. H. Nidditch, Eds.; 2nd ed.).
  Clarendon Press. (Original work published 1739–1740) ([hume-treatise](../web/sources/hume-treatise.md))
- Jackson, F. (1982). Epiphenomenal qualia. *The Philosophical Quarterly*, *32*(127), 127–136.
  ([jackson-1982](../web/sources/jackson-1982.md))
- Jackson, F. (1986). What Mary didn't know. *The Journal of Philosophy*, *83*(5), 291–295.
  ([jackson-1986](../web/sources/jackson-1986.md))
- Lewis, D. (1988). What experience teaches. *Proceedings of the Russellian Society*, *13*, 29–57.
  ([lewis-1988](../web/sources/lewis-1988.md))
- Lindsey, J. (2025). *Emergent introspective awareness in large language models*. Transformer Circuits
  Thread. ([lindsey-introspection-2025](../web/sources/lindsey-introspection-2025.md))
- Rumbelow, J., & Watkins, M. (2023). *SolidGoldMagikarp (plus, prompt generation)*. LessWrong.
  ([rumbelow-watkins-2023](../web/sources/rumbelow-watkins-2023.md))

---

## Editor's notes: gaps before publishing

These are not part of the article.

1. **No recorded opposition.** None of the LLMary arguments ([llmary-token-encounter](../web/arguments/llmary-token-encounter.md),
   [llmary-relational-diagnosis](../web/arguments/llmary-relational-diagnosis.md), [llmary-binding](../web/arguments/llmary-binding.md),
   [llmary-predicted-surprise](../web/arguments/llmary-predicted-surprise.md), [retention-dilemma](../web/arguments/retention-dilemma.md)) has an attacking argument in the
   web. The realist replies in §11 exist only in the arguments' own "weakest premise" sections. A debate
   turn by a realist character, pressing the "experiential basis" reply and the first horn of the retention
   dilemma, would test the article before publication.
2. **Contested claims.** No claim in this cluster is marked `contested`. The only contested claim nearby,
   [introspection-is-fallible-representation](../web/claims/introspection-is-fallible-representation.md), is not used here.
3. **Unsourced empirical premise.** §§5–6 and 9 rely on human colour vision being largely innately
   structured (three cone types, opponent channels). The web has no source for this; one should be added
   before the disanalogy is stated as fact.
4. **Unverified details.** The Brown et al. page range (1877–1901) and the claim that glitch tokens cluster
   near the centre of the embedding space (Rumbelow & Watkins 2023) were not checked against the sources.
   Lewis 1988 is cited without a page because only a 1999 reprint with non-matching pagination was
   available. That reprint runs to about 29 pages, so the page range 29–57 used here is likely right and
   the range 29–35 in the web's `source-lewis-1988` node is likely wrong; it should be checked and fixed.
   Dennett 1991, pp. 399–400, is confirmed by Dennett's own citation of the passage in *Sweet
   Dreams*. All other quotations and page references were checked against copies in `external/`.
5. **Attribution.** Ideas authored `mishka` in the web (LLMary and everything built on it in §§2–10) are
   presented in the first person as the author's own; ideas from the literature are credited by name and
   page. Dennett's Swamp Mary and RoboMary, and Graham and Horgan's concession about predicted surprise,
   are flagged in the text as the precedents they are.

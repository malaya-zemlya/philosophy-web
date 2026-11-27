# What LLMary Knows

### A language-model Mary and what she reveals about the knowledge argument

*Draft, second version, revised in response to a critical review. Links to the web's nodes, which
record each step of the argument, are collected in an endnote.*

---

## Abstract

Frank Jackson's Mary knows every physical fact about colour vision yet seems to learn something when she
first sees red. The debate over her rests on intuitions about a person no one can really imagine. I
replace her with LLMary, a language model that has read everything that can be said about a token she
has never processed, because LLMary can be calculated rather than imagined. Her case separates three
achievements that discussions of Mary run together: *describing* an encounter in advance, *identifying*
what one encounters, and *being changed* by it in the way that makes the item one's own. A learner can
have the first without the others, and can predict her own surprise at an encounter while still being
surprised by it. What the encounter adds is not a further fact but a state that no description puts her
in. The knowledge argument then turns on whether being put into that state leaves some fact, about
oneself or about other people, still unknown. I argue that the model makes the anti-physicalist answer
costlier than it looks, without claiming that it refutes it.

---

## 1. A pause before writing

Daniel Dennett's RoboMary is a robot colour scientist whose colour system has been locked. Using her
complete knowledge of herself, she calculates the state *B* that her system would enter if she saw a
red tomato. Then she "makes all the necessary adjustment and puts herself into state B", and when her
colour cameras are finally switched on "there are no surprises for her" (Dennett 2005).

Stop the story just before the adjustment. At that moment RoboMary can describe exactly what would
happen to her. Can she also recognise red when she meets it? Can she bring the red state about in
herself? Does she know what red looks like? These are three further questions, and the classic
discussion of Mary seldom keeps them apart. This paper is about keeping them apart. The tool is a
learner whose capacities can be varied one at a time: a language model in Mary's position.

Jackson introduced Mary in one paragraph. She investigates the world "from a black and white room via a
black and white television monitor" and acquires "all the physical information there is to obtain
about what goes on when we see ripe tomatoes". When she is released, "it seems just obvious that she
will learn something about the world and our visual experience of it", so her previous knowledge was
incomplete, and since it included all the physical information, "Physicalism is false" (Jackson 1982,
p. 130). Two features of Jackson's later restatement matter below. He takes Mary's reaction as evidence:
she "will not say 'ho, hum'" (Jackson 1986, p. 291). And he locates the trouble for physicalism not in
what Mary learns about herself but in what she learns about *others*: on release "she will realize how
impoverished her conception of the mental life of others has been all along" (1986, p. 292).

The standard replies say that Mary gains abilities rather than facts (Lewis 1988), acquaintance, an old
fact under a new guise, or self-locating knowledge, or else, with Dennett, that a Mary who really knew
all the physical facts would learn nothing. Dennett's diagnosis of the whole debate is that no one
imagines what the premise asks, because "what they ask you to imagine is so preposterously immense, you
can't even try" (1991, p. 399). A language model that knows everything sayable about one of its tokens
is not preposterously immense. Its knowledge is a finite set of weights, its encounter with the token
is a forward pass, and its learning is a gradient step. So my method is to settle each question for the
model first, and then to ask, separately, what further premise is needed to carry the answer over to
Mary.

## 2. LLMary

LLMary is a large language model trained on every book about AI and the whole of arXiv. She knows her
own architecture, how text is broken into tokens, and everything anyone has written about one token,
called Token #123: its index, its embedding vector, its statistical role, and even the training update
that *would* follow if she met it. By stipulation, the word-piece itself has never appeared in her
training stream. It has been exhaustively *mentioned* and never *used*. Then, mid-training, it appears. I will call
this event *first light*, after the first observation made by a new telescope.

This is not merely a fable. "Glitch tokens" such as *SolidGoldMagikarp* entered GPT's vocabulary while
being almost absent from its training data, so the model had a name, an index and an essentially
untrained representation for them, and behaved erratically when one was used (Rumbelow & Watkins 2023).

A running example will keep things concrete. Suppose LLMary has two tokens she has never processed,
whose rows in her network I will call A and B. Exactly one of them, token 123, has a role she has read
about: it is the word-piece that follows three *Shazam*s in a row. Throughout, it matters to ask what
LLMary knows and *which part of her* can use it. She knows, as a fact stated in her training text, that
the row at index 123 is the one that follows the Shazams. Her next-token predictor, the part of her that
assigns probabilities to what comes next, is a different matter, as section 5 explains.

The trigger is three Shazams, not one, for a reason that is itself a case of use and mention. If token
123 followed a single *Shazam*, a familiar word, then any text describing the role would have to use
the word, and so would contain the trigger. Every such sentence, and every unrelated occurrence of
*Shazam* elsewhere in her training, would be an instance of the trigger followed by some other token,
and the predictor would be trained on the trigger context without the token. The description would
contaminate the very context it describes. A trigger made of a combination of familiar tokens that
never occurs in the training text avoids this. It can be described ("three Shazams in a row") without
being produced, just as token 123 can be mentioned without being used. This is not part of the main
argument, but it shows that the case has to be built with care. Otherwise a stipulation that
LLMary "knows only by description" can be quietly broken by the text that carries the description.

From the training stream itself there are exactly two things for LLMary to learn about token 123: in
what contexts it appears, and what appears once it has been seen, which may be familiar tokens or yet
newer ones. The first is the token's place as an effect, the second its place as a cause. The division
is not special to language models. The experience of red, for Mary or anyone, has antecedents, the
stimuli and states that bring it on, and consequents, what it leads her to expect, say and do.

In a language model the division has a definite implementation. Each token has two learned vectors.
Its *input embedding* is the row looked up when the token appears in the context, and it fixes what
difference the token makes to everything after it. Its *output embedding* is the row against which the
model's internal state is compared when the token is scored as a candidate for the next position, and
it fixes in which contexts the token is predicted. Some models use a single matrix for both, a design
called *tied* embeddings.

The implementation yields a general fact. A physical learner like LLMary is changed by
her first encounter with a token, however much she has learned before, and that learning may include
any amount of discussion of the token, of Mary, of her own weights, of anything, provided the token
itself never appears. On the input side the reason is the difference between use and mention. On the
output side it is the problem of picking out which of the unknown tokens is the one that has arrived.
Both follow from nothing more than the way tokens are fed in and scored. A token enters the network as a one-hot vector $e_i$, all
zeros except a 1 at its index, and its input embedding is the product $E^\top e_i$, which simply selects
row $i$ of the embedding matrix $E$. By the chain rule, the gradient of the loss with respect to any
row $j$ is the gradient with respect to the selected embedding multiplied by the $j$-th entry of the
one-hot vector, which is zero unless token $j$ is in the input. So a token that has never appeared in
her input has never had a nonzero gradient on its input row, and the row is still whatever it was set
to at initialization (shrunk toward zero, if training applies weight decay to it). Her knowledge about
token 123, however complete, is stored elsewhere, in the rows of the tokens used to describe it and in
the layers that process them, and no error signal from that text can reach row 123. So at the first
encounter the token enters her computation as a vector that carries no information about it, and the
first training step on it must change that row.

The output side has been trained, but no more informatively. With logits $z = U h$, where $h$ is the
model's final internal state, and the softmax probabilities $p$, the gradient of the loss with respect
to output row $u_t$ is $(p_t - [t = y])\,h$, where $y$ is the actual next token. For a token that is
never the target the bracket is always zero, so every step moves its row a little away from whatever
state the model is in, in proportion to the probability it was wrongly given. Every never-seen token
receives the same kind of push, and what its row comes to encode is only that the token does not
occur, which is equally true of A and B. With tied embeddings this push is also all the shared row has
received, so the row is no longer at its initial value, but it is still silent about the token's role.
The only way round the
forced update is for the learner to write the row herself, which is RoboMary's move (section 7). For
Mary, the corresponding claim would be that her colour system has never been shaped by red
experiences, however much she knows about them. How far that is true of a human visual system is the
question of prewiring taken up in section 10.

Two versions of LLMary must now be told apart. Unless I say otherwise, LLMary is *untied*: her input
and output rows are separate, so the two things she has to learn about token 123 sit in separate
places. *Tied LLMary* uses one row for both. It is tempting to think that tying merely mirrors the
autoregressive loop, in which each token is first predicted and then read back as input. It does not.
The loop is closed by the token's identity, the index passed from one step to the next, and it works
the same way in both versions. Tying adds a substantive assumption: that the vector by which a token is
anticipated is the vector by which, once it arrives, it acts on what follows. In effect it assumes that
tokens which appear in similar contexts also make similar differences afterwards. For language this is
roughly true, since words of the same grammatical category can stand in for one another on either
side, but it is not exactly true. Language is not symmetric in time: "of the" is common, "the of" is
not.

The assumption changes what first light does. It gives tied LLMary no head start beforehand, since her
shared row has received only the push common to all unseen tokens and says nothing about token 123's
role. But at first light, the update that teaches her what leads up to the token lands on the very row
that governs what the token does as context, so one lesson does double duty. If the assumption holds
for token 123, tied LLMary has less left to learn from the token's later occurrences, and is less
surprised by what follows them, than untied LLMary. If it fails, she has more to learn, because she
must first undo what the assumption supplied. Either way the saving is not knowledge she had. It is a
bet built into her architecture, which pays when the world matches it. That a learner whose
assumptions turn out true needs to update less is a general truth about learning, but it is easy to
miss here, because tying looks like mere bookkeeping.

The point carries over to Mary, and it sharpens the question of prewiring in section 10. Whatever
structure her visual system has before release works as such a bet. To the extent that it matches the
world, she has less to learn at first light, without knowing any more beforehand. The bias is a fact
about her, not a fact she knows. How much Mary gains at first light therefore depends not only on what
she knows but on what her architecture assumes, and the premise of the knowledge argument, which
concerns only what she knows, is silent about the second.

The first result is modest. A first encounter can change what a learner can do even when she could
already describe the change in advance, and the whole episode can be physical. That shows that
"knew everything sayable, yet gained something on first encounter" does not by itself imply that the
gain was non-physical. It does not show that Mary learns no new fact. To infer that she does, one needs
an account of what makes her gain an instance of factual learning, and that is the premise Jackson
actually defends. The rest of the paper asks what LLMary's gain consists in, so that the question about
Mary can be put precisely.

## 3. What the encounter changes

Next-token training says exactly what LLMary learns that is specific to token 123, along the two lines
drawn in section 2. As the *target* predicted from the text before it, the token's output row is
adjusted by the prediction error toward the state that text produces: she learns what leads up to it.
As part of the *context* for what follows, its input row receives its first error signal: she learns
what difference it makes to what comes next. Before the encounter, neither row carried information about
the role. The encounter supplies the first positive training example for token 123, and the loss on it
is large because her predicted probability was near zero.

What she gains is therefore relational: the token's place among its antecedents and consequents.
Carried over by analogy, this suggests that what Mary gains is knowledge of where the experience of red
sits among her expectations, what brings it on and what it leads to. That reading is close to Lewis's
ability hypothesis, since recognising, imagining and remembering are just such dispositions, but it is
neutral on whether the gain is know-how or knowledge-that, and it supplies a mechanism where Lewis
supplies a classification.

## 4. Description, example and binding

The relational reading invites the objection that turns out to be the key to the case. If everything
LLMary learns about token 123 is relational, and relational facts can be stated, then a detailed enough
description should have taught her the same thing in advance. What does the encounter add?

Machine learning distinguishes learning from a description alone (*zero-shot*) from learning from
examples (*few-shot*) (Brown et al. 2020). Two contrasts hide in these words: description versus
example, and learning by changing one's weights during training versus learning in context while the
weights stay fixed. They work by different mechanisms and should not be confused. LLMary before the
encounter has learned from description, in her weights. The encounter is a single example, also in her
weights.

The limits of description show up in the running example. A model never sees token numbers, only the
vectors that represent them. So a description can attach her knowledge to token 123 only through cues
that the context provides. If she meets "Shazam Shazam Shazam" followed by an unfamiliar token, she can
infer that it is token 123. But a description of the token's intrinsic features, "it is number 123" or
"its vector is [0.12, −0.40, …]", gives her nothing to check against what actually arrives.

I will call what the encounter adds the **binding** of the token's role to the token itself, and define
it by what it lets the learner do, not by where it is stored. A learner has bound token 123 if she can:

- *identify* it when it appears in a neutral context, with no cue to give it away;
- *produce* it when a context calls for it;
- *predict* what tends to follow it.

The Shazam cue supplies none of these. A simple control shows why: put the *wrong* unfamiliar token,
B, after the three Shazams, and a learner relying on the cue will take B for token 123. The cue tells her
what belongs in the slot, not which item is in front of her.

The binding can in principle be implemented anywhere in the network; it need not be written into
token 123's own row. Defining it by competence first leaves open where a particular model stores it.
And an encounter in context, with the weights fixed, does not produce it: a fixed model can relate the
token to its neighbours for the length of a prompt, but the competence is gone when the prompt is.

The idea that complete descriptive knowledge can coexist with lacking the right representation has a
precedent. Paul Churchland recast the knowledge argument as a non sequitur from "(a) Mary has mastered
the complete set of true propositions about people's brain states" and "(b) Mary does not have a
representation of redness in her prelinguistic medium of representation for sensory variables"
(Churchland 1985, p. 24). The binding account agrees, and adds a mechanism and some tests.

## 5. Knowing versus being able to use

Section 2 said that LLMary *knows* the row at index 123 is the one that follows the Shazams. Yet her
predictor cannot pick out row A over row B. Is this a contradiction? It is not, but the point needs
care, because there are two different cases.

In the **fully informed case**, the information really is present in LLMary. Ask her, in words, "which
row follows three Shazams?", and she answers "the row at index 123". Ask her predictor to put
probability on that row, and it cannot. To favour row A, her predictor would need to produce an internal
state lined up with the particular vector in row A. The only route from her knowledge to that state runs
through the numbers she has read, translated into the geometry of her own network, and nothing in her
training has ever rewarded that translation. So the information is available to her as a whole but not
usable by the part of her that predicts. This is a fact about how such models are built and trained, not
a logical necessity. A model that could make the translation would have a richer kind of access to
itself, of the sort discussed in section 7, where ZenMary makes it by search.

In the **hidden-assignment case**, the information is genuinely missing. Suppose a fair coin decided
whether A or B is token 123, and nothing she has read distinguishes the two outcomes. Then the encounter
reveals which assignment was made, and what she learns is itself a relational fact: that *this* row is
the one that follows the Shazams.

The point about the fully informed case is that her predictor is in the position of the hidden-assignment
case, even though she is not. That is what lets the second case put a number on the first. If her
predictor gives the unknown tokens total probability *p*, and cannot tell which of *k* of them is the
target, then its *expected* surprise when the target arrives is at least

$$-\log p + \log k ,$$

with equality when it spreads *p* evenly. (A predictor that happened to favour the right row could be
luckier on a particular occasion; the bound is on what it can expect.) With a single unknown token the
selection term $\log k$ vanishes, but the first term does not: nothing ensures that the predictor puts
much probability on the one remaining token in the context where it belongs. With several, no amount of further description lowers the bound, since what is
missing is not information but the ability to use it.

Could negative information do the work instead? The output row of a never-seen token is not idle. By
the gradient given in section 2, after training it is its initial value minus a sum of small pushes
away from every internal state the model has visited,

$$u_t = u_t^{(0)} - \eta \sum_i p_t(x_i)\, h_i ,$$

so its logit in a new context with state $h^*$ shifts by $-\eta \sum_i p_t(x_i)\,(h_i \cdot h^*)$. The
shift is negative where the new state resembles visited ones, and *positive* where it points away from
them. An unseen token can therefore gain probability in contexts unlike anything seen, which is a
version of "it must be the one that is left". But this is not guaranteed, since it depends on where the
new context's state happens to fall, and nothing about the token's actual role enters the sum. The
limiting behaviour points the same way. Gradient descent on cross-entropy with separable data converges
in direction to the maximum-margin solution, a result proved for linear predictors and extended to the
multi-class case (Soudry et al. 2018). A token that is never the target is trivially separable from
every target, so its row grows along a direction fixed by the margin constraints on the data it has
seen, and every never-seen token is driven toward the same direction. (This application to unseen
classes is my own corollary, and it assumes fixed features, as the theorem does.)

Negative information also cannot settle *which* unseen token is which. Training treats token labels
symmetrically: swap the labels of A and B throughout, and the same procedure on the same data produces
the swapped model. If neither token appears in the data and their initial rows are drawn from the same
distribution, the distribution of trained models is unchanged by the swap. So no amount of training
without the token can make LLMary's predictor favour the right one of A and B, except through the luck
of its initial values. That symmetry is why the bound above is a bound on expectation.

The disanalogy with Mary should be stated plainly. A token's row is arbitrary, bearing no relation to its
role. Human colour vision is structured from its earliest stages, beginning with three types of cone, so
much of where red will fall may be fixed before Mary ever sees it. To that extent Mary faces less of a
selection problem than LLMary does. How much less is a question for vision science, which section 10
takes up.

## 6. Recognising, producing, imagining

Lewis lists the abilities that knowing what an experience is like confers: "you gain abilities to
remember and to imagine … Further, you gain an ability to recognize" (Lewis 1988). LLMary separates them.
Description supports recognising the token *in context*, by its role, and that is what Dennett's blue
banana dramatises: Mary knows bananas are yellow and knows how yellow and blue affect her, so she can tell
this banana is the wrong colour (Dennett 1991, pp. 399–400). Description does not support producing the
token. The output row that would let her emit it has never been the target of any training, so she cannot
bring it up unprompted.

Is producing a token the counterpart of *imagining* red? Not exactly. Emitting a token is closer to saying
a word, and a person could say "red" and describe the expected brain activity while being unable to
picture red at all. The closer counterpart is reinstating the token's internal representation without the
token being present: bringing up, in herself, the state the token would cause. Description cannot do this
either, for the same reason, but it is worth keeping the two apart, and even a model that could do it would
show only an analogy to imagery. Whether such reinstatement has anything to do with what an experience
feels like remains a philosophical question. Jackson insists that it is a separate one: "Imagination is a
faculty that those who lack knowledge need to fall back on" (1986, p. 292).

Two classic cases sit between recognising and producing. Hume grants that someone who knew every shade of
blue but one could "raise up to himself the idea of that particular shade, tho' it had never been conveyed
to him by his senses" (*Treatise* 1.1.1.10). Churchland suggests that a Mary who thinks of her inner life in
neuroscientific terms might imagine a cortical state "even in advance", as a trained musician can construct
a chord never heard (1985, pp. 25–27). Both produce a new item by interpolating within a *structured* space.
LLMary cannot do even that, because her rows have no structure to interpolate in. Whether Mary can depends,
again, on how structured her colour system is.

## 7. Four kinds of self-access

"Complete knowledge of oneself" hides four different relations a system can bear to itself.

- **Reading**: taking in a description of one's own make-up as data. A language model can read its weights
  only as text, and that gives her nothing usable, for the reason given in section 5.
- **Introspecting**: registering one's own current states. With introspection, a description of a vector
  could be matched against the activation the vector causes. Present models show at most a limited and
  unreliable capacity of this kind (Lindsey 2025).
- **Simulating**: working out what one would undergo, without undergoing it. LLMary can calculate the
  update the encounter would produce. Calculating an update is not undergoing it.
- **Writing**: changing one's own parameters directly, and so putting oneself into the state an experience
  would have produced.

Only writing changes the learner. This is Dennett's insight, credited to him: his Locked RoboMary installs
state *B* by calculation, and his Swamp Mary has the same state installed by a lightning bolt, which puts
her brain into "the dispositional state, the competence state" that seeing a red rose would have produced
(Dennett 2005). What the four-way distinction adds is the pause from section 1. RoboMary "figures out
exactly what it is like to see red" and "hence is not the least bit surprised", but figuring out is
simulation, and avoiding surprise needs writing. RoboMary stopped before her final adjustment is in
LLMary's position: she knows exactly what will happen to her, and it has not happened yet.

### ZenMary

A defender of the knowledge argument has an obvious reply to everything so far. Jackson's Mary is a
brilliant scientist, and LLMary is not. A dull enough person is surprised by anything, colour or no
colour, so a learner whose surprise could come from mere lack of intelligence is a poor model of Mary.
Her surprise at first light would show the limits of her reasoning, not the limits of physical
knowledge. The reply deserves an answer, and the answer is to make LLMary as resourceful as the case
allows and see what surprise survives.

Writing is the direct route to self-change, but there is an indirect one, which combines reading and
simulating with the ordinary channel of learning. Suppose LLMary can read her own weights exactly, can
run a copy of herself in inference mode, and can choose some of the text she is trained on. Call her
*ZenMary*, because she tries to point at something she has no word for by meditating on words that look
like nonsense.

ZenMary knows the output row $u_{123}$. Using her copy, she searches over strings $s$ of familiar
tokens for one that maximises $u_{123} \cdot h(s)$, the score the copy gives token 123 as the next
token after $s$. The search is a computation on numbers. Token 123 is never fed to the copy, and never
to her. Methods of this kind already exist. Rumbelow and Watkins (2023) generated inputs "that maximise
the output probability of the target completion", and adversarial-suffix search finds strings that
force a chosen reply (Zou et al. 2023). The strings found this way typically look like gibberish, which
is where ZenMary's koans come from. She then trains herself, on familiar text only, so that three
Shazams put her in a state close to $h(s^*)$, for instance by learning to continue the Shazams as her
copy continues the koan. The match is only approximate, since agreeing on familiar continuations does
not guarantee agreement in the direction of $u_{123}$, and a loss that matched internal states directly
would be closer to writing. But to the extent that it succeeds, she knows that on hearing three Shazams
she will meet something like *this*.

The method achieves a good deal. It performs the translation that section 5 said nothing in LLMary's
training rewards, turning "the row at index 123" into the geometry of her predictor, by an outside
procedure rather than a learned skill. Because the search aims at row 123 by its index, it also settles
which of A and B is the target, so both terms of the surprise bound fall. And it gives her one of the
three competences that make up binding, the ability to *produce* the token when the context calls for
it. What she has rehearsed is the state of being about to emit the token, which is closer to expecting
it than to undergoing its effects.

It cannot reach the input side. When token 123 finally arrives, it enters through its input row, and
that row has still never had a gradient, since ZenMary never fed the token in. Simulating its arrival
does not help: feeding 123 to the copy only runs the uninformative row, and there is nothing to learn
from that. She could train her later layers to continue correctly after three Shazams whatever vector
arrives, but that is the cue route of section 4, which fails the wrong-token control. So two
competences wait for first light: identifying the token in a neutral context, and predicting what
follows from the token itself. Self-tutoring can remove the surprise of predicting the token, but the
forced update on the input side survives everything short of writing its row.

This is the answer to the objection from stupidity. ZenMary removes every part of LLMary's surprise that
cleverness can remove, and what is left is not a failure of reasoning. It follows from the one-hot
encoding, which gives token 123 an input channel that nothing else can reach, however well the learner
reasons about it. A smarter LLMary would be no less surprised on the input side, because no amount of
reasoning trains a row that no input has touched. The residue is a fact about how she is built, not about
how well she thinks, and that is what makes it a fair model of what might remain for Mary.

For Mary the comparison is instructive, because she has something like ZenMary's trick inside the room.
Benham's top, a spinning disc patterned only in black and white, makes most observers see faint
colours (Benham 1894). Black-and-white stimuli, chosen with knowledge, can therefore drive a human
colour system, and on the *input* side. That works because human colour channels are shared with
achromatic input, through the same cones, whereas LLMary's input channel for token 123 belongs to index
123 alone, which is the one-hot point of section 2 again. The side that is closed to LLMary may be
partly open to Mary, and how far is once more a question for vision science. A defender of Jackson
will reply that ZenMary, like RoboMary, uses abilities her knowledge does not give her: a simulator,
and control over her own training. That is fair, but her abilities are much more modest than
RoboMary's, and a Mary who spins a top uses none at all beyond what the room provides.

## 8. Surprise

Surprise has done quiet work in the literature on Mary. Jackson takes her not saying "ho, hum" as evidence
that she lacked knowledge. Dennett runs the link the other way: his Mary had "already written down, in
exquisite detail" how colours would affect her, and so "was not in the slightest surprised". George Graham
and Terence Horgan's "Mary Mary", who also accepts a materialist theory of phenomenal content, "has no good
reason to expect surprise", yet "surely" she will be surprised (Graham & Horgan 2000, pp. 71–72).

LLMary occupies a position none of these quite takes: she *expects* surprise and is surprised. She can
calculate, in the fully informed case, that her predictor will give token 123 low probability and so incur
a large error, and when the token arrives it does. Her knowledge of the coming surprise and the surprise
itself are carried by different parts of her: the first by what she can say about herself, the second by
her predictor, which never consults what she can say.

Graham and Horgan come close to this. They concede that Mary Mary could "predict in advance … that she
will be surprised by her post-release color experiences", call this "beside the point", and ask instead
for an account of "why it is rationally appropriate for Mary Mary to find her post-release color
experiences surprising" (pp. 76–77). In a footnote they leave open whether "Mary Mary cannot both know that
she will be surprised in a certain way and be surprised in that way" (p. 85 n. 7). LLMary shows that she
can, once knowing and being surprised are seen to belong to different parts of one system. (Diana Raffman's
reply to Graham and Horgan also connects Mary's surprise to the formation of new perceptual
representations [Raffman 2005]; the model offers a setting in which that connection can be calculated.)

**What exactly is improbable?** The sharpest objection to all this is that Mary can be *certain* red is
coming. Suppose she picks the red patch, checks the apparatus and presses the release button herself. She
still looks and thinks, *so that's what it looks like*. If surprise is a low probability for an event, what
event did she find improbable? Not the arrival of red, which she predicted.

LLMary answers this directly, because her version of the case can be run. Put into her context the
sentence "the next token will be token 123". She is now certain, in what she can say, of what comes next.
Her predictor still cannot put probability on row A rather than B, so the token still arrives with low
probability and a large error. The improbable event is not "red arrives", described; it is the outcome at
the level of her own representations, which her certainty, held elsewhere, cannot reach. Mary's *so that's
what it looks like* is, on this account, the human counterpart: a large mismatch at the level of her colour
representations, unaffected by her certainty about the stimulus. The analogy has a weak point that should
be admitted. A model's predictor always gives every token some probability. Whether Mary's visual system
represented the outcome at all beforehand, rather than lacking the resources to formulate it, is a further
question about the brain.

**What surprise diagnoses.** Surprise alone is not a sign of a missing binding. A familiar token in a wildly
unlikely context produces high surprise in a model with a perfect binding. And a context cue can lower
surprise with no binding at all, as the Shazam cue does. What diagnoses a missing binding is narrower: the
part of the surprise that persists in the fully informed case *however much description and cueing the
learner is given*. That residue is what the selection bound of section 5 measures, and it is what writing
removes.

**The comparison with writing.** This gives the paper's central argument. Give two copies of LLMary the same
conditional knowledge: "without adjusting myself, my predictor will give token 123 probability *q*; with
the adjustment, probability *r*." One copy makes the adjustment and the other does not. Their knowledge is
the same; only one of them has written herself. The one that has not is surprised, predictably and to a
calculable degree; the one that has is not. The irreducible surprise tracks the binding, not the knowledge.
So in a fully informed learner, that surprise is rationally appropriate in the sense Graham and Horgan ask
for: it is an accurate signal that her representations needed adjusting, not an error, and not evidence of
a fact she lacked. Whether Mary's *felt* surprise is fully accounted for in the same way is the question the
model cannot settle by itself, and I return to it in section 12.

## 9. Jackson's real target: other people

Jackson's 1986 paper concedes the first-person part of all this in advance. Before release, he writes, Mary
"could not have known facts about her experience of red, for there were no such facts to know", and
"physicalism can happily admit that she learns this; after all, some physical things will change, for
instance, her brain states and their functional roles" (p. 292). The trouble, he says, is that she now sees
that all along other people's experiences "had a feature conspicuous to them but until now hidden from her"
(pp. 292–293). Since she knew all the physical facts about them, that feature is not physical.

So the question for LLMary is not only what she gains about herself but whether she gains something about
*other* models. Suppose she has studied other networks processing token 123 and knows every physical fact
about their states. After her own encounter, she has something she lacked: a representation of token 123
that is bound in herself, and so a way of representing what goes on in those networks *through* her own
state rather than only through descriptions of theirs. Before, she could describe their token-123 states;
now she can also think of them as being like *this*. What she has gained is a new way of representing facts
about them that she already had.

This is the old-fact-new-guise reply, which says that Mary comes to grasp known facts about others under a
new, first-personal concept. The model adds a mechanism for how the new guise is acquired and why no
description could supply it. It does not settle the dispute. A defender of the argument will say that the
feature "conspicuous to them" is a further fact, not a new way of representing old ones. But the model at
least shows how a learner can come to see others differently on release without learning any fact about
them she did not already have, and so it puts the burden on the claim that Mary's case is different.

## 10. Prewiring, and a test for learning

Whether Mary learns anything colour-specific on release depends on a fact about her brain: how much of her
colour pathway is fixed before colour experience. If her early colour system is wholly prewired, her first
sight of red engages it just as anyone's does, and there is nothing colour-specific for the encounter to
install there; she will still form memories of the occasion, as anyone does after any experience. If some
stages are shaped by colour experience, and she has no other way of setting them, then what happens there on
release is learning, whose details depend on how her brain learns. Knowing the state of those stages would
not help, since knowing is reading and reading changes nothing. Dennett adds that assuming Mary's colour
system survives confinement intact is itself "a nontrivial empirical assumption, given what is known about
the ready reassignment of unused cortical resources" (2005). The thought experiment does not settle what
happens to Mary. Vision science does.

For LLMary the question can be answered by an experiment, and the experiment gives the opening promise,
that she can be calculated, a concrete meaning. Take two copies of the same trained model, in the same
state. Give one a training example containing token 123 in its diagnostic context, and give the other a
matched example without it. Then test both, on fresh material, for the three competences of section 4:
identifying the token in neutral contexts, producing it when the context calls for it, and predicting what
follows it. Repeat with the roles of A and B swapped, and test again after further training to see what
lasts. The differences between the copies show which competences the encounter changed and whether the
change persists. In the human case the same logic applies in principle: what a first encounter teaches is the
lasting difference it makes, compared with what the same encounter does to someone already familiar with the
item.

## 11. Swamp Mary

Compare two Marys. Released Mary sees a red tomato, and a month later her brain is in a state *S*. Swamp Mary
never leaves the room, but lightning rearranges her brain into exactly *S*, including an apparent memory of
seeing a red tomato, false in her case. (The duplicate has to be complete, memories included, or the two
Marys differ in ways that raise other questions.) Does Swamp Mary know what red looks like?

I originally drew a dilemma from this case: either the knowledge is carried by the state the two share, and
so can be had without the experience, against the knowledge argument; or it depends only on a past event
that leaves no mark in Mary, which makes it undetectable from the inside. The dilemma is weaker than it
looked, for three reasons.

First, the first horn does not contradict the knowledge argument. The argument says that physical
*information* cannot give Mary the knowledge. Swamp Mary did not acquire information; she was put into a
state. So "she knows, though she never saw red" is compatible with Jackson's premise. Second, a dualist can
accept the first horn outright, holding that the same psychophysical laws give the two Marys' shared state
the same phenomenal character. Third, causal history may matter to *warrant*: Released Mary's judgement arose
through the encounter it registers, while Swamp Mary's arose by luck. And the false memory bears only on
what she knows *about an episode*, that she saw a red tomato, not on what she knows about how red looks.

What survives is still worth having. Whatever Mary gains on release, it is fixed by the state she comes to be
in, and that state is one no amount of information puts her in. That is the moral of the binding account,
reached from the other side. It does not show that the state lacks a non-physical aspect; a dualist can say
it has one. What it shows is where the question lies: not in a fact Mary was missing but in a state she had
not been in.

The case does keep real force against the view Jackson defended alongside the knowledge argument in 1982,
that qualia are epiphenomenal. In that paper he answers the worry that epiphenomenal qualia could not be
known in *other* people with an analogy of two newspapers reporting the same match: behaviour and qualia are
separate effects of a common cause in the brain (1982, pp. 133–135). He does not discuss how Mary knows her
*own* qualia after release. On his model, everything she later judges and says about red is caused by the
brain state she shares with Swamp Mary, and the quality itself does no work in producing it. What then grounds
her judgement about the quality? That is the familiar charge of self-stultification against epiphenomenalism,
in a form specific to Mary, and it gives the defender a definite question to answer.

## 12. What carries over

| Result | For LLMary | What carrying it to Mary needs |
|---|---|---|
| A physical gain on first encounter (§2) | a training update | nothing further; but it shows only that a gain can be physical, not that Mary's is |
| The gain is relational (§3) | the token's antecedents and consequents | the analogy between a token and a colour experience |
| Binding, defined by competence (§4) | identifying, producing, predicting | that Mary's new competences are of the same kind |
| Knowing versus using (§5) | the predictor cannot use what she can say | that a comparable split exists in Mary's brain |
| Selection bound (§5) | at least log *k* expected surprise | that Mary's colour space is as unstructured as a token's row, which it largely is not |
| Recognising, producing, imagining (§6) | recognition by cue, no production | that reinstating a representation corresponds to imagery |
| Four kinds of self-access (§7) | read, introspect, simulate, write | none: applies to Mary and RoboMary directly |
| Predicted, irreducible surprise (§8) | calculable, removed only by writing | that Mary's felt surprise is a representation-level mismatch |
| Other minds (§9) | a new way to represent other models | that Mary's new view of others is a new guise, not a new fact |
| Prewiring and the two-copy test (§10) | an experiment that can be run | facts from vision science |
| Swamp Mary (§11) | n/a | applies to Mary directly; strongest against epiphenomenalism |

The weak point is the same throughout: the analogy between LLMary and Mary. A phenomenal realist can accept
every result about the model and hold that Mary's gain contains a further component, acquaintance with an
intrinsic quality, with no counterpart in a training update. Graham and Horgan locate what delights Mary Mary
in "the unanticipated experiential basis" of her new capacities. Nothing here refutes that view. What the
model does is say what the further component would have to be like. If binding, or something like it,
accounts for what Mary recognises, imagines, predicts and reports, then the further component makes no
difference to any of these. It is fixed by the state she comes to be in, like everything else she gains. And
on an epiphenomenalist view, it does no work in producing her judgements about it. Whether something with
those properties is worth positing is the hard problem in miniature; the model's contribution is to make the
question precise.

## 13. Conclusion

Mary has been a puzzle about intuitions, and the intuitions are unreliable because the case cannot really be
imagined. LLMary can be calculated, and the calculation separates what the classic discussion fuses:
describing an encounter in advance and identifying what one meets; knowing something and being able to use
it; recognising, producing and imagining; predicting a change and undergoing it; knowing oneself and
rewriting oneself. Carried back to Mary, these distinctions suggest that what she gains on release is a state
no information could put her in; that her surprise is an accurate signal of a representation still to be
adjusted; that her new view of other people may be a new way of representing what she already knew; and that
how much there is to adjust is a question for vision science. None of this proves physicalism. It does show
that the knowledge argument's conclusion needs more than Mary's surprise to support it.

---

## References

- Benham, C. E. (1894). The artificial spectrum top. *Nature*, *51*. [Page numbers not yet checked.]
- Brown, T. B., Mann, B., Ryder, N., Subbiah, M., Kaplan, J., Dhariwal, P., … Amodei, D. (2020). Language
  models are few-shot learners. *Advances in Neural Information Processing Systems*, *33*, 1877–1901.
- Churchland, P. M. (1985). Reduction, qualia, and the direct introspection of brain states. *The Journal of
  Philosophy*, *82*(1), 8–28.
- Dennett, D. C. (1991). *Consciousness explained*. Little, Brown and Company.
- Dennett, D. C. (2005). What RoboMary knows. In *Sweet dreams: Philosophical obstacles to a science of
  consciousness* (pp. 103–130). MIT Press.
- Graham, G., & Horgan, T. (2000). Mary Mary, quite contrary. *Philosophical Studies*, *99*(1), 59–87.
- Hume, D. (1978). *A treatise of human nature* (L. A. Selby-Bigge & P. H. Nidditch, Eds.; 2nd ed.).
  Clarendon Press. (Original work published 1739–1740)
- Jackson, F. (1982). Epiphenomenal qualia. *The Philosophical Quarterly*, *32*(127), 127–136.
- Jackson, F. (1986). What Mary didn't know. *The Journal of Philosophy*, *83*(5), 291–295.
- Lewis, D. (1988). What experience teaches. *Proceedings of the Russellian Society*, *13*, 29–57.
- Lindsey, J. (2025). *Emergent introspective awareness in large language models*. Transformer Circuits Thread.
- Raffman, D. (2005). Even zombies can be surprised: A reply to Graham and Horgan. *Philosophical Studies*,
  *122*(2), 189–202. [Not yet checked against the paper.]
- Rumbelow, J., & Watkins, M. (2023, February 5). *SolidGoldMagikarp (plus, prompt generation)*. LessWrong.
  https://www.lesswrong.com/posts/aPeJE8bSo6rAFoLqg/solidgoldmagikarp-plus-prompt-generation
- Soudry, D., Hoffer, E., Nacson, M. S., Gunasekar, S., & Srebro, N. (2018). The implicit bias of gradient
  descent on separable data. *Journal of Machine Learning Research*, *19*(70), 1–57.
- Zou, A., Wang, Z., Carlini, N., Nasr, M., Kolter, J. Z., & Fredrikson, M. (2023). *Universal and
  transferable adversarial attacks on aligned language models* (arXiv:2307.15043). arXiv.
  https://doi.org/10.48550/arXiv.2307.15043

---

## Endnote: the argument in the web

Each section draws on nodes of the philosophy web, where the steps are stated separately with their
sources.

- §1: [knowledge-argument](../web/arguments/knowledge-argument.md), [what-does-mary-learn](../web/questions/what-does-mary-learn.md), [mary-misimagined](../web/arguments/mary-misimagined.md)
- §2: [llmary](../web/concepts/llmary.md), [llmary-token-encounter](../web/arguments/llmary-token-encounter.md)
- §3: [first-token-update-is-relational](../web/claims/first-token-update-is-relational.md), [llmary-relational-diagnosis](../web/arguments/llmary-relational-diagnosis.md),
  [mary-analogous-to-llmary](../web/claims/mary-analogous-to-llmary.md)
- §4: [zero-shot-few-shot-learning](../web/concepts/zero-shot-few-shot-learning.md), [description-binds-token-only-relationally](../web/claims/description-binds-token-only-relationally.md),
  [first-encounter-adds-binding](../web/claims/first-encounter-adds-binding.md), [llmary-binding](../web/arguments/llmary-binding.md)
- §5: [unknown-token-selection-bound](../web/claims/unknown-token-selection-bound.md)
- §6: [description-cannot-confer-token-production](../web/claims/description-cannot-confer-token-production.md), [ability-hypothesis](../web/arguments/ability-hypothesis.md)
- §7: [self-access-kinds](../web/concepts/self-access-kinds.md), [reading-own-weights-is-description](../web/claims/reading-own-weights-is-description.md),
  [write-access-installs-binding](../web/claims/write-access-installs-binding.md)
- §8: [surprise-predictable-yet-undergone](../web/claims/surprise-predictable-yet-undergone.md), [llmary-predicted-surprise](../web/arguments/llmary-predicted-surprise.md),
  [surprise-registers-missing-binding](../web/claims/surprise-registers-missing-binding.md)
- §9: [old-fact-new-guise](../web/arguments/old-fact-new-guise.md)
- §10: [mary-gain-depends-on-prewiring](../web/claims/mary-gain-depends-on-prewiring.md), [snapshot-test-first-encounter-learning](../web/claims/snapshot-test-first-encounter-learning.md)
- §11: [retention-dilemma](../web/arguments/retention-dilemma.md), [phenomenal-knowledge-needs-lasting-vehicle](../web/claims/phenomenal-knowledge-needs-lasting-vehicle.md),
  [epiphenomenalism](../web/positions/epiphenomenalism.md), [swampman](../web/arguments/swampman.md)
- §12: [mary-gains-acquaintance](../web/claims/mary-gains-acquaintance.md)

## Revision notes (not part of the article)

This version responds to the critique in `what-llmary-knows-critique.md`.

**Adopted.**
- The opening now starts from RoboMary's pause, and a single two-token example runs throughout.
- §2's first result is restated in the weaker form the critique proposes: a physical gain on first
  encounter shows only that such a gain *can* be physical. The earlier talk of "falsifying a conditional"
  is gone.
- Binding is now defined by three testable competences, with a control (the wrong token after the cue),
  and its location in the network is left open.
- The fully informed and hidden-assignment cases are separated (§5). The selection bound is now stated as
  an expected-loss bound, derived for the predictor's situation.
- Producing a token is no longer equated with imagining (§6).
- The self-chosen red patch objection is answered with the in-context version of the case (§8). The
  diagnostic claim is narrowed to the part of the surprise that no description or cue removes.
- The co-variation argument is restated with conditional knowledge (§8).
- A new §9 takes up Jackson's own statement (1986, pp. 292–293) that the trouble for physicalism concerns
  other people's experiences.
- The snapshot test is replaced by a two-copy experiment (§10), and the prewiring claim no longer says a
  prewired Mary learns nothing at all.
- The Swamp Mary dilemma is weakened (§11): its first horn does not contradict the knowledge argument, a
  dualist can accept it, and history may matter to warrant. What survives is stated, and its force against
  Jackson's epiphenomenalism is kept.
- §12 is now conditional, and node links are moved to an endnote.

**Not adopted, or adopted only briefly.**
- Gradient details: bounded logit gradients are left out. Tied versus untied embeddings were first cut to
  one sentence, then restored to §2 in the third revision, where they ground the point that the first
  encounter forces an update whatever LLMary knows. The point is derived from one-hot encoding and the
  softmax gradient, with no empirical citation. §2 now also introduces two versions, untied LLMary (the
  default) and tied LLMary, and treats tying as an inductive bias whose payoff at first light depends on
  whether its assumption is true. The first encounter is named *first light*. Later sections still say
  "first encounter" and could be switched to the new name.
- Separate tests for reinstating a representation are mentioned but not designed.

**Open before publishing.**
- Raffman (2005) is cited as the critique describes it and should be read and checked. A copy in
  `external/` would let me do that.
- The web nodes still state the stronger versions of three claims and need updating to match: the
  retention dilemma, the snapshot test, and the fact that the selection bound is an expectation.
- The empirical claim about the structure of early colour vision still needs a source.
- The Brown et al. page range is unverified. The Rumbelow and Watkins centroid claim and their prompt
  generation method are now checked against the post.
- Benham (1894): page numbers unchecked (one secondary source gives *Nature* 51, 113–114). Whether
  Benham's top has already been raised against the black-and-white room in the literature is unchecked.
- ZenMary (§7) is new in this revision and has no web node yet.
- The page range in `source-lewis-1988` (29–35) is probably wrong.
- None of the LLMary arguments has yet been attacked in the web by a realist character.

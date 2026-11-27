# First Light

### A dialogue on Mary, LLMary and ZenMary

*Working draft. Alice defends Frank Jackson's knowledge argument; Bob is a physicalist. The points about
language models are worked out in more detail in `what-llmary-knows-revised.md`.*

---

## 1. Two Marys

**Alice.** Let me state the case as Jackson gave it, so that we argue about the same thing. Mary is a
brilliant scientist who has spent her whole life in a black-and-white room. From books and a
black-and-white monitor she learns "all the physical information there is to obtain about what goes on
when we see ripe tomatoes". Then she is let out and sees a red tomato. It seems obvious that she learns
something, namely what it is like to see red. So her physical knowledge was incomplete, and since it was
all the physical knowledge there is, physicalism is false.

**Bob.** And her reaction is part of the evidence. Jackson says she "will not say 'ho, hum'".

**Alice.** Right. She is surprised, and the surprise is a sign that something new has come in.

**Bob.** My trouble with the case is Dennett's. Nobody actually imagines what the premise asks. "All the
physical information" is so immense that we picture a woman who has read a great many textbooks, and then
consult our intuitions about *her*. So I want to offer you a Mary we don't have to imagine, because we can
calculate her. Call her LLMary. She is a large language model, trained on every book about AI, the whole of
arXiv, the whole internet if you like. Language models read and write text in small pieces called tokens,
each with an index number in a fixed vocabulary. LLMary's vocabulary contains a token, say token 123,
which has never once appeared in her training text. But she has read everything anyone has written
*about* it: its index, the vector that represents it inside her, its statistics, even the training update
that would follow if she met it. It has been endlessly *mentioned* and never *used*. Then, during
training, it turns up. I'll call that moment *first light*, after a telescope's first observation.

At first light two things happen, each with a precise meaning. She is surprised: the probability she gave
the token was close to zero, so her loss, the measure of her prediction error, is enormous. And she
learns: the training step changes her weights. Every part of this is physical, and before it she knew
everything that can be said about the token.

**Alice.** I have two objections already. First, LLMary has no experience at all, so she can't be a model of
learning what an experience is like. Second, her surprise may be nothing but a failure to put her
knowledge together. A dull enough person is surprised by anything.

**Bob.** Both deserve answers, and I'll give them, the second one first, once we've seen what LLMary has to
learn. Hold me to it.

## 2. What there is to learn

**Bob.** From the text alone, there are exactly two things LLMary can learn about token 123. One is in what
contexts it appears: what comes before it. The other is what appears once it has been seen: what comes
after it, which may be familiar tokens or yet newer ones. Its place as an effect, and its place as a
cause.

**Alice.** That's true of anything one learns about, surely.

**Bob.** It is, and that's why it carries over. The experience of red has antecedents, the stimuli and
states that bring it on, and consequents, what it leads Mary to expect, say and do. But in a language model
the two have separate homes, and that is what lets us calculate. Each token has two learned vectors. Its
*input embedding* is looked up when the token appears in the text she is reading, and it fixes what
difference the token makes to what follows. Its *output embedding* is what her internal state is compared
with when she scores the token as a candidate for the next position, and it fixes where she predicts it.

**Alice.** And neither has been trained for token 123.

**Bob.** It's more exact than that, and the two sides differ. A token enters the network as a *one-hot*
vector: all zeros, with a single 1 at its index. Its input embedding is just the row of a matrix that the 1
selects. In training, the correction that reaches any row is multiplied by that row's entry in the one-hot
vector. So a row gets no correction at all unless its token is actually in the input. The input row for
token 123 is still whatever it was set to at the start, a random vector. And notice what that means.
Everything LLMary knows about token 123 is stored somewhere: in the rows of the words used to describe it,
and in the layers that process those words. None of it can reach row 123, because no correction from text
that only *mentions* the token ever lands there. So however much she knows, about the token, about Mary,
about her own weights, at first light the token enters her as a vector that carries no information about
it, and the first training step must change that row. Mentioning is not using, and on the input side
that's arithmetic.

The output side has been trained, but only in one direction. At every step, the probabilities of all the
tokens that were not the actual next one are pushed down. A token that is never the next one is only ever
pushed down. Its row learns that it doesn't occur, which is true, but says nothing about where it belongs.

## 3. The Shazam cue

**Bob.** Now let me make the example concrete. Suppose LLMary has two tokens she has never processed. Call
their rows A and B. She has read that exactly one of them, token 123, is the word-piece that always follows
three "Shazam"s in a row.

**Alice.** Why three? Why not just "Shazam"?

**Bob.** Because of the same distinction. "Shazam" is a familiar word. If token 123 followed a single
Shazam, then any text describing its role would have to *use* the word, and so would contain the trigger
followed by something other than token 123. So would every unrelated "Shazam" anywhere in her training.
The description would spoil the very context it describes. Three in a row is a combination that never
occurs in her training, so it can be described without being produced, just as token 123 can be mentioned
without being used.

**Alice.** So the Shazams also tell her when the token is coming.

**Bob.** Yes, and that matters for her surprise. It splits into two parts: surprise *that* something new
appears now, and surprise at *which* new thing it is and what it is like. The Shazams remove the first
part. Without a warning, some of her surprise would just be surprise at a sudden change.

**Alice.** I accept that, and I'll accept the same for Mary. Let her release be announced: "In one minute you
will see a ripe tomato." Jackson's point survives. She will still be surprised by what she sees.

**Bob.** Then we agree that only the second part counts. Let's see how much of it there is.

## 4. Elimination

**Alice.** Your two-token setup is doing a lot of work. Give her a single unseen token, and elimination
should find it. Negative information is information. If token 123 has been pushed down everywhere it
doesn't belong, then it is pushed relatively *up* where it does belong.

**Bob.** I hoped so too, but it isn't guaranteed even then. Add up all the pushes, and in a new context the
token's score goes down if that context resembles ones she has seen, and up if it points away from all of
them. So an unseen token can gain probability in contexts unlike anything seen, which is a kind of "it must
be the one that's left". But whether that happens depends on the geometry of the new context, and nothing
about the token's actual role enters the sum. A known theorem says the same in the limit: training of this
kind drives the weights toward a maximum-margin solution, and applied to a token that never appears, it
pushes the token's row in a direction fixed by everything *else*. Every unseen token is pushed the same
way.

**Alice.** So with one unseen token she may be lucky.

**Bob.** She may. With two she can't even be systematically lucky. Training treats the tokens' labels
symmetrically: swap A and B everywhere and the same procedure on the same data gives the swapped model. If
neither appears and they started out alike, nothing in training can make her favour the right one, except
chance in their random starting values. With several unknown tokens there is a part of her surprise that no
further description can lower.

## 5. Description and encounter

**Alice.** Grant all that. She can still *recognise* token 123. If she meets three Shazams followed by an
unfamiliar token, she can infer that it's token 123.

**Bob.** From the cue, yes. But put the wrong unfamiliar token, B, after the Shazams, and she'll take B for
token 123 just as confidently. The cue tells her what belongs in the slot, not which item is in front of
her. Call that the *wrong-token test*. What first light gives her, I'd say, is a *binding* of the role to
the token itself, and I'd define it by three things it lets her do: identify the token in a neutral context
with no cue, produce it when a context calls for it, and predict what follows from it. Description gives
her none of the three.

**Alice.** She can't even produce it? She knows which row it is.

**Bob.** She knows it in words. Ask her "which row follows three Shazams?" and she will say "the row at
index 123". But for the part of her that predicts to put probability on that row, it would have to produce
an internal state lined up with that particular vector, and nothing in her training has ever rewarded
translating "row 123" into the geometry of her own network. The information is in her, but the part of her
that predicts can't use it. Call it the *translation problem*.

**Alice.** That sounds like Churchland's old reply to Jackson. Mary has every true proposition, but no
representation of red in her "prelinguistic medium of representation for sensory variables".

**Bob.** It is Churchland's reply, with a mechanism attached. And it lets us be careful about kinds of
learning. Learning from a description differs from learning from an example. Learning by changing one's
weights differs from learning inside a single conversation, with the weights fixed. A model with fixed
weights can relate a new token to its neighbours for the length of one prompt, but the competence is gone
when the prompt is. LLMary before first light has learned from description, in her weights. First light is
a single example, also in her weights.

**Alice.** Now let me test your test on Mary. Dennett imagines her captors showing her a banana painted
blue, and says she would know at once that it was the wrong colour.

**Bob.** And that's the wrong-token test for Mary. If her knowledge of colour is attached to objects and
situations, to bananas and tomatoes and the opening door, she will expect yellow and take what she sees
for yellow, as LLMary takes B for 123. To pass, her knowledge must be attached to the colour state itself.
Short of having been in that state, the only way is to notice the state she is in and compare it with her
description of what yellow does to her. That's introspection, which is a third thing, neither binding nor
reading.

**Alice.** And Mary, being human, can introspect.

**Bob.** Somewhat. Present language models, by the best evidence, only a little and unreliably. But the point
is that the blue banana tests binding or introspection, not knowledge.

## 6. "So that's what it's been like"

**Alice.** Suppose I grant all of that. Mary passes the blue banana test, and she is exactly as surprised as
she expected to be. Yesterday she knew everything about my visual system. Today she turns to me and says,
"So *that's* what it's been like for you." Jackson's point was never only about Mary. He says that on
release she will realise "how impoverished her conception of the mental life of others has been all
along". Other people's experiences had "a feature conspicuous to them but until now hidden from her". What,
in your model, corresponds to the word "that"?

**Bob.** Her own state, newly bound. Suppose LLMary has studied other networks processing token 123 and knows
every physical fact about their states. After first light she has something she lacked: a representation of
token 123 that works *in her*. So she can represent what goes on in those networks through her own state,
and not only through descriptions of theirs. Before, she could describe their token-123 states. Now she can
also think of them as being like *this*. "That" points at a state of hers, and she uses it to model them.

**Alice.** Then she has learned something about them: that they have states like *this*. That's a new fact
about other people.

**Bob.** It's a fact she already had, that their states have such-and-such structure, now held under a new
concept, one that points at her own state. It's the old reply that Mary learns old facts in a new guise.
What LLMary adds is an account of how the guise is acquired, and why no description could supply it: the
guise is the binding.

**Alice.** And I say the guise presents something. When Mary says "*that*", she isn't pointing at her own
brain. She's pointing at a quality, and the quality was conspicuous to me all along and hidden from her.
Your binding explains how she comes to point. It doesn't tell me that there's nothing there to point at.

**Bob.** Then that's the question between us, and I'll keep it in view.

## 7. Tied LLMary

**Alice.** Let me try to close your gap from another side. Some models use the same matrix for input and
output embeddings. Then training on the output side does reach the input row, and your arithmetic no longer
protects it.

**Bob.** Call that model Tied LLMary. It's tempting to think tying just mirrors the way these models run,
in which each token is first predicted and then read back in. It doesn't. That loop is closed by the token's
*identity*, its index passed from one step to the next, and it works the same with or without tying. Tying
adds an assumption: that the vector by which a token is anticipated is the vector by which, once it
arrives, it acts on what follows. In effect, that tokens which appear in similar contexts make similar
differences afterwards. For language that's roughly true, but not exactly. "Of the" is common and "the of"
is not.

**Alice.** But she'd learn less at first light.

**Bob.** She has no head start beforehand, because her shared row has had only the push-down that every
unseen token gets. But at first light, the update that teaches her what leads up to the token lands on the
row that governs what the token does, so one lesson does double duty. If the assumption holds for token
123, she has less left to learn afterwards. If it fails, she has more, because she must undo what the
assumption supplied. The saving isn't knowledge she had. It's a bet built into her architecture.

**Alice.** And you'll say Mary's visual system is full of such bets.

**Bob.** It is. Whatever structure her colour vision has before release works the same way. To the extent it
matches the world, she has less to learn, without knowing any more. That bias is a fact *about* her, not a
fact she knows, and your premise is only about what she knows.

## 8. The objection from stupidity

**Alice.** Then here is my second objection, in full, since you promised to answer it. Jackson's Mary is a
brilliant scientist and LLMary is not. If her surprise might come from limited reasoning, it tells us
nothing about the limits of physical knowledge. You've shown that a weak learner can be surprised, which
nobody doubted.

**Bob.** The way to answer that is to make her as clever as the case allows and see what surprise is left.
The cleverest Mary in the literature is Dennett's RoboMary, a robot colour scientist whose colour system is
locked. She knows everything about her own design, works out the internal state she would be in after
seeing a red tomato, then "makes all the necessary adjustment and puts herself into state B". When her
colour cameras are switched on, "there are no surprises for her".

**Alice.** And RoboMary cheats. Michael Beaton made the point: a knower who is entitled only to what her
knowledge gives her may not also have the power to rebuild herself. Writing your own weights is not a
consequence of knowing them.

**Bob.** Then I'll keep that rule: no writing. Here is a Mary who never writes her weights. She can read
them exactly, she can run a copy of herself, and she can choose some of the text she is trained on. I call
her ZenMary, because she tries to point at something she has no word for by meditating on words that look
like nonsense. Her first method is a search. She knows the output row for token 123 as numbers, so using
her copy she searches over strings of familiar tokens for one that makes the copy give token 123 a high
probability next. It's a calculation, and token 123 is never fed to anyone. Researchers already find such
strings, and they look like gibberish, hence the koans.

But she can do better. She builds training sequences from what she has read: three Shazams, then token 123,
then what follows it. Token 123 appears in them only as an index. She trains her *copy* on them. The copy
has, in effect, had first light. Then she trains herself to match the copy's predictions, context by
context, using only familiar tokens. That is called *distillation*, and it dissolves the translation
problem, because the copy is in her own coordinates. The predictions she matches include probabilities for
token 123 itself. When the copy says "after three Shazams, token 123, with high probability", the
correction lands on her output row exactly as it would if token 123 had really been the next token, only
spread thinner. So she learns where the token belongs, she settles which of A and B it is, and at first
light she is hardly surprised that it comes.

**Alice.** Then your example collapses.

**Bob.** Look at the input side. When token 123 finally arrives, it enters through its input row, and that
row has still never been corrected, because she never had the token in her input. She knows, from her copy,
what tends to follow the token. But to put that inside herself she has to train on examples, and examples
without the token can teach her directly only what follows *three Shazams and something*. That knowledge
sits in her attached to the Shazams rather than to the token.

**Alice.** That sounds like a distinction without a difference.

**Bob.** The wrong-token test makes the difference. Put B after the Shazams and she predicts the same
continuation. But I have to be careful here. What never changes before first light is the row itself, the
vector token 123 arrives with. The layers that *read* that vector are shared with every other token, and
she can train those. And she knows the vector's value, because she can read her weights.

**Alice.** So she can prepare her network to respond correctly to a vector she has never received.

**Bob.** In principle she can try. Every training step on familiar text changes how her layers respond to
*every* vector, including that one. Using her copy, she can calculate those side effects and choose training
text whose side effects move her response to token 123 where she wants it. Researchers who poison training
data do something like this: they craft harmless-looking examples whose effect on training mimics a
forbidden one. Whether it can be done exactly, without disturbing everything else she knows, nobody can
promise. There's no guarantee either way.

**Alice.** Then your residue may vanish if she's clever enough.

**Bob.** And either outcome suits me. If some residue survives her best efforts, it's a fact about how she is
built, not about how well she reasons. If nothing survives, then a clever enough LLMary prepares herself
fully by legitimate means, with no first light at all, and Dennett was right about Mary. Your objection
assumed only two sources of surprise in a knower who has every fact: bad reasoning, or a missing fact.
Architecture is a third, and if cleverness can get round the architecture, there's no surprise left to
explain.

**Alice.** You're forgetting a third outcome. This preparation is RoboMary through the back door. She isn't
writing her weights, but she's choosing her training text *in order to* set them, by calculation. That's
writing with extra steps.

**Bob.** Then you'll have to say where ordinary learning ends and writing begins, because every student who
chooses what to practise is doing a mild version of the same thing. Let's come back to that when we discuss
the rules of the room. But notice one thing first. You said her surprise is explained by her limits. That's
the physicalist's diagnosis of Mary. If you explain LLMary's gap by her limits, you've accepted the pattern
of explanation. To win, you need to show that Mary's gap has a *different* source from LLMary's.

**Alice.** Then here's a difference. ZenMary's distillation gave her probabilities over tokens, including
the one she has never seen. That isn't reading about token 123. It isn't seeing it in her input either. It's
something in between.

**Bob.** I agree. There are three ways a token can reach LLMary. It can be *mentioned*, in text about it, and
nothing reaches its rows. It can be *used as a target*, as in distillation, and its output row is corrected.
Or it can be *used as an input*, and its input row is corrected. Only the last is first light proper.
Distillation is half an encounter, the output half.

**Alice.** And humans can't have half an encounter.

**Bob.** No, and the reason is interesting. In LLMary, what she reads and what she is corrected against are
separate channels. In a human, on the predictive-processing view of perception at least, they are one
channel. The brain predicts its incoming signal, and the correction is computed against the signal itself.
You can't give Mary a target for red without giving her red.

## 9. What counts as cheating

**Alice.** Then I'll say what follows from that. Half an encounter is an encounter. ZenMary hasn't stayed in
the room.

**Bob.** Let me press you on the room, then. Mary has an equivalent of the trick available. Benham's top is a
spinning disc patterned only in black and white, and most people who watch it see faint colours. Black-and-
white stimuli, cleverly chosen, can drive a human colour system.

**Alice.** Then Jackson should have said "a room in which she never sees colour", not "a black-and-white
room".

**Bob.** And ZenMary has a back door of the same kind. Run her in generative mode, writing out her reasoning
as models do. After distillation she gives token 123 a high probability after the Shazams, so sooner or
later she writes it, and whatever she writes is read back into her as input. She has given herself first
light from inside the room.

**Alice.** That is cheating, and so is the top. Both peek at the new data early. If those are allowed, Mary
might as well prick her finger, or set the room on fire, and look. When she steps outside she'll say "I knew
what red looks like", and she'll be right, and it will prove nothing, because she learned it the ordinary
way. She only did it early.

**Bob.** Agreed. So we need a rule for what Mary, and LLMary, may do. It can't be "no coloured objects",
since the top and the finger get round that.

**Alice.** The rule is that she must never undergo the experience. Whatever the stimulus, she must never be in
the state of seeing red.

**Bob.** For LLMary, then, the token must never be in her input, and you've also ruled out the target
channel, since half an encounter is an encounter. So she may read anything that *mentions* the token, and
she may calculate with its vector as numbers. She may not write it and read it back, and she may not be
trained against it. Your rule for the room is the line between use and mention that I've been drawing all
along.

**Alice.** That's not a concession. It's the point. Some knowledge is available only by being in the state, and
that's what "knowing what it is like" means.

**Bob.** Then let's sort the methods, because the hard cases are in the middle. Reading and reasoning: allowed
by everyone. Pricking her finger, the top, ZenMary writing her own token: forbidden, since each is the
encounter by a side door. Distillation: forbidden by your rule, though it is ordinary learning for LLMary.
And then Hume's missing shade. Hume grants that someone who knew every shade of blue but one could "raise up
to himself the idea of that particular shade", by filling the gap between its neighbours. Mary might do the
same for red, if her colour space is structured enough.

**Alice.** Imagining is borderline. Jackson's line is that "imagination is a faculty that those who lack
knowledge need to fall back on".

**Bob.** And the preparation from before, ZenMary choosing familiar text to shape how she will respond to
token 123? It uses only familiar tokens, so your rule allows it.

**Alice.** My rule forbids being in the state. If her preparation puts her into the state the token would
leave, it's forbidden however she got there. If it doesn't, it hasn't done the job.

**Bob.** Then your rule forbids whatever would work, and the argument's conclusion has become the rule. If
what's forbidden is *being in the state*, by any route, then "she can't know what it's like until first
light" says she can't be in the state until she is in it. That's true, and no physicalist denies it. The
argument needs more: that being in the state gives her a *fact* she lacked, rather than a capacity, a
representation, a binding. And notice that the rule depends on the architecture. Distillation is ordinary
learning for LLMary. The human equivalent would be setting Mary's colour expectations directly, which is
writing, and we both rule that out. So "learning by legitimate means" isn't a fixed list. It depends on which
channels a learner's ordinary learning uses.

**Alice.** The rule is doing honest work. It separates what can be learned by description from what can't, which
is what Jackson wanted.

**Bob.** It separates *routes*. Whether what comes down the forbidden route is a fact is the question we started
with.

## 10. The countdown flash

**Bob.** Let me put that to a test. Suppose Mary isn't released into a world of colour. She hears a countdown,
and at zero she sees a single red flash, once. LLMary's version is three Shazams and one occurrence of token
123. Everything predictable about that event can be attached to the countdown: that something comes, which
colour, and what follows, her report and her associations. A ZenMary who keeps to your rule can't distill,
but she can still use the cue. She can learn, from text, what follows "countdown, flash" and attach it to the
countdown. Her prediction error in what she says and does can be close to zero. So she honestly says "ho,
hum".

**Alice.** Then her "ho, hum" proves nothing. She still doesn't know what red is like.

**Bob.** I agree. So her surprise can be absent while the gap remains.

**Alice.** I never said surprise was proof. I said it was a sign. Signs can be suppressed. A poker player
holding a royal flush shows nothing, and he still knows something new.

**Bob.** Fair. Then the countdown shows only that the sign is optional. But it does mean the argument can't
rest on her reaction, only on what she knows. And it tells us where to look for a sign that can't be
suppressed. Surprise has levels. The countdown can remove surprise in what she reports. It probably can't
remove surprise in her early visual system, which receives a signal it has never processed, whatever she
expects. That is the input side again, and Beaton points to such low-level differences too.

Jackson's colourful world also does work his story never mentions. Released into it, Mary sees colour for
days, in contexts nobody announced. That's where knowledge attached to cues breaks down, because the world
keeps running the wrong-token test on her. And LLMary says something about those days. First light is the
*first* correction, not the whole of what she learns. The token keeps appearing, and she keeps learning,
almost all of it on the input side: how the new signal is processed and related to everything else. In
human terms that is perceptual learning. So I'd predict that what red is like for Mary is not fixed at the
moment of release. It should change over days or weeks as she learns to see.

**Alice.** That would be a fact about how she sees, not a refutation of what she learns in the first moment.

**Bob.** Agreed. It's only a prediction, and an empirical one. But it shows that "she learns what red is like"
names a process, which your story compresses into a moment.

## 11. Is the residue a fact?

**Alice.** Then let me take up my first objection, in its strong form. LLMary has no experience. Whatever
happens in her input row, nothing is like anything for her. So your model of Mary leaves out the one thing
Mary gains.

**Bob.** I don't claim LLMary is conscious. I claim she models the *structure* of what happens at first light:
what can be known beforehand, what can't, and why. The question between us is whether Mary gains anything
beyond that structure. So tell me what the further thing is, and where it is.

**Alice.** It is knowledge of a fact: what seeing red is like.

**Bob.** Here's a test. Compare Mary's brain just before first light, just after, and long after, once the slow
learning has settled. If the connections differ, learning took place, by definition. If they don't, nothing
colour-specific was learned, apart from the memories anyone forms of any occasion. Which it is depends on how
much of her colour system is fixed from birth and how much is shaped by colour experience. If it's wholly
prewired, first light engages it as it would anyone's, and there's nothing for it to install. If parts start
in a state she can't set, what happens there is learning, and its details depend on how her brain learns.
Knowing the state of those parts wouldn't help her, because knowing is reading, and reading changes nothing.

**Alice.** I can accept your snapshots and still say that Mary's knowledge of the phenomenal fact is something
they don't capture.

**Bob.** Then you're saying Mary *knows* something that leaves no mark on her brain. That's a much harder claim
than saying she is conscious of something. Consciousness you can locate in the experience. Knowledge she must
carry about afterwards, and use, and act on. Knowledge that leaves no trace in the knower comes very close to
the paranormal.

**Alice.** Not if the knowledge depends on her history. Imagine a Swamp Mary, a molecule-for-molecule duplicate
of Mary after her release, made by a lightning strike. She has never seen red. Does she know what red is
like?

**Bob.** Then let's be clear that she is a full duplicate, with every memory trace Mary has, including the
memory of seeing the tomato, which in her case is false. Like Neo in *The Matrix*, who wakes up knowing kung
fu, except that she would also seem to remember learning it. Either she knows what red is like, in which case
knowing it doesn't require ever having seen red, and that suits me. Or she doesn't, and the knowledge depends
on a past event that left no trace in the person who knows.

**Alice.** The first horn doesn't refute me. A dualist can say the lightning installed the phenomenal knowledge
too.

**Bob.** Fair. But the second horn asks a lot, and it sits badly with Jackson in particular. He thought the
qualities of experience have no physical effects. If the knowledge depends on an event that left no physical
trace, it's hard to see how it could make a difference to anything, even to what Mary says about red.

**Alice.** History might matter to whether her belief is *warranted*, even if not to what she believes.

**Bob.** That's a good reply. But then what Swamp Mary lacks is warrant, not the content of the belief.

**Alice.** If knowledge requires warrant, lacking warrant is lacking knowledge. Swamp Mary believes something true
about red and doesn't know it. That's my point: knowing what red is like depends on her history, not only on
her present state.

**Bob.** Then look where that puts the missing thing. Swamp Mary has the content: whatever Mary believes about
red, her physical duplicate believes it too. What she lacks is the right history, and history is causal, so
it's physical as well. A non-physical fact can't be in the content, and it can't be in the warrant.

**Alice.** Unless the warrant is acquaintance. Real Mary's history includes having been acquainted with a
quality. Swamp Mary's doesn't. The event left only physical traces, but what it acquainted her with need not
be physical.

**Bob.** Then the quality left no trace of its own, only traces of the event, and Jackson's own view was that it
has no physical effects at all. I don't see how you'd ever know it was there.

**Alice.** By having been acquainted with it. That's not a proof, I grant. But it isn't nothing either.

## 12. Where they stand

**Alice.** I'll grant you this much. Knowing everything that can be said and still gaining something at first
light doesn't, by itself, show that the gain was non-physical.

**Bob.** And I grant that I haven't shown Mary learns no new fact. I've shown that the gain can be described
without one: much of it can be had in advance by legitimate means, and the rest is a channel that only use
opens, or else cleverness closes the gap altogether.

**Alice.** We still disagree about "that". You say it points at her own state. I say it points through her state
at something she was missing.

**Bob.** Yes. That's where we've got to.

---

## Notes (not part of the dialogue)

- Sources are those of `what-llmary-knows-revised.md`: Jackson 1982 and 1986 (the other-minds quotations in
  §6 are from 1986, pp. 292–293), Dennett 1991 and 2005, Churchland 1985, Hume's *Treatise* 1.1.1.10,
  Beaton 2005, Soudry et al. 2018 (the margin theorem, §4), Rumbelow & Watkins 2023 and Zou et al. 2023
  (prompt search, §8), Benham 1894 (§9), Lindsey 2025 (introspection in models, §5). Quotations are those
  verified for the article.
- New source for §8: the data-poisoning precedent is Geiping, J., Fowl, L., Huang, W. R., Czaja, W., Taylor,
  G., Moeller, M., & Goldstein, T. (2021). Witches' brew: Industrial scale data poisoning via gradient
  matching. *International Conference on Learning Representations*. https://arxiv.org/abs/2009.02276
- Benham (1894): page numbers still unchecked.
- New relative to the article, and not yet in it: self-distillation as ZenMary's main method; preparing the
  layers that read token 123's untrained row, and the dilemma it gives Bob (§8); the three ways a token can
  reach a model; the cheating rule and its dependence on architecture; the announced release; the blue
  banana as the wrong-token test; the countdown flash and levels of surprise; first light as the start of
  perceptual learning; the warrant and acquaintance exchange on Swamp Mary.
- The prediction in §10 is stated without a citation. Studies of people given sight late in life may bear on
  it, but none has been checked.
- Consistency notes: Alice's two opening objections are answered in order, the stupidity objection in §8 and
  the no-experience objection in §11. Alice treats surprise as a sign throughout (§1, §10) and never as proof.
  Her concession of the announced release (§3) is kept afterwards. Her rule "never in the state" (§9)
  includes the target channel because of her claim that half an encounter is an encounter (§8), and it rules
  on ZenMary's preparation by its result, not its route. The countdown ZenMary in §10 therefore uses only
  cues, not distillation. The "that" question raised in §6 is the disagreement left standing in §12.

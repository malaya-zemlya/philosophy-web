# LLMary: working notes (session of 24–27 Nov 2026)

Notes, not prose for publication. They collect points raised after the "First Light" dialogue
(`drafts/llmary-dialogue.md`) and the revised article (`drafts/what-llmary-knows-revised.md`) were
drafted. Nothing here has been folded into either yet.

## 1. Two technical clarifications

**"Nothing after the token."** The input row $e_{123}$ is corrected only by losses at positions
*after* 123 (the causal mask keeps the loss on predicting 123 itself away from $e_{123}$). So if 123
were the last token she trains on, first light would be one-sided: the output row learns *that* 123
came, the input row learns nothing from *reading* it. For LLMary this needs a contrived setup (a
window cut exactly at 123); in ordinary training an end-of-text token or the next document always
follows. LLMary is assumed to be in training mode throughout (the dialogue says "she keeps
learning"; the only inference-mode run in either draft is ZenMary's *copy*). For Mary the caveat
cannot arise unless she dies at the flash: experience has no end of sequence, and the afterimage, her
"oh!", and the next moment are all "next tokens". Decision: not worth mentioning; it is an
engineering detail with no counterpart in Mary.

**Weight decay.** With decoupled decay (AdamW, or SGD with an L2 penalty), an untouched row is
multiplied by $(1-\eta\lambda)$ each step: still Gaussian, smaller variance, same random direction.
"Still random" is correct. (Exception, obscure: Adam with L2 folded into the gradient gives roughly
sign(w) steps toward zero, which is not pure scaling. Some setups exempt embeddings from decay
altogether.) The reviewer's rewording was a nitpick; rejected.

The Fable review of the dialogue (16 items) was provisionally **not** accepted.

## 2. Zombie Mary

- The case is Chalmers's, not Dennett's: "Phenomenal concepts and the explanatory gap" (2007, in
  Alter & Walter, eds., *Phenomenal Concepts and Phenomenal Knowledge*), https://consc.net/papers/pceg.html.
  Zombie Mary gains abilities ("to perceptually classify red things together") and indexical
  knowledge ("I am in this state now"), but "all is dark inside", so no substantive knowledge.
  She is the hinge of his master argument against the phenomenal concept strategy: whatever
  physical feature of concepts the physicalist names, Zombie Mary has it too, yet her epistemic
  situation differs from Mary's.
- Balog's (1999) "Yogis", with direct recognitional concepts of their own brain states and no
  phenomenal quality, are even closer to LLMary pointing at row 123. Chalmers: a Yogi gains only
  "trivial knowledge" ("that sort of brain state is that sort of brain state"). His footnote: a
  Yogi's question closes once the triggering brain state is found; ours stays "wide open". That
  footnote restates the disputed intuition; it is where Bob should push.
- Physicalists answer consistently. Dennett: a physical duplicate of Mary *is* Mary; there is no
  Zombie Mary. Type-B (phenomenal concept) physicalists: zombies are conceivable but impossible.
  But conceivability is all Chalmers's argument needs, so "impossible" does not get them out.
  Their third listed reaction, denying that Zombie Mary is conceivable, is Dennett's.
- Anti-physicalists are pulled two ways: (a) she learns nothing, there is nothing it is like;
  (b) she plainly learns (abilities, memories, a recognitional concept, real surprise) and sincerely
  argues Alice's case. Taking (a) means the ability hypothesis fully explains everything observable
  about Mary, including her reports: Chalmers's *paradox of phenomenal judgment* (*The Conscious
  Mind*, 1996, ch. 5), and a direct consequence of Jackson's 1982 epiphenomenalism.
- Unless Alice thinks LLMary conscious, **LLMary is Zombie Mary by Alice's own lights**. Alice's
  cleanest line: "granted, all of it; the phenomenal fact is extra." Bob's reply: "then the extra
  is not why you say there is an extra."
- Moody's Zombie Earth presses from another side: zombies with no contact with conscious beings
  would arguably never invent experience-talk, yet a physical duplicate of our world must produce it.

## 3. The asymmetry problem ("chosen ones")

- Chalmers: when I say "experience" I mean it; my zombie twin, saying the same words for the same
  physical reasons, means something else or nothing, and is unjustified. User's parody: "I and my
  friends are the chosen ones. How do I know? It's the most obvious thing ever. Others who claim it
  are speaking of something else."
- Not strictly no-true-Scotsman: the distinction is fixed in advance by the definition of a zombie,
  not moved after a counterexample. And meaning-splitting between internal duplicates is
  respectable (Putnam's Twin Earth: H₂O vs XYZ).
- Where it really is strange: (1) the Twin Earth difference can be found by chemistry; the zombie
  difference by nobody, from inside or out; (2) Twin Oscar is as justified as Oscar, while Chalmers
  needs Zombie Mary's "aha" to be *unjustified*; (3) applied to himself, he cannot tell he is not
  the zombie. His answer, acquaintance, makes justification something with no causal or behavioural
  trace.
- Within our world Chalmers excludes no one: psychophysical laws give experience to everyone with the
  right organization; the exclusion is only across worlds. But to credit *you* with consciousness he
  must reason from your physical/functional likeness to him. So acquaintance does work in exactly
  one case, his own: a chosen *one*.
- "Only humans named David are conscious": he can reject it by (a) simplicity of fundamental laws and
  (b) organizational invariance (fading/dancing qualia, *The Conscious Mind* ch. 7). But every datum
  in consciousness science is a *report*, and zombie worlds produce the same reports. So
  calibration needs a pre-experimental bridging principle (reports track experience: "structural
  coherence"; his 1998 NCC paper calls such principles pre-experimental), which the zombie argument
  denies across worlds. His estimation procedure is a functionalist's; the non-physical residue does
  no work in it. Rejecting "only Davids" has the standing of rejecting Last Thursdayism.
- Chalmers does not put LLMs on the zombie side by default ("Could a large language model be
  conscious?", 2023): low credence now, successors taken seriously. So "LLMary is Zombie Mary" is
  Alice's move, not necessarily his.

## 4. The knowledge argument is an argument, not just a thought experiment

- Jackson 1982 ("Epiphenomenal qualia"): physical information does not exhaust information; qualia
  exist and are epiphenomenal. Mary and Fred (who sees an extra colour) support the first claim.
- Jackson 1986 ("What Mary didn't know"): (1) before release Mary knows everything physical about
  other people; (2) she does not know everything about them, since she learns something on release;
  (3) so some truths about other people (and herself) escape the physicalist story. Mary is the
  support for premise 2.
- Replies sort by the step they attack: nothing new is learned (Dennett, against 2); the gain is an
  ability, not a fact (Lewis/Nemirow); old fact, new concept (phenomenal concepts, against 2 ⇒ 3);
  Mary could not know all the physical facts (Churchland in part, against 1).
- `web/concepts/knowledge-argument.md` opens "a thought experiment… that aims to show". Strictly it
  is an argument with Mary as its thought experiment. **Possible reword, awaiting decision** (rule 5).
- Jackson later recanted: "Postscript on qualia" (1998, *Mind, Method, and Conditionals*) and "Mind
  and illusion" (2003, in O'Hear, ed., *Minds and Persons*), largely because epiphenomenal qualia
  make our knowledge of and talk about them inexplicable. Both are cited in Beaton 2005
  (`external/text/What RoboDennett Still Doesn't Know -- Beaton -- 2005.txt`); not read directly.

## 5. Bicycle and Paris

- Bicycle = ability hypothesis (Nemirow 1990, Lewis 1988): the coach lacks a skill, not a fact.
  Paris = acquaintance hypothesis (Conee 1994, after Russell): arriving gives a new relation, not a
  new truth. Both are physicalist in intent. Web: `argument-ability-hypothesis`,
  `argument-acquaintance-hypothesis`.
- User's objection: both are real knowledge gains. The coach learns how *his* body reacts to *this*
  bike and *this* swerve; the Paris reader lacked bandwidth. With movies, games, and finally a
  high-fidelity simulator (as pilots train), real Paris would feel familiar; the residue is only the
  sim-vs-real difference.
- Consequences: (1) both examples mix ordinary missing physical facts into the gap, so they are
  contaminated as models of Mary, whose physical knowledge is complete. (2) The simulator works
  because it supplies inputs through the *same channels* (looks, vestibular signals). For colour
  that route is the pricked finger: a high-fidelity simulation of red *is* seeing red. (3) Paris and
  the bike are gaps of **bandwidth**; Mary's is a gap of **channel**. The issue becomes whether a
  channel gap is anything more than an extreme bandwidth gap.
- LLMary makes this exact: the best simulation is ZenMary's distillation (soft labels on row 123),
  which removes nearly all predictive surprise; the leftover is one identifiable vector, the input
  row, which no simulation can reach without the token as input.
- The bicycle case is not pure know-how either: there is something it is like to balance.

## 6. Has anyone gone this fine-grained?

Mostly no; the classic debate argued at the level of "new fact or not". Finer-grained precedents:

- Dennett, "What RoboMary knows" (2005): §2 surprise; §3 Swamp Mary and the "nontrivial empirical
  assumption" that her colour system survives intact; §5 Locked RoboMary installs the state herself.
  No account of which parts update, no question of cheating.
- Graham & Horgan, "Mary Mary, quite contrary" (2000): predictable surprise "beside the point";
  footnote 7 leaves open whether she can know she will be surprised and still be surprised. Per
  Wikipedia they also tighten the stipulation to colour experience *through light perception*
  (unverified).
- Nida-Rümelin's Marianna (1995, from memory, unverified): sees colours in abstract pictures without
  knowing their names, separating experience from binding.
- Hume's missing shade; Beaton 2005 on RoboMary.
- Stuart Armstrong (with Laurent Orseau), "mAIry's room" (LessWrong, 2019): the closest precedent.
  Now `web/sources/armstrong-2019.md`; archived in `external/` and `external/text/`.

What looks new (subject to a proper literature search, e.g. Ludlow, Nagasawa & Stoljar 2004; Alter &
Walter 2007; predictive processing and Mary): the input/output split derived from one-hot encoding;
the causal ordering; Shazam as a use/mention device; soft labels as a third route; the countdown
flash; tied embeddings as an architectural bet; negative information.

Why the classic debate stayed coarse: thought experiments fix premises by decree ("knows all
physical facts") and say nothing about mechanism. LLMary is a learner whose "all the facts" is finite
and whose update can be computed, so "which part changes, by which route, and is the route allowed?"
cannot be dodged.

## 7. "Who cares? Mary is not an LLM"

The answer to sketch for the article:

1. Jackson's argument has a general form and does not mention humans. The step from "she learns at
   release" to "a non-physical fact exists" is supposed to follow from what learning and knowing are.
2. LLMary satisfies both premises (she has read everything, including her own weights; as ZenMary she
   can compute her first-light update in advance), yet the conclusion is false for her. So she is a
   **counterexample to the form**, independent of whether physicalism is true.
3. The residual is the gap between *knowing* what state you will be in and *being* in it. Reading
   writes elsewhere; only the token writes its own input row. Any learner with separate channels has
   this gap, and brains are such learners. (Toy-model move: the Ising model matters because it shows
   a mechanism suffices, not because magnets are lattices.)
4. Debunking: the marks that trigger "she learns something" (surprise, state change, new abilities,
   a "that") all occur in LLMary without a knowledge gap, so the intuition would arise whether or not
   its content were true.
5. Alice's replies all cost her: "she lacks physical facts" (she does not); "her learning is not the
   relevant kind" (then the argument presupposes its conclusion); "she is Zombie Mary" (Chalmers
   grants Zombie Mary abilities plus an indexical, which accounts for every observable mark).

Precedence: the counterexample-to-form move and "predictable but unavoidable change" belong to
Armstrong (2016, 2019). Ours: the derivation, the fine structure, the analysis
of cheating. The article's novelty claims must be revised accordingly.

## 8. What makes a physical system a good model of Mary

User's three:

1. **Learning from description** (zero-shot from text), with descriptions able to *refer* to the
   missing experience.
2. **A separate, updatable experience channel**: working but untrained (Mary's intact cortex).
3. **Knowledge of her own particular self**, not just generic facts about brains or robots, since
   Jackson's "all physical facts" includes her own brain and the exact update depends on her quirks.

Further candidates:

4. Description cannot write to the experience channel's parameters (one-hot for LLMary; empirical
   prewiring assumption for Mary).
5. The novelty is a new dimension, not a new combination (Hume's missing shade is the borderline).
6. "All physical facts" is finite and checkable, so the counterexample is transparent.
7. Leak-proofing can be verified (grep the corpus; nobody can audit Mary's pricked fingers).
8. Copyable for the experimenter (snapshot test, from an identical starting state), distinct from
   copyable for herself (point 3).
9. A measurable learning signal (loss, prediction error), with report-level and low-level surprise
   measured separately.
10. Reports come from the learning mechanism, not wired in.
11. Binding is testable (wrong-token test).
12. Self-access can be varied: read, simulate, choose data, write.
13. She survives and goes on learning (retention, extended exposure).
14. Others who have had the experience exist (Jackson 1986's "others"; sources for distillation).
15. Clearly physical, but neutral on consciousness, so the argument begs no question.

Tension: points 3, 6, 8 and 12 make the model *better* than human Mary. Alice: too transparent to
model Mary. Reply: Jackson stipulated the transparency ("knows all the physical facts"); the model
makes it real. LLMary is weak on point 5 (tokens are discrete, colour is continuous) and point 10
(do her reports come from learning, or from having read about Mary?).

Possible use: open the article with this list and score LLMary against it.

## 9. Open items

- Decide on the Fable review of the dialogue (provisionally rejected).
- Literature search before any novelty claim.
- Credit Armstrong in the article's §1.
- Possible reword of `concept-knowledge-argument` (argument vs thought experiment).
- Read Jackson 1998 and 2003 directly before Alice cites the recantation.
- Verify Nida-Rümelin's Marianna and Graham & Horgan's stipulation before citing.
- Older items: Benham pages; Held et al. 2011; Raffman 2005; LLMary web nodes; "first encounter" →
  "first light" in later article sections; book-chapters commit d81fc14 unpushed; llmary-branch
  changes uncommitted.

## Appendix: what LLMary proves and what it does not

*Written as an independent check on §7. Its main verdict: the phrase "counterexample to the form"
should be dropped, and the debunking claim (§7.4) is weaker than stated.*

### The argument has no form to counter

Jackson's own statement (1986, p. 293) is: (1′) before release Mary knows everything physical there
is to know about other people; (2′) she does not know everything there is to know about them,
because she learns something about them on release; so (3′) there are truths about other people
that escape the physicalist story. Read with "knows" and "learns" meaning the same thing throughout
(coming to know a truth), this argument is valid. A valid argument has no counterexamples: nothing
can make both premises true and the conclusion false.

So §7.2 cannot be right as written. Suppose LLMary really satisfied both premises in Jackson's
sense. Then she knew every physical truth about token 123, and at first light came to know a
further truth. That further truth would be non-physical, and the conclusion would hold for her too.
The only way to have "both premises, false conclusion" is to read premise 2 weakly, as "she is
changed, surprised and newly able", while reading premise 1 as propositional knowledge. That is an
equivocation, and it is the one Churchland charged Jackson with in 1985 and Jackson explicitly
disowned in 1986. He did not argue the weak version.

The correct description is this. Fix one sense of "know" and apply it to LLMary in both premises.
On a functional sense (stored, retrievable, usable in inference and report), premise 1 is roughly
true of her, and premise 2 is *false*: in the fully informed case there is no proposition she can
state or use after first light that she could not state or use before. On a thicker sense that
language models do not meet at all, neither premise applies. Either way she is not an instance of
true premises and a false conclusion. She is a model in which premise 2 *appears* true while being
false. That makes her a witness for the ability and acquaintance replies, not a counterexample to
Jackson. (The dispute is over soundness, namely premise 2, and always was.)

What she does refute is a bridge principle that sits underneath premise 2:

> If a learner who has complete descriptive knowledge of an encounter is nonetheless unavoidably
> changed, surprised and newly able when the encounter comes, then she was missing a fact.

This is universal, so one clear instance against it is enough, and the instance need not resemble
Mary. That is the legitimate core of "who cares, Mary is not an LLM". But how much it matters
depends on how much of Jackson's support for premise 2 runs through the bridge, which is taken up
below.

### What is established, by strength

**Proved (mathematics).** With one-hot lookup, the input row of a token receives zero gradient from
any training text that does not contain the token. The statement quantifies over *all* corpora.
This is the model's best feature, and it partly sidesteps the worry about premise 1: we need not
decide whether LLMary "really knows everything", because whatever a complete description would
contain, adding it changes nothing in that row. Also proved: the symmetry under swapping unseen
labels, and hence the expected-surprise bound for the predictor.

Three limits belong next to the theorem. It is a fact about one architecture: a model whose
embeddings were composed from characters, or generated from descriptions by another network, would
have no such sealed channel. It says the first gradient is the first; it does not say one step
installs a competence, and in practice one step does very little, whereas Mary's one look seems to
suffice. And the update is "forced" only if she is training; with the learning rate at zero the
token passes through a random row and nothing is learned.

**Shown by construction (engineering plus conceptual analysis).** Describing an encounter,
identifying the item, and being changed by it are separable. Predicting one's own prediction error
is compatible with incurring it. Computation can remove part of the gap (ZenMary's output side) and
cannot remove another part (the input side) short of writing. These are solid, and they are the
real content of the project.

**Established philosophically, and modest.** The bridge principle is false. Change, surprise and
new ability at first encounter are not, by themselves, evidence of a missing fact, physical or
otherwise. Graham and Horgan's open question, whether one can know one will be surprised and still
be surprised, gets a clean yes for surprisal. And Dennett's "she would not be surprised" is shown to
need writing, not just knowing, which is a point *against* the no-learning physicalist.

**Suggested by analogy only.** That Mary's gain is a binding; that her felt surprise is a
representation-level mismatch; that her new view of others is a new guise. Each needs a premise
about brains or about experience that the model does not supply. The article's §12 table says this
honestly. The notes' §7.3 ("brains are such learners") asserts what §10 of the article treats as an
open question for vision science, and Benham's top suggests Mary's channel is not sealed.

### What is not established

*Anything about phenomenal consciousness.* LLMary is, by Alice's lights, Zombie Mary. Everything
the model exhibits is what Chalmers already grants Zombie Mary: abilities, a state change, an
indexical. Against a Chalmers-style opponent the model therefore makes concrete what was conceded
and moves the dispute not at all. It also cannot show the residue in Mary is *not* a fact. It shows
a residue that is not a fact exists in one system; whether Mary's is the same residue is the
original question.

*That she satisfies premise 1 in full.* A network cannot hold a verbatim description of all its
weights in those weights without a fixed-point construction, since reading changes what is read.
(Nicely, the untouched input row is the one part reading leaves stable; the output row is a moving
target.) ZenMary's exact self-access is an external tool, not knowledge stored in her. So premise 1
holds for a targeted, finite slice. Because the theorem quantifies over corpora this does little
damage to the input-side result, but "has read everything, including her own weights" should not
be leaned on.

*Jackson's actual target, other people.* Article §9 says that after first light she can represent
other networks' token-123 states "through her own state". Nothing in the mechanism does this.
Descriptions of other models mention token 123 in familiar tokens and never activate row 123, so
the updated row plays no part when she thinks about them. The claim is an analogy laid over the
model, not a result computed in it, and it is the one section that fails the article's own standard
("calculated rather than imagined"). Worse for the analogy, two models' rows for the same token are
unrelated vectors; what they share is only the role, which she already knew.

### The debunking claim

§7.4 says the marks that trigger "she learns something" all occur in LLMary without a knowledge
gap, so the intuition would arise whether or not it were true. Two things are run together here.

The first is evidential: Jackson's "she will not say ho, hum" treats Mary's reaction as evidence.
The model does undercut that. Reactions of this kind are what any channel-separated learner shows.

The second is the source of the intuition, and it is not Mary's behaviour. Jackson's real support
for premise 2 is the reader's judgment: I know what red is like, and I cannot see how any book
would have told me. He says so directly: "as a matter of fact, she would not know". That judgment
is made from the reader's own acquaintance, not inferred from surprise or new abilities in Mary. To
debunk it one must show that a system would form *that judgment* for reasons insensitive to its
truth. LLMary does not form it. Her reports that anything is ineffable would most plausibly be
copied from the literature about Mary (§8, point 10). Nothing in her mechanism produces the
judgment "I learned something I cannot state" from the gap itself.

This limits only one of Bob's two strategies. Whether she *learned* is settled by the weight update,
not by any report: the snapshot test is the better criterion. An update she cannot report is still
learning, a failure of introspection that Alice and Bob would both accept; a report with no update
is not learning at all, only saying so. Nor do Alice and Bob dispute that she learned. They dispute
whether what she gained is a fact or only a state, and the update cannot settle that, since both
views predict it. Bob's *sufficiency* strategy (the update accounts for everything that happens to
her, so the extra fact is idle) needs no report mechanism, and LLMary supports it fully. His
*debunking* strategy (Alice's judgment would arise whether or not it is true) needs a model of how
that judgment is produced, and LLMary supplies none. So the missing report mechanism leaves her case
about learning and its sufficiency intact; it only means she cannot by herself debunk the reader's
intuition.

Is Alice's appeal to acquaintance question-begging? Used defensively, no. She is not obliged to
discard her evidence because a system lacking it behaves similarly. Used offensively, as a premise
the physicalist must accept, yes. The same holds in reverse for Bob: "the extra is not why you say
there is an extra" presupposes that Mary's reports are fully explained by the binding, which is the
point at issue. The honest score is a stalemate with the burden clarified, not a debunking.

So §7.5 overstates. The reply "her learning is not the relevant kind" does not presuppose the
conclusion; it is simply Jackson's premise 2, which the model has not tested.

### Which disanalogy hurts which conclusion

- *Discrete, arbitrary token versus structured colour space.* Damages the selection bound and the
  claim that description cannot reach the channel (interpolation, Benham). Leaves the refutation of
  the bridge principle intact.
- *Reports possibly copied from text.* Damages debunking and anything about report-level surprise.
  Leaves the gradient results intact.
- *No evidence of experience.* Costs the existence proof nothing, since neutrality is its point.
  Blocks every inference about what Mary's residue is.
- *Part of the gap closes by computation.* Jackson says Mary's gap is not one that "following
  through enough logical consequences" would close. ZenMary closes the output side by exactly that.
  So only the input side is a fair analogue, and the article should say the output-side surprise is
  the kind Jackson sets aside.
- *Knowledge split across subsystems.* Her "knowing" is the verbal system's and her surprise the
  predictor's. This supports Churchland's diagnosis, but it also invites the reply that a knower
  whose parts do not talk to each other never had unified knowledge, which is not Mary's stipulated
  condition.

### What the anti-physicalist gets

More than the notes allow. The model confirms that the phenomenon behind premise 2 is robust:
complete description really does leave something for the encounter, and no cleverness removes it.
That closes Dennett's easiest exit. It gives a sharp statement of the residue, knowing which state
you will be in versus being in it, and Alice can accept the statement whole and add that being in
the state is the only way to know what it is like. And LLMary is a worked specimen for Chalmers's
master argument: here is everything the physicalist story explains, present in a system where
(Alice says) all is dark, so that story does not yet explain what distinguishes Mary.

### Precedence

Armstrong 2016 already has the core in one line: knowing about a state, even perfectly, does not
put you in it. Armstrong 2019 has "predictable and unavoidable" weight changes, and the escape by
self-modification. Churchland 1985 and Lewis 1988 denied the bridge principle on the philosophical
side, and Dennett 2005 supplied writing. What LLMary adds is that the gap is *derived* rather than
stipulated (mAIry's node $n_p$ is posited; row 123 falls out of the chain rule), that the derivation
holds for every possible description, the input/output decomposition, ZenMary's separation of what
computation can and cannot remove, and controls that can be run. That is a contribution of rigour
and resolution. The philosophical move is not new.

### Bottom line

LLMary proves that a physical learner can know everything sayable about an encounter and still be
unavoidably changed by it, and that this change has a fine structure which can be computed. That
refutes the inference from "changed, surprised, newly able" to "lacked a fact", and it makes the
ability and acquaintance replies concrete where they were verbal. It does not refute, or
counterexemplify, Jackson's argument, which is valid and stands or falls with the claim that Mary
comes to know a truth; LLMary comes to know none, so she is silent on that claim. It does not debunk
the intuition behind the claim, because that intuition comes from the reader's acquaintance with
colour and not from Mary's reactions, and LLMary has no mechanism that generates the corresponding
judgment. It says nothing about consciousness, and its treatment of other minds is analogy, not
calculation. The fair summary for the article is the one its own §2 already gives, that a gain on
first encounter *can* be wholly physical, plus a precise map of what such a gain consists in. The
notes' stronger framing in §7 should be cut back to that.

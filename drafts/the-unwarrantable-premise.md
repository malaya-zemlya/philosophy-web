# The Unwarrantable Premise

### A Computability-Theoretic Objection to the Zombie Argument Against Physicalism

*Draft*

---

## Abstract

The conceivability argument against physicalism infers, from the ideal conceivability of philosophical zombies, that physicalism is false. Existing objections target either the move from conceivability to possibility (type-B materialism, the appeal to a posteriori necessity) or the conceivability of zombies itself (Dennett, the anti-zombie symmetry). I grant both. I argue instead that the argument's first premise — that the zombie scenario is *ideally* conceivable — cannot be **warrantedly asserted** by any reasoner whose mind is physical and computable, and can be warrantedly asserted by other reasoners only at the cost of presupposing the conclusion or an independently anti-physicalist thesis about the mind. The core is a reduction: the faculty that would certify ideal conceivability for scenarios as rich as a complete physical description must, on reflection, compute the halting set $\emptyset'$, and so is not an effective procedure. A trilemma on the nature of the mind then shows that every way of possessing such a faculty defeats the argument's dialectical ambition. The result is not that physicalism is true, nor that zombies are impossible, but that this particular route to anti-physicalism is unwalkable: the one faculty that could license its premise is an oracle with no realizer in a world governed by computable physics.

---

## 1. Introduction

The zombie argument is the most discussed *a priori* argument against physicalism. A philosophical zombie is a being physically identical to a conscious person but wholly lacking phenomenal experience. If such a being is genuinely possible — if there is a world with all of our physics and none of our experience — then the physical facts do not necessitate the facts about consciousness, and physicalism, understood as the thesis that the physical fixes everything, is false. The argument moves from the *conceivability* of zombies to their *possibility*, and from their possibility to the falsity of physicalism (Chalmers 1996, 2010).

The literature has concentrated its fire on two joints. The first is the inference from conceivability to possibility. Type-B materialists grant that zombies are conceivable but deny that they are possible, holding that the identity (or necessitation) of the phenomenal by the physical is necessary but knowable only *a posteriori*, on the model of "water is $\mathrm{H_2O}$" (Loar 1997; Papineau 2002; Block and Stalnaker 1999). Chalmers's two-dimensional framework is built precisely to neutralize this move for phenomenal concepts (Chalmers 2002). The second joint is the conceivability of zombies itself: Dennett (1991, 1995) argues that what passes for conceiving a zombie is merely a failure to imagine the relevant physical complexity in sufficient detail; Frankish (2007) and others press an *anti-zombie* symmetry, on which a being whose consciousness is wholly physically necessitated is equally conceivable, yielding physicalism by the same logic.

This paper opens a third front, orthogonal to both. I grant, for the sake of argument, that conceivability entails possibility (the conceivability principle, CP), and I grant that zombies may be conceivable *in principle*. My target is **epistemic**, and it is grounded in computability theory rather than in the semantics of phenomenal concepts. The argument's first premise must say that the zombie scenario is *ideally* conceivable — that it harbors no incoherence detectable by any amount of rational reflection — because Chalmers rightly concedes that the weaker, merely apparent conceivability ("I have found no contradiction so far") is worthless. I shall argue that *ideal* conceivability, for scenarios as logically rich as a complete physical description of our world, is a property whose instances cannot be certified by any effective method without begging the question. The premise the argument needs is therefore one no suitably situated reasoner can be warranted in asserting.

The structure is as follows. Section 2 states the argument and isolates its demanding premise. Section 3 articulates and defends the dialectical constraint (W) that the objection deploys. Sections 4–5 establish the computational core: certifying ideal conceivability is certifying a consistency statement, and reliable consistency-certification across rich scenarios is Turing-equivalent to the halting oracle. Section 6 presents the trilemma on the nature of the mind and proves its exhaustiveness. Section 7, the longest, answers objections — including the most serious one, that we *do* sometimes know $\Pi_1$ truths. Section 8 distinguishes the objection from its neighbors in the literature. Section 9 states the conclusion and its scope.

## 2. The Argument and Its Demanding Premise

Fix notation. Let $P$ be the complete physical description of the actual world, comprising all physical particulars and laws, regarded as a theory. Let $C$ be the proposition that phenomenal consciousness is instantiated. Let
$$ Z := P \wedge \neg C $$
be the **zombie scenario**: the full physics with consciousness subtracted. Following the standard formulation, *physicalism* is the thesis $\Box(P \to C)$, equivalently $\neg\Diamond Z$. The anti-physicalist holds $\Diamond Z$.

A point of bookkeeping matters here. Physicalism is the *lean* ontology: $C$ is not an ingredient added on top of $P$ but is taken to be necessitated by $P$. It is the dualist and the panpsychist who hold that $P$ is incomplete and must be supplemented by bridging principles or fundamental experiential properties. Accordingly $\neg C$ in $Z$ is a *subtraction* from the physicalist's base, and the disputed question is whether that subtraction leaves a coherent scenario. The zombie is not "$P$ plus a stipulation"; it is $P$ with its alleged surplus removed.

The argument is then:

- **(T1)** $Z$ is ideally conceivable.
- **(T2)** Ideal conceivability entails possibility: ideal-conceivability$(Z) \to \Diamond Z$. *(CP)*
- **(T3)** Hence $\Diamond Z$. *(T1, T2)*
- **(T4)** Physicalism $\Leftrightarrow \neg\Diamond Z$. *(definitional)*
- **(T5)** Hence physicalism is false. *(T3, T4)*

The argument is valid, T4 is definitional, and T2 is the premise the literature contests. **I attack none of these.** My objection concerns T1, and specifically the warrant available for it.

Everything turns on what "conceivable" means in T1. There is a weak, *prima facie* notion — a scenario is prima facie conceivable when, on the reasoning one has actually carried out, no incoherence has appeared. And there is a strong, *ideal* notion — a scenario is ideally conceivable when no incoherence would appear under *any* improvement of reasoning whatsoever. Chalmers is explicit that the argument requires the strong notion. Prima facie conceivability is no guide to possibility: one can fluently "conceive" that a given large number is prime when in fact it is composite, the appearance of coherence reflecting only an arithmetic one has not performed. Only ideal conceivability — the absence of *any* discoverable incoherence — is offered as a guide to possibility, and only the ideal notion can sustain CP. Write $\mathrm{IC}(Z)$ for "$Z$ is ideally conceivable." T1 is $\mathrm{IC}(Z)$, and the question is whether anyone can be justified in asserting it.

## 3. The Dialectical Constraint

The objection deploys a constraint on what it takes for an argument to discharge its intended function. The zombie argument is advertised as a *proof*: a piece of reasoning that ought to move a physicalist, from premises she can accept, to a conclusion she presently rejects. Call an argument **cogent** (for an audience) when it can rationally move that audience to its conclusion. Cogency requires more than validity and truth; it requires that the audience can come to be *justified* in the premises without already being committed to the conclusion. I state the constraint as:

> **(W)** An argument is cogent against an opponent only if its premises admit justification that is (i) in-principle accessible to a suitably idealized version of the parties, and (ii) not such that acquiring it requires already accepting the conclusion.

Clause (ii) is the familiar prohibition on begging the question, here applied not to the *content* of a premise but to the *route by which warrant for it is obtained*. Clause (i) is an accessibility condition: a premise whose truth value no party could ever come to know cannot be the lever by which one party rationally moves another. (W) does not say that an inaccessible or circular premise is *false*; the argument might be sound. It says such an argument lacks *probative force* — it cannot do the persuasive work its proponents claim for it.

(W) is weak enough to be widely shared. It is the principle on which standard complaints against the modal ontological argument rest: granting that "possibly, a necessary being exists" entails "a necessary being exists," the argument still fails to compel, because warrant for the possibility premise is not available independently of accepting the theistic conclusion. A theist may hold the argument sound; no atheist is rationally moved. My claim is that the zombie argument is in the same position, and for a reason that can be made exact.

A reader who rejects (W) outright may read the conclusion conditionally: *if* cogency requires accessible non-circular warrant, then the zombie argument is not cogent. Since proponents do claim cogency — they present the argument as giving physicalists a reason to convert — the conditional suffices to engage the dialectic on its own terms.

## 4. From Premise to Consistency Statement

The first step toward the computational core is to see what kind of claim $\mathrm{IC}(Z)$ is.

By definition, $\mathrm{IC}(Z)$ holds iff $Z$ harbors no incoherence detectable by ideal *a priori* reasoning — that is, iff $Z$ is **consistent** under the relation of a priori entailment. Let $\vdash_a$ denote ideal a priori derivability and let $\mathrm{Con}_a(Z)$ abbreviate "$Z \nvdash_a \bot$." Then:

> **(L1)** $\mathrm{IC}(Z) = \mathrm{Con}_a(Z)$, and to be justified in T1 is to be justified in the consistency claim $\mathrm{Con}_a(P \wedge \neg C)$.

Two features of $\mathrm{Con}_a(Z)$ are worth flagging immediately, as they drive everything downstream.

First, **polarity**. The physicalist asserts the *negation*, $\neg\mathrm{Con}_a(Z)$: $P$ necessitates $C$, so adjoining $\neg C$ yields an incoherence (whether a priori or, for the type-B physicalist, a posteriori — see §7.4). The conceiver must establish the *positive* claim, $\mathrm{Con}_a(Z)$. As we will see, the positive direction is the computationally intractable one.

Second, **non-triviality of the subtraction**. One cannot discharge T1 by declaring the removal of $C$ from $P$ "obviously coherent." Whether $\neg C$ can be consistently conjoined to $P$ *is* the disputed question; a non-question-begging certification that consciousness detaches from the physics simply *is* a certification of $\mathrm{Con}_a(Z)$. The work cannot be skipped.

## 5. Consistency-Certification as an Oracle

I now make precise the claim that the "ideally rational reasoner" the argument invokes is a halting oracle. The claim must be pitched at the right level. A single fixed sentence such as $\mathrm{Con}_a(Z)$ is *some* $\Pi_1$ proposition with a determinate truth value; in isolation it is "decidable" by a trivial one-state machine that outputs the correct verdict. Hardness never resides in a single instance. It resides in **method**: in the requirement that warrant for $\mathrm{Con}_a(Z)$ be produced by a procedure that is *reliable* across the relevant class of cases and that does not take the disputed verdict as an input.

Make this explicit. To be justified in $\mathrm{Con}_a(Z)$, on any plausible epistemology, the conceiver must form the belief by a method $\mathsf{M}$ such that (a) $\mathsf{M}$ is *reliable*: it tracks $\mathrm{Con}_a$ across the class $\mathcal{S}$ of scenarios for which the conceiver claims competence — for CP is asserted in full generality, "for any $S$, $\mathrm{IC}(S) \to \Diamond S$," so its authority is the authority of a general competence in ideal conceiving; and (b) $\mathsf{M}$'s application to $Z$ does not presuppose the answer (else clause (ii) of (W) is violated — the verdict would be smuggled in, not earned). The objection is that no *effective* $\mathsf{M}$ satisfies (a) for any $\mathcal{S}$ rich enough to include $Z$.

**The richness assumption.** Assume:

> **(Rich)** $P$ interprets Robinson arithmetic $Q$.

This is not demanding. $P$ describes a world containing universal computers and arithmetic-competent reasoners; any complete physical description of such a world represents arbitrary Turing-machine computation, and so interprets $Q$. The scenarios the conceiver must adjudicate, if its competence is to underwrite CP for cases like $Z$, therefore include arithmetic-rich theories.

**The reduction.** Consider the family of theories
$$ T_{M,x} := Q \cup \{\neg h_{M,x}\}, \qquad h_{M,x} := \text{``}M \text{ halts on } x\text{''} \ (\Sigma_1). $$
For each Turing machine $M$ and input $x$:

- If $M$ halts on $x$, then $h_{M,x}$ is a true $\Sigma_1$ sentence, so $Q \vdash h_{M,x}$ ($Q$ proves all true $\Sigma_1$ sentences). Then $T_{M,x} \vdash h_{M,x} \wedge \neg h_{M,x}$: **inconsistent**.
- If $M$ does not halt on $x$, then $h_{M,x}$ is false, and the standard model $\mathbb{N} \models Q \cup \{\neg h_{M,x}\}$: **consistent**.

Hence
$$ T_{M,x} \text{ is consistent} \iff M \text{ does not halt on } x. $$
A method that reliably delivers consistency-verdicts for the family $\{T_{M,x}\}$ therefore decides the complement of the halting set, hence the halting set $\emptyset'$ itself. So reliable consistency-certification over arithmetic-rich theories computes $\emptyset'$; it is **at least** as hard as $\emptyset'$. Conversely, for recursively axiomatized theories "inconsistent" is $\Sigma_1$ (search for a proof of $\bot$), so "consistent" is $\Pi_1$ and is decidable *relative to* $\emptyset'$. Therefore:

> **(L2)** The verdict-function of reliable consistency-certification over arithmetic-rich theories is $\Pi_1$-complete and Turing-equivalent to the halting oracle: $\equiv_T \emptyset'$.

This is the exact content of the slogan that the logically omniscient sages of the inductive puzzles — the islanders who instantly know every consequence of every announcement — are a fiction of the same kind as the halting oracle. Logical omniscience over a language interpreting arithmetic is not *like* $\emptyset'$-power; it is $\emptyset'$-power. And from L2 with Turing's theorem ($\emptyset'$ is not computable):

> **(L3)** No effective method reliably certifies $\mathrm{Con}_a$ over arithmetic-rich scenarios.

A relabeling does not evade L3. If a faculty called "rational insight" reliably outruns proof-search on these inputs, then by definition it computes a non-computable set; calling it insight rather than computation does not lower its Turing degree.

It remains to connect L3, a claim about reliable methods over a class, to the single case $Z$. The connection is clause (b) of the warrant requirement. The conceiver's competence in ideal conceiving is general — it is what licenses CP across cases — so the method $\mathsf{M}$ that grounds her belief in $\mathrm{Con}_a(Z)$ must belong to a reliable general competence, which by L3 is non-effective. The only effective methods that return the correct verdict on $Z$ specifically are those antecedently tuned to that verdict — i.e. methods that encode the contested answer and so violate (b). Thus: under any constraint that the conceiver's warrant be both reliable-in-general and non-question-begging, that warrant requires a non-effective faculty.

## 6. The Trilemma on the Nature of the Mind

Whether a reasoner can *possess* a non-effective faculty depends on what minds are. Partition the possibilities by two successive yes/no questions; this generates an exhaustive trilemma.

> **Question 1.** Is the mind a physical system?
> &nbsp;&nbsp;— No $\Rightarrow$ **(D3)**.
> &nbsp;&nbsp;— Yes $\Rightarrow$ Question 2.
>
> **Question 2.** Does the physical Church–Turing thesis (PCTT) hold of the mind's substrate — i.e., is every function its physical processes compute Turing-computable?
> &nbsp;&nbsp;— Yes $\Rightarrow$ **(D1)**.
> &nbsp;&nbsp;— No $\Rightarrow$ **(D2)**.

**Exhaustiveness.** Question 1 is a bivalent partition of the space of views into {mind is physical, mind is not physical}; D3 occupies the negative cell. On the positive cell, Question 2 is a bivalent partition into {PCTT holds of the substrate, PCTT fails of the substrate}; D1 and D2 occupy its two cells. The three cells are pairwise disjoint (D1 and D2 differ on PCTT; D3 differs from both on physicality) and jointly exhaust the leaves of a complete binary tree over two independent yes/no questions. No fourth option exists: a faculty must be realized either by Turing-computable physical means (D1), by non-Turing-computable physical means (D2), or by non-physical means (D3).

**(D1) Physical mind, PCTT holds.** The reasoner realizes only Turing-computable functions. By L3 the certifying faculty is non-computable, so the reasoner cannot possess it; by §5 the only effective surrogate either fails to track $\mathrm{Con}_a$ in general (delivering at most "no contradiction found so far," the prima facie notion the argument disavows) or begs the question. Hence **T1 is unwarrantable** in a D1-world. By (W) the argument is not cogent: it may be valid and even sound, but its soundness cannot be known by the parties, and so it cannot move the physicalist.

**(D2) Physical mind, PCTT fails of its substrate.** The reasoner can possess the faculty, but only because its own physical substrate realizes hypercomputational processes. The locality matters and is easy to misstate. What rescues the conceiver is not the generic thesis that physics *somewhere* harbors non-computable processes; a world could contain exotic non-recursive dynamics in some cosmological or quantum-gravitational corner while the reasoner's faculty remained fully effective — and that reasoner is back in D1. The escape requires the stronger, *local* claim that the very faculty doing the conceiving is a physical hypercomputer: non-computable physics that the mind actually *harnesses* to reason. This is the position Roger Penrose defends (1989, 1994) — non-recursive physical dynamics (for him, in an objective-collapse quantum gravity) together with a brain that exploits them — minus his particular microtubule mechanism and minus his Gödelian route to it.

Two things must then be said precisely. First, this local $\neg$PCTT does *not* by itself entail $\neg$physicalism: a world could be both physicalist and cognitively hypercomputational, with $P$ still necessitating $C$. So D2 is not immediately self-defeating, and I do not claim it is false; it is a coherent and live possibility, offered here without adjudication. But second, the position is (i) a substantive empirical thesis about the physics of cognition, not available to an argument that advertises itself as *a priori* and proceeds from the armchair of imaginability; and (ii) explicitly denied by the argument's principal target, *computational* physicalism, the conjunction of physicalism with PCTT. Under D2 the argument therefore either ceases to be a priori or loses purchase on the very position it was framed to refute. It secures T1 only by importing a premise its method forbids and its opponent rejects — and, as §7.4 notes, by *presupposing* a thesis for which the strongest available case is itself a separate and contested argument.

**(D3) Non-physical mind.** The reasoner possesses the faculty because minds are not wholly physical systems. But that *is* $\neg$physicalism about the mind — the conclusion. Warrant for T1 is here obtained only by already accepting what the argument set out to prove: a transparent violation of clause (ii) of (W). The argument **begs the question**.

Since D1 $\vee$ D2 $\vee$ D3 is exhaustive, in every case T1 is either unwarrantable (D1), warranted only by an inadmissible empirical premise (D2), or warranted only by presupposing the conclusion (D3). In no case can the argument do what it claims.

## 7. Objections and Replies

### 7.1 The normative-ideal rejoinder

**Objection.** Ideal conceivability is not a faculty any agent *runs*; it is a normative or counterfactual fact. $\mathrm{Con}_a(Z)$ holds iff no possible improvement of reasoning *would* reveal an incoherence. So T1 requires no one to possess an oracle; it is a fact about the limit of inquiry, and the trilemma, which is about what agents can compute, is beside the point.

**Reply.** The rejoinder concerns the *truth-conditions* of T1; (W) concerns its *warrant*; these come apart. Grant that $\mathrm{Con}_a(Z)$ has a determinate truth value fixed by the idealized relation $\vdash_a$. The only instrument any party has for adjudicating the specific case is its actual reasoning relation $\vdash_{\mathrm{act}}$, which under D1 is effective. The discrepancy between the two relations is exactly the non-effective surplus of L2:
$$ \{\,S : \mathrm{Con}_a(S)\,\} \ \setminus\ \{\,S : \text{no contradiction found by } \vdash_{\mathrm{act}}\,\} \ \equiv_T\ \emptyset'. $$
So justified assertion cannot outrun $\vdash_{\mathrm{act}}$, and $\vdash_{\mathrm{act}}$ delivers at most a finite, $\Sigma_1$-bounded body of evidence — "no contradiction in the searches performed" — which is logically consistent with both $\mathrm{Con}_a(Z)$ and its negation. Defining the ideal precisely thus rescues the *meaning* of T1 while leaving our *access* to its truth value exactly oracle-shaped. The trilemma's verdict stands: under D1 the determinate fact is real and unreachable.

### 7.2 But we know some $\Pi_1$ truths

This is the most serious objection. We are sometimes justified in believing $\Pi_1$ statements. We believe particular non-halting facts; mathematicians believe $\mathrm{Con}(\mathrm{PA})$. If finite agents can be warranted in *those* $\Pi_1$ claims, why not in $\mathrm{Con}_a(Z)$?

**Reply.** The cases where we know a $\Pi_1$ truth are exactly the cases that do not help the conceiver, and seeing why sharpens the whole result. We come to know a particular non-halting fact, or a particular consistency statement, in one of two ways, and neither is *conceiving*.

(a) *By proof.* We prove that machine $M$ loops by exhibiting an invariant, or we prove $\mathrm{Con}(T)$ relative to a stronger theory. This is genuine warrant, but it is **piecemeal and demonstrative**, not the deliverance of a general faculty that surveys a scenario and finds it coherent. There is no uniform effective proof-method covering all instances — that is just L2 again. For the conceiver to know $\mathrm{Con}_a(Z)$ *this* way, she would need an actual **proof that consciousness detaches from the physics** — a demonstration that $P \wedge \neg C$ is consistent. But the argument offers no such proof; it offers *conceivability*, the appearance of coherence under inspection. A proof of $\mathrm{Con}_a(Z)$ would be a far stronger thing than the argument supplies, and producing one would require exhibiting a model of $P \wedge \neg C$ — precisely the anti-physicalist's contested claim, now asserted rather than imagined.

(b) *By extra-systematic grounds.* We believe $\mathrm{Con}(\mathrm{PA})$ because we take ourselves to grasp the standard model $\mathbb{N}$, on which the axioms are true. This warrant is real but it is grounded in a *positive conception of the intended structure*. The analogue for $Z$ would be warrant grounded in a positive conception of a world that is physically just like ours yet experientially empty — i.e. in an antecedent commitment to the very detachability at issue. Again the warrant, where it exists, presupposes the answer.

So the objection, pressed, splits the conceiver's possible warrant into exactly the two unhelpful kinds: demonstrative proof of detachability (which the argument does not offer and which would outstrip conceiving) or a positive grasp of a zombie-structure (which begs the question). The residual option — warrant from the mere *failure to find* an incoherence on inspection — is the prima facie conceivability that Chalmers concedes is no guide to possibility. There is no fourth source. Far from undermining the result, the existence of genuine $\Pi_1$ knowledge isolates why the conceiver cannot have the kind she needs.

### 7.3 Does this prove too much?

**Objection.** If certifying consistency is oracle-hard, the objection seems to wreck *all* modal knowledge, not just the zombie premise. But we plainly have modal knowledge — this table could have been red. So the argument overgenerates and must be unsound.

**Reply.** The result is targeted, and the targeting is principled. It bites only on conceivability claims that simultaneously (i) require the *ideal*, not prima facie, notion to do their work; (ii) concern scenarios rich enough to interpret arithmetic, so that consistency is undecidable; and (iii) are such that the weaker prima facie notion is conceded insufficient *because* the modal fact at stake is a strict necessitation that prima facie appearances cannot settle. Ordinary modal knowledge fails (i)–(iii): "the table could have been red" is secured by recombination at a level where prima facie conceivability is a perfectly good guide, because nothing in the vicinity claims a hidden *necessary* connection between table and color that careful reasoning might expose. The zombie premise is special precisely in meeting all three conditions — the physicalist's whole position is that there *is* a hidden necessitation $P \to C$, which downgrades prima facie conceivability to worthlessness and forces the appeal to the ideal notion. The objection's burden, the certification of consistency, is one the zombie argument *itself* shoulders by retreating to ideal conceivability under physicalist pressure. The overgeneration worry thus mislocates the result: it is the structure of *this* dispute, not a general fact about modality, that puts the intractable consistency claim on the conceiver's plate.

### 7.4 Rational insight outruns computation (the Lucas–Penrose escape)

**Objection.** The trilemma assumes that to certify consistency is to compute. But perhaps rational insight is non-algorithmic — perhaps human mathematical understanding already grasps consistency facts no Turing machine can decide (Lucas 1961; Penrose 1989, 1994). If so, the conceiver simply has the faculty, and D1 does not apply.

**Reply.** This is not a way around the trilemma; it is the choice of horn D2 or D3, and the paper's claim is not that it is *unavailable* but that it is *costly*. To say that rational insight reliably decides consistency facts beyond $\emptyset'$-reach is to say either that the mind's physical substrate is hypercomputational (D2: local PCTT fails) or that the mind is not wholly physical (D3). The first is precisely Penrose's proposal, and I take it to be a coherent and genuine out — I do not argue here that it is false. What I claim is only what it costs to take it.

The cost has two parts. First, a dependence. The case for cognitive hypercomputation is itself a separate, controversial *anti-mechanist* argument, widely contested on its own merits. To rescue the zombie argument by leaning on it is to make a supposedly free-standing route to anti-physicalism *depend* on an independent argument whose own soundness is roughly the question of whether minds compute. The two arguments do not so much reinforce each other as require each other; an argument that can move only those already persuaded by Penrose has lost its claim to independent probative force.

Second, and worse for the conceivability theorist, a matter of *direction*. Penrose argues *from* "the mind exploits non-computable physics" *to* "the mind is non-algorithmic"; he offers an argument for the thesis. The cornered conceivability theorist cannot do this — she must *assume* cognitive hypercomputation as an unargued premise simply to license T1. She thus borrows not merely Penrose's conclusion but Penrose's conclusion stripped of Penrose's argument, which is dialectically weaker than Penrose's own position. The honest summary is that the appeal to non-algorithmic insight does not dissolve the objection; it relocates the argument's burden onto an even stronger and more contested premise, and presupposes rather than earns it.

### 7.5 The richness assumption

**Objection.** Perhaps $\mathrm{Con}_a(Z)$ lies in a decidable fragment, even if consistency is undecidable in general; then an effective method suffices for $Z$ specifically.

**Reply.** Two responses, given in §5 and recalled here. *Notion-level:* CP's licensing authority is the authority of a *general* competence in ideal conceiving — "for any $S$, $\mathrm{IC}(S) \to \Diamond S$" — and one may not invoke that general authority for $Z$ while paying only for a decidable fragment; the warrant for applying CP to $Z$ inherits the competence's general profile, which by L2 is $\emptyset'$-equivalent. *Case-level:* by (Rich), $P$ embeds universal computation, so whether $P \wedge \neg C$ is consistent turns inter alia on halting facts about the machines $P$ describes; $Z$ is not in an antecedently certified decidable fragment, and certifying that it is would itself require the general capacity. The single-instance triviality noted in §5 — that *some* machine outputs the right verdict on $Z$ — is no help, since such a machine encodes the contested verdict and violates clause (ii) of (W).

### 7.6 The dialectical constraint is too strong

**Objection.** (W) is more demanding than legitimate argument requires. Many good arguments rest on premises we cannot *certify* yet are reasonable to believe.

**Reply.** (W) does not require certainty or certification in any strong sense; it requires accessible, non-circular *justification*. The zombie argument fails the condition not because $\mathrm{Con}_a(Z)$ is merely uncertain but because, under D1, the only available ground for it is either (a) finite failure-to-refute, which the argument itself classifies as insufficient, or (b) a ground that presupposes the verdict. A premise for which the *only* routes to justification are an avowedly insufficient one and a circular one is not "reasonable to believe" in the sense cogency needs; believing it is either under-supported or question-begging. And as noted in §3, a reader who still finds (W) too strong may take the conclusion conditionally — *if* cogency requires accessible non-circular warrant, the argument is not cogent — which is enough to defeat the argument's advertised ambition of converting physicalists.

## 8. Relation to Existing Objections

The objection is independent of, and compatible with, the standard ones, and locating it among them clarifies its contribution.

Against **Dennett** (1991, 1995): Dennett argues that zombies are not really conceivable, that the appearance of conceiving one is a failure to represent physical detail. My objection grants, *arguendo*, that zombies may be ideally conceivable in the sense of having a determinate $\mathrm{Con}_a$ value; it denies only that the conceiver can be *warranted* in asserting that value. Dennett's is a claim about the metaphysics of the scenario; mine is a claim about the epistemology of the premise. They can both be right; they are not the same.

Against **type-B materialism** (Loar 1997; Papineau 2002; Block and Stalnaker 1999): the type-B materialist grants conceivability and denies CP, locating the necessitation of $C$ by $P$ in an *a posteriori* identity. My objection grants CP. Notably, the present argument does not need the type-B materialist's distinctive commitment; it shows the zombie argument unwarrantable even if the necessitation, should it hold, is *a priori*. It thus reaches a conclusion friendly to the type-B materialist by a route that does not presuppose her semantics of phenomenal concepts.

Against the **anti-zombie** objection (Frankish 2007): the anti-zombie strategy alleges a *symmetry* — that physicalism-vindicating "shombies" are as conceivable as zombies, yielding a standoff. My objection is not a symmetry claim. It does not say "conceive the opposite and cancel"; it says the conceiving on which the original argument relies cannot, on either side, be warrantedly performed for arithmetic-rich scenarios. Where the anti-zombie objection neutralizes the argument with a mirror-image conceiving, the present objection removes the faculty that both conceivings would require.

The closest kin is **Yablo** (1993), who asks whether conceivability is a guide to possibility and catalogues the ways the inference can fail. The present paper can be read as identifying a specific, formally characterized failure mode for a specific class of scenarios: where the modal claim demands ideal conceivability of an arithmetic-rich scenario, the guide is one no effective reasoner can consult.

## 9. Conclusion and Scope

Granting the conceivability principle and the conceivability-in-principle of zombies, the zombie argument still fails to be a cogent *a priori* proof of anti-physicalism. Establishing its first premise requires certifying the consistency of a scenario as logically rich as a complete physical description; reliable consistency-certification over such scenarios is Turing-equivalent to the halting oracle; and the trilemma on the nature of the mind shows that every way of possessing the requisite faculty defeats the argument's purpose — leaving the premise unwarrantable (D1), warranted only by inadmissible non-computable physics (D2), or warranted only by presupposing anti-physicalism (D3).

The scope of this result should be stated as carefully as the result. It does **not** show that physicalism is true. It does **not** show that zombies are inconceivable or impossible; their ideal conceivability may be a determinate fact. It does **not** refute the conceivability principle. It shows only that *this route* — establishing anti-physicalism via the ideal conceivability of zombies — cannot be traversed by any reasoner whose mind is physical and computable, and can be traversed by others only by assuming, rather than proving, the matter in dispute.

Two soft joints are flagged in the spirit of honest accounting. The force of the D2 horn depends on bundling PCTT into the targeted physicalism, or on the claim that an a priori argument may not lean on contested empirical physics. The escapee here must be not merely a non-computationalist about physics in general but a *cognitive* hypercomputationalist — one who holds that the reasoning faculty itself is a physical hypercomputer, the Penrose-style position located in §6 and §7.4. Such a theorist escapes the "begs the question" charge and faces only the "not a priori, dialectically loaded, and presupposed-not-argued" charge; the paper offers this as a real possibility and declines to adjudicate its truth. And (W), though weak and widely shared, is not beyond dispute; the conditional reading of §3 and §7.6 is available to those who balk at it. The D1 and D3 horns carry no comparable softness.

The governing image is exact rather than decorative. The faculty that could certify the zombie premise is the logically omniscient sage of the inductive puzzles, who knows at once every consequence of what is given. That sage decides the halting set. The halting set has no realizer in a world of computable physics. The sage, in such a world, does not exist — and an argument that can be completed only by consulting him cannot move those of us who must reason without him.

---

## References

Balog, K. (1999). Conceivability, Possibility, and the Mind-Body Problem. *Philosophical Review* 108(4).

Block, N., and Stalnaker, R. (1999). Conceptual Analysis, Dualism, and the Explanatory Gap. *Philosophical Review* 108(1).

Brown, R. (2010). Deprioritizing the A Priori Arguments Against Physicalism. *Journal of Consciousness Studies* 17.

Chalmers, D. (1996). *The Conscious Mind: In Search of a Fundamental Theory*. Oxford University Press.

Chalmers, D. (2002). Does Conceivability Entail Possibility? In T. Gendler and J. Hawthorne (eds.), *Conceivability and Possibility*. Oxford University Press.

Chalmers, D. (2010). *The Character of Consciousness*. Oxford University Press.

Church, A. (1936). An Unsolvable Problem of Elementary Number Theory. *American Journal of Mathematics* 58(2).

Copeland, B. J. (2002). Hypercomputation. *Minds and Machines* 12(4).

Dennett, D. (1991). *Consciousness Explained*. Little, Brown.

Dennett, D. (1995). The Unimagined Preposterousness of Zombies. *Journal of Consciousness Studies* 2(4).

Etesi, G., and Németi, I. (2002). Non-Turing Computations via Malament–Hogarth Spacetimes. *International Journal of Theoretical Physics* 41.

Frankish, K. (2007). The Anti-Zombie Argument. *Philosophical Quarterly* 57(229).

Gödel, K. (1931). Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I. *Monatshefte für Mathematik und Physik* 38.

Hogarth, M. (1992). Does General Relativity Allow an Observer to View an Eternity in a Finite Time? *Foundations of Physics Letters* 5.

Kripke, S. (1980). *Naming and Necessity*. Harvard University Press.

Loar, B. (1997). Phenomenal States. In N. Block, O. Flanagan, and G. Güzeldere (eds.), *The Nature of Consciousness*. MIT Press.

Lucas, J. R. (1961). Minds, Machines and Gödel. *Philosophy* 36(137).

Papineau, D. (2002). *Thinking About Consciousness*. Oxford University Press.

Penrose, R. (1989). *The Emperor's New Mind*. Oxford University Press.

Penrose, R. (1994). *Shadows of the Mind*. Oxford University Press.

Tarski, A. (1936). Der Wahrheitsbegriff in den formalisierten Sprachen. *Studia Philosophica* 1.

Turing, A. M. (1936). On Computable Numbers, with an Application to the Entscheidungsproblem. *Proceedings of the London Mathematical Society* s2-42.

Yablo, S. (1993). Is Conceivability a Guide to Possibility? *Philosophy and Phenomenological Research* 53(1).

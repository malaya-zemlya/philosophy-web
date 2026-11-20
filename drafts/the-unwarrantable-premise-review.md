# Review: "The Unwarrantable Premise"

*Review of [the-unwarrantable-premise.md](the-unwarrantable-premise.md), 2026-11-19.*

## Verdict

The formal components are correct, but the argument is **not sound as stated**. It fails at the step from
"no effective method decides consistency over arithmetic-rich theories" (L3) to "no computable reasoner is
warranted in asserting T1". Several independent problems sit at that step, and any one of them is enough
to block it.

The web nodes built from the paper are affected: `argument-unwarrantable-zombie-premise`,
`claim-zombie-premise-unwarrantable`, `claim-consistency-certification-is-oracle-hard` and the transferred
`argument-agent-causation-certificate`.

## What holds

- **The reduction (§5, L2/L3) is correct.** $T_{M,x} = Q \cup \{\neg h_{M,x}\}$ is consistent iff $M$ does
  not halt on $x$, so a method that decides consistency over arithmetic-rich theories decides $\emptyset'$.
  If a complete $P$ is not recursively axiomatized, the lower bound only gets stronger.
- **The trilemma (§6) is exhaustive.** Two bivalent questions yield three leaves.
- **The scope discipline (§9) is good.** The paper grants CP, grants that zombies may be conceivable in
  principle, and does not claim that physicalism is true.

## Problems, most serious first

### 1. Fallible warrant is dismissed, not refuted

L3 rules out an effective method that *infallibly decides* consistency. That excludes certification, not
justification, and §7.6 itself says (W) requires only justification. The paper closes the gap by treating
careful failure-to-refute as "the prima facie notion the argument disavows". That runs two claims together:

- Chalmers disavows prima facie conceivability as *entailing possibility*, which is why CP is stated for
  ideal conceivability.
- He does not disavow it as *defeasible evidence for* ideal conceivability. The SEP *Zombies* entry
  describes the conceivability claim as "an epistemic claim dependent on our cognitive abilities", and
  therefore defeasible (Kirk, "Zombies", §4).

The paper's own model case cuts against it. Belief in Con(ZFC) rests neither on a proof nor on a clear
grasp of an intended model. It rests largely on long, serious failure to find a contradiction, and it is
not regarded as unwarranted. The three-way split in §7.2 (demonstrative proof, positive grasp of a model,
worthless failure-to-find) leaves out this fourth source of warrant: fallible evidence. The web node
already names this as "the genuine open crux". The paper's answer, that any reliable insight collapses
into D2 or D3, depends on problem 2.

### 2. "Reliable" slides into "decides every case"

§5 requires a method that is "reliable across the class". Undecidability forbids a method that is correct
on *every* input. It does not forbid one that is highly reliable, for instance correct on all but a sparse
set of cases, or on the cases that actually arise. The reduction establishes worst-case hardness, while
warrant answers to reliability, so the step from L3 to "no reliable effective method" is invalid.

### 3. The reference class for reliability is arbitrary

The bridge from L3 to the single case $Z$ (end of §5) and the "notion-level" reply in §7.5 move from the
generality of CP ("for any $S$, $\mathrm{IC}(S) \to \Diamond S$") to the claim that the conceiver's
*competence* must be general over all arithmetic-rich theories. These are different kinds of generality:

- CP is a universally quantified conditional, a claim about the relation between ideal conceivability and
  possibility.
- Applying CP to $Z$ needs warrant only for the antecedent instance, by whatever method actually produced
  it.
- Reliability is judged against that method's own reference class, not the widest class one can name. This
  is the generality problem for reliabilism.

§7.2(a) concedes the point: particular $\Pi_1$ truths *are* known by methods that are reliable only over
narrow classes.

### 4. The arithmetic that carries the hardness is common ground

$P$ is true of the actual world, and both parties accept that. Since truth implies consistency, Con($P$) is
warranted at no cost, with no oracle. Next, suppose no a priori bridge truths link the phenomenal
vocabulary in $C$ to $P$'s vocabulary. Then $P \wedge \neg C$ is consistent *relative to* $P$ by an
elementary construction: take any model of $P$ and give the phenomenal predicates the empty extension.

So $\mathrm{Con}_a(Z)$ reduces to the question whether there *are* a priori bridge principles. That is the
type-A versus non-type-A dispute about the analysis of phenomenal concepts, and it is where Chalmers's
actual warrant for T1 operates (structural truths entail only structural truths). The halting-hardness
sits in the arithmetic content of $P$, which nobody disputes, and the reduction never reaches the bridge
question. The case-level reply in §7.5 ("whether $P \wedge \neg C$ is consistent turns inter alia on halting
facts about the machines $P$ describes") is true only if the bridge principles themselves refer to such
facts, and the paper does not argue that they do.

### 5. A logical model is confused with a possible world

§7.2(a) says that proving $\mathrm{Con}_a(Z)$ "would require exhibiting a model of $P \wedge \neg C$ —
precisely the anti-physicalist's contested claim, now asserted rather than imagined." A model in the
logician's sense establishes *consistency*, which is T1, not $\Diamond Z$. Getting from consistency to
possibility is CP's work, and the paper grants CP. The charge of begging the question therefore fails.

### 6. Most physicalists accept T1

Type-B physicalists grant that zombies are ideally conceivable and deny CP (Loar 1997; Papineau 2002; Block
and Stalnaker 1999 deny an a priori entailment from $P$ to $C$). Against them, (W) is *satisfied*: the
audience accepts the premise without accepting the conclusion. §8 says the objection "reaches a conclusion
friendly to the type-B materialist". In fact it implies that type-B physicalists cannot be warranted in
their own explanatory-gap thesis, so it proves too much inside physicalism. The objection's dialectical
force is confined to type-A physicalists, and against them the real dispute is the conceptual one in
problem 4.

### 7. D2 and D3 assume an internalist reading of "presupposing"

On an externalist account of warrant, a reasoner with a reliable faculty is warranted whether or not she
*believes* anything about what realizes that faculty.

- **D3** is therefore not "already accepting the conclusion". The conceiver need not assume that her mind
  is non-physical in order to be warranted.
- **D2** is not "importing an empirical premise into an a priori argument". Arithmetic knowledge is a
  priori although the nature of the brain is an empirical matter, so a belief can be a priori even when
  the nature of the faculty that produced it is empirical.

Both horns lose their force unless the paper argues for internalism about warrant, and it does not.

## What survives

A narrower thesis holds: **no computable reasoner can have conclusive, certification-level warrant for
T1, so the zombie argument cannot be a demonstrative proof.** This is true, and it comes with a precise
computability-theoretic explanation. It is, however, a weaker result than the paper claims, because the
live debate already treats T1 as defeasibly justified and argues about the existence of a priori bridge
principles.

## Routes to a stronger version

1. **Defeat fallible warrant for this case specifically.** Argue that defeasible evidence cannot support
   $\Pi_1$ claims of this shape, for example because the physicalist's hypothesis predicts exactly the same
   failure-to-refute evidence, so the evidence does not discriminate between the hypotheses. This answers
   problems 1–3 together, and it is probably the most promising route.
2. **Make the bridge question hard.** Argue that whether a priori bridge principles exist is itself
   $\emptyset'$-hard, for instance because candidate functionalist analyses of consciousness are
   $\Sigma_1$ conditions on the computations $P$ describes. This answers problem 4.
3. **Re-aim at type-A physicalism** and say so explicitly. This answers problem 6.
4. **Argue for internalism about warrant**, or recast D2/D3 so that they do not depend on it. This answers
   problem 7.
5. Repair §7.2(a), the model/world confusion (problem 5).

## Consequences for the web

`argument-unwarrantable-zombie-premise` and `claim-zombie-premise-unwarrantable` are currently `status:
asserted`, and of the problems above only problem 1 is acknowledged, as an open crux. Options:

- Record problems 1, 4 and 6 as objection arguments that `attacks` the argument or its premises. The natural
  targets are `claim-consistency-certification-is-oracle-hard` (the "reliable over the class" step) and the
  conclusion claim.
- Set the conclusion claim to `status: contested`.
- Apply the same review to `argument-agent-causation-certificate`, which reuses all three premises.

The objection nodes would need sources:

- the generality problem: Conee & Feldman (1998);
- relative consistency via new vocabulary: a standard model-theory text;
- fallible belief in Con(ZFC): to be researched;
- the SEP *Zombies* entry on defeasibility.

None of these sources has been researched yet, and no citation in this file has been verified against the
original works.

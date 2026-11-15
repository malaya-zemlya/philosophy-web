---
id: dilemma
title: Argument by Dilemma (and n-lemma)
aka: [constructive dilemma, destructive dilemma, trilemma, n-lemma, disjunctive elimination, forced choice]
source: classical logic (constructive and destructive dilemma; disjunctive syllogism); project extension as a
  pattern, not in Walton's canon
inference_form: deductive
---

## Form
- Premise (Partition): Either $A_1$ or $A_2$ or … or $A_n$. (For a dilemma $n = 2$; trilemma $n = 3$.)
- Premise (Horn $i$, one per option): If $A_i$, then $C_i$.
- Premise (Verdict): Each $C_i$ is unacceptable to the opponent (or: each $C_i$ entails the same $C$).
- Conclusion: The opponent's position is untenable (or: $C$).

Variants:
- **Constructive**: $A \lor B$, $A \to C$, $B \to D$ ⊢ $C \lor D$. In the *simple* case $C = D$ and
  the conclusion is $C$ outright.
- **Destructive**: $A \to C$, $B \to D$, $\lnot C \lor \lnot D$ ⊢ $\lnot A \lor \lnot B$.
- **Eliminative** (disjunctive syllogism): every horn but one is closed off, so the remaining one
  must be accepted. Strawson's genetic argument for panpsychism has this shape.
- **Graded partition**: the options are regions of a continuum ("too strict / too loose", "too
  liberal / too chauvinistic"), not discrete alternatives. The grain dilemmas have this shape.

## Critical questions
1. **exhaustiveness**: Do the options really exhaust the possibilities, or is there a way between
   the horns (a false dilemma)? For a graded partition: is there a principled intermediate point,
   and has the arguer shown that every point on the continuum falls under some horn? → attacks the
   *Partition* premise (cf. `web/arguments/organisational-grain-dissolves-dilemma.md`, which escapes
   between the horns of the grain dilemma).
2. **horn-link**: Does option $A_i$ really lead to $C_i$, or can the opponent take hold of that horn
   and deny the consequence follows? Ask this of each horn separately; one horn is usually weaker.
   → attacks one *Horn* premise (cf. `web/arguments/strong-emergence-acceptable.md`, which grasps
   the emergence horn of the genetic argument).
3. **bullet**: Is $C_i$ really unacceptable, or can the opponent accept it at tolerable cost? →
   attacks the *Verdict* premise (cf. Carruthers accepting that most animals lack phenomenal
   consciousness rather than abandon higher-order theory).
4. **equivocation**: Is a key term read the same way in every horn, or does each horn use the
   reading that makes it bite? → attacks the inference (a dilemma that partitions on one sense of
   "physics" and evaluates a horn on another fails, for example).
5. **proves-too-much**: Does an exactly parallel dilemma hit the arguer's own view, or every rival
   view? Then it shows a shared burden, not a defect of the target. → bounds the conclusion (the
   standard tu quoque reply to grain dilemmas: every theory of consciousness owes a principled grain).
6. **counter-dilemma**: Can the opponent build a rebutting dilemma from the same partition with the
   opposite conclusion (the classical "rebuttal" of a dilemma, as in Protagoras and Euathlus)? →
   raises a competing argument.

## Notes
**Any conditional is a dilemma.** An argument of the shape $X \to Y$ can always be restated as
"either $Y$ or not-$X$", since $X \to Y$ is equivalent to $\lnot X \lor Y$. The restatement changes no
logical content but often changes the argument's force. It turns a derivation into a forced choice
for the opponent, who must now either give up $X$ or swallow $Y$, and it makes the familiar point
that one person's modus ponens is another's modus tollens explicit. It is worth doing when $X$ is
something the opponent holds and $Y$ something they would reject. Then the restated argument says
plainly what it costs them to keep $X$. When citing `pattern: dilemma` for a restated conditional,
note that CQ-exhaustiveness is trivially met (the partition is $\lnot X$ versus $X$), so the attack
surface collapses onto CQ-horn-link (does $X$ really lead to $Y$?) and CQ-bullet (is $Y$ really so
bad?).

For an n-lemma, name the horns in the body (*Horn A*, *Horn B*, …) and say which one the arguer
takes to be the weakest escape route. That is almost always where the opponent will push. An
argument with one pattern slot can still cite `dilemma` when its partition is graded and its horns
are filled by thought experiments. Cite the pattern that carries the argument's main weight.

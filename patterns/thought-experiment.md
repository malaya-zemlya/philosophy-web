---
id: thought-experiment
title: Argument from a Thought Experiment
aka: [intuition pump, imagined counterexample, method of cases]
source: project extension (not in Walton's canon); cf. Dennett's "intuition pumps",
  Gettier-style counterexamples, the method of cases in analytic philosophy
inference_form: counterexample
---

## Form
- Premise (Scenario): Consider an imagined case S, described in such-and-such terms.
- Premise (Intuition): Competent judges intuit verdict V about S.
- Premise (Bridge): V is incompatible with thesis T (or: V is what T must explain).
- Conclusion: T is false / inadequate (or: T is supported), defeasibly.

This is the move behind most of the web's set pieces — the lookup-table/blockhead case, the
Chinese Nation, dancing/inverted qualia, Parfit's rewiring. It refutes a *universal* or
*sufficiency* thesis by exhibiting one case the thesis gets wrong.

## Critical questions
1. **coherence** — Is the scenario S actually coherent / genuinely possible, or does its
   description smuggle in an impossibility? → attacks the *Scenario* premise (cf.
   `web/arguments/lookup-table-physical-impossibility.md`,
   `web/arguments/lookup-table-combinatorial-impossibility.md`).
2. **verdict** — Is intuition V robust and widely shared, or parochial / theory-laden / an
   artefact of how S was framed? → attacks the *Intuition* premise.
3. **trained-domain** — Is the intuition operating inside the domain it was trained on, or
   extrapolated past it? → attacks the *Intuition* premise's warrant (cf.
   `web/arguments/intuition-domain-asymmetry.md`).
4. **bridge** — Does V really bear on T, or only on a neighbouring thesis T′? Does T have a
   reading that the case doesn't touch? → attacks the *Bridge* premise (the standard "your case
   refutes behaviourism, not organisational functionalism" move — cf.
   `web/arguments/organisational-grain-dissolves-dilemma.md`).
5. **begs-the-question** — Does fixing the verdict require already assuming T is false? → attacks
   the inference as circular (cf. `web/arguments/dancing-qualia-begs-the-question.md`).
6. **scope** — Even granting V, exactly which theses does the case threaten, and which does it
   leave standing? → bounds the conclusion rather than defeating it.

## Notes
This pattern is the workhorse of the existing web, so its CQs are deliberately aligned with moves
already present. When citing `pattern: thought-experiment`, state the bridge (premise 3) in the
body explicitly — most live cruxes here are CQ-bridge and CQ-scope (which thesis the case really
hits), not CQ-coherence. CQ-begs-the-question applies sharply to *self-undermining* cases (dancing
qualia) where the verdict and the thesis under test are the same intuition.

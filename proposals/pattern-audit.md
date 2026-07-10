# Argument-pattern audit — 2026-07-09

Scope: every `argument` node in `web/arguments/` (110 files), checked against the seven
schemes in `patterns/`. Two deliverables: (1) `pattern:` declarations added where a scheme
genuinely fits; (2) a critical-question (CQ) coverage map for every patterned argument, with
drafted sharper objections for the open CQs — a ready menu for future debate turns, per
`patterns/_README.md` ("each unanswered CQ is a ready-made line of attack").

**Citations caveat:** the objection sketches below name real literature from model knowledge.
Before promoting any sketch into a web node, research the exact citation and create/cite a
`source` node per rule 10 — do not copy a reference from this file unverified.

> **Follow-up (2026-07-09, same day).** Two things since this audit: (a) a **`best-explanation`**
> pattern now exists (`patterns/best-explanation.md`) — the IBE gap noted in §1 is closed, and
> its five customers (`explanatory-gap`, `intrinsic-nature`,
> `teleosemantics-explains-misrepresentation`, `llm-representations-reply`,
> `deutsch-anti-solipsism`) are tagged. (b) **Ranked openings 1–5 (§3) are filled** as real
> nodes, with researched `source` nodes — no longer sketches. New objection nodes:
> `two-sided-precaution` + `unforgeability-proxy` (opening 1), `undivided-split-brain` +
> `conscious-usa-counter-analogy` (opening 2), `mary-scope-reply` + `mary-equivocation`
> (opening 3), `anti-zombie-parity` (opening 4), `trained-mimicry-rival` (opening 5). The
> §2 coverage rows for these CQs are now **raised**, not open. Opening 4's companion (Dennett
> CQ1 under-specification charge on `zombie-conceivability`) remains open, as do all the
> non-ranked family objections below.

## 1. Coverage

Before: 23 of 110 arguments declared a pattern. After: **32**. The remaining 78 were each
read and classified: they are deductive derivations, constructive dilemmas, regresses,
parity/"proves-too-much" reductios, question-begging charges, inferences to the best
explanation, or conceptual distinctions — moves the pattern library deliberately does not
cover. Omission there is per the schema checklist ("deliberately omitted because none fits"),
not backlog. IBE is the most common unrepresented engine (e.g. `explanatory-gap`,
`intrinsic-nature`, `teleosemantics-explains-misrepresentation`, `llm-representations-reply`,
`deutsch-anti-solipsism`); if a `best-explanation` pattern is ever added to `patterns/`, those
five are its first customers.

### New declarations (9)

| argument | pattern | why |
|---|---|---|
| `china-nation-absent-qualia` | thought-experiment | canonical absent-qualia intuition pump; body says "counterexample, an intuition pump" |
| `brain-simulator-reply` | thought-experiment | imagined synapse-level simulator + "what difference could remain" intuition against A3 |
| `parfit-rewiring` | thought-experiment | imagined rewiring spectrum + tolerance intuition; named as a set piece in `patterns/thought-experiment.md` itself |
| `rejoinder-chinese-gym` | thought-experiment | imagined parallel gym + "no one understands" verdict, extending A3 |
| `rejoinder-internalize-rulebook` | thought-experiment | imagined memorised-rulebook variant + "still understands nothing" verdict |
| `rejoinder-room-in-robot` | thought-experiment | imagined man-in-robot's-head variant + "symbols still meaningless" verdict |
| `rejoinder-water-pipes` | thought-experiment | imagined water-pipe brain + "nothing understands" verdict |
| `other-minds-reply` | analogy | parity-of-cases: verdict (credit understanding on behavioural grounds) transferred from humans to the behaviourally identical room |
| `rights-sign-forgeable` | consequences | prudential should-conclusion: don't adopt the gameable criterion, because of what adopting it causes |

Notable non-assignments (classifier verified by hand): `olympia-recording-objection` (a
CQ2/CQ6-raising dissolution, not itself a scheme), `bike-rider-learns-facts` (deductive from
the Stanley–Williamson thesis), `chinese-room-derivation` (deliberately the *deductive*
presentation, contrasted with the `chinese-room` intuition pump), `sorites-paradox` and the
continuity-schema arguments (their engine is the tolerance-premise reductio, catalogued as
`concept-continuity-argument-schema`, not a Walton scheme).

## 2. CQ coverage map

"Raised" means an existing argument node attacks this argument (or one of its premise claims)
in a way that instantiates the CQ, even if the body doesn't name it. "Open" CQs are the
attack surface no node yet occupies.

### thought-experiment (20)  — CQs: 1 coherence · 2 verdict · 3 trained-domain · 4 bridge · 5 begs-the-question · 6 scope

| argument | raised | open (sharpest bolded) |
|---|---|---|
| `chinese-room` | CQ4 (`systems-reply`), CQ6 (`systems-reply`, `connectionist-reply`, `many-mansions-reply`), CQ2 (`other-minds-reply`) | CQ1, CQ3, **CQ5** |
| `knowledge-argument` | CQ2 (`ability-hypothesis`, `acquaintance-hypothesis`, `mary-misimagined`), CQ4 (`old-fact-new-guise`, `indexical-reply`, `llmary-token-encounter`), CQ1 (`mary-omniscience-unrealizable`) | CQ3, **CQ5**, **CQ6** |
| `lookup-table-objection` | CQ1 (`lookup-table-physical-impossibility`, `lookup-table-combinatorial-impossibility`, `storage-not-stable-kind`), CQ2 (`blockhead-dilemma`) | CQ3, **CQ4**, **CQ5**, CQ6 (CQ4/CQ6 partly absorbed in-body and via `organisational-grain-dissolves-dilemma`) |
| `olympia` | CQ1 + CQ6 (`olympia-quantum-counterfactuals`), CQ2 + CQ6 (`olympia-recording-objection`) | CQ3, **CQ4**, **CQ5** |
| `dancing-qualia` | CQ2 + CQ5 (`dancing-qualia-no-memory-trace`; `dancing-qualia-begs-the-question` presses CQ5 at the deployment) | CQ1, CQ3, **CQ4**, **CQ6** |
| `zombie-conceivability` | CQ4 (`conceivability-not-guide-to-possibility`); `unwarrantable-zombie-premise` is a warrant-level attack outside the six | **CQ1**, CQ3, **CQ5**, CQ6 |
| `role-grain-dilemma` | CQ4 (`organisational-grain-dissolves-dilemma`) | **CQ1**, **CQ2**, CQ3, CQ5, CQ6 |
| `brain-simulator-reply` | CQ4 + CQ2 (`rejoinder-water-pipes`) | **CQ1**, CQ3, **CQ5**, CQ6 |
| `china-nation-absent-qualia` | none wired (Systems Reply + `gap-deflated-by-phenomenal-concepts` recorded in prose only) | **CQ1**, **CQ2**, CQ4, CQ6 |
| `dense-china-brain-regress` | none | **CQ1**, **CQ5** |
| `fading-qualia` | none wired (begs-question charge exists as a node but targets `dancing-qualia`) | CQ2, **CQ5** |
| `fission` | none | CQ2, **CQ4**, **CQ6** |
| `llmary-token-encounter` | none wired (phenomenal-realist dilemma self-recorded in prose) | **CQ1**, **CQ4** |
| `parfit-rewiring` | none wired (rival horns recorded in prose) | **CQ2**, **CQ5** |
| `rejoinder-chinese-gym` | none wired (Churchlands' charge in prose) | CQ2, **CQ5** |
| `rejoinder-internalize-rulebook` | none wired (level-confusion crux in prose) | CQ2, **CQ4** |
| `rejoinder-room-in-robot` | none wired ("misses the reply" crux in prose) | **CQ4**, **CQ5** |
| `rejoinder-water-pipes` | none wired (dilemma crux self-stated) | CQ2, **CQ5** |
| `swampman` | none wired (bullet-biting reply in prose; `teleosemantics-explains-misrepresentation` is the positive counterpart) | **CQ2**, **CQ4**, CQ6 |
| `transplant-intuition` | none wired (animalist reply self-flagged, citing Olson) | CQ2, **CQ3**, **CQ4** |

### analogy (6) — CQs: 1 relevance · 2 disanalogy · 3 base · 4 counter-analogy

| argument | raised | open (sharpest bolded) |
|---|---|---|
| `report-scepticism-proves-too-much` | CQ2 on both arms (`de-novo-origination-breaks-report-parity` on R2, `feel-is-the-watching-not-an-unwatched-difference` on R1) | **CQ1**, CQ3, **CQ4** |
| `other-minds-reply` | CQ1 (`rejoinder-attribution-vs-detection`) | **CQ2**, CQ3, **CQ4** |
| `introspective-gap-from-internal-limits` | CQ2 (`architectural-account-leaves-hard-problem`, via the conclusion claim) | **CQ1**, CQ3, **CQ4** |
| `de-novo-origination-breaks-report-parity` | none | **CQ1**, **CQ3** |
| `luminous-room` | CQ2 in-body only (Searle's reply) | **CQ1**, CQ3, **CQ4** |
| `subjects-can-combine` | none (CQ2 self-anticipated in prose) | CQ1, **CQ3**, **CQ4** |

### sign (3) — CQs: 1 reliability · 2 alternatives · 3 forgeability

| argument | raised | open (sharpest bolded) |
|---|---|---|
| `behavioral-parity` | CQ3 three ways (`lookup-table-objection`, `rights-sign-forgeable`, `role-grain-dilemma`; the latter also presses CQ1 at premise 1) | **CQ2** (trained-mimicry form), **CQ1** (constitution form) |
| `consciousness-freewill-duality` | CQ1 (`graded-polarity`, via the polarity premise claims) | **CQ2**, **CQ3** |
| `llm-workspace-from-functional-signature` | none (CQ2/CQ3 self-discussed in the weakest-premise section) | CQ1, **CQ2**, **CQ3** |

### cause-to-effect (1) — CQs: 1 strength · 2 other-causes · 3 interference · 4 correlation

| argument | raised | open |
|---|---|---|
| `ai-hard-problem-from-self-model-architecture` | CQ1 (`self-model-prediction-phenomenality-neutral`, explicitly), CQ2 (`contaminated-testimony-carries-no-weight`) | **CQ3**, **CQ4** |

### example (1) — CQs: 1 support · 2 representativeness · 3 counter-examples

| argument | raised | open |
|---|---|---|
| `introspective-confabulation` | CQ2/CQ3 (`no-appearance-reality-gap`, via the supported thesis) | **CQ1** |

### consequences (1) — CQs: 1 likelihood · 2 evidence · 3 counter-consequences · 4 value

| argument | raised | open |
|---|---|---|
| `rights-sign-forgeable` | none | CQ1, CQ2, **CQ3**, **CQ4** |

## 3. Sharper objections (debate-turn menu)

Drafted in neutral voice, each opening with the schema's `Raises <pattern> CQ<n> (<slug>)`
convention. These are sketches, not nodes: a character (or `/import-argument`) should own the
move, verify the citation, and wire the `attacks` edge at the premise the CQ targets.

### Highest-value openings (ranked) — ✅ all five FILLED (2026-07-09)

Node ids: (1) `two-sided-precaution` + `unforgeability-proxy`; (2) `undivided-split-brain` +
`conscious-usa-counter-analogy`; (3) `mary-scope-reply` + `mary-equivocation`; (4)
`anti-zombie-parity` (companion CQ1/Dennett still open); (5) `trained-mimicry-rival`.

1. **`rights-sign-forgeable` ← consequences CQ3 (counter-consequences).** The flesh
   criterion's own consequence column is empty in the web: resting standing on biology
   wrongly denies standing to any genuinely sentient digital system, and wrongful exclusion
   of a real mind is a grave moral cost, not a safe default (Schwitzgebel & Garza 2015;
   Birch, *The Edge of Sentience*, 2024, makes precaution explicitly two-sided). Until this
   is answered, "caution" begs which error is worse. Companion CQ4 (value): unforgeability
   is a value of epistemic security against deception, not of tracking suffering — the
   policy substitutes the proxy for the value, as its own fingerprint concession shows.
2. **`subjects-can-combine` ← analogy CQ3 (base).** The flagship base case may not exhibit
   merging at all: Pinto et al., "Split brain: divided perception but undivided
   consciousness" (*Brain*, 2017) report divided perceptual access with a single undivided
   responding subject. If the split brain is one subject with disunified access, premise 1
   loses its principal support. Companion CQ4: Schwitzgebel's conscious-USA case (2015) — a
   densely integrated group agent most treat as a reductio — shows integration bandwidth can
   be satisfied while subjecthood is intuitively absent.
3. **`knowledge-argument` ← thought-experiment CQ6 (scope).** Even granting the epistemic
   gap, the case bounds only a-priori/deducibility physicalism, leaving a-posteriori
   token-identity physicalism untouched (Horgan, *Philosophical Quarterly*, 1984).
   Companion CQ5: reading "learns something" as "learns a new *fact*" individuates facts
   finely enough to outstrip the physical only if physicalism is already assumed false
   (Churchland, *Journal of Philosophy*, 1985).
4. **`zombie-conceivability` ← thought-experiment CQ5 (begs-the-question).** The anti-zombie
   parity argument: a world where the physical necessitates the phenomenal is equally
   conceivable, and the same bridge then proves physicalism true; the intuitions are
   symmetric until one side is presupposed (Frankish, "The Anti-Zombie Argument,"
   *Philosophical Quarterly*, 2007). Companion CQ1: the Dennettian charge that the scenario
   is only apparently conceivable through under-specification (Dennett 1995).
5. **`behavioral-parity` ← sign CQ2 (alternatives), trained-mimicry form.** For a system
   trained by next-token prediction on a human corpus, the rival state the behavioural sign
   indicates is high-fidelity distributional imitation of mind-talk, not realisation of the
   mental role — and the training objective makes that rival antecedently likely, so the
   argument's own IBE form obliges it to rule the rival out (Bender & Koller 2020; Bender et
   al. 2021).

### thought-experiment family

- **`chinese-room`** — CQ5: the verdict is secured by looking for understanding where a
  component could introspectively report it, presupposing understanding cannot be a
  system-level property of rule-governed manipulation — the negation of the thesis under
  test; the room is an intuition pump whose staging smuggles the conclusion (Dennett 1991;
  Hofstadter & Dennett 1981). CQ1: a static shape-keyed rulebook sustaining open-ended apt
  conversation may be an impossible object — anything that actually does this computes and
  generalises (cf. Block 1981) — so the case is unrealisable or has quietly become a genuine
  processor.
- **`knowledge-argument`** — see ranked list (CQ6, CQ5).
- **`lookup-table-objection`** — CQ4: Block himself aims the blockhead at input–output
  functionalism and grants the table lacks the requisite internal states ("Troubles with
  Functionalism," 1978), so the verdict refutes behaviourism/IO-functionalism (T′), not the
  organisational functionalism actually defended for LLMs. CQ5: "full behavioural profile
  but no mind" *just is* the denial of behaviourism, so against the behaviourist the
  intuition restates the dispute.
- **`olympia`** — CQ4: the trilemma bites only a counterfactual/dispositional theory of
  implementation; a mechanistic account of implementation (cf. Chalmers, *Synthese*, 1996)
  can deny that inert blocked-Klara scaffolding makes Olympia implement π, dissolving the
  triad. CQ5: resolving the triad by dropping Sufficiency rather than Supervenience
  presupposes that standing counterfactual structure is causally idle — the very thesis the
  computationalist denies.
- **`dancing-qualia`** — CQ6: the reductio secures at most *nomological* organisational
  invariance, compatible with metaphysically possible inverts — too weak for metaphysical
  substrate-independence (Chalmers 1996, ch. 7, restricts it himself). CQ4: the switching
  device fixes introspective *judgement and report* (access), not phenomenal character;
  identifying the two is exactly what the access/phenomenal distinction blocks (Block, *BBS*,
  1995).
- **`zombie-conceivability`** — see ranked list (CQ5, CQ1).
- **`role-grain-dilemma`** — CQ2: horn 1's "no mind" verdict on the China-system is a
  contestable intuition a functionalist may bite (Block 1978 concedes the bullet-biting
  option), not a fixed absurdity. CQ1: the too-liberal horn rests on the cosmically
  unrealisable table (the web's own `lookup-table-physical-impossibility`), so if the only
  buildable coarse-role realiser is organised, horn 1 has no instance.
- **`brain-simulator-reply`** — CQ5: "must understand on pain of denying the brain does"
  presupposes organisational sufficiency, the thesis A3 denies — the reply asserts rather
  than argues against biological naturalism (Searle 1980, 1992). CQ1: "simulates exactly,
  synapse by synapse" equivocates between formal pattern-duplication and causal-power
  duplication; on the first reading the verdict is contested, on the second it is no longer
  a *program* — the instancing/depicting seam.
- **`china-nation-absent-qualia`** — CQ2: the absent-qualia verdict may have no evidential
  standing — if functionalism is true a full isomorph must share qualia, so the confident
  "nothing it is like" either presupposes functionalism false or is an artefact of imagining
  scattered people rather than one organised subject (Shoemaker, "Absent Qualia Are
  Impossible," *Philosophical Review*, 1981). CQ1: a population signalling at human speed
  may realise only a slowed caricature — if organisation includes timing (Chalmers 1996 on
  fine-grained organisation), the nation is not the isomorph it advertises.
- **`dense-china-brain-regress`** — CQ5: Horn B assumes fine timing and causal density lie
  *below* the transition structure; on the fine-grained construal of organisation they are
  part of it, so the dilemma has an unexcluded middle. CQ1: drill-enforced counterfactuals
  may depict rather than instantiate the structure (Maudlin, *J. Phil.*, 1989).
- **`fading-qualia`** — CQ5: holding the isomorph's introspective judgement fixed
  presupposes functionalism about introspection; if introspection is partly acquaintance,
  the judgement fades with the quale and no deceived introspector is ever constructed (the
  assumption Chalmers isolates himself). CQ2: the "too weird to believe" step is a
  plausibility cost a biological naturalist simply pays (Searle 1992).
- **`fission`** — CQ4: the perdurantist multiple-occupancy reply — two persons shared their
  pre-fission stages, continuity stays one-one at the stage level (Lewis, "Survival and
  Identity," 1976). CQ6: at most the case forces a uniqueness clause (closest-continuer /
  no-branching repair, Nozick 1981), not abandonment of the continuity criterion.
- **`llmary-token-encounter`** — CQ1: a gradient step is a sub-personal weight adjustment,
  not personal-level acquisition of knowledge-that; if the "gain" isn't knowledge in the
  argument's sense, the counterexample's antecedent is unsatisfied (personal/sub-personal
  distinction, Dennett 1969; Lewis 1988). CQ4: the conceded phenomenal reading is the only
  one the knowledge argument ever asserted (Jackson 1986), so refuting the access reading
  refutes T′.
- **`parfit-rewiring`** — CQ2: epistemicism denies the tolerance premise — a sharp,
  unknowable cutoff exists and tolerance intuitions are ignorance artefacts (Williamson,
  *Vagueness*, 1994). CQ5: reading the graded middle as identity *itself* coming in degrees
  presupposes the reductionist bundle view against the simple view (Chisholm 1976; Swinburne
  in Shoemaker & Swinburne 1984).
- **`rejoinder-chinese-gym`** — CQ5: the gym re-asserts A3 against the very objection that
  contested it (Churchlands, "Could a Machine Think?", 1990). CQ2: "the crowd understands no
  more than any member" is the disputed claim, not a datum — no single neuron understands
  either.
- **`rejoinder-internalize-rulebook`** — CQ4: internalising makes the man *host* a second
  system, not *be* it, so "the man doesn't understand" again reports the wrong system (the
  virtual-mind reading, Hofstadter & Dennett 1981). CQ2: whether a person who has absorbed
  the rules to fluency "still understands nothing" is not a stable stipulation.
- **`rejoinder-room-in-robot`** — CQ4: the Robot Reply's thesis is about the grounded
  *system*; the man-in-the-head verdict reaches only the cog (cf. Harnad 1990). CQ5:
  "changes what symbols do, not what they mean" asserts that causal grounding cannot
  constitute content — precisely what informational semantics contests (Dretske 1981).
- **`rejoinder-water-pipes`** — CQ5: the "mere simulation" label is earned only if the
  causal-powers thesis is already granted; against a stipulated functional duplicate it begs
  the question (Churchlands 1990; Chalmers 1996). CQ2: the "obviously not" verdict on
  plumbing trades on homely scale — unreliable exactly where needed.
- **`swampman`** — CQ2: the pro-content intuition has no standing against a naturalistic
  theory; teleosemanticists bite the bullet outright (Millikan, "On Swampkinds," 1996;
  Papineau 2001). CQ4: the case refutes only *etiological* content theories; history-free
  accounts (Fodor's asymmetric dependence, 1990) count Swampman as a confirming case.
- **`transplant-intuition`** — CQ4: the animalist re-description — intuition tracks what
  *matters*, not numerical identity; Brown dies, Brownson is a new bearer of his mental life
  (Olson, *The Human Animal*, 1997; already self-flagged in-body, unoccupied as a node).
  CQ3: identity intuitions were never calibrated on brain-swaps; unanimity evidences a
  shared imaginative habit, not a tracked fact (Wilkes, *Real People*, 1988).

### analogy family

- **`report-scepticism-proves-too-much`** — CQ1: for a type-B physicalist the mechanistic
  explanation of human reports is not phenomenality-*neutral* — the mechanisms may *be* the
  phenomenal properties (Loar 1997; Papineau 2002), so discount-rule R1's antecedent is
  unmet for humans; independent of the existing first-person-datum reply. CQ4: sole-source
  first-person testimony is sometimes *correctly* discounted wholesale (Nisbett & Wilson
  1977), severing "only evidence" from "cannot be discounted."
- **`other-minds-reply`** — CQ2: the classical other-minds inference runs on behaviour
  *plus* constitutional likeness (Mill 1865; Russell 1948); the Room lacks the second
  conjunct, so no double standard. CQ4: Block's lookup-table conversationalist (1981) is a
  behaviourally indistinguishable third case where we confidently withhold understanding.
- **`introspective-gap-from-internal-limits`** — CQ1: what generates genuine independence in
  the formal base case is diagonal self-reference, not mere poverty of observables (Putnam
  1960; Feferman 1995 on informal Gödel transfers); limited access shares the incidental
  respect, not the relevant one. CQ4: a system whose self-access is enriched (neurofeedback,
  externalised read-out) and whose gap-sense recedes would show the gap is an access deficit,
  not an architectural invariant.
- **`de-novo-origination-breaks-report-parity`** — CQ3: the base verdict ("conceived de novo")
  is historically contestable — the what-it-is-like locution predates Nagel (Farrell, *Mind*,
  1950) and the framers worked inside an inherited dualist discourse, so the R2 trigger may
  not be "demonstrably unmet" for humans. CQ1: provenance may be the wrong variable — a
  topic-neutral debunking mechanism would produce the discourse afresh in any lossy
  self-modeller (Chalmers, "The Meta-Problem," 2018).
- **`luminous-room`** — CQ4: "obviously this doesn't think" intuitions are not uniformly
  unreliable — Block's lookup-table intuition (1981) is widely taken to track something real,
  so one discredited instance shows defeasibility, not worthlessness. CQ1: the luminosity
  intuition failed for a specific reason (sub-threshold magnitude) that is *absent* in the
  target — Searle's verdict claims to survive any speed or scale (Searle, *Sci. Am.*, 1990).
- **`subjects-can-combine`** — see ranked list (CQ3, CQ4).

### sign family

- **`behavioral-parity`** — see ranked list (CQ2). Also CQ1 (reliability): the
  behaviour→mind correlation was calibrated on beings sharing our constitution and
  evolutionary history; an artefact engineered to reproduce the output sits outside the
  calibration range, so premise 2 cannot simply inherit the everyday correlation.
- **`consciousness-freewill-duality`** — CQ3 (forgeability): a correspondence table can be
  manufactured by selection — recording arrow-reversals that land on existing positions and
  passing over flips that fail; without an accounting of negative analogy (Hesse 1966) the
  matching entries are partly produced by the method. CQ2 (alternatives), sharpened: absent
  a systematicity criterion (Gentner 1983) the matched pairs evidence only the generic shape
  of any realist-vs-deflationist stalemate — the rival the body concedes but no node presses.
- **`llm-workspace-from-functional-signature`** — CQ2: "workspace" reads functionally
  (Baars) or architecturally (recurrent ignition, Dehaene & Changeux 2011); broadcast within
  a feedforward pass is, for recurrent-processing theorists, the signature of *unconscious*
  processing (Lamme 2006), so the five-property sign underdetermines workspace against mere
  feedforward integration. CQ3: the J-space is *identified* by the verbalizability lens, so
  the "names its J-space contents when asked" premise is partly guaranteed by the detector's
  construction — the sign is manufactured by the instrument (form/meaning conflation, Bender
  & Koller 2020).

### cause-to-effect

- **`ai-hard-problem-from-self-model-architecture`** — CQ4 (correlation): human co-occurrence
  of ineffable self-presentation and hard-problem talk is equally compatible with a
  common-cause structure in which a genuine phenomenal fact produces both; discharging that
  is the meta-problem's burden (Chalmers 2018), and until then the generalisation is not
  shown causal. CQ3 (interference): instruction-tuned assistants are trained to disclaim
  inner experience — a masking variable symmetric to the contamination worry, which
  confounds both appearance and non-appearance of the predicted reports (the web's own
  controlled-experiment proposal is what would isolate it).

### example

- **`introspective-confabulation`** — CQ1 (support): Ericsson & Simon (1980) argue the
  Nisbett–Wilson paradigm elicits causal "why" judgments outside the range of reliable
  report, while reports of currently heeded content are accurate — so the cited instances
  may show absent access to *causes*, not a confabulating faculty. Sub-point: the
  split-brain instance is a surgical pathology (the interpreter effect); generalising from
  the severed to the intact brain is an instance-level over-reach.

### consequences

- **`rights-sign-forgeable`** — see ranked list (CQ3, CQ4).

## 4. Hygiene notes

- Analogy bodies mostly state their respects R explicitly (good — the pattern file requires
  it). `other-minds-reply` gives R ("behaviour") without labelling it; harmless.
- Several arguments answer a CQ *in prose* without any node occupying the attack
  (`china-nation-absent-qualia`'s systems-reply paragraph, `llmary-token-encounter`'s
  phenomenal-realist dilemma, `transplant-intuition`'s Olson reply, `fading-qualia` vs the
  begs-question node wired only to `dancing-qualia`). Where a debate turn takes up the menu
  above, prefer *wiring the existing move as a node/edge* over re-inventing it.
- `zombie-conceivability`'s `unwarrantable-zombie-premise` attack is deliberately outside
  the six CQs (a warrant-level move); the pattern file could gain a CQ-warrant if this
  recurs.
- Lint passes after the nine frontmatter edits (the two "possibly non-atomic claim" warnings
  pre-date this audit). `make embed` was not run; the embedding cache advisory may fire
  until it is.

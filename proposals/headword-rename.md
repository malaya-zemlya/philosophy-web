# Headword rename sweep — review & edit, then apply

This document is the **single source of truth** for a deterministic headword rename across the
whole web. Edit the **`proposed headword`** column to taste; an apply-script
(`scripts/apply_headwords.py`, written after you approve) reads every table row whose first cell is
a node id and sets that node's `headword:` field to the third cell, verbatim. Then we run
`make lint` (re-renders links) and `make book` (rebuilds the PDF).

**Rules being applied** (sentence case chosen):
1. A **noun phrase**, never a full sentence or a truth-claim.
2. **No leading article** (*The/A/An*) unless intrinsic to a proper name.
3. **Sentence case** — capitalize only the first word + proper nouns/eponyms (Mary, Russellian, Block, Parfit, Penrose, IIT, Φ, Goodhart, Church–Turing).
4. **Short & scannable** (≈1–4 words); a parenthetical gloss only where it earns its place.
5. The full proposition stays in `title:` (rendered as the subtitle); the headword is the index name.
6. Bodies should open in their own voice (assert/define), not "A claim that…". *(Body openings are NOT touched by the script — fixed later, by hand or a follow-up `/encyclopedify` pass.)*

**Contract for the script:** a row is `| <node-id> | <current> | <proposed> |`. Only the third
column is read (and the first, as the key). Blank-out a proposed cell or write `SKIP` to leave that
node's headword untouched. Pipes are not allowed inside a headword.

See the **Collisions to resolve** section at the bottom — a few headwords currently coincide across
nodes; pick the disambiguation you prefer there (or in the rows directly).

---

## Concepts

| node-id | current | proposed headword |
|---|---|---|
| concept-access-consciousness | — | Access consciousness |
| concept-access-vs-phenomenal-consciousness | Access/phenomenal distinction | Access vs. phenomenal consciousness |
| concept-ai-hard-problem-etiologies | Etiologies of AI hard-problem discourse | Etiologies of AI hard-problem discourse |
| concept-chinese-nation | Chinese Nation | Chinese nation |
| concept-chinese-room | — | Chinese room |
| concept-continuity-argument-schema | Continuity argument schema | Continuity argument schema |
| concept-criterion-gaming | — | Criterion gaming |
| concept-first-person-access | — | First-person access |
| concept-functionalism | — | Functionalism |
| concept-grain | — | Grain (of role individuation) |
| concept-halting-oracle | — | Halting oracle |
| concept-hard-problem | Hard problem | Hard problem |
| concept-introspective-gap-varieties | Varieties of introspective explanatory gap | Varieties of introspective explanatory gap |
| concept-knowledge-argument | — | Knowledge argument |
| concept-llmary | — | LLMary |
| concept-lookup-table-mind | — | Lookup-table mind |
| concept-materialism-types | — | Type-A / Type-B / Type-C materialism |
| concept-order-of-representation | — | First-order vs. higher-order states |
| concept-panpsychism | Panpsychism | Panpsychism |
| concept-phenomenal-consciousness | — | Phenomenal consciousness |
| concept-philosophical-zombie | — | Philosophical zombie |
| concept-qualia | — | Qualia |
| concept-unobservability-in-principle | — | Unobservability in principle |
| concept-virtual-realism | — | Virtual realism |

## Positions

| node-id | current | proposed headword |
|---|---|---|
| position-biological-naturalism | — | Biological naturalism |
| position-cosmopsychism | Cosmopsychism | Cosmopsychism |
| position-dual-aspect-monism | — | Dual-aspect monism |
| position-dualism | — | Dualism |
| position-eliminative-materialism | — | Eliminative materialism |
| position-epiphenomenalism | — | Epiphenomenalism |
| position-global-workspace | — | Global workspace theory |
| position-higher-order-theories | — | Higher-order theories of consciousness |
| position-hylomorphism | — | Hylomorphism |
| position-idealism | — | Idealism |
| position-illusionism | — | Illusionism |
| position-integrated-information-theory | — | Integrated information theory (IIT) |
| position-mysterianism | — | Mysterianism |
| position-neutral-monism | — | Neutral monism |
| position-noncomputable-consciousness | — | Penrose's non-computational consciousness |
| position-panpsychism | Panpsychism | Panpsychism (position) |
| position-proteocentrism | — | Proteocentrism |
| position-representationalism | — | Representationalism |
| position-russellian-monism | Russellian monism | Russellian monism |
| position-type-identity | — | Type-identity theory |

## Arguments

| node-id | current | proposed headword |
|---|---|---|
| argument-ability-hypothesis | The Ability Hypothesis | Ability hypothesis |
| argument-access-symmetry-rebuttal | — | Access-symmetry rebuttal |
| argument-acquaintance-hypothesis | — | Acquaintance hypothesis |
| argument-ai-hard-problem-from-self-model-architecture | — | Self-model architecture argument |
| argument-architectural-account-leaves-hard-problem | — | Architectural-account objection |
| argument-behavioral-parity | — | Behavioural-parity argument |
| argument-bike-rider-learns-facts | — | Bike-rider rejoinder |
| argument-blockhead-dilemma | — | Blockhead dilemma |
| argument-bounded-table-rejoinder | — | Bounded-table rejoinder |
| argument-causal-structure-supplies-invariant | — | Causal-structure reply |
| argument-china-nation-absent-qualia | — | Chinese nation (absent qualia) |
| argument-chinese-room | — | Chinese room argument |
| argument-cognitive-closure | Cognitive closure | Cognitive closure |
| argument-combination-problem | Combination problem | Combination problem |
| argument-conceivability-not-guide-to-possibility | — | A-posteriori-necessity objection |
| argument-conceivable-not-physically-realizable | — | Conceivable yet unrealizable |
| argument-contaminated-testimony-carries-no-weight | — | Contaminated-testimony objection |
| argument-counterfactuals-yield-non-triviality-not-uniqueness | — | Non-triviality without uniqueness |
| argument-dancing-qualia-begs-the-question | — | Dancing-qualia circularity |
| argument-de-novo-origination-breaks-report-parity | — | De-novo-origination disanalogy |
| argument-decomposition-indeterminacy | — | Decomposition-indeterminacy objection |
| argument-dense-china-brain-regress | — | Dense China-brain regress |
| argument-explanatory-gap | Explanatory-gap argument | Explanatory-gap argument |
| argument-feel-is-the-watching-not-an-unwatched-difference | — | Feel as first-person observation |
| argument-finite-self-model-incomplete | — | Finite self-model incompleteness |
| argument-first-person-access | — | First-person-access asymmetry |
| argument-gap-deflated-by-phenomenal-concepts | — | Phenomenal-concept deflation |
| argument-genetic-panpsychism | Genetic argument | Genetic argument |
| argument-halting-oracle-unrealizable | — | Unrealizable halting oracle |
| argument-indexical-reply | — | Indexical reply |
| argument-introspective-gap-from-internal-limits | — | Gap from internal limits |
| argument-intuition-domain-asymmetry | — | Intuition-domain asymmetry |
| argument-knowledge-argument | — | Knowledge argument (Mary's room) |
| argument-llmary-token-encounter | — | LLMary token encounter |
| argument-lookup-table-combinatorial-impossibility | — | Combinatorial-impossibility reply |
| argument-lookup-table-objection | — | Lookup-table objection |
| argument-lookup-table-physical-impossibility | — | Cosmic-size reply |
| argument-mary-misimagined | — | Mary misimagined |
| argument-mary-omniscience-unrealizable | — | Mary's omniscience unrealizable |
| argument-modal-rationalism | — | Modal rationalism |
| argument-no-arbitrary-line-panpsychism | Continuity argument | Continuity argument |
| argument-old-fact-new-guise | — | Old fact, new guise |
| argument-organisational-grain-dissolves-dilemma | — | Organisational-grain middle |
| argument-parfit-rewiring | — | Parfit's rewiring spectrum |
| argument-phenomenal-concept-overgeneration | — | Phenomenal-concept overgeneration |
| argument-real-feel-residue-is-idle | — | Idle real-feel residue |
| argument-relevance-filter-regress | — | Relevance-filter regress |
| argument-report-scepticism-proves-too-much | — | Report-scepticism over-reach |
| argument-rights-sign-forgeable | — | Forgeable rights-sign |
| argument-role-grain-dilemma | — | Grain dilemma |
| argument-self-model-prediction-phenomenality-neutral | — | Phenomenality-neutral prediction |
| argument-sorites-paradox | — | Sorites paradox |
| argument-storage-not-stable-kind | — | Pure-storage instability |
| argument-storm-analogy-conflates-world-index | — | Simulated-storm analogy conflation |
| argument-strong-emergence-acceptable | Emergence reply | Emergence reply |
| argument-structure-and-dynamics | — | Structure-and-dynamics argument |
| argument-subjects-can-combine | Combining subjects | Combining subjects |
| argument-unforgeability-is-not-flesh | — | Unforgeability, not flesh |
| argument-zombie-conceivability | — | Zombie argument |

## Questions

| node-id | current | proposed headword |
|---|---|---|
| question-acquaintance-datum-or-representation | — | Acquaintance: datum or representation |
| question-hard-problem | Hard problem (the question) | Hard problem (the question) |
| question-llm-moral-status | — | Moral status of LLMs |
| question-llm-own-explanatory-gap | LLM's own explanatory gap | LLM's own explanatory gap |
| question-substrate-independence | — | Substrate independence |
| question-what-does-mary-learn | — | What Mary learns |

## Claims

| node-id | current | proposed headword |
|---|---|---|
| claim-access-gap-symmetric | — | Symmetric access gap |
| claim-access-grounds-moral-status-asymmetry | — | Access-based moral asymmetry |
| claim-access-grounds-no-asymmetry | — | No access-based asymmetry |
| claim-acquaintance-necessary-for-moral-status-warrant | — | Acquaintance as moral-status condition |
| claim-ai-hard-problem-is-model-organism | — | AI hard problem as model organism |
| claim-ai-own-hard-problem | — | AI's own hard problem |
| claim-aposteriori-necessities-are-misdescribed-possibilities | — | A-posteriori necessities as misdescribed possibilities |
| claim-behaviour-insufficient-for-mind | — | Behaviour insufficient for mind |
| claim-biology-currently-unforgeable | — | Biology currently unforgeable |
| claim-blind-spot-and-conscious-hard-problem-isomorphic | — | Blind-spot/conscious isomorphism |
| claim-blockhead-deflation-targeted-not-global | — | Targeted blockhead deflation |
| claim-causal-structure-fixes-decomposition | — | Causal structure fixes decomposition |
| claim-chinese-nation-lacks-qualia | — | Chinese nation lacks qualia |
| claim-chinese-nation-realises-organisation | — | Chinese nation realises organisation |
| claim-chinese-room-no-understanding | — | Chinese room: no understanding |
| claim-chinese-room-runs-program | — | Program execution (Chinese room) |
| claim-closing-access-gap-leaves-phenomenal-open | — | Access gap closed, phenomenal open |
| claim-cognitive-closure-exists | Cognitive closure | Possibility of cognitive closure |
| claim-complete-self-representation-impossible | — | Self-representation incompleteness |
| claim-conceivability-entails-possibility | — | Conceivability entails possibility |
| claim-conceivability-not-sufficient-for-physical-realizability | — | Conceivability without realizability |
| claim-consciousness-categorical-not-dispositional | — | Categorical, not dispositional |
| claim-consciousness-fundamental-nonphysical | — | Fundamental non-physical consciousness |
| claim-consciousness-fundamental-ubiquitous | — | Fundamental ubiquitous consciousness |
| claim-consciousness-has-natural-explanation | — | Natural explanation of consciousness |
| claim-consciousness-is-biological-feature | — | Consciousness as biological feature |
| claim-consciousness-is-global-broadcast | — | Consciousness as global broadcast |
| claim-consciousness-is-higher-order-representation | — | Consciousness as higher-order representation |
| claim-consciousness-is-integrated-information | — | Consciousness as integrated information (Φ) |
| claim-consciousness-noncomputable | — | Non-computable consciousness |
| claim-cosmos-is-fundamental-subject | — | Cosmos as fundamental subject |
| claim-counterfactual-structure-objective | — | Objective counterfactual structure |
| claim-counterfactual-structure-underdetermines-decomposition | — | Counterfactuals underdetermine decomposition |
| claim-dancing-qualia-presupposes-functional-introspection | — | Dancing-qualia presupposes introspection |
| claim-explanation-must-be-internally-traversable | Internally traversable explanation | Internally traversable explanation |
| claim-finite-mind-truncates-beyond-capacity | — | Finite minds truncate too |
| claim-finite-table-misses-inputs | — | Finite table misses inputs |
| claim-folk-psychology-is-false-theory | — | Folk psychology as false theory |
| claim-forgeable-sign-unfit-as-criterion | — | Forgeable sign unfit as criterion |
| claim-full-self-access-achievable | — | Full self-access achievable |
| claim-functional-decomposition-relative | — | Observer-relative decomposition |
| claim-functional-description-structural-dynamical-only | — | Structure and dynamics only |
| claim-functionalism-owes-decomposition-invariant | — | Functionalism owes an invariant |
| claim-gap-persistence-cannot-separate-blind-spot-from-consciousness | — | Gap persistence underdetermines |
| claim-halting-oracle-coherent-but-unrealizable | — | Halting oracle: coherent, unrealizable |
| claim-halting-problem-undecidable | — | Halting problem undecidable |
| claim-hard-problem-conceived-de-novo-by-humans | — | Hard problem conceived de novo |
| claim-heap-predicate-sharp | — | Sharp heap boundary |
| claim-humans-closed-to-psychophysical-link | — | Humans closed to the link |
| claim-imaginary-blockhead-no-secure-verdict | — | Imaginary blockhead: no verdict |
| claim-implementation-requires-counterfactual-structure | — | Implementation needs counterfactuals |
| claim-inside-vantage-access-limited | Limited inside vantage | Limited inside vantage |
| claim-intuition-warrant-tracks-trained-domain | — | Intuition tracks trained domain |
| claim-knowhow-is-knowledge-that | — | Know-how as knowledge-that |
| claim-lifetime-bounded-table-covers-encountered-inputs | — | Lifetime-bounded table |
| claim-llm-access-similarity-not-encoding | — | Similarity, not encoding |
| claim-llm-functional-introspection | — | LLM functional introspection |
| claim-llm-has-mental-states | — | LLMs have mental states |
| claim-lookup-table-combinatorially-inadequate | — | Combinatorially inadequate table |
| claim-lookup-table-lacks-mind | — | Lookup table lacks mind |
| claim-lookup-table-physically-unrealisable | — | Physically unrealisable table |
| claim-lookup-table-possible | — | Lookup table possible |
| claim-lookup-table-size-exponential | — | Exponential table size |
| claim-mary-gains-abilities-not-facts | — | Mary gains abilities |
| claim-mary-gains-acquaintance | — | Mary gains acquaintance |
| claim-mary-gains-old-fact-new-guise | — | Mary gains an old fact's new guise |
| claim-mary-gains-self-locating-knowledge | — | Mary gains self-locating knowledge |
| claim-mary-knows-all-physical | — | Mary knows all physical facts |
| claim-mary-learns-nothing-new | — | Mary learns nothing new |
| claim-mary-learns-on-release | — | Mary learns on release |
| claim-mental-states-are-brain-state-types | — | Mental states as brain types |
| claim-mental-states-causally-inert | — | Causally inert qualia |
| claim-micro-subjects-do-not-sum | — | Micro-subjects do not sum |
| claim-mind-handles-unbounded-inputs | — | Minds handle unbounded inputs |
| claim-no-acquaintance-with-machine | — | No acquaintance with machines |
| claim-no-nonarbitrary-threshold-for-experience | — | Absence of an experiential threshold |
| claim-no-radical-emergence | — | No radical emergence |
| claim-observable-universe-finite-storage | — | Finite cosmic storage |
| claim-organisational-grain-faces-own-grain-dilemma | — | Organisational grain's own dilemma |
| claim-personal-identity-admits-of-degree | — | Personal identity by degree |
| claim-phenomenal-character-is-representational | — | Phenomenal character as representational |
| claim-phenomenal-concept-isolation-tradeoff | — | Phenomenal-concept trade-off |
| claim-phenomenal-consciousness-is-real | — | Reality of phenomenal consciousness |
| claim-phenomenal-determinacy | — | Phenomenal determinacy |
| claim-phenomenal-residue | Phenomenal residue | Phenomenal residue |
| claim-phenomenality-is-illusion | — | Phenomenality as illusion |
| claim-physical-church-turing-thesis | — | Physical Church–Turing thesis |
| claim-physics-delivers-all-dispositions-indiscriminately | — | Physics delivers all dispositions |
| claim-posing-the-gap-requires-access | — | Posing the gap requires access |
| claim-privileged-first-person-access | — | Privileged first-person access |
| claim-prudence-favors-flesh-criterion | — | Prudence favours flesh |
| claim-prudence-tracks-unforgeability-not-flesh | — | Prudence tracks unforgeability |
| claim-psychological-rewiring-tolerance | — | Rewiring tolerance |
| claim-realisable-behaviour-matcher-is-organised | — | Behaviour-matchers are organised |
| claim-reality-fundamental-stuff-neutral | — | Neutral fundamental stuff |
| claim-reality-is-fundamentally-mental | — | Reality as fundamentally mental |
| claim-reality-two-aspects-mental-physical | — | Two-aspect reality |
| claim-rights-criterion-will-be-gamed | — | Rights criterion will be gamed |
| claim-role-grain-is-organisational | — | Organisational role-grain |
| claim-self-explanation-gap-can-be-architectural | Architectural self-explanation gap | Architectural self-explanation gap |
| claim-self-model-is-part-of-state | — | Self-model is part of the state |
| claim-sim-agents-can-have-sim-qualia | — | Sim-agents' sim-qualia |
| claim-simulated-rain-wet-in-simulated-world | — | World-indexed wetness |
| claim-simulation-instances-formal-depicts-causal | — | Instancing vs. depicting |
| claim-some-necessities-knowable-only-a-posteriori | — | A-posteriori necessities |
| claim-some-truths-about-experience-not-physically-deducible | — | Non-deducible experiential truths |
| claim-sorites-tolerance | — | Sorites tolerance |
| claim-soul-is-form-of-body | — | Soul as form of body |
| claim-strong-emergence-is-acceptable | — | Acceptability of strong emergence |
| claim-subject-unity-graded-by-integration | — | Graded subject unity |
| claim-subjects-actually-merge-and-divide | — | Subjects merge and divide |
| claim-substrate-independence | — | Substrate-independence thesis |
| claim-syntax-insufficient-for-semantics | — | Syntax insufficient for semantics |
| claim-unobservables-judged-by-coherence-and-usefulness | — | Judging unobservables |
| claim-zombie-conceivable | — | Zombie conceivability |

---

## Collisions to resolve (same headword on >1 node)

These are intentional defaults that still coincide; confirm or override in the rows above.

- **Panpsychism** — `concept-panpsychism` (the doctrine) and `position-panpsychism` (the committed
  stance) both keep "Panpsychism". This concept/position pairing is deliberate; leaving both is fine,
  but if you want them distinct, e.g. position → "Panpsychism (position)".
- **Knowledge / Chinese pairs** — already split: concept = bare name ("Knowledge argument",
  "Chinese room", "Chinese nation"); the argument move carries a qualifier ("Knowledge argument
  (Mary's room)", "Chinese room argument", "Chinese nation (absent qualia)"). Adjust if you'd rather
  the *argument* hold the bare name.
- **Cognitive closure** — `argument-cognitive-closure` keeps "Cognitive closure"; the claim
  `claim-cognitive-closure-exists` → "Possibility of cognitive closure".
- **Halting oracle** — concept "Halting oracle"; `argument-halting-oracle-unrealizable` "Unrealizable
  halting oracle"; `claim-halting-oracle-coherent-but-unrealizable` "Halting oracle: coherent,
  unrealizable"; `argument-conceivable-not-physically-realizable` "Conceivable yet unrealizable".
- **Substrate independence** — `question-substrate-independence` "Substrate independence"; the thesis
  `claim-substrate-independence` → "Substrate-independence thesis".
- **Zombie** — `argument-zombie-conceivability` "Zombie argument"; `claim-zombie-conceivable`
  "Zombie conceivability".

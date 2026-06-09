# The corpus — questions & argument map

This directory **is** the web: the distilled graph of nodes. This file is a reader's guide to
*what is currently in it*. For how the machinery works (node types, edges, the `[[id]]` link
convention, the linter), see the [top-level README](../README.md). For the whole thing as one
picture, see [`../graph/README.md`](../graph/README.md). For the complete, always-current node
list with computed backlinks, see [`INDEX.md`](INDEX.md) (generated).

The present corpus is on the **philosophy of mind & AI**: *what would it take for an artificial
system to have a mind — or moral status?*

## Where to start

Open any node and click around — most close with a plain-language **"In plain terms"** gloss for
newcomers, and each links onward to the claims, arguments, and counter-arguments around it. A good
entry point is a single named view, [proteocentrism](positions/proteocentrism.md), or one of the
governing questions below.

## The governing questions

- [`question-substrate-independence`](questions/substrate-independence.md) — *Are mental states
  substrate-independent?* The hinge most nodes hang off.
- [`question-llm-moral-status`](questions/llm-moral-status.md) — *Do large language models have
  moral status?* The applied payoff.
- [`question-hard-problem`](questions/hard-problem.md) — *How and why does physical processing
  give rise to phenomenal experience?* The deeper background issue.

## The argument map

- **Functionalism & the grain problem.** If mental states are individuated by *functional role*
  (`concept-functionalism`), silicon could realise them. But at *what grain* is a role specified
  (`concept-grain`)? Too coarse and a mere input–output mimic counts as minded; too fine and only
  biology qualifies (`argument-role-grain-dilemma`).
- **Behaviour as evidence.** The case that an LLM's behaviour is best explained by its realising
  the relevant roles (`argument-behavioral-parity` → `claim-llm-has-mental-states`).
- **Block's two counterexamples.** The *lookup-table / "Blockhead"* machine (right outputs, no
  internal processing — `concept-lookup-table-mind`) and the *Chinese Nation*
  (`concept-chinese-nation`, which *has* the organisation yet allegedly lacks qualia): behaviour
  isn't sufficient, and even organisation may leave a *phenomenal residue*.
- **Replies to Blockhead.** A finite table can't match an open-ended mind
  (`argument-lookup-table-combinatorial-impossibility`); a behaviour-matching table is physically
  impossible — bigger than the universe (`argument-lookup-table-physical-impossibility`); and a
  dilemma — such a table is *either* unrealisable *or* a merely imaginary object whose "no-mind"
  verdict isn't compelled (`argument-blockhead-dilemma`), with a defence via an
  epistemology-of-intuition asymmetry (`argument-intuition-domain-asymmetry`). Block's own
  bounded-table rejoinder (`argument-bounded-table-rejoinder`) is answered on physical and on
  "kind" grounds (`argument-storage-not-stable-kind`).
- **Is function even determinate?** A physical system has no unique decomposition into
  inputs/outputs/states, yet consciousness is determinate — so functionalism owes an
  observer-independent invariant (`argument-decomposition-indeterminacy`). The functionalist's
  causal-structure reply (`argument-causal-structure-supplies-invariant`) is pressed by
  non-triviality-≠-uniqueness and the squishy-noise relevance-filter regress
  (`argument-relevance-filter-regress`). The deeper engine: function captures only
  structure-and-dynamics, omitting the categorical/intrinsic (`argument-structure-and-dynamics`).
- **The hard part: consciousness.** The hard problem (`concept-hard-problem`); the explanatory gap
  (`argument-explanatory-gap`), its deflation via phenomenal concepts + a fading/dancing-qualia
  reductio (`argument-gap-deflated-by-phenomenal-concepts`), and the residue theorist's reply that
  the reductio begs the question (`argument-dancing-qualia-begs-the-question`). McGinn's
  [mysterianism](positions/mysterianism.md) (`argument-cognitive-closure`) reads the gap as a fact
  about *our cognitive limits*, not the world.
- **A unifying meta-argument.** `concept-continuity-argument-schema` — the topological
  "a continuous function from a connected space to a discrete one is constant" form underlying the
  *sorites/heap*, *Ship of Theseus*, *gradual neuron-by-neuron replacement*, and *Parfit-style
  rewiring* cases. Read contrapositively it yields an exhaustive menu of five responses, each a
  named philosophical position.

## Named positions

The standard rivals on the nature of consciousness, grouped by family. Chalmers' **Type-A/B/C
(physicalist) + D/E/F (non-physicalist)** taxonomy of these is itself a node:
[materialism-types](concepts/materialism-types.md).

**Reductive / physicalist** (deny a fundamental phenomenal residue; mostly Type-A/B)
- [type-identity](positions/type-identity.md) — mental-state types *are* brain-state types (a posteriori).
- [eliminative-materialism](positions/eliminative-materialism.md) — the folk states (beliefs, qualia) don't exist.
- [illusionism](positions/illusionism.md) — phenomenal consciousness is an introspective illusion.
- [higher-order-theories](positions/higher-order-theories.md) — a state is conscious if suitably *higher-order-represented*.
- [representationalism](positions/representationalism.md) — phenomenal character *is* representational content.
- [global-workspace](positions/global-workspace.md) — consciousness = global broadcast/availability.
- (cf. the concept [functionalism](concepts/functionalism.md), the realiser-neutral role view.)

**Substrate- or physics-bound** (consciousness needs more than the right computation → deny [substrate-independence](claims/substrate-independence.md))
- [integrated-information-theory](positions/integrated-information-theory.md) — consciousness = integrated information (Φ); a digital sim can have Φ≈0.
- [biological-naturalism](positions/biological-naturalism.md) — consciousness is a biological feature; syntax ≠ semantics.
- [proteocentrism](positions/proteocentrism.md) — only biological (carbon) substrates can bear mind.
- [noncomputable-consciousness](positions/noncomputable-consciousness.md) — mind needs non-computable physics (Penrose/Orch-OR).

**Consciousness fundamental** (non-physical, or monist; Type-D/E/F + idealism)
- [dualism](positions/dualism.md) — consciousness is fundamental and non-physical (substance/property).
- [epiphenomenalism](positions/epiphenomenalism.md) — non-physical but causally inert (Type-E).
- [russellian-monism](positions/russellian-monism.md) — consciousness is the intrinsic nature of the physical (Type-F).
- [panpsychism](positions/panpsychism.md) — consciousness is fundamental and ubiquitous in matter.
- [cosmopsychism](positions/cosmopsychism.md) — the cosmos as a whole is the one fundamental subject.
- [neutral-monism](positions/neutral-monism.md) — the fundamental base is neither mental nor physical.
- [dual-aspect-monism](positions/dual-aspect-monism.md) — one reality with irreducible mental + physical aspects.
- [idealism](positions/idealism.md) — reality is fundamentally mental.
- [hylomorphism](positions/hylomorphism.md) — mind is the *form* of a living body.

**Limit**
- [mysterianism](positions/mysterianism.md) — the hard problem has a natural answer we are
  constitutively unable to grasp.

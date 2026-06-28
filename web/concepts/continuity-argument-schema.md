---
id: concept-continuity-argument-schema
type: concept
title: Continuity–connectedness argument schema (no-sharp-line / sorites form)
headword: Continuity argument schema
author: mishka
status: asserted
tags: [method, vagueness, sorites, personal-identity, philosophy-of-mind]
uses_concept: []
presupposes: []
style: encyclopedia
created: 2026-06-04
---

The *continuity–connectedness argument schema* is a general template — an argument form, not a
first-order claim — behind a whole family of "you cannot draw a sharp line, so the distinction breaks
down" arguments. It takes any "no single small step makes the difference" intuition and converts it
into an *exhaustive* menu of escape routes: a fixed list of exactly five positions, one of which any
such puzzle must adopt.

### The underlying fact

The schema exploits a simple topological theorem: *a continuous function from a connected space into
a discrete space is constant.* Model a predicate or verdict as a function $f : X \to Y$, where $X$ is
a space of cases joined by *admissible small steps* — remove one grain, swap one plank, replace one
neuron, alter one psychological connection — and $Y$ is the space of verdicts (heap / non-heap; same
ship / different ship; conscious / not; me / not-me). Read the theorem's contrapositive: if $f$ takes
at least two values, then at least one of the conditions below must fail. Each failure is a named
philosophical position. The schema is *neutral* — it does not pick a horn; it proves the horns
jointly exhaust the options.

### The five horns

- **$f$ is discontinuous** — there is a sharp threshold, a single step that flips the verdict; the
  cutoff exists even if it is unknowable. This is *epistemicism* about the predicate.
- **$Y$ is not discrete** — the verdicts form a continuum, and the predicate comes in *degrees*. This
  is *degree theory*, fuzzy logic, and other many-valued approaches.
- **$f$ is not well-defined** — at some cases there is no fact of the matter which value obtains. This
  is *indeterminacy* or *supervaluationism* (truth-value gaps).
- **$X$ is disconnected** — there is no path of genuinely admissible small steps from one endpoint to
  the other; some step is not in fact negligible. This *denies the inductive (tolerance) premise* —
  some single step really does carry the difference.
- **$f$ is constant** — the two endpoint "values" are in fact the same, and the apparent difference is
  illusory. This is *deflation* or *eliminativism* about the distinction.

### Instances

The schema's generality is that the same five-way fork recurs with different $X$ and $Y$:

- *Sorites / the heap.* $X$ = grain-counts under one-grain removal, $Y$ = {heap, non-heap}. The
  paradigm; here the five horns are exactly the standard taxonomy of responses to vagueness. See the
  [sorites paradox](../arguments/sorites-paradox.md).
- *Ship of Theseus.* $X$ = plank-replacement sequences, $Y$ = {same ship, distinct ship}.
- *Gradual neural prosthesis.* Neuron-by-neuron silicon replacement — Chalmers' fading- and
  dancing-qualia thought experiments ([chalmers-1995b](../sources/chalmers-1995b.md)): $X$ = a part-replacement series
  from all-carbon to all-silicon, $Y$ = {conscious / same qualia, not}. This is the schema's bridge
  into the consciousness debate.
- *Parfit-style rewiring.* Gradually re-wiring one psychology into another person's: $X$ = paths
  through psychological configuration-space, $Y$ = {me, not-me}. The standard move here takes the
  degree horn — see [Parfit's rewiring spectrum](../arguments/parfit-rewiring.md).

### The topology models a premise

A caveat keeps the schema honest. On a *literally* discrete domain — integer grain-counts — every
function is trivially continuous, so "$f$ is discontinuous" is always vacuously available and the
theorem has no bite. The real force comes from the *tolerance premise* itself — "no single admissible
step changes the verdict" — which is a uniform-continuity, no-large-jumps constraint, together with
the connectedness of $X$ under the small-step adjacency. So the schema's actual content is that
*tolerance, a connected domain, and a genuinely discrete verdict-space are jointly inconsistent.*
Whatever gives is one of the five horns. Naming the domain's topology and the metric of "small step"
is where the substantive philosophical work lives.

### The dispute it feeds

In this web the gradual-replacement instance is the engine of [substrate
independence](../claims/substrate-independence.md). The fading- and dancing-qualia reductio argues for the *$f$-constant* horn: if no
admissible one-neuron step could flip or fade qualia — on pain of an absurd "dancing" or "fading"
experience the subject cannot notice — then qualia are preserved across the whole carbon-to-silicon
path, and consciousness is substrate-independent. Resistance to that reductio is resistance over
*which horn* the case takes. A [phenomenal-residue](../claims/phenomenal-states-not-exhausted-by-role.md) theorist may instead
seize the *discontinuity* horn (some replacement does flip qualia) or the *disconnection* horn (the
carbon-to-silicon series is not a path of genuinely admissible steps, because biology is
load-bearing); [the begs-the-question objection](../arguments/dancing-qualia-begs-the-question.md) disputes
whether the reductio has really closed off those horns or merely assumed them shut. The grain debate
([grain](grain.md), [the role–grain dilemma](../arguments/role-grain-dilemma.md)) is the same
structure one level down: the "admissible small step" is fixed only once the grain of
role-individuation is fixed.

This node does not assert epistemicism, degree theory, or any other first-order position on
vagueness. It is the *frame* showing those are the only options for any sorites-shaped puzzle. An
argument that instantiates it links here via `uses_concept` and states, in its own body, which horn
it grabs and why the case is an instance.

### In plain terms

Lots of arguments share one shape: "you can't draw a sharp line, so the distinction must break
down." Take a heap of sand — remove one grain and it's still a heap; repeat, and is there ever a
single grain that turns it into a non-heap? The same shape shows up for the Ship of Theseus (swap its
planks one at a time), for replacing your neurons one by one with computer chips, for slowly rewiring
your personality into someone else's. This node is the master template behind all of them. Its useful
trick: whenever you have a chain of tiny steps leading from one verdict to its opposite, it proves
there are exactly **five** ways out, and no others:

1. There's a hidden sharp line somewhere — one step really does flip it — even if we can never find it.
2. The verdict isn't a flat yes/no but a matter of *degree*.
3. Somewhere in the middle there's simply no fact of the matter.
4. One of the "tiny" steps wasn't actually tiny — it carried the whole difference.
5. The two ends were never really different to begin with.

The template stays neutral — it doesn't tell you which door to take, it just guarantees those are the
only doors. The real philosophical work is arguing over which one a given case forces you through.

### See also

- [sorites-paradox](../arguments/sorites-paradox.md) — the paradigm instance; the heap, run forward.
- [parfit-rewiring](../arguments/parfit-rewiring.md) — the personal-identity instance, taking the degree horn.
- [substrate-independence](../claims/substrate-independence.md) — the consciousness conclusion the gradual-replacement instance is
  marshalled to drive.
- [phenomenal-residue](../claims/phenomenal-states-not-exhausted-by-role.md) — the residue a discontinuity- or disconnection-horn theorist invokes
  to resist the silicon path.
- [dancing-qualia-begs-the-question](../arguments/dancing-qualia-begs-the-question.md) — disputes whether the reductio really closes off the
  rival horns.
- [grain](grain.md) — fixes what counts as an "admissible small step."
- [role-grain-dilemma](../arguments/role-grain-dilemma.md) — the same five-way structure one level down.

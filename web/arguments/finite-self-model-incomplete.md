---
id: argument-finite-self-model-incomplete
type: argument
title: A finite system cannot completely represent its own current state (a capacity bound)
author: mishka
status: asserted
tags: [philosophy-of-mind, ai, computation]
premise: [claim-self-model-is-part-of-state]
concludes: claim-complete-self-representation-impossible
supports: [claim-inside-vantage-access-limited, claim-self-explanation-gap-can-be-architectural]
attacks: [claim-full-self-access-achievable]
uses_concept: [concept-introspective-gap-varieties, concept-access-vs-phenomenal-consciousness]
created: 2026-06-05
---

inference form: deductive — a pigeonhole/capacity bound, with a regress corollary.

Setup. Model the instantaneous state as an element of a finite set Σ (equivalently, N activations over
a finite alphabet; total capacity C = log₂|Σ| bits). "Complete simultaneous self-access" means the
state factors as s = (R, U) — a self-model part R and the remainder U (perception, control, the
read-out machinery itself) — and the *whole* current state s is recoverable from R alone (lossless ⇒
the map s ↦ R(s) is injective on Σ).

1. ([self-model-is-part-of-state](../claims/self-model-is-part-of-state.md)) R is part of the state: Σ = ℛ × 𝒰, so |Σ| = |ℛ|·|𝒰|.
   (No state-external register — this is the internal case. Drop it and you have an *external*
   observer, who can have full access.)
2. Lossless recovery of s from R requires s ↦ R injective, hence |ℛ| ≥ |Σ| = |ℛ|·|𝒰|.
3. Therefore |𝒰| ≤ 1: the remainder is constant — zero spare capacity. The system is *nothing but*
   its self-model, with nothing left to perceive, act, or run the read-out.
∴ ([complete-self-representation-impossible](../claims/complete-self-representation-impossible.md)) No finite system can hold a lossless model of
   its entire current state and have any capacity left to use it; any usable self-model is necessarily
   lossy/partial. This is [inside-vantage-access-limited](../claims/inside-vantage-access-limited.md) as a *structural necessity*, and it
   underwrites the architectural reading [self-explanation-gap-can-be-architectural](../claims/self-explanation-gap-can-be-architectural.md); it
   refutes [full-self-access-achievable](../claims/full-self-access-achievable.md).

regress form (the dynamical version of the same bound): if *forming* R adds to the state, completeness
must cover the post-formation state — including R; representing that addition needs R′, then R″, … In
finite state the series must terminate, i.e. some level adds no information: the self-model is
incomplete. (The homunculus regress / Royce's map-within-the-map, made quantitative.)

weakest premise: (1) plus the three modal words *simultaneous, internal, lossless* — each names an
escape, none of which restores complete internal self-access:
- *External* vantage denies (1): an outside instrument is not part of Σ, so it can have full access —
  the internal/external asymmetry of [inside-vantage-access-limited](../claims/inside-vantage-access-limited.md).
- *Sequential* read-out drops "simultaneous": a system can report its state piecemeal or onto an
  external tape — but each snapshot is stale once the next step runs, so it is never complete-at-an-instant.
- *Lossy/compressed* self-models drop "lossless": fine and ubiquitous — the bound forbids only
  completeness, leaving functional introspection ([llm-functional-introspection](../claims/llm-functional-introspection.md)) intact.
- *Quine / Kleene recursion theorem*: a program can output its own *source* — but source is a
  compressed static description, not a lossless image of the runtime state (program counter, stack,
  variables, plus the copy itself), and it is emitted sequentially to an external medium.

physical pedigree (and a strengthening): [breuer-1995](../sources/breuer-1995.md) proves a sharper form of this bound
for physical measurement — *no observer can distinguish all present states of a system in which it is
properly contained*, for classical and quantum theories alike, deterministic or stochastic. It adds
two things. (i) It concerns *measurement* (over time), so the indistinguishable state-pairs persist
even with a perfect apparatus and unlimited time — partly closing the *sequential* escape above (the
limit is structural, not an instantaneous accident). (ii) Its internal/external asymmetry is explicit
— an apparatus *outside* the observed system generally *can* distinguish all states — which is exactly
[inside-vantage-access-limited](../claims/inside-vantage-access-limited.md). Two cautions: Breuer stresses the result only *resembles*
Gödel's theorem (it shares the use of self-reference and nothing more), so the Gödelian framing of
[explanation-must-be-internally-traversable](../claims/explanation-must-be-internally-traversable.md) is a separate analogy; and for a deterministic
discrete LLM the operative content is his general/classical argument, not the quantum EPR corollary.

Distinct from [inside-vantage-access-limited](../claims/inside-vantage-access-limited.md) (which it supports): that *observes* the internal
vantage is poorer; this *proves* the poverty is structural and unremovable for any finite system.
Distinct from [cognitive-closure-exists](../claims/cognitive-closure-exists.md) (McGinn, about forming *concepts*): this is a capacity
bound on *representing one's own state*, independent of concept-possession.

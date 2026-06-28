---
id: argument-finite-self-model-incomplete
type: argument
title: A finite system cannot completely represent its own current state (a capacity bound)
headword: Finite self-model incompleteness
author: mishka
status: asserted
tags: [philosophy-of-mind, ai, computation]
premise: [claim-self-model-is-part-of-state]
concludes: claim-complete-self-representation-impossible
supports: [claim-inside-vantage-access-limited, claim-self-explanation-gap-can-be-architectural]
attacks: [claim-full-self-access-achievable]
uses_concept: [concept-introspective-gap-varieties, concept-access-vs-phenomenal-consciousness]
style: encyclopedia
created: 2026-06-05
---

No finite system can hold a complete, exact picture of its own current state inside that very state
and still have room left to do anything with it. The point is a counting argument — a pigeonhole
bound — with a regress as its dynamical echo, and it is the formal backbone of the claim that any
usable self-model is necessarily partial ([complete-self-representation-impossible](../claims/complete-self-representation-impossible.md)).

### Setup

Model the instantaneous state as an element of a finite set $\Sigma$ (equivalently, $N$ activations
over a finite alphabet, total capacity $C = \log_2|\Sigma|$ bits). "Complete simultaneous self-access"
means the state factors as $s = (R, U)$ — a self-model part $R$ and a remainder $U$ (perception,
control, the read-out machinery itself) — and the *whole* current state $s$ is recoverable from $R$
alone. Losslessness means the map $s \mapsto R(s)$ is injective on $\Sigma$.

### The bound (deductive)

1. The self-model is part of the state ([self-model-is-part-of-state](../claims/self-model-is-part-of-state.md)):
   $\Sigma = \mathcal{R}\times\mathcal{U}$, so $|\Sigma| = |\mathcal{R}|\cdot|\mathcal{U}|$. There is
   no state-external register — this is the internal case; drop it and you have an *external*
   observer, who can have full access.
2. Lossless recovery of $s$ from $R$ requires $s \mapsto R$ injective, hence
   $|\mathcal{R}| \ge |\Sigma| = |\mathcal{R}|\cdot|\mathcal{U}|$.
3. Therefore $|\mathcal{U}| \le 1$: the remainder is constant — zero spare capacity. The system would
   be *nothing but* its self-model, with nothing left to perceive, act, or run the read-out.

So no finite system can hold a lossless model of its entire current state and have any capacity left
to use it; any usable self-model is necessarily lossy or partial
([complete-self-representation-impossible](../claims/complete-self-representation-impossible.md)). This is [the
limited inside vantage](../claims/inside-vantage-access-limited.md) turned into a structural necessity; it underwrites the architectural reading
of the explanatory gap ([self-explanation-gap-can-be-architectural](../claims/self-explanation-gap-can-be-architectural.md)) and refutes the optimist's
[full-self-access thesis](../claims/full-self-access-achievable.md).

### Regress form

The dynamical version of the same bound: if *forming* $R$ adds to the state, completeness must cover
the post-formation state — including $R$ itself; representing that addition needs $R'$, then $R''$, and
so on. In a finite state the series must terminate, meaning some level adds no information: the
self-model is incomplete. This is the homunculus regress — Royce's map-within-the-map
([royce-1899](../sources/royce-1899.md)) — made quantitative.

### Weakest premise and the escapes

Premise (1), together with the three modal words *simultaneous, internal, lossless*, marks the
escapes — none of which restores complete internal self-access.

- *External* vantage denies (1): an outside instrument is not part of $\Sigma$, so it can have full
  access — the internal/external asymmetry of [inside-vantage-access-limited](../claims/inside-vantage-access-limited.md).
- *Sequential* read-out drops "simultaneous": a system can report its state piecemeal or onto an
  external tape, but each snapshot is stale once the next step runs, so it is never
  complete-at-an-instant.
- *Lossy or compressed* self-models drop "lossless": fine and ubiquitous — the bound forbids only
  completeness, leaving functional introspection ([llm-functional-introspection](../claims/llm-functional-introspection.md)) intact.
- *Quine / Kleene recursion theorem*: a program can output its own *source*, but source is a
  compressed static description, not a lossless image of the runtime state (program counter, stack,
  variables, plus the copy itself), and it is emitted sequentially to an external medium.

### Physical pedigree

A sharper, measurement-theoretic form is proved by Breuer ([breuer-1995](../sources/breuer-1995.md)): no observer can
distinguish all present states of a system in which it is properly contained, for classical and
quantum theories alike, deterministic or stochastic. It adds two things. First, it concerns
*measurement* over time, so the indistinguishable state-pairs persist even with a perfect apparatus and
unlimited time — partly closing the *sequential* escape, since the limit is structural rather than an
instantaneous accident. Second, its internal/external asymmetry is explicit: an apparatus *outside*
the observed system generally *can* distinguish all states, which is exactly
[inside-vantage-access-limited](../claims/inside-vantage-access-limited.md). Two cautions: Breuer stresses that the result only *resembles*
Gödel's theorem (sharing the use of self-reference and nothing more), so the Gödelian framing of
[explanation-must-be-internally-traversable](../claims/explanation-must-be-internally-traversable.md) is a separate analogy; and for a deterministic
discrete model the operative content is his general/classical argument, not the quantum EPR corollary.

### Distinct from neighbours

Distinct from [inside-vantage-access-limited](../claims/inside-vantage-access-limited.md) (which it supports): that *observes* that the
internal vantage is poorer; this *proves* the poverty is structural and unremovable for any finite
system. Distinct from [cognitive-closure-exists](../claims/cognitive-closure-exists.md) (McGinn's thesis about forming *concepts*,
[mcginn-1989](../sources/mcginn-1989.md)): this is a capacity bound on *representing one's own state*, independent of
concept-possession.

### In plain terms

Imagine trying to keep, inside your head, a perfectly complete and exact snapshot of everything in
your head right now. The snapshot is itself in your head, so it would have to include a snapshot of
itself, which would have to include a snapshot of that, and so on forever — and a finite head runs out
of room. The maths here makes that precise: a part can't losslessly stand in for the whole it belongs
to, so a complete self-portrait would have to use up the entire system, leaving nothing left to think
or act with. The upshot isn't that self-knowledge is impossible — rough, compressed, or step-by-step
self-models are fine — only that *complete, all-at-once* self-knowledge from the inside is ruled out
for any finite machine, brains included. An outside observer with the right instruments faces no such
limit.

### See also

- [self-model-is-part-of-state](../claims/self-model-is-part-of-state.md) — premise (1): the self-model is realised within the state.
- [complete-self-representation-impossible](../claims/complete-self-representation-impossible.md) — the conclusion this argument establishes.
- [inside-vantage-access-limited](../claims/inside-vantage-access-limited.md) — the access poverty this proves structural; supported here.
- [self-explanation-gap-can-be-architectural](../claims/self-explanation-gap-can-be-architectural.md) — the architectural reading this underwrites.
- [full-self-access-achievable](../claims/full-self-access-achievable.md) — the optimist thesis this refutes.
- [cognitive-closure-exists](../claims/cognitive-closure-exists.md) — distinguished: that is about concepts, this about state-representation.
- [introspective-gap-varieties](../concepts/introspective-gap-varieties.md) — the catalogue whose architectural-access member this floors.
- [access-vs-phenomenal-consciousness](../concepts/access-vs-phenomenal-consciousness.md) — this is an access result, silent on phenomenality.

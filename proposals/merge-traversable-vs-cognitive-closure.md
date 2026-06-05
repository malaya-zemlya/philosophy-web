# Merge proposal: explanation-must-be-internally-traversable  vs  cognitive-closure-exists

Status: **RECOMMENDATION — keep separate** (no merge)
Flagged during import; reviewed against the web 2026-06-05.

## Candidate nodes (exact titles)
- `claim-explanation-must-be-internally-traversable` — "An explanation is intuitively satisfying
  for a system only if it is traversable by that system's own cognitive operations"
  (author: mishka)
- `claim-cognitive-closure-exists` — "A type of mind can be constitutively incapable of grasping
  some concepts" (author: mcginn)

## Why they look like the same proposition
Both are "a system cannot reach/grasp something from inside" claims, and both feed the same
taxonomy (`concept-introspective-gap-varieties`) and McGinn-style mysterianism. Surface reading:
"there is something an inside vantage cannot get to."

## The strongest reason they are NOT the same (case AGAINST merging)
- **Different missing thing.** cognitive-closure is about being unable to *form certain concepts /
  grasp certain properties* at all (a rat and arithmetic). internally-traversable is about a system
  that *already possesses* both descriptions (mechanistic and first-person) but lacks an internal
  *route between* them — a missing *derivation*, not a missing concept. The traversable claim's body
  states this distinction explicitly, and the `introspective-gap-varieties` concept files them under
  different senses (conceptual-translation gap vs the closure it is offered as a *mechanism* for).
- **Different modal force.** cognitive-closure is constitutive/permanent ("constitutively
  incapable"). internally-traversable is about *intuitive satisfaction / internal intelligibility*
  for a system given its current observables and abstraction layers — explicitly NOT a claim about
  truth or in-principle external explicability.
- **Different provenance.** cognitive-closure is `author: mcginn` (McGinn 1989, an established
  position). internally-traversable is `author: mishka` (introduced while building this web, using a
  provability-relative-to-a-system analogy). Merging would erase a real attribution boundary —
  exactly the fragmentation-in-reverse the protocol's provenance rule guards against.
- **Different role in the graph.** internally-traversable is offered as a *specified mechanism* that
  could underwrite closure-style appearances without asserting ontological residue
  (`claim-self-explanation-gap-can-be-architectural` cites it alongside
  `claim-inside-vantage-access-limited`). cognitive-closure is the general McGinn category that
  `claim-humans-closed-to-psychophysical-link` specialises. They sit at different levels: general
  closure vs one candidate mechanism for an internal gap.
- Note also the nearby third claim `claim-inside-vantage-access-limited` (missing *data*) — the
  three form a deliberate trichotomy (missing concept / missing data / missing derivation), all with
  authored `Distinct from` notes. Collapsing any pair would damage the taxonomy.

## Suggested canonical id
None — **keep separate.** These are distinct propositions with distinct authors and distinct roles.

## Edges that would need rewiring (only if a human overrides and merges)
If the two were merged (NOT recommended), inbound references to confirm/rewire:
- `claim-self-explanation-gap-can-be-architectural` — references
  `claim-explanation-must-be-internally-traversable` (and `claim-inside-vantage-access-limited`) in
  prose as the mechanism; would need its citations checked.
- `concept-introspective-gap-varieties` — cites `claim-explanation-must-be-internally-traversable`
  (conceptual-translation sense) and `claim-cognitive-closure-exists` (the dispute it feeds) in
  prose; a merge would force rewriting two separate senses into one, which is itself a reason NOT to
  merge.
- `argument-cognitive-closure` and `claim-humans-closed-to-psychophysical-link` hang off
  `claim-cognitive-closure-exists`; none reference the traversable claim.
These are prose `[[id]]` references rather than frontmatter edges — verify against `web/INDEX.md`
backlinks (run `scripts/lint.py`) before any action.

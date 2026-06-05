# Merge proposal: posing-the-gap-requires-access  vs  phenomenal-concept-isolation-tradeoff (+ overgeneration argument)

Status: **RECOMMENDATION — keep separate** (no merge)
Flagged during import; reviewed against the web 2026-06-05.

## Candidate nodes (exact titles)
- `claim-posing-the-gap-requires-access` — "Formulating the hard problem from the first-person
  side requires access to a representation of one's own phenomenal-seeming states"
- `claim-phenomenal-concept-isolation-tradeoff` — "A phenomenal concept cannot be at once
  informative enough to ground self-knowledge while isolated enough to deflate the explanatory gap"
- `argument-phenomenal-concept-overgeneration` — "The phenomenal-concept strategy over-generates —
  it debunks the self-knowledge it presupposes" (an argument node; `premise`/`concludes` =
  `claim-phenomenal-concept-isolation-tradeoff`, `attacks`/`responds_to` =
  `argument-gap-deflated-by-phenomenal-concepts`)

## Why they look like the same proposition
All three live in the same neighbourhood: access / phenomenal-concepts as a precondition for
first-person talk about the phenomenal. Each says, loosely, "to do first-person work on the
phenomenal you need a cognitive grip (access / a concept) on it." Surface vocabulary overlaps
(access, phenomenal concept, first-person, self-knowledge), and all three are `author: mishka`,
created within two days of each other.

## The strongest reason they are NOT the same (case AGAINST merging)
- `posing-the-gap-requires-access` is a **precondition** claim: merely *raising* the hard problem
  is a cognitive act and so requires *access consciousness* of a representation of the phenomenal
  relatum. It is deliberately the *weak* point — it says nothing about whether any concept can
  both ground self-knowledge and deflate the gap. Its scope note explicitly disclaims the stronger
  "phenomenal requires access" reading.
- `phenomenal-concept-isolation-tradeoff` is a **trade-off** claim internal to a *specific
  deflationary strategy* (the phenomenal-concept strategy): a dilemma on the strategy's
  isolation parameter (isolated-enough-to-deflate vs informative-enough-to-ground). It presupposes
  far more machinery (cognitive isolation, P(E|H1), the deflation move) and is false-making for a
  different target.
- `argument-phenomenal-concept-overgeneration` is not a claim at all; it is the **argument node
  that concludes** the isolation-tradeoff claim and attacks `argument-gap-deflated-by-phenomenal-
  concepts`. Claims and arguments are different node types and are never merged with each other.
- Logical relationship, not identity: posing-the-gap-requires-access is the *prior, weaker* point
  that some access is needed at all; the isolation-tradeoff is a *downstream* point about a
  particular move's cost structure. One can hold the first and reject the second (e.g. an
  acquaintance theorist who thinks access is needed to pose the gap but denies the trade-off).
- The two claims already carry mutual `Distinct from` notes in their bodies; the distinction is
  authored, not accidental.

## Suggested canonical id
None — **keep all three separate.** The argument node is a distinct type and stays. The two
claims are at different dialectical levels (precondition vs strategy-internal trade-off) and are
not restatements of one proposition.

## Edges that would need rewiring (only if a human overrides and merges the two claims)
If `claim-posing-the-gap-requires-access` were ever folded into
`claim-phenomenal-concept-isolation-tradeoff` (NOT recommended), the following would need
attention. Current inbound edges by id:
- `argument-phenomenal-concept-overgeneration` — `premise` and `concludes` point to
  `claim-phenomenal-concept-isolation-tradeoff` (would survive a merge into that id; would break if
  the isolation-tradeoff claim were the one retired).
- No node currently carries a frontmatter edge to `claim-posing-the-gap-requires-access`
  (it is referenced only in prose `Distinct from` notes in
  `claim-phenomenal-concept-isolation-tradeoff` and `argument-phenomenal-concept-overgeneration`).
  Confirm with `scripts/lint.py` INDEX backlinks before any action.

Because no inbound frontmatter edges target `claim-posing-the-gap-requires-access`, a merge would
be low-cost mechanically — but it is the wrong move semantically. Keep separate.

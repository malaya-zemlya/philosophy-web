# Scope proposal: `claim-consciousness-fundamental-ubiquitous` (experience vs proto-experience)

Status: **IMPLEMENTED 2026-11-19 (option A)**, approved by the user
Flagged 2026-11-19 while reconciling panqualityism with `claim-micro-subjects-do-not-sum`.

## The problem

The claim's **title** says one thing and its **body** says another:

- title: "Consciousness is fundamental, present even in the simplest physical entities"
- body: "experience, or proto-experience, is a fundamental, ubiquitous feature of the physical world"

The two readings imply different formal edges:

| node | edge | correct under the title reading? | correct under the body reading? |
|---|---|---|---|
| `position-panqualityism` | `rejects` | yes: unexperienced qualities are not consciousness | **no**: panqualityism is a panprotopsychism, so it asserts the proto-experiential disjunct |
| `argument-combination-problem` | `attacks` | yes: the premise (micro-subjects do not sum) targets micro-*subjects* | **too broad**: the premise does not touch the proto-experiential disjunct, which posits no micro-subjects |
| `argument-genetic-panpsychism` (Strawson) | `concludes` | yes: Strawson concludes real experience | yes |
| `argument-no-arbitrary-line-panpsychism` | `supports` | yes: a threshold for *experience* | yes |
| `argument-intrinsic-nature` (Russellian) | `concludes` | **too strong**: Chalmers (2017) concludes panpsychism *or* panprotopsychism | yes |
| `position-panpsychism` | `commits_to` | yes, but its body also says "experiential, or proto-experiential" | yes |

Whichever reading is chosen, at least one edge is wrong today.

## Options

**A. Narrow the claim to its title, and add a sibling (recommended).**
1. Edit the body of `claim-consciousness-fundamental-ubiquitous` to drop "or proto-experience", so that the
   claim is that *experience* (with micro-subjects) is fundamental and ubiquitous. This matches its title,
   headword, and the Strawson and Goff attributions in the body.
2. Create `claim-protophenomenal-properties-fundamental`: the fundamental physical entities have
   intrinsic properties that are not themselves experiential but that constitute experience when suitably
   combined. Attribute it to `chalmers`, cite `source-chalmers-2017` and `source-sep-panpsychism`, and give
   it a body explaining why it is distinct from the experiential claim.
3. `position-panqualityism`: keep `rejects: claim-consciousness-fundamental-ubiquitous` and add
   `commits_to: claim-protophenomenal-properties-fundamental`. Panqualityism's
   `claim-qualities-exist-unexperienced` is a species of it.
4. `argument-intrinsic-nature`: its conclusion is the disjunction. Either retarget `concludes` to a
   disjunctive claim, or keep it on the experiential claim and have the "weak point" section record that the
   argument licenses only the disjunction (Chalmers 2017). This needs a decision; see open question 1.
5. `position-panpsychism`: remove "or proto-experiential" from the body, and refer readers to
   [[position-panqualityism]] and the new claim for the protopsychist variant.

Effect: `argument-combination-problem` attacks exactly the claim its premise bears on, and panqualityism's
`rejects` becomes true.

**B. Keep the broad body, and fix the title and edges around it.**
Retitle the claim as the disjunction, then change `position-panqualityism` from `rejects` to `commits_to`
and add a new narrow micro-subject claim for `argument-combination-problem` to attack. This edits more
nodes, and it gives panqualityism and Strawson's panpsychism the same core commitment, which loses the
distinction the web most needs here.

**C. Do nothing structural.** Add a scope note to the claim saying that the combination problem targets only
the experiential disjunct. This leaves the panqualityism `rejects` edge false under the body reading.

## Recommendation

Option A. It makes the smallest change to meaning, because it brings the body into line with the title
that every edge was evidently written against. It also keeps the experiential claim and the
protophenomenal claim atomic, as rule 4 requires.

## Open questions for the reviewer

1. `argument-intrinsic-nature`: should it conclude a disjunctive claim, or keep the experiential claim and
   record the overreach in its prose?
2. Should the new claim also serve other panprotopsychist views (e.g. Chalmers's protophenomenal
   Russellian monism, `position-russellian-monism`)? Check that position's edges at the same time.

## Resolution (2026-11-19)

Option A was implemented. The open questions were settled as follows:

1. `argument-intrinsic-nature` keeps `concludes: claim-consciousness-fundamental-ubiquitous`. Under the
   narrowed reading the edge is correct, because premise (5) explicitly excludes a non-experiential
   intrinsic nature. Its "weak point" section now records the panprotopsychist reply (accept 1–2, deny 5).
2. `position-russellian-monism`'s edges are unchanged, since it commits to neither disjunct. Its body now
   links the new claim at the point where it mentions panprotopsychism.

Changes: created `claim-protophenomenal-properties-fundamental` (author `chalmers`); narrowed the body of
`claim-consciousness-fundamental-ubiquitous` and added panprotopsychists to its deniers;
`position-panqualityism` now also `commits_to` the new claim; prose links added in `position-panpsychism`,
`position-russellian-monism` and `argument-intrinsic-nature`.

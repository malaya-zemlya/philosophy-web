# Argument patterns (argumentation schemes)

A **pattern** is a stereotyped, *defeasible* form of reasoning — premises to a conclusion by a
recognisable move (appeal to expertise, analogy, cause→effect, a thought experiment …). Each
pattern ships with a fixed list of **critical questions (CQs)**: the standard ways that move can
fail. The CQs are a *checklist of legitimate attacks* tailored to the pattern.

> Naming: these are what the literature calls **argumentation schemes** (Walton, Reed &
> Macagno 2008; realised in the Carneades system). We call them **patterns** here so the word
> doesn't collide with `schemas/`, which defines node *types*. `schemas/` = the shape of a node;
> `patterns/` = the shape of an inference.

## What this directory is (and isn't)
- It is a **reference library**, like `schemas/` — static docs, **not** web nodes. There are no
  `patterns/` ids in `web/INDEX.md` and patterns have no `author`/provenance of their own.
- A pattern is **cited from** an `argument` node via the optional `pattern:` field
  (`pattern: cause-to-effect`). That declares "this argument instantiates this move," which in
  turn names its known attack surface — the pattern's CQs.

## Why patterns matter for the web
1. **A principled menu of attacks.** Instead of inventing an objection from scratch, an attacker
   walks the cited pattern's CQ list: each unanswered CQ is a ready-made line of attack.
2. **Absence becomes informative.** If an argument cites `pattern: expert-opinion` and *no*
   attacking argument has raised CQ-consistency (do other experts disagree?), that gap is a
   concrete prompt for the next debate turn.
3. **Burden of proof shifts.** Raising a CQ doesn't require proving the conclusion false — it
   reopens a presumption the arguer must answer. This matches how `attacks`/`responds_to`
   already chain in the web.

## How a CQ becomes an edge
A critical question is realised as an ordinary `argument` node with an `attacks` edge — exactly
the existing objection machinery, just *typed* by which CQ it instantiates. Convention:

- The attacking argument's body opens by naming the CQ it raises, e.g.
  `Raises cause-to-effect CQ2 (could the effect have another cause?).`
- It `attacks` the premise or inference the CQ targets (the pattern file says which, per CQ).
- It may itself declare a `pattern:` if the objection is also a positive move (e.g. an attack
  that works *by analogy* cites `pattern: analogy`).

So a pattern adds no new node type and no new edge — it only labels *why* an `attacks` edge is
the one the move invites.

## Pattern file format
Frontmatter is minimal (these aren't web nodes): `id`, `title`, `aka`, `source`, `inference_form`.
Body = **Form** (premise/conclusion skeleton) + **Critical questions** (numbered; each names a
short slug, the doubt it raises, and *what it attacks*) + **Notes** on typical use.

## The library
| id | move |
|----|------|
| `expert-opinion`   | appeal to a relevant authority |
| `analogy`          | transfer a verdict between similar cases |
| `cause-to-effect`  | predict/explain via a causal generalisation |
| `consequences`     | argue for/against an action by its outcomes |
| `sign`             | infer a state from an observable indicator |
| `example`          | generalise from instances |
| `thought-experiment` | intuition pump / counterexample (project extension) |

To add a pattern: copy an existing file, keep the body structure, and add a row above.

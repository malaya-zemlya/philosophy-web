---
name: web-protocol
description: "The schema and write discipline for the philosophy web. Use whenever creating, editing, citing, or navigating nodes in web/ (concepts, claims, arguments, questions, positions, sources, characters). Defines frontmatter fields, the edge vocabulary, id/slug conventions, and the grep-before-create rule."
---

# Web protocol

Every node is one Markdown file with YAML frontmatter + a prose body. Filename is a **slug**;
frontmatter carries a stable **id**. References live in two layers:
- **Frontmatter edges reference other nodes by id** (the machine layer `scripts/lint.py` reads),
  so renaming a file never breaks an edge (lint resolves id→path from frontmatter; the slug
  usually matches the filename but need not).
- **Body and transcript prose reference nodes with the `[[id]]` shorthand**, which `lint.py`
  renders into a clickable relative Markdown link `[slug](relpath)` and keeps fresh. Like the
  computed backlinks, these links are *derived* — author the `[[id]]`, never hand-write the link.
  Use `[[id|your label]]` when you want custom link text.

## Universal frontmatter (every node)
```yaml
id: <type>-<slug>          # e.g. claim-substrate-independence  (STABLE, never reuse)
type: concept | claim | argument | question | position | source | character
title: <one line>
author: <real-philosopher | generic | mishka>   # provenance, mandatory; content nodes are NEVER authored by a character (see "Neutral perspective" below). A `character` portfolio node is the sole exception: it is authored by its own character id.
status: asserted | contested | retracted | superseded   # default asserted
superseded_by: <id>        # only if status: superseded
tags: [..]
created: YYYY-MM-DD
```

## Edge vocabulary (store only the OUTGOING direction)
The node that does the citing/attacking owns the edge. Targets are ids.

| edge            | lives on            | points to            | meaning                              |
|-----------------|---------------------|----------------------|--------------------------------------|
| `uses_concept`  | any                 | concept              | invokes this concept                 |
| `presupposes`   | claim, argument     | claim, concept       | takes this as given                  |
| `premise`       | argument            | claim                | a premise of the argument            |
| `concludes`     | argument            | claim                | the conclusion                       |
| `supports`      | argument            | claim, argument      | gives positive reason for target     |
| `attacks`       | argument            | claim, argument      | gives reason against target          |
| `responds_to`   | argument            | argument             | reply to an earlier argument         |
| `answers`       | claim, position     | question             | a candidate answer to the issue      |
| `commits_to`    | position, character | claim                | endorses                             |
| `rejects`       | position, character | claim                | denies                               |

**Do NOT** record `supported_by` / `attacked_by` / `held_by` / candidate-answer lists.
Those are backlinks — `scripts/lint.py` computes them and writes `web/INDEX.md`.

## Per-type notes
- **concept** — term + definition(s), including competing ones. Body may list `senses`.
- **claim** — exactly one proposition in `title`. Body: gloss, scope, who would deny it.
  Keep it atomic; if you're tempted to write "X and Y", make two claims.
- **argument** — `premise`(s) + `concludes`, or `supports`/`attacks`/`responds_to`. Body
  states the inference form (deductive/abductive/analogy) and the weakest premise.
  **Always set the `pattern:` field** when the move fits a named scheme: pick the best match from
  `patterns/` (`expert-opinion`, `analogy`, `cause-to-effect`, `consequences`, `sign`, `example`,
  `thought-experiment`) — read that pattern file and confirm the move's premises/conclusion line
  up with its **Form** before committing to it. `pattern` is a *reference* into `patterns/`, **not
  an edge** (don't list it with the edges above; it points to a filename, not a node id, and lint
  computes no backlink from it). If no pattern genuinely fits, omit it rather than forcing one.
  When the argument *attacks* a target that itself cites a pattern, prefer the attack the pattern
  invites: name the **critical question** you raise in the first line of the body (e.g.
  `Raises thought-experiment CQ4 (bridge): …`) and aim the `attacks` edge at what that CQ targets.
- **question** — the IBIS *issue*. Minimal: just the question + tags. Candidate answers are
  found by backlink (nodes with `answers: <this id>`), not listed here by hand.
- **position** — a named view (e.g. proteocentrism) independent of any character.
  `commits_to` / `rejects` claims, `answers` questions. Reusable; characters cite it.
- **source** — philosopher/text/paper for provenance. Body: relevance, key page refs.
- **character** — evolving portfolio. See template; this is the character's memory.

## Body style: the encyclopedia standard (content nodes)
Concept, position, argument and question bodies are written as entries in a good general
encyclopedia (Britannica is the model) — they will eventually be collected into a printed
personal encyclopedia of philosophy, so each must stand alone on a page. Lead with a
plain-language definition, then the nuances; be self-contained (`[[id]]` links enrich, never
required reading); stay approachable to an interested amateur without losing precision; include
a concrete example or canonical case where the subject allows; write real prose with `###`
subheadings for longer entries — never `label: fragment` notes. The style never costs the web its
cross-links: weave `[[id]]` links into the prose where natural, and close the entry with a
`### See also` section (the very last section, after any `### In plain terms`) mapping the entry's
related nodes — required for every related node the prose didn't absorb, allowed for the body's
most important links, each item an `[[id]]` plus a clause saying how it relates. Claims stay
atomic and short but still read as prose. Full standard + worked example: `schemas/_style.md`.

## Optional `### In plain terms` section (content nodes)
When a claim, concept, argument, question, or position is technical or jargon-heavy, end its body
with a `### In plain terms` section — a short, plain-language explanation for a casual visitor to
the repo with **no** philosophy training who has **not** read the rest of the web. Rules:
- **Additive, never a substitute.** It does not override, soften, or restate-away the precise prose
  above it; the nuances stay upstairs. Think "front porch", not "replacement".
- **Self-contained, but link what it leans on.** Avoid jargon; if a term is unavoidable, unpack it
  in a phrase. Never rely on reading order — a casual reader may land on this node first, so don't
  write "the previous reply" / "just proposed". When the section refers to **another move in the
  web** (a reply it answers, an objection it rebuts, a case it sharpens), name that move in a few
  plain words *and* link it with `[[id]]`: the gloss carries the gist, the link carries the full
  story. Keep links to the genuinely-referenced moves only — don't gratuitously link every concept.
- **Only where it earns its keep.** A node already readable by a layperson needs none. Where a term
  genuinely cannot be removed, simplify as far as possible without flattening the distinction rather
  than dropping the section.
- Heading is exactly `### In plain terms`, placed after the main prose; only a `### See also`
  section may follow it.

## Neutral perspective (non-negotiable for content nodes)
A **claim, concept, argument, question, or position belongs to philosophy in general, not to a
character.** Its body is written from a neutral standpoint and **must not name a character**
(mu-043, alvin, sophia, rinat, …). Write "the organisational-role functionalist holds X", not
"mu-043 holds X"; write the position itself, not who in the debate voiced it.
- References to a **real** philosopher or scientist (Block, Chalmers, Putnam, …) and to `source`
  nodes are encouraged — that is attribution, not a character tie.
- The `author` of a content node follows the same rule: a real philosopher (`block`), `generic`
  (well-known idea, no single source), or `mishka` (introduced while building this web). Never a
  character id. **`mishka` is reserved for ideas genuinely original to this web**: if a node
  restates a known thinker's view (a philosopher, scientist, writer …), attribute it to that
  person (`putnam`, `chalmers`, `block`, …), not `mishka`.
- What a character believes, concedes, or will be moved by lives **only** in that character's
  portfolio (`web/characters/<id>.md`) and in the transcripts — never baked into a content node.

## The grep-before-create rule (non-negotiable)
Before creating a node:
1. `grep -ri "<2-3 key phrases>" web/` and read the closest hits.
2. If an equivalent exists → cite it: by id in a frontmatter edge, and/or as `[[id]]` in prose. Done.
3. If genuinely new → create it, and in the body add a line:
   `Distinct from [[<id>]] because …`
This single discipline prevents the fragmentation that makes the graph unusable at
treatise-writing time. When unsure whether two claims are the same, create the new one
**and** flag the pair for `/reconcile` rather than silently merging.

## Citing nodes in prose (bodies and transcripts)
In any prose — a node's body or a transcript — reference another node with the `[[id]]` shorthand
(e.g. `[[claim-substrate-independence]]`, or `[[claim-substrate-independence|substrate
independence]]` for custom text). Do **not** hand-write the Markdown link: `scripts/lint.py`
renders `[[id]]` into a clickable `[slug](relpath)` link and refreshes it on every run, so a reader
browsing on GitHub can click straight through to the target. References stay greppable — by slug
and path in the rendered link, and by full id in the frontmatter edges. Frontmatter edges always
stay bare ids; only prose gets links.

## Mathematics in a body
Write formulas in LaTeX maths: **inline** between single dollars (`$P(h\mid e)=\frac{P(e\mid h)P(h)}{P(e)}$`),
**display** by fencing with `$$` on their own lines (a centred block) — content between the
delimiters is passed to LaTeX verbatim, so `\frac`, sub/superscripts and `aligned` all work. The
`$` must hug its content (no inner spaces), which keeps a prose dollar like `$5` literal; keep
display maths on its own line(s). A single symbol in prose can just be the Unicode glyph
(`∴ ∧ Φ Σ`). Full guide + worked fixture: `schemas/_style.md` ("Mathematics").

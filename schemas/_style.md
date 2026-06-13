# Node body style — the encyclopedia standard

The defining nodes of this web — **concept, position, argument, question** — will eventually be
collected into a PDF: a personal encyclopedia of philosophy. Write each one as if it were an
entry in a good general encyclopedia (Encyclopedia Britannica is the model): an educated,
interested amateur should be able to open the entry cold, with no philosophy training and no
other node in hand, and come away understanding the thing.

## The rules

1. **Lead with a plain definition.** The first paragraph says what the thing *is* in one to
   three sentences of ordinary language, before any history, taxonomy, or dispute. A reader who
   stops after the first paragraph should leave with a correct (if shallow) picture.
2. **Self-contained.** The entry must be comprehensible on its own. `[[id]]` links enrich and
   connect; they are never required reading. If understanding the entry genuinely requires
   another idea, summarize that idea in a clause *and* link it.
3. **Approachable, not dumbed down.** Precision is never sacrificed — but jargon is spent like
   money. Introduce a term of art in *italics* on first use and unpack it in a phrase. Prefer
   the plain word when it loses nothing.
4. **Give an example.** Wherever the subject allows, include at least one concrete example,
   illustration, or canonical case — a good encyclopedia shows, then generalizes.
5. **Real prose, good formatting.** Full sentences and connected paragraphs — never
   `label: fragment` note-taking style. Use `###` subheadings to structure longer entries
   (e.g. competing senses, history, the live dispute). Use bold sparingly, for genuine
   signposts. The entry should typeset cleanly on a printed page.
6. **The print test.** Before saving, ask: *dropped alone onto a page of an encyclopedia of
   philosophy, would this entry stand?* If it reads like internal notes, a changelog, or a
   move in a conversation the reader hasn't seen, rewrite it.
7. **Keep the web dense — `### See also` is the entry's map of its neighborhood.** The
   encyclopedia style must not cost the web its cross-links: an entry keeps all the `[[id]]`
   references the old body carried, and adds the ones a reader would want. Prefer working a
   link into the prose where it arises naturally; then close the entry with a `### See also`
   section (placed at the very end, after the optional `### In plain terms`) listing the
   entry's related nodes. It *must* include every related node that found no natural home in
   the prose, and it *may* repeat the body's most important links — the section should read as
   a complete map of the entry's neighborhood. Each See-also item is an `[[id]]` link followed
   by a short clause saying *how* it relates — never a bare list of ids.

**Claims** are exempt from entry-length expectations — a claim stays one atomic proposition —
but its body is still written as readable, self-contained prose, not fragments. The optional
`### In plain terms` section (cardinal rule 9) is unchanged: where the entry is technical or
jargon-heavy it still gets that plain-language gloss, additive and never a substitute for a
readable main body. Section order at the end of an entry: main prose, then `### In plain
terms` (optional), then `### See also` (optional) last.

## Worked example

A concept entry written to this standard (frontmatter per `schemas/concept.md`):

```markdown
---
id: concept-qualia
type: concept
title: Qualia
author: generic
status: asserted
tags: [philosophy-of-mind, consciousness]
created: 2026-06-12
---

*Qualia* (singular *quale*, from the Latin for "of what kind") are the subjective, felt
qualities of conscious experience: the redness of a ripe tomato as it looks to you, the
bitterness of coffee, the particular ache of a stubbed toe. The term names not the tomato,
the coffee, or the toe, but what undergoing those experiences is *like* from the inside.

The standard way to isolate the idea is by contrast with function. Two states might play
exactly the same role — both produced by tissue damage, both causing you to wince and say
"ouch" — and we can still ask whether they *feel* the same. That residue, the felt character
left over once every causal role is accounted for, is what "qualia" is meant to capture.
Canonical illustrations include the *inverted spectrum* (could your "red" experience be like
my "green" one, with all our behavior unchanged?) and Frank Jackson's black-and-white
scientist Mary, who knows every physical fact about color vision yet seems to learn something
new when she first sees red ([[concept-knowledge-argument]]).

### Senses of the term

The word is contested, and the dispute is often over the definition rather than the facts.
In a **thin** sense, qualia are simply the ways experiences feel, with no further commitment —
almost no one denies these exist. In a **thick** sense (associated with critics like Daniel
Dennett), qualia are additionally *intrinsic*, *ineffable*, *private*, and *directly
apprehended* — and Dennett's "Quining Qualia" (1988) argues that nothing satisfies that job
description, so qualia in the thick sense should be abandoned. A claim that is obvious on the
thin reading can be question-begging on the thick one; entries citing this concept should say
which sense they use.

### Why the concept matters

Qualia mark the spot where the mind seems hardest to fit into a scientific world picture.
They drive the [[concept-hard-problem]] of consciousness — explaining why physical processing
is accompanied by felt experience at all — and they power the classic anti-materialist
thought experiments, from Mary's room to the [[concept-philosophical-zombie]], a creature
physically identical to you with no inner feel. How much weight qualia can bear is, in large
part, what the materialism debate is about.

### In plain terms

"Qualia" is the philosopher's word for how things *feel* to you — the way red looks, the way
coffee tastes, the way a headache hurts. A brain scanner can show what your neurons are doing
when you see red, but it doesn't show the redness *you* experience; qualia are that inner,
felt side of the story. Philosophers argue about whether these feels are something extra that
science struggles to explain, or whether — as skeptics like Daniel Dennett say — the whole
idea falls apart once you look at it closely.

### See also

- [[concept-hard-problem]] — why physical processing is accompanied by felt experience at all;
  the problem qualia pose in its sharpest form.
- [[concept-knowledge-argument]] — Mary the colour scientist; whether complete physical
  knowledge still leaves the qualia out.
- [[concept-philosophical-zombie]] — a physical duplicate with no qualia; the conceivability
  test for whether the physical facts fix the felt facts.
- [[concept-functionalism]] — the theory of mind qualia are most often said to outrun: mental
  states defined by causal role, with the felt character left unaccounted for.
- [[concept-access-vs-phenomenal-consciousness]] — Block's distinction separating the
  information a state makes available from what the state feels like; qualia live on the
  phenomenal side.
```

Why this passes: the first paragraph alone gives a correct picture; every technical term
(*quale*, *inverted spectrum*, thin/thick) is unpacked where it appears; it shows examples
before generalizing; the links are enrichment, with enough said in place that the entry
survives without them; it closes with an `### In plain terms` gloss a reader with no
philosophy background can take away whole, followed by a `### See also` that carries the
related nodes the prose didn't absorb; and it would sit comfortably on a printed
encyclopedia page.

For contrast, the same content fails the standard when written as internal notes:

```markdown
primary definition: subjective felt qualities of experience (what-it's-likeness).
senses: thin (uncontroversial) vs thick (intrinsic/ineffable/private — Dennett denies).
feeds: concept-hard-problem, concept-philosophical-zombie, concept-knowledge-argument.
```

Accurate — but it is a database record, not an entry anyone could read.

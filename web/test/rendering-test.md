---
id: concept-rendering-test
type: concept
title: Rendering test fixture (every book feature)
headword: Rendering test
author: mishka
status: asserted
tags: [meta, test]
uses_concept: [concept-hard-problem]
style: legacy
created: 2026-06-13
---

This node is a *fixture*: it is not philosophy but a deliberate exercise of every formatting
feature the encyclopedia renderer supports, so that `make entry ID=concept-rendering-test` (or a
full `make book STYLE=any`) shows at a glance whether anything has regressed. It lives under
`web/test/` and is tagged `style: legacy`, both of which keep it out of the default encyclopedia
build. The opening paragraph alone covers the basics: **bold** text, an *italicised term*, a
snippet of `inline code`, a cross-reference woven into a sentence as a noun, the way
[access-consciousness](../concepts/access-consciousness.md) names a concept, and a parenthetical pointer to a related entry
([hard-problem](../concepts/hard-problem.md)).

A multi-target pointer should collapse to a single "see" with comma-separated labels
([phenomenal-consciousness](../concepts/phenomenal-consciousness.md), [cognitive-closure-exists](../claims/cognitive-closure-exists.md)). An explicit alias must
render the chosen short label rather than the title, as in [the hard problem](../concepts/hard-problem.md).
A reference whose target has no headword falls back to its full title in italics
([posing-the-gap-requires-access](../claims/posing-the-gap-requires-access.md)), where one with a headword is set in small caps
([introspective-gap-varieties](../concepts/introspective-gap-varieties.md)).

Inline mathematics is written between single dollar signs: the posterior is
$P(h\mid e) = \frac{P(e\mid h)\,P(h)}{P(e)}$, and a subscripted, superscripted variable such as
$x_i^{2}$ should survive untouched. A stray prose dollar amount like $5 and $10 must stay literal,
and a dollar inside `code such as $PATH` must not be read as maths. Single Unicode symbols in
running prose still work through the symbol map: $\therefore$ the conjunction $\wedge$, the field
$\Phi$, and the sum $\Sigma$ render as mathematics even when typed as ∴, ∧, Φ, and Σ. Curly
"quotation marks" should come out directional.

### Display mathematics and subheadings

A block of display mathematics is fenced by `$$` on their own lines and is emitted verbatim, so
multi-line constructions work:

$$
\Phi(\text{world}) = \Phi_{\text{physical}}
\quad\text{and}\quad
\mathcal{Q} = \varnothing
$$

A display block may also be written on a single line of its own:

$$ E = mc^{2} $$

It should still be set centred on its own line.

Ordered and unordered lists must render, including items that wrap onto a second source line:

- The first bullet states something short.
- The second bullet runs long enough that it continues onto another line in the source, and that
  continuation must be folded into the same item rather than dropped.
- A third bullet citing an entry inline, namely [access-consciousness](../concepts/access-consciousness.md), for good measure.

1. First numbered step.
2. Second numbered step, with inline maths $a^2 + b^2 = c^2$ inside it.

### In plain terms

This section tests the shaded aside, and in particular a sub-heading nested *inside* it. The next
heading is written with two hashes precisely so it stays within the aside instead of being split
off as a new top-level entry section.

## Illustration

A heading at level two should render as a run-in heading here, not print its hash marks literally.
A short inline formula like $1 + 1 = 2$ should also render inside the aside.

### See also

- [hard-problem](../concepts/hard-problem.md) — a headworded concept, so this label should be small caps; the clause
  wraps onto a second source line to confirm the continuation is not truncated at the break.
- [posing-the-gap-requires-access](../claims/posing-the-gap-requires-access.md) — a claim with no headword, so its full sentence title
  should appear in italics rather than shouting in small caps.
- [introspective-gap-varieties](../concepts/introspective-gap-varieties.md) — the taxonomy entry, included to confirm a long headword
  renders cleanly in the cross-reference list.

# source
A philosopher, text, or paper, for provenance and citation.

## Frontmatter (copy & fill)
```yaml
---
id: source-<slug>                         # REQUIRED · stable
type: source                              # REQUIRED
title: <Author — Work (year)>             # REQUIRED
author: <who-added-it>                    # REQUIRED · the NODE's author, NOT the cited work's author
status: asserted                          # asserted | contested | retracted | superseded
tags: []                                  # optional
created: YYYY-MM-DD                        # REQUIRED
# --- edges: NONE are legal for a source ---
---
```
A source is referenced by other nodes' bodies and by their `author` field, not via edges.

## Body
- **relevance** to this project (which idea(s) the work grounds; content vs. method/form), with
  `[[id]]` links to the nodes it grounds.
- the **reference**: the work's full bibliographic citation in **APA 7th-edition** style (below),
  plus any key page refs.

## Reader-facing citation (APA 7th edition)
The reference in a source body is written in **APA 7th-edition** reference-list style, so it reads
the same in the Markdown, on GitHub, and in the typeset PDF. The frontmatter `title` stays the short
`<Author — Work (year)>` handle; this is the full citation a reader sees. Head the citation block
**`Reference:`** (or **`References:`** for more than one work) — do not annotate it with "(APA 7)";
APA is simply the style, not a visible label.

Encode it in Markdown so it renders correctly (Markdown `*…*` → italics in TeX/PDF and on GitHub):
- **Author** is `Surname, A. A.` (last name, then initials). Join the final author with `&`; for
  3–20 authors list them all, for 21+ list the first 19, `…`, then the last.
- **Year** in parentheses after the authors: `(2008)`. Then the title.
- **Italics** for the periodical/book title **and** the volume number; the issue number in
  parentheses stays roman — `*The Philosophical Review*, *90*(1), 5–43`.
- **Sentence case** for article/chapter/book titles (capitalize only the first word, the first word
  after a colon, and proper nouns), and **no quotation marks** on them; **Title Case** for the
  journal/periodical name.
- **En dash** (`–`, not a hyphen) in page ranges (`261–325`).
- A **DOI or URL** goes last as a bare link with **no** trailing period: `https://doi.org/10.1234/x`.

Templates (the three common cases):
- **Journal article** — `Surname, A. A. (Year). Title of the article. *Journal Title*, *Vol*(Issue), pp–pp. https://doi.org/…`
- **Whole book** — `Surname, A. A. (Year). *Title of the book: Subtitle* (Nth ed.). Publisher.`
- **Chapter in an edited book** — `Surname, A. A. (Year). Title of the chapter. In E. E. Editor (Ed.), *Title of the book* (pp. pp–pp). Publisher.`

Examples, exactly as they should read in the body:
- Block, N. (1981). Psychologism and behaviorism. *The Philosophical Review*, *90*(1), 5–43.
- Block, N. (1978). Troubles with functionalism. In C. W. Savage (Ed.), *Perception and cognition: Issues in the foundations of psychology* (Minnesota Studies in the Philosophy of Science, Vol. 9, pp. 261–325). University of Minnesota Press.
- Lewis, D. (1988). What experience teaches. *Proceedings of the Russellian Society*, *13*, 29–35.

A reprint may be noted after the entry: `(Reprinted in W. G. Lycan (Ed.), *Mind and cognition*,
pp. 499–519, Blackwell, 1990)`. **Note:** APA's sentence case and absence of quotation marks on
article titles can look unfamiliar for philosophy works (*What experience teaches*, not "What
Experience Teaches") — that is the standard, and is intended.

A **citing node** refers to the work in APA in-text form — the author and year, carrying the link:
`Lewis ([[source-lewis-1988|1988]])` or `(Lewis, [[source-lewis-1988|1988]])`.

**Keep the `Reference:` block to the bare citation.** The encyclopedia build (`scripts/book.py`)
collects every source cited by the entries in a volume and prints its `Reference:` block, verbatim,
in a back-matter **Sources** section (with the in-text citations hyperlinked to it). So editorial
annotation — what the work shows, key passages, page-referenced quotes — belongs in the `relevance`
prose or a separate labelled note, **not** inside the reference, or it will bloat the bibliography.
A short clause such as `(Original work published 2008)` is fine; a paragraph of commentary is not.

## Pre-save checklist
- [ ] read this schema; not duplicating an existing source
- [ ] node `author` (who added it) set, distinct from the cited work's author
- [ ] reference written in APA 7th-edition style (sentence-case title, italic journal/volume,
      en-dash pages, DOI without trailing period)

"""Type glyphs for the encyclopedia — EDIT THIS FILE to experiment.

`GLYPHS` maps a node type to the little mark that prefaces its entry (and its row in the List of
Entries), signalling the kind of article at a glance. The mark is rendered small and dimmed, and
appears ONLY in the entry head and the List of Entries — never in sorting, anchors, cross-references,
the running head, or the Markdown. Change a value and re-run `make book`; nothing else needs editing.

Each value is a LaTeX snippet (a raw string, so backslashes are literal — no escaping). The book
preamble already loads amsmath/amssymb, so any symbol from those is safe under every engine
(pdflatex / xelatex / lualatex / tectonic). Wrap a math symbol in $…$; a text command (\\dag, \\S)
needs no dollars.
"""

# Order the types appear in the front-matter "Symbols" key.
GLYPH_ORDER = ["concept", "claim", "argument", "position", "question"]

GLYPHS = {
    "concept":  r"$\blacklozenge$",   # ◆  a defined term / idea
    "claim":    r"$\odot$",           # ⊙  a proposition
    "argument": r"$\vdash$",          # ⊢  proof-theory turnstile: "derives"
    "position": r"$\bigstar$",        # ★  a held stance
    "question": r"?",                 #    an open issue
}

# Palette to copy from (all render-safe). Avoid pairing look-alikes (◆ with ■, ⊢ with ⊨).
#   diamonds    $\blacklozenge$ ◆    $\lozenge$ ◇
#   circles     $\odot$ ⊙    $\bigcirc$ ○    $\oslash$ ⊘    $\circledast$ ⊛
#   squares     $\blacksquare$ ■    $\square$ □
#   triangles   $\blacktriangle$ ▲    $\blacktriangleright$ ▶    $\triangledown$ ▽
#   stars       $\bigstar$ ★
#   turnstiles  $\vdash$ ⊢    $\vDash$ ⊨    $\dashv$ ⊣
#   arrows      $\Rightarrow$ ⇒    $\mapsto$ ↦    $\to$ →
#   marks       \dag † · \ddag ‡ · \S § · \P ¶ · $\checkmark$ ✓
#   logic       $\therefore$ ∴    $\because$ ∵
#   question    ? · \textquestiondown ¿

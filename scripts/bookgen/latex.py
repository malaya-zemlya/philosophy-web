"""LaTeX escaping and the portable Unicode map.

The corpus mixes em dashes, logic/maths symbols (`∴ ∧ ¬ ⟹ ↦ Φ Σ ℛ`), subscripts, and accented
Latin. Rather than transliterate, we keep bodies as readable UTF-8 and declare each glyph once in
the preamble via `\\newunicodechar`, mapping it to an engine-agnostic LaTeX form. That way the
generated .tex compiles identically under xelatex / lualatex / pdflatex / tectonic.
"""
import re

# char -> portable LaTeX replacement (emitted as \newunicodechar declarations in the preamble)
UNICODE_MAP = {
    "—": "---", "–": "--", "…": r"\ldots{}",
    "§": r"\S{}", "·": r"\textperiodcentered{}", "×": r"\ensuremath{\times}",
    "−": r"\ensuremath{-}", "≈": r"\ensuremath{\approx}", "≠": r"\ensuremath{\neq}",
    "≥": r"\ensuremath{\geq}", "≤": r"\ensuremath{\leq}",
    "∴": r"\ensuremath{\therefore}", "∧": r"\ensuremath{\wedge}", "¬": r"\ensuremath{\neg}",
    "→": r"\ensuremath{\rightarrow}", "↦": r"\ensuremath{\mapsto}",
    "⇒": r"\ensuremath{\Rightarrow}", "⟹": r"\ensuremath{\Longrightarrow}",
    "Φ": r"\ensuremath{\Phi}", "Σ": r"\ensuremath{\Sigma}",
    "ℛ": r"\ensuremath{\mathcal{R}}", "𝒰": r"\ensuremath{\mathcal{U}}",
    "′": r"\ensuremath{{}^{\prime}}", "″": r"\ensuremath{{}^{\prime\prime}}",
    "₂": r"\textsubscript{2}",
    "ö": r'\"o', "é": r"\'e", "ł": r"\l{}",
}

# Single-character LaTeX specials (backslash is handled first, separately).
_ESCAPE = {"&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#", "_": r"\_",
           "{": r"\{", "}": r"\}", "~": r"\textasciitilde{}", "^": r"\textasciicircum{}"}


def _smart_quotes(text: str) -> str:
    r"""Straight ASCII double quotes -> LaTeX directional quotes (``…''). A `"` is *opening* when it
    starts the string or follows whitespace or an opening bracket, and *closing* otherwise. Deciding
    by the preceding char (not the following one) is what keeps a closing quote before punctuation —
    `bat?";` — from being mis-opened into `` ?` ``, which TeX would ligature into `¿`. (Apostrophes
    are left as-is; `'` already renders correctly.)"""
    text = re.sub(r'(^|[\s([{])"', r"\1``", text)
    return text.replace('"', "''")


def latex_escape(text: str) -> str:
    """Escape LaTeX specials in plain text. Backslash first; Unicode is mapped in the preamble."""
    text = text.replace("\\", r"\textbackslash{}")
    return _smart_quotes("".join(_ESCAPE.get(c, c) for c in text))


def unicode_declarations() -> str:
    r"""The block of \newunicodechar declarations for the preamble."""
    return "\n".join(r"\newunicodechar{%s}{%s}" % (ch, repl) for ch, repl in UNICODE_MAP.items())

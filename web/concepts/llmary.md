---
id: concept-llmary
type: concept
title: LLMary (the language model that never saw token 123)
headword: LLMary
author: mishka
status: asserted
tags: [philosophy-of-mind, consciousness, ai, thought-experiment]
uses_concept: [concept-knowledge-argument]
style: encyclopedia
created: 2026-06-12
---

*LLMary* is a thought experiment that recreates Frank Jackson's "Mary the colour scientist"
([jackson-1982](../sources/jackson-1982.md)) inside an artificial intelligence, in order to test the *inference* the
[knowledge argument](knowledge-argument.md) draws rather than its conclusion about what exists.
Where Mary is a human who knows all the physics of colour yet has never seen red, LLMary is a language
model that knows everything sayable about a word it has never actually processed.

### The setup

LLMary is a large language model trained on every book about AI and the whole of arXiv. Its prior
knowledge is meant to be as *complete* as Mary's: it knows all of machine learning, its own programming
and architecture, how transformers work, and how text is broken into *tokens* (the word-pieces a model
reads and predicts). It has even read extensive discussions of one particular token, referred to
throughout as *Token #123* — its index, its entry in the tokeniser table, its *embedding vector* (the
list of numbers that stands for it inside the network), its statistical role, the effect it would have
on the model's activations, and even the exact *update rule* — the gradient-descent step, with the very
gradient — that *would* occur if the model were ever trained on it. Everything any paper, or the
model's own equations, could state about the token. Knowing the update that *would* happen is still
description, not occurrence: the weights have not yet changed.

The one thing LLMary lacks, by stipulation, is that the actual word-piece corresponding to token 123
has never once appeared in its training stream. The token has been exhaustively *mentioned* to it; it
has never been *used* — never flowed through its input to be embedded and predicted. This mirrors Mary,
who has read every description *of* red, including the word "red" and the functional story of
red-experiences, but has never had the experience. The gap is purely one of use versus mention:
complete third-person knowledge *about* the token, zero first-pass *processing* of the token itself.

### The encounter

Then, mid-training on a new book, LLMary encounters token 123 for the first time — the word-piece
itself, used rather than mentioned. It plainly gains something. Because the model's predicted
probability for that token was near zero, the cross-entropy loss is large and the resulting gradient
update is large: a real, measurable change in its weights. This is the analogue of Mary "learning
something" the moment she first sees red.

The point of the construction is that *every element of the episode is uncontroversially physical*. The
prior knowledge is weights; the gain is a weight change; the trigger (token 123) is an integer, a
one-hot vector, a pattern of voltages. So LLMary is a case in which a system has complete prior
(sayable) knowledge, *and* undergoes a genuine gain on first encounter, *and* the whole affair is
plainly physical — exactly the combination the knowledge argument says cannot occur. What that buys
dialectically is worked out in [llmary-token-encounter](../arguments/llmary-token-encounter.md), where the standard reply is also
taken up: that LLMary "learns" only in the [access](access-vs-phenomenal-consciousness.md) sense,
with no felt residue.

### The general moral: use versus mention

What LLMary and the original Mary both expose is a *use/mention gap* — the gulf between a symbol or
description that *names* a thing and that thing itself *in use*. "Token #43453" (a mention) versus the
word-piece it denotes, met in the stream (a use); "red" — the word, the wavelength "700 nm", the
complete neuroscience — versus the actual red one undergoes.

This is not merely a fable. *SolidGoldMagikarp* is a real instance of exactly LLMary's predicament: an
anomalous "glitch token" that entered GPT's tokeniser vocabulary but was almost absent from the
training corpus, so the model possessed a name, an index, and an essentially untrained embedding for
it, yet behaved erratically the first time the token was actually used
([rumbelow-watkins-2023](../sources/rumbelow-watkins-2023.md)). The gap Mary dramatises for colour is the same gap that separates a
fully-described-but-never-encountered token from its first live use.

### What the gap settles, and what it does not

Identifying the gap as use/mention shows that "Mary learns something" has an innocent reading — but it
does not by itself decide what the *use*-side delivers. The deflationist reads the lesson as being
about the *mode of access* to a thing, a new guise on facts already possessed, rather than a second
realm of things. The realist grants the very same use/mention gap and denies that reading, holding that
the use-side *acquaints* one with a phenomenal property that no amount of mention conveys — the
acquaintance reply, [mary-gains-acquaintance](../claims/mary-gains-acquaintance.md). The token cases look decisive only because there
is uncontroversially nothing it is like for the model to process SolidGoldMagikarp; importing that
verdict to *red* is the contested step, not a result the gap supplies. So the use/mention framing
*relocates* the dispute — to whether acquaintance yields a new property or only a new guise — rather
than winning it.

This is why LLMary targets not physicalism directly but the knowledge argument's *inference*: the move
from "complete knowledge yet a gain on encounter" to "a non-physical fact." By furnishing a wholly
physical instance of that antecedent, it pressures the conditional. It asserts nothing about whether
colour experience is physical.

### In plain terms

LLMary is the Mary thought experiment redone with an AI. Mary is a scientist who knows all the physics
of colour but has never seen red ([knowledge argument](knowledge-argument.md)). LLMary is a
language model that has read every AI book and all of arXiv — so it knows how AIs like itself work, how
text gets chopped into tokens, and it has even read people *discussing* one particular token, which
they call "Token #123" — it could even work out in advance the precise way its own internal numbers
would shift the moment it finally met that token. The only thing it never got was the actual word-piece
that "Token #123" stands for: it has read *about* that token endlessly, but the token itself never once
showed up in the text it learned from. (Like reading every word ever written about the taste of
pineapple without once tasting one.)

Then one day it finally meets the real thing in its input, and it clearly *learns*: it was caught off
guard (it expected that token almost never), so its internal numbers get a big correction. The whole
point is that nothing spooky is going on — it's just numbers changing inside a computer because of an
input. So here's a case where something "knew everything sayable" — including all about its own
machinery — and *still* got updated the first time it actually met the thing, with everything fully
physical. (This is not just a fable: real AI systems have "glitch tokens" like **SolidGoldMagikarp** —
word-pieces that got into the vocabulary but were barely in the training text, so the model knows *of*
them but goes haywire the first time it has to actually use one.) The deeper point is a plain gap
between a *name or description* of something and the *thing itself* — "the word red" versus *red*. (What
that shows about Mary's argument, and the obvious objection that the AI doesn't actually *feel*
anything, are spelled out in the companion argument, [llmary-token-encounter](../arguments/llmary-token-encounter.md).)

### See also

- [knowledge-argument](knowledge-argument.md) — Jackson's "Mary the colour scientist"; the original of which LLMary
  is the computational variant.
- [llmary-token-encounter](../arguments/llmary-token-encounter.md) — the argument that turns this scenario into a counterexample to
  the knowledge argument's inference, and fields the "no felt residue" reply.
- [access-vs-phenomenal-consciousness](access-vs-phenomenal-consciousness.md) — the access/phenomenal split on which the deflationist
  and realist readings of LLMary's "gain" divide.
- [mary-gains-acquaintance](../claims/mary-gains-acquaintance.md) — the realist reply that the use-side acquaints one with a
  phenomenal property no description conveys; the move LLMary relocates rather than refutes.

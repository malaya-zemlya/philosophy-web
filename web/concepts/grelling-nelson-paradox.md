---
id: concept-grelling-nelson-paradox
type: concept
title: Grelling–Nelson paradox (the paradox of heterological words)
headword: Grelling–Nelson paradox
author: grelling
status: asserted
style: encyclopedia
tags: [logic, paradox, philosophy-of-language, self-reference]
uses_concept: [concept-content-vehicle-distinction]
created: 2026-11-15
---

The *Grelling–Nelson paradox*, also called the paradox of *heterological* words, is a contradiction
that arises from asking whether words have the properties they name. Some adjectives describe
themselves: "short" is a short word, "English" is an English word, "polysyllabic" has many syllables.
Call these *autological*. Others do not: "long" is not a long word, "German" is not a German word,
"monosyllabic" has more than one syllable. Call these *heterological*. The paradox comes from asking
which kind of word "heterological" is. It was published by Kurt Grelling and Leonard Nelson
([1908](../sources/grelling-nelson-1908.md)) in a paper on the paradoxes of Russell and Burali-Forti.

### The argument

Every adjective, it seems, is either autological or heterological, since a word either has the
property it expresses or lacks it. So take "heterological" itself.

- Suppose "heterological" is heterological. Then it has the property it expresses, so by definition it
  is autological, not heterological.
- Suppose instead that it is not heterological. Then it lacks the property it expresses, which is
  exactly what being heterological means, so it is heterological.

Each answer implies the other, so the word is heterological if and only if it is not. Nothing in the
reasoning looks suspicious. It uses only a definition that seems perfectly clear, the assumption that
the definition applies to every adjective, and elementary logic.

### Relation to Russell's paradox

Grelling and Nelson presented their antinomy as a close relative of Bertrand Russell's paradox in set
theory, which concerns the set of all sets that are not members of themselves. The two share one
proof. Write $\mathrm{ext}(P)$ for the *extension* of a predicate $P$, the set of things it is true of.
Then "heterological" is the predicate whose extension is $\{P \mid P \notin \mathrm{ext}(P)\}$, while
Russell's set is $R = \{x \mid x \notin x\}$ ([Bolander, SEP](../sources/sep-self-reference.md)):

$$
\begin{aligned}
\mathrm{het} \in \mathrm{ext}(\mathrm{het}) &\iff \mathrm{het} \notin \mathrm{ext}(\mathrm{het}) \\
R \in R &\iff R \notin R
\end{aligned}
$$

The only difference is that one ranges over predicates and *being true of*, the other over sets and
*being a member of*. Both are instances of the *diagonal* pattern behind Cantor's theorem that a set
has more subsets than members. Both also rest on an *impredicative* definition, one that defines a
thing by reference to a totality that includes the thing being defined: "heterological" is defined
in terms of all adjectives, itself among them. Russell ([1908](../sources/russell-1908.md)) diagnosed the
paradoxes of his day as arising from such "vicious circles" and proposed his theory of types, which
sorts entities into levels so that nothing can be defined in terms of a totality to which it belongs.

### Semantic and logical paradoxes

Frank Ramsey ([1926](../sources/ramsey-1926.md)) divided the paradoxes into two groups. *Logical*
contradictions, such as Russell's and Burali-Forti's, involve only logical and mathematical notions
like class and number, and so show that something is wrong with logic or mathematics. The others,
which Ramsey called *epistemological* and which are now usually called *semantic*, involve notions
such as meaning, naming and truth. Grelling's paradox belongs to the second group, with the liar
("this sentence is false") and Berry's paradox about "the least number not nameable in fewer than
nineteen syllables". Ramsey argued that only the logical paradoxes call for a hierarchy of types in
logic itself. The semantic ones, he held, show faulty ideas about language
([Cantini & Bruni, SEP](../sources/sep-paradoxes-contemporary-logic.md)).

The classification is useful but contested. The shared proof with Russell's paradox suggests that
the two groups are less different than Ramsey thought, and the same diagonal structure reappears in
Gödel's incompleteness theorems ([Bolander, SEP](../sources/sep-self-reference.md)).

### Responses

The most influential response treats semantic notions as belonging to a different level of language
from the expressions they apply to. Alfred Tarski ([1935](../sources/tarski-1935.md)) showed that no
sufficiently rich language can consistently contain its own truth predicate, so that truth for an
*object language* must be defined in a stronger *metalanguage*. Applied to Grelling's paradox, being
true of an adjective is a notion of the metalanguage, and "heterological" therefore cannot itself be
among the adjectives it classifies. The question "is 'heterological' heterological?" cannot be
formulated, and the paradox does not arise. The cost is that natural languages like English seem to
talk about their own words freely, so the hierarchy fits formal languages better than ordinary
speech.

Saul Kripke ([1975](../sources/kripke-1975.md)) proposed a way for a language to contain its own truth
predicate. Truth is built up in stages, starting from sentences that do not mention truth. Sentences
whose truth depends only on themselves, like the liar, are never assigned a value and count as
*ungrounded*, neither true nor false. On approaches of this kind the sentence "'heterological' is
heterological" is likewise left without a truth value, so the argument's assumption that every
adjective either has or lacks the property it expresses fails for this one case. Other responses
accept the contradiction as true while denying that it makes everything provable (*dialetheism*), or
restrict which definitions can introduce a predicate in the first place.

### Significance

The paradox shows that the innocent-looking practice of comparing a word with what it names is not
safe without restriction. Every word has two sides: its own features, such as its length or its
language, and the property it expresses. The definition of "heterological" sets the two against each
other, and the contradiction appears when the word is turned on itself. In this sense the paradox is
the point where the [distinction between a representation and
what it represents](content-vehicle-distinction.md) becomes a source of contradiction rather than mere confusion.

### In plain terms

Some words describe themselves. "Short" is a short word and "English" is an English word. Others don't:
"long" is not a long word. Call the words that don't describe themselves "heterological". Now ask
whether "heterological" describes itself. If it does, it is a word that describes itself, so it isn't
heterological after all. If it doesn't, then it is one of the words that don't describe themselves,
so it is heterological, and it does describe itself. Either answer flips into the other. Logicians
use the puzzle to show that talking about words using words has to be done with care, and it has the
same structure as a famous paradox about sets found by Bertrand Russell.

### See also

- [content-vehicle-distinction](content-vehicle-distinction.md): the difference between a sign's own properties and what it
  stands for, which the definition of "heterological" sets against each other.
- [sorites-paradox](../arguments/sorites-paradox.md): another classical paradox in which plausible premises and valid
  steps lead to an unacceptable conclusion, there from vagueness rather than self-reference.
- [complete-self-representation-impossible](../claims/complete-self-representation-impossible.md): a different limit on self-reference, the claim
  that no finite system can fully represent its own state, which rests on counting rather than on a
  diagonal argument.

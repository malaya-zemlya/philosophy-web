---
id: concept-postdiction
type: concept
title: Postdiction (later input shaping how an earlier event is experienced)
headword: Postdiction
author: generic
status: asserted
style: encyclopedia
tags: [philosophy-of-mind, consciousness, time, perception, neuroscience]
uses_concept: [concept-binding-problem, concept-unity-of-consciousness, concept-time-represented-vs-time-of-representing]
created: 2026-11-15
---

*Postdiction* is the brain's use of sensory input that arrives after an event to settle how that
event is experienced. What a person seems to see or feel at a given moment can depend on what
happens a fraction of a second later. The term was introduced for visual perception by David
Eagleman and Terrence Sejnowski ([2000](../sources/eagleman-sejnowski-2000.md)). It contrasts with
*prediction*, the use of past input to anticipate what comes next. Postdiction matters to philosophy
because it seems to show experience doing something impossible: filling in a moment with information
that did not yet exist at that moment.

### Canonical cases

**Colour phi.** Flash a red spot, then a green spot a short distance away a fraction of a second
later, and observers see a single spot moving from the first place to the second. Paul Kolers and
Michael von Grünau ([1976](../sources/kolers-vongrunau-1976.md)) found that the spot seems to change colour
abruptly at about the midpoint of its path. The experiments answered a question from Nelson Goodman,
who put the puzzle this way: how can the visual system fill in the spot at the places and times
between the two flashes *before* the second flash has occurred ([Goodman,
1978](../sources/goodman-1978.md), p. 73)? At the midpoint the system cannot yet know that the spot will be green, or where it
is headed.

**Cutaneous rabbit.** Frank Geldard and Carl Sherrick ([1972](../sources/geldard-sherrick-1972.md))
delivered a few quick taps at the wrist followed by a few near the elbow. Subjects did not feel two
clusters. They felt a run of evenly spaced taps hopping up the arm, as if a small animal were running
along it, including at places between the stimulators where nothing touched the skin. Where the
second tap is felt depends on taps that come after it.

**Flash-lag.** When a brief flash is shown exactly in line with a moving object, the flash appears to
lag behind the object. Eagleman and Sejnowski ([2000](../sources/eagleman-sejnowski-2000.md)) showed that
changing the object's motion *after* the flash changes where the object is seen at the moment of the
flash. They concluded that what is perceived as happening at the flash depends on motion signals
gathered over roughly the following 80 milliseconds.

### Rival interpretations

All parties agree on the data. They disagree about what happens in experience at the earlier moment.

The disagreement is easiest to state in the vocabulary of signal processing, which Rick Grush
([2005](../sources/grush-2005.md)) brought to the problem. A *filter* estimates the state of a system at
time *t* using data up to *t*. A *smoother* estimates the state at some earlier time using data that
arrived later, and a *fixed-lag smoother* always estimates the state a fixed interval in the past.
A *predictor* estimates a future state.

On a **delay** reading, conscious experience lags behind the stimulus. The brain waits a short while,
collects the later input, and only then commits to a single coherent version of events, so nothing
false is ever experienced. Rajesh Rao, David Eagleman and Terrence Sejnowski
([2001](../sources/rao-eagleman-sejnowski-2001.md)) proposed that the visual system works as a fixed-lag
smoother with a lag of about 100 milliseconds, so that perception of an event "is not online but
rather is delayed" until information from the immediate future is in. Grush objects that this keeps a
single definitive version of each moment, merely shown late, which makes it closer to the "Cartesian
theater" that Dennett attacked than its authors suppose ([Grush, 2005](../sources/grush-2005.md),
pp. 193–194). He also argues that such a delay would have to be imposed on all perception all the
time, which is not a free assumption ([Dainton, SEP](../sources/sep-consciousness-temporal.md)).

On a **revision** reading, the earlier moment is first experienced one way and the record is then
rewritten. Grush's own proposal, which he calls a *moving window* emulator and which is also known as his
*trajectory estimation model*, combines all three operations. At every moment the system maintains
an estimate of what the perceived process was doing over a short window reaching from slightly in
the past to slightly in the future, built on the control-theory technique known as the Kalman
filter. As new input arrives it may rewrite its estimate of what happened at an earlier moment.
In the rabbit case, the second tap is first experienced at the wrist and then re-placed further up
the arm, and only the revised version survives to be reported. Because an estimate of the present
exists at the present, Grush argues, perception is not simply late, and the model makes precise the
"multiple drafts" that Dennett described only by metaphor ([Grush, 2005](../sources/grush-2005.md),
pp. 194–196).

Daniel Dennett and Marcel Kinsbourne ([1992](../sources/dennett-kinsbourne-1992.md)) call these the
*Stalinesque* option (a staged show trial, doctored before it reaches consciousness) and the
*Orwellian* option (history rewritten afterwards). They argue that at time scales this short no
evidence, not even the subject's own, could tell the two apart, and that the question therefore has
no answer. The lesson they draw is that there is no single place or moment in the brain where
contents "become conscious", and that the brain need not experience events in the order they occur
as long as it represents that order correctly
([time-represented-vs-time-of-representing](time-represented-vs-time-of-representing.md)). Critics reply that if experience is a real
phenomenon, there is a fact about what was experienced at the earlier moment, whether or not anyone
can find it out.

### A comparison with trading systems

The same problem arises in any engineered system that must act on a stream of signals arriving with
different delays. Financial backtesting offers a useful contrast. A trading model that is allowed to
see data from after the moment it is supposed to decide (*lookahead bias*) appears to predict better
than it really could. Postdiction is not an error of this kind, because perception is not trying to
predict the moment it reports, only to describe it. Drawing on a slightly later window is legitimate
for a description, provided that the experience is either delayed until the window closes or revised
once it does. Those two conditions are the delay reading and the revision reading again.

### Why it matters

Postdiction bears on several questions in the philosophy of mind. It tests models of *temporal
experience*, the way we seem to experience change and succession directly rather than inferring them
from a series of snapshots ([Dainton, SEP](../sources/sep-consciousness-temporal.md)). It extends the
[binding-problem](binding-problem.md) across time: the brain must decide not only which features belong to one
object but which signals belong to one moment. It also bears on the
[unity of consciousness](unity-of-consciousness.md), since a unified experience at a given
moment turns out to be assembled from information that arrived over an interval.

### In plain terms

Your brain does not show you the world the instant light or touch reaches you. It waits a split
second and uses what happens next to decide what you "saw". Flash a red dot and then a green dot
nearby, and you see one dot gliding across and turning green halfway, even though your brain could
not have known about the green dot when the glide supposedly started. Scientists and philosophers
argue about whether the brain simply delays your experience until it has all the facts, or shows you
a first draft and quietly edits your memory of it. Some, like Daniel Dennett, think there is no real
difference between those two stories.

### See also

- [time-represented-vs-time-of-representing](time-represented-vs-time-of-representing.md): the distinction that lets the brain represent
  the right order of events without processing them in that order.
- [binding-problem](binding-problem.md): how separately processed features are joined into one percept; postdiction
  is its temporal counterpart.
- [unity-of-consciousness](unity-of-consciousness.md): the togetherness of a subject's experiences at a time, which
  postdiction shows is assembled over an interval.
- [consciousness-is-cerebral-celebrity](../claims/consciousness-is-cerebral-celebrity.md): Dennett's view of consciousness as influence won by
  competing contents, the setting of his Multiple Drafts reading of postdiction.
- [zombie-dualizes-to-volitional-zombie](../claims/zombie-dualizes-to-volitional-zombie.md): a claim pairing input-side postdictive phenomena with
  Libet-style timing findings about the will.
- [hindsight-bias](hindsight-bias.md): a different kind of "after the fact" revision, in which knowing an outcome
  distorts judgments about how foreseeable it was; it concerns belief, not perception.

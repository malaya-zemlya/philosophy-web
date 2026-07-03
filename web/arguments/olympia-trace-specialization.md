---
id: argument-olympia-trace-specialization
type: argument
title: The Klara→Olympia transformation is trace specialization with guarded deoptimization
headword: Olympia as trace specialization
author: mishka
status: contested
tags: [philosophy-of-mind, consciousness, computation, functionalism]
premise: [claim-implementation-requires-counterfactual-structure]
supports: [argument-olympia]
style: encyclopedia
created: 2026-07-02
---

The step at the heart of [olympia](olympia.md) — turning the computer Klara into the replaying
automaton Olympia — can be stated as a purely computational, effectively computable program
transformation, with the physical machinery of troughs, floats, and blocked copies appearing only as
hardware for formally specified items. The transformation is one compiler engineers know well:
*trace specialization*, the technique behind tracing just-in-time compilation, in which a program's
actual execution path on one input is recorded, replayed by branch-free straight-line code, and
protected by guard checks that fall back ("deoptimize") to the original program the moment the data
deviate from the recording. Making this precise yields a theorem — Olympia really does implement
Klara's program, on every input — and so supports the construction step of Maudlin's argument
([maudlin-1989](../sources/maudlin-1989.md)). It also localizes exactly where the argument can be attacked, which is why this
reconstruction is recorded as contested.

The move runs:

1. A physical system implements a program π just in case its states, under some mapping, support
   the full counterfactual structure of π's machine table
   ([implementation-requires-counterfactual-structure](../claims/implementation-requires-counterfactual-structure.md)).
2. The guarded trace machine defined below is provably counterfactually equivalent to π, under an
   explicit state mapping, across *all* inputs (the implementation theorem).
3. Maudlin's physical Olympia realizes the guarded trace machine item for item (the dictionary
   below).

∴ Olympia implements π, and the Klara→Olympia transformation is a syntactic operation computable
from the program and the input alone — no appeal to anything non-computational is needed to build
her.

### The setup: Klara's run as a trace log

Model Klara as a deterministic Turing machine: a finite state set $Q$, tape alphabet $\Sigma$, and
machine table $\delta : Q \times \Sigma \to \Sigma \times \{-1,+1\} \times Q$ encoding the program
π. A *configuration* is a triple $(S, a, T)$: current state, head address $a \in \mathbb{Z}$, and
tape contents $T : \mathbb{Z} \to \Sigma$. One step: if $\delta(S, T(a)) = (w, d, S')$, the machine
writes $w$ at $a$, moves to $a + d$, and enters $S'$ — the next configuration is
$(S',\, a+d,\, T[a \mapsto w])$.

Fix the input tape $R$ (encoding the input $r$) and run Klara from $(S_0, a_0, R)$ for the $N$ steps
of the episode of interest, obtaining configurations $(S_t, a_t, T_t)$ for $t = 0, \dots, N$.
Recording every memory access gives the **trace log**

$$\Lambda \;=\; \big\langle\, (S_t,\; a_t,\; v_t,\; w_t,\; d_t) \,\big\rangle_{t=0}^{N-1},$$

where $v_t = T_t(a_t)$ and $(w_t, d_t, S_{t+1}) = \delta(S_t, v_t)$, together with the terminal
pair $(S_N, a_N)$. Here $a_t$ is the address visited at step $t$, $v_t$
the value found there *on arrival* (before that step's write), and $w_t$ the value written. The log
is exactly the "unrolled" run: which cell, which value, at every step.

*Log-consistency lemma.* For each $t$: if $k = \max\{\, j < t : a_j = a_t \,\}$ exists then
$v_t = w_k$, otherwise $v_t = R(a_t)$. (Induction on $t$: the tape changes only at written
addresses, $T_{j+1} = T_j[a_j \mapsto w_j]$, so the value met at $a_t$ is the last value written
there, or the input value if the cell is untouched.) So the log never needs to be checked for
coherence — it inherits it from being a genuine run.

### The transformation

Klara's step $t$ is a **branch**: *in state $S_t$, read address $a_t$, and do one of $|\Sigma|$
different things depending on the value found*. The transformation replaces each branch with a
**guarded straight-line command**, using the log to pre-resolve both the branch and everything
downstream of it:

$$\begin{aligned}
&\textbf{for } t = 0, \dots, N-1: \\
&\quad \texttt{guard}_t:\; \textbf{if } T(a_t) \neq v_t \to \mathrm{DEOPT}(t)\\
&\quad \texttt{write}_t:\; T(a_t) := w_t\\
&\mathrm{DEOPT}(N)
\end{aligned}$$

where $\mathrm{DEOPT}(t)$ means: shut the straight-line executor down and start a dormant full copy
of Klara in configuration $(S_t,\, a_t,\, \text{current tape})$. The three ingredients of Klara's
step — state, address, read value — are deleted from the *program* and reappear as *data*: $S_t$
labels the deoptimization target, $a_t$ becomes the guard's address, $v_t$ becomes the guard's
expected value. The **bare armature** is this program with the guards deleted: branch-free writes
that never read the tape at all.

The state mapping σ (Maudlin's own definition, restated): *the system is in machine state $S$ iff
either an awakened copy of Klara is in state $S$, or no copy is awake and the executor is at stage
$t$ with $S = S_t$.*

The dictionary to Maudlin's hardware is exact:

- **Time-indexing of memory** — re-index cells by step, so cell $t$ *is* the access $a_t$ — is the
  reordering of the troughs into visit order. The index map $t \mapsto a_t$ is not injective; its
  fibers $\{\, i, j : a_i = a_j \,\}$ are precisely the trough-classes joined by pipes
  (bi-location). Computationally the reordering is an inessential change of coordinates, needed only
  so that the *physical* executor can be dumb — an armature moving uniformly rightward, addressing
  by position rather than by lookup.
- $\texttt{write}_t$ — the armature's drain-rods and hose at trough $t$.
- $\texttt{guard}_t$ — the latched float at trough $t$, preset to $v_t$ and released as the armature
  arrives, *before* the write (Maudlin's fn. 7 fixes exactly this ordering).
- $\mathrm{DEOPT}(t)$ — the chain from float $t$ to the wooden block of the Klara-copy frozen in
  state $S_t$ with its head at trough $t$; the return chain that kills the armature enforces
  "guard before write". $\mathrm{DEOPT}(N)$ is the final copy, started when the armature completes
  its trip. One dormant copy per guard plus the completion copy — Maudlin's $N+2$ machines.

### The implementation theorem

**Theorem.** *For every initial tape $T_0$ — not just $R$ — the guarded trace machine and Klara,
started alike in $S_0$ with head at $a_0$, pass through the same sequence of machine states (under
σ) and perform the same sequence of tape operations (same addresses, same values, same order). In
particular they compute the same function and halt in the same configuration.*

**Proof (summary).** The proof is an induction along the recorded run; the full formal version is
set out in the appendix that closes this entry. So long as every guard has passed, a step-by-step
invariant holds: the trace machine's tape is identical to the tape Klara herself would have produced
on $T_0$, and Klara's state and head position agree with the log. A passing guard means Klara, too,
would be reading the logged value at that step, so determinism forces her to make exactly the logged
transition — the very write the armature performs — and the invariant carries over to the next step.
If every guard passes, the completion copy wakes in precisely Klara's final configuration and
continues her run. If some guard fails first, it fails *before* that step's write, so the awakened
copy stands in precisely the configuration Klara herself would occupy at the first point of
divergence, and determinism does the rest: identical configurations have identical futures. Either
way, every write and every mapped state coincides with Klara's own run.

Three corollaries carry the philosophical weight:

- **Implementation.** Under σ, the system's states satisfy every counterfactual of the machine
  table across the whole input space — precisely the criterion of premise 1. Olympia implements π.
- **Triviality of the bare armature.** Delete the guards and the write sequence
  $\langle (a_t, w_t) \rangle$ is fixed independently of the tape: the guard-free machine computes a
  constant function, exactly Maudlin's observation (fn. 6 of [maudlin-1989](../sources/maudlin-1989.md)) that the armature
  alone instantiates only a trivial program.
- **Effectiveness.** The whole transformation is computable from $(\pi, r)$ alone: run π on $r$,
  record $\Lambda$, emit the guarded program and the deoptimization table. Building Olympia requires
  nothing but the trace log.

On the input $r$ itself, no guard ever fires and no $\mathrm{DEOPT}$ executes: the entire
counterfactual apparatus is, in compiler vocabulary, *dynamically unused* on that run. Maudlin's
"physically inert" machinery is the hardware shadow of this fact — specialization converts live
branches into statically present but (on the training input) never-triggered fallbacks.

### Inference form and weakest premise

The inference is deductive; the theorem itself is not in dispute. What the formalization does is
force any attack on [olympia](olympia.md)'s construction step to land on one of the bridge premises,
and the weakest is **premise 3's inertness gloss** — the reading of the guards as *no activity*.
In the computational statement, $\texttt{guard}_t$ is an **executed instruction on every run,
including the actual one**: at each step the tape value at $a_t$ is read and compared with $v_t$,
and the check *passes* — an event, not an absence. The triviality corollary shows the guards are
ineliminable: remove them and implementation provably collapses into the constant machine. So all
of the input-reading that π requires is being done, on the actual run, by the guards. Maudlin's
hardware makes a passing check *look* like inactivity — a latched float, released, sitting
motionless in the very water level it tests — but the supervenience step of his argument needs "no
motion" to entail "no relevant physical activity", and the formal restatement exposes that
identification as a substantive further premise rather than an observation. A float testing a
trough and finding the expected level is arguably a null-result measurement, physically realized by
the water's support of the float; whether that counts as the system "reading its tape" is exactly
what the argument must settle, and the trace-specialization framing suggests it cannot be settled
by inspection. This is why the node is recorded as contested.

Two further, lesser attack points: the state mapping σ is disjunctive ("an awakened copy is in $S$,
*or* the armature is at stage $t$…"), inviting the observer-relativity worry pressed by
[decomposition-indeterminacy](decomposition-indeterminacy.md); and the counterfactual support is *parasitic* — carried by
$N+2$ embedded whole copies of the original machine, so one may ask whether Olympia is a new
implementation of π at all rather than a warehouse of blocked Klaras with a mechanical replayer in
front.

### Appendix: proof of the implementation theorem

Write $(S'_t, a'_t, T'_t)$ for Klara's run on $T_0$, and $T^{O}_t$ for the trace
machine's tape after $t$ completed writes. Let $t^\ast$ be the least $t < N$ at which
$\texttt{guard}_t$ fails, i.e. $T^{O}_t(a_t) \neq v_t$; set $t^\ast = N$ if every guard passes.

Establish by induction the invariant $I(t)$, for $0 \le t \le t^\ast$:

$$I(t):\quad T^{O}_t = T'_t,\;\; S'_t = S_t,\;\; a'_t = a_t .$$

*Base.* $I(0)$ is immediate: both machines start on the same tape $T_0$ in state $S_0$ at address
$a_0$.

*Step.* Assume $I(t)$ with $t < t^\ast$. Since $t < t^\ast$, $\texttt{guard}_t$ passes:
$T^{O}_t(a_t) = v_t$. By $I(t)$, Klara-on-$T_0$ is in state $S_t$ with head at $a_t$ reading
$T'_t(a_t) = T^{O}_t(a_t) = v_t$ — the logged state reading the logged value. Determinism of
$\delta$ then forces the logged transition $\delta(S_t, v_t) = (w_t, d_t, S_{t+1})$: Klara writes
$w_t$ at $a_t$, moves to $a_t + d_t = a_{t+1}$, and enters $S_{t+1}$. The trace machine's
$\texttt{write}_t$ makes the identical write. Hence

$$\begin{aligned}
T^{O}_{t+1} &= T^{O}_t[a_t \mapsto w_t]\\
            &= T'_t[a_t \mapsto w_t] = T'_{t+1},\\
S'_{t+1} &= S_{t+1}, \quad a'_{t+1} = a_{t+1},
\end{aligned}$$

which is $I(t+1)$. Moreover the two machines' step-$t$ activity coincides: the same state under σ,
the same address, the same write.

*Case 1: $t^\ast = N$ (all guards pass).* $I(N)$ holds, so when the executor completes,
$\mathrm{DEOPT}(N)$ awakens a copy of Klara in configuration
$(S_N, a_N, T^{O}_N) = (S'_N, a'_N, T'_N)$ — Klara's own configuration at step $N$. A duplicate of
Klara governed by the same $\delta$, started in the same configuration, runs step-for-step
identically from there on. Together with the loop steps, the whole computations coincide.

*Case 2: $t^\ast < N$.* Steps $0, \dots, t^\ast - 1$ coincide by the induction, and $I(t^\ast)$
holds. $\texttt{guard}_{t^\ast}$ fires *before* $\texttt{write}_{t^\ast}$ executes, so the tape is
still $T^{O}_{t^\ast} = T'_{t^\ast}$, and $\mathrm{DEOPT}(t^\ast)$ awakens a copy of Klara in
configuration $(S_{t^\ast}, a_{t^\ast}, T'_{t^\ast})$ — by $I(t^\ast)$ exactly the configuration
Klara-on-$T_0$ occupies at step $t^\ast$. Determinism again: identical configurations have identical
futures. So the runs coincide from $t^\ast$ onward too. $\blacksquare$

### In plain terms

Modern language runtimes speed programs up with a trick called a tracing JIT ("just-in-time")
compiler. Watch the program run once on real data and write down everything it actually did; replace
the program with a dumb, super-fast replay of exactly those steps; and at every point where the
replay silently *assumed* something about the data, insert a cheap check — "is this value still
what it was last time?" If a check ever fails, the replay is abandoned and the original, slow,
fully general program takes over from that exact point. Maudlin's Olympia, described in the 1980s,
is this trick built out of water troughs and clockwork: the armature is the dumb replay, the floats
are the checks, and the frozen copies of Klara are the fully general program waiting to take over.
This entry proves the folklore carefully: the replay-plus-checks machine really does behave exactly
like the original computer on *every* possible input, so by the standard definition it really is
running the same program — which is the load-bearing step in Maudlin's
Olympia argument ([olympia](olympia.md)) against the idea that consciousness is just computation.

But the proof also shows the fine print. The checks are not decoration: take them away and the
machine provably stops counting as running the program. And a check *runs* every single time, even
when it passes — asking "is this value what I expected?" and getting *yes* is still asking. Maudlin
needs those passed checks to count as the machine doing *nothing*; stated computationally, they look
instead like the one place where the machine is still genuinely reading its input. That doubt is
why this reconstruction is marked contested.

### See also

- [olympia](olympia.md) — the argument whose Klara→Olympia construction step this entry formalizes
  and (as a matter of implementation) vindicates.
- [implementation-requires-counterfactual-structure](../claims/implementation-requires-counterfactual-structure.md) — the criterion of implementation the
  theorem discharges; premise 1 of this reconstruction.
- [maudlin-1989](../sources/maudlin-1989.md) — the source of the construction; footnotes 6 and 7 of the paper fix,
  respectively, the constant-function reading of the bare armature and the guard-before-write
  ordering the proof relies on.
- [decomposition-indeterminacy](decomposition-indeterminacy.md) — the observer-relativity worry that bears on the
  disjunctive state mapping σ.
- [lookup-table-mind](../concepts/lookup-table-mind.md) — the kindred replay structure: Blockhead pre-computes a table over
  *all* possible inputs, where Olympia records the run on *one* input and guards the rest; both
  raise the question whether canned behaviour plus dispositional backup amounts to the real
  computation.

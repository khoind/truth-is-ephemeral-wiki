---
title: "Lecture 1 — Truth is Ephemeral"
lecture: 1
date: 2023-08-29
pdf_pages: "1–12"
printed_pages: "L1.1–L1.12"
tags:
  - lecture
  - substructural-logic
  - inference
  - state-change
prerequisites:
  - "Basic familiarity with propositions and inference rules"
---

# Lecture 1 — Truth is Ephemeral

## 1. Why this lecture exists

Ordinary mathematical logic is often presented as reasoning about facts that, once established, remain available forever. Computation needs a broader account. A register can contain one value and later another; a permission can be spent; a message can be received; two symbols may be adjacent now and separated after a rewrite. This lecture therefore begins below the level of logical connectives. It asks how the *shape of a state* and the permitted structural laws determine what an inference means.

The progression from sets, to multisets, to sequences isolates three regimes. Structural inference accumulates reusable facts. Linear inference treats occurrences as consumable resources. Ordered inference additionally treats position as significant. Together they explain why “truth is ephemeral” is not a metaphor but a disciplined account of state change.

## 2. Learning objectives

After this lecture, a reader should be able to:

- distinguish a premise, conclusion, schematic variable, rule instance, and proof;
- execute structural, linear, and ordered rules on their appropriate state forms;
- explain exchange, contraction, and weakening without conflating them;
- distinguish saturation of knowledge, saturation of a reachability graph, and quiescence of one state;
- recognize don’t-care and don’t-know nondeterminism;
- explain how substructural rewriting handles the frame problem;
- state an adequacy claim that connects syntax, execution strategy, and intended meaning.

## 3. Dependency map

The lecture’s ideas build in this order:

1. inference rules give local steps;
2. structural laws determine whether a state is a set, multiset, or sequence;
3. the state representation determines whether premises persist, are consumed, or must be adjacent;
4. the chosen search strategy determines whether one normal outcome or all reachable outcomes matter;
5. an adequacy statement connects those formal choices to the modeled problem.

The main companion pages are [Structural Inference](../Concepts/Structural%20Inference.md), [Linear Inference](../Concepts/Linear%20Inference.md), [Ordered Inference](../Concepts/Ordered%20Inference.md), and [Frame Problem and Adequacy](../Concepts/Frame%20Problem%20and%20Adequacy.md).

## 4. Section-by-section reconstruction covering every numbered heading

### 4.1 Section 1 — Introduction

The opening contrasts persistent truth with facts that change during computation. Substructural logic does not discard ordinary logic; it separates regimes in which assumptions may be copied, ignored, exchanged, or must instead be used with resource discipline. The lecture postpones connectives so that the operational force of inference rules can be seen directly.

### 4.2 Section 2 — Structural Inference

A graph-reachability relation illustrates bottom-up inference. An edge supplies a one-step path, and composable paths supply a longer path. Starting from a database of edges, rule instances add consequences until every possible conclusion is already present. The resulting state is saturated.

Because order and multiplicity do not matter, a structural state is a set. Exchange identifies reordered states, and contraction identifies duplicate occurrences. Derived facts retain proof justifications, but saturation is tested on propositions rather than on proofs: a finite fact set may support infinitely many cyclic proofs. Rule scheduling is don’t-care nondeterministic when every fair order produces the same closure.

### 4.3 Section 3 — Linear Inference

Linear inference keeps exchange but denies contraction. A state is therefore a multiset: two occurrences are two resources. Applying a rule removes the matched premise occurrences and inserts its conclusions. Multiple or zero conclusions now make sense because one atomic step can produce several resources or consume resources without replacement.

State change breaks the monotone “one growing database” picture. To analyze all possibilities, one saturates a *set of reachable multisets*. To run a deterministic-enough computation, one may instead choose enabled steps until a quiescent state is reached—provided an adequacy or confluence argument justifies that strategy. The unmatched remainder of the multiset is carried along automatically, which gives an intrinsic answer to the frame problem.

### 4.4 Section 4 — Ordered Inference

Removing exchange as well as contraction makes states sequences. A rule matches a consecutive subsequence and replaces it in place. A cancellation rule with no conclusions can recognize properly nested parentheses: adjacent matching pairs disappear, perhaps exposing a new adjacent pair. Empty and merely stuck are different outcomes; an ill-matched word can be quiescent without reducing to the empty sequence.

This section also makes adequacy explicit. Rules alone do not say which initial states are legal, whether execution explores one branch or every branch, or how a result should be interpreted. Those are metalevel obligations.

### 4.5 Section 5 — Binary Increment as Ordered Inference

Binary digits, an end marker, and increment tokens form an ordered state. Local rules move a carry leftward across a one, turn a zero into a one, or extend the number at its end marker. Position encodes which bit an increment acts upon. Although two increment tokens can sometimes be processed in different orders, the example is intended for don’t-care execution to a quiescent digit string. Regular-expression descriptions specify legal inputs, legal intermediate forms, and finished outputs.

### 4.6 Section 6 — Blocks World as Linear Inference

The planning example represents the robot hand and block configuration by linear propositions. A tempting negative premise—“nothing is on this block”—would inspect the unmatched remainder and destroy the locality that makes linear rewriting modular. The repair is to represent that condition positively with a maintained resource such as `clear(x)`.

Picking up and putting down then consume exactly the facts that cease to hold and produce exactly the facts that begin to hold. The example also exposes another metalevel issue: the rules preserve sensible configurations only when supplied a well-formed initial state. Characterizing physical possibility is separate from merely listing transition rules.

### 4.7 Section 7 — Summary

The final section compares the regimes. Structural states are sets and inference grows knowledge. Linear states are multisets and inference rewrites resources. Ordered states are sequences and rewrite sites must be consecutive. Linear and ordered inference are substructural because they deny contraction, and ordered inference additionally denies exchange. Either substructural regime may support exhaustive reachability or don’t-care reduction, but the intended strategy must be stated.

## 5. Formal core (rules/judgments/theorems, with each symbol explained)

An inference rule has the schematic form

$$
\frac{P_1\quad\cdots\quad P_m}{Q_1\quad\cdots\quad Q_n}\;r.
$$

Here $r$ names the rule; each $P_i$ is a premise pattern; each $Q_j$ is a conclusion pattern; and schematic variables inside the patterns are instantiated consistently when the rule is applied. A zero-premise rule creates facts. In substructural inference a zero-conclusion rule consumes resources.

For **structural inference**, a state $S$ is a set. A ground instance of $r$ is enabled when $\{P_1,\ldots,P_m\}\subseteq S$, and its result is

$$S' = S\cup\{Q_1,\ldots,Q_n\}.$$

Exchange and contraction are expressed by $P,Q=Q,P$ and $P,P=P$. A state is saturated when every enabled rule has all its conclusions already in $S$.

For **linear inference**, a state $\Delta$ is a multiset. If $\uplus$ denotes multiset union and

$$\Delta=R\uplus\{P_1,\ldots,P_m\},$$

then one step produces

$$\Delta'=R\uplus\{Q_1,\ldots,Q_n\}.$$

$R$ is the unmatched frame. It is preserved without being named in the rule. Multiplicity matters: matching two copies of $P$ requires two occurrences.

For **ordered inference**, a state $\Omega$ is a finite sequence. If concatenation is written by juxtaposition and

$$\Omega=\Omega_L\,P_1\cdots P_m\,\Omega_R,$$

then the step is

$$\Omega'=\Omega_L\,Q_1\cdots Q_n\,\Omega_R.$$

$\Omega_L$ and $\Omega_R$ are the unchanged left and right frames. The premises must be adjacent and in the displayed order.

Write $X\longrightarrow X'$ for one step and $X\longrightarrow^{*}Y$ for zero or more steps. A state $Y$ is **quiescent** when no $Y'$ satisfies $Y\longrightarrow Y'$. A collection $R$ of states is reachability-saturated when it contains the initial state and is closed under $\longrightarrow$.

## 6. Operational/computational reading

A structural rule behaves like a monotone database clause: firing it records a consequence without invalidating its inputs. A linear rule behaves like an atomic transaction over a multiset: matched resources are debited, produced resources are credited, and unrelated resources remain. An ordered rule behaves like a local string rewrite: it performs the same transaction but only at a contiguous position.

The scheduler is not supplied by the rule notation. Don’t-care execution commits to one enabled step because all permitted choices are observationally equivalent for the stated goal. Don’t-know execution preserves alternatives because different choices may reach genuinely different states. See [Nondeterminism Dont-Care vs Dont-Know](../Concepts/Nondeterminism%20Dont-Care%20vs%20Dont-Know.md) and [State Saturation and Quiescence](../Concepts/State%20Saturation%20and%20Quiescence.md).

## 7. Worked derivation or trace in original notation and prose

Consider a tiny fabrication system with resources `ore`, `fuel`, `ingot`, and `stamp`:

$$
\frac{\mathit{ore}\quad\mathit{fuel}}{\mathit{ingot}}\;\mathsf{smelt}
\qquad
\frac{\mathit{ingot}\quad\mathit{stamp}}{\mathit{plate}}\;\mathsf{press}.
$$

Begin with the linear state

$$\Delta_0=\mathit{ore},\mathit{fuel},\mathit{stamp},\mathit{ticket}.$$

1. `smelt` matches `ore` and `fuel`. The frame is `stamp, ticket`, so
   $$\Delta_1=\mathit{ingot},\mathit{stamp},\mathit{ticket}.$$
2. `press` matches `ingot` and `stamp`. The frame is now `ticket`, so
   $$\Delta_2=\mathit{plate},\mathit{ticket}.$$
3. No rule matches $\Delta_2$, so it is quiescent.

The trace demonstrates two points. Premises disappear rather than remaining true, and `ticket` survives without any frame axiom. If the same tokens formed an ordered state `ore fuel stamp ticket`, both steps would work; in `fuel stamp ore ticket`, `smelt` would fail because its premises are not adjacent in the required order.

## 8. Conceptual synthesis

Substructural inference makes context management part of meaning. The difference between a database fact, an inventory item, and a symbol at a particular position is not encoded by changing the proposition alone; it is encoded by the algebra of the whole state. Exchange erases order, contraction erases multiplicity, and weakening permits irrelevance. Denying a structural principle creates observable information.

This perspective also separates three layers that should remain distinct: rules describe local transitions; an execution policy selects or explores transitions; an adequacy theorem says that those formal executions correspond exactly to the intended domain. [Exchange Contraction and Weakening](../Concepts/Exchange%20Contraction%20and%20Weakening.md) develops the structural layer in detail.

## 9. Common confusions and failure modes

- **Calling a multiset a set.** In a multiset, $P,P$ provides two consumable occurrences; it is not equal to $P$.
- **Treating linear premises as tests.** A matched premise is consumed unless a conclusion explicitly restores it.
- **Assuming ordered matching can skip symbols.** Ordered premises must occupy one contiguous segment.
- **Equating quiescence with success.** A malformed parenthesis sequence may be stuck but nonempty.
- **Calling one state “saturated” in a changing system.** Exhaustive linear search saturates the collection of reachable states, not an individual state of knowledge.
- **Leaving the scheduler implicit.** Don’t-care and don’t-know interpretations answer different questions.
- **Using a negative side condition over the whole state.** Such a condition can break the local frame behavior of linear rules.

## 10. Self-test questions with concise answers

1. **Why can structural reachability ignore duplicate facts?** Because contraction identifies repeated occurrences, so presence, not multiplicity, matters.
2. **What changes when contraction is denied?** Occurrences become countable resources, and rule application must consume the matched occurrences.
3. **What changes when exchange is also denied?** Relative order becomes observable and rule premises must match consecutively.
4. **Can a quiescent state be incorrect?** Yes. Quiescence only says no rule applies; adequacy determines whether that state represents success.
5. **Where is the frame in a linear step?** It is the unmatched remainder $R$, carried unchanged from the old state to the new one.
6. **Why might proofs be infinite in number while facts are finite?** Cyclic inference can generate distinct justifications for an already-known proposition.

## 11. Related concept pages

- [Structural Inference](../Concepts/Structural%20Inference.md)
- [Linear Inference](../Concepts/Linear%20Inference.md)
- [Ordered Inference](../Concepts/Ordered%20Inference.md)
- [Exchange Contraction and Weakening](../Concepts/Exchange%20Contraction%20and%20Weakening.md)
- [State Saturation and Quiescence](../Concepts/State%20Saturation%20and%20Quiescence.md)
- [Frame Problem and Adequacy](../Concepts/Frame%20Problem%20and%20Adequacy.md)
- [Nondeterminism Dont-Care vs Dont-Know](../Concepts/Nondeterminism%20Dont-Care%20vs%20Dont-Know.md)

## 12. Source trail (lecture, numbered sections, printed-page range, PDF-page range)

Primary source: Frank Pfenning, *Truth is Ephemeral*, Lecture 1, August 29, 2023.

| Numbered section | Printed pages | PDF pages |
|---|---:|---:|
| 1. Introduction | L1.1 | 1 |
| 2. Structural Inference | L1.2–L1.3 | 2–3 |
| 3. Linear Inference | L1.4–L1.5 | 4–5 |
| 4. Ordered Inference | L1.5–L1.7 | 5–7 |
| 5. Binary Increment as Ordered Inference | L1.7 | 7 |
| 6. Blocks World as Linear Inference | L1.8–L1.9 | 8–9 |
| 7. Summary | L1.9–L1.10 | 9–10 |
| References | L1.10–L1.12 | 10–12 |

## 13. Previous/next navigation

Previous: none — this is the first lecture.

Next: [Lecture 2 — From Inference to Logical Connectives](Lecture%2002%20-%20From%20Inference%20to%20Logical%20Connectives.md)

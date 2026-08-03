---
title: "Linear Inference"
aliases:
  - "multiset rewriting"
  - "resource-sensitive inference"
tags:
  - concept
  - linear-logic
  - state-change
source_lectures:
  - 1
  - 2
prerequisites:
  - "Inference rules"
  - "Multisets"
related:
  - "Structural Inference"
  - "Ordered Inference"
  - "Frame Problem and Adequacy"
---

# Linear Inference

## 1. One-sentence definition

**Linear inference is multiset rewriting in which a rule atomically consumes the matched premise occurrences, produces its conclusion occurrences, preserves the unmatched remainder, and treats order as irrelevant but multiplicity as significant.**

## 2. Why the concept is needed

Persistent facts cannot faithfully express a changing inventory, an exclusive permission, or a message that may be received once. Linear inference makes the lifetime of each occurrence explicit. A premise is not merely inspected; it is part of the old state that the transition replaces. This gives a compact account of local state change and prevents accidental reuse.

It also solves a modularity problem. A transition names only what changes. Unrelated resources survive as an implicit frame, even when the system is extended with new resource kinds. That connection is developed in [Frame Problem and Adequacy](Frame%20Problem%20and%20Adequacy.md).

## 3. Intuitive model

**Intuition.** Treat propositions as physical tokens in a bag. A rule takes a specified handful out and puts another handful in. The bag has no left-to-right order, but two blue tokens are different capacity from one blue token. The model is intuitive only: formally, occurrences are elements of a multiset and a transition is defined by multiset subtraction and union.

## 4. Formal core

Let $P_i$ and $Q_j$ be ground propositions and let

$$r=\frac{P_1\quad\cdots\quad P_m}{Q_1\quad\cdots\quad Q_n}$$

be an instantiated rule. A linear state $\Delta$ is a finite multiset. Write $\uplus$ for multiset union. The rule is enabled exactly when there is a remainder $R$ such that

$$\Delta=R\uplus[P_1,\ldots,P_m],$$

where brackets emphasize a multiset with the displayed occurrences. Firing $r$ yields

$$\Delta'=R\uplus[Q_1,\ldots,Q_n].$$

$R$ is the **frame**: resources not mentioned by the rule. Exchange holds, so $P,Q=Q,P$. Contraction does not: $P,P\neq P$ in general. A rule may have several conclusions or none. Several conclusions are one atomic production event, not separate rules; zero conclusions mean pure consumption.

Write $\Delta\longrightarrow_r\Delta'$ for one firing and $\longrightarrow^*$ for its reflexive-transitive closure. The reachable set from $\Delta_0$ is

$$\mathrm{Reach}(\Delta_0)=\{\Delta\mid\Delta_0\longrightarrow^*\Delta\}.$$

A single $\Delta$ is quiescent if it enables no rule. A searched collection is saturated if it is closed under all one-step successors.

In the sequent $\Delta\vdash A$, every occurrence in $\Delta$ must be accounted for. Identity is exactly $A\vdash A$, not $\Delta,A\vdash A$.

## 5. How to use/read it

To execute a rule, find the required multiplicities anywhere in the multiset, remove exactly those occurrences, insert all conclusions together, and leave the frame unchanged. To analyze a planning problem, retain every distinct successor: this is don’t-know nondeterminism. To compute a result under a confluence guarantee, select any enabled step until quiescence: this is don’t-care nondeterminism.

When reading a rule, ask four questions: Which facts are consumed? Which are produced? Which facts merely survive in the frame? Does the intended question require one outcome or all reachable outcomes?

## 6. Worked example

A repair bench has tokens `broken`, `kit`, `tested`, `fixed`, and `receipt`:

$$
\frac{\mathit{broken}\quad\mathit{kit}}{\mathit{fixed}}\;\mathsf{repair}
\qquad
\frac{\mathit{fixed}}{\mathit{tested}\quad\mathit{receipt}}\;\mathsf{inspect}.
$$

Start with

$$\Delta_0=[\mathit{broken},\mathit{kit},\mathit{badge}].$$

1. `repair` consumes `broken` and `kit`. `badge` is the frame. The result is $\Delta_1=[\mathit{fixed},\mathit{badge}]$.
2. `inspect` consumes `fixed` and atomically produces two tokens. The result is $\Delta_2=[\mathit{tested},\mathit{receipt},\mathit{badge}]$.
3. No rule is enabled, so $\Delta_2$ is quiescent.

The badge was never listed in either rule, yet it survived both steps. The kit cannot be reused because its occurrence disappeared in step 1. The two outputs of `inspect` belong to one transition.

## 7. Non-example or boundary case

A read-only catalog fact such as `compatible(modelA,part7)` should normally remain available after arbitrarily many checks. Encoding it as an ordinary linear premise would consume it on the first check unless every rule reproduced it. Such genuinely persistent knowledge belongs in a structural context or under a persistence mechanism such as $!A$.

Another boundary: if location in a queue matters, a multiset loses too much information. [Ordered Inference](Ordered%20Inference.md) is required.

## 8. Key consequences

- Multiplicity represents usable capacity.
- A transition’s footprint is local; the unmatched frame is preserved.
- Multiple conclusions express atomic correlated production.
- State evolution is nonmonotone: old propositions can cease to hold.
- Reachability may branch, cycle, or be infinite.
- Reusable rules and ephemeral state require different logical treatment when rules are internalized as formulas.

## 9. Relations to nearby concepts

[Structural Inference](Structural%20Inference.md) treats propositions as persistent set members; linear inference instead counts and consumes occurrences. [Ordered Inference](Ordered%20Inference.md) has the same consumption discipline but restricts matching to consecutive sequences. [Exchange Contraction and Weakening](Exchange%20Contraction%20and%20Weakening.md) explains why retaining exchange but rejecting contraction yields a multiset. [State Saturation and Quiescence](State%20Saturation%20and%20Quiescence.md) distinguishes exhaustive reachability from reaching one stuck state. [CBA Diagrams and True Concurrency](CBA%20Diagrams%20and%20True%20Concurrency.md) makes resource flow between linear rule instances visible.

## 10. Common mistakes

- Consuming only some premises or producing conclusions in separate steps.
- Treating duplicate propositions as redundant.
- Requiring the rule to mention every fact in the state.
- Assuming a quiescent state is the only reachable outcome.
- Encoding a persistent invariant as an un-reproduced linear premise.
- Treating a rule formula $A\multimap B$ as automatically reusable.

## 11. What to remember

- Linear states are multisets, not sets or sequences.
- Premise occurrences are consumed; conclusion occurrences are produced.
- Exchange holds, contraction does not.
- The unmatched frame survives automatically.
- Search policy—one quiescent run or all reachable states—is part of the specification.

## 12. Source trail

- Lecture 1, §3 “Linear Inference,” printed pp. L1.4–L1.5, PDF pp. 4–5.
- Lecture 1, §6 “Blocks World as Linear Inference,” printed pp. L1.8–L1.9, PDF pp. 8–9.
- Lecture 1, §7 “Summary,” printed pp. L1.9–L1.10, PDF pp. 9–10.
- Lecture 2, §2 “CBA Diagrams for Substructural Proofs,” printed pp. L2.2–L2.3, PDF pp. 14–15.
- Lecture 2, §§5–8, printed pp. L2.6–L2.13, PDF pp. 18–25.


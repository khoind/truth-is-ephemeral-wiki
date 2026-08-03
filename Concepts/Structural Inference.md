---
title: "Structural Inference"
aliases:
  - "set-based inference"
  - "monotone inference"
tags:
  - concept
  - structural-logic
  - inference
source_lectures:
  - 1
  - 2
prerequisites:
  - "Inference rules"
related:
  - "Linear Inference"
  - "Exchange Contraction and Weakening"
  - "State Saturation and Quiescence"
---

# Structural Inference

## 1. One-sentence definition

**Structural inference is rule-based deduction over a set of persistent facts, where rule application adds conclusions without consuming premises and states are identified up to exchange and contraction.**

## 2. Why the concept is needed

Many computations accumulate knowledge: graph reachability, type-constraint closure, database queries, and static analyses derive consequences without invalidating their evidence. Structural inference captures this monotonicity directly. Once a proposition is known, later reasoning may use it again, use it several times, or never use it. The state records *which* facts hold, not how many copies of each fact were derived or where each fact appears.

This regime is also the baseline against which substructural systems are understood. Denying contraction turns occurrences into resources; denying exchange makes order observable. See [Linear Inference](Linear%20Inference.md) and [Ordered Inference](Ordered%20Inference.md).

## 3. Intuitive model

**Intuition.** Think of a shared whiteboard of established facts. A rule may read facts already written and add another fact. Reading does not erase anything. Writing the same sentence twice changes nothing, and rearranging the sentences changes nothing. The whiteboard analogy is only an intuition: formally, a state is a set and a rule instance is a precise condition for extending it.

## 4. Formal core

Let $P,Q,R$ range over ground propositions. Let $x,y,z$ range over objects, and let a rule contain schematic variables that may be instantiated by those objects. A rule has premises above a line and conclusions below it:

$$
\frac{P_1\quad\cdots\quad P_m}{Q_1\quad\cdots\quad Q_n}\;r.
$$

$r$ is the rule name, $P_i$ are premise patterns, and $Q_j$ are conclusion patterns. A structural state $S$ is a set of ground propositions. If one consistent substitution makes every instantiated premise a member of $S$, then the rule instance is enabled and produces

$$S' = S\cup\{Q_1,\ldots,Q_n\}.$$

No $P_i$ is removed. Exchange and contraction appear as state equalities:

$$P,Q=Q,P \qquad P,P=P.$$

The comma denotes set combination. A state $S$ is **saturated** when every enabled ground rule instance concludes only members already in $S$. Equivalently, the immediate-consequence operator $T$ satisfies $T(S)\subseteq S$. Starting with $S_0$, repeated fair application computes the least rule-closed set containing $S_0$ when that process terminates.

Proofs and facts must be distinguished. A fact may have several proof trees, even infinitely many when cycles exist, while it occupies only one position in $S$.

## 5. How to use/read it

Read a structural rule as “whenever all premises are known, the conclusions may also be recorded.” Operationally, choose an enabled instance and add any new conclusions. The scheduling choice is ordinarily don’t-care: different fair orders compute the same least closure. “Fair” means that an instance that remains relevant is not postponed forever.

In a sequent $\Gamma\vdash A$, $\Gamma$ is a structural context and $A$ is the single desired conclusion. Structural identity may be written $\Gamma,A\vdash A$: the unused part $\Gamma$ is harmless because weakening is admitted. This sequent reading internalizes, rather than replaces, the set-based inference reading introduced in Lecture 1.

## 6. Worked example

Suppose a build system records direct prerequisites and wants their transitive closure. Use

$$
\frac{\mathit{needs}(x,y)}{\mathit{depends}(x,y)}\;\mathsf{Direct}
\qquad
\frac{\mathit{depends}(x,y)\quad\mathit{depends}(y,z)}{\mathit{depends}(x,z)}\;\mathsf{Chain}.
$$

Start with

$$S_0=\{\mathit{needs}(app,ui),\mathit{needs}(ui,core),\mathit{needs}(core,log)\}.$$

1. Three `Direct` instances add `depends(app,ui)`, `depends(ui,core)`, and `depends(core,log)`.
2. `Chain` adds `depends(app,core)` and `depends(ui,log)`.
3. A further `Chain` instance adds `depends(app,log)`.
4. Every remaining enabled instance concludes a fact already present, so the state is saturated.

The proof of `depends(app,log)` records a dependency chain. If another derivation reaches the same fact, the fact set remains unchanged even though a second proof exists.

## 7. Non-example or boundary case

Inventory transfer is not faithfully structural. A rule

$$\frac{\mathit{raw}}{\mathit{finished}}$$

would leave `raw` available and permit the same item to be finished repeatedly. If the premise is meant to be spent, the intended model is linear, not structural. A second boundary is an unbounded generator such as $\mathit{nat}(x)\Rightarrow\mathit{nat}(s(x))$: structural inference remains meaningful, but saturation is not reached in finitely many steps.

## 8. Key consequences

- Knowledge grows monotonically: $S\subseteq S'$ after every step.
- Rule order does not change the least closed fact set under fair execution.
- Duplicate derivations affect proof evidence but not the extensional state.
- Set-based closure can support tabled lookup after saturation.
- Structural rules cannot directly model exclusive ownership or consumable tokens.

## 9. Relations to nearby concepts

[Linear Inference](Linear%20Inference.md) retains exchange but denies contraction, so occurrences are counted and premises are consumed. [Ordered Inference](Ordered%20Inference.md) also denies exchange, so positions matter. [State Saturation and Quiescence](State%20Saturation%20and%20Quiescence.md) distinguishes closure of the structural database from being stuck in a rewriting state. [Exchange Contraction and Weakening](Exchange%20Contraction%20and%20Weakening.md) separates the three structural principles: set behavior directly reflects exchange and contraction, while weakening appears most clearly in hypothetical judgments.

## 10. Common mistakes

- Counting two derivations as two fact occurrences.
- Removing structural premises after firing a rule.
- Declaring saturation while an enabled instance still has a new conclusion.
- Assuming termination merely because inference is monotone.
- Tracking infinitely many proofs when only fact closure is needed.
- Using structural inference for a resource that must not be reused.

## 11. What to remember

- A structural state is a set of persistent facts.
- Rule firing adds; it does not consume.
- Exchange erases order and contraction erases duplicate occurrences.
- Saturation concerns new facts, not new proof trees.
- Fair schedules compute the same least closure when closure is attainable.

## 12. Source trail

- Lecture 1, §1 “Introduction,” printed p. L1.1, PDF p. 1.
- Lecture 1, §2 “Structural Inference,” printed pp. L1.2–L1.3, PDF pp. 2–3.
- Lecture 1, §7 “Summary,” printed pp. L1.9–L1.10, PDF pp. 9–10.
- Lecture 2, §4 “CBA Diagrams for Structural Inference,” printed pp. L2.5–L2.6, PDF pp. 17–18.
- Lecture 2, §5 “Hypothetical Judgments,” printed pp. L2.6–L2.8, PDF pp. 18–20.


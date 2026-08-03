---
title: "Lecture 2 — From Inference to Logical Connectives"
lecture: 2
date: 2023-08-31
pdf_pages: "13–25"
printed_pages: "L2.1–L2.13"
tags:
  - lecture
  - sequent-calculus
  - linear-logic
  - proof-diagrams
prerequisites:
  - "Lecture 1 — Truth is Ephemeral"
  - "Structural, linear, and ordered inference"
---

# Lecture 2 — From Inference to Logical Connectives

## 1. Why this lecture exists

Bare inference rules can compute reachability, but they cannot themselves express the question “if this state were available, could that state be obtained?” Lecture 2 crosses that boundary. It first gives substructural executions a proof representation—CBA diagrams—then internalizes state formation and hypothetical reasoning as logical connectives. The move requires a single-succedent sequent, distinct context disciplines, and a way to make selected linear assumptions persistent.

The result is a bridge from rewriting systems to proof theory: states become contexts, state formers become conjunctions, reachability becomes implication, and reusable rules become modal propositions.

## 2. Learning objectives

After this lecture, a reader should be able to:

- read nodes, rule boxes, wires, and slices in a CBA diagram;
- explain true concurrency as the absence of an imposed order between independent events;
- distinguish linear, ordered, and structural slices;
- read $\Gamma\vdash A$, $\Delta\vdash A$, and $\Omega\vdash A$;
- apply identity and the left/right rules for structural, linear, and ordered conjunction;
- apply structural and linear implication rules bottom-up;
- explain why linear implication alone does not make an encoded rule reusable;
- use $!A$ and its restrictions to represent controlled persistence.

## 3. Dependency map

[Lecture 1](Lecture%2001%20-%20Truth%20is%20Ephemeral.md) supplies three state disciplines and their transitions. This lecture develops two branches from them:

- transitions → proof events → [CBA diagrams and true concurrency](../Concepts/CBA%20Diagrams%20and%20True%20Concurrency.md);
- states → antecedent contexts → conjunction, implication, and persistence.

The branches meet because a proof now records how resources flow while the sequent calculus internalizes that flow as propositions. The structural constraints are summarized in [Exchange Contraction and Weakening](../Concepts/Exchange%20Contraction%20and%20Weakening.md).

## 4. Section-by-section reconstruction covering every numbered heading

### 4.1 Section 1 — Introduction

Proofs already had domain-specific readings in Lecture 1: a path, plan, parse, exchange history, or computation trace. Ordinary proof terms are awkward for rules with several conclusions or none. CBA diagrams instead represent individual proposition occurrences as nodes and rule applications as connecting events. The lecture then identifies the limitation of external reachability questions and motivates logical connectives that can express them inside the object language.

### 4.2 Section 2 — CBA Diagrams for Substructural Proofs

For a linear execution, each premise occurrence flows into a rule box and each conclusion occurrence flows out. A horizontal slice selects the live resources at one stage. Moving a slice past an event replaces that event’s premises by its conclusions. One diagram may compress several sequential schedules, while adding a consume-produce detour yields a genuinely different proof diagram even if the final multiset is unchanged. Identical resources require care because exchanging indistinguishable occurrences should not create a spurious distinction.

### 4.3 Section 3 — CBA Diagrams and True Concurrency

In an ordered increment example, two events can be independent: neither consumes a node produced or consumed by the other. Reversing their execution order then produces the same diagram. This is true concurrency—the proof records causal dependence without inventing an observable total order.

Ordered diagrams add geometric constraints. Wires cannot be freely permuted, and a rule’s premises must become adjacent. A zero-output cancellation event may therefore create a causal dependency by removing intervening symbols; a dashed dependency or empty output marker can make that enabling relation explicit.

### 4.4 Section 4 — CBA Diagrams for Structural Inference

Structural facts persist after supporting an inference, so a slice cannot behave like a linear frontier. It must be upward or ancestor closed: selecting a derived fact also retains the facts earlier in its justification. Multiple proofs of one proposition complicate a fully formal definition, so the lecture offers the construction as a useful picture rather than a completed mathematical theory.

### 4.5 Section 5 — Hypothetical Judgments

Reachability questions have an initial side and a desired final side. Writing $\Delta\longrightarrow\Sigma$ suggests a linear hypothetical judgment, but allowing many formulas on the right makes implication introduction scope assumptions incorrectly. Restricting the succedent to one formula yields sequents: $\Gamma\vdash A$ for structural, $\Delta\vdash A$ for linear, and $\Omega\vdash A$ for ordered logic.

Identity closes a proof when the conclusion is available as an assumption. Linear and ordered identity require the context to be exactly $A$; structural identity may ignore other assumptions because weakening is available. Sequents support forward use of antecedents through left rules and backward decomposition of the desired succedent through right rules.

### 4.6 Section 6 — Internalizing State Formation as Conjunction

The comma or juxtaposition that forms a state becomes a connective. Structural conjunction $A\land B$ allows the same context to prove both components. Linear tensor $A\otimes B$ divides a multiset of resources between its two proofs. Ordered product $A\mathbin{\bullet}B$ divides a sequence at one boundary, sending the prefix to $A$ and suffix to $B$.

The expected algebra follows: all three products associate; structural and linear products commute because exchange is present; only structural conjunction is generally idempotent because contraction is present. The left rules unpack a compound antecedent back into the context discipline it internalizes.

### 4.7 Section 7 — Internalizing Hypothetical Judgments as Implication

Structural implication $A\supset B$ and linear implication $A\multimap B$ turn the sequent relation into a proposition. Their right rules assume $A$ while proving $B$. Their left rules use an implication by first proving its input and then continuing with its output. Structural antecedents can be shared between these premises; linear antecedents must be partitioned.

Inference rules can consequently be encoded as implications between products. A complete coin-exchange proof demonstrates this internalization, but it also exposes a mismatch: an encoded linear implication is consumed after one use, while a metalevel inference rule may fire arbitrarily often.

### 4.8 Section 8 — Persistence as a Modality

One remedy is a mixed context with persistent and ephemeral assumptions. The lecture presents another: the exponential modality $!A$, read “of course $A$.” The proposition $!A$ remains a linear assumption, but special contraction and weakening principles allow it to be copied or discarded, while dereliction exposes one usable $A$.

The right rule is restricted. To prove $!A$, every dependency must itself have the form $!B$; otherwise one ephemeral resource could be smuggled into an arbitrarily duplicable value. Encoded inference rules can be placed under $!$ and then used any required number of times.

## 5. Formal core (rules/judgments/theorems, with each symbol explained)

A **sequent** has an antecedent context to the left of $\vdash$ and exactly one succedent formula to the right:

$$\Gamma\vdash A\qquad \Delta\vdash A\qquad \Omega\vdash A.$$

$A,B,C$ range over formulas. $\Gamma$ is a structural set-like context, $\Delta$ a linear multiset context, and $\Omega$ an ordered sequence context. Commas denote order-insensitive context combination; juxtaposition denotes ordered concatenation. Subscripts such as $\Delta_1$ and $\Omega_R$ distinguish context portions.

Identity is:

$$
\frac{}{\Gamma,A\vdash A}\;\mathsf{id}
\qquad
\frac{}{A\vdash A}\;\mathsf{id}
\qquad
\frac{}{A\vdash A}\;\mathsf{id}.
$$

The extra $\Gamma$ is legal only structurally, by weakening.

Conjunction left rules unpack antecedents:

$$
\frac{\Gamma,A,B\vdash C}{\Gamma,A\land B\vdash C}\land L
\quad
\frac{\Delta,A,B\vdash C}{\Delta,A\otimes B\vdash C}\otimes L
\quad
\frac{\Omega_L A B\Omega_R\vdash C}{\Omega_L(A\mathbin{\bullet}B)\Omega_R\vdash C}\bullet L.
$$

Their right rules construct succedents:

$$
\frac{\Gamma\vdash A\quad\Gamma\vdash B}{\Gamma\vdash A\land B}\land R
\quad
\frac{\Delta_1\vdash A\quad\Delta_2\vdash B}{\Delta_1,\Delta_2\vdash A\otimes B}\otimes R
\quad
\frac{\Omega_1\vdash A\quad\Omega_2\vdash B}{\Omega_1\Omega_2\vdash A\mathbin{\bullet}B}\bullet R.
$$

Thus structural proof branches share $\Gamma$, linear branches partition occurrences, and ordered branches split at a position.

Implication rules are:

$$
\frac{\Gamma,A\vdash B}{\Gamma\vdash A\supset B}\supset R
\qquad
\frac{\Gamma\vdash A\quad\Gamma,B\vdash C}{\Gamma,A\supset B\vdash C}\supset L,
$$

$$
\frac{\Delta,A\vdash B}{\Delta\vdash A\multimap B}\multimap R
\qquad
\frac{\Delta_1\vdash A\quad\Delta_2,B\vdash C}{\Delta_1,\Delta_2,A\multimap B\vdash C}\multimap L.
$$

$A\supset B$ is structural implication; $A\multimap B$ is linear implication. Rules are read bottom-up during proof search.

For persistence:

$$
\frac{\Delta,!A,!A\vdash C}{\Delta,!A\vdash C}\mathsf{contraction}
\quad
\frac{\Delta\vdash C}{\Delta,!A\vdash C}\mathsf{weakening}
\quad
\frac{\Delta,A\vdash C}{\Delta,!A\vdash C}!L
\quad
\frac{!\Delta\vdash A}{!\Delta\vdash !A}!R.
$$

$!A$ marks controlled persistence, and $!\Delta$ means every formula in $\Delta$ is itself banged.

## 6. Operational/computational reading

Left rules consume or expose capabilities already available; right rules describe how to build the requested result. For $\otimes R$, resource splitting is a search choice. For $\bullet R$, the choice is a sequence boundary. For $\land R$, no split occurs because structural assumptions may be reused.

A CBA diagram gives the corresponding event structure. Nodes are resource occurrences or facts, boxes are rule instances, wires are producer-consumer dependencies, and a slice is a legal current state. Two boxes are concurrent when neither lies in the causal past of the other and structural constraints do not create a hidden adjacency dependency.

## 7. Worked derivation or trace in original notation and prose

Linear exchange should make the order of two resources irrelevant. We can derive

$$\cdot\vdash A\otimes B\multimap B\otimes A,$$

where $\cdot$ is the empty linear context.

1. Apply $\multimap R$ bottom-up. It remains to prove $A\otimes B\vdash B\otimes A$.
2. Apply $\otimes L$ to unpack the antecedent. It remains to prove $A,B\vdash B\otimes A$.
3. Apply $\otimes R$, choosing the partition $\Delta_1=B$ for the left output and $\Delta_2=A$ for the right output.
4. Both premises close by identity:

$$
\frac{
  \frac{
    \frac{}{B\vdash B}\mathsf{id}
    \qquad
    \frac{}{A\vdash A}\mathsf{id}
  }{A,B\vdash B\otimes A}\otimes R
}{
  A\otimes B\vdash B\otimes A
}\otimes L
$$

followed by $\multimap R$ at the root. The layout is schematic—the logical dependency is the sequence of rule applications above. The proof succeeds because $\Delta$ admits exchange. Replacing $\otimes$ by ordered $\bullet$ would not in general prove the reversed product.

## 8. Conceptual synthesis

The lecture internalizes two metalevel separators. State combination becomes a conjunction whose behavior remembers the context algebra. Hypothetical reachability becomes an implication whose proof rules remember whether assumptions may be shared or must be divided. Modal $!$ then marks the exceptional linear formulas for which contraction and weakening are restored.

CBA diagrams add a complementary lesson: a proof need not be only a parenthesized sequence of steps. For substructural systems it can be a causal network in which resource flow and independence are visible. See [CBA Diagrams and True Concurrency](../Concepts/CBA%20Diagrams%20and%20True%20Concurrency.md).

## 9. Common confusions and failure modes

- **Using multiple succedents naively.** Implication introduction can accidentally make a new assumption available to unrelated conclusions.
- **Reading sequent rules top-down during proof search.** The displayed rules specify derivability; proof construction here decomposes the conclusion bottom-up.
- **Sharing a linear context across branches.** $\otimes R$ partitions resources; only $\land R$ duplicates contextual availability.
- **Treating an encoded $A\multimap B$ as a reusable rule.** It is a linear formula and is consumed unless persistence is added.
- **Allowing unrestricted $!R$.** A proof of $!A$ may depend only on persistent assumptions.
- **Equating different schedules with different concurrent proofs.** Independent event orders can be two linearizations of one CBA diagram.
- **Forgetting ordered adjacency.** Noncrossing wires alone do not guarantee that a rule was enabled.

## 10. Self-test questions with concise answers

1. **Why use a single succedent?** To keep an assumption introduced for one implication scoped to that conclusion alone.
2. **How does $\otimes R$ differ from $\land R$?** Tensor partitions a linear context; structural conjunction gives the whole context to both premises.
3. **How many candidate ordered splits exist for $n$ antecedents?** $n+1$, one at each boundary including both ends.
4. **What makes two CBA events independent?** Neither depends on resources produced, consumed, or made adjacent by the other.
5. **Why is $!R$ restricted to $!\Delta$?** Otherwise an ephemeral dependency could be duplicated or erased through $!A$.
6. **What does $!L$ do?** It exposes an ordinary $A$ from a persistent-capable assumption $!A$ for one use.

## 11. Related concept pages

- [CBA Diagrams and True Concurrency](../Concepts/CBA%20Diagrams%20and%20True%20Concurrency.md)
- [Exchange Contraction and Weakening](../Concepts/Exchange%20Contraction%20and%20Weakening.md)
- [Structural Inference](../Concepts/Structural%20Inference.md)
- [Linear Inference](../Concepts/Linear%20Inference.md)
- [Ordered Inference](../Concepts/Ordered%20Inference.md)
- [Nondeterminism Dont-Care vs Dont-Know](../Concepts/Nondeterminism%20Dont-Care%20vs%20Dont-Know.md)

## 12. Source trail (lecture, numbered sections, printed-page range, PDF-page range)

Primary source: Frank Pfenning, *From Inference to Logical Connectives*, Lecture 2, August 31, 2023.

| Numbered section | Printed pages | PDF pages |
|---|---:|---:|
| 1. Introduction | L2.1 | 13 |
| 2. CBA Diagrams for Substructural Proofs | L2.2–L2.3 | 14–15 |
| 3. CBA Diagrams and True Concurrency | L2.3–L2.5 | 15–17 |
| 4. CBA Diagrams for Structural Inference | L2.5–L2.6 | 17–18 |
| 5. Hypothetical Judgments | L2.6–L2.8 | 18–20 |
| 6. Internalizing State Formation as Conjunction | L2.9–L2.10 | 21–22 |
| 7. Internalizing Hypothetical Judgments as Implication | L2.10–L2.12 | 22–24 |
| 8. Persistence as a Modality | L2.12–L2.13 | 24–25 |

## 13. Previous/next navigation

Previous: [Lecture 1 — Truth is Ephemeral](Lecture%2001%20-%20Truth%20is%20Ephemeral.md)

Next: Lecture 3 — Cut and Identity Elimination (not authored in this assignment).

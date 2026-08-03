---
title: "Nondeterminism: Don't-Care vs Don't-Know"
aliases:
  - "don't-care nondeterminism"
  - "don't-know nondeterminism"
tags:
  - concept
  - nondeterminism
  - operational-semantics
source_lectures:
  - 1
  - 2
prerequisites:
  - "Reachability"
  - "Quiescence"
related:
  - "State Saturation and Quiescence"
  - "CBA Diagrams and True Concurrency"
  - "Frame Problem and Adequacy"
---

# Nondeterminism: Don't-Care vs Don't-Know

## 1. One-sentence definition

**Don't-care nondeterminism permits an arbitrary enabled choice because the intended observation is choice-independent, while don't-know nondeterminism preserves all choices because different branches may represent different relevant possibilities.**

## 2. Why the concept is needed

Inference rules can leave several next steps enabled without specifying a scheduler. That syntactic fact does not tell us whether alternatives are redundant schedules of one computation or distinct answers of a search problem. The distinction determines the algorithm: commit to one branch, or retain a frontier and explore them all.

It also determines what must be proved. A don’t-care claim needs a property such as confluence, unique observable normal form, or order-independent fixed-point closure. A don’t-know interpretation needs reachability coverage and often duplicate-state detection.

## 3. Intuitive model

**Intuition.** If two clerks can stamp two independent forms, it does not matter which stamp happens first; that is don’t-care scheduling. If a traveler can take a train north or south to different cities, choosing one hides the other possible destination; that is don’t-know branching. The intuition depends on the observation: if timing of the stamps were observable, the first example might no longer be don’t-care.

## 4. Formal core

Let $X\longrightarrow Y$ be a one-step transition relation. A state may have successors $Y_1$ and $Y_2$ with

$$X\longrightarrow Y_1\qquad X\longrightarrow Y_2.$$

Under a **don’t-know** reading, both successors contribute to

$$\mathrm{Reach}(X)=\{Y\mid X\longrightarrow^*Y\}.$$

An exhaustive algorithm expands all newly discovered states until the collection is closed, or continues indefinitely if reachability is infinite.

Under a **don’t-care** reading, an executor may choose one successor and continue. This is justified only relative to an observation $\mathcal O$. A strong sufficient property for terminating systems is unique normal form: whenever $X\longrightarrow^*Q_1$ and $X\longrightarrow^*Q_2$ with both $Q_i$ quiescent, then $Q_1=Q_2$. A weaker specification may require merely

$$\mathcal O(Q_1)=\mathcal O(Q_2).$$

For structural closure, rule applications may occur in different orders, yet every fair schedule reaches the same least saturated fact set when evaluation terminates. “Fair” excludes permanently ignoring a still-productive rule instance.

Don’t-care is not synonymous with deterministic: several transitions may exist. Don’t-know is not epistemic uncertainty inside the object language; it is an operational demand to preserve alternatives.

## 5. How to use/read it

First define the observable result: a final state, acceptance bit, set of reachable plans, or saturated database. Then test whether alternative steps can change that observation.

- If not, state don’t-care execution and cite or prove the relevant independence/confluence property.
- If yes, use a worklist or search tree, retain every distinct successor, and state don’t-know execution.
- If only some steps commute, quotient reorderings of independent events while retaining genuinely different branches; CBA diagrams help express this intermediate structure.

Never infer the policy from the rule set alone. The same relation can support a sampler, an exhaustive analyzer, or a normalizer under different specifications.

## 6. Worked example

Consider two systems.

**Don’t-care system.** Let an ordered state contain independent marked pairs and use

$$aA\to X\qquad bB\to Y.$$

From $aA\,bB$, either rule may fire first:

$$aA\,bB\to X\,bB\to X\,Y,$$

or

$$aA\,bB\to aA\,Y\to X\,Y.$$

The steps touch disjoint consecutive segments and lead to the same quiescent state. For the observation “final sequence,” scheduling is don’t-care.

**Don’t-know system.** Let a linear token `request` enable

$$\mathit{request}\to\mathit{approved}
\qquad
\mathit{request}\to\mathit{rejected}.$$

From `[request]`, consuming the only token commits to `[approved]` or `[rejected]`. Neither result reaches the other, and both are relevant outcomes. A reachability analysis must keep both; an arbitrary single choice is incomplete.

## 7. Non-example or boundary case

Two different schedules ending in the same state do not by themselves prove don’t-care behavior for all inputs. They are one example, not a confluence theorem. Conversely, two distinct final states may still be don’t-care relative to a coarse observation—for instance, if both encode “accepted” and internal layout is intentionally hidden. The adequacy statement must identify the observation.

Unfair structural execution is another boundary: repeatedly selecting a rule that adds nothing while ignoring a productive rule can fail to reach closure even though rule order is otherwise don’t-care.

## 8. Key consequences

- Nondeterminism is classified relative to an intended observation.
- Don’t-care execution can avoid exponential schedule exploration.
- Don’t-know execution computes a set of possible states or witnesses.
- Fairness matters for monotone saturation.
- Confluence or unique normal forms can justify arbitrary reduction choices.
- True concurrency quotients orders of independent events without collapsing real alternatives.

## 9. Relations to nearby concepts

[State Saturation and Quiescence](State%20Saturation%20and%20Quiescence.md) supplies the stopping notions used by the two policies. [CBA Diagrams and True Concurrency](CBA%20Diagrams%20and%20True%20Concurrency.md) represents independent actions once rather than as every possible interleaving. [Frame Problem and Adequacy](Frame%20Problem%20and%20Adequacy.md) requires the policy and observation to be stated in the representation theorem. [Structural Inference](Structural%20Inference.md) usually supports order-independent closure; [Linear Inference](Linear%20Inference.md) and [Ordered Inference](Ordered%20Inference.md) may support either policy depending on the modeled problem.

## 10. Common mistakes

- Calling all rule-choice nondeterminism don’t-care.
- Exploring only one branch of a planning or reachability problem.
- Exploring every interleaving of independent events as if each were a different causal proof.
- Omitting fairness from a structural saturation claim.
- Using “same final state in this example” as a general proof.
- Forgetting that observational equivalence may be weaker than literal state equality.

## 11. What to remember

- Don’t-care: choose one because choices preserve the intended result.
- Don’t-know: keep all because branches may encode distinct results.
- Rules expose choices; the specification classifies them.
- Confluence, unique normal forms, or fixed-point uniqueness justify don’t-care execution.
- Reachability closure is the standard don’t-know objective.

## 12. Source trail

- Lecture 1, §2 “Structural Inference,” printed pp. L1.2–L1.3, PDF pp. 2–3.
- Lecture 1, §§3–4 “Linear Inference” and “Ordered Inference,” printed pp. L1.4–L1.7, PDF pp. 4–7.
- Lecture 1, §§5–6, printed pp. L1.7–L1.9, PDF pp. 7–9.
- Lecture 1, §7 “Summary,” printed pp. L1.9–L1.10, PDF pp. 9–10.
- Lecture 2, §§2–3 “CBA Diagrams for Substructural Proofs” and “CBA Diagrams and True Concurrency,” printed pp. L2.2–L2.5, PDF pp. 14–17.


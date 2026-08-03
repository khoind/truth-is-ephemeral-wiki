---
title: Modes and the Dependence Preorder
aliases: [mode preorder, independence principle]
tags: [modes, preorder, dependence, structural-properties, lecture-11]
source_lectures: ["Lecture 11 - Adjoint Logic"]
prerequisites: [contexts, weakening and contraction]
related: [Adjoint Logic, Adjoint Modalities, Cut Elimination Across Modes]
---

# Modes and the Dependence Preorder

## One-sentence definition

**A mode classifies a proposition’s structural permissions, and the preorder $m\ge k$ says that assumptions at mode $m$ are permitted dependencies of conclusions at mode $k$.**

## Why the concept is needed

Combining substructural logics requires more than labeling formulas “linear” or “structural.” The system must say which layers may depend on which others and ensure that cut cannot smuggle a duplicable conclusion across a nonduplicable dependency. The mode preorder provides the dependency test, while $\sigma$ supplies weakening and contraction permissions.

## Intuitive model

**Intuition.** Modes are trust/usage tiers. A computation at a lower tier may call a higher-tier service, but a higher-tier reusable definition cannot close over a lower-tier one-use resource. The order points from allowed dependency to dependent result, not from “less powerful” to “more powerful.”

## Formal core

A preorder is reflexive and transitive: $m\ge m$, and $m\ge k$ with $k\ge r$ implies $m\ge r$. Distinct modes may satisfy both directions; antisymmetry is not required.

For context $\Delta=B_{\ell_1},\ldots,B_{\ell_n}$, define

$$\Delta\ge m\quad\text{iff}\quad \ell_i\ge m\text{ for every }i.$$

The sequent $\Delta\vdash A_m$ is presupposed well formed only if $\Delta\ge m$. Here $A_m$ is a proposition at mode $m$, and each $B_{\ell_i}$ is an assumption at mode $\ell_i$.

Structural permissions are recorded by

$$\sigma(m)\subseteq\{W,C\},$$

where $W$ authorizes weakening and $C$ contraction. Exchange is implicit in this development. The coherence condition is

$$m\ge k\Longrightarrow\sigma(m)\supseteq\sigma(k).$$

Thus if a lower conclusion may be copied or discarded, every higher-mode dependency used to prove it supports the same operation.

The cut rule makes the order visible:

$$
\frac{\Delta\ge m\ge r\quad\Delta\vdash A_m\quad\Delta',A_m\vdash C_r}
{\Delta,\Delta'\vdash C_r}.
$$

$r$ is the conclusion mode, $m$ the cut-formula mode, and $\Delta,\Delta'$ are multisets.

## How to use/read it

Before deriving anything, annotate every proposition with its intrinsic mode. For a goal $C_r$, reject any assumption whose mode is not $\ge r$. When applying a rule that creates a subgoal at mode $m$, recheck that its allocated context satisfies $\Delta\ge m$. Conditions such as $\Delta\ge m$ on $\to L$ and $\downarrow R$ are proof-search guards, not extra logical premises.

## Worked example

Use three modes $S\ge A\ge L$ with

$$\sigma(S)=\{W,C\},\quad\sigma(A)=\{W\},\quad\sigma(L)=\varnothing.$$

1. A linear conclusion $C_L$ may depend on $S$, $A$, and $L$ assumptions by transitivity and reflexivity.
2. An affine conclusion $B_A$ may depend on $S$ and $A$, but not on $L$ unless $L\ge A$ is separately declared.
3. A structural conclusion $D_S$ may depend only on modes known to be $\ge S$—here just $S$.
4. If a proof of $B_A$ ignores a dependency at $S$, that is allowed because $W\in\sigma(S)$.
5. It may not duplicate an $A$ dependency because $C\notin\sigma(A)$.
6. Monotonicity holds: the higher mode $S$ has all permissions of $A$, and both have all permissions of $L$.

This example shows that dependency and structural strength are coordinated but not collapsed into one Boolean choice.

## Non-example or boundary case

Choose $m\ge k$ with $\sigma(k)=\{W,C\}$ and $\sigma(m)=\varnothing$. A $k$-mode theorem could depend on an $m$-mode linear resource. Contracting the theorem and eliminating the cuts would require two copies of that resource. The proposed mode signature is therefore invalid for the calculus.

Incomparability is not failure: if neither $m\ge k$ nor $k\ge m$, the layers are intentionally independent.

## Key consequences

The preorder determines which mixed cuts exist and which shifts are legal. It recovers the LNL independence principle $S>L$, supports more than two usage regimes, and makes conservative fragments syntactically visible. Monotone structural properties are used critically in multicut reductions.

## Relations to nearby concepts

[Adjoint Logic](Adjoint%20Logic.md) provides the full uniform calculus. [Adjoint Modalities](Adjoint%20Modalities.md) require comparable endpoints. [Cut Elimination Across Modes](Cut%20Elimination%20Across%20Modes.md) shows where $\sigma$ monotonicity repairs duplication created during reduction.

## Common mistakes

- Reversing the dependency reading of $\ge$.
- Assuming incomparable modes can interact through an unindexed coercion.
- Forgetting reflexive dependencies within a mode.
- Treating $\sigma(m)$ as a property of individual formulas rather than the mode.
- Assuming $\{C\}$ or $\{W\}$ modes are forbidden; both are legitimate when coherent.

## What to remember

- $m\ge k$ means $m$-assumptions may support $k$-conclusions.
- Every sequent must satisfy its dependence presupposition.
- $\sigma(m)$ independently records $W$ and $C$.
- Structural permissions grow upward along dependencies.
- A preorder need not be total or antisymmetric.

## Source trail

Lecture 11, §§1–2 and §5, printed lecture pages L11.1–L11.3 and L11.5–L11.6, PDF pages 123–125 and 127–128. See [Lecture 11 - Adjoint Logic](../Lectures/Lecture%2011%20-%20Adjoint%20Logic.md).

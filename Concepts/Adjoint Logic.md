---
title: Adjoint Logic
aliases: [adjoint logical framework, multimode substructural logic]
tags: [adjoint-logic, modes, substructural-logic, lecture-11]
source_lectures: ["Lecture 11 - Adjoint Logic", "Lecture 12 - Focusing"]
prerequisites: [Mixed Linear-Nonlinear Logic, weakening and contraction, cut]
related: [Modes and the Dependence Preorder, Adjoint Modalities, Cut Elimination Across Modes]
---

# Adjoint Logic

## One-sentence definition

**Adjoint logic is a uniform sequent-calculus schema in which every proposition has a mode, modes control structural rules and dependency, and indexed shifts connect propositions at comparable modes.**

## Why the concept is needed

LNL combines two useful logics but duplicates connective rules: structural and linear implication alone require several variants. It also fixes the combination to two regimes. Adjoint logic abstracts the common structure so implication has one right and one left rule at every mode, while a configurable mode preorder can represent linear, affine, strict, structural, modal, or staged fragments together.

## Intuitive model

**Intuition.** A mode is a usage policy and dependency level attached to a type. Rather than inventing a new connective family for each policy, adjoint logic uses one family and checks the policy at the sequent boundary. Indexed shifts are controlled bridges between levels.

## Formal core

Modes are written $m,k,\ell,r$. A proposition $A_m$ has intrinsic mode $m$. The function $\sigma(m)\subseteq\{W,C\}$ records whether weakening ($W$) and contraction ($C$) are allowed; exchange is assumed. Modes carry a preorder $\ge$. The judgment

$$\Delta\vdash A_m$$

is well formed only when $\Delta\ge m$: for every $B_\ell\in\Delta$, $\ell\ge m$. $\Delta$ is a multiset, so structural actions remain explicit.

Representative uniform rules are

$$
\frac{\Delta,A_m\vdash B_m}{\Delta\vdash A_m\to B_m}\;\to R
$$

and

$$
\frac{\Delta\ge m\qquad\Delta\vdash A_m\qquad\Delta',B_m\vdash C_r}
{\Delta,\Delta',A_m\to B_m\vdash C_r}\;\to L.
$$

$\Delta\ge m$ ensures the argument proof may depend only on modes permitted to prove $A_m$. Cut is

$$
\frac{\Delta\ge m\ge r\qquad\Delta\vdash A_m\qquad\Delta',A_m\vdash C_r}
{\Delta,\Delta'\vdash C_r}\;\mathsf{cut}.
$$

Structural rules require $W\in\sigma(m)$ or $C\in\sigma(m)$. Crucially, $m\ge k$ implies $\sigma(m)\supseteq\sigma(k)$: higher dependencies must support every structural behavior required below.

The connective grammar includes $\to,\times,1,\mathbin{\&},\top,+,0$ at each mode plus indexed $\uparrow^m_k A_k$ and $\downarrow^\ell_m A_\ell$.

## How to use/read it

First verify that a sequent is well formed under the preorder. Second apply the connective rule uniformly at the principal proposition’s mode. Third check only the explicit conditions shown by noninvertible rules. Read bottom-up rules as proof search and top-down cuts as composition of providers and clients. A mode configuration instantiates a logic; it is not itself an object-language proposition.

## Worked example

Recover ordinary LNL.

1. Choose modes $S$ and $L$ with $S>L$; reflexivity supplies $S\ge S$ and $L\ge L$, while $L\not\ge S$.
2. Set $\sigma(S)=\{W,C\}$ and $\sigma(L)=\varnothing$.
3. A sequent concluding $A_S$ may contain only $S$-mode assumptions, because an $L$ assumption would require $L\ge S$.
4. A sequent concluding $A_L$ may contain both modes because $S\ge L$ and $L\ge L$.
5. Instantiate uniform $\to$ at $S$ to obtain structural implication and at $L$ to obtain linear implication.
6. The general cut condition yields exactly $SS$, $SL$, and $LL$ cuts; $LS$ is excluded.

Thus one rule schema recovers the duplicated LNL cases.

## Non-example or boundary case

Suppose $m\ge k$, $C\in\sigma(k)$, but $C\notin\sigma(m)$. A proof of an $A_k$ may depend on a resource at $m$; cutting that proof into a context that contracts $A_k$ duplicates the $m$-resource, although its mode forbids contraction. Cut elimination fails. The monotonicity of $\sigma$ is therefore a metatheoretic necessity, not aesthetic bookkeeping.

## Key consequences

Specific mode signatures recover intuitionistic linear logic, LNL, intuitionistic S4, and lax logic. Uniform rules reduce duplication, while mode constraints preserve independence. Adjoint shifts generate comonadic or monadic composites. Cut elimination requires multicut when explicit contraction is present, tying structural permissions directly to normalization.

## Relations to nearby concepts

[Modes and the Dependence Preorder](Modes%20and%20the%20Dependence%20Preorder.md) isolates well-formedness and monotonicity. [Adjoint Modalities](Adjoint%20Modalities.md) explains indexed bridges. [Cut Elimination Across Modes](Cut%20Elimination%20Across%20Modes.md) develops multicut. [Mixed Linear-Nonlinear Logic](Mixed%20Linear-Nonlinear%20Logic.md) is the two-mode instance.

## Common mistakes

- Treating $m\ge k$ as a total order; it is only a preorder.
- Reading the inequality backwards: assumptions at $m$ may support conclusions at $k$ when $m\ge k$.
- Assuming every mode has both weakening and contraction.
- Applying rules to a sequent that violates $\Delta\ge m$.

## What to remember

- Modes own structural policy and dependency.
- Connective rules are uniform across modes.
- Dependence is constrained before proof search begins.
- Structural permissions must be monotone along $\ge$.
- LNL is one instance, not the whole framework.

## Source trail

Lecture 11, §§1–6, printed lecture pages L11.1–L11.7, PDF pages 123–129; Lecture 12, §2, printed pages L12.1–L12.4, PDF pages 132–135. See [Lecture 11 - Adjoint Logic](../Lectures/Lecture%2011%20-%20Adjoint%20Logic.md) and [Lecture 12 - Focusing](../Lectures/Lecture%2012%20-%20Focusing.md).

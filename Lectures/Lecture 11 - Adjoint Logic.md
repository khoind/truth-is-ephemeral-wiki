---
title: "Lecture 11 - Adjoint Logic"
lecture: 11
date: 2023-10-03
pdf_pages: "123-131"
printed_pages: "L11.1-L11.9"
tags:
  - lecture
  - adjoint-logic
  - modes
  - substructural-logic
  - shifts
  - proof-theory
prerequisites:
  - mixed linear-nonlinear logic
  - weakening and contraction
  - cut and identity
  - polarity and shifts
---

# Lecture 11 - Adjoint Logic

## 1. Why this lecture exists

LNL successfully combines structural and linear reasoning, but it hard-codes two modes and duplicates connective rules. Implication alone needs two right rules and three left rules. It also cannot directly describe affine reasoning (weakening without contraction), strict/relevant reasoning (contraction without weakening), or richer combinations of structural disciplines.

Adjoint logic replaces the fixed structural/linear split with a preorder of modes. Each proposition has an intrinsic mode; each mode declares whether it admits weakening and/or contraction; and the preorder controls which assumptions a conclusion may depend on. Connectives then have one uniform pair of rules at every mode, while indexed shifts cross between comparable modes. This both streamlines LNL and provides a schema whose instances include intuitionistic linear logic, LNL, intuitionistic S4, and lax logic.

## 2. Learning objectives

After this lecture, a reader should be able to:

- interpret a mode preorder $m\ge k$ as a permitted dependency;
- use $\sigma(m)$ to determine whether assumptions at mode $m$ may weaken or contract;
- check the well-formedness presupposition $\Delta\ge m$ for a sequent $\Delta\vdash A_m$;
- reconstruct side conditions on cut, implication left, and the shift rules;
- read all uniform logical rules and explain every mode index;
- instantiate the schema as linear logic, LNL, intuitionistic S4, or lax logic;
- distinguish a comonadic shift composite from a monadic one.

## 3. Dependency map

The [independence principle](../Concepts/Modes%20and%20the%20Dependence%20Preorder.md) becomes the general relation $m\ge k$. [Exchange, contraction, and weakening](../Concepts/Exchange%20Contraction%20and%20Weakening.md) become mode-indexed membership tests in $\sigma$. [Shifts between logics](../Concepts/Shifts%20Between%20Logics.md) become [adjoint modalities](../Concepts/Adjoint%20Modalities.md) between arbitrary comparable modes. Uniform connective rules rely on [Polarity and invertibility](../Concepts/Polarity%20and%20Invertibility.md) and [Cut elimination across modes](../Concepts/Cut%20Elimination%20Across%20Modes.md). Specific choices of modes recover [Linear inference](../Concepts/Linear%20Inference.md), [Mixed linear-nonlinear logic](../Concepts/Mixed%20Linear-Nonlinear%20Logic.md), and modal systems explained by [Adjoint modalities](../Concepts/Adjoint%20Modalities.md).

## 4. Section-by-section reconstruction

### 1. Introduction

Adjoint logic addresses two problems simultaneously: remove LNL's rule duplication and generalize beyond exactly two structural disciplines. Exchange is assumed at every mode in this lecture, so antecedents are multisets rather than ordered sequences. Weakening $W$ and contraction $C$ are independently configurable.

This independence matters. A mode with $\{W,C\}$ is structural; a mode with neither is linear; $\{W\}$ gives affine behavior suitable for cancellation or failure because a resource may go unused but not be copied; $\{C\}$ gives strict/relevant behavior suitable for analyses where an argument must be used but may be used more than once. Rust's affine flavor and Haskell strictness analysis are motivating analogies, not exact encodings in the calculus presented here. Ordered logic would require dropping universal exchange and is explicitly left outside this lecture's development.

### 2. Adjoint Logic: The Basics

Every proposition carries a mode. $A_m$ means proposition $A$ is true at mode $m$. A preorder $\ge$ on modes is reflexive and transitive. The assertion

$$
m\ge k
$$

means that a proof of a conclusion at mode $k$ may depend on an antecedent at mode $m$. If $m\not\ge k$, that dependency is forbidden. In the LNL instance, $S>L$: structural assumptions may support linear conclusions, while $L\not\ge S$ prevents linear assumptions from supporting structural conclusions.

The uniform proposition grammar is

$$
A_m ::= P_m
\mid A_m\to B_m
\mid A_m\times B_m
\mid 1_m
\mid A_m\mathbin{\&}B_m
\mid \top_m
\mid A_m+B_m
\mid 0_m
\mid \uparrow^m_k A_k
\mid \downarrow^\ell_m A_\ell.
$$

$P_m$ is atomic. At each mode, $\to$ is implication; $\times$ is multiplicative conjunction; $1_m$ is its unit; $\mathbin{\&}$ is additive conjunction (shown as “N” in the extraction); $\top_m$ is its unit; $+$ is additive disjunction; and $0_m$ is falsehood. The notation intentionally unifies structural $\supset,\land,\lor$ and linear $\multimap,\otimes,\oplus$: behavior arises from the mode's structural permissions, not from separate connective names.

The upshift $\uparrow^m_k A_k$ has result mode $m$ and requires $m\ge k$. The downshift $\downarrow^\ell_m A_\ell$ has result mode $m$ and requires $\ell\ge m$. Superscripts name the upper mode; subscripts name the lower mode.

The structural signature

$$
\sigma(m)\subseteq\{W,C\}
$$

records whether mode $m$ permits weakening and contraction. It must be monotone along dependency:

$$
m\ge k\quad\Longrightarrow\quad\sigma(m)\supseteq\sigma(k).
$$

Intuitively, assumptions allowed to support a less structural conclusion cannot themselves have fewer structural capabilities than that conclusion's mode. More importantly, this is a proof-theoretic requirement: cut elimination fails without it.

A sequent has one form,

$$
\Delta\vdash A_m,
$$

but it carries the presupposition $\Delta\ge m$: for every antecedent $B_\ell\in\Delta$, $\ell\ge m$. This is a well-formedness condition, not an inference rule. Because $\Delta$ is a multiset, weakening and contraction are explicit:

$$
\frac{W\in\sigma(m)\qquad\Delta\vdash C_r}
     {\Delta,A_m\vdash C_r}\;\mathsf{weaken}
\qquad
\frac{C\in\sigma(m)\qquad\Delta,A_m,A_m\vdash C_r}
     {\Delta,A_m\vdash C_r}\;\mathsf{contract}.
$$

Identity is uniform: $A_m\vdash A_m$. Cut requires a mode side condition:

$$
\frac{\Delta\ge m\ge r\qquad
      \Delta\vdash A_m\qquad
      \Delta',A_m\vdash C_r}
     {\Delta,\Delta'\vdash C_r}\;\mathsf{cut}.
$$

$\Delta\ge m$ ensures the proof of the cut formula is well formed; $m\ge r$ ensures the cut formula may be used in the second premise and that dependencies inherited from $\Delta$ can reach the final conclusion. With modes $S>L$, the allowed assignments $(m,r)=(S,S),(S,L),(L,L)$ reproduce exactly LNL's $SS$, $SL$, and $LL$ cuts; $(L,S)$ is excluded.

### 3. Logical Rules

Implication right is uniform and condition-free:

$$
\frac{\Delta,A_m\vdash B_m}{\Delta\vdash A_m\to B_m}\;\to R.
$$

The conclusion's presupposition $\Delta\ge m$ automatically makes the premise well formed. This absence of a side condition agrees with the negative polarity of implication and its right invertibility.

Implication left needs one explicit check:

$$
\frac{\Delta\ge m\qquad
      \Delta\vdash A_m\qquad
      \Delta',B_m\vdash C_r}
     {\Delta,\Delta',A_m\to B_m\vdash C_r}\;\to L.
$$

The conclusion already guarantees $m\ge r$ and $\Delta'\ge r$, but it gives only $\Delta\ge r$, not the stronger $\Delta\ge m$ needed to prove the argument $A_m$. This one side condition subsumes LNL's three implication-left cases.

Multiplicative product and unit need no additional mode checks:

$$
\frac{\Delta\vdash A_m\qquad\Delta'\vdash B_m}
     {\Delta,\Delta'\vdash A_m\times B_m}\;\times R
\qquad
\frac{\Delta,A_m,B_m\vdash C_r}
     {\Delta,A_m\times B_m\vdash C_r}\;\times L,
$$

$$
\frac{}{\cdot\vdash1_m}\;1R
\qquad
\frac{\Delta\vdash C_r}{\Delta,1_m\vdash C_r}\;1L.
$$

$\times R$ partitions the antecedent multiset; $\times L$ decomposes a pair in place. These same rules behave structurally at modes with $W,C$ and linearly at modes without them.

### 4. The Shifts

Mode constraints determine the shift rules. For upshift:

$$
\frac{\Delta\vdash A_k}{\Delta\vdash\uparrow^m_k A_k}\;\uparrow R
\qquad(m\ge k),
$$

$$
\frac{k\ge r\qquad\Delta,A_k\vdash C_r}
     {\Delta,\uparrow^m_k A_k\vdash C_r}\;\uparrow L.
$$

No extra premise is needed on $\uparrow R$: the conclusion says $\Delta\ge m$, and $m\ge k$, so transitivity gives $\Delta\ge k$. The left rule explicitly requires $k\ge r$ because the lower-mode payload must be allowed to support the conclusion. Thus $\uparrow$ remains negative: its right rule is unconstrained beyond the shift's formation condition.

For downshift:

$$
\frac{\Delta\ge\ell\qquad\Delta\vdash A_\ell}
     {\Delta\vdash\downarrow^\ell_m A_\ell}\;\downarrow R
\qquad(\ell\ge m),
$$

$$
\frac{\Delta,A_\ell\vdash C_r}
     {\Delta,\downarrow^\ell_m A_\ell\vdash C_r}\;\downarrow L.
$$

The downshift conclusion guarantees only $\Delta\ge m$, so $\downarrow R$ must demand the stronger $\Delta\ge\ell$ needed for its premise. On the left, the conclusion gives $m\ge r$ and formation gives $\ell\ge m$; transitivity supplies $\ell\ge r$, so no side condition is needed. Hence $\downarrow$ remains positive through left invertibility.

The lecture notes that constraint analysis and expanded identity both support these polarity assignments, but neither informal check substitutes for the full metatheory developed later.

### 5. Specific Logics as Instances of the Adjoint Schema

An instance specifies three things: a set of modes, a preorder, and a structural signature $\sigma$; it may also restrict the grammar available at a mode.

**Intuitionistic linear logic.** Choose $S>L$, with $\sigma(S)=\{W,C\}$ and $\sigma(L)=\varnothing$. Restrict structural propositions to $A_S::=\uparrow^S_L A_L$ and disallow same-mode shifts. Then

$$
!A_L\;\overset{\mathrm{def}}{=}\;\downarrow^S_L\uparrow^S_L A_L.
$$

The structural mode exists only to support reuse of linear propositions.

**LNL.** Use the same two modes and structural properties, but allow the full connective grammar at $S$. Disallow the trivial same-mode shifts $\uparrow^m_m$ and $\downarrow^m_m$. This recovers Lecture 10 while uniform rules replace its duplicated schemas.

**Intuitionistic S4.** Choose validity $V$ above truth $T$, with both modes structural: $\sigma(V)=\sigma(T)=\{W,C\}$. Restrict $A_V::=\uparrow^V_T A_T$ and define

$$
\Box A_T\;\overset{\mathrm{def}}{=}\;\downarrow^V_T\uparrow^V_T A_T.
$$

This composite is a comonad. It captures necessity/validity, but the possibility monad $\Diamond$ does not arise merely as the opposite composite in this instance.

**Lax logic.** Choose truth $T$ above lax truth $X$, with both modes structural, and restrict the lower grammar to $A_X::=\downarrow^T_X A_T$. Define

$$
\bigcirc A_T\;\overset{\mathrm{def}}{=}\;
\uparrow^T_X\downarrow^T_X A_T.
$$

$\bigcirc$ is a strong monad and can represent computations/effects in the sense motivating lax logic. The schema can also combine validity for staged computation, monadic effects, comonadic persistence, and distinct structural policies in a single mode graph.

### 6. Summary

The complete calculus has one sequent form, explicit mode-indexed structural rules, uniform identity and cut, two rules per connective, and two indexed shifts. Side conditions occur exactly where a premise requires a stronger dependency than the conclusion already guarantees. This systematic derivation is the central method: start with a rule's logical shape, read it bottom-up, propagate the sequent presupposition, and add only the missing mode comparisons.

The full rule inventory from the summary figure is reproduced in the Formal core below so that this guide is usable without reopening the notes.

## 5. Formal core

### Modes and well-formed sequents

- $m,k,\ell,r$ range over modes.
- $m\ge k$ means an $m$-mode assumption may support a $k$-mode conclusion.
- $\sigma(m)\subseteq\{W,C\}$ records weakening and contraction; exchange is always assumed.
- $\Delta,\Delta'$ are multisets of mode-annotated propositions.
- $\Delta\ge m$ abbreviates: for every $A_k\in\Delta$, $k\ge m$.
- $\Delta\ge m\ge r$ abbreviates both $\Delta\ge m$ and $m\ge r$.
- $C_r$ is an arbitrary conclusion at mode $r$; the letter $C$ here is a proposition metavariable, while $C\in\sigma(m)$ denotes the contraction permission. Context distinguishes them.

Every displayed sequent $\Delta\vdash A_m$ presupposes $\Delta\ge m$. Shift formation requires $m\ge k$ for $\uparrow^m_k A_k$ and $\ell\ge m$ for $\downarrow^\ell_m A_\ell$.

### Structural, identity, cut, and shift rules

$$
\frac{W\in\sigma(m)\quad\Delta\vdash C_r}{\Delta,A_m\vdash C_r}\;W
\qquad
\frac{C\in\sigma(m)\quad\Delta,A_m,A_m\vdash C_r}{\Delta,A_m\vdash C_r}\;C
$$

$$
\frac{}{A_m\vdash A_m}\;\mathsf{id}
\qquad
\frac{\Delta\ge m\ge r\quad\Delta\vdash A_m\quad\Delta',A_m\vdash C_r}
     {\Delta,\Delta'\vdash C_r}\;\mathsf{cut}
$$

$$
\frac{\Delta\vdash A_k}{\Delta\vdash\uparrow^m_k A_k}\;\uparrow R
\qquad
\frac{k\ge r\quad\Delta,A_k\vdash C_r}
     {\Delta,\uparrow^m_k A_k\vdash C_r}\;\uparrow L
$$

$$
\frac{\Delta\ge\ell\quad\Delta\vdash A_\ell}
     {\Delta\vdash\downarrow^\ell_m A_\ell}\;\downarrow R
\qquad
\frac{\Delta,A_\ell\vdash C_r}
     {\Delta,\downarrow^\ell_m A_\ell\vdash C_r}\;\downarrow L.
$$

### Uniform connective rules

$$
\frac{\Delta,A_m\vdash B_m}{\Delta\vdash A_m\to B_m}\;\to R
\qquad
\frac{\Delta\ge m\quad\Delta\vdash A_m\quad\Delta',B_m\vdash C_r}
     {\Delta,\Delta',A_m\to B_m\vdash C_r}\;\to L
$$

$$
\frac{\Delta\vdash A_m\quad\Delta'\vdash B_m}
     {\Delta,\Delta'\vdash A_m\times B_m}\;\times R
\qquad
\frac{\Delta,A_m,B_m\vdash C_r}
     {\Delta,A_m\times B_m\vdash C_r}\;\times L
$$

$$
\frac{}{\cdot\vdash1_m}\;1R
\qquad
\frac{\Delta\vdash C_r}{\Delta,1_m\vdash C_r}\;1L
$$

$$
\frac{\Delta\vdash A_m\quad\Delta\vdash B_m}
     {\Delta\vdash A_m\mathbin{\&}B_m}\;\mathbin{\&}R
$$

$$
\frac{\Delta,A_m\vdash C_r}{\Delta,A_m\mathbin{\&}B_m\vdash C_r}\;\mathbin{\&}L_1
\qquad
\frac{\Delta,B_m\vdash C_r}{\Delta,A_m\mathbin{\&}B_m\vdash C_r}\;\mathbin{\&}L_2
$$

$$
\frac{}{\Delta\vdash\top_m}\;\top R
\qquad\text{there is no }\top L
$$

$$
\frac{\Delta\vdash A_m}{\Delta\vdash A_m+B_m}\;+R_1
\qquad
\frac{\Delta\vdash B_m}{\Delta\vdash A_m+B_m}\;+R_2
$$

$$
\frac{\Delta,A_m\vdash C_r\quad\Delta,B_m\vdash C_r}
     {\Delta,A_m+B_m\vdash C_r}\;+L
$$

$$
\text{there is no }0R
\qquad
\frac{}{\Delta,0_m\vdash C_r}\;0L.
$$

The repeated $\Delta$ in additive rules is the same context in both premises; $\Delta,\Delta'$ in multiplicative rules partitions resources. At structural modes, explicit contraction/weakening can reproduce ordinary intuitionistic behavior; at linear modes, their absence preserves exact use.

## 6. Operational/computational reading

Modes can be read as resource classes or communication regimes. The preorder is an information-flow/dependency policy: data from a higher mode may flow into a lower conclusion, but forbidden edges prevent a long-lived result from capturing a shorter-lived resource. The structural signature is a usage policy: $W$ allows cancellation/nonuse; $C$ allows sharing/repetition.

Under a message-passing interpretation, a shift crosses a mode boundary while recording the allowed dependency. An upshift exposes a lower-mode behavior through a higher-mode interface; a downshift packages higher-mode behavior for use at a lower mode. The side conditions are static safety checks ensuring every continuation created by that crossing remains well typed.

This reading is an interpretation, not an extra inference rule. The lecture itself develops the proof theory; detailed process dynamics for general adjoint logic belong to later work. Still, the LNL instance confirms that the abstract constraints correspond to concrete persistence and channel-lifetime invariants.

## 7. Worked derivation or trace in original notation and prose

Let $S>L$, with $\sigma(S)=\{W,C\}$ and $\sigma(L)=\varnothing$. Define the linear package

$$
D_L=\downarrow^S_L A_S.
$$

We derive $D_L\vdash D_L\times D_L$. The result does not duplicate a linear resource arbitrarily; it opens the wrapper and then uses contraction specifically authorized at mode $S$.

Bottom-up:

1. Apply $\downarrow L$, reducing the goal to $A_S\vdash D_L\times D_L$.
2. Because $C\in\sigma(S)$, apply contraction bottom-up, yielding $A_S,A_S\vdash D_L\times D_L$.
3. Apply $\times R$, allocating one $A_S$ to each premise.
4. In each branch, use identity $A_S\vdash A_S$, then $\downarrow R$. Its side condition holds because the branch context has mode $S$, so $A_S\ge S$.

The proof skeleton is

$$
\frac{
 \frac{A_S\vdash A_S}{A_S\vdash\downarrow^S_L A_S}\;\downarrow R
 \qquad
 \frac{A_S\vdash A_S}{A_S\vdash\downarrow^S_L A_S}\;\downarrow R
}{A_S,A_S\vdash D_L\times D_L}\;\times R,
$$

then contraction concludes $A_S\vdash D_L\times D_L$, and $\downarrow L$ concludes $D_L\vdash D_L\times D_L$.

Two boundary cases reveal the guards:

- If $C\notin\sigma(S)$ and $A_S$ is atomic, the contraction step is unavailable; one payload cannot feed both multiplicative branches.
- The apparent sequent $A_L\vdash\uparrow^S_L A_L$ is not merely unprovable—it is ill formed when $L\not\ge S$, because a structural-mode conclusion may not depend on a linear antecedent.

## 8. Conceptual synthesis

Adjoint logic turns “structural versus linear” from a global choice into local mode data. One proposition grammar and one sequent shape suffice because modes carry the structural distinctions. The preorder answers **which dependencies are legal**; $\sigma$ answers **how many times an assumption may be used**; shifts answer **how a proposition crosses a legal mode boundary**.

The side conditions are not decorative annotations. They are precisely the missing premises discovered by checking whether bottom-up rule application preserves sequent well-formedness. Their systematic origin is what makes the calculus scalable: adding modes does not require inventing another family of connective rules.

## 9. Common confusions and failure modes

- **$m\ge k$ means $m$ is logically stronger.** Operationally useful, but imprecise. Formally it licenses an $m$-mode assumption in a proof of a $k$-mode conclusion.
- **The preorder must be a total order.** No. Modes may be incomparable, forbidding dependencies in both directions.
- **$\Delta\ge m$ is a derivable premise.** It is the well-formedness presupposition for even writing $\Delta\vdash A_m$.
- **If $m\ge k$, then $m$ may have fewer structural rules.** The calculus requires the opposite inclusion: $\sigma(m)\supseteq\sigma(k)$.
- **Exchange is encoded by $\sigma$.** Not here. Exchange is globally assumed; $\sigma$ tracks only $W$ and $C$.
- **$\times$ always means linear tensor.** Its resource behavior depends on the mode. At structural modes, available weakening/contraction make it behave like ordinary product.
- **Upshift and downshift can be formed between arbitrary modes.** Their indices must be comparable in the stated direction.
- **All rule side conditions should be copied symmetrically.** Side conditions are asymmetric because only some premises demand dependencies stronger than the conclusion provides.
- **$\Box$ and $\bigcirc$ are the same round trip.** $\Box=\downarrow\uparrow$ is comonadic in the S4 instance; $\bigcirc=\uparrow\downarrow$ is monadic in the lax instance.
- **Showing that identity expansion appears to work proves cut elimination.** It is evidence for rule design, not the metatheorem itself.

## 10. Self-test questions with concise answers

1. **What does $\sigma(m)=\{W\}$ describe?** An affine mode: assumptions may be unused but not duplicated.
2. **Why must $\sigma$ be monotone?** If $m\ge k$, assumptions at $m$ must support every structural behavior allowed at $k$; cut elimination otherwise fails.
3. **Which LNL cut does $m=L,r=S$ suggest?** An illegal $LS$ cut, excluded because $L\not\ge S$.
4. **Why does $\to L$ require $\Delta\ge m$?** Its first premise proves $A_m$, a stronger dependency demand than the final $C_r$ may impose.
5. **Why does $\uparrow R$ need no extra context condition?** $\Delta\ge m$ and $m\ge k$ already imply $\Delta\ge k$.
6. **Why does $\downarrow R$ require $\Delta\ge\ell$?** The conclusion only ensures dependencies reach mode $m$, while the premise concludes at the higher mode $\ell$.
7. **How is $!A_L$ recovered?** As $\downarrow^S_L\uparrow^S_L A_L$ in the two-mode linear-logic instance.
8. **What data defines an adjoint-logic instance?** Modes, their preorder, their structural signatures, and any mode-specific grammar restrictions.

## 11. Related concept pages

- [Adjoint logic](../Concepts/Adjoint%20Logic.md)
- [Modes and the dependence preorder](../Concepts/Modes%20and%20the%20Dependence%20Preorder.md)
- [Exchange, contraction, and weakening](../Concepts/Exchange%20Contraction%20and%20Weakening.md)
- [Adjoint modalities](../Concepts/Adjoint%20Modalities.md)
- [Cut elimination across modes](../Concepts/Cut%20Elimination%20Across%20Modes.md)
- [Polarity and invertibility](../Concepts/Polarity%20and%20Invertibility.md)
- [Strict, affine, linear, and structural resource regimes](../Comparisons/Resource-Regimes.md)
- [Linear versus structural persistence](../Comparisons/Linear%20vs%20Structural%20Persistence.md)

## 12. Source trail

- **Lecture:** 11, “Adjoint Logic,” October 3, 2023.
- **Numbered sections:** §1 Introduction; §2 Adjoint Logic: The Basics; §3 Logical Rules; §4 The Shifts; §5 Specific Logics as Instances of the Adjoint Schema; §6 Summary.
- **Printed pages:** L11.1–L11.9.
- **PDF pages:** 123–131.

## 13. Previous/next navigation

[← Lecture 10 - A Mixed Linear-Nonlinear Logic](Lecture%2010%20-%20A%20Mixed%20Linear-Nonlinear%20Logic.md) · [Lecture 12 - Focusing →](Lecture%2012%20-%20Focusing.md)

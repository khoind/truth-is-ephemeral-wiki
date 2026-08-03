---
title: "Polarity and Invertibility"
aliases:
  - "Positive and negative connectives"
  - "Invertible proof rules"
tags:
  - polarity
  - invertibility
  - proof-search
  - focusing
source_lectures:
  - 3
  - 4
prerequisites:
  - "Identity and cut admissibility"
  - "Left and right rules"
related:
  - "Additive and Multiplicative Connectives"
  - "Identity and Cut Admissibility"
  - "Proof Terms and Cut Reductions"
---

# Polarity and Invertibility

## 1. One-sentence definition

**A connective is negative when its right rule can always be applied backward without losing provability, and positive when its left rule has that property.**

## 2. Why the concept is needed

Naive backward proof search repeatedly chooses among every applicable left and right rule. Even when termination is guaranteed, this creates needless branching. An invertible step is safe: its premises are provable exactly when its conclusion is, so applying it cannot steer search away from a proof. Polarity records which side offers those safe decompositions and later supports focusing and computational distinctions such as lazy behavior versus eager data.

## 3. Intuitive model

**Intuition.** An invertible rule is a door that never locks behind you: walking backward through it preserves every possibility of success. Positive data can safely be opened when it appears as an available resource; negative behavior can safely be requested or specified when it is the goal. This is a search metaphor, not a truth valuation—“positive” does not mean true, and “negative” does not mean false.

## 4. Formal core

For a rule

$$\frac{J_1\quad\cdots\quad J_n}{J}\;R,$$

ordinary sound use of the rule gives: if all premises $J_i$ are provable, then conclusion $J$ is provable. $R$ is **invertible** when the converse also holds: if $J$ is provable, then every $J_i$ is provable. Thus backward application preserves provability in both directions.

For connectives, classify top-level behavior rather than isolated rule syntax:

- **Negative / right-invertible:** $A\backslash B$, $B/A$, $A\mathbin{\&}B$, $\top$.
- **Positive / left-invertible:** $A\bullet B$, ordered twist $A\circ B$, $1$, $A\oplus B$, $0$.

$A,B$ are propositions. $\mathbin{\&}$ is external choice, $\oplus$ internal choice, $1$ the multiplicative unit, $\top$ the additive truth unit, and $0$ additive falsehood. Twist is the order-reversing multiplicative companion listed in Lecture 4; fuse is the order-preserving one treated in detail.

Identity expansion gives a useful diagnostic. Expand $F\vdash F$ for compound $F$. The side whose rule must be applied first bottom-up is the candidate invertible side. For fuse:

$$
\frac{\overline{A\vdash A}\qquad\overline{B\vdash B}}
     {AB\vdash A\bullet B}\;\bullet R
\quad\text{then}\quad
\frac{AB\vdash A\bullet B}{A\bullet B\vdash A\bullet B}\;\bullet L.
$$

Since $\bullet L$ must first expose $A,B$, fuse is left-invertible. Formally, if $\Omega_L(A\bullet B)\Omega_R\vdash C$ is provable, cut it with the displayed proof $AB\vdash A\bullet B$ and eliminate the cut to obtain $\Omega_LAB\Omega_R\vdash C$.

## 5. How to use/read it

During bottom-up proof search, exhaust applicable invertible decompositions before making noninvertible choices. For a negative succedent, apply its right rule. For a positive antecedent, apply its left rule. The remaining steps may require choosing a context split, an injection, or a projection; those choices are the real search points.

Be precise about side conditions. A connective is classified as invertible on a side only when its decomposition is applicable whenever that connective appears top-level there and provability is preserved. This avoids vacuous claims about zero-premise rules.

## 6. Worked example

Suppose the goal is

$$X\bullet Y\vdash X\bullet Y.$$

Bottom-up application of $\bullet R$ first would require splitting the single antecedent $X\bullet Y$ between two premises. Giving it wholly to either premise leaves the other empty, and neither atomic goal can be completed. The noninvertible choice is premature.

Apply the positive connective’s invertible left rule first:

$$X,Y\vdash X\bullet Y.$$

Now $\bullet R$ has the forced successful split $X\mid Y$, and atomic identities close both premises. This example shows that invertibility is about preserving the existence of a proof, while noninvertible rules may still be correct when applied with the right choice.

## 7. Non-example or boundary case

The premise-free rule $\cdot\vdash1$ is vacuously invertible as an implication from its conclusion to all zero premises. Yet it cannot be applied to $X\vdash1$, because its conclusion requires the empty context. Calling “$1R$ invertible” without mentioning applicability therefore gives a misleading proof-search instruction. The connective $1$ is classified positive because its left rule is the uniformly safe top-level decomposition.

Another boundary: invertibility does not mean a rule can be reversed syntactically in every arbitrary context, nor does it mean the connective has a semantic inverse.

## 8. Key consequences

- Proof search can separate deterministic decompositions from genuine choices.
- Every ordered connective in the presented calculus receives a polarity.
- Identity expansion predicts polarity; cut elimination supports formal invertibility proofs.
- Structural conjunction conflates positive tensor-like and negative with-like behavior.
- Positive types foreshadow eager data; negative types foreshadow lazy observations.
- Polarity is orthogonal to additive versus multiplicative classification.

## 9. Relations to nearby concepts

[Additive and Multiplicative Connectives](<Additive and Multiplicative Connectives.md>) classifies resource allocation, not safe proof-search direction. Thus additive $\oplus$ is positive while additive $\mathbin{\&}$ is negative. [Identity and Cut Admissibility](<Identity and Cut Admissibility.md>) supplies the proof transformations used to establish invertibility. [Proof Terms and Cut Reductions](<Proof Terms and Cut Reductions.md>) makes the corresponding introductions and eliminations syntactic. [Ordered Conjunction and Implications](<Ordered Conjunction and Implications.md>) provides the clearest contrast: fuse is positive, directional implications negative.

Invertibility is a local property of rules/connectives; focusing is a larger proof-search discipline that groups sequences of invertible and noninvertible steps. The latter is anticipated here but not yet developed in Lectures 3–4.

## 10. Common mistakes

- Treating positive/negative as truth values or formula negation.
- Equating additives with negative connectives and multiplicatives with positive ones.
- Assuming a correct rule is necessarily invertible.
- Inferring invertibility only from the number of premises.
- Ignoring side conditions such as the empty context for $1R$.
- Thinking an invertible strategy proves every provable goal without any later search.
- Claiming the identity-expansion test alone replaces a proof.

## 11. What to remember

- Invertible backward steps preserve provability exactly.
- Negative means right-invertible; positive means left-invertible.
- Apply safe decompositions before making choices.
- Identity expansion is a diagnostic; cut admissibility proves representative cases.
- Polarity and additive/multiplicative are different axes.
- Rule applicability matters, especially for units.

## 12. Source trail

- Lecture 3, Section 5, printed pp. L3.8–L3.9, PDF pp. 33–34: implication right invertibility as a proof-construction observation.
- Lecture 3, Section 6, printed pp. L3.9–L3.10, PDF pp. 34–35: external-choice identity expansion and right invertibility.
- Lecture 4, Section 4, printed pp. L4.7–L4.8, PDF pp. 49–50: definition, identity test, cut proof for fuse, unit caveat, and ordered polarity classification.
- Lecture 4, Section 5, printed pp. L4.8–L4.9, PDF pp. 50–51: connective comparison and polarity collapse in structural logic.

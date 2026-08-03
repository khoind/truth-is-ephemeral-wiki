---
title: Quantifiers in Substructural Logic
aliases: [substructural quantification, universal and existential quantifiers]
tags: [quantifiers, eigenvariables, substitution, ordered-logic, lecture-13]
source_lectures: ["Lecture 13 - Quantifiers"]
prerequisites: [sequent calculus, cut elimination, variable binding]
related: [Positive vs Negative Polarity, Cut Elimination Across Modes, Continuation Channels]
---

# Quantifiers in Substructural Logic

## One-sentence definition

**Universal and existential quantification extend substructural sequents with scoped individuals while keeping the individual-variable context structural and the proposition context subject to its original resource discipline.**

## Why the concept is needed

Inference rules implicitly quantify schematic variables, but internal logical propositions must state that quantification. Quantifiers express rules such as transitivity, witnesses, and freshness of generated channels. Their rules must preserve ordered or linear assumptions, enforce eigenvariable freshness, and interact harmoniously with cut through substitution.

## Intuitive model

**Intuition.** Proposition assumptions are resources; individual names are references mentioned inside those resources. Mentioning the same name twice does not duplicate a channel or proof. Therefore names live in a structural scope even when propositions are ordered or linear.

## Formal core

Use judgments

$$\Gamma;\Omega\vdash A,$$

where $\Gamma=i_1\;\mathsf{ind},\ldots,i_n\;\mathsf{ind}$ is a structural context of distinct individual variables, $\Omega$ is the substructural proposition context (ordered in Lecture 13), and every free individual in $\Omega,A$ is declared in $\Gamma$.

Universal rules are

$$
\frac{\Gamma,i\;\mathsf{ind};\Omega\vdash A(i)}
{\Gamma;\Omega\vdash\forall i.A(i)}\;\forall R
$$

and

$$
\frac{\Gamma\vdash t\;\mathsf{ind}\quad
\Gamma;\Omega_L,A(t),\Omega_R\vdash C}
{\Gamma;\Omega_L,\forall i.A(i),\Omega_R\vdash C}\;\forall L.
$$

$i$ is fresh in the conclusion (an eigenvariable); $t$ is a well-formed term using variables from $\Gamma$; $\Omega_L,\Omega_R$ preserve ordered position.

Existential rules reverse the choices:

$$
\frac{\Gamma\vdash t\;\mathsf{ind}\quad\Gamma;\Omega\vdash A(t)}
{\Gamma;\Omega\vdash\exists i.A(i)}\;\exists R
$$

and

$$
\frac{\Gamma,i\;\mathsf{ind};\Omega_L,A(i),\Omega_R\vdash C}
{\Gamma;\Omega_L,\exists i.A(i),\Omega_R\vdash C}\;\exists L.
$$

Harmony relies on individual substitution: from $\Gamma\vdash t\;\mathsf{ind}$ and $\Gamma,i\;\mathsf{ind};\Omega(i)\vdash A(i)$, derive $\Gamma;\Omega(t)\vdash A(t)$.

## How to use/read it

To prove a universal, introduce a genuinely fresh name and argue parametrically. To use a universal, choose a well-scoped term. To prove an existential, choose and prove a witness. To use an existential, open it with a fresh abstract name; the client may not depend on which witness it is. Keep substitution of individuals separate from cut substitution of proofs/resources.

## Worked example

Encode fresh channel creation in a cut transition:

$$
\forall P.\forall Q.\;\mathsf{proc}(x\leftarrow P(x);Q(x))
\multimap\exists a.\mathsf{proc}(P(a))\otimes\mathsf{proc}(Q(a)).
$$

1. The configuration’s existing names $a_1,\ldots,a_n$ are declared in $\Gamma$.
2. Applying the transition produces an existential package rather than choosing an old global name.
3. Use $\exists L$ with fresh eigenvariable $a$, extending $\Gamma$.
4. Apply $\otimes L$ to obtain the two linear process facts $\mathsf{proc}(P(a))$ and $\mathsf{proc}(Q(a))$.
5. Because $a$ was fresh for the conclusion context, both processes share a new channel, and no existing process accidentally refers to it.

The existential is the logical form of the operational freshness condition.

## Non-example or boundary case

From $A(n)$ one may not conclude $\forall i.A(i)$ using the same already-declared $n$. That would turn one instance into a parametric proof. Similarly, $\forall L$ cannot instantiate with a term containing an undeclared variable, and $\exists L$ cannot expose its witness as a globally chosen constant. If proposition assumptions themselves contain linear channels, placing them in $\Gamma$ would be wrong; only individual declarations are structural.

## Key consequences

Principal cut reductions for both quantifiers replace a cut on $\forall i.A(i)$ or $\exists i.A(i)$ with a cut on the smaller $A(t)$ after substitution. Universal quantification is negative; existential is positive. The construction carries from ordered logic to linear, structural, and adjoint settings as long as context presuppositions are preserved.

## Relations to nearby concepts

[Positive vs Negative Polarity](../Comparisons/Positive%20vs%20Negative%20Polarity.md) classifies the quantifiers. [Cut Elimination Across Modes](Cut%20Elimination%20Across%20Modes.md) provides the normalization pattern generalized beyond ordered logic. [Continuation Channels](Continuation%20Channels.md) uses fresh names operationally, though allocation and existential scope remain distinct levels.

## Common mistakes

- Confusing schematic metavariables with object-language quantifiers.
- Forgetting the eigenvariable freshness condition.
- Treating individual names as consumable proposition resources.
- Ignoring left/right ordered context around a quantified assumption.
- Measuring term size when proving that $A(t)$ is a smaller cut formula; logical structure is what decreases.

## What to remember

- Names are structural; propositions retain their substructural regime.
- $\forall R$ and $\exists L$ introduce fresh eigenvariables.
- $\forall L$ and $\exists R$ choose terms.
- Substitution is the key quantifier cut reduction.
- Existentials express fresh generated names.

## Source trail

Lecture 13, “Quantifiers,” §§1–4, printed lecture pages L13.1–L13.6, PDF pages 142–147. See [Lecture 13 - Quantifiers](../Lectures/Lecture%2013%20-%20Quantifiers.md).

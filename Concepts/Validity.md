---
title: Validity
aliases: [valid judgment, persistent truth]
tags: [validity, linear-logic, exponential, lecture-09]
source_lectures: ["Lecture 09 - Validity"]
prerequisites: [linear sequents, cut, weakening and contraction]
related: [Girard vs Andreoli Exponentials, Linear vs Structural Persistence, Mixed Linear-Nonlinear Logic]
---

# Validity

## One-sentence definition

**Validity is the judgment that a proposition can be proved without consuming ephemeral assumptions, so its proof may be reproduced and used structurally.**

## Why the concept is needed

Ordinary linear truth records a state-dependent resource: a derivation of $A$ may consume exactly the linear assumptions used to obtain it. That discipline cannot express a theorem, library routine, or server that may be invoked arbitrarily often. Recursion can simulate reuse operationally, but it does not explain reuse proof-theoretically. Validity separates conclusions that require no linear resources from merely current truths and thereby justifies weakening and contraction for those conclusions.

The construction also explains the exponential $!A$ instead of taking its structural behavior as primitive. First define a judgment; then internalize that judgment as a proposition.

## Intuitive model

**Intuition.** A linear fact is a ticket: presenting it spends it. A valid fact is a printing plate: it uses no tickets to operate, so a fresh ticket can be printed whenever needed. The plate is not “a ticket with a very large quantity.” Its repeatability follows from its independence from the linear stock.

## Formal core

There are two judgments:

$$
\Gamma;\Delta \vdash A\;\mathsf{true}
\qquad
\Gamma \vdash A\;\mathsf{valid}.
$$

$A$ and $C$ range over linear propositions. $\Gamma$ is a structural context—order and multiplicity do not matter, and its members may be weakened or contracted. $\Delta$ is a multiset of linear assumptions, each of which must be used exactly once. The empty linear context is $\cdot$.

Validity is governed by:

$$
\frac{\Gamma;\cdot\vdash A\;\mathsf{true}}{\Gamma\vdash A\;\mathsf{valid}}\;\mathsf{validR}
\qquad
\frac{\Gamma,A\;\mathsf{valid};\Delta,A\;\mathsf{true}\vdash C\;\mathsf{true}}
{\Gamma,A\;\mathsf{valid};\Delta\vdash C\;\mathsf{true}}\;\mathsf{validL}.
$$

The first rule demands an empty linear context. The second materializes one usable linear copy of a valid assumption. These are rules for judgments, not connective rules.

Validity is internalized by $!A$:

$$
\frac{\Gamma\vdash A\;\mathsf{valid}}{\Gamma;\cdot\vdash !A\;\mathsf{true}}\;!R
\qquad
\frac{\Gamma,A\;\mathsf{valid};\Delta\vdash C\;\mathsf{true}}
{\Gamma;\Delta,!A\vdash C\;\mathsf{true}}\;!L.
$$

Combining $\mathsf{validR}$ and $!R$ gives $\frac{\Gamma;\cdot\vdash A}{\Gamma;\cdot\vdash !A}\;!R'$. The empty $\Delta$ is essential.

## How to use/read it

Read a member of $\Gamma$ as a recipe that may be instantiated into $\Delta$ whenever a linear rule must inspect it. Operationally, a valid provider can serve arbitrarily many clients because each request starts a fresh linear interaction. Proof-theoretically, the structural behavior belongs to the validity judgment; $!$ merely makes that status mentionable inside linear formulas.

## Worked example

Derive the usable content of $!A$, namely $\cdot;!A\vdash A$.

1. Linear identity gives $A;A\vdash A$; the left $A$ is in the structural zone and the right one in the linear zone.
2. Apply $\mathsf{validL}$ bottom-up: it explains the linear copy as an instance of the structural $A$, yielding $A;\cdot\vdash A$.
3. Apply $!L$ bottom-up to move the assumption $!A$ from the linear context into structural status.
4. The result is $\cdot;!A\vdash A$.

The same structural $A$ could be materialized in two branches of a proof, which explains reuse without duplicating any linear premise.

## Non-example or boundary case

$P\multimap !P$ is not generally derivable from a lone linear atom $P$. The only route to $!P$ uses $!R'$, whose premise must have empty linear context; $P$ cannot be discarded. If $!R'$ allowed $\Delta=P$, then one could derive both $P\vdash P\otimes P$ and $P\vdash 1$, collapsing linear logic by admitting contraction and weakening for every resource.

Likewise, $!(A\otimes B)\multimap(!A\otimes !B)$ fails: each reusable pair supplies $A$ and $B$ together, not independently reusable streams.

## Key consequences

Validity yields a principled exponential, validates $!A\multimap A$ and $!A\multimap!!A$, and supports a compositional embedding of structural logic into linear logic. Cut and identity remain admissible, but cut elimination must simultaneously handle an auxiliary cut that removes a valid assumption. The construction also generalizes: over a structural base it resembles necessity in intuitionistic S4.

## Relations to nearby concepts

[Girard vs Andreoli Exponentials](../Comparisons/Girard%20vs%20Andreoli%20Exponentials.md) compares explicit structural rules on $!A$ with the two-context presentation. [Linear vs Structural Persistence](../Comparisons/Linear%20vs%20Structural%20Persistence.md) distinguishes repeatable facts from persistent runtime objects. [Mixed Linear-Nonlinear Logic](Mixed%20Linear-Nonlinear%20Logic.md) replaces the single encoded structural layer with native structural and linear strata.

## Common mistakes

- Treating $A\;\mathsf{valid}$ as an object-language proposition rather than a judgment.
- Forgetting that only $\Delta$ is linear; $\Gamma$ is propagated to premises.
- Applying a logical left rule directly to $A$ in $\Gamma$ without first materializing a linear copy.
- Reading failure of one proof attempt as nonderivability without using normalization or a proof-search argument.

## What to remember

- Valid means provable with no linear dependencies.
- Structural reuse is justified by repeatable production, not arbitrary duplication.
- $!A$ internalizes validity.
- The empty linear context in $!R$ is the boundary protecting linearity.

## Source trail

Lecture 9, “Validity,” §§1–4 and §6, printed lecture pages L9.1–L9.6 and L9.8–L9.10, PDF pages 102–107 and 109–111. See [Lecture 09 - Validity](../Lectures/Lecture%2009%20-%20Validity.md).

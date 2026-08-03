---
title: Girard vs Andreoli Exponentials
aliases: [exponential presentations, dyadic exponential]
tags: [comparison, exponential, linear-logic, validity, lecture-09]
source_lectures: ["Lecture 09 - Validity"]
prerequisites: [linear sequent calculus, weakening, contraction]
related: [Validity, Linear vs Structural Persistence, Shifts Between Logics]
---

# Girard vs Andreoli Exponentials

## One-sentence definition

**Girard’s presentation marks reusable formulas with $!$ inside one antecedent, whereas Andreoli’s dyadic presentation separates reusable assumptions into a structural context and ordinary resources into a linear context.**

## Why the concept is needed

Both systems explain how linear logic can use some assumptions zero, once, or many times, but they locate that freedom differently. Confusing them leads to malformed rules—for example, contracting an unmarked linear formula or applying a connective rule inside a context that contains judgments of validity. The comparison also exposes why the dyadic system is more than notation: it separates the structural regime from the linear connectives and makes the judgmental source of $!$ visible.

## Intuitive model

**Intuition.** Girard labels every reusable item in a single warehouse with a “photocopy permitted” sticker. Andreoli uses two rooms: a permanent catalog $\Gamma$ and a consumable shelf $\Delta$. Fetching from the catalog creates one item on the shelf. The inventories describe equivalent reuse behavior, but the second makes the boundary explicit.

## Formal core

Let $A,B,C$ be propositions. In Girard’s one-context calculus, $\Delta$ is a multiset and $!\Delta$ means every formula in $\Delta$ has outer form $!B$:

$$
\frac{!\Delta\vdash A}{!\Delta\vdash !A}\;!R
\quad
\frac{\Delta,A\vdash C}{\Delta,!A\vdash C}\;!L
\quad
\frac{\Delta,!A,!A\vdash C}{\Delta,!A\vdash C}\;\mathsf{contract}
\quad
\frac{\Delta\vdash C}{\Delta,!A\vdash C}\;\mathsf{weaken}.
$$

Andreoli writes $\Gamma;\Delta\vdash A$. $\Gamma$ is structural (often treated as a set), $\Delta$ is linear (a multiset), and logical rules act on $A$ and formulas in $\Delta$. In the validity reconstruction:

$$
\frac{\Gamma;\cdot\vdash A}{\Gamma\vdash A\;\mathsf{valid}}
\qquad
\frac{\Gamma,A;\Delta,A\vdash C}{\Gamma,A;\Delta\vdash C}
\qquad
\frac{\Gamma;\cdot\vdash A}{\Gamma;\cdot\vdash !A}\;!R'.
$$

The middle rule is $\mathsf{validL}$: the first $A$ belongs to $\Gamma$, the second is its linear instance in $\Delta$.

| Question | Girard | Andreoli / validity reconstruction |
|---|---|---|
| Where is reuse recorded? | Outer $!$ on an antecedent | Membership in structural $\Gamma$ |
| Sequent shape | $\Delta\vdash A$ | $\Gamma;\Delta\vdash A$ |
| Weakening/contraction | Explicit rules for $!A$ | Structural behavior of $\Gamma$ |
| Promotion condition | All antecedents already exponential | Linear context is empty |
| Applying linear left rules | Derelict $!A$ to $A$ | Materialize $A$ from $\Gamma$ into $\Delta$ |
| Conceptual emphasis | Modality inside linear logic | Separation of judgments/contexts |

## How to use/read it

In Girard’s system, inspect outer syntax: only $!A$ is reusable. In the dyadic system, inspect position: assumptions before the semicolon are reusable even though their underlying propositions use linear connectives. A translation typically sends Girard’s exponential assumptions into $\Gamma$ and leaves ordinary formulas in $\Delta$; administrative $!L$ and validity steps account for movement across the boundary.

## Worked example

Show why the promotion side condition is the same invariant in two forms.

1. Suppose a proof of $A$ depends only on reusable assumptions $!B_1,\ldots,!B_n$ in Girard’s calculus.
2. Since every antecedent has outer $!$, $!R$ may conclude $!A$.
3. In dyadic notation, place the underlying reusable assumptions in $\Gamma=B_1,\ldots,B_n$ and use no linear assumptions: $\Gamma;\cdot\vdash A$.
4. Apply $!R'$ to obtain $\Gamma;\cdot\vdash !A$.
5. If one extra unmarked resource $D$ were present, the Girard premise would not be of shape $!\Delta\vdash A$, and the Andreoli premise would have nonempty linear context $D$. Both reject promotion for the same reason.

## Non-example or boundary case

Do not identify $\Gamma;\Delta\vdash A$ with the comma-separated sequent $\Gamma,\Delta\vdash A$. The semicolon changes structural permission. Nor may one apply $\otimes L$ directly to a formula stored as valid in $\Gamma$: its linear connective becomes available only after a linear instance is produced.

The presentations are proof-theoretically related, but their derivations are not textually identical; the dyadic form can require visible administrative moves between zones.

## Key consequences

The dyadic organization explains why reusable assumptions propagate to every premise while linear assumptions split. It isolates the empty-context invariant behind promotion and prepares the move to mixed linear/nonlinear and adjoint logics, where structural propositions acquire their own connectives rather than being only $!$-marked linear propositions.

## Relations to nearby concepts

[Validity](../Concepts/Validity.md) supplies the judgmental derivation of the dyadic rules. [Linear vs Structural Persistence](Linear%20vs%20Structural%20Persistence.md) warns that context-level reuse and runtime persistence are different axes. [Shifts Between Logics](../Concepts/Shifts%20Between%20Logics.md) decomposes $!A$ into crossings between native strata.

## Common mistakes

- Saying Andreoli merely “uses two lists”; the lists obey different structural laws.
- Reading $!\Delta$ as “apply $!$ to the conjunction of $\Delta$.”
- Allowing promotion with an unconsumed linear assumption.
- Assuming equivalence means each proof has exactly the same rule sequence.

## What to remember

- Girard marks reuse syntactically; Andreoli locates it contextually.
- $!\Delta$ and $\Gamma;\cdot$ encode the same promotion boundary.
- Linear rules operate in the linear zone.
- The dyadic form reveals the role of validity.

## Source trail

Lecture 9, “Validity,” §§2–4 and §6, printed lecture pages L9.1–L9.6 and L9.8–L9.10, PDF pages 102–107 and 109–111. See [Lecture 09 - Validity](../Lectures/Lecture%2009%20-%20Validity.md).

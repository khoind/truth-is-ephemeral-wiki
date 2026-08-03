---
title: Strict, Affine, Linear, and Structural Resource Regimes
aliases:
  - resource regimes
  - weakening and contraction comparison
tags:
  - comparison
  - resources
  - proof-search
source_lectures:
  - 18
  - 19
prerequisites:
  - "[Forward proof search and inverse method](../Concepts/Forward-Proof-Search-and-Inverse-Method.md)"
related:
  - "[Resource semantics](../Concepts/Resource-Semantics.md)"
  - "[Mixed linear and structural futures](../Concepts/Mixed-Linear-and-Structural-Futures.md)"
---

# Strict, Affine, Linear, and Structural Resource Regimes

## One-sentence definition

A resource regime specifies whether assumptions must be used and whether they may be duplicated: strict allows contraction but not weakening, affine allows weakening but not contraction, linear allows neither, and structural allows both.

## Why the concept is needed

The same connective can behave differently when its context admits different structural principles. Proof search, operational ownership, and semantic resource combination all depend on whether unused or duplicated assumptions are legal. Naming the regimes prevents “nonlinear” from collapsing two independent permissions.

## Intuitive model

**Intuition.** Think of assumptions as tickets. A linear ticket must be used exactly once; an affine ticket at most once; a strict template at least once but may be copied; a structural fact any number of times. The ticket story is only intuition: formal rules govern derivations, not physical objects.

## Formal core

| Regime | Weakening $\frac{\Gamma\vdash C}{\Gamma,A\vdash C}$ | Contraction $\frac{\Gamma,A,A\vdash C}{\Gamma,A\vdash C}$ | Intended use count |
|---|---:|---:|---|
| Linear | no | no | exactly once |
| Affine | yes | no | zero or one |
| Strict | no | yes | one or more |
| Structural | yes | yes | zero or more |

The displayed contraction rule is read bottom-up during backward proof search as duplication, but forward from premise to conclusion it merges two occurrences. In a focused inverse method, contractible antecedents can be stored as sets. For weakening regimes define subsumption

$$
(\Delta\vdash A)\le(\Delta'\vdash A')\quad\text{iff}\quad \Delta\subseteq\Delta'\text{ and }A=A'.
$$

The smaller antecedent is stronger because it proves the same goal with fewer assumptions. In affine additive conjunction, contexts from separate forward branches combine by multiset maximum $\Delta_1\max\Delta_2$, not by sum.

## How to use/read it

Ask two separate questions: may an assumption disappear, and may it be copied? Use those answers when splitting contexts, closing identities, pruning forward facts, and deciding whether a program can discard or share a capability.

## Worked example

Consider $\vdash A\multimap(B\multimap A)$, with $\multimap$ understood under each regime.

1. After two right rules, the stable obligation is $A,B\vdash A$.
2. Linear: $B$ cannot disappear, so identity on $A$ is insufficient; unprovable.
3. Affine: weaken $B$, then use $A\vdash A$; provable.
4. Strict: weakening is absent, so $B$ must be used; contraction does not help; unprovable.
5. Structural: weakening discards $B$; provable.

Now $\vdash A\multimap(A\otimes A)$ separates contraction: strict and structural can duplicate $A$, while affine and linear cannot.

## Non-example or boundary case

“Not linear” does not imply structural. Affine and strict each permit only one of weakening and contraction. Ordered logic is another independent axis: it restricts exchange/order, not just use count.

## Key consequences

Linear logic enforces exact accounting. Affine logic models discardable capabilities. Strict logic models relevant assumptions that cannot be ignored but may recur. Structural logic recovers ordinary reusable hypotheses. Mixed adjoint systems can assign different regimes to different modes.

These permissions affect theorem-prover representation as well as provability: multisets are essential without contraction, sets suffice for contractible formulas, and weakening requires ordering facts by strength so saturation does not enumerate every irrelevant supercontext.

## Relations to nearby concepts

[Resource semantics](../Concepts/Resource-Semantics.md) represents linear combination by a free commutative monoid and suggests dropping commutativity for ordered logic. [Mixed linear and structural futures](../Concepts/Mixed-Linear-and-Structural-Futures.md) realizes two regimes operationally as consumable and persistent cells. [Forward proof search and inverse method](../Concepts/Forward-Proof-Search-and-Inverse-Method.md) explains why weakening requires subsumption.

## Common mistakes

- Swapping affine and strict.
- Reading forward contraction as if it adds a copy.
- Using set union for linear multisets.
- Assuming weakening can be applied eagerly without expanding the search space.
- Confusing exchange/order with weakening/contraction.

## What to remember

- Linear: exactly once.
- Affine: at most once.
- Strict: at least once.
- Structural: any number of times.
- Weakening and contraction are independent permissions.

## Source trail

Lecture 18, §4 “Strict, Affine, and Structural Logic,” printed pp. L18.10–L18.12, PDF pp. 196–198. Linear resource combination and the ordered/affine variants are discussed in Lecture 19, §2, printed pp. L19.2–L19.3, PDF pp. 202–203.

---
title: Validity and Untethering
aliases:
  - empty-resource validity
  - untethered resource rules
tags:
  - validity
  - resource-semantics
  - translation
source_lectures:
  - 19
prerequisites:
  - "[Resource semantics](Resource-Semantics.md)"
related:
  - "[Explicit-resource sequent calculus](../Comparisons/Sequent-Calculus-SAX-and-Explicit-Resources.md)"
  - "[Mixed linear and structural futures](Mixed-Linear-and-Structural-Futures.md)"
---

# Validity and Untethering

## One-sentence definition

Validity is truth requiring the empty resource $\epsilon$, and untethering lets antecedent formulas carry their own resource justifications so negative left rules no longer calculate usage only through the current succedent.

## Why the concept is needed

Structural propositions in mixed logic can be reused because they do not consume linear resources. Resource semantics captures this precisely as $A[\epsilon]$. The initial annotated rules are nevertheless “tethered”: left decomposition talks directly about the resources in the goal annotation. Untethering reorganizes the system into local formula translations $A@p$, making a compositional embedding in first-order intuitionistic logic possible.

## Intuitive model

**Intuition.** A valid fact is a machine powered from outside the token budget. Untethering attaches a bill of materials to every intermediate component instead of waiting until the final product to total every cost. This does not make resources free; it relocates their accounting.

## Formal core

$A[\epsilon]$ says $A$ is justified with no linear resource. Representative shift rules are:

$$
\frac{\Gamma\vdash A[\epsilon]}{\Gamma\vdash\downarrow A[\epsilon]}
\qquad
\frac{\Gamma,\uparrow A[\epsilon],A[\alpha]\vdash C[p*\alpha]}
{\Gamma,\uparrow A[\epsilon]\vdash C[p]}.
$$

The second rule may generate a fresh usable copy $A[\alpha]$ at no resource cost because $\uparrow A$ is valid. Identity expansion must begin with the invertible right rule for negative $\uparrow$; attempting its noninvertible left rule first gets stuck, which confirms the polarity orientation.

Untethered negative rules allow complex annotations on antecedents. For implication:

$$
\frac{\Gamma\vdash A[q]\qquad\Gamma,B[p*q]\vdash C[r]}
{\Gamma,A\multimap B[p]\vdash C[r]}.
$$

This says that an implication costing $p$, applied to an argument costing $q$, yields a result costing $p*q$. The formula translation is

$$
\begin{aligned}
P@p&=P(p),\\
(A\multimap B)@p&=\forall\alpha.\,(A@\alpha)\supset(B@(p*\alpha)),\\
(A\mathbin{\&}B)@p&=(A@p)\land(B@p).
\end{aligned}
$$

## How to use/read it

Read $\epsilon$ as semantic independence, not an empty syntax placeholder. During untethered reasoning, compute each antecedent's local requirement and combine it at application. Use the monoid equations when comparing annotations. The adequacy target is first-order intuitionistic logic with those equations axiomatized.

## Worked example

Translate $(P\mathbin{\&}Q)\multimap P$ at $\epsilon$:

1. Apply the implication clause:
   $\forall\alpha.((P\mathbin{\&}Q)@\alpha)\supset(P@(\epsilon*\alpha))$.
2. Expand additive conjunction: $(P(\alpha)\land Q(\alpha))$.
3. Use the unit equation $\epsilon*\alpha=\alpha$.
4. Obtain $\forall\alpha.(P(\alpha)\land Q(\alpha))\supset P(\alpha)$, intuitionistically provable.

For $P\multimap(Q\multimap P)$ the translation ends in $P(\alpha*\beta)$ after assuming only $P(\alpha)$ and $Q(\beta)$; no monoid law discards $\beta$, so the linear formula remains unprovable.

## Non-example or boundary case

$A[\epsilon]$ does not mean a proof of $A$ may secretly consume a label and later erase it. Nor does untethering permit both $A[p]$ and a decomposed consequence with the same $p$ to contribute simultaneously to one linear receipt.

## Key consequences

Validity explains structural reuse semantically. Untethering sacrifices a close step-for-step match with source derivations in exchange for a compositional predicate translation. Adequacy states $\cdot\vdash A$ iff $\cdot\vdash A@\epsilon$ in the target theory.

The two ideas are complementary rather than synonymous: empty cost explains persistence, while untethering changes where nonempty costs are recorded. A formula may be untethered with a nonempty index and therefore remain genuinely resource-dependent.

## Relations to nearby concepts

[Resource semantics](Resource-Semantics.md) supplies $*$ and $\epsilon$. [Mixed linear and structural futures](Mixed-Linear-and-Structural-Futures.md) gives operational persistence to the same structural distinction. [Logical frameworks and judgments as types](Logical-Frameworks-and-Judgments-as-Types.md) uses adequacy for a different representation problem: proofs as typed objects.

## Common mistakes

- Reading $\epsilon$ as “unknown resources.”
- Assuming a valid proposition is automatically an object-language theorem with no context.
- Calling an untethered left rule a weakening rule.
- Forgetting monoid equations in the target theory.
- Proving only soundness and calling it adequacy.

## What to remember

- Validity means an empty resource receipt.
- Valid assumptions can generate reusable copies.
- Untethering attaches resource needs locally to antecedents.
- $A@p$ is a predicate-logic translation indexed by resources.
- Adequacy is an if-and-only-if statement.

## Source trail

Lecture 19, §3 “Adding Validity,” printed pp. L19.5–L19.7, PDF pp. 205–207; §4 “Untethering,” printed pp. L19.7–L19.8, PDF pp. 207–208.

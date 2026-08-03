---
title: "Ordered Conjunction and Implications"
aliases:
  - "Fuse and directional implication"
  - "Lambek connectives"
tags:
  - ordered-logic
  - fuse
  - implication
source_lectures:
  - 3
  - 4
prerequisites:
  - "Hypothetical judgments"
related:
  - "Additive and Multiplicative Connectives"
  - "Identity and Cut Admissibility"
  - "Polarity and Invertibility"
---

# Ordered Conjunction and Implications

## 1. One-sentence definition

**Ordered conjunction $A\bullet B$ packages an $A$-state followed by a $B$-state, while $A\backslash B$ and $B/A$ consume an $A$ from the left and right respectively to produce $B$.**

## 2. Why the concept is needed

Ordinary conjunction and implication hide order because structural logic admits exchange. That is unsuitable when position carries meaning: tokens in a sentence, instructions in a protocol, or resources in a stack cannot generally trade places. Ordered logic therefore splits implication by direction and equips conjunction with a rule that preserves concatenation exactly. These connectives internalize operations on an ordered context, allowing a proposition to describe not only which resources are needed but where they must occur.

## 3. Intuitive model

**Intuition.** Read $A\bullet B$ as a two-car train with the $A$ car before the $B$ car. Read $A\backslash B$ as a machine whose input socket faces left, and $B/A$ as one whose socket faces right. Connecting an argument on the wrong side is physically impossible. This picture helps with orientation, but the sequent rules—not spatial imagery—are authoritative.

## 4. Formal core

For ordered sequences $\Omega$:

$$
\frac{\Omega_1\vdash A\qquad\Omega_2\vdash B}
     {\Omega_1\Omega_2\vdash A\bullet B}\;\bullet R
\qquad
\frac{\Omega_L A B\Omega_R\vdash C}
     {\Omega_L(A\bullet B)\Omega_R\vdash C}\;\bullet L.
$$

The right rule splits the context into a prefix $\Omega_1$ for $A$ and the remaining suffix $\Omega_2$ for $B$. The left rule replaces one fused antecedent by adjacent $A,B$ in that order.

Directional implication rules are

$$
\frac{A\Omega\vdash B}{\Omega\vdash A\backslash B}\;\backslash R
\qquad
\frac{\Omega_A\vdash A\qquad\Omega_L B\Omega_R\vdash C}
     {\Omega_L\Omega_A(A\backslash B)\Omega_R\vdash C}\;\backslash L,
$$

$$
\frac{\Omega A\vdash B}{\Omega\vdash B/A}\;/R
\qquad
\frac{\Omega_A\vdash A\qquad\Omega_L B\Omega_R\vdash C}
     {\Omega_L(B/A)\Omega_A\Omega_R\vdash C}\;/L.
$$

$A,B,C$ are propositions. $\Omega,\Omega_A,\Omega_L,\Omega_R$ are ordered sequences. Juxtaposition means concatenation. $\vdash$ separates antecedents from the single succedent. The formula in parentheses is the principal antecedent decomposed by the left rule.

These rules validate compound identity and principal cut reduction. For example, a cut where $\bullet R$ meets $\bullet L$ reduces to a cut on $A$ and then a cut on $B$, preserving the context order $\Omega_L\Omega_1\Omega_2\Omega_R$.

## 5. How to use/read it

Bottom-up, use $\backslash R$ by placing its argument at the far left of the context, and use $/R$ by placing its argument at the far right. To use an implication on the left, locate a contiguous context segment on its required side that proves the argument. Do not search the whole context as though it were a bag.

$\bullet L$ is safe to apply eagerly because it merely exposes two adjacent components. $\bullet R$ requires a genuine choice of split and may fail even when another split succeeds. Conversely, the implication right rules are invertible: exposing their boundary assumption preserves provability.

## 6. Worked example

Derive

$$X\,(X\backslash(Y/Z))\,Z\vdash Y.$$

1. $X\vdash X$ by atomic identity.
2. $Z\vdash Z$ and $Y\vdash Y$ by atomic identities.
3. Use $/L$ on $Y/Z$ with those last two premises to obtain $(Y/Z)\,Z\vdash Y$.
4. Use $\backslash L$ on $X\backslash(Y/Z)$, combining step 1 with step 3.

Formally:

$$
\frac{\overline{X\vdash X}
 \qquad
 \frac{\overline{Z\vdash Z}\qquad\overline{Y\vdash Y}}
      {(Y/Z)Z\vdash Y}\;/L}
 {X(X\backslash(Y/Z))Z\vdash Y}\;\backslash L.
$$

The derivation composes a left-facing and a right-facing dependency without exchange.

## 7. Non-example or boundary case

The swapped fuse rule

$$
\frac{\Omega_2\vdash A\qquad\Omega_1\vdash B}
     {\Omega_1\Omega_2\vdash A\bullet B}\;\bullet R?
$$

is not a harmless convention. With atomic $P,Q$, it cannot expand the identity $P\bullet Q\vdash P\bullet Q$ after $\bullet L$, because the available order is $P,Q$ but the proposed right rule wants the proof of $P$ from the later segment. Combined with general identity and cut, it can derive exchange and erase the distinction between ordered and linear logic.

Also, $A\backslash B$ and $B/A$ coincide only when exchange is available. In ordered logic they are not alternative spellings.

## 8. Key consequences

- Fuse records both resource multiplicity and left-to-right order.
- Directional implication is residuated to context concatenation: it abstracts an argument at one boundary.
- Parsing can be represented as proof search over word categories.
- Identity and cut sharply detect an incorrectly oriented rule.
- With exchange, the two implications collapse to linear $A\multimap B$.

## 9. Relations to nearby concepts

$\bullet$ is multiplicative because its right rule partitions resources; compare [Additive and Multiplicative Connectives](<Additive and Multiplicative Connectives.md>). It is positive because its left rule is invertible, whereas both directional implications are negative because their right rules are invertible; see [Polarity and Invertibility](<Polarity and Invertibility.md>). [Identity and Cut Admissibility](<Identity and Cut Admissibility.md>) provides the harmony test that fixes the orientation of all three rules. [Proof Terms and Cut Reductions](<Proof Terms and Cut Reductions.md>) records their introduction and use with constructors and binders.

## 10. Common mistakes

- Reversing the pronunciation: $A\backslash B$ expects $A$ on the left; $B/A$ expects $A$ on the right.
- Allowing a noncontiguous set of assumptions to prove an implication’s argument.
- Splitting the right context for $\bullet$ in a different order from the conclusion.
- Treating $\bullet$ as commutative tensor inside ordered logic.
- Assuming specialized adjacent parsing rules replace the general implication-left rules.
- Reading $\dashv\vdash$ as formula equality rather than mutual derivability.

## 11. What to remember

- $A\bullet B$ preserves “$A$ then $B$.”
- $A\backslash B$ looks left; $B/A$ looks right.
- Ordered context concatenation is not commutative.
- $\bullet L$ and implication right rules are the invertible sides.
- Identity expansion is a quick orientation check; cut reduction confirms it.

## 12. Source trail

- Lecture 3, Sections 2.1–3, printed pp. L3.3–L3.7, PDF pp. 28–32: rules, identity expansions, principal cut reductions, and the bad swapped rule.
- Lecture 3, Sections 4–5, printed pp. L3.7–L3.9, PDF pp. 32–34: Lambek parsing and the implication equivalence.
- Lecture 4, Section 2, printed pp. L4.2–L4.6, PDF pp. 44–48: proof-term annotations for the three connectives.
- Lecture 4, Sections 4–5, printed pp. L4.7–L4.9, PDF pp. 49–51: invertibility, polarity, and collapse under exchange.


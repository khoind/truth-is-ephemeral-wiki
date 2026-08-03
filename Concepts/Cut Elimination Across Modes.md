---
title: Cut Elimination Across Modes
aliases: [adjoint cut elimination, multicut]
tags: [cut-elimination, multicut, adjoint-logic, modes, lecture-12]
source_lectures: ["Lecture 11 - Adjoint Logic", "Lecture 12 - Focusing"]
prerequisites: [Adjoint Logic, Modes and the Dependence Preorder]
related: [Cut Elimination for SAX, Focusing, Linear vs Structural Persistence]
---

# Cut Elimination Across Modes

## One-sentence definition

**Cut elimination across modes replaces composition by cut-free derivations while respecting mode dependencies and the permitted multiplicity of the cut formula, using multicut when contraction or weakening is explicit.**

## Why the concept is needed

Ordinary linear cut reduction substitutes one proof for one assumption. At a mode admitting contraction, the assumption may occur several times; naïvely substituting sequentially duplicates the producing context and breaks the induction measure. At a mode admitting weakening, it may occur zero times. Multicut absorbs both structural cases into the statement being proved, restoring a well-founded normalization argument.

## Intuitive model

**Intuition.** A cut connects a producer to one socket. A multicut connects that producer to exactly the number of sockets the mode authorizes: zero for discard, one for linear use, or many for sharing. The proof eliminates all sockets in one controlled operation instead of repeatedly reopening the same normalization problem.

## Formal core

Let $A_m$ be the cut formula at mode $m$, $C_r$ the conclusion, and $\Delta,\Delta'$ contexts. Write $(A_m)^n$ for $n$ copies. Allowed multiplicities are

$$
\mu(m)=
\begin{cases}
\{1\} & \sigma(m)=\varnothing,\\
\{0,1\} & \sigma(m)=\{W\},\\
\{1,2,\ldots\} & \sigma(m)=\{C\},\\
\{0,1,2,\ldots\} & \sigma(m)=\{W,C\}.
\end{cases}
$$

The generalized rule is

$$
\frac{\Delta\ge m\ge r\quad n\in\mu(m)\quad\Delta\vdash A_m\quad
\Delta',(A_m)^n\vdash C_r}
{\Delta,\Delta'\vdash C_r}\;\mathsf{multicut}_{A_m}.
$$

$\sigma(m)$ records weakening $W$ and contraction $C$. The dependence condition and monotonicity $\ell\ge m\Rightarrow\sigma(\ell)\supseteq\sigma(m)$ ensure that any assumptions duplicated or discarded with the producing proof allow the corresponding action.

The proof proceeds by lexicographic induction: first on the structure of $A_m$, then on the relevant derivations. Principal reductions replace a cut on a compound formula by cuts on strict subformulas; commutative reductions move multicut above nonprincipal rules.

## How to use/read it

Treat multicut as an admissibility target, not an object-language inference permanently added to normal proofs. To analyze a case, identify whether the last rule introduces the cut formula, acts elsewhere, contracts it, or weakens it. Verify mode and multiplicity conditions before comparing induction measures.

## Worked example

Reduce a cut whose client contracts $A_m$.

1. Given $D:\Delta\vdash A_m$ and $E':\Delta',(A_m)^{n+2}\vdash C_r$, contraction produces $E:\Delta',(A_m)^{n+1}\vdash C_r$.
2. A multicut with multiplicity $n+1$ appears below $E$.
3. Instead, apply the induction hypothesis directly to $D$ and $E'$ with multiplicity $n+2$.
4. This multiplicity is legal because the contraction rule establishes $C\in\sigma(m)$, so whenever $n+1\in\mu(m)$, also $n+2\in\mu(m)$.
5. The resulting conclusion is still $\Delta,\Delta'\vdash C_r$; the producing context is not duplicated by two sequential cuts.

The generalized rule turns contraction from a problematic nested-cut case into a direct smaller-derivation case.

## Non-example or boundary case

Sequentially cutting $D$ into two copies of $A_m$ first yields $\Delta,\Delta',A_m\vdash C_r$ and then $\Delta,\Delta,\Delta'\vdash C_r$. Contracting the two copies of $\Delta$ may repair the sequent when modes permit it, but the intermediate derivation produced by the first induction hypothesis can be larger than the original client. The second cut is therefore not justified by the usual measure. This is a proof failure even when the proposed operational reduction looks plausible.

## Key consequences

Weakening is multicut with $n=0$, contraction with $n=2$, and ordinary linear cut with $n=1$. The method proves that adjoint composition preserves mode discipline and that normalization can accommodate structural, affine, strict, and linear modes uniformly. It also explains why monotonicity of structural properties is required for cut elimination.

## Relations to nearby concepts

[Adjoint Logic](Adjoint%20Logic.md) supplies the mode-indexed cut. [Modes and the Dependence Preorder](Modes%20and%20the%20Dependence%20Preorder.md) explains the side conditions. [Cut Elimination for SAX](Cut%20Elimination%20for%20SAX.md) has a different endpoint—snips may remain. [Focusing](Focusing.md) uses cut-free structure to organize proof search.

## Common mistakes

- Calling multicut an ordinary derived rule without proving admissibility.
- Ignoring the zero-copy weakening case.
- Repairing a duplicated context without checking every mode admits contraction.
- Comparing only formula size when a commuting case keeps the same formula.
- Confusing a valid process reduction with a well-founded proof of normalization.

## What to remember

- Explicit contraction forces a generalized cut statement.
- $\mu(m)$ encodes exactly the mode’s legal multiplicities.
- Mode monotonicity justifies duplicating or discarding dependencies.
- Principal cuts shrink formulas; other cases must shrink derivations.
- Multicut unifies cut, weakening, and contraction.

## Source trail

Lecture 11, §§2–4, printed lecture pages L11.2–L11.5, PDF pages 124–127; Lecture 12, §2, printed lecture pages L12.1–L12.4, PDF pages 132–135. See [Lecture 11 - Adjoint Logic](../Lectures/Lecture%2011%20-%20Adjoint%20Logic.md) and [Lecture 12 - Focusing](../Lectures/Lecture%2012%20-%20Focusing.md).

---
title: Positive vs Negative Polarity
aliases: [polarity comparison, synchronous versus asynchronous connectives]
tags: [comparison, polarity, focusing, invertibility, lecture-12]
source_lectures: ["Lecture 10 - A Mixed Linear/Nonlinear Logic", "Lecture 12 - Focusing", "Lecture 13 - Quantifiers"]
prerequisites: [left and right rules, identity expansion]
related: [Focusing, Inversion Chaining and Proof Phases, Adjoint Modalities]
---

# Positive vs Negative Polarity

## One-sentence definition

**A positive connective has an invertible left rule and information-carrying right rules, while a negative connective has an invertible right rule and information-carrying left rules.**

## Why the concept is needed

Polarity predicts safe proof-search steps, communication direction, and which SAX rules become messages. Without it, “invertible,” “synchronous,” and “positive” are easily conflated or assigned to the wrong side of a sequent. The distinction also explains why a composite such as $!A=\downarrow\uparrow A$ has no single uniform polarity.

## Intuitive model

**Intuition.** A positive value is constructed by making a choice—selecting a label, supplying a pair, or ending—so its consumer can safely take it apart. A negative object is observed by its clients—choosing a projection or supplying an argument—so its provider can safely wait for that observation.

## Formal core

In the adjoint grammar at mode $m$:

$$
\begin{aligned}
A_m^- &::= P_m^-\mid A_m\to B_m\mid A_m\mathbin{\&}B_m\mid\top\mid\uparrow^m_k A_k,\\
A_m^+ &::= P_m^+\mid A_m\times B_m\mid1\mid A_m+B_m\mid0\mid\downarrow^\ell_m A_\ell.
\end{aligned}
$$

Atoms $P_m$ receive a chosen polarity because they have no connective rule. The universal quantifier $\forall i.A(i)$ is negative: $\forall R$ introduces a fresh eigenvariable deterministically, while $\forall L$ chooses an instantiating term. The existential $\exists i.A(i)$ is positive: $\exists L$ opens a fresh witness parametrically, while $\exists R$ chooses a witness.

| Feature | Positive | Negative |
|---|---|---|
| Invertible side | Left | Right |
| Information-carrying side | Right | Left |
| Focused phase | Right focus | Left focus |
| Session provider typically | Sends | Receives |
| Examples | $\times,1,+,0,\downarrow,\exists$ | $\to,\&,\top,\uparrow,\forall$ |
| SAX transformation | Right rules become axioms | Left rules become axioms |

Invertibility is an admissibility property: if the conclusion is derivable, the rule’s premises are derivable. It is not merely “the rule has one premise.”

## How to use/read it

For proof search, apply negative right and positive left rules eagerly. Delay positive right and negative left rules until focus selects their principal formula. For process interpretation, read the information-carrying side as the sender and the invertible side as the receiver. Always state the side: a connective is not “invertible everywhere.”

## Worked example

Compare $A+B$ with $A\mathbin{\&}B$.

1. To prove $A+B$, choose $+R_1$ or $+R_2$; the choice can lose completeness if made wrongly. Hence the right side is noninvertible.
2. Given $A+B$ on the left, $+L$ must cover both alternatives. Any proof using the sum can be reorganized to begin with this case split, so left decomposition is invertible.
3. To prove $A\mathbin{\&}B$, establish both $A$ and $B$ in the same context. This is safely right-invertible.
4. Given $A\mathbin{\&}B$ on the left, choose projection $\&L_1$ or $\&L_2$ according to what is needed; the choice is noninvertible.
5. In focusing, $A+B$ is handled under right focus, while $A\&B$ is handled under left focus.

## Non-example or boundary case

$!A$ in the validity calculus is neither uniformly positive nor negative. Its right rule waits for the linear context to become empty, so it is not freely right-invertible; moving it left into validity does not always immediately restore a usable linear copy. Decomposing it as $\downarrow\uparrow A$ reveals a positive exterior and negative interior instead of forcing a false classification.

Atoms are another boundary: their assigned polarity affects focused normal forms but not ordinary provability.

## Key consequences

Polarity yields phase-structured proof search, predicts provider/client communication, and guides the semi-axiomatic transformation. Quantifier polarity explains eigenvariable versus witness choices. Explicit shifts can insert polarity boundaries, enabling polarized syntax and finer control over normalization.

## Relations to nearby concepts

[Focusing](../Concepts/Focusing.md) operationalizes the classification. [Inversion, Chaining, and Proof Phases](../Concepts/Inversion%2C%20Chaining%2C%20and%20Proof%20Phases.md) contrasts the phases called asynchronous and synchronous. [Adjoint Modalities](../Concepts/Adjoint%20Modalities.md) gives the opposite-polarity shifts.

## Common mistakes

- Saying positive means “true” or negative means “false.”
- Calling a connective invertible without naming left or right.
- Classifying $!$ by only its outer glyph.
- Assuming asynchronous communication is identical to the asynchronous proof phase; they are related terminology, not the same dynamics.

## What to remember

- Positive: invert left, focus/send right.
- Negative: invert right, focus/send left.
- Polarity is proof-theoretic, not semantic truth value.
- $\forall$ is negative and $\exists$ positive.
- Composite modalities may cross polarity.

## Source trail

Lecture 10, §§1 and 4, printed pages L10.1 and L10.3–L10.4, PDF pages 113 and 115–116; Lecture 12, §§3–4, printed pages L12.5–L12.8, PDF pages 136–139; Lecture 13, §4, printed page L13.6, PDF page 147. See [Lecture 12 - Focusing](../Lectures/Lecture%2012%20-%20Focusing.md) and [Lecture 13 - Quantifiers](../Lectures/Lecture%2013%20-%20Quantifiers.md).

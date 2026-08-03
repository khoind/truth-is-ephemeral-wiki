---
title: Inversion, Chaining, and Proof Phases
aliases: [asynchronous and synchronous phases, inversion versus chaining]
tags: [inversion, chaining, proof-phases, focusing, lecture-12]
source_lectures: ["Lecture 12 - Focusing", "Lecture 15 - Adjoint SAX"]
prerequisites: [Focusing, Positive vs Negative Polarity]
related: [Focusing, Positive vs Negative Polarity, Adjoint SAX Message Sequences and Pattern Matching]
---

# Inversion, Chaining, and Proof Phases

## One-sentence definition

**Inversion is the asynchronous phase of exhausting invertible rules without commitment, while chaining is the synchronous phase of focusing on one formula and repeatedly applying its noninvertible rules.**

## Why the concept is needed

Proof search contains two kinds of work: logically forced decomposition and genuine decisions. Mixing them produces redundant permutations and hides where backtracking is necessary. Separating inversion from chaining makes the control structure explicit, connects polarity to algorithms, and clarifies the later distinction between full focusing for proof construction and partial focusing for message sequences.

## Intuitive model

**Intuition.** Inversion unfolds everything that can be learned for free. Chaining follows one chosen constructor or observer as far as possible. “Asynchronous” here means the forced rules need no coordination with an alternative proof choice; “synchronous” means a focused sequence is coordinated around one principal formula.

## Formal core

Let $\Delta^-$ contain suspended noninvertible assumptions, $\Omega$ be an ordered inversion context, and $C_r^+$ a positive goal at mode $r$. The phase boundary is represented schematically by

$$
\frac{\Delta^-\xrightarrow{C}C_r^+}
{\Delta^-;\cdot\xrightarrow{IL}C_r^+}\;C/IL.
$$

During right inversion ($IR$), negative succedents decompose. During left inversion ($IL$), positive antecedents decompose. When neither applies, a choice judgment $C$ selects

$$\Delta^-\xrightarrow{FR}[C_r^+]$$

or

$$\Delta^-;[A_m^-]\xrightarrow{FL}C_r^+.$$

$FR$ and $FL$ are right and left focus; brackets mark the unique principal formula. Focused rules preserve those brackets through positive right or negative left subformulas. Reaching an invertible formula releases focus back to $IR$ or $IL$.

The terminology “synchronous/asynchronous phase” comes from focusing. It must be distinguished from synchronous/asynchronous message delivery in SAX: the former organizes proof search, the latter says whether a sender blocks for a receiver.

## How to use/read it

Normalize the search schedule:

1. Decompose every negative goal on the right.
2. Decompose accumulated positive assumptions on the left.
3. Suspend atoms and formulas whose relevant rule is noninvertible.
4. At the choice point, select one eligible formula.
5. Chain only on that focus.
6. Return to inversion at the next polarity boundary.

Backtracking belongs primarily at step 4, not between deterministic inversion steps.

## Worked example

Prove $A\times(B+C)$ from resources $a:A$ and $b:B$.

1. The goal is positive, so right inversion cannot decompose it; left inversion also has no positive compound assumption. Search reaches choice.
2. Right-focus $A\times(B+C)$.
3. The focused $\times R$ rule splits resources: allocate $a$ to the $A$ branch and $b$ to the $B+C$ branch.
4. Focused identity closes $[A]$ with $a:A$.
5. Focus remains on $[B+C]$; choose the $+R_1$ branch.
6. Focused identity closes $[B]$ with $b:B$.

Choosing $+R_2$ would fail because no $C$ is available. The tensor split and sum injection are genuine synchronous choices; there was no benefit in interleaving unrelated invertible rules.

## Non-example or boundary case

Do not chain through a negative right subformula: its rule is invertible, so focus must be released and inversion resumed. Conversely, do not apply $+R_1$ during inversion merely because it is syntactically available; it commits to a branch. Also, a runtime with nonblocking sends is not thereby executing a focused asynchronous phase—one is an operational scheduling property, the other a proof-search classification.

## Key consequences

Phase separation concentrates nondeterminism, yields more canonical proofs, and supplies an algorithmic account of “don’t know” choices. In session interpretations, inversion aligns with receiving and chaining with information-carrying sends. Partial focusing relaxes maximal chaining: a message sequence may stop early at a continuation channel while remaining well typed.

## Relations to nearby concepts

[Focusing](Focusing.md) is the full calculus built from these phases. [Positive vs Negative Polarity](../Comparisons/Positive%20vs%20Negative%20Polarity.md) determines rule placement. [Adjoint SAX, Message Sequences, and Pattern Matching](Adjoint%20SAX%2C%20Message%20Sequences%2C%20and%20Pattern%20Matching.md) interprets message construction as partial focus and pattern matching as partial inversion.

## Common mistakes

- Calling every left rule inversion or every right rule chaining.
- Confusing phase asynchrony with nonblocking network sends.
- Permitting multiple simultaneous foci.
- Continuing focus across an invertible polarity boundary.
- Assuming full focusing and partial focusing have the same stopping rule.

## What to remember

- Inversion is forced and commitment-free.
- Chaining follows one chosen principal formula.
- Choice is localized at the phase boundary.
- “Synchronous/asynchronous” has separate proof-search and runtime uses.
- Partial focusing permits earlier stopping.

## Source trail

Lecture 12, §§3–5, printed lecture pages L12.5–L12.10, PDF pages 136–141; Lecture 15, §§5–7, printed lecture pages L15.6–L15.12, PDF pages 164–170. See [Lecture 12 - Focusing](../Lectures/Lecture%2012%20-%20Focusing.md) and [Lecture 15 - Adjoint SAX](../Lectures/Lecture%2015%20-%20Adjoint%20SAX.md).

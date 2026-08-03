---
title: Focusing
aliases: [focused proof search, Andreoli focusing]
tags: [focusing, proof-search, polarity, adjoint-logic, lecture-12]
source_lectures: ["Lecture 12 - Focusing"]
prerequisites: [Positive vs Negative Polarity, sequent calculus, invertibility]
related: [Inversion Chaining and Proof Phases, Cut Elimination Across Modes, Adjoint SAX Message Sequences and Pattern Matching]
---

# Focusing

## One-sentence definition

**Focusing is a complete proof-search discipline that exhausts invertible rules, then selects one noninvertible formula and chains decompositions on it until inversion becomes available again.**

## Why the concept is needed

Unrestricted sequent calculus admits many permutations of independent inferences. Most represent the same essential proof, yet a search procedure explores them as different branches. Focusing removes this bureaucratic nondeterminism: safe steps are mandatory, and genuine choices are localized. It also aligns proof phases with polarity and explains why sequences of messages later resemble partial focused derivations.

## Intuitive model

**Intuition.** First clear every deterministic task from an inbox. When none remain, choose one case that requires commitment and follow that thread without switching attention until it reaches another deterministic boundary. The brackets of a focused judgment mark the single active thread.

## Formal core

At mode $m$, negative propositions include atoms assigned negative polarity, $A_m\to B_m$, $A_m\mathbin{\&}B_m$, $\top$, and $\uparrow^m_k A_k$. Positive propositions include positive atoms, $A_m\times B_m$, $1$, $A_m+B_m$, $0$, and $\downarrow^\ell_m A_\ell$.

Representative judgments are:

- $\Delta^-;\Omega\xrightarrow{IR} A_m$: right inversion, with ordered accumulator $\Omega$.
- $\Delta^-;\Omega\xrightarrow{IL} C_r^+$: left inversion.
- $\Delta^-\xrightarrow{C}C_r^+$: inversion is finished; a choice is required.
- $\Delta^-\xrightarrow{FR}[A_m^+]$: right focus.
- $\Delta^-;[A_m^-]\xrightarrow{FL}C_r^+$: left focus.

$\Delta^-$ holds suspended negative formulas and positive atoms; $\Omega$ is processed deterministically from the left. $IR,IL,C,FR,FL$ label phases, not propositions. Square brackets identify the unique focus.

For example, right inversion includes

$$
\frac{A_m\,\Omega\xrightarrow{IR}B_m}{\Omega\xrightarrow{IR}A_m\to B_m}\;\to R,
$$

while right focus retains focus through a positive connective:

$$
\frac{\Delta_1^-\xrightarrow{FR}[A_m]\quad\Delta_2^-\xrightarrow{FR}[B_m]}
{\Delta_1^-,\Delta_2^-\xrightarrow{FR}[A_m\times B_m]}\;\times R.
$$

The Lecture 12 chaining rules are stated only for linear modes; structural focusing needs additional care.

## How to use/read it

Start by repeatedly applying negative right rules. Accumulate introduced assumptions in $\Omega$, then decompose positive assumptions on the left. Suspend anything noninvertible into $\Delta^-$. When $\Omega$ is empty, choose either a positive succedent for right focus or a negative antecedent for left focus. Keep the same principal formula in focus through its synchronous rules. Release focus when an invertible subformula is reached.

## Worked example

Consider $(P\to Q)\to((Q\to R)\to(P\to R))$ with positive atoms.

1. Right-invert the three implications, accumulating $P$, $Q\to R$, and $P\to Q$.
2. Left inversion suspends positive atom $P$ and the two negative implications; the positive goal $R$ also suspends. The search reaches a choice judgment.
3. Right focus on $R$ cannot close: suspended $R$ is absent from the antecedents.
4. Left focus on $Q\to R$ cannot yet supply its $Q$ argument.
5. Focus on $P\to Q$. Its left rule focuses on argument $P$, closed by atomic identity, and produces $Q$.
6. Return to inversion, then focus on $Q\to R$; identity supplies $Q$, producing $R$.
7. Focused identity closes the goal $R$.

The failed choices are shallow and informative; irrelevant rule permutations never arise.

## Non-example or boundary case

Focusing is not “always apply right rules first.” Positive right rules are noninvertible and must wait for focus. Nor may a proof focus simultaneously on two formulas. Most importantly, the displayed linear chaining calculus is not soundly generalized to structural modes by merely adding weakening and contraction; several phase-transition rules interact with those properties.

## Key consequences

Focused proofs are canonical up to much less permutation, improving proof search and logic programming. Invertible phases correspond to receiving behavior; focused phases correspond to information-carrying actions. Full focusing minimizes choice, whereas partial focusing permits a message sequence to stop at any continuation channel.

## Relations to nearby concepts

[Positive vs Negative Polarity](../Comparisons/Positive%20vs%20Negative%20Polarity.md) determines which rules belong to each phase. [Inversion, Chaining, and Proof Phases](Inversion%2C%20Chaining%2C%20and%20Proof%20Phases.md) separates deterministic decomposition from commitment. [Adjoint SAX, Message Sequences, and Pattern Matching](Adjoint%20SAX%2C%20Message%20Sequences%2C%20and%20Pattern%20Matching.md) uses partial focusing operationally.

## Common mistakes

- Calling every deterministic tactic “focusing”; focus specifically chains noninvertible rules.
- Treating suspension brackets or angle brackets as object-language modalities.
- Switching principal formulas during a focused phase.
- Applying the simplified chaining rules to modes with $W$ or $C$.

## What to remember

- Invert first, choose once, then chain.
- Exactly one proposition is focused.
- Polarity organizes phases.
- Focusing removes permutations, not genuine choices.
- Lecture 12’s displayed chaining system assumes linear modes.

## Source trail

Lecture 12, §§1 and 3–5, printed lecture pages L12.1 and L12.5–L12.10, PDF pages 132 and 136–141. See [Lecture 12 - Focusing](../Lectures/Lecture%2012%20-%20Focusing.md).

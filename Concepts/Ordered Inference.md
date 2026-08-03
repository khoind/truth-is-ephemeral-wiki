---
title: "Ordered Inference"
aliases:
  - "sequence rewriting"
  - "noncommutative inference"
tags:
  - concept
  - ordered-logic
  - substructural-logic
source_lectures:
  - 1
  - 2
prerequisites:
  - "Inference rules"
  - "Finite sequences"
related:
  - "Linear Inference"
  - "Exchange Contraction and Weakening"
  - "CBA Diagrams and True Concurrency"
---

# Ordered Inference

## 1. One-sentence definition

**Ordered inference is local sequence rewriting in which a rule consumes one consecutive, correctly ordered block of premises and replaces it in place with an ordered block of conclusions.**

## 2. Why the concept is needed

Some state is not merely a collection of resources. Parser input, protocol traces, stacks, tapes, and serialized messages depend on relative position. Linear multisets remember how many occurrences exist but forget where they are. Ordered inference preserves exactly that extra information by denying exchange as well as contraction.

This makes adjacency into a logical resource. A rule may become enabled only after another rule deletes the symbols between its premises, even when no output token is passed directly between the two rule applications.

## 3. Intuitive model

**Intuition.** Imagine letter tiles fixed in one row. A rule may lift a neighboring run of tiles and insert a replacement run into the same gap. It cannot gather matching tiles from distant positions, and it cannot swap tiles merely for convenience. Formally, the state is a sequence and the untouched prefix and suffix form an ordered frame.

## 4. Formal core

Let $P_i$ and $Q_j$ be propositions after any schematic variables have been instantiated. An ordered rule is

$$r=\frac{P_1\;\cdots\;P_m}{Q_1\;\cdots\;Q_n}.$$

An ordered state $\Omega$ is a finite sequence. Juxtaposition denotes sequence concatenation, and $\epsilon_s$ denotes the empty sequence. (This metanotation should not be confused with any object-language end-marker proposition.) The rule is enabled when

$$\Omega=\Omega_L\,P_1\cdots P_m\,\Omega_R,$$

for some prefix $\Omega_L$ and suffix $\Omega_R$. Firing gives

$$\Omega'=\Omega_L\,Q_1\cdots Q_n\,\Omega_R.$$

Neither exchange nor contraction is valid in general:

$$P\,Q\neq Q\,P,\qquad P\,P\neq P.$$

Concatenation is associative and has unit $\epsilon_s$, so ordered states form a monoid. A zero-conclusion rule deletes its matched block. A state is quiescent when no consecutive block matches any premise sequence.

In the ordered sequent $\Omega\vdash A$, $\Omega$ is the sequence of antecedents. Ordered product obeys

$$
\frac{\Omega_1\vdash A\quad\Omega_2\vdash B}{\Omega_1\Omega_2\vdash A\mathbin{\bullet}B}\bullet R,
$$

where the context is cut once: its prefix proves $A$ and its suffix proves $B$.

## 5. How to use/read it

Scan the state for an exact contiguous occurrence of a rule’s premise word. Replace that occurrence, without rearranging either the frame or the output. If several sites match, the execution strategy decides whether to pick one or explore all.

An ordered specification should state the legal initial language, the possible intermediate language, the reduction policy, and the meaning of terminal forms. Regular expressions or grammars are often useful for these metalevel sets, but they are not themselves inference rules.

## 6. Worked example

The following original rewrite system removes adjacent unlike markers and then seals an exposed pair:

$$
\frac{a\;b}{x}\;\mathsf{pair}
\qquad
\frac{x\;x}{z}\;\mathsf{seal}.
$$

Start with $\Omega_0=a\,b\,a\,b\,t$.

1. `pair` may match positions 1–2 or 3–4. Choose the second pair: $\Omega_1=a\,b\,x\,t$.
2. Apply `pair` to the first two positions: $\Omega_2=x\,x\,t$.
3. The two `x` occurrences are now adjacent, so `seal` yields $\Omega_3=z\,t$.
4. $\Omega_3$ is quiescent.

Choosing the other `pair` first produces the same causal situation: the two pairing events are independent, while `seal` depends on both. A linear multiset version would wrongly allow `seal` whenever two `x` tokens existed anywhere, ignoring what lay between them.

## 7. Non-example or boundary case

Suppose warehouse items may be selected in any order. Modeling the inventory as `red blue green` and requiring adjacent premises would introduce arbitrary failures caused by presentation order. A linear multiset is the correct model when order has no domain meaning.

A second boundary is “stuck means accepted.” The sequence $b\,a$ is quiescent under `pair`, but nothing in quiescence alone says it is a successful input. Acceptance requires a separate adequacy condition about the final form.

## 8. Key consequences

- Relative order and multiplicity are both observable.
- Rule matching is local to a contiguous segment.
- Deletion can enable a later event by creating adjacency.
- Independent rewrites can still admit true concurrency.
- A quiescent sequence may be a successful normal form or an erroneous stuck form.
- Ordered conjunction is associative but neither commutative nor idempotent in general.

## 9. Relations to nearby concepts

[Linear Inference](Linear%20Inference.md) consumes occurrences but retains exchange, so its frame is an unordered multiset. [Structural Inference](Structural%20Inference.md) additionally admits contraction and preserves premises. [Exchange Contraction and Weakening](Exchange%20Contraction%20and%20Weakening.md) explains the structural-law boundary. [CBA Diagrams and True Concurrency](CBA%20Diagrams%20and%20True%20Concurrency.md) shows why ordered proof diagrams require both noncrossing order and explicit adjacency dependencies. [Frame Problem and Adequacy](Frame%20Problem%20and%20Adequacy.md) explains the metalevel contract for valid inputs and outputs.

## 10. Common mistakes

- Matching premises in the right order but with intervening symbols.
- Reordering the sequence because the same propositions would form an equal multiset.
- Confusing the empty sequence with an end-marker proposition.
- Assuming every choice of redex is don’t-care without a proof.
- Treating quiescence as acceptance.
- Drawing noncrossing proof wires while overlooking that a prior deletion was needed for adjacency.

## 11. What to remember

- An ordered state is a sequence.
- Premises match consecutively and are replaced in place.
- Exchange and contraction are unavailable.
- Prefix and suffix are the preserved ordered frame.
- Adjacency can create causal dependencies even without an ordinary produced token.

## 12. Source trail

- Lecture 1, §4 “Ordered Inference,” printed pp. L1.5–L1.7, PDF pp. 5–7.
- Lecture 1, §5 “Binary Increment as Ordered Inference,” printed p. L1.7, PDF p. 7.
- Lecture 1, §7 “Summary,” printed pp. L1.9–L1.10, PDF pp. 9–10.
- Lecture 2, §3 “CBA Diagrams and True Concurrency,” printed pp. L2.3–L2.5, PDF pp. 15–17.
- Lecture 2, §6 “Internalizing State Formation as Conjunction,” printed pp. L2.9–L2.10, PDF pp. 21–22.


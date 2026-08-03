---
title: "Exchange, Contraction, and Weakening"
aliases:
  - "structural rules"
  - "context structural principles"
tags:
  - concept
  - proof-theory
  - structural-rules
source_lectures:
  - 1
  - 2
prerequisites:
  - "Contexts and sequents"
related:
  - "Structural Inference"
  - "Linear Inference"
  - "Ordered Inference"
---

# Exchange, Contraction, and Weakening

## 1. One-sentence definition

**Exchange, contraction, and weakening are the context principles that respectively permit reordering assumptions, merging or duplicating an assumption’s availability, and adding or ignoring an unused assumption.**

## 2. Why the concept is needed

The same inference-rule syntax can mean persistent reasoning, resource consumption, or ordered rewriting depending on how contexts behave. Structural principles make those background permissions explicit. They tell us whether position, multiplicity, and mandatory use are semantically observable.

Without separating the three, it is easy to say “linear means use exactly once” and miss the mechanism. Linear logic retains exchange but restricts contraction and weakening for ordinary linear formulas. Ordered logic restricts exchange too. Structural logic admits all three in its hypothetical judgments.

## 3. Intuitive model

**Intuition.** Imagine assumptions as tickets. Exchange lets you shuffle the tickets. Contraction lets one reusable pass stand in for two requested uses, or conversely regard duplicate copies as no extra power. Weakening lets you carry a ticket without using it. The analogy identifies permissions, not literal proof steps: some systems build the permissions into context equality or identity rather than displaying named rules.

## 4. Formal core

Let $\Gamma$ be a structural context, $\Delta$ a linear context, $\Omega$ an ordered context, and $A,C$ formulas. The turnstile $\vdash$ separates assumptions from the conclusion.

Displayed as sequent rules, the structural principles are:

$$
\frac{\Gamma,A,B,\Gamma'\vdash C}{\Gamma,B,A,\Gamma'\vdash C}\mathsf{exch}
$$

$$
\frac{\Gamma,A,A\vdash C}{\Gamma,A\vdash C}\mathsf{contr}
\qquad
\frac{\Gamma\vdash C}{\Gamma,A\vdash C}\mathsf{weak}.
$$

Read bottom-up, contraction permits the one assumption $A$ in the conclusion to supply two occurrences in the premise. Read top-down, it merges duplicates. Weakening read bottom-up discards $A$ from the proof obligation; top-down it adds an unused assumption.

At the state level, exchange and contraction can appear as equalities:

$$P,Q=Q,P,\qquad P,P=P.$$

This makes a structural state set-like. Keeping exchange but denying contraction makes it multiset-like. Denying both makes it sequence-like. Weakening is not the equality $P=\cdot$; it is a relation of usable information and is visible in the structural identity rule

$$\frac{}{\Gamma,A\vdash A}\mathsf{id},$$

where $\Gamma$ may be ignored. Linear and ordered identity are instead exactly $A\vdash A$.

The modality $!A$ selectively restores contraction and weakening inside linear logic: only formulas marked with $!$ receive those permissions.

## 5. How to use/read it

When examining a context, ask three independent questions:

1. May assumptions be rearranged before matching a rule? That is exchange.
2. May one occurrence support several uses, or may duplicates be collapsed? That is contraction.
3. May an occurrence remain unused in a completed proof? That is weakening.

Do not infer one permission from another. In particular, an unordered context need not be idempotent: linear multisets have exchange without contraction. Also distinguish a rule being **admissible**—every proof using it can be transformed into one without it—from being an explicit object-language connective rule.

## 6. Worked example

Consider a goal that pairs two authorizations, $A\otimes A$.

- In a structural context containing $A$, contraction makes two uses available, so an analogous structural conjunction $A\land A$ can be proved from $A$ by using the same assumption in both branches.
- In a linear context $A\vdash A\otimes A$ is not derivable from tensor right and identity: $\otimes R$ must split the one occurrence between two premises, leaving one branch without $A$.
- From $A,A\vdash A\otimes A$, the split gives one occurrence to each identity premise, so the linear proof succeeds.

Now consider $A,B\vdash B\otimes A$. Exchange allows the linear context to be partitioned as $B$ for the first component and $A$ for the second. In an ordered context $A\,B\vdash B\mathbin{\bullet}A$ generally fails because the only allowed splits preserve the original order.

Finally, $A,B\vdash A$ succeeds structurally by weakening but fails linearly when $B$ has no rule that consumes it.

## 7. Non-example or boundary case

Copying a *name* in ordinary notation is not necessarily logical contraction. Two textual mentions may refer to one immutable structural fact, two linear occurrences, or an alias to a single external object. The context discipline determines the logical meaning.

Likewise, a rule that consumes $A$ and reproduces $A$ is not weakening: it explicitly threads a resource through a transition. Weakening would permit the resource to be ignored altogether.

## 8. Key consequences

- Exchange determines whether contexts are commutative.
- Contraction determines whether multiplicity is observable.
- Weakening determines whether every assumption must be accounted for.
- Structural, linear, and ordered regimes arise from different combinations of these permissions.
- Modal formulas can receive structural permissions selectively inside a substructural system.
- Right rules inherit context discipline: sharing, multiset partition, or ordered splitting.

## 9. Relations to nearby concepts

[Structural Inference](Structural%20Inference.md) uses set-like states and persistent premises. [Linear Inference](Linear%20Inference.md) keeps exchange but makes multiplicity and consumption observable. [Ordered Inference](Ordered%20Inference.md) additionally preserves position. [State Saturation and Quiescence](State%20Saturation%20and%20Quiescence.md) concerns execution closure or stuckness, not structural permission. [CBA Diagrams and True Concurrency](CBA%20Diagrams%20and%20True%20Concurrency.md) visualizes how the absence of contraction gives individual resource occurrences distinct causal paths.

## 10. Common mistakes

- Treating exchange as if it also collapsed duplicates.
- Describing weakening as a state equality.
- Saying contraction only “deletes duplicates”; bottom-up it licenses repeated use.
- Applying structural identity $\Gamma,A\vdash A$ in a linear context.
- Assuming association of concatenation implies exchange.
- Calling $!A$ itself an unrestricted structural context rather than a linear formula governed by special rules.

## 11. What to remember

- Exchange: order does not matter.
- Contraction: one reusable assumption can cover repeated use.
- Weakening: an assumption may go unused.
- Linear contexts retain exchange but reject ordinary contraction and weakening.
- Ordered contexts also reject exchange.
- These are metalevel context principles, even when presented as explicit proof rules.

## 12. Source trail

- Lecture 1, §2 “Structural Inference,” printed pp. L1.2–L1.3, PDF pp. 2–3.
- Lecture 1, §§3–4 “Linear Inference” and “Ordered Inference,” printed pp. L1.4–L1.7, PDF pp. 4–7.
- Lecture 1, §7 “Summary,” printed pp. L1.9–L1.10, PDF pp. 9–10.
- Lecture 2, §5 “Hypothetical Judgments,” printed pp. L2.6–L2.8, PDF pp. 18–20.
- Lecture 2, §§6–8, printed pp. L2.9–L2.13, PDF pp. 21–25.


---
title: "Hypothetical Judgments"
aliases:
  - "Sequent judgments"
  - "Reasoning from assumptions"
tags:
  - judgments
  - sequents
  - contexts
source_lectures:
  - 3
  - 4
prerequisites:
  - "Propositions and inference rules"
related:
  - "Ordered Conjunction and Implications"
  - "Identity and Cut Admissibility"
  - "Proof Terms and Cut Reductions"
---

# Hypothetical Judgments

## 1. One-sentence definition

**A hypothetical judgment $\Omega\vdash A$ asserts that the conclusion $A$ follows from the assumptions in context $\Omega$, with the context’s structural discipline determining how those assumptions may be ordered, used, copied, or discarded.**

## 2. Why the concept is needed

An isolated assertion “$A$ is true” cannot express dependence. Logic and computation often need conditional knowledge: a result follows only if particular resources, inputs, or earlier facts are available. A hypothetical judgment makes that dependency explicit and lets each logic regulate it. The same formulas can behave very differently when hypotheses form a reusable set, a use-once multiset, or a use-once sequence.

It also separates propositions from judgments. $A\backslash B$ is a proposition inside the language; $\Omega\vdash A\backslash B$ is the metalinguistic claim that it has a proof from $\Omega$. Confusing these levels makes it easy to treat an inference rule as a connective or to invent structural rearrangements that the logic forbids.

## 3. Intuitive model

**Intuition.** Think of $\Omega$ as a workbench and $A$ as the required finished object. In structural logic the workbench is a library: items may be consulted repeatedly or ignored. In linear logic it is a bag of parts: every listed part is used once, but their order is irrelevant. In ordered logic it is an assembly line: every part is used once and position matters. The analogy explains dependence, but it is not the formal definition; formal permission comes only from the rules.

## 4. Formal core

Three common forms are

$$
\Gamma\vdash A \quad\text{(structural)},\qquad
\Delta\vdash A \quad\text{(linear)},\qquad
\Omega\vdash A \quad\text{(ordered)}.
$$

$A,B,C$ range over propositions. $\Gamma$ is treated with structural rules such as exchange, contraction, and weakening; $\Delta$ permits exchange but normally neither contraction nor weakening; $\Omega$ is a sequence and permits none of those rules unless explicitly added. $\vdash$ is the turnstile. Its left side is the **antecedent** context and its right side is the single **succedent**. Juxtaposition, as in $\Omega_L A\Omega_R$, inserts $A$ between ordered prefix $\Omega_L$ and suffix $\Omega_R$. $\cdot$ denotes the empty context.

Two fundamental principles are

$$
\frac{}{A\vdash A}\;\mathrm{id}_A
\qquad
\frac{\Omega\vdash A\qquad\Omega_L A\Omega_R\vdash C}
     {\Omega_L\Omega\Omega_R\vdash C}\;\mathrm{cut}_A.
$$

Identity closes the gap between an antecedent and the same succedent. Cut replaces an assumed occurrence of $A$ with a derivation of $A$, preserving the exact position. In a cut-free calculus these displays describe admissible metatheoretic operations, as explained in [Identity and Cut Admissibility](<Identity and Cut Admissibility.md>).

An annotated version is

$$
(x_1:A_1)\cdots(x_n:A_n)\vdash M:A,
$$

where $x_i$ are distinct proof variables and $M$ records the derivation. The declarations remain ordered even though names identify them.

## 5. How to use/read it

Read a sequent from the outside in. First identify the context regime; never assume commas mean the same operation in every logic. In backward proof construction, a right rule decomposes the succedent. A left rule selects a top-level connective in an antecedent and exposes how that assumption can be used. In ordered logic, keep a visible divider around the selected formula so that prefixes and suffixes cannot drift across it.

Operationally, the antecedents are the exact dependencies of a proof term. A derivation of $\Omega\vdash M:A$ certifies not just $M$’s result type but its permitted resource use.

## 6. Worked example

Let $P$ and $Q$ be atomic propositions. We derive

$$P\,(P\backslash Q)\vdash Q.$$

$P\backslash Q$ expects $P$ to its left. The two identities and the left implication rule give

$$
\frac{\overline{P\vdash P}^{\mathrm{id}_P}qquad
      \overline{Q\vdash Q}^{\mathrm{id}_Q}}
     {P\,(P\backslash Q)\vdash Q}\;\backslash L.
$$

Step by step: the first premise proves the required argument $P$; the second says that once the implication yields $Q$, the goal $Q$ is immediate; $\backslash L$ combines those dependencies without reordering them.

## 7. Non-example or boundary case

The reversed sequent $(P\backslash Q)\,P\vdash Q$ is not justified by the same rule. Its $P$ is to the right, while $P\backslash Q$ requires it on the left. Treating $\Omega$ as a multiset would incorrectly validate the sequent by exchange. The corresponding right-looking proposition is $Q/P$, not $P\backslash Q$.

Another boundary: $\cdot\vdash P$ does not follow by identity. Identity requires $P$ as the sole antecedent; it does not create an atomic fact from nothing.

## 8. Key consequences

- Context structure becomes part of the meaning of implication and conjunction.
- Left and right rules can be checked for harmony through identity and cut.
- Ordered sequents model word order and other positional protocols directly.
- Annotated sequents support exact reconstruction of proof dependencies.
- Cut elimination yields a subformula discipline for hypothetical reasoning.

## 9. Relations to nearby concepts

[Ordered Conjunction and Implications](<Ordered Conjunction and Implications.md>) internalize context operations as propositions: fuse internalizes concatenation, while the two implications internalize left- and right-sided extension. [Additive and Multiplicative Connectives](<Additive and Multiplicative Connectives.md>) distinguishes rules that offer alternatives from those that combine separate resource segments. [Proof Terms and Cut Reductions](<Proof Terms and Cut Reductions.md>) enriches the judgment with a witness $M$. [Polarity and Invertibility](<Polarity and Invertibility.md>) determines which side may safely be decomposed during backward reasoning.

## 10. Common mistakes

- Calling $A$ itself a judgment; it is a proposition until placed in a judgment form.
- Assuming every context allows exchange, weakening, or contraction.
- Reading repeated use of a context in additive premises as resource duplication during one execution.
- Forgetting that a single-succedent sequent is intuitionistic.
- Moving an ordered argument across the principal formula.
- Treating admissible identity or cut as necessarily primitive syntax.

## 11. What to remember

- $\Omega\vdash A$ records both a conclusion and its regulated dependencies.
- The kind of context—set-like, multiset-like, or sequential—is semantically significant.
- Left rules use antecedents; right rules establish the succedent.
- In ordered logic, position is never silently exchangeable.
- Annotated judgments add a proof witness without changing the underlying claim.

## 12. Source trail

- Lecture 3, Section 1, printed pp. L3.1–L3.2, PDF pp. 26–27: propositions versus judgments, sequents, antecedents/succedent, and ordered identity/cut.
- Lecture 3, Sections 2–3, printed pp. L3.3–L3.7, PDF pp. 28–32: context-sensitive left and right rules.
- Lecture 4, Section 2, printed pp. L4.1–L4.6, PDF pp. 43–48: annotated hypothetical judgments and distinct antecedent variables.


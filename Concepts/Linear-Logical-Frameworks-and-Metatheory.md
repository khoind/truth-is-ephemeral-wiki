---
title: Linear Logical Frameworks and Metatheoretic Reasoning
aliases:
  - LLF
  - linear logical framework
  - metatheoretic reasoning
tags:
  - llf
  - metatheory
  - logical-frameworks
source_lectures:
  - 21
prerequisites:
  - "[Representing sequent derivations](Representing-Sequent-Derivations.md)"
related:
  - "[CLF and monadic concurrency](CLF-and-Monadic-Concurrency.md)"
  - "[Resource semantics](Resource-Semantics.md)"
---

# Linear Logical Frameworks and Metatheoretic Reasoning

## One-sentence definition

Linear LF extends LF with linear hypotheses and linear connectives so encodings can preserve exact resource use, while metatheoretic reasoning represents transformations such as cut admissibility as total relations over encoded derivations.

## Why the concept is needed

Structural LF permits every local hypothesis to be weakened and contracted, so it cannot directly represent a linear antecedent. LLF adds a linear zone without discarding structural declarations: inference rules must remain reusable. Encoding is only the first goal; one also wants machine-checked claims such as admissibility, preservation, or translation correctness, which require analyzing derivation structure without corrupting the object-level encoding.

## Intuitive model

**Intuition.** LLF has a reusable library shelf for rules and a checkout desk for assumptions that must be returned exactly once. Metareasoning is a verified workshop that transforms complete checkout records. It must inspect representations at a separate level rather than adding illicit inspection to ordinary object-level functions.

## Formal core

LLF adds $A\multimap B$ and both structural and linear assumptions:

$$
A,B::=P\mid A\to B\mid\Pi x:A.B(x)\mid A\multimap B\mid A\mathbin{\&}B,
$$

$$
\Delta::=\cdot\mid\Delta,x_S:A\mid\Delta,x_L:A.
$$

In left focus, a structural function argument may depend only on $\Gamma_S$, whereas a linear function splits linear resources across argument and continuation. SAX constructors can therefore be declared:

```text
lolliR : ΠA:prop. ΠB:prop.
           (ante A -o succ B) -o succ (lolli A B)
lolliX : ΠA:prop. ΠB:prop.
           ante A -o ante (lolli A B) -o succ B
id     : ΠA:prop. ante A -o succ A
```

Additive conjunction $A\mathbin{\&}B$ is needed in the framework so its right inversion can feed the same linear context to both branches without duplicating resources as data.

For structural metatheory, a cut-admissibility relation has type schematically

```text
cutadmit : ΠA. ΠC.
  succ A -> (ante A -> succ C) -> succ C -> type
```

Inputs are two derivations; the final argument is an output derivation. A totality proof shows every well-typed input pair has an output, thereby establishing admissibility constructively.

## How to use/read it

Put reusable signature constants and parameters in the structural zone; put encoded linear antecedents in the linear zone. Select framework connectives whose focusing behavior matches the object rule. For metatheorems, define a relation by cases over proof constructors, then verify totality, termination, and coverage rather than pretending an ordinary weak LF function can inspect proofs.

## Worked example

Derive the usual left rule for object-level `with` from SAX axioms and cut.

1. `withX1` consumes $y:\mathsf{ante}(A\mathbin{\&}B)$ to produce `succ A`.
2. A hypothetical continuation $f:\mathsf{ante}\,A\multimap\mathsf{succ}\,C$ represents $\Delta,A\vdash C$.
3. Encoded cut connects the produced `succ A` to $f$.
4. Abstract linearly over $y$; it occurs exactly once.
5. Abstract over $f$; the result represents transformation of any derivation from $A$ into one from $A\mathbin{\&}B$.

The linear typing rules certify that neither $y$ nor the produced proof is discarded or duplicated.

## Non-example or boundary case

A purported LF function that pattern-matches on arbitrary `succ A` proofs is not available in LF's weak function space. Adding such computation directly would undermine the term/derivation bijection. Metatheoretic case analysis belongs in a separate relational or stronger meta-level mechanism.

## Key consequences

LLF makes substructural adequacy direct. The framework still needs structural declarations for reusable rules. Additives in the framework express shared-context branching. Total relational encodings turn constructive metaproofs into checked algorithms, though substructural metatheory remains harder and less completely understood than structural Twelf practice.

## Relations to nearby concepts

[Representing sequent derivations](Representing-Sequent-Derivations.md) shows the structural baseline. [CLF and monadic concurrency](CLF-and-Monadic-Concurrency.md) adds positive results and concurrent forward steps. [Resource semantics](Resource-Semantics.md) offers another route to substructural metatheory through explicit usage indices.

## Common mistakes

- Making inference-rule declarations linear.
- Using structural implication where exact use is required.
- Duplicating a linear context to encode an additive rule instead of using framework $\mathbin{\&}$.
- Treating object-level cut as the same as a metatheorem of cut admissibility.
- Claiming totality without coverage and termination.

## What to remember

- LLF has structural and linear assumptions.
- Signature rules remain structural.
- Framework focusing must match object inference.
- Metatheorems are often total relations, not ordinary LF functions.
- Object rules and meta-level admissibility stay distinct.

## Source trail

Lecture 21, §3 “A Linear Logical Framework,” printed pp. L21.4–L21.7, PDF pp. 223–226; §4 “Metatheoretic Reasoning,” printed pp. L21.7–L21.8, PDF pp. 226–227.


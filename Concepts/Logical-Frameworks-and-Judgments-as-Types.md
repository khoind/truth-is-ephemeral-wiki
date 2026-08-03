---
title: Logical Frameworks and Judgments as Types
aliases:
  - LF methodology
  - judgments-as-types
  - proofs-as-objects
tags:
  - logical-frameworks
  - lf
  - adequacy
source_lectures:
  - 20
prerequisites:
  - "[Canonical forms and hereditary substitution](Canonical-Forms-and-Hereditary-Substitution.md)"
related:
  - "[Representing sequent derivations](Representing-Sequent-Derivations.md)"
  - "[Linear logical frameworks and metatheory](Linear-Logical-Frameworks-and-Metatheory.md)"
---

# Logical Frameworks and Judgments as Types

## One-sentence definition

A logical framework is a typed metalanguage plus a representation method in which an object-system judgment becomes a type and each derivation of that judgment becomes an object of that type.

## Why the concept is needed

Defining each logic, type system, or operational semantics from scratch duplicates binding, substitution, and proof-checking machinery. LF abstracts these recurring mechanisms. Once an adequate encoding is fixed, checking an object proof reduces to checking the type of its representation, while higher-level algorithms can perform proof search, transformations, or metareasoning over the encoding.

## Intuitive model

**Intuition.** A judgment is a specification for a certificate, and a derivation is the certificate. An inference rule is a constructor that turns certificates for its premises into a certificate for its conclusion. This intuition is precise only when the encoding is adequate: well-typed objects and intended derivations must correspond in both directions.

## Formal core

For graph reachability, declare:

```text
vertex : type
edge   : vertex -> vertex -> type
path   : vertex -> vertex -> type
```

`edge` and `path` are type families indexed by vertices. Rule constants are dependent functions:

```text
step  : Πx:vertex. Πy:vertex. edge x y -> path x y
trans : Πx:vertex. Πy:vertex. Πz:vertex.
          path x y -> path y z -> path x z
```

$\Pi x:A.B(x)$ binds object $x$ of type $A$ in type $B(x)$; $A\to B$ is a nondependent function type. If `eab : edge a b` and `ebc : edge b c`, then

```text
trans a b c (step a b eab) (step b c ebc) : path a c
```

represents the two-step derivation. The LF signature $\Sigma$ contains type-family declarations and proof constructors; the context $\Gamma$ contains local assumptions. The fundamental judgment is $\Gamma\vdash_\Sigma M:A$.

## How to use/read it

Choose the object system's basic judgments first, represent each as a type family, and turn every inference rule into a constructor whose arguments represent premises. Use LF binding for hypothetical derivations and object-language binding. Then prove adequacy: representation preserves and reflects derivations, usually modulo an explicit notion of equality.

## Worked example

Add vertices $a,b,c$ and edges $a\to b$, $b\to c$.

1. `a`, `b`, `c` inhabit `vertex`.
2. `eab : edge a b` and `ebc : edge b c` represent edge facts.
3. `step a b eab` has type `path a b`.
4. `step b c ebc` has type `path b c`.
5. Instantiate `trans` with `a b c` and apply the two path proofs.
6. Type checking returns `path a c`; the object syntax records exactly the rule tree.

No separate proof-checking algorithm for reachability rules is required beyond LF type checking.

## Non-example or boundary case

A general-purpose program of type `path a c` that inspects proof objects in arbitrary ways would not necessarily represent one rule-by-rule derivation. LF deliberately uses weak function spaces and canonical forms to maintain the representation discipline. LF is also structural, so it cannot directly enforce linear use of encoded assumptions.

## Key consequences

Framework type checking implements object proof checking. Dependent types express uniformly quantified rule schemas. Higher-order abstract syntax can delegate binding and substitution to the metalanguage. The framework remains distinct from the represented object logic: framework implication is not automatically object implication.

## Relations to nearby concepts

[Canonical forms and hereditary substitution](Canonical-Forms-and-Hereditary-Substitution.md) explains LF's focused normal forms and total substitution operation. [Representing sequent derivations](Representing-Sequent-Derivations.md) encodes antecedent and succedent judgments separately. [Linear logical frameworks and metatheory](Linear-Logical-Frameworks-and-Metatheory.md) extends the context discipline.

## Common mistakes

- Equating an object proposition with an LF proposition without a representation function.
- Confusing a type family such as `path` with a proof constructor such as `trans`.
- Proving only that derivations map to terms, not the converse.
- Assuming LF's structural context can enforce object-level linearity.
- Treating a logical framework as merely a general theorem prover.

## What to remember

- Judgments become types; derivations become objects.
- Inference rules become typed constructors.
- Dependent products express rule parameters.
- Type checking becomes proof checking only under adequacy.
- Object logic and metalanguage remain separate levels.

## Source trail

Lecture 20, §1 “Introduction” and §2 “Judgments as Types,” printed pp. L20.1–L20.4, PDF pp. 210–213; the role of signatures and LF typing is in §3, printed pp. L20.4–L20.7, PDF pp. 213–216.


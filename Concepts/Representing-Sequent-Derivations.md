---
title: Representing Sequent Derivations
aliases:
  - LF sequent encoding
  - antecedent and succedent judgments
tags:
  - logical-frameworks
  - sequent-calculus
  - adequacy
source_lectures:
  - 21
prerequisites:
  - "[Logical frameworks and judgments as types](Logical-Frameworks-and-Judgments-as-Types.md)"
related:
  - "[Linear logical frameworks and metatheory](Linear-Logical-Frameworks-and-Metatheory.md)"
  - "[Explicit-resource sequent calculus](../Comparisons/Sequent-Calculus-SAX-and-Explicit-Resources.md)"
---

# Representing Sequent Derivations

## One-sentence definition

Representing a sequent derivation in LF maps object propositions to `prop`, antecedent occurrences to assumptions of type `ante A`, the succedent to `succ C`, and each inference step to a framework constructor.

## Why the concept is needed

“Encoding a logic” is underspecified: distinct inference systems for the same connectives have different proof objects. A sequent-calculus encoding must distinguish the two sides of a sequent and preserve hypothetical reasoning, context behavior, and last-rule structure. This makes proof checking and adequacy precise rather than merely encoding formulas.

## Intuitive model

**Intuition.** Formula encodings name the pieces on a board; `ante` and `succ` say which side each piece occupies; rule constructors record legal moves. A typed LF object is then the complete move history. The board analogy does not determine structural versus linear use—that comes from the framework context.

## Formal core

Object propositions use constructors such as:

```text
prop : type
imp  : prop -> prop -> prop
ante : prop -> type
succ : prop -> type
```

For representation function $\ulcorner-\urcorner$, a derivation
$A_1,\ldots,A_n\vdash C$ maps to

$$
x_1:\mathsf{ante}\,\ulcorner A_1\urcorner,\ldots,x_n:\mathsf{ante}\,\ulcorner A_n\urcorner
\vdash_\Sigma \ulcorner D\urcorner:\mathsf{succ}\,\ulcorner C\urcorner.
$$

Implication right is represented by

```text
impR : ΠA:prop. ΠB:prop.
         (ante A -> succ B) -> succ (imp A B)
```

The LF lambda discharges an `ante A` assumption, matching the object rule. A structural implication-left constructor has the shape

```text
impL : ΠA:prop. ΠB:prop. ΠC:prop.
         succ A -> (ante B -> succ C)
         -> (ante (imp A B) -> succ C)
```

Focusing shows that a canonical object headed by `impR` can inhabit only a matching `succ (imp A B)`, supporting the reflection half of adequacy.

## How to use/read it

Define proposition representation first, then one LF type family per basic object judgment, then one constant per inference rule. Check every binder against an object-level discharged assumption. Finally state adequacy for derivations, not merely for end sequents, and specify which proof equalities are identified.

## Worked example

Represent $A\vdash B\supset A$.

1. Context has $x:\mathsf{ante}\,A$.
2. Implication right requires an LF function from $y:\mathsf{ante}\,B$ to a proof of $\mathsf{succ}\,A$.
3. An identity constructor `id : ΠP:prop. ante P -> succ P` uses $x$, not $y$.
4. Form $\lambda y.\mathsf{id}\ A\ x$.
5. Apply `impR A B` to obtain `impR A B (λy. id A x) : succ (imp B A)`.
6. The unused $y$ is legal only because this encoding and LF context are structural; a linear encoding would reject it.

## Non-example or boundary case

Encoding both sides as a single family `true A` erases whether a formula is an antecedent or succedent and cannot directly reflect sequent left/right rules. Likewise, reusing this structural signature for linear logic would incorrectly permit weakening and contraction on encoded linear assumptions.

## Key consequences

Framework focusing supports a bijection between canonical terms and object derivations. Weak framework functions model hypothetical proofs parametrically. Different calculi—ordinary sequent calculus, SAX, or natural deduction—require different constructor signatures even when their propositions coincide.

Propositional variables require their own `prop` declarations in the LF context or signature. This bookkeeping is distinct from assumptions of type `ante A`: one class names formulas, while the other supplies usable object-level hypotheses.

## Relations to nearby concepts

[Logical frameworks and judgments as types](Logical-Frameworks-and-Judgments-as-Types.md) gives the general method. [Linear logical frameworks and metatheory](Linear-Logical-Frameworks-and-Metatheory.md) repairs the structural-context mismatch for linear encodings. [Sequent calculus, SAX, and explicit resources](../Comparisons/Sequent-Calculus-SAX-and-Explicit-Resources.md) distinguishes the systems being represented.

## Common mistakes

- Encoding propositions but not judgments.
- Using one judgment family for both sequent sides.
- Assuming proposition arguments may always be omitted without reconstruction constraints.
- Ignoring the framework's own context regime.
- Calling a map adequate without proving reflection.

## What to remember

- Represent an inference system, not an abstract logic.
- Use separate `ante` and `succ` families.
- LF functions encode discharged assumptions.
- Canonical constructor heads reveal the last encoded rule.
- Context discipline must match the object system.

## Source trail

Lecture 21, §2 “Representing Sequent Derivations,” printed pp. L21.1–L21.4, PDF pp. 220–223.

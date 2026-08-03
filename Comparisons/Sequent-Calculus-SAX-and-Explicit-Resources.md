---
title: Sequent Calculus, SAX, and Explicit-Resource Calculus
aliases:
  - explicit-resource sequent calculus
  - SAX comparison
tags:
  - comparison
  - sequent-calculus
  - resource-semantics
source_lectures:
  - 16
  - 17
  - 19
prerequisites:
  - "[Resource semantics](../Concepts/Resource-Semantics.md)"
related:
  - "[Futures and single assignment](../Concepts/Futures-and-Single-Assignment.md)"
  - "[Representing sequent derivations](../Concepts/Representing-Sequent-Derivations.md)"
---

# Sequent Calculus, SAX, and Explicit-Resource Calculus

## One-sentence definition

Ordinary sequent calculus expresses resource discipline through context formation, SAX replaces selected left rules by axioms and admits restricted cuts, while explicit-resource calculus uses a structural context plus algebraic usage annotations.

## Why the concept is needed

All three systems may present judgments resembling $\Gamma\vdash C$, yet they serve different purposes. Confusing them leads to false claims about cut elimination, runtime allocation, or weakening. The comparison also locates the “explicit-resource sequent calculus” requested by resource semantics: it is a structural target calculus whose annotations recover substructural meaning, not SAX's process language.

## Intuitive model

**Intuition.** Ordinary sequent calculus puts rules on the ledger itself; SAX replaces some multi-step withdrawals with certified vouchers; resource calculus keeps an ordinary copyable ledger but attaches an unforgeable receipt to each conclusion. This is only a memory aid, not a definition.

## Formal core

| Feature | Ordinary cut-free sequent calculus | SAX / SNAX | Explicit-resource calculus |
|---|---|---|---|
| Judgment | $\Delta\vdash C$ | $\Delta\vdash P::(x:C)$ | $\Gamma\vdash C[p]$ |
| Context discipline | built into $\Delta$ | built into typed process inputs | $\Gamma$ structural; $p$ records use |
| Left behavior | general left rules | connective-specific axioms plus cut | rules retain decomposed assumptions structurally but transfer labels |
| Cut | admissible/eliminable metatheoretically | term constructor; some restricted cuts/snips may remain | explicit substitution of resource expressions |
| Computational reading | proof reduction | processes; cut allocates future cell | semantic translation, not primarily a runtime |

The resource cut rule is

$$
\frac{\Gamma\vdash A[q]\qquad \Gamma,A[\alpha]\vdash C[p*\alpha]}
{\Gamma\vdash C[p*q]}\;\mathsf{cut}_\alpha,
$$

where $\alpha$ is fresh. A representative left rule is

$$
\frac{\Gamma,A\otimes B[\gamma],A[\alpha],B[\beta]\vdash C[p*\alpha*\beta]}
{\Gamma,A\otimes B[\gamma]\vdash C[p*\gamma]}.
$$

The principal $A\otimes B$ assumption remains in the structural context, but its label $\gamma$ cannot also occur in the premise receipt.

## How to use/read it

Use ordinary sequent calculus to state proof-theoretic admissibility and cut elimination. Use SAX when interpreting proofs as processes with direct constructor actions. Use explicit-resource calculus when translating substructural derivability into structural predicate logic while retaining an auditable resource expression.

## Worked example

For $A\otimes B\vdash A\otimes B$:

1. Ordinary calculus expands identity: decompose the left tensor, prove atomic identities, rebuild the right tensor.
2. SAX may use a tensor axiom that directly writes or projects the pair, depending on the formulation; a snip can compute a component address relative to the existing layout rather than allocate an unrelated cell.
3. Resource calculus starts from $(A\otimes B)[\gamma]$, introduces $A[\alpha],B[\beta]$, derives $A\otimes B[\alpha*\beta]$, and the left rule replaces $\alpha*\beta$ by $\gamma$ in the conclusion.

The endpoint proposition agrees; proof structure and intended interpretation do not.

## Non-example or boundary case

The fact that $\Gamma$ is structurally weakenable in resource calculus does not make the modeled logic affine: an unused assumption has a label absent from $p$, and adequacy restricts the context to labels in $p$. Likewise, a SAX snip is not unrestricted cut.

## Key consequences

Identity expansion and cut reduction test whether each formulation preserves the intended meaning. In resource calculus, strengthening removes structurally present assumptions whose labels are absent; weakening adds such inert assumptions. In SAX, operational progress reasons about processes and cells, a category absent from the semantic resource calculus.

## Relations to nearby concepts

[Resource semantics](../Concepts/Resource-Semantics.md) explains the annotation algebra. [Futures and single assignment](../Concepts/Futures-and-Single-Assignment.md) supplies SAX's shared-memory interpretation. [Representing sequent derivations](../Concepts/Representing-Sequent-Derivations.md) shows that each inference system needs its own logical-framework signature.

## Common mistakes

- Calling the structural target context itself linear.
- Treating the receipt operator $*$ as tensor.
- Assuming SAX has traditional unrestricted cut elimination.
- Translating a sequent calculus proof and a SAX proof with the same constructors.
- Confusing a semantic interpretation with an operational semantics.

## What to remember

- Context discipline, axiomatic structure, and explicit receipts are three different mechanisms.
- SAX gives proofs process meaning.
- Explicit-resource calculus gives structural proofs substructural annotations.
- Similar endpoints do not imply identical derivations.

## Source trail

Lecture 16, §2, printed pp. L16.2–L16.4, PDF pp. 172–174; Lecture 17, §1, printed p. L17.1, PDF p. 180; Lecture 19, §2, printed pp. L19.2–L19.5, PDF pp. 202–205.


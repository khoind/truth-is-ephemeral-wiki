---
title: Canonical Forms and Hereditary Substitution
aliases:
  - LF canonical forms
  - hereditary substitution
  - spine calculus
tags:
  - lf
  - canonical-forms
  - substitution
source_lectures:
  - 20
prerequisites:
  - "[Logical frameworks and judgments as types](Logical-Frameworks-and-Judgments-as-Types.md)"
related:
  - "[Partial focusing](Partial-Focusing.md)"
  - "[Representing sequent derivations](Representing-Sequent-Derivations.md)"
---

# Canonical Forms and Hereditary Substitution

## One-sentence definition

LF canonical forms are focused, beta-normal and eta-long objects, and hereditary substitution replaces a variable while immediately reducing any redex created so the result remains canonical.

## Why the concept is needed

Ordinary capture-avoiding substitution is not closed over LF's canonical syntax. Replacing a head variable by a lambda can create an application whose head is no longer a constant or variable, so the result is neither grammatical nor normal. Hereditary substitution combines substitution with normalization and uses the substituted variable's type to prove termination.

## Intuitive model

**Intuition.** Canonical syntax stores a function call as a head plus a queue of arguments called a spine. If substitution replaces the head with a lambda, hereditary substitution immediately feeds the queue to that lambda instead of leaving a redex behind. It is normalization during replacement, not an unrestricted evaluator.

## Formal core

LF's negative canonical grammar is:

$$
\begin{aligned}
A,B&::=P\mid A\to B\mid\Pi x:A.B(x),\\
M&::=c\,S\mid x\,S\mid\lambda x.M,\\
S&::=(M;S)\mid().
\end{aligned}
$$

$c$ is a signature constant, $x$ a variable, $P$ an atomic type, and $S$ a spine. Right inversion produces lambdas; left focus consumes a function through its spine; focus ends at a suspended atom. These are **canonical forms** because introduction structure is exposed and no beta redex remains.

Hereditary substitution is written $[M/x]^A N$, indexed by the type $A$ of $x$. Key clauses are:

$$
\begin{aligned}
[M/x]^A(hS)&=h([M/x]^A S) && h\ne x,\\
[M/x]^A(xS)&=M\mathbin{|_A}([M/x]^A S),\\
(\lambda y.N)\mathbin{|_{A\to B}}(M';S)&=[M'/y]^A N\mathbin{|_B}S,\\
(hS)\mathbin{|_P}()&=hS.
\end{aligned}
$$

$|_A$ is typed spine application. Termination uses a lexicographic induction: first on type $A$, then on the object/spine being traversed. Function application recurses at smaller result type $B$.

## How to use/read it

When substituting under lambdas, rename binders to avoid capture. Recurse structurally until the replaced variable occurs as a head. Then switch to typed application, consuming its substituted spine and reducing lambdas immediately. An undefined case signals a type mismatch; well-typed uses compute.

## Worked example

Let $x:P\to Q$, $f:Q\to R$, and substitute $\lambda z.f(z)$ for $x$ in canonical object $x(a;())$, where $a:P$.

1. The head matches $x$, so calculate
   $(\lambda z.f(z))|_{P\to Q}(a;())$.
2. Consume argument $a$ and beta-reduce by hereditary substitution:
   $[a/z]^P f(z)$.
3. Since head $f\ne z$, retain it and substitute in its spine.
4. The argument $z$ becomes $a$.
5. Result: $f(a;())$, a canonical head-spine object with no intermediate $(\lambda z.fz)\,a$ redex.

## Non-example or boundary case

Naively producing `(λz. f z) (a; ())` is not an LF canonical object because lambdas are not allowed at the head of a spine. Hereditary substitution may also be undefined for ill-typed input; computability is not a claim that every arbitrary syntax combination has a result.

## Key consequences

Canonical syntax supports syntax-directed type checking and tight proof encodings. Hereditary substitution is the computational content of focused cut elimination for the negative fragment. Weak function spaces remain parametric because their only computation is this typed substitution.

Because normal forms are maintained by construction, adequacy proofs can inspect a canonical object's head to recover its final encoded inference rule; they do not first need a separate normalization theorem for arbitrary framework terms.

## Relations to nearby concepts

[Logical frameworks and judgments as types](Logical-Frameworks-and-Judgments-as-Types.md) supplies the representation purpose. [Partial focusing](Partial-Focusing.md) similarly derives normal observable forms, but for compound positive data. [Representing sequent derivations](Representing-Sequent-Derivations.md) relies on canonical head constructors to reflect the last object-rule step.

## Common mistakes

- Calling beta-normal alone canonical while ignoring eta expansion/focused form.
- Performing raw textual substitution.
- Dropping the type index $A$ from the termination argument.
- Treating spines as ordinary lists without typed application.
- Claiming hereditary substitution is defined on all ill-typed syntax.

## What to remember

- Canonical LF objects are heads, spines, and lambdas in focused normal form.
- Substitution must preserve that grammar.
- Hereditary substitution reduces redexes as it substitutes.
- The type index makes termination visible.
- It operationalizes cut elimination.

## Source trail

Lecture 20, §3 “The Formal Metalanguage,” printed pp. L20.4–L20.7, PDF pp. 213–216; §4 “Hereditary Substitution,” printed pp. L20.7–L20.8, PDF pp. 216–217.

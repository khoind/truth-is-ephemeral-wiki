---
title: "Proof Terms and Cut Reductions"
aliases:
  - "Term-annotated proofs"
  - "Proof-term normalization"
tags:
  - proof-terms
  - binders
  - cut-reduction
  - ordered-logic
source_lectures:
  - 4
prerequisites:
  - "Hypothetical judgments"
  - "Identity and cut admissibility"
related:
  - "Ordered Conjunction and Implications"
  - "Identity and Cut Admissibility"
  - "Polarity and Invertibility"
---

# Proof Terms and Cut Reductions

## 1. One-sentence definition

**A proof term is a rule-by-rule linear encoding of a sequent derivation, and a cut reduction is a typed rewrite that replaces an introduction immediately consumed by its matching elimination with interactions on smaller proofs.**

## 2. Why the concept is needed

Proof trees are spatial objects: premises spread across a page, rule labels sit between rows, and repeated transformations require redrawing large fragments. A term makes the structure portable and manipulable. It can be checked, compared up to bound-variable renaming, stored as syntax, and rewritten locally. Explicit terms also clarify which antecedent a left rule uses—essential when several assumptions share a type—and prepare proofs for a computational reading.

## 3. Intuitive model

**Intuition.** A proof term is an abstract syntax tree whose constructor names say which proof rule was used. A binder is a labelled socket for the result made available in a premise. A cut plugs a producer into such a socket. Reduction opens matching packaging and consumption operations. This resembles evaluation, but Lecture 4 still treats terms primarily as proof records rather than concrete run-time processes.

## 4. Formal core

The annotated judgment

$$
(x_1:A_1)\cdots(x_n:A_n)\vdash M:A
$$

states that proof term $M$ establishes $A$ using the ordered, distinctly labelled assumptions on the left. $x_i$ are proof variables; $A_i,A$ are propositions; $M,N,P$ are metavariables for proof terms.

Representative constructors and rules are:

$$\overline{(x:A)\vdash \mathsf{Id}\,x:A}^{\mathrm{id}},$$

$$
\frac{(x:A)\Omega\vdash M:B}
     {\Omega\vdash \backslash R(x.M):A\backslash B},
$$

$$
\frac{\Omega_A\vdash M:A\qquad\Omega_L(y:B)\Omega_R\vdash P:C}
     {\Omega_L\Omega_A(x:A\backslash B)\Omega_R
       \vdash \backslash L\,x\,M\,(y.P):C},
$$

$$
\frac{\Omega_1\vdash M:A\qquad\Omega_2\vdash N:B}
     {\Omega_1\Omega_2\vdash\bullet R\,M\,N:A\bullet B},
$$

$$
\frac{\Omega_L(y:A)(z:B)\Omega_R\vdash P:C}
     {\Omega_L(x:A\bullet B)\Omega_R
       \vdash\bullet L\,x\,(y.z.P):C}.
$$

In $x.M$, the dot binds $x$ in $M$. Terms differing only by consistent renaming of bound variables are alpha-equivalent. Freshness means a newly bound name is distinct from all declarations already in scope.

Cut is

$$
\frac{\Omega\vdash M:A\qquad\Omega_L(x:A)\Omega_R\vdash P:C}
     {\Omega_L\Omega\Omega_R\vdash\mathsf{Cut}_A M(x.P):C}.
$$

Its fuse principal reduction is

$$
\mathsf{Cut}_{A\bullet B}(\bullet R M N)
 (x.\bullet L x(y.z.P))
\longrightarrow_R
\mathsf{Cut}_B N(z.\mathsf{Cut}_A M(y.P)).
$$

The subscript $R$ marks a principal reduction relation, not a right inference rule here.

## 5. How to use/read it

Read constructors from outside inward to reconstruct a derivation bottom-up. The outer constructor determines the last rule. Its arguments determine premise terms; binders determine fresh antecedent declarations. In a left constructor, the first variable identifies the principal antecedent.

To type-check in ordered logic, track free variables and ensure each multi-premise constructor receives the proper consecutive context segment. Names identify assumptions but do not authorize reordering. Given the labelled context, term, and result type, there is at most one valid derivation; malformed terms simply have none.

To reduce a cut, inspect the producer’s outer right constructor and the consumer’s matching left constructor. Replace the compound interaction with the stated smaller cuts, renaming bound variables first if needed to avoid capture.

## 6. Worked example

Start with $m:A$ and $n:B$. Package them:

$$m:A,n:B\vdash \bullet R(\mathsf{Id}\,m)(\mathsf{Id}\,n):A\bullet B.$$

Define a consumer that unpacks $u:A\bullet B$ and returns the same ordered pair:

$$u:A\bullet B\vdash
\bullet L u(a.b.\bullet R(\mathsf{Id}\,a)(\mathsf{Id}\,b)):A\bullet B.$$

Cutting producer to consumer and applying the principal rule yields

$$
\mathsf{Cut}_B(\mathsf{Id}\,n)
 (b.\mathsf{Cut}_A(\mathsf{Id}\,m)
 (a.\bullet R(\mathsf{Id}\,a)(\mathsf{Id}\,b))).
$$

The inner identity cut replaces $a$ by the provided $m$ proof; the outer identity cut similarly supplies $n$. The normal result is the original packaging term. The trace demonstrates type decrease first, followed by identity cancellation.

## 7. Non-example or boundary case

$\bullet L u(a.b.\mathsf{Id}\,a)$ is not a valid proof from only $u:A\bullet B$ in pure ordered logic: unpacking exposes both $a:A$ and $b:B$, but the term ignores $b$. There is no weakening rule to discard it.

Likewise, $\bullet R(\mathsf{Id}\,n)(\mathsf{Id}\,m)$ cannot inhabit $A\bullet B$ under context $m:A,n:B$. Its components have the wrong types and order. Variable names make references explicit; they do not relax the context discipline.

## 8. Key consequences

- Terms and suitably marked derivations determine one another uniquely.
- Alpha-renaming removes irrelevant choices of bound names.
- Cut elimination can be presented as local typed rewriting.
- Free-variable analysis supports context-splitting during checking.
- A non-atomic identity or cut may denote a metalevel proof transformation rather than an object constructor.
- Nondeterministic commuting reductions make normalization naturally relational.

## 9. Relations to nearby concepts

[Hypothetical Judgments](<Hypothetical Judgments.md>) is the unannotated form of the typing judgment. [Ordered Conjunction and Implications](<Ordered Conjunction and Implications.md>) explains the positional rules that constructors encode. [Identity and Cut Admissibility](<Identity and Cut Admissibility.md>) supplies the metatheorem implemented by reductions. [Polarity and Invertibility](<Polarity and Invertibility.md>) organizes constructors by whether their right or left behavior may be applied eagerly during proof search.

A proof term is not automatically a value, process, or message. It is proof syntax. Later operational semantics may reinterpret constructors, but those categories should remain distinct until a translation or semantics explicitly relates them.

## 10. Common mistakes

- Treating a bound variable as globally declared.
- Forgetting freshness or capture avoidance during rewriting.
- Believing names permit ordered assumptions to exchange.
- Assuming every syntactic term has a typing derivation.
- Replacing the stated nested-cut reduction silently by ordinary substitution.
- Confusing one-to-one proof encoding with uniqueness of proofs for a proposition.
- Claiming cut reduction is deterministic.

## 11. What to remember

- One rule application corresponds to one named constructor.
- Antecedent variables identify resources; binders delimit local scope.
- Valid terms retain enough information to reconstruct proofs.
- Principal reduction matches a right constructor against its left constructor.
- Compound cuts become cuts at smaller types.
- Proof syntax precedes, but enables, computational interpretation.

## 12. Source trail

- Lecture 4, Sections 1–2, printed pp. L4.1–L4.6, PDF pp. 43–48: motivation, annotated sequents, binders, examples, reconstruction, and fuse terms.
- Lecture 4, Section 3, printed pp. L4.6–L4.7, PDF pp. 48–49: cut constructor and principal fuse reduction.
- Lecture 4, Section 6 and Figure 1, printed pp. L4.9–L4.10, PDF pp. 51–52: full term grammar and metalevel reading.

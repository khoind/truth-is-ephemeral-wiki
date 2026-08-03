---
title: "Lecture 20 — Logical Frameworks"
lecture: 20
date: 2023-11-28
pdf_pages: "210–219"
printed_pages: "L20.1–L20.10"
tags:
  - lecture-guide
  - logical-frameworks
  - lf
prerequisites:
  - "[Logical frameworks and judgments as types](../Concepts/Logical-Frameworks-and-Judgments-as-Types.md)"
---

# Lecture 20 — Logical Frameworks

## 1. Why this lecture exists

The course shifts from studying one logic to metalanguages for defining many deductive systems. LF turns judgments into types and proofs into objects, so framework type checking becomes object proof checking under an adequate representation. Focusing explains LF's canonical syntax; hereditary substitution preserves it during dependent application.

## 2. Learning objectives

- distinguish a logical framework from an object logic and general theorem prover;
- encode judgments, facts, and rules as types and constructors;
- read dependent products, kinds, signatures, objects, and spines;
- explain canonical LF syntax through focusing;
- compute a hereditary substitution; and
- state the adequacy obligation.

## 3. Dependency map

Deductive judgments $\rightarrow$ [judgments as types](../Concepts/Logical-Frameworks-and-Judgments-as-Types.md). Negative focusing $\rightarrow$ canonical objects and spines. Dependent application $\rightarrow$ [hereditary substitution](../Concepts/Canonical-Forms-and-Hereditary-Substitution.md). Structural LF limitation $\rightarrow$ [Lecture 21](Lecture-21-Substructural-Frameworks.md).

## 4. Section-by-section reconstruction covering every numbered heading

### 1 Introduction

A logical framework combines a formal metalanguage and representation methodology. LF targets deductive systems specifically. It supports definitions, algorithms such as proof checking/search and translation, and metareasoning. LF is structural; LLF and CLF extend it for substructural and concurrent systems. This lecture emphasizes definition and proof checking.

### 2 Judgments as Types

`vertex : type`, `edge : vertex -> vertex -> type`, and `path : vertex -> vertex -> type` turn graph judgments into indexed type families. Facts are proof constants. Inference rules become constructors. $\Pi x:A.B(x)$ expresses a rule schema indexed by an object of type $A$. A term headed by `trans` with two path arguments represents exactly a transitivity derivation.

### 3 The Formal Metalanguage

LF uses negative atomic, function, and dependent-function types. Signature declarations act as reusable antecedents. Left focusing chooses a constant/variable and consumes its function type with a spine; right inversion creates lambdas; focus closes at a matching suspended atom. Canonical objects are constant/variable heads with spines or lambdas. Kinds classify type families, and signatures contain family and term constructors. Adequacy requires a bijection between intended derivations and well-typed canonical objects.

### 4 Hereditary Substitution

Raw substitution can create a beta redex outside canonical grammar. Hereditary substitution $[M/x]^A N$ is indexed by $x$'s type, substitutes recursively, and when $x$ occurs as a head invokes typed spine application. A lambda consumes the next spine argument and recursively substitutes at a smaller type. Nested induction on type and syntax establishes termination; the operation can remain undefined on ill-typed inputs.

## 5. Formal core

$$
\begin{aligned}
A,B&::=P\mid A\to B\mid\Pi x:A.B(x),\\
M&::=cS\mid xS\mid\lambda x.M,\\
S&::=(M;S)\mid(),\\
\Sigma&::=\cdot\mid\Sigma,a:K\mid\Sigma,c:A.
\end{aligned}
$$

$P$ is atomic, $M$ an object, $S$ a spine, $K$ a kind, $c$ a proof constructor, and $a$ a type-family constructor. The main judgment is $\Gamma\vdash_\Sigma M:A$. For a function, $\Gamma,x:A\vdash M(x):B$ yields $\Gamma\vdash\lambda x.M(x):A\to B$.

## 6. Operational/computational reading

Type checking a canonical object verifies its derivation tree. Focusing gives syntax-directed checking: lambdas correspond to invertible right rules; a head selects one signature rule; the spine supplies its parameters and premises. Computation is deliberately weak and consists chiefly of hereditary substitution, maintaining parametric encodings.

## 7. Worked derivation or trace in original notation and prose

With `eab : edge a b` and `ebc : edge b c`:

1. `step a b eab : path a b`.
2. `step b c ebc : path b c`.
3. Instantiate `trans` at $a,b,c$.
4. Its first spine argument checks as `path a b`.
5. Its second checks as `path b c`.
6. Therefore `trans a b c (step a b eab) (step b c ebc) : path a c`.

The head `trans` identifies the last object-rule step; the two subobjects encode its premises.

### Extended reconstruction: representation, canonicality, and substitution

**Section 1** distinguishes three layers. The *object system* is the graph calculus, sequent calculus, or language being represented. LF is the *framework metalanguage* in which its judgments and rules are declared. An LF implementation supplies a further tool layer for parsing, type checking, and search. A framework is therefore not automatically a theorem prover for every encoded logic: the signature defines legal derivations, while separate algorithms decide how to construct or analyze them.

**Section 2** applies the judgments-as-types principle precisely. A declaration `path : vertex -> vertex -> type` is a family of types indexed by endpoints. The type `path a c` represents the proposition that a path judgment holds; an inhabitant represents one derivation of that judgment. A fact such as an edge becomes a constant whose type is the corresponding judgment instance. A rule becomes a constant with function type from representations of premises to the representation of its conclusion. Dependent product $\Pi x:A.B(x)$ is needed when the conclusion or later premises mention the object chosen for $x$. Ordinary $A\to B$ is the nondependent case.

This encoding uses higher-order abstract syntax when an object-level binder is represented by an LF binder. Framework substitution then implements capture-avoiding object substitution. That convenience carries an adequacy obligation: exotic LF functions must not represent unintended object syntax. Canonical LF's weak, parametric function space and the shape of the signature are what support the correspondence; it cannot simply be assumed from suggestive constructor names.

**Section 3** organizes LF around canonical forms. Kinds classify type families: `type` is the kind of ordinary LF types, and $\Pi x:A.K(x)$ classifies an indexed family. A signature $\Sigma$ is a persistent collection of family declarations $a:K$ and object constants $c:A$. A local context $\Gamma$ contains variables introduced while checking one object. In

$$\Gamma\vdash_\Sigma M:A,$$

$M$ is checked using both sources, but signature constants are globally reusable.

Negative focusing explains the grammar. To prove a function type on the right, inversion introduces a lambda. To prove an atomic type, checking focuses on a head constant or variable. Its spine is the ordered list of arguments that eliminates all function or dependent-product layers until the resulting atomic type matches the goal. Thus `c S` is not arbitrary application syntax: $c$ determines the final rule constructor, and $S$ records its parameters and premise derivations. Beta-normality removes computational detours, while eta-longness ensures function objects reveal their lambdas.

Adequacy is usually split into representation and uniqueness claims. Every intended derivation must map to a well-typed canonical object; every such object must decode to an intended derivation; and the two maps should be inverse up to the chosen equality of derivations. Type soundness of LF alone proves none of these object-specific claims. Focusing helps reflection because an inhabitant of an atomic judgment must have a head drawn from the declarations capable of concluding it.

**Section 4** repairs closure of canonical syntax under substitution. Suppose $x:A\to B$ is replaced by canonical $\lambda y.N$. Raw substitution into $x\,M$ creates $(\lambda y.N)M$, a beta redex and therefore not a canonical object. Hereditary substitution immediately reduces it to $[M/y]^A N$, recursively normalizing any new redexes. The type index on $[M/x]^A(-)$ controls termination: when application exposes a lambda, recursion proceeds at a proper substructure of $A$ even if the resulting term is not syntactically smaller.

For an original concrete calculation, let

$$F=\lambda p.\,\mathsf{trans}\ a\ b\ c\ p\ (\mathsf{step}\ b\ c\ e_{bc})$$

have type $\mathsf{path}\ a\ b\to\mathsf{path}\ a\ c$, and let $N=\mathsf{step}\ a\ b\ e_{ab}$. Applying $F$ to $N$ through a spine cannot leave the raw redex $F\,N$. Hereditary application opens the lambda, substitutes $N$ for $p$, and returns

$$\mathsf{trans}\ a\ b\ c\ N\ (\mathsf{step}\ b\ c\ e_{bc}),$$

which is again headed by a signature constant and has a canonical spine. Type checking the spine verifies endpoint indices: the first path ends at $b$, the second begins at $b$, and the resulting index is `path a c`. An endpoint mismatch makes hereditary application undefined on that ill-typed input rather than manufacturing a term.

The computational reading is deliberately intensional. A canonical object's head reveals its final inference rule, so proof checking recursively checks premises. Search can run this relationship in the other direction, but termination and completeness depend on the signature. Definitional equality is handled through canonicalization and hereditary substitution, not through unrestricted runtime evaluation.

Additional checks: **Is `path a b` a derivation?** No, it is a type representing a judgment; an inhabitant is the derivation. **Why are spines useful?** They make focused elimination and dependency propagation explicit. **Can two canonical terms encode the same proof?** That depends on the chosen object proof equality and the adequacy theorem. **Why index substitution by a type?** To justify termination when reduction recurses on a smaller function domain/codomain structure.

A useful checking trace separates synthesis from dependency. Looking up `trans` supplies a dependent function type with endpoint parameters followed by two proof arguments. Feeding the endpoint objects specializes the remaining type; feeding the first path proof substitutes its indices into what follows; feeding the second finishes the spine and produces an atomic result. At every stage the framework compares canonical indices, so an apparently plausible proof term is rejected as soon as adjacent endpoints disagree.

Canonical syntax also supports inversion principles used later. If a closed canonical object has atomic type `path a c`, it cannot be a lambda. Its head must be a variable from the local context or a signature constant whose result specializes to that family. In an empty local context, only declared path constructors are possible. This finite head analysis is the foundation for decoding LF objects back into object derivation trees.

## 8. Conceptual synthesis

LF makes the structure common to deductive systems executable while separating metalanguage and object language. Focusing is not merely a proof-search optimization here: it determines the canonical representation whose heads reflect inference rules. Dependent types express indexed judgments, and hereditary substitution preserves their normal forms.

## 9. Common confusions and failure modes

- Framework implication and object implication are different layers.
- A type family is a judgment form, not a proof.
- Canonical terms cannot contain unreduced beta redexes.
- Raw substitution is insufficient.
- Well-typed terms correspond to derivations only after adequacy is established.

## 10. Self-test questions with concise answers

1. **What represents a judgment instance?** An LF type.
2. **What represents an inference rule?** A typed signature constant.
3. **Why use $\Pi$?** The conclusion type may depend on the rule parameter.
4. **What is a spine?** The ordered sequence of arguments eliminating a focused head type.
5. **Why hereditary substitution?** It substitutes while preserving canonical normal form.

## 11. Related concept pages

- [Logical frameworks and judgments as types](../Concepts/Logical-Frameworks-and-Judgments-as-Types.md)
- [Canonical forms and hereditary substitution](../Concepts/Canonical-Forms-and-Hereditary-Substitution.md)
- [Representing sequent derivations](../Concepts/Representing-Sequent-Derivations.md)

## 12. Source trail

Lecture 20 “Logical Frameworks”: §1, printed pp. L20.1–L20.2, PDF pp. 210–211; §2, L20.2–L20.4, PDF pp. 211–213; §3, L20.4–L20.7, PDF pp. 213–216; §4, L20.7–L20.8, PDF pp. 216–217; references, L20.9–L20.10, PDF pp. 218–219.

## 13. Previous/next navigation

Previous: [Lecture 19 — Resource Semantics](Lecture-19-Resource-Semantics.md). Next: [Lecture 21 — Substructural Frameworks](Lecture-21-Substructural-Frameworks.md).


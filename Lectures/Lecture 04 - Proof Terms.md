---
title: "Proof Terms"
lecture: 4
date: "September 7, 2023"
pdf_pages: "43–53"
printed_pages: "L4.1–L4.11"
tags:
  - proof-terms
  - ordered-logic
  - cut-reduction
  - polarity
prerequisites:
  - "Lecture 3 — Cut and Identity Elimination"
  - "Ordered sequent calculus"
---

# Lecture 4 — Proof Terms

## 1. Why this lecture exists

A two-dimensional proof tree displays logical structure well, but it is cumbersome to store, compare, transform, or execute. Lecture 4 gives each inference rule a term constructor so that a derivation becomes a compact, first-class object. The annotation is not merely decorative: with distinctly named antecedents and explicit binders, a valid term determines its derivation. Cut reduction can then be stated as a local rewrite on terms, and identity expansion reveals which side of each connective is invertible. This is the bridge from proof theory to the computational interpretation developed in later lectures.

## 2. Learning objectives

After this lecture, a reader should be able to:

- read the annotated judgment $\Omega\vdash M:A$;
- explain why ordered assumptions receive distinct variable names;
- distinguish free antecedent variables from variables bound by a rule constructor;
- annotate the rules for $\backslash$, $/$, and $\bullet$ with proof terms;
- translate a principal cut reduction from proof trees to a term rewrite;
- distinguish an invertible rule from a connective that is invertible on one side;
- classify ordered, linear, and structural connectives by polarity.

## 3. Dependency map

[Hypothetical judgments](<../Concepts/Hypothetical Judgments.md>) supply the sequent. [Ordered conjunction and implications](<../Concepts/Ordered Conjunction and Implications.md>) supply the rules being annotated. [Identity and cut admissibility](<../Concepts/Identity and Cut Admissibility.md>) justifies transformation of proofs. This lecture internalizes derivation structure as [proof terms and cut reductions](<../Concepts/Proof Terms and Cut Reductions.md>) and uses identity expansion to motivate [polarity and invertibility](<../Concepts/Polarity and Invertibility.md>).

## 4. Section-by-section reconstruction covering every numbered heading

### 1. Introduction

Cut-free proofs give propositions their compositional meaning, so proofs themselves deserve an explicit notation. A satisfactory notation must retain enough information to reconstruct the proof tree and must work despite structural differences among ordered, linear, and structural contexts. Lecture 4 initially treats terms neutrally: they record proofs. Their execution becomes central only when later lectures interpret cuts as interacting processes.

### 2. Annotating the Sequent

The annotated judgment is

$$
(x_1:A_1)\cdots(x_n:A_n)\vdash M:A.
$$

$M$ is a proof term for the succedent $A$. Each antecedent receives a distinct variable $x_i$. Numerical positions would be brittle: a rule can split a context, and linear exchange can change positions. Names remain stable through those transformations.

For left implication, the right rule introduces a fresh assumed $x:A$ and binds it in the premise term:

$$
\frac{(x:A)\,\Omega\vdash M:B}
     {\Omega\vdash \backslash R(x.M):A\backslash B}\;\backslash R.
$$

The notation $x.M$ is a binder: occurrences of $x$ in $M$ refer to the newly introduced antecedent, and renaming bound $x$ consistently does not change the proof. The matching left constructor names the implication being used, records a proof of its argument, and binds the produced result:

$$
\frac{\Omega_A\vdash M:A \qquad
      \Omega_L(y:B)\Omega_R\vdash P:C}
     {\Omega_L\Omega_A(x:A\backslash B)\Omega_R
       \vdash \backslash L\,x\,M\,(y.P):C}\;\backslash L.
$$

The $/$ rules mirror these positions:

$$
\frac{\Omega(x:A)\vdash M:B}{\Omega\vdash /R(x.M):B/A}\;/R
$$

$$
\frac{\Omega_A\vdash M:A \qquad \Omega_L(y:B)\Omega_R\vdash P:C}
     {\Omega_L(x:B/A)\Omega_A\Omega_R\vdash /L\,x\,M\,(y.P):C}\;/L.
$$

Identity uses an explicit constructor, $(x:A)\vdash \mathsf{Id}\,x:A$, rather than treating every variable as an implicit term. This keeps the correspondence “one inference rule, one constructor” uniform.

The lecture annotates the ordered implication equivalence from Lecture 3 step by step. Fresh variables are first assigned bottom-up where rules create assumptions; constructors are then assembled top-down from the identities. The result contains enough information to recover the complete derivation.

Two correspondence claims capture this precision. Given a uniquely labelled $\Omega$, term $M$, and type $A$, there is at most one derivation of $\Omega\vdash M:A$. Conversely, once applications of left rules in an unannotated proof identify their target variables, exactly one proof term annotates it. Checking still has an algorithmic subtlety: a multi-premise rule must determine how an ordered context is divided. One can inspect free-variable occurrences or thread unused inputs onward, provided each premise consumes a consecutive segment.

For fuse, $\bullet R$ builds a pair-like proof without binding:

$$
\frac{\Omega_1\vdash M:A\qquad\Omega_2\vdash N:B}
     {\Omega_1\Omega_2\vdash \bullet R\,M\,N:A\bullet B}.
$$

$\bullet L$ pattern-matches an antecedent and binds its two ordered components:

$$
\frac{\Omega_L(y:A)(z:B)\Omega_R\vdash P:C}
     {\Omega_L(x:A\bullet B)\Omega_R
       \vdash \bullet L\,x\,(y.z.P):C}.
$$

The order $y$ then $z$ is part of the term’s meaning.

### 3. Cut Reductions on Proof Terms

Cut also receives a constructor:

$$
\frac{\Omega\vdash M:A\qquad\Omega_L(x:A)\Omega_R\vdash P:C}
     {\Omega_L\Omega\Omega_R\vdash \mathsf{Cut}_A\,M\,(x.P):C}.
$$

When a fused value built by $\bullet R$ meets a consumer using $\bullet L$, the proof-tree reduction becomes the term rewrite

$$
\mathsf{Cut}_{A\bullet B}(\bullet R\,M\,N)
  (x.\bullet L\,x\,(y.z.P))
\longrightarrow_R
\mathsf{Cut}_B\,N\,(z.\mathsf{Cut}_A\,M\,(y.P)).
$$

The single cut on $A\bullet B$ is replaced by cuts on the proper subformulas $A$ and $B$. This resembles pattern matching, but at this stage it is deliberately expressed through smaller cuts rather than ordinary capture-avoiding substitution.

### 4. Invertibility and Polarity

Bottom-up proof construction presents choices: a right rule may decompose the succedent, or a left rule may decompose any matching antecedent. Cut elimination implies termination for finite propositional ordered logic because every cut-free rule application reduces the total number of connectives. It does not remove branching, however.

A rule is invertible when provability of its conclusion implies provability of every premise; the rule itself already gives the converse direction. Applying an invertible rule bottom-up therefore preserves provability exactly. Identity expansion supplies a useful test: the side decomposed first in the expanded identity indicates the invertible side. For $A\bullet B$, $\bullet L$ comes first and is invertible; $\bullet R$ cannot always split the antecedents successfully.

Nullary rules expose a wording trap. $1R$ has no premises, so it is vacuously invertible as a rule, yet it cannot be applied whenever $1$ is the succedent because the antecedent must be empty. It is clearer to classify a **connective** by whether its relevant rule can always be applied at top level without losing provability.

Right-invertible connectives are called **negative**; left-invertible connectives are **positive**. In ordered logic, the implications, external choice, and $\top$ are negative. Fuse, twist, $1$, internal choice, and $0$ are positive.

### 5. A Zoo of Connectives

Structural rules can collapse distinctions that substructural logics expose. Ordered left and right implications $A\backslash B$ and $B/A$ coincide as linear implication $A\multimap B$ once exchange makes direction irrelevant. Ordered fuse and twist coincide as linear tensor $A\otimes B$. Linear logic retains two conjunction-like connectives: positive tensor $A\otimes B$ and negative external choice $A\mathbin{\&}B$. Structural conjunction $A\land B$ conflates them because contraction and weakening make both styles available.

The units split similarly. Linear and ordered $1$ is positive, while $\top$ is negative; structural truth hides that distinction. Internal choice $\oplus$ and falsehood $0$ remain positive. The polarity split has a computational forecast: positive data behaves eagerly and is revealed by pattern matching, while negative data behaves lazily and is observed by requesting one of its behaviors.

### 6. Summary

Rule-named constructors provide a lossless linear notation for derivations. Operations previously shown as tree transformations become relations or rewrites over terms. If general identity and cut are absent from the object calculus, $\mathsf{Id}_A$ for non-atomic $A$ and $\mathsf{Cut}_A$ should be understood as metalevel operations that produce cut-free proofs. Because reductions may commute in several valid orders, cut normalization is best treated as a relation, not assumed to be a deterministic evaluator.

## 5. Formal core (rules/judgments/theorems, with each symbol explained)

The judgment $\Omega\vdash M:A$ has four ingredients:

- $\Omega$ is an ordered sequence of declarations $(x_i:A_i)$ with pairwise distinct variables;
- $M$ is a proof term;
- $A$ and every $A_i$ are propositions;
- $\vdash$ asserts that $M$ proves $A$ using exactly the declarations in $\Omega$ in their permitted order.

Core term forms include

$$
\begin{aligned}
M,N,P ::= {}& \mathsf{Id}\,x
\mid \mathsf{Cut}_A\,M\,(x.P)\\
&\mid \backslash R(x.M)
\mid \backslash L\,x\,M\,(y.P)\\
&\mid /R(x.M)
\mid /L\,x\,M\,(y.P)\\
&\mid \bullet R\,M\,N
\mid \bullet L\,x\,(y.z.P)\mid\cdots.
\end{aligned}
$$

$x,y,z$ range over proof variables. A dot marks binding; for example, $x$ is bound in $P$ in $x.P$. $M,N,P$ are metavariables for terms, not propositions. The type subscript on $\mathsf{Cut}_A$ is the cut formula. Ellipsis stands for the systematic constructors for twist, additives, and units, not an untyped escape hatch.

For completeness, the remaining constructors follow the same “one rule, one term former” policy:

| Connective | Right constructor(s) | Left constructor(s) | Reading |
|---|---|---|---|
| twist $A\circ B$ | $\circ R\,M\,N$ | $\circ L\,x\,(z.y.P)$ | construct two components but expose them in reversed order |
| external choice $A\mathbin{\&}B$ | $\&R\,M\,N$ | $\&L_1\,x\,(y.P)$ or $\&L_2\,x\,(z.P)$ | offer both observations; select one projection |
| multiplicative unit $1$ | $1R$ | $1L\,x\,M$ | construct empty state; remove its marker |
| internal choice $A\oplus B$ | $\oplus R_1\,M$ or $\oplus R_2\,N$ | $\oplus L\,x\,(y.N)\,(z.P)$ | select one injection; cover both cases |
| additive truth $\top$ | $\top R$ | none | prove the nullary external offer |
| falsehood $0$ | none | $0L\,x$ | eliminate an impossible antecedent |

Here $x$ names the principal antecedent; $y$ and $z$ are fresh component variables bound in the term after their dots. Subscripts $1$ and $2$ select the left or right alternative. “None” means that the sequent calculus has no rule on that side, not that a missing constructor may be supplied arbitrarily.

## 6. Operational/computational reading

A proof term is first a serialization of a proof tree. A right constructor describes how a provider builds an observation of its type; a left constructor describes how a named assumption is used. A binder records the local result of opening or applying that assumption. A cut connects a provider term to the consumer context that binds its output. Rewriting a principal cut exposes the next smaller interactions. This is an operational reading, but the lecture does not yet identify these terms with concrete processes, messages, addresses, or values.

## 7. Worked derivation or trace in original notation and prose

Let $p:P$ and $q:Q$ be ordered assumptions. First construct $P\bullet Q$, then immediately unpack it to rebuild $P\bullet Q$. The producer is

$$p:P,\ q:Q\vdash \bullet R(\mathsf{Id}\,p)(\mathsf{Id}\,q):P\bullet Q.$$

The consumer of $u:P\bullet Q$ is

$$u:P\bullet Q\vdash
\bullet L\,u\,(a.b.\bullet R(\mathsf{Id}\,a)(\mathsf{Id}\,b)):P\bullet Q.$$

Connecting them yields

$$
\begin{aligned}
&\mathsf{Cut}_{P\bullet Q}
  (\bullet R(\mathsf{Id}\,p)(\mathsf{Id}\,q))\\
&\qquad(u.\bullet L\,u\,(a.b.\bullet R(\mathsf{Id}\,a)(\mathsf{Id}\,b)))\\
&\longrightarrow_R
\mathsf{Cut}_Q(\mathsf{Id}\,q)
  (b.\mathsf{Cut}_P(\mathsf{Id}\,p)
    (a.\bullet R(\mathsf{Id}\,a)(\mathsf{Id}\,b))).
\end{aligned}
$$

The two remaining cuts are identity cases and disappear, leaving $\bullet R(\mathsf{Id}\,p)(\mathsf{Id}\,q)$. As a boundary case, replacing the consumer binder by $b.a.P$ is not harmless alpha-renaming: it reverses the component order and generally does not type-check in the original ordered context.

## 8. Conceptual synthesis

Proof terms make the internal semantics manipulable. Variable labels solve the bookkeeping problem created by splitting and ordered use; binders make fresh assumptions and local results explicit; constructors retain the derivation’s rule structure. Cut reduction then becomes syntax-directed interaction. Polarity extracts a global proof-search discipline from the same local harmony witnessed by identity expansion.

## 9. Common confusions and failure modes

- **Treating antecedent labels as positional indices.** Variables are stable names; their order still comes from $\Omega$.
- **Confusing free and bound variables.** $x.M$ binds $x$ only in $M$, and bound names may be consistently renamed.
- **Assuming any well-shaped term is valid.** It must have a derivation using exactly the ordered assumptions prescribed by the rules.
- **Reading cut reduction as ordinary substitution.** The displayed system reduces compound cuts to smaller cuts; substitution is not silently inserted.
- **Calling a premise-free rule universally applicable.** $1R$ still requires an empty context.
- **Equating negative with false or positive with true.** Polarity describes invertibility and proof behavior, not truth value.
- **Assuming one normalizing schedule.** Commuting reductions may make cut elimination nondeterministic.

## 10. Self-test questions with concise answers

1. **Why label antecedents with variables?** To identify uses robustly across context splits and exchange.
2. **What does $x.M$ express?** $x$ is bound in the proof term $M$.
3. **What does $\bullet L$ bind?** Two fresh variables for the left and right components, in that order.
4. **What makes a connective negative?** Its right behavior is invertible.
5. **Why is $\bullet$ positive?** Its left rule can always expose adjacent components without losing provability.
6. **Are proof terms already processes here?** No. They compactly encode proofs; the process interpretation comes later.

## 11. Related concept pages

- [Hypothetical Judgments](<../Concepts/Hypothetical Judgments.md>)
- [Ordered Conjunction and Implications](<../Concepts/Ordered Conjunction and Implications.md>)
- [Additive and Multiplicative Connectives](<../Concepts/Additive and Multiplicative Connectives.md>)
- [Identity and Cut Admissibility](<../Concepts/Identity and Cut Admissibility.md>)
- [Proof Terms and Cut Reductions](<../Concepts/Proof Terms and Cut Reductions.md>)
- [Polarity and Invertibility](<../Concepts/Polarity and Invertibility.md>)

## 12. Source trail (lecture, numbered sections, printed-page range, PDF-page range)

- Frank Pfenning, *Proof Terms*, Lecture 4, Sections 1–6, printed pp. L4.1–L4.11, PDF pp. 43–53.
- Annotated sequents, variable binding, reconstruction, and connective constructors: Section 2, printed pp. L4.1–L4.6, PDF pp. 43–48.
- Term-level cut reduction: Section 3, printed pp. L4.6–L4.7, PDF pp. 48–49.
- Invertibility, polarity, and connective comparison: Sections 4–5, printed pp. L4.7–L4.9, PDF pp. 49–51.
- Summary and proof-term grammar: Section 6, printed pp. L4.9–L4.10, PDF pp. 51–52. References are on printed p. L4.11, PDF p. 53.

## 13. Previous/next navigation

Previous: [Lecture 3 — Cut and Identity Elimination](<Lecture 03 - Cut and Identity Elimination.md>).

Next: Lecture 5, *Linear Message Passing I* (not authored in this assignment).

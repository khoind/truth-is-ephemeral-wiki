---
title: "Curry-Howard for Linear Natural Deduction"
aliases: ["proofs as linear programs", "propositions as linear types"]
tags: [curry-howard, lambda-calculus, linear-types]
source_lectures: [23]
prerequisites: ["Linear Natural Deduction", "Harmony in Natural Deduction"]
related: ["Linear Natural Deduction", "Harmony in Natural Deduction", "Introduction versus Elimination"]
---
# Curry-Howard for Linear Natural Deduction

## 1. One-sentence definition
**Curry–Howard identifies linear propositions with types, ND proofs with resource-sensitive programs, and proof normalization with evaluation.**

## 2. Why the concept is needed
The correspondence explains why proof terms are computational rather than decorative. It turns harmony reductions into executable laws and linear hypothesis discipline into a static guarantee against implicit duplication and disposal.

## 3. Intuitive model
**Intuition.** A proof of $A\multimap B$ consumes one $A$ to produce one $B$; a proof of $A\otimes B$ is a pair of independently resourced values. Running removes proof detours. “Resource” means syntactic use, not automatically memory deallocation or physical conservation.

## 4. Formal core
| Logic | Program |
|---|---|
| proposition $A$ | type $A$ |
| proof $M$ | program $M$ |
| $A\multimap B$ | linear function |
| $\multimap I/E$ | lambda/application |
| $A\otimes B$ | linear pair |
| $\otimes I/E$ | pair/pattern match |
| local soundness | beta-like evaluation |
| local completeness | eta expansion |

The implication reduction is
$$(\lambda x.M)N\longrightarrow M[N/x],$$
where $x:A$ occurs exactly once in $M$, $N:A$, and substitution combines disjoint contexts. Tensor computes by
$$\mathsf{match}\ (M,N)\ \mathsf{with}(x,y)\ \mathsf{in}\ P\longrightarrow P[M/x,N/y].$$
$M,N,P$ are terms; $A,B$ types; substitutions are capture-avoiding.

Typing and evaluation meet through preservation: if $\Delta\vdash M:A$ and $M\longrightarrow M'$, then one expects $\Delta\vdash M':A$. For the implication beta step, the substitution theorem proves this while combining the argument’s resources with those of the function body. For tensor beta, simultaneous substitution performs the same accounting for both components. The theorem preserves the whole linear context, not merely the result type, so evaluation cannot silently introduce weakening or contraction.

## 5. How to use/read it
Read a typing derivation as a program certificate. Introductions construct canonical values; eliminations trigger observations or computation. To predict evaluation, find an eliminator whose major premise is visibly an introduction form and apply its local-soundness reduction.

## 6. Worked example
Let
$$\mathsf{swap}=\lambda p.\mathsf{match}\ p\ \mathsf{with}(x,y)\ \mathsf{in}(y,x)$$
have type $(A\otimes B)\multimap(B\otimes A)$. Then
$$\mathsf{swap}(u,v)\longrightarrow\mathsf{match}\ (u,v)\ \mathsf{with}(x,y)\ \mathsf{in}(y,x)\longrightarrow(v,u).$$
The first step is implication beta, the second tensor beta. Both preserve typing and use $u,v$ once.

A pipeline example shows that “consumption” does not mean destruction. Given $f:A\multimap B$, $g:B\multimap C$, and $a:A$, the term $g(fa)$ has type $C$. Evaluation may transform the representation of $a$ through $f$ and then $g$; typing says only that each linear input has one accounted-for use. If $f=\lambda x.M$ and $g=\lambda y.N$, two beta steps yield $N[M[a/x]/y]$, with capture-avoiding substitution preserving the disjoint resource provenance of the three inputs.

## 7. Non-example or boundary case
Curry–Howard does not say every proof has useful runtime behavior, or that logical equivalence makes programs operationally identical. Also $\lambda x.(x,x)$ has no linear type $A\multimap A\otimes A$: ordinary lambda syntax permits duplication, but this typing discipline rejects it.

It also does not equate linear types with linear-time algorithms, unique heap ownership, or guaranteed deallocation. Those properties may be designed using related type systems, but the theorem here concerns derivational use of hypotheses. Additive branching can mention the same context in alternatives because one alternative runs; explicit modalities in richer systems can authorize reuse. Runtime cost and memory behavior require a specified operational semantics and cost model, neither of which follows from the slogan “proofs are programs.”

## 8. Key consequences
- Normalization gives evaluation laws.
- Type preservation follows from substitution.
- Linear typing controls variable use statically.
- Beta laws express local soundness; eta laws local completeness.
- The correspondence extends to units and choices.

## 9. Relations to nearby concepts
[Harmony in Natural Deduction](<Harmony in Natural Deduction.md>) supplies beta/eta transformations. [Introduction versus Elimination](<Introduction versus Elimination.md>) becomes constructors versus consumers. [Natural Deduction versus Sequent Calculus](<Natural Deduction versus Sequent Calculus.md>) organizes the same provability less expression-centrically.

## 10. Common mistakes
- Treating linearity as linear running time.
- Equating proof equality with text equality.
- Forgetting capture avoidance.
- Reading local reductions as a complete machine semantics.
- Giving duplicating lambda terms linear types.
- Ignoring context-use invariants.

## 11. What to remember
- Propositions are types; proofs are programs.
- $\multimap$ is linear function space; $\otimes$ linear pairing.
- Local soundness computes.
- Local completeness eta-expands.
- Linear variables are consumed exactly once.

## 12. Source trail
Sophia Roshal, Lecture 23, §§5.1 and 6, printed pages L23.5–L23.6 and L23.10, PDF pages 241–242 and 246. See [Lecture 23](<../Lectures/Lecture 23 - Linear Natural Deduction.md>).

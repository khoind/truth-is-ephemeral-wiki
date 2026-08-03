---
title: "Harmony in Natural Deduction"
aliases: ["local soundness and completeness", "beta and eta for natural deduction"]
tags: [harmony, normalization, proof-theory]
source_lectures: [23]
prerequisites: ["Introduction versus Elimination", "Substitution"]
related: ["Introduction versus Elimination", "Natural Deduction versus Sequent Calculus", "Curry-Howard for Linear Natural Deduction"]
---
# Harmony in Natural Deduction

## 1. One-sentence definition
**Harmony is the fit between introductions and eliminations, expressed by local soundness (detours reduce) and local completeness (evidence eta-expands).**

## 2. Why the concept is needed
An elimination might extract too much or too little from evidence. Harmony is an internal correctness test independent of another calculus. It corresponds respectively to cut and identity admissibility in sequent calculus.

## 3. Intuitive model
**Intuition.** A constructor and observer form a lossless interface. Packing then unpacking should do no extra work; observing unknown evidence and repacking all observations should preserve its capabilities. “Same” means proof-theoretically interconvertible, not textually identical.

## 4. Formal core
Admissible linear substitution is
$$\frac{\Delta\vdash M:A\quad\Delta',x:A\vdash N(x):C}{\Delta,\Delta'\vdash N(M):C}\mathsf{subst}.$$
It is proved by induction on the second derivation. If its last rule splits context, linearity puts $x$ in exactly one premise.

Local soundness:
$$\mathsf{match}\ (M,N)\ \mathsf{with}(x,y)\ \mathsf{in}\ P\longrightarrow P[M/x,N/y]$$
$$(\lambda x.M)N\longrightarrow M[N/x].$$
Local completeness:
$$P:A\otimes B\leadsto\mathsf{match}\ P\ \mathsf{with}(x,y)\ \mathsf{in}(x,y):A\otimes B$$
$$F:A\multimap B\leadsto\lambda x.Fx:A\multimap B.$$
$M,N,P,F$ are terms; $A,B,C$ types; contexts are disjoint where combined.

The arrow $\longrightarrow$ denotes a reduction of proof terms, while $\leadsto$ above records an expansion principle; neither is the typing turnstile. In tensor beta reduction, $P[M/x,N/y]$ means simultaneous, capture-avoiding substitution. The derivations for $M$ and $N$ may use separate contexts, and substitution imports both contexts into the unique sites formerly occupied by $x$ and $y$. For implication eta, $x$ must be fresh for $F$ so that $\lambda x.Fx$ does not capture a free variable. Eta expansion may make a proof larger; “completeness” here says the eliminations reveal all information needed to rebuild evidence, not that reduction always decreases size.

## 5. How to use/read it
For soundness, introduce then immediately eliminate and derive a smaller proof with the same judgment. For completeness, start with arbitrary evidence, eliminate it, then rebuild it. Substitution justifies reductions but is a metatheorem, not source syntax.

## 6. Worked example
Given $u:A,v:B$, the detour
$$\mathsf{match}\ (u,v)\ \mathsf{with}(x,y)\ \mathsf{in}(y,x)$$
constructs then destroys a tensor. Substitute $u$ for $x$ and $v$ for $y$ to reduce it to $(v,u)$. Context and exact resource use are preserved.

An implication example separates the arbitrary function from a constructed one. If $f:A\multimap B$ is unknown, local completeness expands it to $\lambda z.fz$ with fresh $z:A$; applying the expanded term to $a:A$ beta-reduces back to $fa$. If the major premise is already $\lambda x.M$, then $(\lambda x.M)N$ is a local-soundness redex and contracts to $M[N/x]$. The eta and beta directions therefore answer different adequacy questions: can observations reconstruct arbitrary evidence, and can immediate observations of freshly constructed evidence be simplified?

## 7. Non-example or boundary case
Local soundness is not global strong normalization; principal reductions alone do not show all reduction sequences terminate. Local completeness is not semantic completeness (“all valid formulas are derivable”); it eta-expands already-given evidence.

Harmony is also relative to the proposed rules. A connective can have well-typed syntax yet fail the test: an eliminator that extracts an $A$ from evidence introduced as $A\otimes B$ while forgetting $B$ would violate linear resource preservation. Conversely, an eliminator that never exposes either component would be too weak to support the tensor eta expansion. External agreement with a sequent calculus is stronger, separate evidence and should not be inferred from beta and eta examples alone.

## 8. Key consequences
- Eliminations exploit no more than introductions provide.
- Eliminations expose enough to reconstruct evidence.
- Beta/eta laws arise proof-theoretically.
- Linear substitution preserves exact use.
- Harmony validates connective design internally.

## 9. Relations to nearby concepts
[Introduction versus Elimination](<Introduction versus Elimination.md>) gives the pairs harmony tests. [Natural Deduction versus Sequent Calculus](<Natural Deduction versus Sequent Calculus.md>) relates soundness to cut and completeness to identity. [Curry-Howard for Linear Natural Deduction](<Curry-Howard for Linear Natural Deduction.md>) reads reductions as evaluation.

## 10. Common mistakes
- Swapping local soundness and completeness.
- Calling eta expansion semantic completeness.
- Treating substitution as object syntax.
- Substituting into both linear branches.
- Requiring syntactic equality.
- Claiming harmony alone proves sequent correspondence.

## 11. What to remember
- Soundness contracts detours (beta).
- Completeness reconstructs evidence (eta).
- Substitution powers reductions.
- A linear variable belongs to one split branch.
- Harmony is internal correctness.

## 12. Source trail
Sophia Roshal, Lecture 23, §5.1, printed pages L23.5–L23.6, PDF pages 241–242. See [Lecture 23](<../Lectures/Lecture 23 - Linear Natural Deduction.md>).

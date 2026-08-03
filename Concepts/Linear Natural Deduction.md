---
title: "Linear Natural Deduction"
aliases: ["linear ND"]
tags: [linear-logic, natural-deduction, resources]
source_lectures: [23]
prerequisites: ["Linear contexts", "Natural deduction"]
related: ["Introduction versus Elimination", "Bidirectional Type Checking", "Harmony in Natural Deduction"]
---
# Linear Natural Deduction

## 1. One-sentence definition
**Linear natural deduction is a proof system whose typed terms introduce and eliminate propositions while using every assumption exactly once.**

## 2. Why the concept is needed
Sequent calculus exposes resource flow but organizes proof construction bottom-up. Natural deduction directly describes values and their uses, making proofs resemble functional programs while preserving linear logic’s ban on implicit copying and discarding.

## 3. Intuitive model
**Intuition.** Each declaration $x:A$ is a single-use ticket. Constructing a pair spends two disjoint collections of tickets; opening it gives two fresh tickets, both of which must be spent. This is an aid, not a semantics: contexts are formal hypotheses, not necessarily physical objects.

## 4. Formal core
A judgment $\Delta\vdash M:A$ has linear context $\Delta$, proof term $M$, and type $A$. Representative rules are
$$\frac{\Delta_1\vdash M:A\quad\Delta_2\vdash N:B}{\Delta_1,\Delta_2\vdash(M,N):A\otimes B}\otimes I$$
$$\frac{\Delta_1\vdash P:A\otimes B\quad\Delta_2,x:A,y:B\vdash N:C}{\Delta_1,\Delta_2\vdash\mathsf{match}\ P\ \mathsf{with}(x,y)\ \mathsf{in}\ N:C}\otimes E$$
$$\frac{\Delta,x:A\vdash M:B}{\Delta\vdash\lambda x.M:A\multimap B}\multimap I\qquad
\frac{\Delta_1\vdash F:A\multimap B\quad\Delta_2\vdash N:A}{\Delta_1,\Delta_2\vdash FN:B}\multimap E.$$
Contexts joined in multiplicative rules are disjoint. $\otimes$ is tensor, $\multimap$ linear implication, and $C$ an arbitrary result type. Tensor elimination uses a continuation because natural deduction has one conclusion and both components must be consumed.

More explicitly, $\Delta$ is a finite collection of distinct declarations $x_1:A_1,\ldots,x_n:A_n$; it is not a bag that may be copied between premises. A derivation certifies that the free variables of $M$ are precisely those declared in $\Delta$, each with one use along an executed branch. The subscripts on $\Delta_1$ and $\Delta_2$ do not denote order or time: they identify a partition, so their domains must be disjoint. The empty context is written $\cdot$. The turnstile $\vdash$ separates available assumptions from the term and type being justified, while the colon assigns a type to a term rather than asserting ordinary-language membership.

## 5. How to use/read it
Read introductions backward from a desired type and eliminations forward from evidence. To prove a tensor, partition resources. To consume it, bind both parts. To prove an implication, assume one linear argument; to consume it, apply the function to an independently derived argument.

## 6. Worked example
Tensor symmetry is
$$\cdot\vdash\lambda p.\mathsf{match}\ p\ \mathsf{with}(x,y)\ \mathsf{in}(y,x):(A\otimes B)\multimap(B\otimes A).$$
Implication introduction adds $p:A\otimes B$. Tensor elimination replaces it by $x:A,y:B$. Tensor introduction splits those as $y:B$ and $x:A$. Each assumption is used once; abstraction closes $p$.

As a contrasting constructive example, composition has type
$$
(B\multimap C)\multimap((A\multimap B)\multimap(A\multimap C))
$$
and term $\lambda g.\lambda f.\lambda a.g(fa)$. The innermost application spends $f$ and $a$ to produce a $B$; the outer application spends that result together with $g$ to produce $C$. Each binder occurs once syntactically, and each application combines disjoint contexts. Linearity therefore permits pipelines and reassociation; it prohibits only unlicensed weakening and contraction.

## 7. Non-example or boundary case
$\lambda x.(x,x):A\multimap(A\otimes A)$ is not derivable: tensor introduction would require $x:A$ in both premises. Likewise $\lambda x.():A\multimap1$ discards $x$. Both require structural capabilities absent from this fragment.

“Exactly once” is also connective-sensitive. Additive conjunction may check several branches under the same context because only one branch is selected at run time; this is not contraction. Conversely, an explicit exponential modality in a larger linear logic can mark values that may be copied or discarded. The boundary is therefore not that every visible variable name occurs once in the source text, but that the typing rules account for every linear assumption exactly once on each possible execution path.

## 8. Key consequences
- Typing records exact resource consumption.
- Tensor matching consumes both components.
- Substitution combines disjoint contexts.
- Normalization doubles as evaluation.
- Ordinary and bidirectional presentations differ algorithmically, not in intended provability.

## 9. Relations to nearby concepts
[Introduction versus Elimination](<Introduction versus Elimination.md>) explains the rule families. [Bidirectional Type Checking](<Bidirectional Type Checking.md>) annotates their information flow. [Natural Deduction versus Sequent Calculus](<Natural Deduction versus Sequent Calculus.md>) contrasts proof organization. Unlike intuitionistic ND, this system has no implicit weakening or contraction.

## 10. Common mistakes
- Reusing one context in both tensor premises.
- Reading context commas as unrestricted union.
- Ignoring a pattern-bound component.
- Confusing one conclusion with one-use assumptions.
- Treating proof terms as decorative labels.

## 11. What to remember
- Every assumption is used exactly once.
- Introductions build; eliminations consume.
- Multiplicative premises split contexts.
- Tensor matching binds both components.
- Normalization has computational meaning.

## 12. Source trail
Sophia Roshal, Lecture 23, §§1–2 and 5–6, printed pages L23.1–L23.6 and L23.10, PDF pages 237–242 and 246. See [Lecture 23](<../Lectures/Lecture 23 - Linear Natural Deduction.md>).

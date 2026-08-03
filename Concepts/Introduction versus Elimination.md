---
title: "Introduction versus Elimination"
aliases: ["introduction and elimination rules"]
tags: [natural-deduction, proof-theory]
source_lectures: [23]
prerequisites: ["Linear Natural Deduction"]
related: ["Linear Natural Deduction", "Harmony in Natural Deduction", "Bidirectional Type Checking"]
---
# Introduction versus Elimination

## 1. One-sentence definition
**An introduction rule constructs evidence for a connective, while its elimination rule consumes evidence of that connective.**

## 2. Why the concept is needed
A connective is understood through both its constructors and observations. Separating them exposes proof detours—construction immediately followed by destruction—and supports syntax-directed typing.

## 3. Intuitive model
**Intuition.** Introduction is packaging; elimination is lawful use. A linear pair is packaged from two resources and unpacked into two one-use names. A function is packaged by abstraction and used by application. Formal rules, not the metaphor, determine permitted uses.

## 4. Formal core
For tensor:
$$\frac{\Delta_1\vdash M:A\quad\Delta_2\vdash N:B}{\Delta_1,\Delta_2\vdash(M,N):A\otimes B}\otimes I$$
$$\frac{\Delta_1\vdash P:A\otimes B\quad\Delta_2,x:A,y:B\vdash Q:C}{\Delta_1,\Delta_2\vdash\mathsf{match}\ P\ \mathsf{with}(x,y)\ \mathsf{in}\ Q:C}\otimes E.$$
For implication:
$$\frac{\Delta,x:A\vdash M:B}{\Delta\vdash\lambda x.M:A\multimap B}\multimap I\qquad
\frac{\Delta_1\vdash F:A\multimap B\quad\Delta_2\vdash N:A}{\Delta_1,\Delta_2\vdash FN:B}\multimap E.$$
$\Delta,\Delta_i$ are linear contexts; letters $M$ through $Q$ are terms; $A,B,C$ types. Introductions correspond to sequent right rules. Eliminations embody left-rule uses around a major-premise term.

The **principal formula** of an introduction is the connective appearing in its conclusion, such as $A\otimes B$. In an elimination, the **major premise** supplies evidence with that outer connective; any other premises are minor premises or continuations describing what to do with the exposed information. This vocabulary matters when identifying a principal detour: the major premise must itself end in the matching introduction. Merely having an introduction somewhere inside an elimination argument does not create the corresponding beta redex.

The pattern varies by polarity. Function application synthesizes a result once its major premise synthesizes $A\multimap B$. Tensor elimination instead opens positive data and checks a continuation against a result type $C$ supplied by the surrounding derivation. Thus “introduction checks, elimination synthesizes” is a useful default, not a universal definition of the two rule families.

## 5. How to use/read it
When the goal’s outer connective is known, apply its introduction upward. When a term’s outer type is known, follow its elimination downward. Bidirectionally, introductions normally check and neutral eliminations synthesize. Positive eliminations such as tensor match instead continue checking a result type supplied from outside.

## 6. Worked example
For $(\lambda x.x)z$, $\multimap I$ constructs $\lambda x.x:A\multimap A$ from $x:A\vdash x:A$. Separately $z:A\vdash z:A$. Then $\multimap E$ gives $z:A\vdash(\lambda x.x)z:A$. The introduction/elimination detour reduces to $z$, showing that the rules fit.

For tensor, take disjoint evidence $m:A$ and $n:B$ and a continuation that swaps its inputs. Introduction first forms $(m,n):A\otimes B$; elimination then yields
$$\mathsf{match}\ (m,n)\ \mathsf{with}(x,y)\ \mathsf{in}(y,x).$$
The matched introduction makes this a principal redex, reducing to $(n,m)$. Notice that elimination does not erase the pair. It transfers ownership of its components to fresh names, and substitution carries the resource derivations for $m$ and $n$ into their unique use sites.

## 7. Non-example or boundary case
From $P:A\otimes B$ one cannot conclude $A$ and $B$ as two judgments: ND has one conclusion and linear use must be tracked. The continuation form is essential. Also, not every elimination synthesizes; tensor case analysis checks against the surrounding expected $C$.

Nor is an arbitrary destructor automatically legitimate. A proposed tensor eliminator that returned only the left component would silently discard the $B$ resource. One that returned two independent conclusions would leave unclear whether later derivations could duplicate either result. The lawful continuation rule is calibrated to what tensor introduction provides and to the single-conclusion shape of natural deduction.

## 8. Key consequences
- Rules define production and consumption.
- Principal introduction/elimination pairs normalize.
- Eta expansion shows eliminations expose enough to reconstruct evidence.
- Constructors and observations guide bidirectional modes.
- The distinction aligns proof theory with functional syntax.

## 9. Relations to nearby concepts
[Harmony in Natural Deduction](<Harmony in Natural Deduction.md>) tests whether the halves are neither too strong nor too weak. [Bidirectional Type Checking](<Bidirectional Type Checking.md>) operationalizes information flow. [Natural Deduction versus Sequent Calculus](<Natural Deduction versus Sequent Calculus.md>) explains the right/left correspondence.

## 10. Common mistakes
- Calling every bottom-up rule an introduction.
- Assuming elimination means discarding evidence.
- Forgetting both tensor components.
- Equating eliminations syntactically with sequent left rules.
- Assuming every elimination has one bidirectional mode.

## 11. What to remember
- Introduction constructs; elimination consumes.
- Tensor: pair/match.
- Implication: lambda/application.
- Construct-then-use is a reducible detour.
- Eliminate-then-reconstruct is eta expansion.

## 12. Source trail
Sophia Roshal, Lecture 23, §§1–2 and 5.1, printed pages L23.1–L23.6, PDF pages 237–242. See [Lecture 23](<../Lectures/Lecture 23 - Linear Natural Deduction.md>).

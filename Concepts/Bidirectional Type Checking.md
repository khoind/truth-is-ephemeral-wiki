---
title: "Bidirectional Type Checking"
aliases: ["checking and synthesis"]
tags: [type-checking, bidirectional-typing, linear-logic]
source_lectures: [23]
prerequisites: ["Introduction versus Elimination"]
related: ["Linear Natural Deduction", "Introduction versus Elimination", "Natural Deduction versus Sequent Calculus"]
---
# Bidirectional Type Checking

## 1. One-sentence definition
**Bidirectional type checking divides typing into checking a term against a known type and synthesizing a type from a term.**

## 2. Why the concept is needed
The judgment $M:A$ hides which information a rule requires. Explicit inputs and outputs give an implementable algorithm, reduce annotations, and record ND’s upward introduction and downward elimination phases.

## 3. Intuitive model
**Intuition.** Checking asks, “Given destination $A$, does $M$ fit?” Synthesis asks, “Starting from $M$, what type comes out?” Expected types flow inward through constructors; inferred types flow outward through variables and eliminations. Arrows express information flow, not logical implication.

## 4. Formal core
$\Delta\vdash M\Leftarrow A$ takes $\Delta,M,A$ as inputs. $\Delta\vdash M\Rightarrow A$ takes $\Delta,M$ as input and produces $A$.
$$\frac{}{x:A\vdash x\Rightarrow A}hyp\quad
\frac{\Delta,x:A\vdash M\Leftarrow B}{\Delta\vdash\lambda x.M\Leftarrow A\multimap B}\multimap I$$
$$\frac{\Delta_1\vdash F\Rightarrow A\multimap B\quad\Delta_2\vdash N\Leftarrow A}{\Delta_1,\Delta_2\vdash FN\Rightarrow B}\multimap E$$
$$\frac{\Delta_1\vdash M\Leftarrow A\quad\Delta_2\vdash N\Leftarrow B}{\Delta_1,\Delta_2\vdash(M,N)\Leftarrow A\otimes B}\otimes I$$
$$\frac{\Delta_1\vdash P\Rightarrow A\otimes B\quad\Delta_2,x:A,y:B\vdash Q\Leftarrow C}{\Delta_1,\Delta_2\vdash\mathsf{match}\ P\ \mathsf{with}(x,y)\ \mathsf{in}\ Q\Leftarrow C}\otimes E.$$
Mode changes are
$$\frac{\Delta\vdash M\Rightarrow A'\quad A=A'}{\Delta\vdash M\Leftarrow A}\Rightarrow/\Leftarrow\qquad
\frac{\Delta\vdash M\Leftarrow A}{\Delta\vdash(M:A)\Rightarrow A}\Leftarrow/\Rightarrow.$$
The annotation is syntax. Equality—the sole comparison point—may be replaced by subtyping.

Here $A'$ is a freshly synthesized output, whereas $A$ is the expected input; the premise $A=A'$ is a decidable comparison, not a new proof assumption. In an implementation, a checking procedure can return success or failure plus a resource-usage certificate, while a synthesis procedure returns a type. Both procedures must also ensure that context partitions cover the original linear context without overlap. Bidirectionality removes search about rule direction, but it does not remove the combinatorial question of how resources are assigned to multiplicative subterms; concrete languages often use ordered contexts or usage tracking to make that assignment deterministic.

## 5. How to use/read it
Start from an expected result. Decompose lambdas, pairs, units, and injections. At a variable or annotated neutral, synthesize. Continue synthesis through application or projection. Return to checking by comparing synthesized and expected types. Linear context splitting remains required.

## 6. Worked example
Check $\lambda f.\lambda x.fx$ against $(A\multimap B)\multimap(A\multimap B)$. Two introductions add $f:A\multimap B,x:A$. Hypothesis synthesizes $f$’s type. Application needs $x\Leftarrow A$; hypothesis gives $x\Rightarrow A$, then equality changes mode. Application synthesizes $B$, and another mode change checks the body against $B$.

The information-flow trace is therefore
$$f\Rightarrow A\multimap B,\qquad x\Rightarrow A\leadsto x\Leftarrow A,
\qquad fx\Rightarrow B\leadsto fx\Leftarrow B.$$
The first mode switch supplies the checking premise required by application; the second lets the synthesized body satisfy the lambda’s expected codomain. No annotation is needed because the outer expected type fixes both lambda domains. By contrast, placing the same lambda in a synthesis-only position requires an annotation such as $(\lambda x.x:A\multimap A)$, after which application can read its arrow type.

## 7. Non-example or boundary case
Bare $\lambda x.x$ cannot generally synthesize a unique type: its domain is absent. It checks against $A\multimap A$, or $(\lambda x.x:A\multimap A)$ can synthesize. This is not unrestricted Hindley–Milner inference.

Bidirectional completeness also does not mean that every ordinary term is accepted unchanged. A complete elaboration theorem may insert type annotations at mode boundaries while preserving the underlying ordinary derivation. Likewise, replacing equality by subtyping changes what the mode switch accepts and demands a separate metatheory; it is not justified merely by drawing the same arrow on the judgment.

## 8. Key consequences
- Equality checks are centralized.
- Variables need no redundant annotations.
- Introductions are syntax-directed under expected types.
- Erasing directions yields ordinary ND.
- Completeness may insert annotations or mode changes.

## 9. Relations to nearby concepts
[Introduction versus Elimination](<Introduction versus Elimination.md>) motivates modes but is not an algorithm. [Natural Deduction versus Sequent Calculus](<Natural Deduction versus Sequent Calculus.md>) explains the left/right heuristic. [Linear Natural Deduction](<Linear Natural Deduction.md>) supplies resource splitting.

## 10. Common mistakes
- Reading $\Rightarrow$ as implication.
- Expecting every term to synthesize.
- Omitting equality at the mode switch.
- Making variables check-only.
- Forgetting mutual recursion of the judgments.
- Confusing local synthesis with global polymorphic inference.

## 11. What to remember
- Checking has an expected type; synthesis produces one.
- Constructors check; variables and neutral eliminations synthesize.
- Equality/subtyping occurs at the mode boundary.
- An annotation turns checking into synthesis.
- Resource discipline remains intact.

## 12. Source trail
Sophia Roshal, Lecture 23, §§3–4 and 7, printed pages L23.2–L23.4 and L23.11, PDF pages 238–240 and 247. See [Lecture 23](<../Lectures/Lecture 23 - Linear Natural Deduction.md>).

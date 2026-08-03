---
title: "Lecture 23 - Linear Natural Deduction"
lecture: 23
date: "2023-12-07"
pdf_pages: "237-248"
printed_pages: "L23.1-L23.12"
tags: [linear-logic, natural-deduction, bidirectional-typing, harmony, curry-howard]
prerequisites: ["Sequent calculus", "Identity and cut admissibility", "Linear logic connectives"]
---

# Lecture 23 - Linear Natural Deduction

> **Author:** Sophia Roshal. This additional lecture is not authored by Frank Pfenning.

## 1. Why this lecture exists

Earlier lectures reason mainly in sequent calculus, including SAX and SNAX, by decomposing a goal bottom-up. Natural deduction adds a second direction: **introduction** rules build evidence for a type, while **elimination** rules consume already-available evidence. The lecture develops a linear version, makes the two directions algorithmic through bidirectional typing, and checks the system both internally (harmony) and externally (translation to sequent calculus).

## 2. Learning objectives

After this lecture, you should be able to:

- derive linear introduction and elimination rules for $\otimes$ and $\multimap$;
- distinguish checking, $M\Leftarrow A$, from synthesis, $M\Rightarrow A$;
- explain why linear contexts must be split rather than copied;
- use the synthesis-to-checking rule and type equality at the unique mode switch;
- state local soundness, local completeness, and substitution;
- explain the three translations among ordinary natural deduction, bidirectional natural deduction, and sequent calculus;
- read proof normalization as functional computation.

## 3. Dependency map

[Introduction versus Elimination](<../Concepts/Introduction versus Elimination.md>) supplies the rule architecture. [Bidirectional Type Checking](<../Concepts/Bidirectional Type Checking.md>) makes direction explicit. [Harmony in Natural Deduction](<../Concepts/Harmony in Natural Deduction.md>) depends on substitution and connects to [Natural Deduction versus Sequent Calculus](<../Concepts/Natural Deduction versus Sequent Calculus.md>). [Curry-Howard for Linear Natural Deduction](<../Concepts/Curry-Howard for Linear Natural Deduction.md>) gives the computational reading. The umbrella page is [Linear Natural Deduction](<../Concepts/Linear Natural Deduction.md>).

## 4. Section-by-section reconstruction

### 1 Introduction

Natural deduction has two proof motions. Introduction rules work backward from a desired conclusion, as sequent right rules do. Elimination rules work forward from the type synthesized by a term. The aim is not merely a new notation: the mixed direction exposes canonical constructors, observations, and computation.

### 2 The Base Rules

A judgment $\Delta\vdash M:A$ says that term $M$ has type $A$ while using every declaration in the linear context $\Delta$ exactly once. Context juxtaposition assumes disjoint variables.

Tensor introduction splits resources:

$$\frac{\Delta_1\vdash M:A\qquad\Delta_2\vdash N:B}{\Delta_1,\Delta_2\vdash(M,N):A\otimes B}\;\otimes I.$$

Tensor elimination cannot return both $A$ and $B$ as separate conclusions. Instead it binds both components in a continuation that produces one result:

$$\frac{\Delta_1\vdash M:A\otimes B\qquad\Delta_2,x:A,y:B\vdash N:C}{\Delta_1,\Delta_2\vdash\mathsf{match}\ M\ \mathsf{with}\ (x,y)\ \mathsf{in}\ N:C}\;\otimes E.$$

Linear implication introduction abstracts exactly one use of $x$; elimination is application:

$$\frac{\Delta,x:A\vdash M:B}{\Delta\vdash\lambda x.M:A\multimap B}\;\multimap I
\qquad
\frac{\Delta_1\vdash M:A\multimap B\qquad\Delta_2\vdash N:A}{\Delta_1,\Delta_2\vdash MN:B}\;\multimap E.$$

### 3 Bidirectional Type Checking

Split typing into checking $\Delta\vdash M\Leftarrow A$ (both $M$ and expected $A$ are inputs) and synthesis $\Delta\vdash M\Rightarrow A$ ($M$ is input and $A$ output). Constructors check; variables and eliminations synthesize. Thus pairs and lambdas check, while application synthesizes its codomain and tensor matching checks its continuation against an expected result. The hypothesis rule is $x:A\vdash x\Rightarrow A$—not sequent identity, because it starts a synthesis chain.

### 4 An example

One direction of currying has term

$$\lambda f.\lambda ab.\mathsf{match}\ ab\ \mathsf{with}\(a,b)\ \mathsf{in}\ ((f\ a)\ b)$$

and checks against

$$(A\multimap(B\multimap C))\multimap((A\otimes B)\multimap C).$$

Variables synthesize. Yet arguments $a,b$ and the final application synthesize where a checking premise is required. This reveals the mode-change rule:

$$\frac{\Delta\vdash M\Rightarrow A'\qquad A=A'}{\Delta\vdash M\Leftarrow A}\;\Rightarrow/\Leftarrow.$$

Type equality—or subtyping in an extended language—is concentrated here.

### 5 System Correctness

Correctness has two views. Internally, introductions and eliminations must be harmonious. Externally, the system must correspond to trusted sequent calculus. Ordinary and bidirectional natural deduction are also related by erasing or reconstructing mode annotations.

#### 5.1 Harmony

**Local completeness** expands arbitrary evidence by eliminating then reintroducing it. For tensor, $M:A\otimes B$ expands to $\mathsf{match}\ M\ \mathsf{with}\ (x,y)\ \mathsf{in}\ (x,y)$. For implication, $M:A\multimap B$ expands to $\lambda x.Mx$.

**Local soundness** contracts an introduction immediately followed by its elimination. It needs admissible substitution:

$$\frac{\Delta\vdash M:A\qquad\Delta',x:A\vdash N(x):C}{\Delta,\Delta'\vdash N(M):C}\;\mathsf{subst}.$$

Linearity means $x$ occurs in exactly one branch when the final rule splits context. Principal reductions are

$$\mathsf{match}\ (M,N)\ \mathsf{with}\ (x,y)\ \mathsf{in}\ P\longrightarrow P[M/x,N/y]$$

and

$$(\lambda x.M)N\longrightarrow M[N/x].$$

#### 5.2 Soundness/Completeness wrt Sequent Calculus

Use $\vdash^{nd}$ for ordinary natural deduction, $\vdash^{\uparrow\downarrow}$ for bidirectional deduction, and $\vdash^{seq}$ for sequent calculus.

1. If $\Delta\vdash^{nd}M:C$, then $\Delta\vdash^{seq}C$ (soundness of ND). Elimination cases translate using admissible sequent cut; implication elimination also uses identity.
2. If $\Delta\vdash^{seq}C$, then some $\Delta'\vdash^{\uparrow\downarrow}M\Leftarrow C$, provided $\Delta'\vdash^{sub}\Delta$ maps each sequent assumption to a synthesizing ND term. This context substitution is essential because sequent antecedents are unlabelled formulas while ND contexts bind variables and may represent formulas by compound terms.
3. If a bidirectional checking or synthesis derivation exists, erasing directions yields an ordinary ND derivation. The checking and synthesis claims are proved simultaneously because their rules refer to one another.

For $\otimes L$, the context mapping supplies $M\Rightarrow A\otimes B$; $\otimes E$ exposes $x:A,y:B$, after which the induction hypothesis translates the premise. For $\multimap L$, synthesize the function, translate the argument to a checking term, apply it to synthesize $B$, then translate the remaining premise.

### 6 Curry-Howard Correspondence

Propositions are types, proofs are programs, introduction forms are constructors, eliminations are uses, and normalization is evaluation. The local-soundness reduction for $\multimap$ is beta reduction. Linearity strengthens the programming reading: a bound linear value is consumed exactly once. Tensor is a linear pair and tensor matching destructures it without duplicating either component.

### 7 Full Bidirectional Rules

Let $L$ be a finite label set; $\&\{\ell:A_\ell\}_{\ell\in L}$ is negative choice and $\oplus\{\ell:A_\ell\}_{\ell\in L}$ positive choice. An annotation $(M:A)$ changes checking into synthesis.

$$\frac{\Delta\vdash M\Rightarrow A'\quad A=A'}{\Delta\vdash M\Leftarrow A}\;\Rightarrow/\Leftarrow
\qquad
\frac{\Delta\vdash M\Leftarrow A}{\Delta\vdash(M:A)\Rightarrow A}\;\Leftarrow/\Rightarrow$$

$$\frac{}{x:A\vdash x\Rightarrow A}\;hyp$$

$$\frac{\Delta,x:A\vdash M\Leftarrow B}{\Delta\vdash\lambda x.M\Leftarrow A\multimap B}\;\multimap I
\qquad
\frac{\Delta\vdash M\Rightarrow A\multimap B\quad\Delta'\vdash N\Leftarrow A}{\Delta,\Delta'\vdash MN\Rightarrow B}\;\multimap E$$

$$\frac{\Delta\vdash M_\ell\Leftarrow A_\ell\ (\forall\ell\in L)}{\Delta\vdash\{\ell\Rightarrow M_\ell\}_{\ell\in L}\Leftarrow\&\{\ell:A_\ell\}_{\ell\in L}}\;\& I
\qquad
\frac{\Delta\vdash M\Rightarrow\&\{\ell:A_\ell\}_{\ell\in L}\quad\ell\in L}{\Delta\vdash M.\ell\Rightarrow A_\ell}\;\& E$$

The same $\Delta$ appears in every additive branch because only one branch is selected at run time.

$$\frac{\Delta\vdash M\Leftarrow A\quad\Delta'\vdash N\Leftarrow B}{\Delta,\Delta'\vdash(M,N)\Leftarrow A\otimes B}\;\otimes I$$

$$\frac{\Delta\vdash M\Rightarrow A\otimes B\quad\Delta',x:A,y:B\vdash N\Leftarrow C}{\Delta,\Delta'\vdash\mathsf{match}\ M\ ((x,y)\Rightarrow N)\Leftarrow C}\;\otimes E$$

$$\frac{}{\cdot\vdash()\Leftarrow1}\;1I
\qquad
\frac{\Delta\vdash M\Rightarrow1\quad\Delta'\vdash N\Leftarrow C}{\Delta,\Delta'\vdash\mathsf{match}\ M\ (()\Rightarrow N)\Leftarrow C}\;1E$$

$$\frac{\Delta\vdash M\Leftarrow A_\ell\quad\ell\in L}{\Delta\vdash\ell(M)\Leftarrow\oplus\{\ell:A_\ell\}_{\ell\in L}}\;\oplus I$$

$$\frac{\Delta\vdash M\Rightarrow\oplus\{\ell:A_\ell\}_{\ell\in L}\quad\Delta',x:A_\ell\vdash N_\ell\Leftarrow C\ (\forall\ell\in L)}{\Delta,\Delta'\vdash\mathsf{match}\ M\ (\ell(x)\Rightarrow N_\ell)_{\ell\in L}\Leftarrow C}\;\oplus E$$

## 5. Formal core

The core invariants are: every linear variable is used exactly once; multiplicative premises partition contexts; additive alternatives reuse the same context across mutually exclusive branches; constructors check; neutral terms synthesize; and equality is tested only when synthesized evidence is accepted at an expected type. Substitution is admissible, not an object-language term former. Likewise, translations and harmony are metatheorems, not typing rules.

## 6. Operational/computational reading

Checking follows the expected type inward: to check a function, introduce its argument; to check a pair, split resources and check components. Synthesis follows a neutral term outward: look up a variable, apply a synthesized function, project a synthesized record, or eliminate a synthesized positive value into a checking continuation. Evaluation removes constructor/eliminator detours while preserving type and exact resource use.

## Worked derivation or trace

To check $\lambda p.\mathsf{match}\ p\ \mathsf{with}\(u,v)\ \mathsf{in}\ (v,u)$ against $(A\otimes B)\multimap(B\otimes A)$:

1. $\multimap I$ adds $p:A\otimes B$.
2. $hyp$ gives $p\Rightarrow A\otimes B$.
3. $\otimes E$ binds $u:A,v:B$ and leaves goal $(v,u)\Leftarrow B\otimes A$.
4. $hyp$ gives $v\Rightarrow B$ and $u\Rightarrow A$; two mode changes make them check.
5. $\otimes I$ checks $(v,u)$ with split contexts $v:B$ and $u:A$.

No variable is weakened or contracted.

Here is the resource accounting in more detail. Before the match, the continuation owns no resources besides the components that the match will expose. The major premise consumes the declaration $p:A\otimes B$ in order to synthesize the tensor type. Inside the continuation, $p$ is no longer available: it has been replaced by the fresh declarations $u:A$ and $v:B$. The pair constructor then partitions that two-entry context. Its left premise receives only $v:B$ and checks $v$ against $B$ after a synthesis-to-checking mode change; its right premise receives only $u:A$ and checks $u$ against $A$. Thus the apparent reversal in $(v,u)$ changes order but neither copies nor loses a resource.

The derivation also illustrates why the outer expected type matters. The unannotated lambda cannot synthesize its domain, but the goal $(A\otimes B)\multimap(B\otimes A)$ tells $\multimap I$ both the type assigned to $p$ and the required body type. The match similarly does not infer an arbitrary result type: it inherits the expected $B\otimes A$ and checks its continuation against that type. Only the neutral subterms $p$, $v$, and $u$ synthesize. This alternating trace is the algorithmic content hidden by an ordinary judgment $\Delta\vdash M:C$.

If the resulting function is applied to a constructed pair $(m,n)$, normalization first performs implication beta reduction and then tensor beta reduction:
$$
(\lambda p.\mathsf{match}\ p\ \mathsf{with}(u,v)\ \mathsf{in}(v,u))(m,n)
\longrightarrow
\mathsf{match}\ (m,n)\ \mathsf{with}(u,v)\ \mathsf{in}(v,u)
\longrightarrow (n,m).
$$
The first substitution transfers the disjoint resources used by $(m,n)$ into the body; the second substitutes each component exactly once. This is simultaneously a proof normalization trace and an evaluation trace.

## 8. Conceptual synthesis

Natural deduction makes canonical production and consumption explicit; bidirectionality turns that proof-theoretic distinction into a typing algorithm. Harmony says production and consumption fit without information loss or bureaucratic detours. Sequent translations show equivalent provability despite different proof organization. Curry–Howard then identifies the same normalization steps as program evaluation.

## 9. Common confusions and failure modes

- Copying the whole linear context into both multiplicative premises.
- Treating $M\Rightarrow A$ as “$M$ proves $A$ more strongly”; it describes information flow.
- Giving introductions synthesis rules without annotations, which makes inference underdetermined.
- Calling $hyp$ sequent identity; their roles differ.
- Forgetting context substitution in sequent-to-ND completeness.
- Treating substitution, cut, or translation as object-language rules.
- Calling local completeness “every true proposition is derivable”; it is eta-expansion.

## 10. Self-test questions with concise answers

1. **Why does $\otimes E$ have a continuation?** To consume both components linearly while retaining one conclusion.
2. **Where is type equality checked?** At $\Rightarrow/\Leftarrow$.
3. **Why simultaneous induction for erasure?** Checking and synthesis derivations are mutually defined.
4. **What corresponds to beta reduction?** Local soundness for $\multimap$.
5. **Why context substitution in completeness?** ND assumptions require terms/variables that synthesize the sequent formulas.
6. **What does local completeness for functions produce?** $M$ expands to $\lambda x.Mx$.

## 11. Related concept pages

- [Linear Natural Deduction](<../Concepts/Linear Natural Deduction.md>)
- [Introduction versus Elimination](<../Concepts/Introduction versus Elimination.md>)
- [Bidirectional Type Checking](<../Concepts/Bidirectional Type Checking.md>)
- [Harmony in Natural Deduction](<../Concepts/Harmony in Natural Deduction.md>)
- [Natural Deduction versus Sequent Calculus](<../Concepts/Natural Deduction versus Sequent Calculus.md>)
- [Curry-Howard for Linear Natural Deduction](<../Concepts/Curry-Howard for Linear Natural Deduction.md>)

## 12. Source trail

Sophia Roshal, “Linear Natural Deduction,” Lecture 23, December 7, 2023: §§1–7, printed pages L23.1–L23.12, PDF pages 237–248. The full rules are on L23.11; references on L23.12. Examples here are independently written.

## 13. Previous/next navigation

Previous: [Lecture 22 - The Concurrent Logical Framework](<Lecture-22-The-Concurrent-Logical-Framework.md>). Next: none in the supplied notes.

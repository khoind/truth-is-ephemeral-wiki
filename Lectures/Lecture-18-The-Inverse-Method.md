---
title: "Lecture 18 — The Inverse Method"
lecture: 18
date: 2023-11-15
pdf_pages: "187–200"
printed_pages: "L18.1–L18.14"
tags:
  - lecture-guide
  - inverse-method
  - proof-search
prerequisites:
  - "[Partial focusing](../Concepts/Partial-Focusing.md)"
  - "[Forward proof search and the inverse method](../Concepts/Forward-Proof-Search-and-Inverse-Method.md)"
---

# Lecture 18 — The Inverse Method

## 1. Why this lecture exists

The course returns from proofs-as-programs to automated theorem proving. Backward cut-free search is principled but branches heavily and shares little information between failures. The inverse method instead derives facts forward from identities, using the goal's side-aware subformulas to make the space relevant and often finite. Focusing enlarges steps; resource regimes determine pruning and subsumption.

## 2. Learning objectives

- specialize sequent rules to labeled goal subformulas;
- perform forward saturation and reconstruct a proof;
- distinguish stable focused sequents from arbitrary sequents;
- explain why linear multiplicities prune search;
- adapt search to strict, affine, and structural contexts; and
- describe the special treatment required by $0$ and $\top$.

## 3. Dependency map

Cut-free subformula property $\rightarrow$ finite relevant labels. Atomic identity $\rightarrow$ seed facts. Specialized rules $\rightarrow$ [inverse-method saturation](../Concepts/Forward-Proof-Search-and-Inverse-Method.md). Focusing $\rightarrow$ stable-to-stable big steps. Weakening/contraction $\rightarrow$ [resource regimes](../Comparisons/Resource-Regimes.md). Results motivate [resource semantics](Lecture-19-Resource-Semantics.md).

## 4. Section-by-section reconstruction covering every numbered heading

### 1 Introduction

Substructural theorem proving supports parsing, planning, separation-logic verification, synthesis, and logic programming. Backward search improves with inversion and focusing but still backtracks. Maslov's inverse method reverses direction. Unlike resolution, it is based on cut-free sequent structure and therefore transfers across nonclassical logics, subject to logic-specific resource treatment.

### 2 The Basic Idea

Label each goal subformula by the side on which it can occur; implication antecedents change sides. Generate a finite set of rule instances referring only to labels, then discard the general logical rules. Seed atomic identities and apply specialized rules breadth-first. The provable distributivity example reaches its named goal; the analogous multiplicative formula immediately saturates without it because one $A$ cannot feed two tensor branches.

### 3 The Inverse Method with Focusing

Focused search records only stable sequents. Generate a big rule by focusing on one eligible formula until stable premises appear, name newly exposed stable formulas, and repeat. Suspended atoms cannot themselves be focused. This can reduce ten small facts to two large steps. The linear $S$ combinator fails when saturation produces a fact requiring two copies of suspended $A$; multiplicity beyond the goal can be rejected.

### 4 Strict, Affine, and Structural Logic

Contraction permits contractible antecedents to behave as sets. Weakening is delayed toward the root in forward search and represented by subsumption: a proof from fewer assumptions is stronger. Forward and backward subsumption remove redundant facts. Affine rule matching may omit a premise resource, and additive contexts combine with multiset maximum. Mixed adjoint logics must apply the correct policy per mode.

### 5 $\top$ and $0$ Revisited

The source marks this discussion as not covered live. Their nullary rules would otherwise enumerate arbitrary contexts or succedents. Two proposed devices are weakenable sequents, annotated with $W$, or context/succedent metavariables instantiated during rule application. Either choice requires a formal account of mixed precise and open facts.

## 5. Formal core

For goal $G$, let $\operatorname{Sub}_L(G)$ and $\operatorname{Sub}_R(G)$ be its side-correct labeled occurrences. A database $D$ contains derivable specialized sequents. One saturation step adds the conclusion of rule $r$ when all premises occur in $D$ and resource constraints hold. Stop successfully if $G\in D$; stop unsuccessfully only at a fixed point $D'=D$ in a search space where saturation is complete.

With weakening,

$$
(\Delta\vdash A)\le(\Delta'\vdash A')\iff \Delta\subseteq\Delta'\land A=A'.
$$

Forward subsumption discards a new weaker fact; backward subsumption removes an old weaker fact. $\Delta$ is a multiset/set according to regime, and $A,A'$ are labeled succedents.

## 6. Operational/computational reading

The prover is a production system over sequents. The database is structural even though each stored sequent describes linear resources. Breadth-first evaluation shares intermediate lemmas and makes failure a fixed-point fact. Focused rules are compiled proof macros; provenance links allow the final database fact to be expanded into an ordinary cut-free derivation.

## 7. Worked derivation or trace in original notation and prose

For $A\multimap(B\mathbin{\&}C)\vdash(A\multimap B)\mathbin{\&}(A\multimap C)$, name $L_0=A\multimap L_1$, $L_1=B\mathbin{\&}C$, $R_1=A\multimap B$, $R_2=A\multimap C$, and $R_0=R_1\mathbin{\&}R_2$.

1. Seed $A\vdash A$, $B\vdash B$, $C\vdash C$.
2. Left projections give $L_1\vdash B$ and $L_1\vdash C$.
3. Specialized implication-left gives $A,L_0\vdash B$ and $A,L_0\vdash C$.
4. Implication-right gives $L_0\vdash R_1$ and $L_0\vdash R_2$.
5. Additive right combines the same $L_0$ context, yielding $L_0\vdash R_0$.

The recorded rule names and premise indices reconstruct the proof tree.

### Extended algorithmic reading and saturation example

**Section 1** identifies the inverse method's real advantage: failed subgoals are not rediscovered along unrelated backward branches. Forward facts are memoized lemmas. This does not make unrestricted forward chaining sensible; relevance comes from compiling the particular goal. Side labels matter because an occurrence under the antecedent of implication changes sequent side. Two textually equal atoms may therefore receive distinct left/right roles and participate in different specialized rules.

**Section 2** gives the unfocused algorithm. First remove cut and expand identity to atomic identity so the subformula property is explicit. Next enumerate side-correct occurrences of the goal and instantiate each logical rule only with those names. Initialize $D_0$ with the legal identity facts. Define

$$D_{i+1}=D_i\cup\{\operatorname{concl}(r\theta)\mid
\operatorname{prem}(r\theta)\subseteq D_i\text{ and resource side conditions hold}\}.$$

The substitution $\theta$ chooses labeled occurrences, not arbitrary formulas. Every inserted fact should retain a provenance pair consisting of the specialized rule and pointers to premise facts. Discovery of the goal then yields a proof by recursively following pointers. If the finite database reaches $D_{i+1}=D_i$ without the goal, completeness of the specialization justifies failure; without finiteness or completeness, it justifies only “not found yet.”

**Section 3** compiles maximal phases rather than individual rules. A stable sequent has no invertible rule immediately applicable. One focused macro selects a positive formula on the right or negative formula on the left, performs its synchronous decomposition, and then performs all resulting invertible work until stable premises are exposed. Suspended atoms mark phase boundaries. The database consequently omits transient sequents that differ only by deterministic decomposition. Multiplicity remains visible: a fact containing $A,A$ cannot be silently reduced to $A$ in linear logic.

**Section 4** changes the ordering used for redundancy. In strict/linear logic, contexts are multisets and exact multiplicity matters. In affine logic, weakening means a derivation from fewer resources can be used in a larger context, so the smaller antecedent subsumes the larger one. In structural logic contraction additionally makes repeated copies irrelevant, so antecedents can be normalized to sets. For additive combination under affine use, multiset maximum supplies enough copies for either branch without adding the branches' demands. Mixed-mode logic must compare each context component with its own preorder; applying structural set normalization to a linear mode would be unsound.

**Section 5** exposes why nullary rules are awkward in a finite ground database. The right rule for $\top$ succeeds under any antecedent, and the left rule for $0$ can conclude any succedent. Materializing every such instance defeats specialization. A `W` annotation denotes an open, weakenable part of a sequent, while a context metavariable denotes the same openness at rule-application time. Either technique compactly represents a family of facts, but matching and subsumption must know which portion is precise.

As a small original saturation, test the linear sequent $A\otimes B\vdash B\otimes A$. Label the left tensor $L$, its exposed atoms $A_L,B_L$, and the right tensor $R$ with atoms $B_R,A_R$. Seeds are $A_L\vdash A_R$ and $B_L\vdash B_R$. Specialized tensor-left compiles the assumption $L$ into the multiset $A_L,B_L$. Tensor-right partitions that multiset: the $B_L$ fact proves $B_R$, and the $A_L$ fact proves $A_R$. The conclusion $L\vdash R$ is inserted with two premise pointers. The partition is essential. Giving both premises the whole context would duplicate resources; giving one premise both atoms would leave the other unproved.

Now compare $A\vdash A\otimes A$. There is one identity seed $A_L\vdash A_R$, but tensor-right needs two disjoint premise resources. Saturation cannot manufacture the second $A_L$, so no goal fact appears. In a structural regime, contraction changes the specialized matching policy and the corresponding formula may succeed. This contrast demonstrates that the database's own reuse is meta-level: using the same stored identity fact twice cannot license two uses of one object-level linear assumption unless the rule's resource accounting permits it.

Implementation quality depends on fair rule scheduling, canonical context representation, and duplicate detection. Breadth-first rounds give shortest macro proofs but are not logically mandatory. Indexing rules by newly added premises avoids rescanning everything. Provenance must be retained even when subsumption removes a fact, or reconstruction needs a replacement witness. Finally, focused proof macros must expand to ordinary cut-free derivations; treating them as unexplained axioms would invalidate the prover.

Additional checks: **Is fixed-point failure always decidability?** Only when the compiled fact space is finite and saturation complete. **Why can a stronger fact have fewer affine assumptions?** Weakening can add the unused ones later. **Does focusing change provability?** No; it changes the granularity and canonical organization of search. **What makes the inverse method goal directed?** The side-labeled subformula closure used to generate rules.

## 8. Conceptual synthesis

The inverse method compiles one theorem-proving problem into a goal-specific forward calculus. The subformula property supplies relevance, focusing supplies granularity, and resource structure supplies redundancy criteria. The method can semi-decide an undecidable logic: finding a goal is conclusive, while nontermination says nothing.

## 9. Common confusions and failure modes

- Naive forward inference is not the inverse method.
- The inference database is reusable; the formulas inside a fact remain linear.
- Additive right premises must agree on usable context unless an affine maximum rule applies.
- Saturation failure is conclusive only when the search space and calculus justify it.
- $0$ and $\top$ need open-context machinery, not brute-force enumeration.

## 10. Self-test questions with concise answers

1. **Why label sides?** Implication can move a subformula across the turnstile, so occurrence side constrains rule instances.
2. **What seeds search?** Eligible atomic identity sequents.
3. **What is a focused fact?** A stable sequent between maximal inversion/focus phases.
4. **Why reject two copies of a linear atom?** No backward proof from a goal with one copy can create the extra occurrence.
5. **How is weakening handled?** By subsumption and relaxed premise matching, not eager enumeration.

## 11. Related concept pages

- [Forward proof search and the inverse method](../Concepts/Forward-Proof-Search-and-Inverse-Method.md)
- [Strict, affine, linear, and structural regimes](../Comparisons/Resource-Regimes.md)
- [Partial focusing](../Concepts/Partial-Focusing.md)

## 12. Source trail

Lecture 18 “The Inverse Method”: §1, printed pp. L18.1–L18.2, PDF pp. 187–188; §2, L18.2–L18.6, PDF pp. 188–192; §3, L18.6–L18.10, PDF pp. 192–196; §4, L18.10–L18.12, PDF pp. 196–198; §5, L18.12–L18.13, PDF pp. 198–199; references end on L18.14, PDF p. 200.

## 13. Previous/next navigation

Previous: [Lecture 17 — Data Layout](Lecture-17-Data-Layout.md). Next: [Lecture 19 — Resource Semantics](Lecture-19-Resource-Semantics.md).


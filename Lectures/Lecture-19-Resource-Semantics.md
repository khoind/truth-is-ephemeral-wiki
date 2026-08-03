---
title: "Lecture 19 — Resource Semantics"
lecture: 19
date: 2023-11-16
pdf_pages: "201–209"
printed_pages: "L19.1–L19.9"
tags:
  - lecture-guide
  - resource-semantics
  - translation
prerequisites:
  - "[Lecture 18 — The Inverse Method](Lecture-18-The-Inverse-Method.md)"
  - "[Resource semantics](../Concepts/Resource-Semantics.md)"
---

# Lecture 19 — Resource Semantics

## 1. Why this lecture exists

Substructural logics enforce resource use syntactically, but one can also expose that use inside a structural logic. Since full linear logic with exponentials is undecidable, the target must be intuitionistic predicate logic rather than decidable propositional intuitionistic logic. Explicit resource terms reveal what a derivation consumes, explain validity as empty use, and support a compositional translation after untethering.

## 2. Learning objectives

- distinguish operational, denotational, proof-theoretic, and resource interpretations;
- manipulate resource expressions as a free commutative monoid;
- read the explicit-resource cut and connective rules;
- state both directions of adequacy;
- interpret validity using $\epsilon$; and
- translate negative formulas after untethering.

## 3. Dependency map

[Resource regimes](../Comparisons/Resource-Regimes.md) $\rightarrow$ algebraic laws. Linear sequents $\rightarrow$ [explicit-resource calculus](../Comparisons/Sequent-Calculus-SAX-and-Explicit-Resources.md). Empty receipt $\rightarrow$ validity. Local antecedent receipts $\rightarrow$ [untethered predicate translation](../Concepts/Validity-and-Untethering.md). Adequate encodings anticipate [logical frameworks](Lecture-20-Logical-Frameworks.md).

## 4. Section-by-section reconstruction covering every numbered heading

### 1 Introduction

Rather than interpret logic in a classical mathematical domain, the lecture interprets one constructive language in another. A direct embedding of undecidable linear logic with exponentials into decidable structural propositional logic cannot exist. Intuitionistic predicate calculus is expressive enough. The plan is first to design a structural proof system with explicit usage, then turn it into a translation.

### 2 A Sequent Calculus with Explicit Resources

$A[\alpha]$ labels an antecedent resource; $C[p]$ records the combination used. Linear combination $*$ is associative, commutative, and has unit $\epsilon$, with no other equations. Labels are unique and do not repeat in receipts. Structural weakening keeps irrelevant assumptions available while their labels remain absent. Fresh-label cut substitutes the first proof's receipt for the cut label. Identity expansion, principal cut reduction, strengthening, and weakening confirm the design. Adequacy maps a linear context to distinct labels and maps back by restricting to labels in the receipt.

### 3 Adding Validity

A structural proposition is represented by $A[\epsilon]$: it needs no linear resource. The shift rules reproduce independence conditions by requiring empty receipts. A valid upshift can generate a fresh usable $A[\alpha]$ without adding cost. Identity expansion confirms that negative $\uparrow$ must be introduced on the right before it is used on the left. Adequacy now separates structural $\epsilon$-labeled assumptions from linear labeled ones.

### 4 Untethering

Initially, linear left rules are tethered to the succedent receipt. Allowing complex receipts on antecedents lets a formula carry its own justification. Untethered implication combines the implication cost $p$ and argument cost $q$ into $p*q$ for the result. This suggests the indexed translation $A@p$ into first-order intuitionistic logic. Atomic propositions become predicates of resources; implication quantifies an argument receipt; additive conjunction shares one receipt. With monoid laws axiomatized, $\cdot\vdash A$ iff $\cdot\vdash A@\epsilon$.

## 5. Formal core

Resource syntax is $p::=\epsilon\mid\alpha\mid p*q$ modulo commutative-monoid laws. The cut rule is

$$
\frac{\Gamma\vdash A[q]\quad\Gamma,A[\alpha]\vdash C[p*\alpha]}
{\Gamma\vdash C[p*q]}\;\mathsf{cut}_\alpha,
$$

with fresh $\alpha$. $\Gamma$ is structural; $A,C$ are object formulas; $p,q$ are resource terms. Tensor right multiplies receipts; additive conjunction right requires the same receipt in both premises. The translation clauses include

$$
P@p=P(p),\quad(A\multimap B)@p=\forall\alpha.(A@\alpha)\supset(B@(p*\alpha)).
$$

## 6. Operational/computational reading

This is principally a semantic interpretation, not the future runtime. Still, one may read a receipt as provenance: a proof computes a symbolic account of its inputs. Cut performs symbolic substitution, additive branching demands a common account, and $\epsilon$ certifies independence. Structural context operations are harmless because the receipt decides what counts.

## 7. Worked derivation or trace in original notation and prose

Translate $(P\mathbin{\&}Q)\multimap P$ at $\epsilon$:

$$
\begin{aligned}
((P\mathbin{\&}Q)\multimap P)@\epsilon
&=\forall\alpha.((P\mathbin{\&}Q)@\alpha)\supset(P@(\epsilon*\alpha))\\
&=\forall\alpha.(P(\alpha)\land Q(\alpha))\supset P(\alpha).
\end{aligned}
$$

The last formula is intuitionistically provable. By contrast, $P\multimap(Q\multimap P)$ translates to a conclusion $P(\alpha*\beta)$ from $P(\alpha)$ and $Q(\beta)$; no commutative-monoid equation deletes $\beta$, correctly reflecting linear unprovability.

### Extended rule reading and receipt calculation

**Section 1** should be understood as an adequacy problem, not a complexity trick. The target structural calculus may weaken and contract assumptions, but an index attached to the conclusion records exactly which named source resources justify it. Because first-order variables can range over resource expressions, predicate logic can state this index compositionally. An embedding into decidable propositional intuitionistic logic would wrongly decide the source fragment with exponentials, which explains the need for the stronger target rather than merely motivating it by convenience.

**Section 2** introduces a free commutative monoid of receipts. “Free” means that equality is generated only by associativity, commutativity, and the unit equations for $\epsilon$; in particular, there is no idempotence $p*p=p$ and no cancellation that deletes an input. Each antecedent assumption receives a fresh atom such as $A[\alpha]$. A derivation of $C[p]$ may live in a large structural context, but the atoms occurring in $p$ are its actual linear support. Tensor right combines disjoint supports by $*$, whereas additive conjunction right requires the same support for both alternatives.

The displayed cut rule is symbolic substitution. The second premise's receipt contains the unique fresh placeholder $\alpha$ for its use of $A$. The first premise computes $q$, the support needed to obtain $A$. Replacing $\alpha$ by $q$ changes $p*\alpha$ to $p*q$. If the placeholder repeated, substitution would duplicate $q$; if it were absent, the cut proof would not use its first premise. Those are legitimate behaviors only in resource regimes with corresponding structural rules, not in this linear accounting.

Adequacy has two directions. **Preservation** labels every formula in a linear derivation distinctly and shows that the translated structural derivation's receipt contains exactly the labels consumed. **Reflection** reads a structural explicit-resource proof back by discarding assumptions whose labels are absent and replacing receipt composition by context splitting. Reflection is why receipts cannot be treated as informal comments: their invariants are needed to recover a source proof.

**Section 3** interprets validity as zero cost. A judgment $A[\epsilon]$ states that $A$ has a proof independent of all linear labels. Such a result can be made available structurally and then instantiated with a fresh usage label when crossing the shift boundary. The negative polarity of $\uparrow$ fixes rule order: right introduction establishes independence before left use exposes reusable content. Merely assigning $\epsilon$ to any assumption would be unsound because it would assert validity rather than prove it.

**Section 4** untethers receipts from the final succedent. An antecedent $A[p]$ now carries its own justification, so a left rule can combine local evidence without mentioning a particular final goal. This makes the formula translation compositional. In $(A\multimap B)@p$, the index $p$ records the resource cost of the function itself; an arbitrary argument resource $\alpha$ yields a result indexed by $p*\alpha$. The quantifier is framework-level first-order quantification over receipts. For $A\mathbin{\&}B$, both components are interpreted at the same index because additive choice offers either observation from one common resource account.

Here is a cut calculation independent of the earlier formula translation. Assume

$$\Gamma\vdash A[\beta*\gamma]$$

and

$$\Gamma,A[\alpha]\vdash C[\delta*\alpha].$$

Fresh-label cut yields $\Gamma\vdash C[\delta*(\beta*\gamma)]$. By associativity and commutativity this is equal to $C[\beta*\delta*\gamma]$, but it is not equal to $C[\delta*\beta]$: the atom $\gamma$ cannot disappear. If the source were ordered, we would drop commutativity and preserve the sequence $\delta,\beta,\gamma$; if affine, an additional preorder could permit unused factors. Thus changing the algebra systematically changes the resource regime.

As another boundary test, $(P\mathbin{\&}Q)@\rho$ supplies both $P(\rho)$ and $Q(\rho)$, but $P\otimes Q$ requires receipts that combine as $p*q$. Conflating these clauses would turn additive shared evidence into multiplicative divided evidence. Likewise, $*$ in an index is not a proof term for object-language tensor; it belongs to the semantic resource algebra.

Operational language is useful only with care. A receipt resembles provenance or a usage certificate, and cut resembles substituting provenance graphs. Yet the lecture is not specifying heap execution, blocking, or scheduling as Lecture 16 did. Its computation is proof transformation in the target calculus. The principal metatheorems—identity expansion, cut reduction, strengthening, and weakening—show that this bookkeeping is stable under normal proof operations.

Additional checks: **Can an unused structural assumption appear in $\Gamma$?** Yes; absence of its label from the receipt records nonuse. **Why does $\epsilon*p=p$ matter?** Valid evidence adds no linear cost. **What prevents duplication?** Lack of an idempotence equation and uniqueness of usage labels. **What does untethering buy?** A local interpretation $A@p$ that composes by formula structure rather than by the surrounding sequent.

Receipt normalization is also part of proof checking. Since $p*(q*r)$ and $r*p*q$ denote the same commutative-monoid element, an implementation needs a canonical representation, such as a multiset of atoms, to compare indices. Canonicalization must preserve multiplicity: sorting $\alpha*\alpha*\beta$ is valid, collapsing the duplicate $\alpha$ is not. This makes equality decidable for the free algebra used here and turns side conditions such as equal additive receipts into concrete checks.

The translation theorem is stated at the empty receipt because a closed source theorem consumes no external linear assumptions. Open adequacy is richer: distinct labels relate a source context to the free variables in an index, and reflection reconstructs exactly that selected subcontext. The closed equivalence is the visible endpoint of this stronger invariant.

## 8. Conceptual synthesis

Explicit-resource semantics internalizes the difference between being present and being used. The target calculus can be structural because usage is carried by indices. Validity is not magical duplication; it is zero resource cost. Untethering trades a close proof-step correspondence for compositional formula semantics.

## 9. Common confusions and failure modes

- $*$ is semantic resource combination, not object tensor.
- Structural target assumptions are not all used.
- $\alpha*\alpha$ is not $\alpha$ in the linear model.
- Repeated labels break the lecture's uniqueness presupposition.
- Adequacy requires preservation and reflection.

## 10. Self-test questions with concise answers

1. **Why predicate logic?** The source with exponentials is undecidable, so a decidable propositional target cannot be adequate.
2. **What does $C[\epsilon]$ mean?** $C$ is justified without linear resources.
3. **Why is cut label $\alpha$ fresh?** Its receipt occurrence must uniquely identify the substituted cut resource.
4. **How model ordered logic?** Drop commutativity of $*$.
5. **What is untethering?** Giving antecedents complex local receipts rather than tying their rules directly to the goal receipt.

## 11. Related concept pages

- [Resource semantics](../Concepts/Resource-Semantics.md)
- [Sequent calculus, SAX, and explicit resources](../Comparisons/Sequent-Calculus-SAX-and-Explicit-Resources.md)
- [Validity and untethering](../Concepts/Validity-and-Untethering.md)

## 12. Source trail

Lecture 19 “Resource Semantics”: §1, printed pp. L19.1–L19.2, PDF pp. 201–202; §2, L19.2–L19.5, PDF pp. 202–205; §3, L19.5–L19.7, PDF pp. 205–207; §4, L19.7–L19.8, PDF pp. 207–208; references, L19.8–L19.9, PDF pp. 208–209.

## 13. Previous/next navigation

Previous: [Lecture 18 — The Inverse Method](Lecture-18-The-Inverse-Method.md). Next: [Lecture 20 — Logical Frameworks](Lecture-20-Logical-Frameworks.md).


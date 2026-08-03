---
title: "Lecture 21 — Substructural Frameworks"
lecture: 21
date: 2023-11-30
pdf_pages: "220–228"
printed_pages: "L21.1–L21.9"
tags:
  - lecture-guide
  - llf
  - metatheory
prerequisites:
  - "[Lecture 20 — Logical Frameworks](Lecture-20-Logical-Frameworks.md)"
  - "[Representing sequent derivations](../Concepts/Representing-Sequent-Derivations.md)"
---

# Lecture 21 — Substructural Frameworks

## 1. Why this lecture exists

Structural LF can faithfully encode structural sequent proofs but silently permits weakening and contraction, so it cannot directly enforce linear antecedents. This lecture develops the representation of sequents, then extends LF to LLF with linear resources and additives. It closes by separating object-level proof constructors from meta-level total relations used to establish theorems about encodings.

## 2. Learning objectives

- encode propositions, antecedents, succedents, and derivations separately;
- use focusing to justify representation adequacy;
- explain the weakness/parametricity of LF function spaces;
- encode linear SAX rules in LLF;
- explain why framework additive conjunction is required; and
- distinguish object cut from a metatheoretic cut-admissibility relation.

## 3. Dependency map

[Judgments as types](../Concepts/Logical-Frameworks-and-Judgments-as-Types.md) $\rightarrow$ `ante`/`succ` encoding. Canonical LF focusing $\rightarrow$ derivation reflection. Structural mismatch $\rightarrow$ [LLF](../Concepts/Linear-Logical-Frameworks-and-Metatheory.md). Positive multi-conclusion limitation $\rightarrow$ [Lecture 22](Lecture-22-The-Concurrent-Logical-Framework.md).

## 4. Section-by-section reconstruction covering every numbered heading

### 1 Introduction

The lecture continues LF's representation methodology, identifies limitations, and develops substructural extensions. It emphasizes that an encoding targets a specific inference system, not a logic in the abstract.

### 2 Representing Sequent Derivations

Object formulas map into `prop`; two type families `ante` and `succ` distinguish sequent sides. A derivation $A_1,\ldots,A_n\vdash C$ becomes an LF object of `succ C` under assumptions `ante A_i`. Implication right uses a framework function to discharge `ante A`; implication left uses both a proof of its antecedent and a hypothetical proof from its consequent. Focusing shows every canonical inhabitant is headed by a matching rule constructor, yielding the reflection direction of adequacy. Weak functions are parametric and cannot inspect their arguments.

### 3 A Linear Logical Framework

LLF adds linear implication and linear assumptions while retaining structural functions and signature declarations. Linear sequent antecedents map to $x_L:\mathsf{ante}\,A$. SAX's implication right, implication axiom, and identity become linear constructors. Object additive conjunction creates a difficulty because its right rule shares the same linear context across both premises. Adding framework $\mathbin{\&}$ makes that sharing an invertible meta-level operation. Encoded cut can then show ordinary left rules derivable from SAX axioms.

### 4 Metatheoretic Reasoning

An admissibility proof is an algorithm transforming derivations, but ordinary LF functions cannot case-analyze proof objects. Twelf represents the algorithm as a relation with input and output derivations, then verifies totality. Coverage ensures every input shape is handled and termination ensures recursive calls decrease. Substructural metatheory is less settled; resource semantics and richer contextual systems offer approaches.

## 5. Formal core

The representation judgment is

$$
x_{1m}:\mathsf{ante}\,\ulcorner A_1\urcorner,\ldots,x_{nm}:\mathsf{ante}\,\ulcorner A_n\urcorner
\vdash_\Sigma\ulcorner D\urcorner:\mathsf{succ}\,\ulcorner C\urcorner,
$$

where mode $m=S$ in LF and $m=L$ for linear LLF antecedents. Framework declarations stay structural. A cut-admissibility relation takes encoded proof(s) as inputs and an output proof as its final index; it is a metalevel type family, not an object-language inference constant.

## 6. Operational/computational reading

Canonical type checking is proof checking. Framework lambdas implement hypothetical judgments and assumption discharge. Linear lambda/application certify exact use. A total relation executes a metaproof algorithm by pattern-matching on constructors at the meta level; its totality certificate establishes the theorem for all encoded inputs.

## 7. Worked derivation or trace in original notation and prose

Represent implication right:

1. Assume encoded context $\ulcorner\Gamma\urcorner$.
2. Extend it with $x:\mathsf{ante}\,\ulcorner A\urcorner$.
3. By induction, $M(x):\mathsf{succ}\,\ulcorner B\urcorner$ represents the premise $\Gamma,A\vdash B$.
4. Abstract: $\lambda x.M(x):\mathsf{ante}\,A\to\mathsf{succ}\,B$ (or $\multimap$ in the linear encoding).
5. Apply `impR A B` to obtain a canonical object of `succ (imp A B)`.
6. Conversely, focusing on any canonical inhabitant of that atomic succedent forces head `impR` and recovers a premise representation.

### Extended reconstruction: matching the framework to the object calculus

**Section 1** makes adequacy sensitive to structural discipline. A beautiful LF signature can still be wrong if the framework admits operations the object calculus forbids. In ordinary LF, a hypothetical assumption may be ignored or used repeatedly. That is exactly right for structural derivations and exactly wrong for a linear antecedent. The progression LF $\rightarrow$ LLF $\rightarrow$ CLF is therefore driven by representation failures, not by a desire to accumulate connectives.

**Section 2** separates four representations. An object formula $A$ becomes an LF object $\ulcorner A\urcorner:\mathsf{prop}$. `ante` and `succ` are distinct type families over `prop`, because the same formula has different rule behavior on the two sequent sides. A context is represented by LF assumptions $x_i:\mathsf{ante}\,\ulcorner A_i\urcorner$. Finally, a derivation $D$ is represented by a canonical object of $\mathsf{succ}\,\ulcorner C\urcorner$ under those assumptions. Collapsing any pair—for example, treating formulas themselves as derivations—destroys the intended indexing.

Implication right illustrates hypothetical representation. A premise derivation under a new antecedent variable becomes an LF function; the constructor for right introduction consumes that function. Implication left is more subtle: it consumes a derivation of the antecedent and a hypothetical derivation continuing from the consequent. Focusing supplies reflection. If the goal is an atomic `succ` type, a canonical inhabitant must focus on a signature constant whose result unifies with that type, so its spine exposes exactly the encoded premises.

Weak LF functions are valuable because they are parametric. A function representing an object hypothetical derivation may use its argument only through its declared type; it cannot inspect the internal syntax of an arbitrary proof argument unless the signature explicitly provides such an eliminator. This blocks many exotic encodings. It does not by itself establish adequacy: one still proves that canonical inhabitants and object derivations correspond.

**Section 3** replaces structural local assumptions by linear ones where the object antecedent is linear. The framework judgment now has structural and linear zones; the latter must be split at multiplicative application and consumed exactly once. Signature declarations remain structural because inference rules must be selectable any number of times. A framework linear arrow $A\multimap B$ represents a function consuming one $A$ resource, while ordinary arrow remains available for parameters and reusable hypotheses.

Object additive conjunction reveals why linear implication alone is insufficient. The object rule

$$\frac{\Gamma\vdash A\qquad\Gamma\vdash B}{\Gamma\vdash A\mathbin{\&}B}$$

checks two alternatives against the same linear context; it does not split or duplicate the resources in one execution. Framework additive conjunction internalizes exactly this shared-context inversion. Encoding the premises with positive tensor would instead divide the context and misrepresent the rule.

An original resource check clarifies the difference. Let $x_L:\mathsf{ante}\alpha$ and suppose constructors derive both `succ beta` and `succ gamma` using $x_L$. A framework term of type `succ beta & succ gamma` may contain two branches each checked under the same $x_L$, because a client chooses one branch. A term of tensor type would need to construct both components together and would have to split $x_L$; using it in both halves would be rejected. Additive sharing is therefore logical choice, not runtime cloning.

SAX encodings can make left rules derivable rather than primitive. Axiom-like process constructors and an encoded cut compose to simulate the ordinary rule. This is an object-level derivation inside LLF: it says a term inhabits the encoded rule type. It should not be confused with the framework metatheorem that cut can be eliminated from every represented proof.

**Section 4** explains that latter distinction. LF functions are intentionally too weak to recursively inspect arbitrary canonical derivations by constructor. Twelf-style metatheory declares a relation such as `cutadmit D E F`, where input indices represent derivations to transform and the output index represents the resulting cut-free derivation. Clauses pattern-match through relation declarations. A totality checker establishes **coverage**—every well-typed input shape matches some clause—and **termination**—recursive calls decrease according to a declared ordering. Together with mode information saying which arguments are inputs and outputs, totality turns the relation into a verified transformation.

For example, the identity case of a cut-admissibility relation receives an encoded identity proof on one side. Its output can be the other input proof, with the appropriate hereditary substitution/renaming. An implication principal case recursively cuts smaller premise derivations and rebuilds the constructor. The measure and coverage proof are metalevel artifacts; they are not constructors in the represented object logic.

Substructural metatheory complicates contexts because a recursive call may consume, split, or return resources. Merely reusing structural Twelf techniques can reintroduce weakening or contraction. Resource semantics can make usage explicit, while contextual or substructural frameworks track context transformations directly. The lecture presents this as an active methodological boundary, not as a solved automatic procedure.

Additional checks: **Why are signature constants reusable?** They represent rules, not object resources. **Does an LLF linear variable mean its formula is linear syntax?** No; it means that assumption occurrence is governed linearly. **What proves reflection?** Canonical-form/focusing analysis plus signature-specific adequacy. **What is the difference between `cut` and `cutadmit`?** The former is represented object syntax; the latter is a total meta-level relation transforming proofs.

The mode split can be tested syntactically. Structural parameters may occur zero, one, or many times in a canonical term; linear proof assumptions must occur exactly once along each multiplicative execution path. Additive branches are checked separately against the same linear zone because only one projection is later selected. These are framework typing facts, not informal conventions attached to constructor names.

Totality likewise has two independent failure modes. A relation may terminate on every clause it covers yet omit a proof constructor, so it is not total. Or it may cover every constructor but recurse without a decreasing measure. Coverage and termination must both succeed before the relational program establishes a metatheorem for all represented derivations.

## 8. Conceptual synthesis

Adequate representation depends on matching resource regimes at both levels. LLF is not LF plus a decorative connective: it changes which encodings are valid. Additives show that exact context behavior must be built into the framework. Metatheory then requires a second distinction—represented proof constructors versus verified transformations over them.

## 9. Common confusions and failure modes

- Encoding formulas is not encoding derivations.
- `ante A` and `succ A` are different judgments.
- Signature rules must be reusable even for linear object logic.
- Object additive branching does not duplicate linear resources.
- A `cut` constructor proves derivability with cut; a total `cutadmit` relation proves cut admissible without it.

## 10. Self-test questions with concise answers

1. **Why two judgment families?** Sequent side determines rule behavior.
2. **Why is structural LF inadequate for linear antecedents?** Its local assumptions may be weakened or contracted.
3. **Why add framework $\mathbin{\&}$?** Its inversion shares one linear context across two branches.
4. **What makes weak functions safe for encoding?** They are parametric and do not inspect arguments.
5. **How does Twelf express a metatheorem?** As a relation whose totality is checked.

## 11. Related concept pages

- [Representing sequent derivations](../Concepts/Representing-Sequent-Derivations.md)
- [Linear logical frameworks and metatheoretic reasoning](../Concepts/Linear-Logical-Frameworks-and-Metatheory.md)
- [Sequent calculus, SAX, and explicit resources](../Comparisons/Sequent-Calculus-SAX-and-Explicit-Resources.md)

## 12. Source trail

Lecture 21 “Substructural Frameworks”: §1, printed p. L21.1, PDF p. 220; §2, L21.1–L21.4, PDF pp. 220–223; §3, L21.4–L21.7, PDF pp. 223–226; §4, L21.7–L21.8, PDF pp. 226–227; references, L21.8–L21.9, PDF pp. 227–228.

## 13. Previous/next navigation

Previous: [Lecture 20 — Logical Frameworks](Lecture-20-Logical-Frameworks.md). Next: [Lecture 22 — The Concurrent Logical Framework](Lecture-22-The-Concurrent-Logical-Framework.md).


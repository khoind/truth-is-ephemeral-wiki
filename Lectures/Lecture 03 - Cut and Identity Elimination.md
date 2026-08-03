---
title: "Cut and Identity Elimination"
lecture: 3
date: "September 5, 2023"
pdf_pages: "26–42"
printed_pages: "L3.1–L3.17"
tags:
  - ordered-logic
  - sequent-calculus
  - cut-elimination
  - proof-theoretic-semantics
prerequisites:
  - "Hypothetical judgments"
  - "Ordered contexts"
  - "Left and right rules"
---

# Lecture 3 — Cut and Identity Elimination

## 1. Why this lecture exists

Writing introduction and elimination rules is not enough to show that they define a coherent logic. A badly oriented rule may silently permit exchange, discard an ordered resource, or make even $A \vdash A$ unprovable. This lecture supplies an internal test of the rules: general identity and cut should be unnecessary. Identity expansion shows that a compound proposition can explain itself through its own left and right rules; cut elimination shows that a proof consumed as a hypothesis can be inlined without adding expressive power. Together they establish the harmony needed for a proof-theoretic account of meaning.

## 2. Learning objectives

After this lecture, a reader should be able to:

- distinguish a proposition from a judgment and an antecedent from a succedent;
- state identity and cut for an ordered context;
- test a proposed connective rule by identity expansion and principal cut reduction;
- use $\bullet$, $\backslash$, $/$, $\mathbin{\&}$, $\oplus$, $1$, $\top$, and $0$ without confusing additive and multiplicative behavior;
- classify cut reductions as principal, identity, or commuting cases;
- explain why admissibility is a metatheorem, not another primitive inference rule.

## 3. Dependency map

The starting point is the [hypothetical judgment](<../Concepts/Hypothetical Judgments.md>) $\Omega \vdash A$, where $\Omega$ is an ordered sequence. Left and right rules give local meanings to connectives. [Ordered conjunction and implications](<../Concepts/Ordered Conjunction and Implications.md>) provide the main order-sensitive cases. [Additive and multiplicative connectives](<../Concepts/Additive and Multiplicative Connectives.md>) explain why some rules split a context while others reuse it across alternative premises. These ingredients support [identity and cut admissibility](<../Concepts/Identity and Cut Admissibility.md>), which in turn makes the proof terms of [Lecture 4](<Lecture 04 - Proof Terms.md>) computationally meaningful.

## 4. Section-by-section reconstruction covering every numbered heading

### 1. Introduction

A sequent $\Omega \vdash A$ separates assumptions from the proposition being established. $\Omega$ is the antecedent sequence; $A$ is the succedent. A rule acting on a top-level connective in an antecedent is a left rule, while one acting on the succedent is a right rule. Ordered logic keeps the position of every assumption visible.

Two principles connect the sides. Identity says an assumption $A$ can conclude $A$. Cut says that if $A$ has been proved, a use of an assumed $A$ may be replaced by that proof. These principles are useful, but a well-designed sequent calculus should not need them as primitive rules.

### 2. Right Rules Meeting Left Rules

The diagnostic method is modular: inspect one connective at a time. Replace a general identity with a derivation whose identities mention only smaller formulas, and replace a cut on a compound formula with cuts on its components. Dashed-rule notation in the source indicates that such a transformation is admissible at the metalevel.

#### 2.1 Ordered Conjunction $A \bullet B$

The proposition $A \bullet B$—“$A$ fuse $B$”—packages two adjacent ordered states. Its right rule splits the sequence in order; its left rule unpacks adjacent components:

$$
\frac{\Omega_1 \vdash A \qquad \Omega_2 \vdash B}
     {\Omega_1\,\Omega_2 \vdash A \bullet B}\;\bullet R
\qquad
\frac{\Omega_L\,A\,B\,\Omega_R \vdash C}
     {\Omega_L\,(A \bullet B)\,\Omega_R \vdash C}\;\bullet L.
$$

Identity for $A\bullet B$ expands by first unpacking on the left and then rebuilding on the right from identities for $A$ and $B$. A principal cut between $\bullet R$ and $\bullet L$ becomes a cut on $A$ followed by one on $B$. If the right rule swapped $\Omega_1$ and $\Omega_2$, identity would fail and, with primitive cut, exchange would become derivable. The supposedly ordered logic would collapse toward linear logic.

#### 2.2 Left Implication $A \backslash B$

$A\backslash B$ expects an $A$ immediately from its left-side state and produces $B$. The right rule abstracts an $A$ at the left edge; the left rule supplies a proof of $A$ from the material immediately before the implication:

$$
\frac{A\,\Omega \vdash B}{\Omega \vdash A\backslash B}\;\backslash R
\qquad
\frac{\Omega_A \vdash A \qquad \Omega_L\,B\,\Omega_R \vdash C}
     {\Omega_L\,\Omega_A\,(A\backslash B)\,\Omega_R \vdash C}\;\backslash L.
$$

Its identity expansion exposes the expected $A$, uses the implication to obtain $B$, and reabstracts. Its principal cut reduces to smaller cuts on $A$ and $B$. The smaller cuts may be scheduled in more than one order, so normalization is not necessarily deterministic.

### 3. Right Implication $B/A$

$B/A$ expects $A$ on its right. Thus $/R$ abstracts a right-edge $A$, and $/L$ obtains the argument from the segment following the implication:

$$
\frac{\Omega\,A \vdash B}{\Omega \vdash B/A}\;/R
\qquad
\frac{\Omega_A \vdash A \qquad \Omega_L\,B\,\Omega_R \vdash C}
     {\Omega_L\,(B/A)\,\Omega_A\,\Omega_R \vdash C}\;/L.
$$

This is the mirror image of $\backslash$. The direction is semantic: neither connective licenses moving an argument through other ordered assumptions.

### 4. Excursion: Parsing with the Lambek Calculus

Ordered antecedents can represent a word sequence. Assign names category $n$ and complete sentences category $s$. An intransitive verb has type $n\backslash s$; an adjective that consumes a name to its right has type $n/n$; a transitive verb can have $n\backslash(s/n)$. A proof of the sequent of word categories $\vdash s$ is then a parse.

Specialized left rules may combine adjacent categories directly, but they are weaker than the general rules. Parsing also demonstrates genuine search: combining a verb too early can strand an adjective, whereas first producing the noun phrase leaves the categories aligned. Overloaded words motivate external choice, since one lexical item may support alternative categories.

### 5. A Small Example

The two directional implications satisfy an associativity-like equivalence:

$$A\backslash(C/B) \dashv\vdash (A\backslash C)/B.$$

For the left-to-right direction, bottom-up $/R$ exposes $B$ on the right, then $\backslash R$ exposes $A$ on the left. The antecedent implication consumes $A$ by $\backslash L$, producing $C/B$, which consumes $B$ by $/L$. Atomic identities close the proof. The example previews invertibility: the right rules for the implications can be applied without sacrificing provability.

### 6. External Choice $(A \mathbin{\&} B)$

The source prints the connective in a font resembling “N”; here the standard TeX symbol $\mathbin{\&}$ is used. An antecedent $A\mathbin{\&}B$ may be used through either component, giving two left rules. To prove it, the same ordered context must prove both alternatives:

$$
\frac{\Omega\vdash A \qquad \Omega\vdash B}{\Omega\vdash A\mathbin{\&}B}\;\&R,
\qquad
\frac{\Omega_L A\Omega_R\vdash C}{\Omega_L(A\mathbin{\&}B)\Omega_R\vdash C}\;\&L_1,
\qquad
\frac{\Omega_L B\Omega_R\vdash C}{\Omega_L(A\mathbin{\&}B)\Omega_R\vdash C}\;\&L_2.
$$

The repeated $\Omega$ does not duplicate a run-time resource: a consumer chooses one left rule, so only one branch is ultimately used. Both right premises are needed because the producer cannot know which projection a later consumer will select.

### 7. The Empty State $(1)$

$1$ internalizes the empty ordered state. Its right rule requires no antecedents; its left rule erases the marker $1$ while preserving everything around it:

$$\frac{}{\cdot\vdash1}\;1R \qquad
\frac{\Omega_L\Omega_R\vdash C}{\Omega_L(1)\Omega_R\vdash C}\;1L.$$

It is the unit of fuse: $A\bullet1\dashv\vdash A\dashv\vdash1\bullet A$. Its principal cut vanishes immediately.

### 8. Disjunction $(A\oplus B)$

Internal choice reverses the additive pattern. A producer selects either $\oplus R_1$ or $\oplus R_2$; a consumer must handle both possibilities in $\oplus L$. The context is not split. Identity selects the same label on each branch, and a principal cut keeps only the consumer branch corresponding to the producer’s selected injection.

### 9. Truth $(\top)$

$\top$ is the nullary unit of external choice. It has a premise-free right rule $\Omega\vdash\top$ for every $\Omega$ and no left rule. Consequently no principal right/left cut case exists. Its identity expands directly with $\top R$.

### 10. Falsehood $(0)$

$0$ is the nullary unit of internal choice. It has no right rule and a premise-free left rule deriving any $C$ from an antecedent $0$. There can be no principal cut with a proof of $0$, because no cut-free proof can end in a $0$ right rule.

### 11. Admissibility of Identity, as a Theorem

If primitive identity is restricted to atomic propositions $P$, then $A\vdash A$ is admissible for every compound $A$. The proof is structural induction on $A$: use the top-level connective’s rules and invoke the induction hypotheses on its proper subformulas.

### 12. Admissibility of Cut, as a Theorem

Cut admissibility requires a nested, well-founded induction. Principal cases reduce the cut formula. Identity cases discard the identity and retain the other derivation. Commuting cases push cut above an inference not acting on the cut formula, keeping the formula fixed but replacing a premise with a strict subderivation. The lexicographic measure—first formula structure, then derivation structure—therefore decreases.

From admissibility follow elimination corollaries: any general identities can be expanded until only atomic ones remain, and every primitive cut can be removed from a derivation.

### 13. Summary

The ordered sequent calculus is coherent because each connective’s left and right rules meet correctly. Cut-free proofs use only subformulas of the goal sequent, so their semantic content is internal to that goal. The same proof architecture extends to linear, structural, and mixed systems, though their context disciplines change the commuting cases.

## 5. Formal core (rules/judgments/theorems, with each symbol explained)

The two central admissible rules are

$$
\frac{}{A\vdash A}\;\mathrm{id}_A
\qquad
\frac{\Omega\vdash A \qquad \Omega_L\,A\,\Omega_R\vdash C}
     {\Omega_L\,\Omega\,\Omega_R\vdash C}\;\mathrm{cut}_A.
$$

$A,B,C$ range over propositions. $P$ denotes an atom. $\Omega,\Omega_L,\Omega_R,\Omega_1,\Omega_2$ are ordered sequences; juxtaposition is sequence concatenation, not an exchangeable comma. $\cdot$ is the empty sequence. The turnstile $\vdash$ separates antecedents from the single succedent. The subscript on $\mathrm{id}_A$ or $\mathrm{cut}_A$ records the formula being expanded or eliminated.

Admissible means: whenever the premises have derivations in the cut-free calculus, an effective metalevel transformation constructs a derivation of the conclusion in that same calculus. It does **not** mean the displayed rule is available as an object-language proof step.

## 6. Operational/computational reading

Read identity as a wire carrying a resource unchanged. Read cut as connecting a producer of $A$ to a consumer that temporarily names an $A$. A principal reduction lets the producer’s introduction meet the consumer’s elimination and replaces their protocol with interactions on smaller components. A commuting reduction moves the connection toward the point where $A$ is actually introduced or consumed. This reading anticipates computation, but Lecture 3 itself proves a property of derivations rather than defining a machine.

## 7. Worked derivation or trace in original notation and prose

We derive the original sequent

$$P\,(P\backslash(Q/R))\,R\vdash Q.$$

Here $P,Q,R$ are atoms. The implication $P\backslash(Q/R)$ first needs $P$ on its left; the resulting $Q/R$ then needs $R$ on its right.

$$
\frac{
  \overline{P\vdash P}^{\mathrm{id}_P}
  \qquad
  \frac{
    \overline{R\vdash R}^{\mathrm{id}_R}
    \qquad
    \overline{Q\vdash Q}^{\mathrm{id}_Q}
  }{(Q/R)\,R\vdash Q}\;/L
}{P\,(P\backslash(Q/R))\,R\vdash Q}\;\backslash L
$$

Order is essential. The boundary sequent $R\,(P\backslash(Q/R))\,P\vdash Q$ cannot use the same derivation: $P$ is on the wrong side of $\backslash$, and $R$ is on the wrong side of $/$. No exchange rule is available to repair it.

## 8. Conceptual synthesis

Identity expansion checks that a connective can be understood from its components; cut reduction checks that introducing and then consuming it has no mysterious residual effect. The rules are therefore justified by their interaction rather than by an external truth table. Order makes this test especially sharp: a seemingly small reversal in a rule can validate exchange and destroy the intended resource semantics.

## 9. Common confusions and failure modes

- **Treating sequences as multisets.** $\Omega_1\Omega_2$ cannot silently become $\Omega_2\Omega_1$.
- **Calling cut “derived.”** Admissibility is a transformation on derivations; there may be no cut rule inside the calculus.
- **Checking only principal cuts.** A full theorem also needs identity and commuting cases.
- **Assuming normalization is deterministic.** Independent commuting cuts may be pushed in different orders.
- **Confusing additives with duplication.** Reusing $\Omega$ in both premises of $\&R$ represents alternatives required of one proof, not simultaneous consumption twice.
- **Reading invertibility from rule shape alone.** The reliable argument uses preservation of provability, developed further in Lecture 4.

## 10. Self-test questions with concise answers

1. **Why must $\bullet R$ preserve the order of its context split?** Because reversing the pieces breaks compound identity and can make exchange derivable.
2. **What decreases in a principal cut reduction?** The cut formula becomes a proper subformula.
3. **What decreases in a commuting case?** The cut formula stays fixed, but at least one premise derivation becomes a strict subderivation.
4. **Why does $\top$ have no principal cut reduction?** It has no left rule for a right rule to meet.
5. **Which side supplies the argument to $A\backslash B$?** The ordered material immediately to its left.
6. **What is the subformula consequence of cut elimination?** A cut-free derivation mentions only formulas built from subformulas of its end sequent.

## 11. Related concept pages

- [Hypothetical Judgments](<../Concepts/Hypothetical Judgments.md>)
- [Ordered Conjunction and Implications](<../Concepts/Ordered Conjunction and Implications.md>)
- [Additive and Multiplicative Connectives](<../Concepts/Additive and Multiplicative Connectives.md>)
- [Identity and Cut Admissibility](<../Concepts/Identity and Cut Admissibility.md>)
- [Proof Terms and Cut Reductions](<../Concepts/Proof Terms and Cut Reductions.md>)
- [Polarity and Invertibility](<../Concepts/Polarity and Invertibility.md>)

## 12. Source trail (lecture, numbered sections, printed-page range, PDF-page range)

- Frank Pfenning, *Cut and Identity Elimination*, Lecture 3, Sections 1–13, printed pp. L3.1–L3.17, PDF pp. 26–42.
- Connective-level identity and cut tests: Sections 2.1–10, printed pp. L3.3–L3.12, PDF pp. 28–37.
- Admissibility theorems and elimination corollaries: Sections 11–13, printed pp. L3.12–L3.16, PDF pp. 37–41. The references occupy printed p. L3.17, PDF p. 42.

## 13. Previous/next navigation

Previous: Lecture 2, *From Inference to Logical Connectives* (not authored in this assignment).

Next: [Lecture 4 — Proof Terms](<Lecture 04 - Proof Terms.md>).

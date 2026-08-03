---
title: "Identity and Cut Admissibility"
aliases:
  - "Identity expansion and cut elimination"
  - "Sequent-calculus harmony"
tags:
  - identity
  - cut
  - admissibility
  - normalization
source_lectures:
  - 3
  - 4
prerequisites:
  - "Hypothetical judgments"
  - "Left and right rules"
related:
  - "Ordered Conjunction and Implications"
  - "Proof Terms and Cut Reductions"
  - "Polarity and Invertibility"
---

# Identity and Cut Admissibility

## 1. One-sentence definition

**Identity admissibility reconstructs $A\vdash A$ from atomic identities, while cut admissibility transforms proofs of $\Omega\vdash A$ and $\Omega_LA\Omega_R\vdash C$ into a cut-free proof of $\Omega_L\Omega\Omega_R\vdash C$.**

## 2. Why the concept is needed

Identity and cut are compelling general reasoning principles, but taking them as primitive can hide defects in the logical rules. A connective could have mismatched left and right behavior while cut repairs the mismatch, or an incorrectly ordered rule could make exchange derivable. Proving the principles admissible shows that the connective rules already contain everything required to pass a proof from provider to consumer.

Admissibility also makes proof-theoretic semantics possible. Once cuts are removed, every inference decomposes formulas already present in the end sequent. Meaning is therefore explained through the proposition’s own subformulas instead of through an opaque intermediate lemma.

## 3. Intuitive model

**Intuition.** Identity is a transparent adapter: a resource offered as $A$ can be used as $A$. Identity expansion opens a compound adapter and reconnects its component wires. Cut is a temporary cable joining a producer of $A$ to a socket named $A$ in another proof. Cut elimination splices the cable away. This wiring picture suggests the transformations, but admissibility is formally a theorem about derivation construction.

## 4. Formal core

The general displays are

$$
\frac{}{A\vdash A}\;\mathrm{id}_A
\qquad
\frac{\Omega\vdash A\qquad\Omega_LA\Omega_R\vdash C}
     {\Omega_L\Omega\Omega_R\vdash C}\;\mathrm{cut}_A.
$$

$A,C$ are propositions, $P$ is an atomic proposition, and $\Omega,\Omega_L,\Omega_R$ are ordered sequences. The conclusion of cut substitutes the entire proof context $\Omega$ at the exact position where $A$ occurred. It does not exchange that context with either neighbor.

**Identity theorem.** In the calculus whose only primitive identities are $P\vdash P$, general $A\vdash A$ is admissible. Proof: structural induction on $A$. For $A=A_1\bullet A_2$, for example, use $\bullet L$ bottom-up, apply the induction hypotheses $A_1\vdash A_1$ and $A_2\vdash A_2$, then rebuild with $\bullet R$.

**Cut theorem.** In the calculus without primitive cut, the general cut display is admissible. The proof uses nested induction ordered lexicographically by:

1. the structure of the cut formula $A$; then
2. the structures of the two premise derivations $D$ and $E$.

The cases are:

- **Principal:** $D$ ends in a right rule for $A$ and $E$ in the matching left rule. Replace the cut by cuts on proper subformulas.
- **Identity:** either premise is identity on $A$. Remove the cut and keep the other derivation, with the evident variable/context correspondence.
- **Commuting:** a last inference acts on something other than $A$. Push cut into the relevant premise or premises and reapply that inference. The cut formula stays fixed, but a derivation argument becomes smaller.

Admissibility is a metatheorem: it gives an algorithm or relation that constructs a derivation in the smaller calculus. Derivability would instead mean that a rule’s conclusion has a proof assembled from object-level rules in each instance.

## 5. How to use/read it

To test new rules, first expand identity for the new compound. If the proof gets stuck or needs a forbidden structural rule, the left/right orientation is suspect. Next reduce a principal cut between each new right rule and each matching left rule. Confirm that every resulting cut mentions a strict subformula and that contexts appear in their original order.

For a full admissibility proof, do not stop there. Include base or identity cases and enumerate how cut commutes past every unrelated rule. State the decreasing measure explicitly; “push cuts upward until done” is not a termination argument by itself.

## 6. Worked example

Consider a principal cut on fuse. Let

$$D_1:\Omega_1\vdash A,\qquad D_2:\Omega_2\vdash B,
\qquad E':\Omega_LAB\Omega_R\vdash C.$$

$\bullet R$ combines $D_1,D_2$ into $\Omega_1\Omega_2\vdash A\bullet B$. $\bullet L$ turns $E'$ into $\Omega_L(A\bullet B)\Omega_R\vdash C$. Cutting them gives $\Omega_L\Omega_1\Omega_2\Omega_R\vdash C$.

Reduction proceeds stepwise:

1. Cut $D_1$ into the $A$ position of $E'$, obtaining $\Omega_L\Omega_1B\Omega_R\vdash C$.
2. Cut $D_2$ into the remaining $B$ position, obtaining $\Omega_L\Omega_1\Omega_2\Omega_R\vdash C$.

Both new cut formulas, $A$ and $B$, are proper subformulas of $A\bullet B$. The order is unchanged. This simultaneous decrease in logical complexity is the principal normalization step.

## 7. Non-example or boundary case

A commuting conversion that moves cut past a left rule may leave the cut formula unchanged. That is **not** a failure of the induction: the derivation component has become a strict subderivation, so the secondary measure decreases.

By contrast, merely rewriting a principal cut on $A\bullet B$ to another cut on the same $A\bullet B$ with equally large premises provides no well-founded progress. Likewise, a proposed $\bullet R$ that swaps its context pieces produces $\Omega_L\Omega_2\Omega_1\Omega_R$ after the obvious reduction, not the required conclusion. That mismatch is evidence against the rule, not permission to exchange.

## 8. Key consequences

- General identity can be eliminated down to atomic identity.
- Every derivation using primitive cut has a cut-free counterpart.
- Cut-free proofs satisfy the subformula property in this propositional calculus.
- Left and right rules are harmonious: introduction followed by use reduces internally.
- Principal reductions later support computational interpretations.
- Cut normalization may be nondeterministic even though every reduction is well founded under the theorem’s measure.

## 9. Relations to nearby concepts

[Hypothetical Judgments](<Hypothetical Judgments.md>) supplies the dependency structure that cut composes. [Ordered Conjunction and Implications](<Ordered Conjunction and Implications.md>) shows why context order must be preserved in every reduction. [Proof Terms and Cut Reductions](<Proof Terms and Cut Reductions.md>) encodes these transformations as term rewrites. [Polarity and Invertibility](<Polarity and Invertibility.md>) uses admissible identity and cut to show that one side of each connective preserves provability.

Identity expansion and cut elimination are related but not identical. The first decomposes a reflexive use of a compound formula; the second removes an intermediate formula joining two arbitrary derivations. “Identity elimination” means removing non-atomic identity occurrences from a given derivation, a corollary of identity admissibility.

## 10. Common mistakes

- Confusing an admissible rule with a primitive or derived object-language rule.
- Proving only principal reductions and declaring cut admissible.
- Omitting the lexicographic termination measure.
- Assuming the cut formula shrinks in every commuting case.
- Silently using exchange while rearranging ordered contexts.
- Claiming a unique cut-free normal form from cut admissibility alone.
- Calling the subformula property a premise rather than a consequence of cut freedom.

## 11. What to remember

- Identity expansion reduces compound identity to identities on components.
- Principal cut reduction reduces the cut formula; commuting reduction reduces a premise derivation.
- The proof is nested induction on formula and derivations.
- Admissibility lives at the metalevel.
- Order preservation is part of correctness.
- Cut elimination supports internal, compositional proof meaning.

## 12. Source trail

- Lecture 3, Sections 1–2, printed pp. L3.1–L3.5, PDF pp. 26–30: motivation, general rules, identity expansion, and principal reduction.
- Lecture 3, Sections 6–10, printed pp. L3.9–L3.12, PDF pp. 34–37: additive and nullary identity/cut cases.
- Lecture 3, Sections 11–13, printed pp. L3.12–L3.16, PDF pp. 37–41: admissibility theorems, nested induction, elimination corollaries, and subformula significance.
- Lecture 4, Section 3 and Section 6, printed pp. L4.6–L4.7 and L4.9–L4.10, PDF pp. 48–49 and 51–52: term-level reductions and metalevel status.


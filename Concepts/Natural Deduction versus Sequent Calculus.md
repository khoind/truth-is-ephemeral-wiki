---
title: "Natural Deduction versus Sequent Calculus"
aliases: ["ND and sequent calculus correspondence"]
tags: [natural-deduction, sequent-calculus, translation]
source_lectures: [23]
prerequisites: ["Sequent calculus", "Linear Natural Deduction"]
related: ["Linear Natural Deduction", "Harmony in Natural Deduction", "Bidirectional Type Checking"]
---
# Natural Deduction versus Sequent Calculus

## 1. One-sentence definition
**Linear ND and sequent calculus prove corresponding judgments but organize evidence as term-centered introduction/elimination versus sequent-centered right/left rules.**

## 2. Why the concept is needed
ND’s programs are useful only if they preserve the established logic. Translations supply external correctness, reveal where cut and identity enter, and show why sequent antecedents need more than arbitrary variable names.

## 3. Intuitive model
**Intuition.** Sequent calculus is a ledger of goal/resource transformations; ND is an expression language for constructing and consuming values. Translation resembles compilation, but derivations need not correspond step-for-step.

## 4. Formal core
Write $\vdash^{nd}$ for ordinary ND, $\vdash^{\uparrow\downarrow}$ for bidirectional ND, and $\vdash^{seq}$ for sequents.

1. If $\Delta\vdash^{nd}M:C$, then $\Delta\vdash^{seq}C$.
2. If $\Delta\vdash^{seq}C$, then some $\Delta'\vdash^{\uparrow\downarrow}M\Leftarrow C$, where $\Delta'\vdash^{sub}\Delta$.
3. Checking and synthesis derivations erase to $\Delta\vdash^{nd}M:A$.

Context realization is
$$\frac{}{\cdot\vdash^{sub}\cdot}\qquad
\frac{\Delta'_1\vdash^{sub}\Delta\quad\Delta'_2\vdash M\Rightarrow A}{\Delta'_1,\Delta'_2\vdash^{sub}\Delta,A}.$$
$\Delta$ contains sequent formulas; $\Delta'$ is an ND variable context; $M$ realizes a formula.

The relation $\Delta'\vdash^{sub}\Delta$ should be read as a context realization or substitution judgment: every formula occurrence on the right is represented by a term on the left that synthesizes that formula, and the realizing terms divide the resources of $\Delta'$. It is not ordinary subset notation. The primes distinguish two kinds of antecedent, not two nearly equal lists. This extra invariant lets the reverse proof proceed even when a sequent left rule decomposes a formula represented in ND by a compound neutral term rather than a bare variable.

For ND tensor elimination, induction gives $\Delta_1\vdash^{seq}A\otimes B$ and $\Delta_2,A,B\vdash^{seq}C$. Apply $\otimes L$ to the latter, then admissible cut. Implication elimination similarly uses $\multimap L$, identity, and cut.

## 5. How to use/read it
Map ND introductions to right rules. Map eliminations through left rules plus cut. In reverse, carry context realizers; a left rule consumes a term synthesizing its principal formula. Erasure uses simultaneous induction because checking and synthesis refer to each other.

## 6. Worked example
Translate $f:A\multimap B,a:A\vdash fa:B$. Sequent identity gives $B\vdash B$. With $a:A\vdash A$, $\multimap L$ derives $a:A,A\multimap B\vdash B$. Cut in the derivation realizing $f:A\multimap B$ to obtain $f:A\multimap B,a:A\vdash B$. Application is not translated by one lone rule.

In the reverse direction, suppose a context realizer supplies $F\Rightarrow A\multimap B$ and another translated premise supplies $N\Leftarrow A$. Bidirectional implication elimination builds $FN\Rightarrow B$. That synthesized term can extend the realizer used to translate the remaining sequent premise. This is why synthesis is crucial: a sequent antecedent is available for further left-focused use, so its ND representative must reveal its outer type algorithmically.

## 7. Non-example or boundary case
The naive reverse theorem “$\Delta\vdash^{seq}C$ implies $\Delta\vdash M\Leftarrow C$” gets stuck at $\otimes L$. An antecedent $A\otimes B$ is a formula, not automatically a named term synthesizing it. Context realization supplies that evidence.

The correspondence is about derivability, not literal proof identity, proof size, or reduction order. Admissible cuts inserted by the ND-to-sequent translation may later normalize away, and annotations inserted by the reverse translation may erase in ordinary ND. Two translations can therefore agree on end judgments while producing structurally different derivations. Establishing a tighter operational correspondence would require additional simulation theorems beyond the three claims stated here.

## 8. Key consequences
- The systems agree on intended provability.
- Cut explains elimination translations.
- Identity supports implication elimination translation.
- Context realization makes reverse translation compositional.
- Bidirectional modes erase to ordinary ND.

## 9. Relations to nearby concepts
[Harmony in Natural Deduction](<Harmony in Natural Deduction.md>) is internal; translation is external validation. [Bidirectional Type Checking](<Bidirectional Type Checking.md>) is not sequent calculus despite its right/left heuristic. [Linear Natural Deduction](<Linear Natural Deduction.md>) supplies terms absent from bare sequents.

## 10. Common mistakes
- Claiming one-to-one rule correspondence without cut.
- Omitting context realization.
- Confusing hypothesis with sequent identity.
- Treating cut as object syntax.
- Proving checking erasure alone.
- Assuming translation preserves proof shape.

## 11. What to remember
- Introductions map to right rules.
- Eliminations need left rules plus cut.
- Reverse translation needs synthesizing realizers.
- Modes erase simultaneously.
- Equivalent provability does not mean identical derivations.

## 12. Source trail
Sophia Roshal, Lecture 23, §5.2, printed pages L23.6–L23.10, PDF pages 242–246. See [Lecture 23](<../Lectures/Lecture 23 - Linear Natural Deduction.md>).

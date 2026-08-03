---
title: Forward Proof Search and the Inverse Method
aliases:
  - inverse method
  - forward saturation
tags:
  - proof-search
  - inverse-method
  - focusing
source_lectures:
  - 18
prerequisites:
  - "[Partial focusing](Partial-Focusing.md)"
related:
  - "[Resource regimes](../Comparisons/Resource-Regimes.md)"
  - "[CLF and monadic concurrency](CLF-and-Monadic-Concurrency.md)"
---

# Forward Proof Search and the Inverse Method

## One-sentence definition

The inverse method is a goal-specialized forward proof-search procedure that starts from atomic identity sequents, derives only side-correct subformulas of the goal, and saturates until it reaches the goal or no new sequents remain.

## Why the concept is needed

Backward sequent search repeatedly chooses a rule from the goal and can revisit similar failures across branches. Naive forward search avoids that shape of backtracking but generates infinitely many irrelevant theorems. The inverse method combines the benefits: the cut-free subformula property restricts facts, labels fix which side each occurrence may inhabit, and database saturation shares derived consequences.

## Intuitive model

**Intuition.** Instead of searching backward through a maze from the exit, build a flood from all admissible entrances—but first wall off every corridor that cannot occur in a cut-free route to this particular exit. Saturation records every reached chamber once.

## Formal core

Given goal $G=\Gamma\vdash C$:

1. Restrict identity to atoms and rely on admissible general identity and cut.
2. Label every subformula occurrence by side, such as $L_i$ or $R_j$; an implication antecedent changes side.
3. Specialize each cut-free rule to these labels.
4. Add logic-specific resource handling.
5. Repeatedly apply specialized rules to known sequents.

For example, if $R_0=R_1\mathbin{\&}R_2$ and $R_1=A_L\multimap B_R$, generate

$$
\frac{\Delta\vdash R_1\quad\Delta\vdash R_2}{\Delta\vdash R_0}
\qquad
\frac{\Delta,A_L\vdash B_R}{\Delta\vdash R_1}.
$$

The identical $\Delta$ in the additive rule is essential. With focusing, facts are stable sequents: antecedents contain negative formulas or suspended positive atoms $\langle P^+\rangle$, and succedents contain positive formulas or suspended negative atoms. One generated big-step rule represents a whole focused phase.

## How to use/read it

Create a database seeded by eligible atomic identities. Apply every rule whose premises are present, respecting multiset splitting and equality. Record provenance so a derived goal reconstructs a proof. If the finite relevant space saturates without the goal, unprovability follows for that system; in an undecidable fragment, non-saturation may continue forever.

## Worked example

Test $A\multimap(B\mathbin{\&}C)\vdash(A\multimap B)\mathbin{\&}(A\multimap C)$.

1. Name $L_0=A\multimap L_1$, $L_1=B\mathbin{\&}C$, $R_1=A\multimap B$, $R_2=A\multimap C$, $R_0=R_1\mathbin{\&}R_2$.
2. Seed $A\vdash A$, $B\vdash B$, $C\vdash C$.
3. Specialized left projections derive $L_1\vdash B$ and $L_1\vdash C$.
4. Combine $A\vdash A$ with each fact through the specialized $L_0$ rule: $A,L_0\vdash B$ and $A,L_0\vdash C$.
5. Specialized implication-right rules give $L_0\vdash R_1$ and $L_0\vdash R_2$.
6. The additive right rule reuses the same antecedent and yields $L_0\vdash R_0$, the goal.

Every formula is a named occurrence from the goal; no irrelevant $A\multimap A$ is generated.

## Non-example or boundary case

For $A\multimap(B\otimes C)\vdash(A\multimap B)\otimes(A\multimap C)$, multiplicative right introduction must split resources. The identities alone enable no useful specialized inference, so saturation stops without the goal. Reusing the same $A$ for both output components would be an illicit contraction.

## Key consequences

Forward saturation provides shared lemmas automatically. Focusing reduces administrative facts by moving only between stable sequents. Linearity can prune any fact whose multiplicity exceeds the goal's available occurrences. Affine and structural systems require subsumption rather than plain syntactic equality.

## Relations to nearby concepts

[Resource regimes](../Comparisons/Resource-Regimes.md) details contraction, weakening, and subsumption changes. [Partial focusing](Partial-Focusing.md) also uses phases, but to determine observable value structure rather than theorem-prover saturation. [CLF and monadic concurrency](CLF-and-Monadic-Concurrency.md) turns linear forward rules into concurrent computation.

## Common mistakes

- Running unrestricted forward sequent rules instead of goal-specialized ones.
- Ignoring side information for implication subformulas.
- Combining additive premises with different contexts.
- Declaring failure merely because an undecidable search has not terminated.
- Treating database inference as linear; the prover's database is structural even when facts describe linear sequents.

## What to remember

- Start at atomic identities and move forward.
- Specialize rules to side-labeled goal subformulas.
- Saturation succeeds on the goal and fails only when it genuinely closes.
- Focusing packages many small rules into stable-to-stable steps.
- Resource regimes change redundancy and matching.

## Source trail

Lecture 18, §§1–2, printed pp. L18.1–L18.6, PDF pp. 187–192; focused generation is §3, printed pp. L18.6–L18.10, PDF pp. 192–196; the procedure summary is printed p. L18.10, PDF p. 196.


---
title: "Lecture 12 - Focusing"
lecture: 12
date: 2023-10-05
pdf_pages: "132-141"
printed_pages: "L12.1-L12.10"
tags:
  - lecture
  - focusing
  - polarity
  - cut-elimination
  - adjoint-logic
prerequisites:
  - "Lecture 11 - Adjoint Logic"
  - "Cut elimination"
  - "Positive and negative polarity"
---

# Lecture 12 - Focusing

## 1. Why this lecture exists

Ordinary sequent calculus is intentionally permissive: many rules may be applicable at once, and even sound proof search can wander among irrelevant choices. This lecture addresses that problem in two stages. First, it repairs the cut-elimination argument for adjoint logic when explicit contraction duplicates the cut formula. Second, it turns polarity into a proof-search discipline. Invertible rules are applied eagerly during **inversion**; after inversion is exhausted, one proposition is selected and its noninvertible rules are **chained** during a focused phase.

The result is not merely a faster implementation trick. Focusing exposes a normal form for proofs, explains why negative and positive propositions behave differently, and foreshadows the message-oriented calculi of Lectures 14 and 15. The qualification is important: the focused rules presented here are correct only when every mode is linear. Structural focusing needs further bookkeeping for weakening and contraction.

## 2. Learning objectives

After this lecture, you should be able to:

1. explain why the naive contraction case does not justify cut admissibility;
2. state multicut and calculate the allowed multiplicities $\mu(m)$ from the structural permissions $\sigma(m)$;
3. distinguish right inversion, left inversion, choice, right focus, and left focus;
4. explain the role of the ordered inversion context $\Omega$, the stable context $\Delta^-$, suspended atoms, and square-bracket focus;
5. trace a focused proof search and identify where genuine choices remain; and
6. state precisely why the chaining calculus in this lecture is restricted to linear modes.

## 3. Dependency map

The development has the following dependency structure:

$$
\text{adjoint modes and structural permissions}
\longrightarrow \text{multicut}
\longrightarrow \text{cut admissibility strategy},
$$

$$
\text{polarity} + \text{invertibility}
\longrightarrow \text{forced inversion}
\longrightarrow \text{choice}
\longrightarrow \text{focused chaining}.
$$

The first line depends on the mode preorder and monotonicity of structural permissions from [adjoint logic](<../Concepts/Adjoint Logic.md>). The second depends on the distinction between [positive and negative polarity](<../Comparisons/Positive vs Negative Polarity.md>) and culminates in [focusing](<../Concepts/Focusing.md>). Together they connect proof normalization to proof construction, but they are different results: multicut supports a metatheorem about elimination; focusing restricts the shape of derivations used during search.

## 4. Section-by-section reconstruction

### 1 Introduction

The lecture revisits cut elimination because the earlier ordered proof does not automatically survive explicit weakening and contraction. It then introduces Andreoli-style focusing. In Andreoli's terminology, negative connectives are asynchronous and positive connectives are synchronous: the former invite deterministic inversion, while the latter require a committed choice. The presentation adapts this idea to adjoint logic but deliberately avoids full polarization, because the same up- and downshifts already carry mode information.

Two aims should not be conflated. Cut elimination studies how a derivation containing cut can be transformed. Focusing studies how to construct a derivation while avoiding irrelevant nondeterminism. Both use polarity, but at different metatheoretic levels.

### 2 Cut Elimination Revisited

An adjoint sequent has mode-indexed propositions. Write $A_m$ for proposition $A$ at mode $m$, $C_r$ for a conclusion at mode $r$, and $\Delta \ge m$ when every antecedent in $\Delta$ lies at a mode at least $m$. The ordinary admissible cut is intended to be

$$
\frac{\Delta \ge m \ge r \qquad \Delta \vdash A_m \qquad
      \Delta',A_m \vdash C_r}
     {\Delta,\Delta' \vdash C_r}
\;\mathsf{cut}_{A_m}.
$$

Suppose the last rule in the right premise contracts two copies of $A_m$ into one. A tempting reduction cuts the same derivation of $A_m$ into both copies. That produces $\Delta,\Delta,\Delta' \vdash C_r$. Monotonicity repairs the duplicated context: if contraction $\mathsf C$ is permitted at $m$ and each antecedent mode $\ell$ satisfies $\ell\ge m$, then $\mathsf C\in\sigma(\ell)$, so every formula in $\Delta$ may also be contracted.

This repairs the conclusion but not the induction. The first recursive cut has a smaller right derivation, but its result may be larger than the original right premise. The second cut has the same cut formula and the same left premise, so the usual lexicographic measure is no longer known to decrease. A plausible local rewrite is therefore not yet a proof of admissibility.

The repair is to strengthen the theorem. Let $(A)^n$ mean $n$ copies of $A$, and define the allowed multiplicities at a mode by

$$
\begin{array}{c|c}
\sigma(m) & \mu(m)\\ \hline
\varnothing & \{1\}\\
\{\mathsf W\} & \{0,1\}\\
\{\mathsf C\} & \{1,2,3,\ldots\}\\
\{\mathsf W,\mathsf C\} & \{0,1,2,3,\ldots\}.
\end{array}
$$

Here $\sigma(m)$ records whether weakening $\mathsf W$ and contraction $\mathsf C$ are permitted. The strengthened rule is

$$
\frac{\Delta\ge m\ge r \qquad n\in\mu(m) \qquad
      \Delta\vdash A_m \qquad \Delta',(A_m)^n\vdash C_r}
     {\Delta,\Delta'\vdash C_r}
\;\mathsf{multicut}_{A_m}.
$$

Ordinary cut is $n=1$. Weakening is absorbed by $n=0$, and contraction by $n=2$. In a contraction case with $n+1$ copies below the last rule and $n+2$ above it, the induction makes one multicut eliminating all $n+2$ copies at once. The condition $n+2\in\mu(m)$ follows from $\mathsf C\in\sigma(m)$.

Principal cases become slightly more expensive. If a negative conjunction $A_m\mathbin{\&}B_m$ (written $A_m\mathbin N B_m$ in the extracted source) is introduced on the right and one of $n+1$ copies is decomposed on the left, the reduction first performs a multicut on the remaining $n$ compound copies and then a cut on the selected component. The former decreases the right derivation; the latter decreases the cut formula. This is exactly the lexicographic descent the naive contraction rewrite lacked.

For $n=0$, the proof of $A_m$ is unused. Since $0\in\mu(m)$ implies weakening at $m$, and $\Delta\ge m$ propagates weakening permission to every antecedent in $\Delta$, those antecedents can be added to the existing derivation by repeated weakening.

### 3 Inversion

Inversion forces every available invertible rule. The grammar separates negative propositions $A_m^-$ from positive propositions $A_m^+$. Representative negatives are atoms of chosen negative polarity, implication $A_m\to B_m$, negative conjunction $A_m\mathbin{\&}B_m$, $\top$, and upshift $\uparrow_k^m A_k^+$. Representative positives are positive atoms, product $A_m\times B_m$, unit $1$, sum $A_m+B_m$, $0$, and downshift $\downarrow_m^\ell A_\ell^-$. The superscripts $+$ and $-$ indicate polarity, not truth values.

Right inversion is written

$$
\Delta^-;\Omega \xrightarrow{\mathrm{IR}} A_m,
$$

where $\Omega$ is an ordered accumulator and $\Delta^-$ is a stable multiset containing only propositions with no invertible left rule: negative propositions and suspended positive atoms. Negative right rules are applied eagerly. For example,

$$
\frac{\Delta^-;\Omega\xrightarrow{\mathrm{IR}}A_m
      \qquad
      \Delta^-;\Omega\xrightarrow{\mathrm{IR}}B_m}
     {\Delta^-;\Omega\xrightarrow{\mathrm{IR}}A_m\mathbin{\&}B_m}
\;\&R,
$$

and implication right places its domain at the front of $\Omega$:

$$
\frac{\Delta^-;A_m\,\Omega\xrightarrow{\mathrm{IR}}B_m}
     {\Delta^-;\Omega\xrightarrow{\mathrm{IR}}A_m\to B_m}
\;\to R.
$$

When the succedent is positive, or is a negative atom that cannot be decomposed, right inversion hands control to left inversion. A negative atom is first written $\langle P_m^-\rangle$. These angle brackets are a judgmental suspension marker, not a connective or modal operator.

Left inversion, written $\Delta^-;\Omega\xrightarrow{\mathrm{IL}}C_r^+$, consumes the leftmost element of $\Omega$. Positive products, units, sums, and zero have invertible left rules. When the leftmost formula is negative, it moves to $\Delta^-$. A positive atom similarly moves as the suspension $\langle P_m^+\rangle$. The ordered $\Omega$ makes this sweep deterministic: formulas are processed from one end rather than chosen from an exchangeable context.

When $\Omega$ is empty, inversion has reached the choice judgment

$$
\Delta^-\xrightarrow{\mathrm C} C_r^+.
$$

At that point no invertible rule remains. Any further progress must select a noninvertible action.

### 4 Chaining

Choice selects either the positive succedent for right focus or one negative antecedent for left focus:

$$
\Delta^-\xrightarrow{\mathrm{FR}}[C_m^+]
\qquad\text{or}\qquad
\Delta^-;[A_m^-]\xrightarrow{\mathrm{FL}}C_r^+.
$$

Square brackets identify the unique focused formula. During right focus, noninvertible positive right rules retain focus on the chosen subformula. Product splits the linear context, sum chooses one injection, downshift crosses a permitted mode boundary, and $0$ has no right rule. Encountering a negative subformula releases focus back to right inversion. A suspended positive atom closes by atomic identity.

During left focus, the principal negative antecedent remains focused. Implication left proves the domain in right focus and continues with the codomain in left focus; negative conjunction chooses one projection; upshift crosses modes; and $\top$ has no left rule. Encountering a positive subformula releases focus to left inversion. A focused negative atom closes against its suspended occurrence.

This uninterrupted run of noninvertible rules is **chaining**. Inversion plus chaining is focusing. It greatly reduces proof-search branching because a choice of principal formula is followed to its polarity boundary rather than reconsidered after every rule.

Boundary condition: all modes in these chaining rules must be linear. With weakening or contraction, context distribution and duplication affect several focus transitions, not merely the rule that selects a left focus. The lecture explicitly retracts the broader claim made orally and postpones structural focusing.

### 5 A Simple Example

The source analyzes composition:

$$
(P_m\to Q_m)\to((Q_m\to R_m)\to(P_m\to R_m)),
$$

with $P_m,Q_m,R_m$ chosen positive. Three invertible $\to R$ steps place $P_m$, $Q_m\to R_m$, and $P_m\to Q_m$ in the inversion accumulator and leave $R_m$ as the positive goal. Left inversion suspends $P_m$ and stabilizes the two negative implications. At choice, focusing on $R_m$ fails because there is no suspended $R_m$; focusing on $Q_m\to R_m$ fails initially because $Q_m$ is unavailable. Thus $P_m\to Q_m$ is forced. It consumes suspended $P_m$ and produces suspended $Q_m$. The only useful next focus is $Q_m\to R_m$, after which atomic identity closes $R_m$.

The notation is elaborate because it records every phase boundary, but the important fact is semantic: modulo shallow failed choices, the focused discipline exposes the unique composition proof.

## 5. Formal core

### Judgments and metavariables

- $m,k,\ell,r$ are modes; $\ell\ge m$ means mode $\ell$ can supply a proposition required at mode $m$.
- $\sigma(m)\subseteq\{\mathsf W,\mathsf C\}$ is the set of structural rules permitted at $m$.
- $\mu(m)$ is the set of legal numbers of uses of a proposition at mode $m$.
- $A_m,B_m,C_r$ are mode-indexed propositions; polarity decorations $A_m^+$ and $A_m^-$ classify proof-search behavior.
- $\Delta,\Delta'$ are exchangeable antecedent contexts. $\Delta\ge m$ means every formula in $\Delta$ has a mode above $m$.
- $\Omega$ is an ordered inversion context. Its order is an administrative device for deterministic left inversion, not an ordered-logic resource discipline.
- $\Delta^-$ is a stable context of negative propositions and suspended positive atoms.
- $D,E,F$ denote derivations; $E'<E$ means that $E'$ is a proper subderivation used in the induction measure.
- $\langle P\rangle$ suspends an atom at a phase boundary. $[A]$ marks the one proposition currently in focus.

### Central admissibility statement

The multicut theorem strengthens cut enough to absorb all allowed multiplicities:

$$
\Delta\ge m\ge r, n\in\mu(m),\
\Delta\vdash A_m,\
\Delta',(A_m)^n\vdash C_r
\quad\Longrightarrow\quad
\Delta,\Delta'\vdash C_r.
$$

It is a metatheorem, not an object-language rule to be used freely before admissibility is proved. Its proof uses lexicographic induction, first on the structure of $A_m$, then on the relevant derivations.

### Phase invariant

Focusing maintains this invariant:

1. right inversion decomposes only negative succedents;
2. left inversion decomposes only positive formulas in $\Omega$;
3. choice occurs only when $\Omega$ is empty and the sequent is stable;
4. exactly one formula is focused during chaining; and
5. focus ends only at an invertible subformula or an atomic identity boundary.

## 6. Operational/computational reading

Read inversion as deterministic protocol exposure. A negative offered type determines what the provider must be ready to receive; a positive assumption determines what its client can safely inspect. No implementation choice is encoded by these invertible steps.

Read focus as a committed interaction. Right focus constructs a positive value or sends positive information. Left focus consumes a negative service by selecting how to use it. Staying focused corresponds to completing one coherent burst of protocol actions before returning to administrative decomposition.

This is an interpretation, not an equality between proof search and execution. Focusing restricts which proofs are constructed and may reduce program expressiveness if imposed directly as a term language. Cut reduction, by contrast, describes interaction among already constructed proofs or processes.

## 7. Worked derivation or trace in original notation and prose

Consider the original proposition

$$
(A_m^+\to B_m^+)\to(A_m^+\to B_m^+).
$$

All modes are linear. Begin in right inversion:

$$
\cdot;\cdot\xrightarrow{\mathrm{IR}}
(A_m^+\to B_m^+)\to(A_m^+\to B_m^+).
$$

Two applications of $\to R$ produce

$$
\cdot;A_m^+\,(A_m^+\to B_m^+)
\xrightarrow{\mathrm{IR}} B_m^+.
$$

The positive succedent ends right inversion. Left inversion processes the accumulator from the left. It suspends the atom and moves the negative implication to the stable context:

$$
\langle A_m^+\rangle, A_m^+\to B_m^+
\xrightarrow{\mathrm C}B_m^+.
$$

Right focus on $B_m^+$ cannot close: no $\langle B_m^+\rangle$ exists. The useful choice is left focus on $A_m^+\to B_m^+$:

$$
\langle A_m^+\rangle;
[A_m^+\to B_m^+]
\xrightarrow{\mathrm{FL}}B_m^+.
$$

The focused $\to L$ rule has two obligations. Its domain is solved in right focus by atomic identity against $\langle A_m^+\rangle$. Its codomain remains focused on the left as $[B_m^+]$, which releases to left inversion and suspends $B_m^+$. Choice is reached again:

$$
\langle B_m^+\rangle\xrightarrow{\mathrm C}B_m^+.
$$

Now right focus on $[B_m^+]$ closes by $\mathsf{id}^+$. The trace shows both sources of determinism: invertible rules were forced, and once the implication was selected its application chained through to the polarity boundary.

Boundary case: replace the outer target by $(A_m^+\to B_m^+)\to A_m^+$. After inversion, there is no suspended $A_m^+$ and using the implication requires one. Search correctly fails; focusing does not manufacture an unavailable resource.

## 8. Conceptual synthesis

The lecture's two halves share a methodological theme: strengthen or refine the judgment until the desired invariant becomes explicit. Multicut strengthens cut so contraction and weakening are reflected in the statement being proved. Focusing refines the sequent judgment into phases so invertibility and commitment are reflected in the derivation itself.

Both refinements eliminate hidden assumptions. The naive cut proof hid a nondecreasing recursive call; the unfocused calculus hid the difference between administrative and genuine choices. A rigorous proof theory makes both visible.

## 9. Common confusions and failure modes

- **“The duplicated context can be contracted, so the naive cut proof works.”** Contracting $\Delta,\Delta$ repairs the conclusion but does not make the second induction call smaller.
- **“Multicut is just repeated ordinary cut.”** Repetition is precisely what breaks the induction. Multicut must be the strengthened induction hypothesis.
- **“$n=0$ means no premise is needed.”** The derivation $\Delta\vdash A_m$ remains present in the general statement, but the reduction does not use it; weakening justifies adding $\Delta$.
- **“Negative means false.”** Polarity classifies rule orientation and invertibility, not semantic truth.
- **“$\langle P\rangle$ is a modality.”** It is a judgmental suspension marker for an atom.
- **“$\Omega$ makes the underlying logic ordered.”** Here $\Omega$ is an ordered work list used to make inversion deterministic; the focused fragment discussed is otherwise linear.
- **“Focusing removes all nondeterminism.”** It removes permutations of invertible rules and chains a commitment. Selection of a focus, context splits, and sum branches may still require search.
- **“The displayed focusing rules already handle structural modes.”** They do not. The lecture explicitly restricts chaining to linear modes.
- **“Admissible and derivable are interchangeable.”** Multicut is proved admissible as a metatheorem; it is not automatically a primitive rule of the object system.

## 10. Self-test questions with concise answers

1. **Why does contraction threaten the ordinary cut induction?**  
   Sequentially cutting two copies can make the intermediate right derivation larger while leaving the cut formula unchanged.

2. **What does $0\in\mu(m)$ tell you?**  
   Weakening is permitted at mode $m$.

3. **What does $2\in\mu(m)$ tell you?**  
   Contraction is permitted at mode $m$.

4. **When is the choice judgment reached?**  
   When right inversion has handed off to left inversion and the ordered context $\Omega$ has been exhausted.

5. **What do square brackets mean?**  
   They mark the unique proposition being decomposed in a focused phase.

6. **Why is implication right invertible?**  
   Proving $A\to B$ can safely proceed by assuming $A$ and proving $B$; this does not discard an alternative proof branch.

7. **Why is sum right noninvertible?**  
   A proof must choose which injection to construct.

8. **What ends a focused phase?**  
   Reaching a subformula whose rule is invertible, or closing at an atomic identity.

9. **What is the key restriction on Section 4?**  
   Every mode must be linear, with neither weakening nor contraction.

## 11. Related concept pages

- [Focusing](<../Concepts/Focusing.md>)
- [Inversion, chaining, and proof phases](<../Concepts/Inversion, Chaining, and Proof Phases.md>)
- [Positive vs negative polarity](<../Comparisons/Positive vs Negative Polarity.md>)
- [Multicut and cut elimination across modes](<../Concepts/Cut Elimination Across Modes.md>)
- [Adjoint logic](<../Concepts/Adjoint Logic.md>)
- [Identity and cut admissibility](<../Concepts/Identity and Cut Admissibility.md>)
- [Forward proof search and the inverse method](<../Concepts/Forward-Proof-Search-and-Inverse-Method.md>)
- [Additive and multiplicative connectives](<../Concepts/Additive and Multiplicative Connectives.md>)
- [Cut reduction as process execution](<../Concepts/Cut Reduction as Process Execution.md>)

## 12. Source trail

- Frank Pfenning, *Focusing*, 15-836 Substructural Logics, Lecture 12, October 5, 2023.
- Numbered sections covered exactly: §1 **Introduction**; §2 **Cut Elimination Revisited**; §3 **Inversion**; §4 **Chaining**; §5 **A Simple Example**.
- Printed pages: L12.1-L12.10.
- PDF pages: 132-141.
- This guide reconstructs the formal development in original prose and uses new examples rather than reproducing the source's extended derivations.

## 13. Previous/next navigation

- Previous: [Lecture 11 - Adjoint Logic](<Lecture 11 - Adjoint Logic.md>)
- Next: [Lecture 13 - Quantifiers](<Lecture 13 - Quantifiers.md>)

---
title: "Lecture 09 - Validity"
lecture: 9
date: 2023-09-26
pdf_pages: "102-112"
printed_pages: "L9.1-L9.11"
tags:
  - lecture
  - linear-logic
  - validity
  - exponential
  - proof-theory
prerequisites:
  - linear sequent calculus
  - structural rules
  - multiplicative and additive connectives
  - cut and identity
---

# Lecture 09 - Validity

## 1. Why this lecture exists

Pure linear logic treats every assumption as a resource that must be used exactly once. Ordinary mathematical hypotheses and reusable programs do not behave that way: once established without consuming a resource, they may be used zero, one, or many times. The exponential $!A$ is meant to mark precisely this reusable status, but simply listing special rules for $!$ hides why those rules have their shape.

This lecture reconstructs $!A$ from a prior distinction between two judgments: ephemeral truth and context-independent validity. A proof of $A$ that consumes no linear assumptions can be reproduced whenever needed; a valid assumption therefore belongs in a structural context admitting weakening and contraction. Internalizing that judgment as a proposition gives the exponential. This perspective explains the crucial empty-linear-context side condition on $!R$, supports translations between structural and linear logic, and exposes the remaining proof-theoretic awkwardness that motivates [Lecture 10](Lecture%2010%20-%20A%20Mixed%20Linear-Nonlinear%20Logic.md).

## 2. Learning objectives

After this lecture, a reader should be able to:

- distinguish $A\;\mathsf{true}$ from $A\;\mathsf{valid}$;
- read the two-zone judgment $\Gamma;\Delta\vdash A$ and explain which rules may inspect each zone;
- derive the rules for $!$ from the rules for validity;
- explain why promotion requires an empty linear context;
- prove basic exponential laws and diagnose failed distributivity claims;
- state the call-by-value translation of intuitionistic logic into linear logic;
- distinguish derivable identity/cut rules from their admissibility metatheorems.

## 3. Dependency map

The construction depends on [Linear versus structural persistence](../Comparisons/Linear%20vs%20Structural%20Persistence.md) and the resource-sensitive meaning of [Linear inference](../Concepts/Linear%20Inference.md). It uses [Identity and cut admissibility](../Concepts/Identity%20and%20Cut%20Admissibility.md) to explain hypothetical reasoning, then adds [Validity](../Concepts/Validity.md) as a second judgment. The relationship between the one-zone and dyadic exponentials is isolated in [Girard vs Andreoli exponentials](../Comparisons/Girard%20vs%20Andreoli%20Exponentials.md). The resulting system supports an embedding of intuitionistic logic in linear logic, while its polarity problem leads directly to [Shifts between logics](../Concepts/Shifts%20Between%20Logics.md).

## 4. Section-by-section reconstruction

### 1. Introduction

Earlier lectures kept ordered, linear, and structural assumptions sharply separated. Recursion offered programming expressiveness, but it is not a satisfactory logical explanation of unrestricted reuse. The modality $!A$ had already appeared as a formula allowed to weaken and contract. The point here is to derive that behavior from a general notion of validity rather than treat $!$ as an isolated device.

The construction is not peculiar to linear logic. Applied over a structural base it resembles the modal proposition $\Box A$: $A$ holds necessarily, or throughout all admissible states/worlds. That generality is the first sign that validity is judgmental infrastructure rather than merely another connective.

### 2. Girard's Exponential

In the one-zone presentation, $!A$ is governed by promotion and dereliction together with structural rules restricted to banged assumptions:

$$
\frac{!\Delta\vdash A}{!\Delta\vdash !A}\;!R
\qquad
\frac{\Delta,A\vdash C}{\Delta,!A\vdash C}\;!L
$$

$$
\frac{\Delta,!A,!A\vdash C}{\Delta,!A\vdash C}\;\mathsf{contract}
\qquad
\frac{\Delta\vdash C}{\Delta,!A\vdash C}\;\mathsf{weaken}.
$$

Here $A,C$ are propositions; $\Delta$ is a multiset of linear antecedents; and $!\Delta$ means every member has the form $!B$. Read bottom-up, $!L$ exposes one usable $A$; contraction requests two uses of $!A$; weakening permits none. The $!R$ premise may depend only on already reusable assumptions. It therefore certifies that producing $A$ needs no ephemeral input.

### 3. Andreoli's Exponential

The dyadic presentation makes the explanation explicit:

$$
\Gamma;\Delta\vdash A\;\mathsf{true}.
$$

$\Gamma$ is a set-like structural context of valid assumptions: exchange, weakening, and contraction are implicit. $\Delta$ is a multiset of ephemeral linear assumptions: every member must be consumed exactly once. The semicolon is a boundary, not multiset union. Propositional rules act on the succedent and on $\Delta$; they do not directly decompose formulas stored in $\Gamma$.

Validity is a separate judgment, $\Gamma\vdash A\;\mathsf{valid}$. Its two judgment-defining rules are

$$
\frac{\Gamma;\cdot\vdash A\;\mathsf{true}}
     {\Gamma\vdash A\;\mathsf{valid}}\;\mathsf{valid}_R
\qquad
\frac{\Gamma,A\;\mathsf{valid};\Delta,A\;\mathsf{true}\vdash C\;\mathsf{true}}
     {\Gamma,A\;\mathsf{valid};\Delta\vdash C\;\mathsf{true}}\;\mathsf{valid}_L.
$$

$\mathsf{valid}_R$ says that a resource-free proof is stable enough to count as valid. Read bottom-up, $\mathsf{valid}_L$ copies a valid assumption into the linear zone for one particular use; because the original remains in $\Gamma$, the operation may be repeated.

Validity is internalized by $!$:

$$
\frac{\Gamma\vdash A\;\mathsf{valid}}{\Gamma;\cdot\vdash !A\;\mathsf{true}}\;!R
\qquad
\frac{\Gamma,A\;\mathsf{valid};\Delta\vdash C\;\mathsf{true}}
     {\Gamma;\Delta,!A\vdash C\;\mathsf{true}}\;!L.
$$

Composing $\mathsf{valid}_R$ with $!R$ gives promotion:

$$
\frac{\Gamma;\cdot\vdash A}{\Gamma;\cdot\vdash !A}\;!R'.
$$

The empty $\Delta$ is essential. If promotion could ignore a nonempty linear context, then from $A$ one could prove $!A$, use $!A$ twice, and derive $A\otimes A$; one could also throw $A$ away to derive $1$. Thus contraction and weakening would become admissible for every linear assumption and linearity would collapse.

Identity and ordinary linear cut retain their familiar shapes:

$$
\frac{}{\Gamma;A\vdash A}\;\mathsf{id}
\qquad
\frac{\Gamma;\Delta\vdash A\qquad\Gamma;\Delta' ,A\vdash C}
     {\Gamma;\Delta,\Delta'\vdash C}\;\mathsf{cut}.
$$

The repeated $\Gamma$ emphasizes that valid assumptions are shared parametrically, while the linear contexts are partitioned.

### 4. Examples

The modality validates the familiar normal modal laws

$$
\vdash !(A\multimap B)\multimap(!A\multimap !B),\qquad
\vdash !A\multimap A,\qquad
\vdash !A\multimap !!A,
$$

but not $P\multimap !P$. The failed last formula is exactly the forbidden inference from ephemeral truth to validity.

To prove normality, move the two banged assumptions to the valid context with $!L$, obtain linear instances of $A\multimap B$ and $A$ using $\mathsf{valid}_L$, apply $\multimap L$, and promote the resulting $B$. The administrative movement is correct but cumbersome: formulas in $\Gamma$ cannot be decomposed until copied into $\Delta$.

Tensor does **not** satisfy

$$
!(A\otimes B)\multimap(!A\otimes !B).
$$

A reusable package always supplies $A$ and $B$ together. It does not produce two independent services, one supplying arbitrarily many $A$s and the other arbitrarily many $B$s. Proof search exposes the obstruction: after copying and decomposing $A\otimes B$, both linear resources appear together, while promotion of either component requires the linear zone to be empty.

By contrast, additive conjunction (written $A\mathbin{\&}B$ here; rendered as $A\mathbin{N}B$ in the extracted notes) satisfies

$$
!(A\mathbin{\&}B)\dashv\vdash !A\otimes !B.
$$

Each reuse of $A\mathbin{\&}B$ permits the client to select either projection, so separate reuses can supply $A$ and $B$. In the reverse direction, reusable $A$ and reusable $B$ can answer either branch requested by $\mathbin{\&}R$. This contrast is a concrete instance of [Additive and multiplicative connectives](../Concepts/Additive%20and%20Multiplicative%20Connectives.md).

### 5. Translation from Structural into Linear Logic

There are call-by-name and call-by-value embeddings, named for their functional operational readings. The lecture develops Girard's call-by-value translation $(A)^\vee$. If $\Gamma\vdash A$ in intuitionistic logic, then

$$
\Gamma^\vee;\cdot\vdash A^\vee
$$

in the dyadic linear system. Each translated intuitionistic assumption is stored structurally. The formula translation is

$$
\begin{aligned}
(A\supset B)^\vee &= !A^\vee\multimap !B^\vee,&
(A\land B)^\vee &= !A^\vee\otimes !B^\vee,\\
\top^\vee &= 1,&
(A\lor B)^\vee &= !A^\vee\oplus !B^\vee,\\
\bot^\vee &= 0,&
P^\vee &= P.
\end{aligned}
$$

$\supset,\land,\lor,\top,\bot$ are structural connectives; $\multimap,\otimes,\oplus,1,0$ are their linear targets; $P$ is atomic. Prefixing translated immediate subformulas with $!$ allows the target to reproduce the source's implicit weakening and contraction.

The forgetful translation $(A)^\wedge$ maps linear connectives to structural ones and erases exponentials:

$$
\begin{aligned}
(A\multimap B)^\wedge &= A^\wedge\supset B^\wedge,&
(A\otimes B)^\wedge &= A^\wedge\land B^\wedge,\\
(A\mathbin{\&}B)^\wedge &= A^\wedge\land B^\wedge,&
(A\oplus B)^\wedge &= A^\wedge\lor B^\wedge,\\
1^\wedge=\top^\wedge&=\top,&0^\wedge&=\bot,\\
(!A)^\wedge&=A^\wedge,&P^\wedge&=P.
\end{aligned}
$$

The correctness theorem has two directions:

1. If $\Gamma\vdash A$ structurally, then $\Gamma^\vee;\cdot\vdash A^\vee$ linearly.
2. If $\Gamma;\Delta\vdash A$ linearly, then $\Gamma^\wedge,\Delta^\wedge\vdash A^\wedge$ structurally.

Both are metatheorems proved by induction on derivations. The first inserts promotion and validity steps; the second may weaken away assumptions once resource sensitivity has been forgotten. An optimized positive translation can omit some exponentials beneath $\otimes$ and $\oplus$, but that optimization requires its own correctness argument and is not silently assumed here.

### 6. Cut and Identity Elimination

This section is marked in the source as not covered in the live lecture, but it is part of the numbered notes and therefore part of this guide.

If primitive identity is restricted to atoms, identity for every compound $A$ remains **admissible**. The interesting case $A=!A'$ works by deriving identity for $A'$, copying $A'$ from the valid to the linear zone with $\mathsf{valid}_L$, promoting, and finally applying $!L$.

Cut admissibility must be proved simultaneously for ordinary linear cut and a valid cut:

$$
\frac{\Gamma;\Delta\vdash A\qquad\Gamma;\Delta',A\vdash C}
     {\Gamma;\Delta,\Delta'\vdash C}\;\mathsf{cut}
$$

$$
\frac{\Gamma;\cdot\vdash A\qquad\Gamma,A;\Delta'\vdash C}
     {\Gamma;\Delta'\vdash C}\;\mathsf{cut}_{!}.
$$

The nested induction is ordered first by the structure of cut formula $A$, then by treating $\mathsf{cut}_{!A}$ as larger than $\mathsf{cut}_A$, and finally by derivation size. The middle component is needed when a valid assumption has been copied into the linear context: reduction produces one valid cut and one ordinary cut at the same formula. The exponential principal case reduces from $!A'$ to the strictly smaller $A'$, so formula size takes priority and the induction remains well founded.

## 5. Formal core

The system has two judgments and two context disciplines:

- $\Gamma\vdash A\;\mathsf{valid}$: $A$ has a proof independent of ephemeral resources; $\Gamma$ contains reusable valid assumptions.
- $\Gamma;\Delta\vdash A\;\mathsf{true}$: $A$ is presently true using every resource in the multiset $\Delta$ exactly once, while assumptions in $\Gamma$ may be reused.
- $\cdot$ is the empty context; $\vdash$ separates assumptions from conclusion; $;$ separates structural from linear assumptions.
- $R$ and $L$ label introduction on the right and elimination/use on the left. Subscripts on $\mathsf{valid}_R,\mathsf{valid}_L$ stress that validity is a judgment; they are not ordinary connective rules.

The logical heart is the chain

$$
\Gamma;\cdot\vdash A\;\mathsf{true}
\Longrightarrow
\Gamma\vdash A\;\mathsf{valid}
\Longrightarrow
\Gamma;\cdot\vdash !A\;\mathsf{true}.
$$

The first arrow is judgmental generalization; the second internalizes that stable status in the proposition language. Conversely, $!L$ turns a linear occurrence of $!A$ into a persistent valid assumption. Weakening and contraction for $!A$ are therefore consequences of its passage through the structural zone, not licenses attached to arbitrary $A$.

Theorem status matters:

- General identity and the two cut rules may be displayed like inference rules, but after restricting the primitive calculus they are admissible metatheorems.
- Failed proof search alone does not establish non-derivability. Cut and identity elimination justify restricting attention to cut-free, expanded proofs; only then can rule-shape arguments establish impossibility claims such as $!(A\otimes B)\nvdash !A\otimes !B$.

## 6. Operational/computational reading

Treat $\Delta$ as the live resources of a computation and $\Gamma$ as a library of closed services. A derivation of $\Gamma;\cdot\vdash A$ is a service implementation with no outstanding linear dependency. Promotion packages it as $!A$. A client using $!A$ obtains a fresh linear instance of $A$ while the service remains available for future requests.

Under this reading:

- weakening means a reusable service may receive no requests;
- contraction means it may serve multiple requests;
- $!R$ is a closure check: a reusable service must not capture a one-shot channel;
- $!L$ registers the packaged service in the persistent environment;
- allowing $!R$ to capture a linear resource would let several clients race to duplicate the same one-shot channel, violating the session/resource invariant.

The translation $(A)^\vee$ is called “by value” because structural subvalues are placed behind reusable interfaces. The lecture warns, however, that a logically sound embedding can still alter operational observability. That limitation motivates keeping structural and linear programming native in LNL rather than treating one solely as a compilation target.

## 7. Worked derivation or trace in original notation and prose

We derive the useful law $\cdot;!A\vdash A\otimes A$. This does **not** duplicate the linear proposition $A$ directly; it opens a package whose content has already been certified as reproducible.

First move the banged assumption into the valid zone with $!L$. It remains to prove $A;\cdot\vdash A\otimes A$. Tensor right splits the empty linear context into two empty parts. In each branch, $\mathsf{valid}_L$ creates one linear use of $A$, discharged by identity:

$$
\frac{
  \frac{A;A\vdash A}{A;\cdot\vdash A}\;\mathsf{valid}_L
  \qquad
  \frac{A;A\vdash A}{A;\cdot\vdash A}\;\mathsf{valid}_L
}{A;\cdot\vdash A\otimes A}\;\otimes R
$$

and therefore

$$
\frac{A;\cdot\vdash A\otimes A}
     {\cdot;!A\vdash A\otimes A}\;!L.
$$

The boundary case $\cdot;A\nvdash A\otimes A$ isolates what mattered. Applying $\otimes R$ would have to partition the single $A$ between two premises; one branch would receive no $A$. Linear identity cannot solve both. The successful derivation duplicates a **valid proof source**, not an ephemeral proof object.

## 8. Conceptual synthesis

“Truth is ephemeral, validity forever” becomes a precise resource discipline. Truth is indexed by a current linear context. Validity is truth with that dependency removed. The exponential is the proposition-level reflection of validity back into linear logic.

This three-stage account—resource-free proof, structural judgment, modal proposition—explains both the power and the friction of $!$. It validates controlled reuse and embeds ordinary intuitionistic reasoning, but a compound $!A$ crosses two proof-theoretic boundaries. Consequently it has neither uniformly invertible right behavior nor uniformly invertible left behavior. Lecture 10 separates those crossings into two shifts with distinct polarities.

## 9. Common confusions and failure modes

- **“Valid” means currently true.** No. $A\;\mathsf{valid}$ means a proof of $A$ is independent of the linear state.
- **$\Gamma$ and $\Delta$ are interchangeable collections.** No. $\Gamma$ is structural and shareable; $\Delta$ is linear and partitioned.
- **$!A$ permits copying the same linear proof of $A$.** More accurately, $!A$ certifies a repeatable way to produce fresh uses of $A$.
- **Promotion may leave unused linear assumptions.** That would validate weakening and, together with reuse, contraction for arbitrary linear formulas.
- **A reusable pair is a pair of reusable components.** False for tensor: $!(A\otimes B)$ couples each $A$ with a $B$.
- **Getting stuck proves non-derivability.** Only a metatheoretic restriction such as cut elimination turns exhaustive rule analysis into such a proof.
- **Admissible cut is an object-language constructor.** It is a theorem saying any derivation using cut can be transformed into one without it.
- **The structural-to-linear translation is automatically semantics-preserving as a compiler.** The theorem preserves derivability; it does not by itself prove preservation of every observation or cost behavior.

## 10. Self-test questions with concise answers

1. **Why is $\Delta$ empty in $\mathsf{valid}_R$ and $!R'$?** Because validity must not depend on one-shot resources; otherwise promotion would discard or duplicate them.
2. **What operation does $\mathsf{valid}_L$ perform bottom-up?** It creates one linear occurrence of a valid assumption while retaining the reusable source in $\Gamma$.
3. **Why is $P\multimap !P$ not generally derivable?** A linear $P$ does not provide a resource-independent method for reproducing $P$.
4. **Why can $!(A\mathbin{\&}B)$ yield both $!A$ and $!B$?** Different reuses can choose different additive projections.
5. **Why can $!(A\otimes B)$ not generally yield $!A\otimes !B$?** Every use supplies the components jointly, not as independent reusable services.
6. **What does $(A)^\wedge$ forget?** Linearity and exponentials; both tensor and additive conjunction map to structural conjunction.
7. **What is special about the cut proof?** It simultaneously eliminates ordinary and valid cuts using a lexicographic measure that ranks valid cut above ordinary cut at the same formula.

## 11. Related concept pages

- [Validity](../Concepts/Validity.md)
- [Girard vs Andreoli exponentials](../Comparisons/Girard%20vs%20Andreoli%20Exponentials.md)
- [Identity and cut admissibility](../Concepts/Identity%20and%20Cut%20Admissibility.md)
- [Shifts between logics](../Concepts/Shifts%20Between%20Logics.md)
- [Additive and multiplicative connectives](../Concepts/Additive%20and%20Multiplicative%20Connectives.md)
- [Linear versus structural persistence](../Comparisons/Linear%20vs%20Structural%20Persistence.md)

## 12. Source trail

- **Lecture:** 9, “Validity,” September 26, 2023.
- **Numbered sections:** §1 Introduction; §2 Girard's Exponential; §3 Andreoli's Exponential; §4 Examples; §5 Translation from Structural into Linear Logic; §6 Cut and Identity Elimination (marked “not covered in lecture” in the notes).
- **Printed pages:** L9.1–L9.11.
- **PDF pages:** 102–112.

## 13. Previous/next navigation

[← Lecture 08 - Subtyping](Lecture%2008%20-%20Subtyping.md) · [Lecture 10 - A Mixed Linear-Nonlinear Logic →](Lecture%2010%20-%20A%20Mixed%20Linear-Nonlinear%20Logic.md)

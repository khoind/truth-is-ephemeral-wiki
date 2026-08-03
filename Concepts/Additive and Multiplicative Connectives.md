---
title: "Additive and Multiplicative Connectives"
aliases:
  - "Additives versus multiplicatives"
  - "Resource splitting versus choice"
tags:
  - linear-logic
  - ordered-logic
  - additives
  - multiplicatives
source_lectures:
  - 3
  - 4
prerequisites:
  - "Hypothetical judgments"
related:
  - "Ordered Conjunction and Implications"
  - "Polarity and Invertibility"
---

# Additive and Multiplicative Connectives

## 1. One-sentence definition

**Multiplicative connectives combine independently allocated resource segments, whereas additive connectives express alternatives whose premises are checked against the same surrounding context.**

## 2. Why the concept is needed

In structural logic, contraction and weakening blur two meanings of “and”: possessing both pieces and supporting either requested observation. Substructural logic cannot blur them because resources cannot be copied or discarded freely. A rule must say whether its premises divide the available resources or describe alternative uses of one resource state. That distinction produces different connectives, different units, different polarities, and different operational behavior.

## 3. Intuitive model

**Intuition.** A multiplicative pair is a packed lunch containing a sandwich **and** fruit; opening it yields both components, and preparing it allocates ingredients between them. An additive external choice is a service menu promising tea **and** coffee in the sense that the customer may request either; the provider must support both requests, but one interaction selects one branch. Internal choice reverses who selects. This service picture is intuition only—the formal rules decide resource use.

## 4. Formal core

Ordered fuse is multiplicative:

$$
\frac{\Omega_1\vdash A\qquad\Omega_2\vdash B}
     {\Omega_1\Omega_2\vdash A\bullet B}\;\bullet R
\qquad
\frac{\Omega_L A B\Omega_R\vdash C}
     {\Omega_L(A\bullet B)\Omega_R\vdash C}\;\bullet L.
$$

Its unit is $1$:

$$\frac{}{\cdot\vdash1}\;1R
\qquad
\frac{\Omega_L\Omega_R\vdash C}{\Omega_L1\Omega_R\vdash C}\;1L.$$

External choice (“with”), written $A\mathbin{\&}B$, is additive:

$$
\frac{\Omega\vdash A\qquad\Omega\vdash B}
     {\Omega\vdash A\mathbin{\&}B}\;\&R,
\quad
\frac{\Omega_L A\Omega_R\vdash C}{\Omega_L(A\mathbin{\&}B)\Omega_R\vdash C}\;\&L_1,
\quad
\frac{\Omega_L B\Omega_R\vdash C}{\Omega_L(A\mathbin{\&}B)\Omega_R\vdash C}\;\&L_2.
$$

Its nullary unit $\top$ has $\Omega\vdash\top$ with no premises and has no left rule.

Internal choice $A\oplus B$ is also additive, but the chooser is reversed:

$$
\frac{\Omega\vdash A}{\Omega\vdash A\oplus B}\;\oplus R_1
\quad
\frac{\Omega\vdash B}{\Omega\vdash A\oplus B}\;\oplus R_2
$$

$$
\frac{\Omega_L A\Omega_R\vdash C\qquad\Omega_L B\Omega_R\vdash C}
     {\Omega_L(A\oplus B)\Omega_R\vdash C}\;\oplus L.
$$

Its nullary unit $0$ has no right rule and a premise-free left rule.

$A,B,C$ are propositions; $\Omega$ variables denote ordered contexts; $\cdot$ is empty. Repeating the metavariable $\Omega$ in additive premises means each alternative is verified in the same context. It does not grant contraction inside a single chosen branch.

## 5. How to use/read it

Ask two questions. First, who chooses? For $A\mathbin{\&}B$, the consumer chooses through $\&L_1$ or $\&L_2$, so the provider proves both. For $A\oplus B$, the provider chooses a right injection, so the consumer covers both. Second, are both components simultaneously available? For $A\bullet B$, yes: the provider allocates disjoint ordered segments and the consumer receives adjacent components.

The rule shape predicts proof search. Multiplicative right rules search for a context split. Additive rules retain the whole context while branching over alternatives.

## 6. Worked example

Suppose $r:R$ is an ordered resource and there are proofs

$$r:R\vdash M:A \qquad r:R\vdash N:B.$$

Then $\&R$ constructs $r:R\vdash \&R\,M\,N:A\mathbin{\&}B$. A later consumer choosing the second projection reduces a principal cut to the $N$ branch; $M$ is not executed in parallel with it.

By contrast, to construct $A\bullet B$ from two ordered resources $p:P,q:Q$, we need a split:

$$
\frac{p:P\vdash M:A\qquad q:Q\vdash N:B}
     {p:P,q:Q\vdash\bullet R\,M\,N:A\bullet B}.
$$

$p$ belongs only to the first premise and $q$ only to the second. These examples have similar two-premise shapes but opposite resource discipline.

## 7. Non-example or boundary case

The rule

$$
\frac{\Omega_1\vdash A\qquad\Omega_2\vdash B}
     {\Omega_1\Omega_2\vdash A\mathbin{\&}B}
$$

is not external choice. A consumer may select only $A$, yet the conclusion has committed the $\Omega_2$ resources solely to the unused $B$ proof; they cannot be accounted for in the chosen branch. Conversely, using the same $\Omega$ for both premises of $\bullet R$ would copy resources and violate linear or ordered use.

$\top$ and $1$ are another boundary: both resemble “truth” structurally, but $1R$ requires the empty context while $\top R$ accepts any context.

## 8. Key consequences

- Substructural conjunction splits into positive tensor/fuse and negative external choice.
- Units split into multiplicative $1$ and additive $\top$.
- Principal cut reductions reveal who made a choice and discard only the unselected alternative proof.
- Multiplicative rules express simultaneous composition; additive rules express branching capability.
- Structural contraction and weakening can make these distinctions observationally collapse.

## 9. Relations to nearby concepts

[Ordered Conjunction and Implications](<Ordered Conjunction and Implications.md>) explains why ordered fuse splits a sequence in a direction-preserving way. [Polarity and Invertibility](<Polarity and Invertibility.md>) cuts across the additive/multiplicative distinction: $\bullet,1,\oplus,0$ are positive, while $\mathbin{\&},\top$ are negative. Thus “additive” does not mean “negative.” [Identity and Cut Admissibility](<Identity and Cut Admissibility.md>) explains why the shared-versus-split context patterns are forced by harmony.

## 10. Common mistakes

- Equating additive with optional or disposable.
- Interpreting two additive premises as two simultaneous uses of one linear resource.
- Assuming all conjunctions split the context.
- Confusing $\top$ with $1$ or $0$ with absence of syntax.
- Saying $A\oplus B$ lets the consumer choose; the provider chooses.
- Saying $A\mathbin{\&}B$ contains both values simultaneously; it promises both observable behaviors.

## 11. What to remember

- Multiplicatives partition resources; additives preserve the same context across alternatives.
- $\bullet$ packages both components; $\mathbin{\&}$ lets the consumer choose; $\oplus$ lets the provider choose.
- $1$ is multiplicative, $\top$ additive, and $0$ the empty internal choice.
- Additive/multiplicative and positive/negative are independent classifications.
- Rule premises expose the resource policy precisely.

## 12. Source trail

- Lecture 3, Section 2.1, printed pp. L3.3–L3.5, PDF pp. 28–30: multiplicative ordered conjunction and context splitting.
- Lecture 3, Sections 6–10, printed pp. L3.9–L3.12, PDF pp. 34–37: external choice, $1$, internal choice, $\top$, and $0$.
- Lecture 4, Section 2, printed p. L4.6, PDF p. 48: proof constructors for fuse.
- Lecture 4, Sections 4–5, printed pp. L4.7–L4.9, PDF pp. 49–51: polarity and the structural/linear/ordered connective table.

---
title: Mixed Linear-Nonlinear Logic
aliases: [LNL, mixed linear nonlinear logic]
tags: [lnl, linear-logic, structural-logic, shifts, lecture-10]
source_lectures: ["Lecture 10 - A Mixed Linear-Nonlinear Logic"]
prerequisites: [Validity, linear implication, structural implication]
related: [Shifts Between Logics, Adjoint Logic, Linear vs Structural Persistence]
---

# Mixed Linear-Nonlinear Logic

## One-sentence definition

**Mixed linear/nonlinear logic (LNL) combines native structural and linear propositions in separate strata connected by shifts, rather than encoding all structural reasoning through the linear exponential.**

## Why the concept is needed

Encoding structural logic with $!A$ is expressive, but it makes structural operations pass through linear syntax and can obscure their original computational meaning. The exponential is also neither uniformly positive nor negative. LNL lets functional, freely reusable data remain structural and message-passing resources remain linear, while still allowing typed interaction between them. It aims for cut and identity elimination plus conservative extension: a shift-free structural proof should remain a structural proof, and a downshift-free linear proof should remain linear.

## Intuitive model

**Intuition.** Think of two programming regions. The structural region contains duplicable functions and services; the linear region contains one-use sessions. A shift is a checked interface that creates a session from a service or packages a service reference for use by a session. Neither region is translated away.

## Formal core

The grammars are mode-indexed:

$$
\begin{aligned}
A_S &::= P_S\mid A_S\supset B_S\mid A_S\land B_S\mid\top\mid A_S\lor B_S\mid\bot\mid \uparrow A_L,\\
A_L &::= P_L\mid A_L\multimap B_L\mid A_L\otimes B_L\mid 1\mid A_L\mathbin{\&}B_L\mid\top\mid A_L\oplus B_L\mid0\mid\downarrow A_S.
\end{aligned}
$$

Subscripts $S$ and $L$ mean structural and linear modes. $\Gamma$ contains structural assumptions; $\Delta$ contains linear assumptions. The two judgments are

$$\Gamma\vdash A_S \qquad\text{and}\qquad \Gamma;\Delta\vdash A_L.$$

A structural conclusion cannot depend on $\Delta$. Implications therefore have distinct native rules, such as

$$
\frac{\Gamma,A_S\vdash B_S}{\Gamma\vdash A_S\supset B_S}\;\supset R
\qquad
\frac{\Gamma;\Delta,A_L\vdash B_L}{\Gamma;\Delta\vdash A_L\multimap B_L}\;\multimap R.
$$

Identity has structural and linear forms. Cut has three forms: structural into structural ($\mathsf{cut}_{SS}$), structural into linear ($\mathsf{cut}_{SL}$), and linear into linear ($\mathsf{cut}_{LL}$). There is no linear-into-structural cut because that would violate independence.

## How to use/read it

Determine a proposition’s stratum before choosing a rule. A structural goal uses only $\Gamma$; a linear goal may use both $\Gamma$ and $\Delta$, but each member of $\Delta$ exactly once. To cross strata, use an explicit $\uparrow$ or $\downarrow$ rule. Operationally, a structural provider may spawn many fresh linear sessions; a linear session may transmit access to a structural service.

## Worked example

Suppose a tree fold receives a linear tree $t:\mathsf{tree}_A$ but applies functions at every node and leaf. Give the combining function structural type $f_S:\uparrow(B\otimes B\multimap B)$ and the leaf function $h_S:\uparrow(A\multimap B)$.

1. Receive on linear $t$ and branch on `node` or `leaf`.
2. In a node branch, split the linear children into $l$ and $r$.
3. Recursively process $l$ and $r$. Both calls may mention $f_S,h_S$ because they are structural; the children themselves split linearly.
4. Request a fresh linear instance $f_L:B\otimes B\multimap B$ through the upshift interface.
5. Send the pair of recursive results to $f_L$ and forward its result to the destination.
6. In a leaf branch, request $h_L:A\multimap B$ and apply it once.

The example combines sharing of functions with exact use of tree channels.

## Non-example or boundary case

Typing $f$ merely as $B\otimes B\multimap B$ fails for a recursive tree: every node needs another use, but a linear channel cannot be copied into both recursive calls. Conversely, placing a linear tree channel in $\Gamma$ would silently permit dropping or duplicating its session. LNL does not authorize either coercion; the shift changes how interaction is exposed, not the intrinsic mode of arbitrary data.

## Key consequences

The shifts clarify polarity: $\uparrow$ is negative and $\downarrow$ positive, so $!A\equiv\downarrow\uparrow A$ is positive outside and negative inside. Simultaneous identity and cut admissibility imply conservative extension of both fragments. Operationally, structural cuts yield persistent providers while linear cuts yield one-use processes, enabling pipelined parallel programs.

## Relations to nearby concepts

[Shifts Between Logics](Shifts%20Between%20Logics.md) gives the exact crossing rules and dynamics. [Adjoint Logic](Adjoint%20Logic.md) generalizes two strata to a preorder of modes and unifies duplicated connective rules. [Linear vs Structural Persistence](../Comparisons/Linear%20vs%20Structural%20Persistence.md) separates typing permission from runtime longevity.

## Common mistakes

- Using $\supset$ at mode $L$ or $\multimap$ at mode $S$.
- Allowing $\Gamma;\Delta\vdash A_S$ with nonempty $\Delta$.
- Treating a shift as an implicit coercion that can be inserted anywhere.
- Assuming a structural channel is the same as two pre-created linear channels.

## What to remember

- LNL preserves two native logics and connects them explicitly.
- Structural goals are independent of linear assumptions.
- There are two identities and three possible cuts.
- $!A$ decomposes as $\downarrow\uparrow A$.
- Shared services can spawn fresh linear interactions.

## Source trail

Lecture 10, “A Mixed Linear/Nonlinear Logic,” §§1–10, printed lecture pages L10.1–L10.9, PDF pages 113–121. See [Lecture 10 - A Mixed Linear-Nonlinear Logic](../Lectures/Lecture%2010%20-%20A%20Mixed%20Linear-Nonlinear%20Logic.md).

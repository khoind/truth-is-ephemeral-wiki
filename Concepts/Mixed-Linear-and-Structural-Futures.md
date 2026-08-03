---
title: Mixed Linear and Structural Futures
aliases:
  - mixed-mode futures
  - persistent future cells
tags:
  - futures
  - adjoint-logic
  - persistence
source_lectures:
  - 16
prerequisites:
  - "[Futures and single assignment](Futures-and-Single-Assignment.md)"
related:
  - "[Resource regimes](../Comparisons/Resource-Regimes.md)"
  - "[Positive and negative futures](../Comparisons/Positive-and-Negative-Futures.md)"
---

# Mixed Linear and Structural Futures

## One-sentence definition

Mixed linear/structural futures combine consumable linear addresses with reusable structural addresses, connected by shifts and implemented by ordinary cells versus persistent cells.

## Why the concept is needed

Purely linear futures allow exactly one consumer interaction, but many programs share immutable data or reusable services. Allowing unrestricted reuse everywhere would destroy linear ownership. Modes and shifts state exactly where persistence is permitted while preserving single assignment: structural cells may be read repeatedly, yet they are still written only once.

## Intuitive model

**Intuition.** A linear cell is a one-use ticket collected at the gate. A structural cell is a posted notice that remains after each reader consults it. A shift is the controlled doorway between the two zones; it is not a cast that discards resource rules.

## Formal core

Write $A_S$ for a structural type and $A_L$ for a linear type. The positive downshift $\downarrow A_S$ packages a structural address for linear use, while the negative upshift $\uparrow A_L$ exposes a linear computation through a structural interface. Representative rules are:

$$
\frac{\Delta_S,y_S:A_S\vdash \operatorname{write}\ x_L\langle y_S\rangle::(x_L:\downarrow A_S)}{}
\qquad
\frac{\Delta,y_S:A_S\vdash Q(y_S)::\delta}
{\Delta,x_L:\downarrow A_S\vdash \operatorname{read}\ x_L(\langle y_S\rangle\Rightarrow Q)::\delta}
$$

and

$$
\frac{\Delta\vdash P(y_L)::(y_L:A_L)}
{\Delta\vdash \operatorname{write}\ x_S(\langle y_L\rangle\Rightarrow P)::(x_S:\uparrow A_L)}.
$$

$\Delta_S$ contains only structural assumptions; $\delta$ is an arbitrary succedent judgment. At runtime:

$$
\begin{aligned}
\operatorname{proc}(\operatorname{write}\ a_S S)&\longrightarrow {!}\operatorname{cell}(a_S,S),\\
{!}\operatorname{cell}(a_S,S),\operatorname{proc}(\operatorname{read}\ a_S S')
&\longrightarrow {!}\operatorname{cell}(a_S,S),\operatorname{proc}(S\mathbin{\triangleright\!	riangleleft}S').
\end{aligned}
$$

The persistent cell remains. The symmetric matching operation $\triangleright\!\triangleleft$ chooses whichever storable is the continuation: $K\triangleright\!\triangleleft V=V\triangleright\!\triangleleft K=V\triangleright K$.

## How to use/read it

Assign a structural mode only to data or behavior that may legitimately be duplicated or ignored. Use a downshift when a linear structure holds a reference to shared content. Use an upshift for reusable access to linear behavior. Track the address mode at every read and move: linear transitions consume the source capability; structural transitions retain it.

## Worked example

Consider a linear list whose elements are shared binary numbers:

$$
\mathsf{list}=\oplus\{\mathsf{nil}:1,\ \mathsf{cons}:\downarrow\mathsf{bin}_S\otimes\mathsf{list}\}.
$$

1. Reading a `cons` cell yields $\langle x_S\rangle$ and linear tail $t_L$.
2. A shared function $F_S:\mathsf{bin}_S\to\mathsf{bin}_S$ may be read to produce $y_S$.
3. Recursion consumes $t_L$ exactly once and produces result tail $r_L$.
4. The result cell is written with $\mathsf{cons}(\langle y_S\rangle,r_L)$.
5. Other processes may still read $x_S$, $y_S$, or $F_S$ because their cells persist; no process may reuse $t_L$ after its consuming read.

## Non-example or boundary case

Marking a mutable accumulator structural does not make concurrent updates safe. Structural persistence duplicates read access to an immutable, single-assignment result; it does not authorize overwriting or racing writers.

## Key consequences

Modes separate lifetime and duplication policies from the shape of data. Shifts make cross-mode dependencies explicit. Persistent reads model sharing without abandoning proofs-as-programs. The same positive/negative distinction still controls whether a structural cell stores a value or a continuation.

This separation is useful for modular reasoning: a linear container can guarantee that its spine is consumed exactly once while its shifted payloads remain freely shareable. Changing the payload mode does not require weakening the container's ownership invariant.

## Relations to nearby concepts

[Resource regimes](../Comparisons/Resource-Regimes.md) compares the underlying weakening and contraction permissions. [Validity and untethering](Validity-and-Untethering.md) interprets structural truth as requiring no linear resource. [Data layout and compound values](Data-Layout-and-Compound-Values.md) uses general adjoint shifts even within a single mode to force indirection.

## Common mistakes

- Equating structural with mutable.
- Assuming a persistent cell may be initialized repeatedly.
- Omitting the mode restriction on the context of a shift rule.
- Treating $\downarrow$ and $\uparrow$ as inverse runtime operations.
- Forgetting that linear addresses inside shared interfaces still obey linear use when exposed.

## What to remember

- Linear cells are consumable; structural cells persist across reads.
- Both remain single-assignment.
- Shifts are controlled mode boundaries.
- Persistence changes resource use, not connective polarity.

## Source trail

Lecture 16, §4 “Mixed Linear/Structural Futures,” printed pp. L16.6–L16.8, PDF pp. 176–178.

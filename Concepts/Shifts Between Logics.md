---
title: Shifts Between Logics
aliases: [LNL shifts, upshift and downshift]
tags: [shifts, lnl, modality, polarity, lecture-10]
source_lectures: ["Lecture 10 - A Mixed Linear/Nonlinear Logic"]
prerequisites: [Mixed Linear-Nonlinear Logic, Validity]
related: [Adjoint Modalities, Positive vs Negative Polarity, Adjoint Logic]
---

# Shifts Between Logics

## One-sentence definition

**The LNL shifts $\uparrow$ and $\downarrow$ are explicit modalities that move a proposition across the linear–structural boundary while enforcing independence and resource discipline.**

## Why the concept is needed

Separate structural and linear strata preserve each logic’s native meaning, but isolation alone cannot express a reusable service that supplies linear sessions or a linear protocol that carries structural data. Shifts provide exactly those interfaces. Their rules also explain the mixed polarity of the exponential: $!A$ is not a primitive mystery but the composite $\downarrow\uparrow A$.

## Intuitive model

**Intuition.** $\uparrow A_L$ is a shared service endpoint: each request yields a fresh one-use session of type $A_L$. $\downarrow A_S$ is a linear package whose payload is a structural endpoint of type $A_S$. A shift does not duplicate its linear payload or make all data coercible; it prescribes a communication handshake between modes.

## Formal core

$A_L$ ranges over linear propositions, $A_S$ over structural propositions, $\Gamma$ over structural assumptions, $\Delta$ over linear assumptions, and $C_L$ over linear conclusions. The rules are

$$
\frac{\Gamma;\cdot\vdash A_L}{\Gamma\vdash\uparrow A_L}\;\uparrow R
\qquad
\frac{\Gamma,\uparrow A_L;\Delta,A_L\vdash C_L}
{\Gamma,\uparrow A_L;\Delta\vdash C_L}\;\uparrow L,
$$

$$
\frac{\Gamma\vdash A_S}{\Gamma;\cdot\vdash\downarrow A_S}\;\downarrow R
\qquad
\frac{\Gamma,A_S;\Delta\vdash C_L}
{\Gamma;\Delta,\downarrow A_S\vdash C_L}\;\downarrow L.
$$

The dot is the empty linear context. $\uparrow R$ is right-invertible, so $\uparrow$ is negative; $\downarrow L$ is left-invertible, so $\downarrow$ is positive. With structural mode $S$ above linear mode $L$, $!A_L\equiv\downarrow\uparrow A_L$ has a positive outer shift and negative inner shift.

Process annotations expose the mode change. A provider of $x_S:\uparrow A_L$ receives a fresh linear channel $y_L$ and continues as a provider of $A_L$ on $y_L$; a client sends that fresh $y_L$. For $x_L:\downarrow A_S$, the provider sends a fresh structural channel $y_S$, and the client receives it.

## How to use/read it

Read $\uparrow A_L$ at structural mode as “repeatably initiate an $A_L$ session,” not “store one reusable $A_L$.” Read $\downarrow A_S$ at linear mode as “perform one transfer that reveals an $A_S$ service.” In proof search, use the connective’s rule; do not silently move formulas between contexts. In execution, the shift message carries a fresh channel whose mode differs from the original.

## Worked example

Derive that upshift preserves implication in the expected mixed form:

$$\vdash \uparrow(A_L\multimap B_L)\supset(\uparrow A_L\supset\uparrow B_L).$$

1. Apply $\supset R$ twice. The structural context now contains $f:\uparrow(A_L\multimap B_L)$ and $a:\uparrow A_L$; the goal is $\uparrow B_L$.
2. Apply $\uparrow R$. It suffices to prove $B_L$ with an empty linear context.
3. Apply $\uparrow L$ to $f$, materializing one linear instance $f':A_L\multimap B_L$.
4. Apply $\uparrow L$ to $a$, materializing $a':A_L$.
5. Use $\multimap L$: identity proves the argument $a':A_L$, and identity proves the resulting $B_L$.
6. The two linear instances are consumed, while the structural assumptions remain available.

This is an original schematic derivation; all crossings are explicit.

## Non-example or boundary case

$\Gamma;\Delta\vdash A_L$ with nonempty $\Delta$ cannot be promoted to $\Gamma\vdash\uparrow A_L$. Otherwise a structural service would close over a one-use resource and could replay it for multiple clients. Similarly, $\uparrow A_L$ is not definitionally equal to $A_L$: their modes, judgments, and operational roles differ.

## Key consequences

Shifts support direct mixed programming, expose polarities, and explain both monadic and comonadic composites. Their cut interactions preserve conservative extension: without shifts, proofs remain in their native fragment. Operationally, fresh continuation channels isolate each linear use of a shared provider.

## Relations to nearby concepts

[Mixed Linear-Nonlinear Logic](Mixed%20Linear-Nonlinear%20Logic.md) supplies the two judgments. [Adjoint Modalities](Adjoint%20Modalities.md) indexes shifts by arbitrary comparable modes. [Positive vs Negative Polarity](../Comparisons/Positive%20vs%20Negative%20Polarity.md) explains why upshift and downshift have opposite orientations. [Adjoint SAX, Message Sequences, and Pattern Matching](Adjoint%20SAX%2C%20Message%20Sequences%2C%20and%20Pattern%20Matching.md) turns shift rules into asynchronous messages.

## Common mistakes

- Reading $\uparrow A$ as contraction directly on $A$.
- Omitting the empty-linear-context side condition.
- Swapping provider/client behavior for $\uparrow$ and $\downarrow$.
- Assuming a shift changes only syntax and has no runtime action.

## What to remember

- Shifts are typed interfaces between modes.
- $\uparrow$ is negative; $\downarrow$ is positive.
- $!A=\downarrow\uparrow A$ in the linear fragment.
- Fresh cross-mode channels preserve linear isolation.

## Source trail

Lecture 10, §§2, 4, 6, 8, and 10, printed lecture pages L10.2–L10.8 and L10.9, PDF pages 114–120 and 121. See [Lecture 10 - A Mixed Linear-Nonlinear Logic](../Lectures/Lecture%2010%20-%20A%20Mixed%20Linear-Nonlinear%20Logic.md).

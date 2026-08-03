---
title: Adjoint SAX, Message Sequences, and Pattern Matching
aliases: [adjoint SAX, message sequences, SAX pattern matching]
tags: [adjoint-sax, message-sequences, pattern-matching, partial-focusing, lecture-15]
source_lectures: ["Lecture 15 - Adjoint SAX"]
prerequisites: [Semi-Axiomatic Sequent Calculus and SAX, Adjoint Modalities, Focusing]
related: [Continuation Channels, Linear vs Structural Persistence, Inversion Chaining and Proof Phases]
---

# Adjoint SAX, Message Sequences, and Pattern Matching

## One-sentence definition

**Adjoint SAX extends asynchronous SAX with mode-changing messages, then represents chains of continuation messages as typed sequences and their consumers as nested patterns corresponding to partial focusing and inversion.**

## Why the concept is needed

Purely linear SAX cannot directly express shared functions, multicast, or servers with several clients. Adjoint modalities add structural modes, and asynchronous delivery avoids the unclear notion of synchronously delivering one action to many clients. Meanwhile, allocating a fresh continuation channel for every message is theoretically clean but implementation-heavy. Message sequences compact linked messages; pattern matching consumes them at useful granularity without losing their proof-theoretic account.

## Intuitive model

**Intuition.** Adjoint SAX combines shared service doors with private session corridors. A message sequence is several corridor signs folded into one packet. A nested pattern unfolds just enough signs to reach the data a branch needs, while a variable pattern keeps the rest of the corridor abstract.

## Formal core

For two modes $S>L$, types include structural $\uparrow A_L$ and linear $\downarrow A_S$. In semi-axiomatic form, upshift’s invertible right rule remains and its left rule becomes an axiom:

$$
\frac{\Delta\vdash A_L}{\Delta\vdash\uparrow A_L}\;\uparrow R
\qquad
\Delta_S,\uparrow A_L\vdash A_L\;\uparrow X.
$$

Process annotations use cross-mode message $\langle x'_L\rangle$: a provider receives it on structural $x_S$, while a client sends it and continues on linear $x'_L$. Downshift is symmetric: the provider sends $\langle x'_S\rangle$ on linear $x_L$, and the client receives the structural continuation.

Message sequences are

$$M::=k(M)\mid(y,M)\mid()\mid x'.$$

$k(M)$ is a labeled continuation, $(y,M)$ pairs a transmitted channel with a continuation, $()$ terminates, and $x'$ stops the sequence at a real channel. Typing $\Delta\vdash M:\lfloor A\rfloor$ is **partial right focus** for positive $A$; dual typing for a negative antecedent is partial left focus. The floor brackets are judgmental markers, not modalities.

Continuations are nonempty pattern lists $K::=(M\Rightarrow P\mid K)\mid\cdot$. A judgment $\Delta;A\vdash K::\delta$ partially inverts positive $A$, where $\delta$ is a singleton process succedent. Projection $K@(y,\_)$ filters pair patterns and consistently binds $y$; $K@\ell(\_)$ filters label $\ell$; $K@()$ requires the unit pattern. Nonemptiness and coverage prevent a well-typed message from reaching no branch.

## How to use/read it

Use a shift send/receive when the continuation changes mode. Build a sequence by following the type’s focused constructors, stopping at any actual continuation channel. Type a receiver by projecting its patterns according to the outer connective and recursively checking the remainder. For execution, elaborate sequences into core SAX: allocate fresh intermediate channels and turn nested patterns into nested simple receives.

## Worked example

Type the compact unary-halving patterns for

$$\mathsf{nat}=+\{\mathsf{zero}:1,\mathsf{succ}:\mathsf{nat}\}.$$

1. Pattern `zero()` projects through label `zero`, then matches unit; the branch sends `zero()` as result.
2. Pattern `succ(zero())` first projects `succ`, then `zero`, then unit; it covers input one.
3. Pattern `succ(succ(y))` projects `succ` twice and stops at continuation variable $y:\mathsf{nat}$.
4. The third branch recursively halves $y$ and sends `succ(h)`.
5. Projection by the outer labels separates the branches deterministically; recursive projections validate their nested depths.
6. Elaboration creates fresh channels between each simple label/unit message, recovering ordinary SAX without changing the type.

## Non-example or boundary case

A continuation set omitting the `zero` branch is not well typed for `nat`; an actual `zero()` message would have no recipient. A pair projection applied to a label pattern is undefined, preventing shape confusion. A message sequence is not an unrestricted tree: in $(y,M)$ the transmitted $y:A$ moves to the ordinary context while only $M$ continues the sequence. Finally, shared channels do not make their spawned linear continuation channels reusable.

## Key consequences

Adjoint SAX supports shared providers and linear sessions in one asynchronous calculus. Message sequences model queues compactly and can reduce allocation; patterns offer deterministic deep matching. Their typing reconstructs partial focus/inversion, and type-directed elaboration proves that the extension is conservative over core SAX. Mixed map-reduce gains parallel recursive calls and futures-style pipelining because shared functions can serve multiple fresh linear requests.

## Relations to nearby concepts

[Continuation Channels](Continuation%20Channels.md) gives the core representation that sequences compress. [Adjoint Modalities](Adjoint%20Modalities.md) supplies cross-mode protocols. [Linear vs Structural Persistence](../Comparisons/Linear%20vs%20Structural%20Persistence.md) distinguishes shared services from their private continuations. [Inversion, Chaining, and Proof Phases](Inversion%2C%20Chaining%2C%20and%20Proof%20Phases.md) explains the full versus partial phase discipline.

## Common mistakes

- Treating $\lfloor A\rfloor$ as a new type constructor.
- Allowing empty or nonexhaustive pattern collections.
- Forgetting that projections may be undefined on the wrong shape.
- Assuming compact sequences change core operational semantics.
- Reusing a linear continuation obtained from a structural shift.

## What to remember

- Shift messages carry continuation channels at a different mode.
- Sequences compress chains of SAX messages.
- Sequence typing is partial focusing.
- Pattern typing is partial inversion via projection.
- Elaboration restores simple messages and fresh intermediate channels.
- Structural providers may spawn many distinct linear sessions.

## Source trail

Lecture 15, “Adjoint SAX,” §§1–7, printed lecture pages L15.1–L15.12, PDF pages 159–170. See [Lecture 15 - Adjoint SAX](../Lectures/Lecture%2015%20-%20Adjoint%20SAX.md).

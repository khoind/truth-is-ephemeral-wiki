---
title: Futures, Addresses, and Single Assignment
aliases:
  - futures
  - write-once cells
  - single-assignment memory
tags:
  - futures
  - concurrency
  - sax
source_lectures:
  - 16
prerequisites:
  - "[Semi-axiomatic sequent calculus](../Comparisons/Sequent-Calculus-SAX-and-Explicit-Resources.md)"
related:
  - "[Positive and negative futures](../Comparisons/Positive-and-Negative-Futures.md)"
  - "[Mixed linear and structural futures](Mixed-Linear-and-Structural-Futures.md)"
---

# Futures, Addresses, and Single Assignment

## One-sentence definition

A **future** is a fresh address that one computation will fill exactly once while other computations may proceed using the address and block only when they must inspect its eventual contents.

## Why the concept is needed

Message passing and shared memory need not be rival explanations of concurrency. The future interpretation gives SAX's proofs-as-programs language a shared-memory account without introducing mutation: a sequent variable denotes an address, antecedent addresses are inputs to read, and the succedent address is the unique output to fill. This keeps logical ownership visible while resembling an implementation with allocated cells.

## Intuitive model

**Intuition.** Imagine a claim ticket attached to an empty, sealed display box. A producer owns the one opportunity to put an exhibit in the box. A consumer can carry the ticket and do unrelated work; when it needs the exhibit, it waits. Once filled, the box is never revised. This intuition explains synchronization, but it is not an imperative heap with arbitrary updates.

## Formal core

The process judgment is

$$
x_1:A_1,\ldots,x_n:A_n \vdash P :: (x:A).
$$

Each $x_i$ and $x$ is an address; $A_i$ and $A$ describe cell contents; $P$ is a process. In the linear fragment, $P$ must consume each input capability and produce the output capability. Core syntax is:

$$
P ::= x \leftarrow P_1(x);P_2(x) \mid \operatorname{move}\ x\ y
\mid \operatorname{write}\ x\,S \mid \operatorname{read}\ x\,K.
$$

$S$ is a storable value or continuation, and $K$ is a continuation/pattern. Runtime configurations distinguish active processes from filled cells:

$$
\begin{aligned}
\operatorname{proc}(x\leftarrow P;Q)&\longrightarrow
  \operatorname{proc}(P(a)),\operatorname{proc}(Q(a)) && a\text{ fresh},\\
\operatorname{proc}(\operatorname{write}\ a\,S)&\longrightarrow \operatorname{cell}(a,S),\\
\operatorname{cell}(a,S),\operatorname{proc}(\operatorname{read}\ a\,K)&\longrightarrow
  \operatorname{proc}(S\mathbin{\triangleright}K),\\
\operatorname{cell}(b,S),\operatorname{proc}(\operatorname{move}\ a\ b)&\longrightarrow
  \operatorname{cell}(a,S).
\end{aligned}
$$

$S\triangleright K$ applies a stored value to a matching continuation. Freshness prevents aliasing an already allocated result. No transition overwrites $\operatorname{cell}(a,S)$: this is the operational single-assignment invariant.

## How to use/read it

Read cut as allocation plus parallel composition, identity as copying/moving a completed cell's content to the required destination, `write` as fulfillment, and `read` as synchronization. A process that does not yet need the cell may run. A read with no matching cell is blocked, not erroneous. A final terminating configuration contains cells and no processes.

## Worked example

Suppose a producer writes a tagged unit and a consumer flips the tag:

1. Start with
   $\operatorname{proc}(r\leftarrow \operatorname{write}\ r\,\mathsf{yes}(u);\operatorname{read}\ r\,K)$ and a cell $\operatorname{cell}(u,())$.
2. Cut allocates fresh $a$:
   $\operatorname{proc}(\operatorname{write}\ a\,\mathsf{yes}(u)),\operatorname{proc}(\operatorname{read}\ a\,K)$.
3. The producer fulfills the future:
   $\operatorname{cell}(a,\mathsf{yes}(u)),\operatorname{proc}(\operatorname{read}\ a\,K)$.
4. Let $K=(\mathsf{yes}(z)\Rightarrow\operatorname{write}\ r\,\mathsf{no}(z)\mid
   \mathsf{no}(z)\Rightarrow\operatorname{write}\ r\,\mathsf{yes}(z))$.
5. Reading selects the first branch and yields
   $\operatorname{proc}(\operatorname{write}\ r\,\mathsf{no}(u))$.
6. The result is $\operatorname{cell}(r,\mathsf{no}(u))$.

The consumer could have run until step 3, but its read could not fire before the write.

## Non-example or boundary case

Two processes writing different values to the same address are not a future program:
$\operatorname{proc}(\operatorname{write}\ a\,V_1),\operatorname{proc}(\operatorname{write}\ a\,V_2)$ violates unique production. Updating $\operatorname{cell}(a,V_1)$ to $\operatorname{cell}(a,V_2)$ is also outside this semantics; it requires mutable state and a different reasoning discipline.

## Key consequences

Single assignment removes write/write races. Fresh allocation exposes parallelism because producer and consumer are spawned together. Linearity gives a precise ownership discipline; structural modes later permit persistent reading without permitting a second write. The correspondence also separates addresses from stored values and active processes.

## Relations to nearby concepts

[Positive and negative futures](../Comparisons/Positive-and-Negative-Futures.md) explains why the polarity of a type determines whether a stored object is a value or continuation. [Mixed linear and structural futures](Mixed-Linear-and-Structural-Futures.md) adds persistent cells. [CLF and monadic concurrency](CLF-and-Monadic-Concurrency.md) represents these transitions as linear forward rules.

## Common mistakes

- Treating a future as a mutable reference.
- Saying cut merely substitutes: operationally it allocates a fresh address and spawns two processes.
- Confusing an address $a$ with the value stored at $a$.
- Assuming typing alone proves termination; recursive linear processes need an additional termination argument.
- Calling a blocked read a failed computation.

## What to remember

- A future is a one-writer synchronization cell.
- Sequent variables denote addresses, not values.
- Cut allocates; write fulfills; read synchronizes.
- Linear cells are consumed by a read; structural cells persist.
- Single assignment is weaker than general shared mutable memory.

## Source trail

Lecture 16, §§1–2, printed pp. L16.1–L16.4, PDF pp. 171–174; the mixed-mode persistence refinement is in §4, printed pp. L16.6–L16.8, PDF pp. 176–178.


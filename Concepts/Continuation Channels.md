---
title: Continuation Channels
aliases: [continuation pointers, asynchronous channel chains]
tags: [continuation-channels, sax, asynchronous-communication, session-types, lecture-14]
source_lectures: ["Lecture 14 - Semi-Axiomatic Sequent Calculus", "Lecture 15 - Adjoint SAX"]
prerequisites: [Semi-Axiomatic Sequent Calculus and SAX, linear channels]
related: [Cut Elimination for SAX, Adjoint SAX Message Sequences and Pattern Matching, Quantifiers in Substructural Logic]
---

# Continuation Channels

## One-sentence definition

**A continuation channel is the fresh typed address carried inside an asynchronous message that identifies where the remainder of the session protocol continues.**

## Why the concept is needed

Nonblocking sends can place several messages in a configuration before a receiver runs. If every message uses the same channel, arrival order is unconstrained and types can be confused. A continuation channel makes each protocol state a distinct linear address: consuming one message reveals the only address on which the next state can occur.

## Intuitive model

**Intuition.** Each message is a linked-list cell. Its outer channel is the cell’s address, its payload is the label or transmitted channel, and its continuation channel is the pointer to the next cell. A receiver cannot skip forward without first learning the pointer.

## Formal core

For internal choice $\oplus\{\ell:A_\ell\}_{\ell\in L}$, a message axiom has the process typing

$$
\frac{k\in L}{x':A_k\vdash \mathsf{send}\;x\;k(x')::(x:\oplus\{\ell:A_\ell\}_{\ell\in L})}\;\oplus X.
$$

$x$ is the current channel, $k$ the selected label, $x'$ the continuation channel, and $A_k$ the selected continuation type. A receiver is typed from branches $\Delta,x':A_\ell\vdash Q_\ell(x')::(z:C)$ for every $\ell\in L$.

The communication rule is

$$
\mathsf{proc}(\mathsf{send}\;a\;k(a')),
\mathsf{proc}(\mathsf{recv}\;a\;(\ell(x')\Rightarrow Q_\ell)_{\ell\in L})
\longrightarrow
\mathsf{proc}(Q_k(a')).
$$

The old address $a$ is consumed; communication continues on $a':A_k$. Tensor/implication messages use $(y,x')$, where $y$ is a transmitted channel and $x'$ the continuation. Unit uses $()$ and has no continuation because the protocol ends. Fresh continuation channels are allocated by cut; existential quantification can describe freshness at the logical-rule level.

## How to use/read it

Read the type of $x$ as the protocol state before the message and the type of $x'$ as the state after it. Allocate $x'$ before sending the outer message. The sender can terminate immediately after placing the message because the rest of its behavior is provided at $x'$ by another concurrent process. The receiver substitutes the actual continuation address for its branch variable.

## Worked example

Represent binary one at type

$$\mathsf{bin}=\oplus\{b0:\mathsf{bin},b1:\mathsf{bin},e:1\}.$$

1. Allocate $a'':1$ and send unit $()$ on it.
2. Allocate $a':\mathsf{bin}$ and send $e(a'')$ on $a'$.
3. Send $b1(a')$ on the public channel $a$.
4. The configuration may now contain all three messages concurrently.
5. A receiver on $a$ can match only $b1(a')$, because the other messages live at different addresses.
6. That branch continues on $a'$, where only $e(a'')$ matches, and finally on $a''$, where unit ends the session.

The pointer chain, not scheduler order, enforces the protocol.

## Non-example or boundary case

Sending `b1`, `e`, and `()` all on $a$ is not a shorter equivalent representation. Any could meet the first receive, and the channel would be assigned several incompatible protocol states. Reusing one continuation address in two messages is equally invalid: linearity requires unique ownership. Unit is a boundary case because no future communication remains, so no continuation pointer is needed.

## Key consequences

Continuation channels turn message collections into typed queues, support nonblocking send, and make cut allocation operational. They distinguish stable logical sessions from individual physical addresses: a session can traverse $a,a',a''$ even though no address changes type. Message sequences later compress several linked cells and can sometimes avoid fresh allocation.

## Relations to nearby concepts

[Semi-Axiomatic Sequent Calculus and SAX](Semi-Axiomatic%20Sequent%20Calculus%20and%20SAX.md) derives the message axioms. [Adjoint SAX, Message Sequences, and Pattern Matching](Adjoint%20SAX%2C%20Message%20Sequences%2C%20and%20Pattern%20Matching.md) compacts pointer chains. [Quantifiers in Substructural Logic](Quantifiers%20in%20Substructural%20Logic.md) explains logical freshness.

## Common mistakes

- Calling $x'$ a mutable new type for $x$; it is a distinct channel.
- Assuming physical arrival order replaces the pointer discipline.
- Forgetting to allocate continuation channels through cut.
- Adding a continuation to terminal unit.

## What to remember

- Every nonterminal message points to the next protocol address.
- The old address is consumed exactly once.
- Queue order comes from pointers, not timing.
- Cut creates fresh continuation channels.
- Message sequences are a compact representation of the same chain.

## Source trail

Lecture 14, §§2–3 and §§8–9, printed lecture pages L14.2–L14.3 and L14.7–L14.10, PDF pages 149–150 and 154–157; Lecture 15, §§1 and 5, printed pages L15.1 and L15.6–L15.7, PDF pages 159 and 164–165. See [Lecture 14 - Semi-Axiomatic Sequent Calculus](../Lectures/Lecture%2014%20-%20Semi-Axiomatic%20Sequent%20Calculus.md) and [Lecture 15 - Adjoint SAX](../Lectures/Lecture%2015%20-%20Adjoint%20SAX.md).

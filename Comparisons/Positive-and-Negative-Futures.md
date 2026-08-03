---
title: Positive versus Negative Future Interpretation
aliases:
  - positive futures
  - negative futures
tags:
  - futures
  - polarity
  - comparison
source_lectures:
  - 16
prerequisites:
  - "[Futures and single assignment](../Concepts/Futures-and-Single-Assignment.md)"
related:
  - "[Mixed linear and structural futures](../Concepts/Mixed-Linear-and-Structural-Futures.md)"
  - "[Data layout and compound values](../Concepts/Data-Layout-and-Compound-Values.md)"
---

# Positive versus Negative Future Interpretation

## One-sentence definition

Positive future cells store data selected by a producer, whereas negative future cells store continuations selected by a provider and later invoked with data supplied by a client.

## Why the concept is needed

Replacing every session `send` by `write` and every `receive` by `read` works only for positive types. In SAX, every succedent action becomes a write under the address interpretation. For a negative type, the right rule offers behavior rather than emitting an ordinary datum, so the cell must hold a continuation. Making this polarity reversal explicit prevents an incorrect operational translation.

## Intuitive model

**Intuition.** A positive cell is a parcel: the producer chooses what is inside and the consumer opens it. A negative cell is a service desk: the provider installs a procedure, and the client later supplies a request and return address. Both are write-once cells; what differs is the kind of storable object.

## Formal core

| Aspect | Positive type, e.g. $\oplus\{\ell:A_\ell\}$ or $A\otimes B$ | Negative type, e.g. $\mathbin{\&}\{\ell:A_\ell\}$ or $A\multimap B$ |
|---|---|---|
| Provider/right action | writes a value | writes a continuation |
| Client/left action | reads with a continuation/pattern | reads by supplying a value/request |
| Cell contents | $k(a)$, $(a_1,a_2)$, $()$ | branch continuation or $(x_1,x_2)\Rightarrow P$ |
| Message-passing correspondence | send $\mapsto$ write, receive $\mapsto$ read | send $\mapsto$ read, receive $\mapsto$ write |

For a negative choice $N\{\ell:A_\ell\}$:

$$
\frac{\Delta\vdash P_\ell(y)::(y:A_\ell)\quad(\ell\in L)}
{\Delta\vdash \operatorname{write}\ x\,(\ell(y)\Rightarrow P_\ell(y))_{\ell\in L}::(x:N\{\ell:A_\ell\})}
$$

and a client selects $k$ by reading $x$ with $k(a)$. For a linear function:

$$
\operatorname{write}\ f\,((x,r)\Rightarrow P(x,r))
$$

stores code expecting argument address $x:A$ and result address $r:B$. A client action $\operatorname{read}\ f\,(a,b)$ invokes it. The generic runtime interaction is

$$
\operatorname{cell}(f,K),\operatorname{proc}(\operatorname{read}\ f\,V)
\longrightarrow \operatorname{proc}(V\triangleright K).
$$

Here $V$ is a value, $K$ a continuation, and $V\triangleright K$ their pattern-directed application.

## How to use/read it

First locate the connective's polarity. Then ask what the provider must place at the succedent address. If the right rule constructs data, write a value and have the left rule read with a pattern. If the right rule abstracts over a future interaction, write that continuation and let the left axiom read it with the client-supplied request.

## Worked example

Let $f:A\multimap B$ store the continuation $K=((x,r)\Rightarrow \operatorname{move}\ r\ x)$, an identity-like service.

1. Provider: $\operatorname{proc}(\operatorname{write}\ f\,K)$.
2. Client has argument cell at $a$ and wants the result at $b$, so it runs $\operatorname{proc}(\operatorname{read}\ f\,(a,b))$.
3. The write produces $\operatorname{cell}(f,K)$.
4. The read invokes $(a,b)\triangleright K=\operatorname{move}\ b\ a$.
5. If $\operatorname{cell}(a,V)$ exists, move yields $\operatorname{cell}(b,V)$.

The function itself was not a pair of input and output values. It was stored behavior awaiting those addresses.

## Non-example or boundary case

Storing $(a,b)$ in a function cell $f:A\multimap B$ confuses a call with a function. Conversely, storing a branch continuation in a positive sum cell confuses the case analyzer with the selected tag. Both erase the left/right orientation that polarity determines.

## Key consequences

The memory model uniformly says “right writes, left reads,” but the message-passing vocabulary flips at negative types. Cells therefore store the sum type $S ::= V\mid K$, not values alone. This is also why negative data layout is less directly observable than positive layout.

## Relations to nearby concepts

[Futures and single assignment](../Concepts/Futures-and-Single-Assignment.md) gives the common cell dynamics. [Data layout and compound values](../Concepts/Data-Layout-and-Compound-Values.md) follows positive focusing to determine concrete layouts. [Partial focusing](../Concepts/Partial-Focusing.md) explains where positive construction stops at an address or negative boundary.

## Common mistakes

- Applying the positive send/write recipe to negative types.
- Calling a continuation an ordinary data value.
- Reversing provider and client: the succedent is always the address written by the process.
- Forgetting the destination address in the operational reading of $A\multimap B$.
- Treating polarity as a runtime sign attached to data rather than a property controlling rule orientation.

## What to remember

- Positive: provider writes data; client reads and matches it.
- Negative: provider writes behavior; client reads by supplying a request.
- “Right writes, left reads” is invariant.
- Message-passing send/receive correspondence flips for negative types.

## Source trail

Lecture 16, §2 “Reinterpreting SAX: Positive Types” and §3 “Reinterpreting SAX: Negative Types,” printed pp. L16.2–L16.6, PDF pp. 172–176.


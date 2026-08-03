---
title: "Session Connectives and Channel Passing"
aliases:
  - "Session-Type Connectives"
  - "Channel Mobility in Linear Sessions"
tags:
  - session-types
  - channel-passing
  - polarity
  - linear-logic
source_lectures:
  - 5
  - 6
prerequisites:
  - "Linear Message Passing and Session Types"
related:
  - "Linear Message Passing and Session Types"
  - "Cut Reduction as Process Execution"
---

# Session Connectives and Channel Passing

## 1. One-sentence definition

**Session connectives specify whether a provider or client sends the next label or channel and what residual protocol follows, while linear channel passing transfers—not duplicates—the right to use a communicated endpoint.**

## 2. Why the concept is needed

A protocol needs more structure than a sequence of untyped sends. It must identify who controls a choice, whether a message is control information or a channel capability, and which behavior becomes legal afterward. Four linear connectives provide this structure: internal and external choice for labels, and tensor and linear implication for channels.

Channel messages are especially important because they change network topology. A process can introduce two previously unconnected components by sending one endpoint to the other. Without linear ownership, the sender might keep using the same endpoint and create an uncontrolled race. The typing context prevents that aliasing.

## 3. Intuitive model

**Intuition.** A label message is like selecting a clause in a contract; a channel message is like handing over a single physical key. Internal choice and tensor let the provider initiate the handoff. External choice and linear implication make the provider wait for the client. After a key is handed over, the former owner no longer possesses it.

The physical-key metaphor captures uniqueness but not the full protocol: the key itself opens a channel governed by its own session type, and the carrier channel continues under another type.

## 4. Formal core

All rules classify a judgment $\Delta\vdash P::(x:T)$. $\Delta$ is an unordered linear context of channels used by process $P$; $x$ is the one channel it provides; and $T$ is the current session type on $x$.

### Label connectives

For finite internal choice $\oplus\{\ell:A_\ell\}_{\ell\in L}$, the provider selects $k\in L$:

$$
\frac{\Delta\vdash P::(x:A_k)\quad k\in L}
{\Delta\vdash\mathsf{send}\ x\ k;P::
(x:\oplus\{\ell:A_\ell\}_{\ell\in L})}\;\oplus R.
$$

Its client receives and covers all branches:

$$
\frac{\Delta,x:A_\ell\vdash Q_\ell::(z:C)\quad(\forall\ell\in L)}
{\Delta,x:\oplus\{\ell:A_\ell\}_{\ell\in L}\vdash
\mathsf{recv}\ x(\ell\Rightarrow Q_\ell)_{\ell\in L}::(z:C)}\;\oplus L.
$$

For finite external choice $\&\{\ell:A_\ell\}_{\ell\in L}$, responsibility reverses. The provider receives every possible client selection:

$$
\frac{\Delta\vdash P_\ell::(x:A_\ell)\quad(\forall\ell\in L)}
{\Delta\vdash\mathsf{recv}\ x(\ell\Rightarrow P_\ell)_{\ell\in L}::
(x:\&\{\ell:A_\ell\}_{\ell\in L})}\;\&R,
$$

while the client selects one $k\in L$:

$$
\frac{\Delta,x:A_k\vdash Q::(z:C)\quad k\in L}
{\Delta,x:\&\{\ell:A_\ell\}_{\ell\in L}\vdash
\mathsf{send}\ x\ k;Q::(z:C)}\;\&L.
$$

$L$ is finite, $\ell$ ranges over all labels, $k$ is one selected label, and $A_\ell$ is the residual type for that branch. Universal side conditions mean that a receiver of a choice must implement every advertised alternative.

### Channel connectives

For tensor $A\otimes B$, the provider sends an already-owned channel $w:A$ and continues to provide $x:B$:

$$
\frac{\Delta\vdash P::(x:B)}
{\Delta,w:A\vdash\mathsf{send}\ x\ w;P::(x:A\otimes B)}\;\otimes R^*.
$$

The receiver binds that channel as $y:A$:

$$
\frac{\Delta',y:A,x:B\vdash Q(y)::(z:C)}
{\Delta',x:A\otimes B\vdash
\mathsf{recv}\ x(y\Rightarrow Q(y))::(z:C)}\;\otimes L.
$$

For linear implication $A\multimap B$, the provider receives:

$$
\frac{\Delta,y:A\vdash P(y)::(x:B)}
{\Delta\vdash\mathsf{recv}\ x(y\Rightarrow P(y))::(x:A\multimap B)}\;\multimap R,
$$

and the client sends:

$$
\frac{\Delta',x:B\vdash Q::(z:C)}
{\Delta',w:A,x:A\multimap B\vdash
\mathsf{send}\ x\ w;Q::(z:C)}\;\multimap L^*.
$$

$A$ is the protocol of the transmitted channel and $B$ is the continuation on $x$. $y$ is a fresh bound variable at the receiver; $w$ is the concrete source channel being transferred. The star marks MPASS's single-continuation alternative rule, not a change to the connective.

At runtime, both channel connectives use the same synchronization shape:

$$
\mathsf{proc}(\mathsf{send}\ a\ b;P),
\mathsf{proc}(\mathsf{recv}\ a(y\Rightarrow Q(y)))
\longrightarrow
\mathsf{proc}(P),\mathsf{proc}(Q(b)).
$$

$a$ is the carrier channel, $b$ is the channel sent along it, and $Q(b)$ substitutes $b$ for the receiver's bound variable $y$.

## 5. How to use/read it

Inspect the outermost connective on the offered channel. If it is positive—$\oplus$, $1$, or $\otimes$—the provider sends. If it is negative—$\&$ or $\multimap$—the provider receives. Then update the type to the chosen branch or to $B$.

For channel transfer, also update ownership contexts. Immediately before a send, the sender's context contains $w:A$. In its continuation, $w$ is gone. Immediately after a receive, the receiver's continuation contains the transmitted name at type $A$. This accounting is the static form of topology change.

The label and channel rules reuse send/receive syntax, so syntax alone does not reveal polarity. Determine whether the process is provider or client from the side of the typing judgment on which the carrier channel appears.

## 6. Worked example

Define a reusable handoff protocol, parameterized by a parcel-channel type $P$:

$$
\mathsf{handoff}_P=
\&\{\mathsf{cancel}:1,
\ \mathsf{ship}:P\multimap
\oplus\{\mathsf{accepted}:1,\mathsf{returned}:P\otimes1\}\}.
$$

Suppose the client owns parcel channel $p:P$.

1. The outer $\&$ gives label control to the client. It sends $\mathsf{ship}$, advancing the carrier $h$ to $P\multimap(\cdots)$.
2. At $\multimap$, the client sends $p$ and relinquishes it. The provider receives it and now owns $p:P$.
3. The residual $\oplus$ gives the provider the next decision.
4. If the provider sends $\mathsf{accepted}$, it must consume the parcel through some internal behavior and then close $h$ at $1$.
5. If it sends $\mathsf{returned}$, the residual type is $P\otimes1$. It sends $p$ back, transfers ownership to the client, and closes $h$.

The returned execution prefix is:

$$
\mathsf{ship}\ (\text{client}\to\text{provider});\quad
p\ (\text{client}\to\text{provider});\quad
\mathsf{returned}\ (\text{provider}\to\text{client});\quad
p\ (\text{provider}\to\text{client});\quad
().
$$

This trace shows two independent notions of direction. Label direction follows $\&$ then $\oplus$; channel direction follows $\multimap$ then $\otimes$. The same parcel endpoint changes owner twice but is never held by both parties at once.

## 7. Non-example or boundary case

Consider advertising

$$
\&\{\mathsf{ship}:P\multimap1,\mathsf{cancel}:1\}
$$

but implementing only the ship branch. This is not a partial service that may get stuck only when cancellation occurs; it is untypable because $\&R$ requires a premise for every label.

Another invalid case sends $p:P$ under $\multimap L^*$ and then continues to read from $p$. The premise of the rule deliberately omits $p$, so such a continuation cannot be derived. If sharing is intended, a linear channel is the wrong abstraction.

The empty internal choice $0=\oplus\{\}$ is a logical boundary: there is no label a provider can select, hence no $\oplus R$ proof. An empty external choice has the dual flavor, but MPASS assumes nonempty finite label sets for convenience in the presented language.

## 8. Key consequences

- Connective polarity determines which endpoint sends the next message.
- Receiver rules for choices are exhaustive over the advertised label set.
- Residual types encode message order and branch-dependent futures.
- Channel communication performs capture-avoiding name substitution at the receiver.
- A sent channel disappears from the sender's linear context and appears in the receiver's.
- Mobility changes network connectivity without violating unique ownership.
- The same runtime synchronization can implement tensor or implication because typing determines roles.

## 9. Relations to nearby concepts

[Linear Message Passing and Session Types](Linear%20Message%20Passing%20and%20Session%20Types.md) explains why propositions, proofs, and reductions receive protocol, process, and execution readings. This page isolates the connective-level direction and ownership rules.

[Cut Reduction as Process Execution](Cut%20Reduction%20as%20Process%20Execution.md) explains how a matching send and receive become a configuration transition. This page explains why the actions match and how the types evolve.

Internal versus external choice is about **who selects a label**. Additive versus multiplicative structure is different: $\oplus$ and $\&$ branch among alternatives, whereas $\otimes$ and $\multimap$ transfer a channel and retain a continuation. Tensor also differs from a structural Cartesian product: a session provider sends one linear endpoint over time rather than constructing a freely duplicable pair value.

[Lecture 5](../Lectures/Lecture%2005%20-%20Linear%20Message%20Passing%20I.md) introduces polarity through $\oplus$ and $1$. [Lecture 6](../Lectures/Lecture%2006%20-%20Linear%20Message%20Passing%20II.md) develops finite $\&$, $\otimes$, $\multimap$, and mobile examples.

## 10. Common mistakes

- Memorizing “send is right, receive is left” without accounting for polarity.
- Calling $\&$ provider choice; its provider waits for the client.
- Reading $A\otimes B$ as “send both $A$ and $B$ channels”; $B$ is the continuation type of the carrier.
- Reading $A\multimap B$ as an unrestricted reusable function.
- Keeping a transmitted channel in the sender's continuation.
- Forgetting that a choice receiver needs every labeled continuation.
- Confusing label variables $\ell$ with channel variables $x,y,w$.
- Treating $\otimes R^*$ as the standard two-premise tensor rule; it is an alternative justified by translation.

## 11. What to remember

- $\oplus$ and $\otimes$: provider sends.
- $\&$ and $\multimap$: provider receives.
- Choices transmit labels; tensor and implication transmit channels.
- The continuation is the selected $A_\ell$ or the trailing $B$.
- Linear send transfers ownership and thereby changes connectivity safely.

## 12. Source trail

- Lecture 5, sections 3-6; printed pages L5.3-L5.8; PDF pages 56-61.
- Lecture 6, sections 3-9 and the statics/dynamics summaries; printed pages L6.2-L6.12; PDF pages 67-77.

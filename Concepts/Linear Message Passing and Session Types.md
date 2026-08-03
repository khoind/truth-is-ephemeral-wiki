---
title: "Linear Message Passing and Session Types"
aliases:
  - "Propositions as Sessions"
  - "Linear Propositions as Protocols"
tags:
  - linear-logic
  - session-types
  - message-passing
source_lectures:
  - 5
  - 6
prerequisites:
  - "Linear sequent calculus"
  - "Cut and identity"
related:
  - "Cut Reduction as Process Execution"
  - "Session Connectives and Channel Passing"
---

# Linear Message Passing and Session Types

## 1. One-sentence definition

**Linear message passing interprets a linear proposition as a session protocol, a proof as a process that follows that protocol, and proof reduction as communication between exactly one provider and one client.**

## 2. Why the concept is needed

Ordinary payload types say that a channel carries Booleans or integers, but not who sends first, which alternatives are legal, how later messages depend on earlier ones, or when the channel is finished. A session type answers those temporal questions. Linear logic adds an ownership discipline: an endpoint cannot be silently copied, shared, or dropped, so each protocol action has a unique peer.

The interpretation also gives the process language a proof-theoretic foundation. Communication constructs are not assembled ad hoc. Right and left rules describe the provider and client of a protocol, cut connects them, and the corresponding cut reduction supplies their interaction. This is a propositions-as-types correspondence specialized to concurrent, channel-based programs.

## 3. Intuitive model

**Intuition.** Think of a session type as a two-party contract written from the provider's viewpoint. Each clause says whether the provider must send or receive, what kind of message is involved, and which contract remains afterward. The client sees the complementary obligation.

This contract metaphor is limited. A session is not a shared checklist that many parties may update. It describes one linear channel with one provider and one client. Larger networks arise by composing many such private two-ended sessions.

## 4. Formal core

The typing judgment is

$$
\Delta\vdash P::(x:A).
$$

$P$ is a process. $x$ is the single channel that $P$ provides, and $A$ is its current session type. $\Delta$ is a finite unordered **linear context** of declarations $y:B$: for each such declaration, $P$ uses channel $y$ as a client at protocol $B$. Channel names are distinct, and every channel in $\Delta$ must be used exactly according to its protocol. The symbol $\vdash$ separates used channels from the provided channel; $::$ associates a process with its interface.

The basic session connectives are:

- $1$: the provider sends the unique close token $()$ and terminates;
- $\oplus\{\ell:A_\ell\}_{\ell\in L}$: the provider selects and sends one label $\ell$, then continues as $A_\ell$;
- $\&\{\ell:A_\ell\}_{\ell\in L}$: the provider receives a client-selected label $\ell$, then continues as $A_\ell$;
- $A\otimes B$: the provider sends a channel of type $A$, then continues on the offered channel as $B$;
- $A\multimap B$: the provider receives a channel of type $A$, then continues on the offered channel as $B$.

$L$ is a finite label set; $\ell$ ranges over $L$; and $A_\ell$ is the branch-specific continuation. In $A\otimes B$ and $A\multimap B$, $A$ classifies the transmitted channel and $B$ classifies the continuing session. “Continue” means that the same offered channel now has residual type $B$.

Cut composes two compatible endpoints:

$$
\frac{\Delta\vdash P::(x:A)\qquad
      \Delta',x:A\vdash Q::(z:C)}
     {\Delta,\Delta'\vdash P\parallel_xQ::(z:C)}.
$$

$P$ provides $x:A$; $Q$ uses it; $\parallel_x$ denotes their parallel composition with $x$ private; $z:C$ is the externally provided result; and the disjoint contexts $\Delta$ and $\Delta'$ contain all other used channels. This rule makes matching protocol types a wiring condition.

Recursive equations provide unbounded sessions, for example

$$
\mathsf{meter}=\oplus\{\mathsf{pulse}:\mathsf{meter},\mathsf{stop}:1\}.
$$

The equation is equirecursive: unfolding $\mathsf{meter}$ is silent. It is guarded because a choice constructor is exposed before recurrence. Recursive processes may therefore emit arbitrarily many pulses or an infinite pulse trace; typing does not imply termination.

## 5. How to use/read it

Read a type from the provider's viewpoint, one outer connective at a time. Determine who sends next, consume that action, and replace the channel's type by its continuation. To read the client, reverse the role: it receives provider outputs and sends provider inputs.

For example, at $x:A\otimes B$, a provider that owns $w:A$ may execute $\mathsf{send}\ x\ w;P$. Afterward $w$ is absent from the provider's context and $P$ provides $x:B$. The receiving client binds the transmitted channel and gains its unique ownership. At $x:\&\{\mathsf{again}:A,\mathsf{done}:1\}$, by contrast, the provider waits; the client decides which label to send.

Typing is local but composition is global. Each process is checked against its own used/provided interface; cut then connects equal protocol types. During execution, private residual types evolve, while a well-typed network's external interface is intended to remain unchanged—a property developed formally as preservation after these lectures.

## 6. Worked example

Consider a one-item approval service carrying documents over channels of abstract protocol $D$:

$$
\mathsf{review}_D=
D\multimap
\&\{\mathsf{approve}:1,\mathsf{return}:D\otimes1\}.
$$

Step 1: the outer $D\multimap(-)$ tells the provider to receive a document channel. If the client owns $d:D$, it sends $d$ along service channel $r$. Ownership of $d$ moves to the provider, and $r$ advances to the external-choice type.

Step 2: because the residual outer connective is $\&$, the client sends either $\mathsf{approve}$ or $\mathsf{return}$. The provider must be prepared for both.

Step 3a: after $\mathsf{approve}$, the residual type is $1$. The provider sends $()$ and terminates. It must have consumed the document internally before closing; it cannot leave $d:D$ unused.

Step 3b: after $\mathsf{return}$, the residual type is $D\otimes1$. The provider sends the very document channel $d$, thereby giving ownership back to the client. It then sends $()$ on $r$.

A return trace is therefore:

$$
\text{client sends }d;quad
\text{client sends }\mathsf{return};quad
\text{provider sends }d;quad
\text{provider sends }().
$$

The type expresses direction, ordering, branch dependency, ownership transfer, and termination without choosing an implementation of document review.

## 7. Non-example or boundary case

The ordinary channel declaration “$r$ carries values of type $D$” is not a session type for this service. It does not say whether $D$ travels to or from the provider, whether it may return, or how the session closes.

A more subtle invalid case is a provider for $A\otimes B$ that sends $w:A$ and then also uses $w$ in its continuation. The action looks operationally plausible in an unrestricted language, but it cannot satisfy the linear right rule: $w$ must disappear from the sender's continuation context. Channel passing is transfer, not copying.

At another boundary, two clients cannot share the same endpoint merely because both follow the same label grammar. Binary linear sessions assume unique ownership. Multiparty or shared-session disciplines require additional logical machinery.

## 8. Key consequences

- **Protocol fidelity:** well-typed actions follow the direction and branch structure prescribed by the current connective.
- **Exact ownership:** a transmitted linear channel has one new owner, not an additional owner.
- **Compositional wiring:** cut connects a provider and client only at the same session proposition.
- **Stateful types:** the residual type records progress without mutating the external specification.
- **Dead-code pressure:** a terminating provider cannot hide unused linear resources, because $1R$ requires an empty used context.
- **Expressive recursion:** guarded recursive types finitely describe unbounded or infinite communication traces.

These are protocol and resource guarantees, not automatically fairness, termination, deadlock freedom for arbitrary extensions, or application-level correctness.

## 9. Relations to nearby concepts

[Cut Reduction as Process Execution](Cut%20Reduction%20as%20Process%20Execution.md) explains *how* compatible endpoints step once composed. The present concept is broader: it includes the typing correspondence and ownership discipline as well as reduction.

[Session Connectives and Channel Passing](Session%20Connectives%20and%20Channel%20Passing.md) focuses on the four choice/channel-direction connectives and on mobility. The present page also covers the overall proof/process correspondence, unit, recursion, and interface judgment.

[Lecture 5](../Lectures/Lecture%2005%20-%20Linear%20Message%20Passing%20I.md) develops cut, positive protocols, forwarding, and recursion. [Lecture 6](../Lectures/Lecture%2006%20-%20Linear%20Message%20Passing%20II.md) adds multiset dynamics, negative protocols, and channel transfer.

Session typing differs from an ordinary algebraic datatype interpretation. A datatype is commonly a value inspected in one place; a session proposition prescribes a distributed sequence of complementary actions at two endpoints. It also differs from generic linear typing: linearity says how often a resource is used, while the session connectives additionally say in which order and direction interactions occur.

## 10. Common mistakes

- Reading every type from the client's viewpoint rather than consistently starting with the provider.
- Calling $\oplus$ “external” because a label is externally visible; its technical name is internal choice because the provider chooses.
- Assuming send syntax always belongs to a provider; clients send at $\&$ and $\multimap$.
- Treating the antecedent $\Delta$ as a bag of optional dependencies.
- Forgetting that the type of a live channel advances after a message.
- Treating recursive type unfolding as an observable message.
- Concluding that well-typed recursion terminates.
- Treating channel transmission as duplication rather than ownership transfer.

## 11. What to remember

- Read every session proposition from the provider's viewpoint.
- A sequent has many linearly used channels but exactly one provided channel.
- Right and left rules give complementary provider/client behaviors.
- Cut creates private connectivity; reduction performs the communication.
- Residual types are protocol states, and sending a channel transfers ownership.

## 12. Source trail

- Lecture 5, sections 1-8, especially “Cut as Process Composition,” “Cut Reduction as Communication,” and “Communication and Polarity”; printed pages L5.1-L5.10; PDF pages 54-63.
- Lecture 6, sections 1-8, especially “Dynamics as Linear Inference,” “Sending Channels Along Channels,” “External Choice,” and “Linear Implication”; printed pages L6.1-L6.9; PDF pages 66-74.

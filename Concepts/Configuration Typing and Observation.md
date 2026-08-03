---
title: Configuration Typing and Observation
aliases:
  - Typed Process Configurations
  - Observable Session Results
tags:
  - session-types
  - configurations
  - observation
  - operational-semantics
source_lectures:
  - 7
prerequisites:
  - Process typing
  - Linear message passing
related:
  - Preservation and Progress
  - Session Subtyping
---

# Configuration Typing and Observation

## 1. One-sentence definition

**Configuration typing assigns a directed used/provided interface to a multiset of linear processes, while observation interacts with its exposed positive channels to reveal results message by message and stops when a negative input is required.**

## 2. Why the concept is needed

A single process judgment is insufficient once cut/spawn creates concurrent process objects. Runtime safety must track which fragment provides each channel, which later fragment uses it, which channels simply pass through, and which channels cross the boundary. A flat multiset alone records none of that dependency structure.

Even a typed final configuration is not a conventional fully formed value. In a synchronous language, it may consist of processes blocked while trying to communicate at external channels. Observation explains why this is a valid result and how an environment can progressively expose positive session structure.

## 3. Intuitive model

**Intuition.** Think of a configuration typing as a typed wiring diagram read from upstream providers to downstream clients. Its left edge lists sockets whose providers are elsewhere; its right edge lists sockets whose clients are elsewhere. Internal wires have one producer and one consumer. The typing derivation supplies a topological order for checking the wiring, although the runtime state itself is an unordered bag.

Observation plugs a temporary consumer into a right-edge output. It records the next emitted item and then follows the residual protocol. When the component instead waits for an input, passive inspection ends.

## 4. Formal core

Configurations have grammar

$$C ::= \mathsf{proc}(P)\mid C_1,C_2\mid\cdot.$$

$P$ ranges over process terms; $C,C_1,C_2$ over configurations; comma is associative and commutative; and $\cdot$ is the empty configuration. The typing judgment is

$$\Delta\vdash C::\Delta',$$

where $\Delta$ is the linear input interface used by $C$ and $\Delta'$ the output interface it provides. Each context is a finite collection of distinct channel assignments $a:A$, with $a$ a channel and $A$ its session type.

The rules are

$$
\frac{\Delta\vdash P::(a:A)}
{\Delta',\Delta\vdash\mathsf{proc}(P)::(\Delta',a:A)}
\;\mathsf{proc},
$$

$$
\frac{\Delta_0\vdash C_1::\Delta_1
\qquad
\Delta_1\vdash C_2::\Delta_2}
{\Delta_0\vdash C_1,C_2::\Delta_2}
\;\mathsf{join},
\qquad
\frac{}{\Delta\vdash\cdot::\Delta}
\;\mathsf{empty}.
$$

The premise $\Delta\vdash P::(a:A)$ says $P$ uses the channels in $\Delta$ and provides $a$. In `proc`, $\Delta'$ is a pass-through context: the process does not use those channels, so they remain available. `join` composes the first configuration’s output interface with the second’s input interface. `empty` changes nothing.

For an internal channel there must be exactly one provider and exactly one client. A left-interface channel may lack its provider inside $C$; a right-interface channel may lack its client. The typing order places a provider before its client, but independent process objects may be exchanged. Formally, if $P$ provides $a$ and the following $Q$ does not use $a$, their order in the configuration typing may be swapped. The condition is essential: swapping across an actual dependency would invalidate the intermediate interface.

A left-closed configuration has $\cdot\vdash C::\Delta$. It is final when every process is poised to send or receive along a channel in $\Delta$. Such processes have no internal peer and legitimately wait for the environment.

For positive types, the provider controls the next observable send:

- $\mathbf1$: unit closes the channel;
- $\oplus\{\ell:A_\ell\}$: a label reveals the selected continuation;
- $A\otimes B$: a channel is sent, and the original channel continues as $B$.

For negative types $\&\{\ell:A_\ell\}$ and $A\multimap B$, the provider awaits client input. Passive observation therefore stops rather than inventing an input.

## 5. How to use/read it

To type a runtime configuration, choose an order compatible with provider-to-client dependencies. Apply `proc` to each process, carrying unrelated channels through, and use `join` to match each intermediate interface. Different topological orders are equivalent when justified by exchange.

To read a final result, locate right-interface channels. If one has positive type, attach an observer that receives its next message. This external interaction may change that channel’s interface type to the corresponding continuation. Resume the process until it is final again, then repeat. If a negative type is reached, report an opaque waiting service rather than claiming to know how it responds to every possible input.

## 6. Worked example

Let

$$\mathsf{bit}=\oplus\{\mathsf{o}:\mathbf1,\mathsf{i}:\mathbf1\}.$$

Suppose $P$ provides $a:\mathsf{bit}$ without using any channel, and $Q$ independently provides $b:\mathbf1$. Their process typings are

$$\cdot\vdash P::(a:\mathsf{bit})
\qquad
\cdot\vdash Q::(b:\mathbf1).$$

First lift $P$ with no incoming or pass-through channels:

$$
\cdot\vdash\mathsf{proc}(P)::(a:\mathsf{bit}).
$$

Then lift $Q$ with $a$ passing through:

$$
a:\mathsf{bit}\vdash\mathsf{proc}(Q)::(a:\mathsf{bit},b:\mathbf1).
$$

The intermediate interface of the first judgment is the input interface of the second, so `join` yields

$$
\cdot\vdash\mathsf{proc}(P),\mathsf{proc}(Q)
::(a:\mathsf{bit},b:\mathbf1).
$$

Because neither process uses the other one's channel, exchange also validates the reverse process order; in that derivation, $b$ is the pass-through channel for $P$.

Assume the final $P$ is poised to send label `i` on $a$, and $Q$ is poised to send unit on $b$. The configuration cannot step internally, but it is final: both actions target right-interface channels.

An observer receives `i` on $a$. The observable interface entry advances from $a:\mathsf{bit}$ to $a:\mathbf1$. After $P$ exposes its closing unit, the observer consumes it. Independently it may consume the unit on $b$. The order of these observations does not matter because there is no channel dependency between the process objects.

## 7. Non-example or boundary case

The rule

$$
\frac{\Delta\vdash P::(a:A)}
{\Delta\vdash\mathsf{proc}(P)::(a:A)}
$$

is too weak as the general `proc` rule. If a channel $b:B$ was already available and $P$ did not use it, the conclusion discards $b$; a later client can no longer be typed. The pass-through context in the real rule prevents this loss.

Observation also has a deliberate boundary. Given a final provider at $a:A\multimap B$, there is no canonical passive message to record: the provider is waiting to receive an $A$ channel. Supplying one is an experiment with chosen input behavior, not mere observation of an already produced value.

## 8. Key consequences

- Configuration typing exposes a dependency order without imposing a scheduler order.
- Pass-through interfaces prevent unrelated linear resources from disappearing.
- Exactly-one-provider/exactly-one-client ownership is expressible across a whole runtime state.
- Exchange justifies bringing communicating peers together when no dependency is crossed.
- Final synchronous states are boundary-waiting states, not necessarily empty states.
- Positive observation is incremental and changes the observed interface to a continuation type.
- Negative providers are opaque until an environment actively supplies input.

## 9. Relations to nearby concepts

[Preservation and Progress](Preservation%20and%20Progress.md) quantify over configuration typings. Preservation keeps their outer interfaces fixed during internal steps; progress says a left-closed one reduces or is final. Configuration typing is the judgment those theorems protect.

[Session Subtyping](Session%20Subtyping.md) allows the provider and client views joined at an interface to differ safely. Configuration typing still records direction and ownership; subtyping changes the compatibility condition from equality to “every message understood.”

Process typing concerns one provider and its used channels. Configuration typing composes many such judgments and may provide many channels. Observation is neither typing nor reduction internal to the closed configuration: it models controlled interaction across the provided boundary.

## 10. Common mistakes

- Reading $\Delta\vdash C::\Delta'$ as a single-process judgment with one result.
- Treating configuration comma as ordered because `join` is directed.
- Swapping a provider past its own client under the exchange lemma.
- Omitting the pass-through context in `proc`.
- Calling every nonreducing configuration final without checking that actions use right-interface channels.
- Expecting a final session result to be fully present as a conventional value.
- Probing a negative service and calling the chosen experiment passive observation.

## 11. What to remember

- $\Delta\vdash C::\Delta'$ means “uses $\Delta$, provides $\Delta'$.”
- Runtime configurations are multisets; typing derivations follow provider-to-client dependencies.
- `proc` carries unrelated channels through, `join` composes interfaces, and `empty` is identity.
- Final means waiting only at the external provided boundary.
- Observe positive sessions one message at a time; stop at negative input.

## 12. Source trail

- Lecture 7, section 3 “Typing Configurations of Processes” and the exchange lemma.
- Lecture 7, section 5 “Progress” for left-closed configurations and finality.
- Lecture 7, sections 6 “Observation” and 7 “Refactoring the Dynamics” for positive/negative observation and uniform messages.
- Printed pages: L7.3–L7.10.
- PDF pages: 80–87.
- Full lecture reconstruction: [Lecture 7: Preservation and Progress](../Lectures/Lecture%2007%20-%20Preservation%20and%20Progress.md).

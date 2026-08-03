---
title: "Lecture 5: Linear Message Passing I"
lecture: 5
date: 2023-09-12
pdf_pages: "54-65"
printed_pages: "L5.1-L5.12"
tags:
  - linear-logic
  - message-passing
  - session-types
  - cut-reduction
prerequisites:
  - "Lecture 3: Cut and Identity Elimination"
  - "Lecture 4: Proof Terms"
---

# Lecture 5: Linear Message Passing I

## 1. Why this lecture exists

The earlier proof-theoretic development treated computation as the *construction* of a proof. This lecture changes the unit of computation: a completed proof is now a program, and reducing that proof executes the program. For intuitionistic linear logic in sequent-calculus form, this yields a disciplined language of communicating processes. A proposition describes the protocol on one channel, a proof is a process implementing that protocol, cut connects two processes, and cut reduction explains their interaction.

This shift is substantive. Linear use ensures that the two endpoints of a private channel have exactly one provider and one client; logical rules prescribe who sends next and what must follow; and the changing residual proposition records the state of the conversation. See [Linear Message Passing and Session Types](../Concepts/Linear%20Message%20Passing%20and%20Session%20Types.md) for the central correspondence and [Cut Reduction as Process Execution](../Concepts/Cut%20Reduction%20as%20Process%20Execution.md) for its dynamics.

## 2. Learning objectives

After this lecture, a reader should be able to:

- read a channel-annotated sequent as a process interface;
- explain why cut is parallel composition over a private linear channel;
- derive communication steps from principal and identity cut reductions;
- predict message direction from connective polarity;
- type finite internal choice and the unit protocol;
- explain forwarding, equirecursive protocol types, and guarded recursion;
- read the core MPASS constructs for spawning, sending, receiving, forwarding, and calling; and
- trace a binary-number pipeline while updating each channel's residual type.

## 3. Dependency map

Linear sequent calculus supplies the judgment and connective rules. Cut and identity elimination supply the reductions. Proof terms supply syntax attached to derivations. Lecture 5 combines these ingredients as follows:

$$
\text{linear proposition}
\longrightarrow \text{channel protocol},\qquad
\text{proof}
\longrightarrow \text{process},\qquad
\text{cut reduction}
\longrightarrow \text{execution}.
$$

Internal choice and unit are introduced first because both are positive: their providers initiate communication. Recursive definitions then make finite syntax describe unbounded protocols. Lecture 6 adds channel passing and negative connectives; Lecture 7 separates proof-normalization facts from programming-language safety theorems.

## 4. Section-by-section reconstruction covering every numbered heading

### 1. Introduction

The lecture contrasts two proof/computation correspondences. In proof search, the computation *builds* evidence and the result is a derivation or a yes/no answer. Under proofs-as-programs, the derivation already is the program and computation transforms it. Which programming model arises depends on both the logic and its proof system: changing resource discipline or proof calculus changes program shape and reduction.

The particular choice here is intuitionistic linear logic presented as a sequent calculus. Its propositions become communication protocols, historically connecting the proof-theoretic account to session types. Linear logic is chosen over ordered logic at this stage because exchange permits a broader class of process topologies: channels must be used exactly once according to their protocols, but their textual order is irrelevant.

### 2. Cut as Process Composition

The process typing judgment is

$$
x_1:A_1,\ldots,x_n:A_n \vdash P :: (x:A).
$$

It says that process $P$ *uses* the distinct channels $x_i$ according to protocols $A_i$ and *provides* the distinct channel $x$ according to $A$. The left side is a linear context: it is neither a reusable environment nor a list of optional inputs.

Cut connects a provider $P$ of $x:A$ to a client $Q$ that uses $x:A$:

$$
\frac{\Delta\vdash P::(x:A)\qquad
      \Delta',x:A\vdash Q::(z:C)}
     {\Delta,\Delta'\vdash P\parallel_x Q::(z:C)}\;\mathsf{cut}.
$$

$\Delta$ and $\Delta'$ are disjoint linear contexts; $z:C$ is the externally provided channel. The subscript on $\parallel_x$ makes $x$ private to the two components. Uniqueness of channel names and linear use rule out a third participant silently sharing that endpoint. Cut must remain computationally visible: removing all cuts before execution would also remove the compositions whose reductions constitute communication.

### 3. Cut Reduction as Communication

There are three proof-theoretic cut-reduction families. A **principal** reduction meets the right and left rules for the cut proposition; an **identity** reduction cancels a cut against identity; a **permuting** reduction moves a cut past an unrelated inference. Principal and identity reductions produce the operational steps emphasized here. Permutations express process equality or independence rather than a message event.

For $A\oplus B$, the provider selects one summand and the client must handle both. With $\pi_1$ and $\pi_2$ as branch labels:

$$
(\mathsf{send}\ x\ \pi_i;P_i)\parallel_x
\mathsf{recv}\ x(\pi_1\Rightarrow Q_1\mid\pi_2\Rightarrow Q_2)
\longrightarrow P_i\parallel_x Q_i,
$$

where $i\in\{1,2\}$. The selected branch is the communicated information. If $i=1$, the residual protocol of $x$ becomes $A$; if $i=2$, it becomes $B$. The external interface $\Delta,\Delta'\vdash z:C$ does not change.

### 4. Communication and Polarity

Polarity predicts who has information to transmit. A noninvertible rule embodies a choice; an invertible rule does not. Positive connectives are noninvertible on the right, so their provider sends and their client receives. The positive fragment considered here consists of internal choice $\oplus$, multiplicative unit $1$, and later tensor $\otimes$.

The protocol $1$ contains no payload branch, but it still has a synchronization event. A provider with no used channels sends the unit token $()$ and terminates; a client waits for that token before continuing:

$$
\mathsf{send}\ x\ ()\parallel_x
\mathsf{recv}\ x(()\Rightarrow Q)\longrightarrow Q.
$$

The empty context in the $1R$ rule matters. A process cannot claim to have finished while silently abandoning linear resources.

### 5. An Example: Booleans

The type $\mathsf{bool}=1\oplus1$ admits exactly two terminating protocol traces: choose the left label and close, or choose the right label and close. A client such as Boolean negation receives either label, consumes the subsequent unit token, sends the opposite label on its result channel, and closes that result.

Logically, a proof of $1\oplus1\vdash1\oplus1$ is modest. Operationally, its ordering of receives and sends is an executable transducer. This illustrates the changed viewpoint: proof evidence is inspected for validity, whereas a process is observed through the messages permitted at its boundary.

### 6. Another Example: Natural Numbers

Finite nested sums describe only bounded numerals. Recursion gives the unbounded protocol

$$
\mathsf{nat}=\oplus\{\mathsf{zero}:1,\ \mathsf{succ}:\mathsf{nat}\}.
$$

The notation $\oplus\{\ell:A_\ell\}_{\ell\in L}$ is finite labeled internal choice: $L$ is a finite label set, $\ell$ is one label, and $A_\ell$ is the continuation after that label. A numeral is a finite sequence of $\mathsf{succ}$ labels followed by $\mathsf{zero}$ and the closing unit.

Identity receives an operational name, forwarding:

$$
x:A\vdash \mathsf{fwd}\ y\ x::(y:A).
$$

It connects the client side of one channel to the provider side of another without inspecting $A$. Cutting against it only renames the live endpoint:

$$
P(x)\parallel_x\mathsf{fwd}\ y\ x\longrightarrow P(y),
\qquad
\mathsf{fwd}\ x\ y\parallel_x Q(x)\longrightarrow Q(y).
$$

Recursive protocol equations are **equirecursive**: replacing a type name by its definition emits no message. Operationally they receive a coinductive reading because a recursive process may continue forever. Definitions must therefore be guarded by a protocol constructor. The equation $T=T$ is rejected because it reveals no next action; $T=\oplus\{\mathsf{tick}:T\}$ is guarded and specifies an indefinitely repeatable label stream.

### 7. MPASS Syntax

MPASS gives concrete syntax to the proof terms. A top-level type declaration may be recursive or mutually recursive. A process declaration names its provided channel first and its used channels afterward. Labels are syntactically marked so they cannot be confused with type, process, or channel names.

The key forms introduced by this point are: send a label; receive and branch on a label; send unit; receive unit; forward; spawn a provider on a fresh channel; and call a named process. Calls permit process recursion and go beyond finite linear-logic derivations, even though each body is checked with linear typing.

### 8. Example: Natural Numbers in Binary Form

A binary-natural protocol sends the least significant bit first and ends with an end marker followed by unit:

$$
\mathsf{bin}=\oplus\{\mathsf{b0}:\mathsf{bin},
\mathsf{b1}:\mathsf{bin},\mathsf{end}:1\}.
$$

A successor transducer reacts locally: on bit $0$ it emits $1$ and forwards the remaining channel; on bit $1$ it emits $0$ and recursively propagates a carry; at the end marker it creates a final $1$ before closing. Least-significant-bit-first order is what makes carry propagation follow the incoming message order.

Abstract spawn syntax is typed by cut:

$$
\frac{\Delta\vdash P(x)::(x:A)\qquad
      \Delta',x:A\vdash Q(x)::(z:C)}
     {\Delta,\Delta'\vdash x^A\leftarrow P(x);Q(x)::(z:C)}.
$$

At runtime it allocates a globally fresh channel $a$, starts $P(a)$, and continues with $Q(a)$:

$$
x^A\leftarrow P(x);Q(x)\longrightarrow P(a)\parallel_a Q(a).
$$

This is process creation, not communication: no two existing endpoints synchronize in this step. A succession of spawned successor processes can form a concurrent pipeline, with each stage consuming and producing a linear bit stream.

### 9. Summary

The lecture establishes the message-passing interpretation for cut, identity, internal choice, and unit, then adds guarded recursive types and recursive process calls. Even this small positive fragment expresses Boolean transducers, unary numbers, bit streams, and pipelined binary arithmetic. Lecture 6 completes the core statics and dynamics with finite choice, channel passing, external choice, and linear implication.

## 5. Formal core (rules/judgments/theorems, with each symbol explained)

The central judgment is $\Delta\vdash P::(x:A)$. Here $\Delta$ is a finite unordered linear context of distinct declarations $y:B$; $P$ is a process term; $x$ is the unique channel provided by $P$; and $A,B$ are session propositions. The empty context is $\cdot$. All channels appearing in a rule are assumed distinct except where an endpoint is deliberately connected.

For labeled internal choice:

$$
\frac{\Delta\vdash P::(x:A_k)\quad k\in L}
     {\Delta\vdash \mathsf{send}\ x\ k;P::
      (x:\oplus\{\ell:A_\ell\}_{\ell\in L})}\;\oplus R
$$

$$
\frac{\Delta,x:A_\ell\vdash Q_\ell::(z:C)
      \quad\text{for every }\ell\in L}
     {\Delta,x:\oplus\{\ell:A_\ell\}_{\ell\in L}
      \vdash \mathsf{recv}\ x(\ell\Rightarrow Q_\ell)_{\ell\in L}::(z:C)}
      \;\oplus L.
$$

$L$ is the finite set of legal labels, $k$ is the provider's selected member, and $Q_\ell$ is the client's continuation for label $\ell$. The continuation uses the same channel $x$, but at the residual type $A_\ell$.

For unit:

$$
\frac{}{\cdot\vdash \mathsf{send}\ x\ ()::(x:1)}\;1R
\qquad
\frac{\Delta\vdash Q::(z:C)}
     {\Delta,x:1\vdash \mathsf{recv}\ x(()\Rightarrow Q)::(z:C)}\;1L.
$$

$()$ is the unique unit message, not an arbitrary value. The $1R$ process has no continuation because its protocol is complete. Cut and identity are as stated above; they apply uniformly to every protocol $A$.

## 6. Operational/computational reading

A type is a state machine whose current state is the residual proposition on a channel. A positive connective puts the provider in control of the next observable action. Communication consumes matching send/receive prefixes atomically and exposes both continuations. Linearity makes this local rule sufficient: the synchronized endpoints cannot also be owned elsewhere.

Spawn has a different role. It makes a fresh private name and adds a provider-client pair to the running configuration. Forwarding rewires endpoints and preserves the protocol without synthesizing a message. Recursive calls unfold process definitions, while equirecursive type names unfold silently during type checking. Divergence is therefore possible; typing controls communication shape and resource use, not termination.

## 7. Worked derivation or trace in original notation and prose

Consider an original three-state indicator protocol:

$$
\mathsf{signal}=\oplus\{\mathsf{red}:1,\mathsf{amber}:1,\mathsf{green}:1\}.
$$

Let a provider choose $\mathsf{amber}$ on $s$, and let a client translate that choice to a two-way alert on $t$:

$$
\mathsf{alert}=\oplus\{\mathsf{stop}:1,\mathsf{go}:1\}.
$$

The provider has type

$$
\cdot\vdash
\mathsf{send}\ s\ \mathsf{amber};\mathsf{send}\ s\ ()
::(s:\mathsf{signal}).
$$

The client's amber branch first receives the close on $s$, then sends $\mathsf{stop}$ and closes $t$. Its other two branches are also present so the client is total over the advertised label set. Cutting them together yields these principal steps:

$$
\begin{aligned}
&(\mathsf{send}\ s\ \mathsf{amber};\mathsf{send}\ s\ ())
\parallel_s
\mathsf{recv}\ s(\mathsf{red}\Rightarrow Q_r\mid
\mathsf{amber}\Rightarrow Q_a\mid
\mathsf{green}\Rightarrow Q_g)\\
&\quad\longrightarrow
\mathsf{send}\ s\ ()\parallel_s Q_a\\
&\quad\longrightarrow
\mathsf{send}\ t\ \mathsf{stop};\mathsf{send}\ t\ ().
\end{aligned}
$$

After the first step, $s$ changes from $\mathsf{signal}$ to $1$. After the second, $s$ disappears because its protocol is finished. Throughout, the externally visible result channel retains type $t:\mathsf{alert}$. An omitted green branch would not be a stuck-but-well-typed alternative; it would make the client untypable by $\oplus L$.

## 8. Conceptual synthesis

Three ideas reinforce one another. First, propositions classify complete conversations rather than one-shot payloads. Second, cut creates the private wiring along which dual proof rules meet. Third, reduction updates the local protocol while preserving the external interface. The result is a process calculus extracted from proof theory rather than a process calculus merely decorated with types.

The correspondence is not an assertion that programs and proofs have identical purposes. Recursion permits nontermination, observation hides internal structure, and permuting conversions are better read as process equalities. Those distinctions become explicit in later safety and equivalence results.

## 9. Common confusions and failure modes

- **Treating $\Delta$ as reusable.** It is linear: every listed channel must be consumed exactly according to its protocol.
- **Reading $\oplus$ as client choice.** For internal choice, the provider sends the chosen label; the client receives and covers every label.
- **Forgetting the unit message.** Choosing a branch of type $1$ does not itself close the channel; the $()$ synchronization remains.
- **Equating spawn with communication.** Spawn allocates and schedules; a send/receive pair communicates.
- **Assuming the type of a channel variable is fixed.** Its residual session type advances after each action, while the external interface remains stable across a reduction.
- **Calling forwarding a copy.** It aliases two endpoints by rewiring; it does not duplicate a linear channel or its messages.
- **Accepting unguarded recursive types.** $T=T$ offers no observable constructor and is not a valid finite description of a protocol.
- **Inferring termination from typing.** Recursive processes may produce infinite traces or diverge.

## 10. Self-test questions with concise answers

1. **Why is cut primitive in the process language?** Because its reduction supplies process composition and execution; a cut-free term would contain no such interaction point.
2. **Who chooses a branch of $A\oplus B$?** The provider, using the right rule.
3. **What does $x:A$ left of $\vdash$ mean?** The process is the client/user of channel $x$ at protocol $A$.
4. **Why must $1R$ have an empty context?** A terminating provider may not discard unused linear channels.
5. **What remains invariant in a communication step?** The externally typed interface; the private channel's residual type may change.
6. **Does unfolding an equirecursive type send a message?** No; only its revealed outer constructor determines the next message.
7. **What is the operational content of identity?** Forwarding one channel endpoint to another.
8. **Can a well-typed recursive process diverge?** Yes; session typing constrains interactions, not termination.

## 11. Related concept pages

- [Linear Message Passing and Session Types](../Concepts/Linear%20Message%20Passing%20and%20Session%20Types.md)
- [Cut Reduction as Process Execution](../Concepts/Cut%20Reduction%20as%20Process%20Execution.md)
- [Session Connectives and Channel Passing](../Concepts/Session%20Connectives%20and%20Channel%20Passing.md)
- [Lecture 6: Linear Message Passing II](Lecture%2006%20-%20Linear%20Message%20Passing%20II.md)

## 12. Source trail (lecture, numbered sections, printed-page range, PDF-page range)

- Frank Pfenning, *Linear Message Passing I*, Lecture 5, September 12, 2023.
- Numbered sections covered: 1 “Introduction”; 2 “Cut as Process Composition”; 3 “Cut Reduction as Communication”; 4 “Communication and Polarity”; 5 “An Example: Booleans”; 6 “Another Example: Natural Numbers”; 7 “MPASS Syntax”; 8 “Example: Natural Numbers in Binary Form”; 9 “Summary.”
- Printed pages: L5.1-L5.12.
- PDF pages: 54-65.

## 13. Previous/next navigation

Previous: Lecture 4, *Proof Terms* (not yet authored in this repository).

Next: [Lecture 6: Linear Message Passing II](Lecture%2006%20-%20Linear%20Message%20Passing%20II.md).

---
title: Semi-Axiomatic Sequent Calculus and SAX
aliases: [SAX, semi-axiomatic calculus]
tags: [sax, sequent-calculus, asynchronous-communication, lecture-14]
source_lectures: ["Lecture 14 - Semi-Axiomatic Sequent Calculus"]
prerequisites: [Positive vs Negative Polarity, cut and identity, session types]
related: [Continuation Channels, Cut Elimination for SAX, Adjoint SAX Message Sequences and Pattern Matching]
---

# Semi-Axiomatic Sequent Calculus and SAX

## One-sentence definition

**SAX is a semi-axiomatic sequent calculus that replaces each information-carrying noninvertible rule by an axiom while retaining invertible rules, yielding a proof theory for asynchronous messages.**

## Why the concept is needed

In the ordinary session interpretation of sequent calculus, sending and receiving advance together because a principal cut reduction retains continuations from both premises. Real implementations often use nonblocking sends. Simply deleting a sender continuation loses protocol order. SAX makes a sent message a complete process and transfers the rest of the protocol to an explicit continuation channel; its proof rules explain why this asynchronous representation remains typed and expressively equivalent to sequent calculus.

## Intuitive model

**Intuition.** Ordinary sequent calculus describes a conversation step with both speakers present. SAX lets the sender leave a typed note. The note contains the address for the next note, so the receiver can follow the protocol in order even if several notes already exist.

## Formal core

Let $\Delta$ be a linear multiset of assumptions and $A,B,C$ propositions. For positive sum, SAX replaces right rules by axioms:

$$A\vdash A\oplus B\;\oplus X_1
\qquad
B\vdash A\oplus B\;\oplus X_2,$$

while retaining the invertible left rule

$$
\frac{\Delta,A\vdash C\quad\Delta,B\vdash C}
{\Delta,A\oplus B\vdash C}\;\oplus L.
$$

For negative implication, the right rule remains

$$\frac{\Delta,A\vdash B}{\Delta\vdash A\multimap B}\;\multimap R,$$

while the information-carrying left rule becomes $A,A\multimap B\vdash B\;\multimap X$. Identity and cut remain available. Positive tensor and unit similarly get $\otimes X$ and $1X$; negative additive conjunction gets projection axioms.

| System | Information rules | Invertible rules | Identity/cut role | Process reading |
|---|---|---|---|---|
| Sequent calculus | Ordinary rules with premises | Ordinary rules | Identity and cut normalize away | Synchronous send/receive with continuations |
| Semi-axiomatic calculus | Positive-right and negative-left rules become axioms | Retained | Cut needed to compose axioms into larger proofs | Abstract asynchronous proof calculus |
| SAX process calculus | Axioms annotated as `send x M` | Rules annotated as `recv x K` | Cut allocates/connects; identity forwards | Nonblocking messages with continuation channels |

Soundness and completeness say $\Delta\vdash A$ is derivable in sequent calculus iff it is derivable in SAX. SAX axioms expand by identity plus ordinary rules; ordinary information rules expand in SAX by a message axiom plus cut.

## How to use/read it

Classify the principal connective by polarity. If its information-carrying side is used, produce a SAX axiom/message; if its invertible side is used, retain a rule/receiver. Use cut to allocate the continuation channel and connect the message to the rest of a proof. A send process has no continuation process syntactically—the continuation is named inside its message.

## Worked example

Build a message of type $A\oplus B$ from a proof $D:\Delta\vdash A$.

1. SAX supplies the axiom $A\vdash A\oplus B$ via $\oplus X_1$.
2. Cut $D$ against that axiom on formula $A$.
3. Obtain $\Delta\vdash A\oplus B$.
4. Under process assignment, allocate fresh $x':A$ for the proof $D$.
5. Send label `left` on result channel $x$ with continuation channel $x'$.
6. The receiver on $x$ consumes the label and continues on $x'$; the original $x$ never changes type.

This reproduces ordinary $\oplus R_1$ but isolates the message as an axiom.

## Non-example or boundary case

Removing a sender continuation without adding a continuation channel is unsafe. For a binary stream, messages `b1`, `e`, and unit could race on the same address; the receiver might consume `e` or unit before `b1`, causing an immediate or later type mismatch. SAX does not claim that unordered messages become ordered by linearity alone—the pointer chain enforces order.

Traditional cut elimination also fails: for distinct atoms $P,Q,R$, $Q\vdash(P\oplus Q)\oplus R$ is derivable but cannot start with a SAX axiom or invertible rule. An analytic composition is necessary.

## Key consequences

SAX and sequent calculus prove the same sequents, but they have different normal forms. Message reception removes the cut and leaves only the recipient process. Continuation channels make asynchronous communication type safe and form a linked queue. The calculus generalizes naturally to adjoint modes because shared senders need not synchronize simultaneously with all clients.

## Relations to nearby concepts

[Continuation Channels](Continuation%20Channels.md) explains the pointer discipline. [Cut Elimination for SAX](Cut%20Elimination%20for%20SAX.md) replaces full cut elimination with reduction to snips. [Positive vs Negative Polarity](../Comparisons/Positive%20vs%20Negative%20Polarity.md) determines which half becomes axiomatic. [Adjoint SAX, Message Sequences, and Pattern Matching](Adjoint%20SAX%2C%20Message%20Sequences%2C%20and%20Pattern%20Matching.md) adds modes and compact message sequences.

## Common mistakes

- Saying SAX deletes half the logic; it replaces half the rules with axioms.
- Treating a continuation channel as a continuation process.
- Assuming equivalence of provability implies identical cut-free proofs.
- Calling `send` blocking because its matching receive appears in a reduction rule.

## What to remember

- Information rules become message axioms; invertible rules remain receivers.
- Sends carry continuation channels.
- SAX and sequent calculus are sound and complete for each other.
- Cut remains essential in SAX normal forms.
- Asynchrony preserves order through channel chains.

## Source trail

Lecture 14, “Semi-Axiomatic Sequent Calculus,” §§1–9, printed lecture pages L14.1–L14.10, PDF pages 148–157. See [Lecture 14 - Semi-Axiomatic Sequent Calculus](../Lectures/Lecture%2014%20-%20Semi-Axiomatic%20Sequent%20Calculus.md).

---
title: "Lecture 14 - Semi-Axiomatic Sequent Calculus"
lecture: 14
date: 2023-10-26
pdf_pages: "148-158"
printed_pages: "L14.1-L14.11"
tags:
  - lecture
  - sax
  - sequent-calculus
  - asynchronous-message-passing
  - session-types
prerequisites:
  - "Linear sequent calculus"
  - "Session types and MPASS"
  - "Positive and negative polarity"
---

# Lecture 14 - Semi-Axiomatic Sequent Calculus

## 1. Why this lecture exists

The message-passing interpretation of ordinary linear sequent calculus is synchronous: a sender and receiver both advance when their communication reduces. Real systems usually offer nonblocking sends and blocking receives. Simply allowing senders to run ahead is unsound because several messages on the same channel can arrive out of protocol order.

This lecture derives a disciplined asynchronous calculus from proof theory. Every message carries a fresh continuation channel. The rules that transmit information—the noninvertible positive right and negative left rules—become axioms, while invertible rules remain ordinary inference rules. This is the **semi-axiomatic sequent calculus**, or SAX. SAX proves the same sequents as ordinary sequent calculus, but it does not enjoy traditional cut elimination: a restricted family of analytic cuts, called **snips**, may be essential.

The logical change has a precise operational payoff. A send is a closed message process and does not carry a continuation process; the receiver alone resumes after consuming it. Continuation channels preserve protocol order and form linked queues of asynchronous messages.

## 2. Learning objectives

After this lecture, you should be able to:

1. locate the source of synchronous communication in principal cut reduction;
2. explain why continuation processes cannot simply be discarded;
3. derive SAX's message axioms from connective polarity;
4. translate derivations between ordinary sequent calculus and SAX;
5. distinguish full cuts, analytic cuts, and snips;
6. state the SAX process typing rules and reduction semantics; and
7. trace how continuation channels implement an ordered asynchronous queue.

## 3. Dependency map

$$
\text{linear sequent calculus}
\longrightarrow \text{synchronous cut reduction}
\longrightarrow \text{MPASS communication},
$$

while the new path is

$$
\text{polarity}
\longrightarrow \text{information-carrying rules become axioms}
\longrightarrow \text{SAX}
\longrightarrow \text{asynchronous messages with continuation channels}.
$$

Equivalence with ordinary sequent calculus uses [identity and cut admissibility](<../Concepts/Identity and Cut Admissibility.md>): identity supports the SAX-to-sequent direction and cut the sequent-to-SAX direction. The latter dependency explains why restricted cuts remain in [cut elimination for SAX](<../Concepts/Cut Elimination for SAX.md>).

## 4. Section-by-section reconstruction

### 1 Introduction

MPASS interprets linear propositions as session types, but its send and receive processes synchronize. An asynchronous formulation is closer to implementation and reveals a connection to futures, normally presented as shared-memory concurrency. Although untyped synchronous and asynchronous $\pi$-calculi differ in expressive power, the session-typed setting can recover the same expressiveness. The asynchronous formulation is also a better route from purely linear communication to structural and general adjoint types.

### 2 The Origin of Synchronous Communication

For an internal choice $\oplus\{\ell:A_\ell\}_{\ell\in L}$, the provider selects $k\in L$. In MPASS, the right rule types `send x k; P`, where the same channel $x$ continues at type $A_k$. The left rule types a receiver with one continuation $Q_\ell$ for every label. Their dynamics is

$$
\mathsf{proc}(\mathsf{send}\ a\ k;P),
\mathsf{proc}(\mathsf{recv}\ a\ (\ell\Rightarrow Q_\ell)_{\ell\in L})
\longrightarrow
\mathsf{proc}(P),\mathsf{proc}(Q_k).
$$

Both continuations advance at once. Proof-theoretically, the corresponding principal cut between $\oplus R_k$ and $\oplus L$ becomes a smaller cut between the selected right premise and the matching left premise. Because both subderivations remain, synchronization is inherited directly from cut reduction.

### 3 Continuation Channels instead of Continuation Processes

Removing the sender continuation $P$ does not by itself yield a safe asynchronous calculus. If a process sends the representation of binary one as label `b1`, then label `e`, then unit, three independent messages on the same address could race with one receiver. The receiver might consume `e` before `b1`, or even see unit where it expects a label. Progress fails because protocol order is no longer represented.

The repair is to put a continuation channel in every non-unit message:

$$
\mathsf{send}\ x\ k(x').
$$

The original address $x$ is used exactly once for this message. Subsequent protocol actions use $x'$, then its continuation $x''$, and so on. A receiver for $x$ obtains $x'$ in the selected branch. The SAX rule is an axiom:

$$
\frac{k\in L}{x':A_k\vdash
\mathsf{send}\ x\ k(x')::(x:\oplus\{\ell:A_\ell\}_{\ell\in L})}
\;\oplus X.
$$

There is no continuation process premise. The left rule remains a case analysis, with $x'$ replacing $x$ in each branch. Reduction transfers communication from $a$ to the supplied continuation $a'$:

$$
\mathsf{proc}(\mathsf{send}\ a\ k(a')),
\mathsf{proc}(\mathsf{recv}\ a\ (\ell(x')\Rightarrow Q_\ell(x'))_{\ell\in L})
\longrightarrow
\mathsf{proc}(Q_k(a')).
$$

Only the recipient continues. The message is consumed.

### 4 Back to Logic

Erasing process syntax leaves binary sum axioms

$$
A\vdash A\oplus B\;(\oplus X_1)
\qquad
B\vdash A\oplus B\;(\oplus X_2)
$$

and the usual invertible $\oplus L$. Cutting either axiom against $\oplus L$ selects the matching premise and eliminates the cut completely. Channel-name substitution is implicit in the propositional presentation: the continuation named in the message replaces the branch variable bound by the receiver.

This is the logical signature of asynchronous receipt. Unlike the sequent-calculus principal reduction, no sender continuation remains.

### 5 Generalizing to Other Connectives

Polarity determines which rules carry information. For positive connectives, noninvertible right rules become message axioms and invertible left rules remain:

$$
A,B\vdash A\otimes B\;(\otimes X),
\qquad
\cdot\vdash1\;(1X),
$$

with the usual $\otimes L$ and $1L$. Unit right was already premise-free; renaming it emphasizes its message role.

Negative connectives are symmetric: noninvertible left rules become axioms while invertible right rules remain. For negative conjunction $A\mathbin{\&}B$ (written $A\mathbin N B$ in the source),

$$
A\mathbin{\&}B\vdash A\;(\&X_1),
\qquad
A\mathbin{\&}B\vdash B\;(\&X_2),
$$

while $\&R$ still has two premises. For linear implication,

$$
A,A\multimap B\vdash B\;(\multimap X),
$$

while $\multimap R$ remains. Identity and cut retain their ordinary forms.

“Semi-axiomatic” therefore means that the information-bearing half of the introduction/elimination structure is collapsed into axioms. It does not mean that half of all written rules, counted syntactically, are axioms.

### 6 Relating Sequent Calculus to SAX

SAX is sound and complete with respect to ordinary sequent calculus:

> **Theorem 1 (Soundness and Completeness of SAX).** A sequent $\Delta\vdash A$ is derivable in ordinary sequent calculus if and only if it is derivable in SAX.

For SAX-to-sequent translation, derive each new axiom using ordinary identity followed by the corresponding noninvertible rule. For example, $A\vdash A\oplus B$ follows from $A\vdash A$ by $\oplus R_1$; $A,A\multimap B\vdash B$ follows from identities on $A$ and $B$ by $\multimap L$.

For sequent-to-SAX translation, simulate each removed ordinary rule by cutting its premise against the appropriate SAX axiom. Thus ordinary $\oplus R_1$ is a cut of $\Delta\vdash A$ against $A\vdash A\oplus B$. Ordinary $\multimap L$ uses the implication axiom and two cuts, one connecting the proof of $A$ and one continuing from $B$.

The theorem concerns which sequents are provable. It does not say that derivations have the same normal forms or operational behavior.

### 7 Cut Elimination for SAX

Traditional cut elimination fails. For distinct atoms $P,Q,R$, the sequent

$$
Q\vdash(P\oplus Q)\oplus R
$$

has an ordinary cut-free derivation using two sum-right introductions. In SAX it is neither identity nor a single message axiom, and no logical rule applies at the outer positive succedent. A cut is necessary to compose the inner and outer message axioms.

The required cuts are analytic: their cut formulas are subformulas of the endsequent. SAX uses an even narrower class called **snips**, where one premise is an axiom or another snip. A precise inductive definition is postponed in the source, so this guide does not invent one.

All non-snip cuts can nevertheless be eliminated indirectly: translate the SAX derivation to ordinary sequent calculus, eliminate cut there, and translate the cut-free result back. The back-translation inserts only snips. A direct SAX reduction algorithm can likewise remove general cuts while leaving snips, preserving the connection between proof reduction and computation.

### 8 Completing Process Assignment and Dynamics

SAX process typing adds continuation channels uniformly.

For positive types, send axioms construct messages and left rules receive them:

$$
x':A_k\vdash\mathsf{send}\ x\ k(x')::(x:\oplus\{\ell:A_\ell\}_{\ell\in L}),
$$

$$
y:A,x':B\vdash\mathsf{send}\ x\ (y,x')::(x:A\otimes B),
$$

$$
\cdot\vdash\mathsf{send}\ x\ ()::(x:1).
$$

For negative types, providers receive and clients send messages:

$$
\Delta\vdash
\mathsf{recv}\ x\ (\ell(x')\Rightarrow P_\ell(x'))_{\ell\in L}
::(x:\mathbin{\&}\{\ell:A_\ell\}_{\ell\in L}),
$$

$$
x:\mathbin{\&}\{\ell:A_\ell\}_{\ell\in L}
\vdash\mathsf{send}\ x\ k(x')::(x':A_k),
$$

$$
\Delta\vdash\mathsf{recv}\ x\ ((y,x')\Rightarrow P(y,x'))::(x:A\multimap B),
$$

$$
y:A,x:A\multimap B\vdash\mathsf{send}\ x\ (y,x')::(x':B).
$$

The process language has messages $M$, continuations $K$, and processes $P$:

$$
\begin{aligned}
M &::= k(x')\mid(y,x')\mid(),\\
P &::= x\leftarrow P(x);Q(x)\mid\mathsf{fwd}\ x\ y
\mid\mathsf{send}\ x\ M\mid\mathsf{recv}\ x\ K
\mid\mathsf{call}\ p\ x\ y_1\cdots y_n.
\end{aligned}
$$

The operation $M\triangleright K$ matches a message against a continuation: a label selects its branch, a pair substitutes both received channels, and unit selects the unique unit continuation. Dynamics includes:

$$
\mathsf{proc}(x\leftarrow P(x);Q(x))
\longrightarrow\mathsf{proc}(P(a)),\mathsf{proc}(Q(a))
\quad(a\text{ fresh}),
$$

$$
\mathsf{proc}(P(b)),\mathsf{proc}(\mathsf{fwd}\ a\ b)
\longrightarrow\mathsf{proc}(P(a)),
$$

$$
\mathsf{proc}(\mathsf{send}\ a\ M),\mathsf{proc}(\mathsf{recv}\ a\ K)
\longrightarrow\mathsf{proc}(M\triangleright K),
$$

plus unfolding of a process definition from the global signature $\Sigma$.

### 9 Example Revisited

A SAX producer for binary one must allocate its continuation channels explicitly. With

$$
\mathsf{bin}=\oplus\{\mathsf{b0}:\mathsf{bin},
\mathsf{b1}:\mathsf{bin},\mathsf e:1\},
$$

the process creates the unit message first, then the `e` message pointing to it, then the `b1` message pointing to that. Textual order is reversed because ordinary cut binds the provider before the client:

```text
one(x) = x'' <- send x'' ();
         x'  <- send x' e(x'');
         send x b1(x')
```

Concurrency makes the allocation order operationally unimportant. The resulting configuration contains three independent message processes linked as
$x\to x'\to x''$. This is a queue whose pointers are typed continuation channels.

A reverse-cut syntax can put the client text before the provider text and recover a more familiar surface order without changing the logic. A second future direction is to compute continuation addresses from the original address; that idea corresponds to snips and is only sketched here.

## 5. Formal core

### Logical vocabulary

- $A,B,C$ are linear propositions.
- $\Delta,\Delta'$ are exchangeable linear contexts; every entry must be used exactly once.
- $\oplus$ and $\otimes$ are positive; $1$ is the positive unit.
- $\mathbin{\&}$ and $\multimap$ are negative.
- A rule name ending in $X$ denotes a SAX axiom produced from a noninvertible rule.
- $\Delta\vdash A$ is an unannotated logical sequent.
- $\Delta\vdash P::(x:A)$ says process $P$ uses exactly the channels in $\Delta$ and provides along $x$ according to session type $A$.

### Process vocabulary

- $x$ is the current communication channel; $x'$ is its continuation channel.
- $y$ is a payload channel.
- $M$ is a message, $K$ a receiver continuation, and $P,Q$ processes.
- $\mathsf{proc}(P)$ is a process in a runtime multiset configuration.
- $\Sigma$ is a global signature of possibly recursive type and process definitions.
- $M\triangleright K$ is defined only for a message and continuation of matching shape and label.
- `fwd x y` identifies two channels at the identity type.
- `x <- P(x); Q(x)` is cut: allocate fresh $x$, run provider $P$ and client $Q$ concurrently.

### Equivalence and normalization claims

Provability equivalence is a theorem proved by mutual rule simulation. Traditional cut elimination is false for SAX. The valid weaker claim is elimination of non-snip cuts, indirectly through ordinary sequent calculus or directly by SAX reductions. A snip is not “an arbitrary cut we decided to keep”; its analyticity and axiom/snipping-premise restriction are essential.

## 6. Operational/computational reading

A SAX axiom is a message. It contains exactly the channels needed to describe the next protocol state and has no process continuation. Sending therefore does not block. An unchanged invertible rule is a receiver: it waits until a matching message exists, then continues.

Positive and negative types reverse provider/client roles:

- for a positive type, the provider sends and the client receives;
- for a negative type, the provider receives and the client sends.

Continuation channels enforce FIFO-like protocol order without a primitive mutable queue. They are logical addresses linking one message cell to the next. This encoding distinguishes a channel's stable protocol identity from the succession of concrete addresses used by the core calculus.

## 7. Worked derivation or trace in original notation and prose

Take

$$
\mathsf{bit}=\oplus\{\mathsf{zero}:1,\mathsf{one}:1\}.
$$

Construct a message representing `one` followed by its unit continuation.

1. By $1X$,
   $$\cdot\vdash\mathsf{send}\ a'\ ()::(a':1).$$
2. By $\oplus X_{\mathsf{one}}$,
   $$a':1\vdash\mathsf{send}\ a\ \mathsf{one}(a')::(a:\mathsf{bit}).$$
3. Cut these processes:
   ```text
   a' <- send a' ();
         send a one(a')
   ```
   Runtime allocation produces a fresh address $b$ and two processes:
   $$
   \mathsf{proc}(\mathsf{send}\ b\ ()),
   \mathsf{proc}(\mathsf{send}\ a\ \mathsf{one}(b)).
   $$
4. Place beside them a receiver
   ```text
   recv a (zero(u) => Z(u) | one(u) => O(u))
   ```
   The message match reduces only the receiver:
   $$
   \mathsf{send}\ a\ \mathsf{one}(b)\triangleright K=O(b).
   $$
5. If $O(b)$ next receives unit on $b$, it synchronizes with the already available unit message. The two sends did not have to wait, but the continuation link forced `one` to be observed before unit.

Boundary case: if one instead emitted both messages on $a$, the unit could race with the label receiver and $M\triangleright K$ would be undefined. This is exactly the progress failure continuation channels prevent.

## 8. Conceptual synthesis

SAX relocates sequentiality. Ordinary sequent calculus keeps protocol order inside a continuation process; SAX externalizes it into a chain of typed addresses. The proof system and runtime remain aligned because the message-bearing, noninvertible rules become axioms, while the receiving, invertible rules retain premises.

The cost is equally revealing. Since a sequence of introductions is now a sequence of axioms, composing them requires analytic cuts. Snips are thus not a blemish unrelated to asynchrony; they are the proof-theoretic counterpart of chaining message fragments.

## 9. Common confusions and failure modes

- **“Asynchronous means messages may be received in any protocol order.”** Sends may proceed independently, but continuation channels constrain which address the next receive uses.
- **“Drop the sender continuation and keep the same channel.”** That creates races among differently shaped messages and breaks progress.
- **“An $X$ rule is an ordinary zero-premise theorem.”** It is a semi-axiomatic replacement for a specific information-carrying rule and exposes the channels contained in its message.
- **“Only positive types have messages.”** Negative types also have messages, but they travel from client to provider because negative left rules carry information.
- **“Soundness and completeness imply identical dynamics.”** They establish the same provable sequents, not the same derivations or process behavior.
- **“SAX has ordinary cut elimination.”** The sequent $Q\vdash(P\oplus Q)\oplus R$ is a counterexample.
- **“Every analytic cut is a snip.”** Snips are more restricted; the source postpones their precise definition.
- **“The reverse cut is a new logical principle.”** It only reverses the textual presentation of the two ordinary cut premises.
- **“Three message processes are unordered data.”** Their addresses form a typed linked queue even if the runtime multiset itself is unordered.

## 10. Self-test questions with concise answers

1. **Why is MPASS communication synchronous?**  
   Its principal cut reduction retains and advances both the sender and receiver continuations.

2. **What replaces the sender continuation in SAX?**  
   A continuation channel carried by the message.

3. **Which rules become SAX axioms?**  
   Positive right rules and negative left rules—the noninvertible, information-carrying rules.

4. **How is SAX shown sound relative to sequent calculus?**  
   Derive each SAX axiom using ordinary identity and the corresponding ordinary rule.

5. **How is SAX shown complete?**  
   Simulate each removed ordinary rule by cutting against a SAX axiom.

6. **Why can snips remain?**  
   Composing several message axioms may require analytic cuts even when the ordinary proof is cut-free.

7. **What does $M\triangleright K$ do?**  
   It selects and instantiates the receiver branch matching message $M$.

8. **Who continues after a send/receive reduction?**  
   Only the recipient continuation; the message process is consumed.

## 11. Related concept pages

- [Semi-axiomatic sequent calculus and SAX](<../Concepts/Semi-Axiomatic Sequent Calculus and SAX.md>)
- [Cut elimination for SAX and snips](<../Concepts/Cut Elimination for SAX.md>)
- [Continuation channels](<../Concepts/Continuation Channels.md>)
- [Linear message passing and session types](<../Concepts/Linear Message Passing and Session Types.md>)
- [Cut reduction as process execution](<../Concepts/Cut Reduction as Process Execution.md>)
- [Sequent calculus, SAX, and explicit resources](<../Comparisons/Sequent-Calculus-SAX-and-Explicit-Resources.md>)
- [Futures and single assignment](<../Concepts/Futures-and-Single-Assignment.md>)

## 12. Source trail

- Frank Pfenning, *Semi-Axiomatic Sequent Calculus*, 15-836 Substructural Logics, Lecture 14, October 26, 2023.
- Numbered sections covered exactly: §1 **Introduction**; §2 **The Origin of Synchronous Communication**; §3 **Continuation Channels instead of Continuation Processes**; §4 **Back to Logic**; §5 **Generalizing to Other Connectives**; §6 **Relating Sequent Calculus to SAX**; §7 **Cut Elimination for SAX**; §8 **Completing Process Assignment and Dynamics**; §9 **Example Revisited**.
- Printed pages: L14.1-L14.11.
- PDF pages: 148-158.
- This guide preserves the source's distinction between equivalence of provability and normalization, and uses an original `bit` trace.

## 13. Previous/next navigation

- Previous: [Lecture 13 - Quantifiers](<Lecture 13 - Quantifiers.md>)
- Next: [Lecture 15 - Adjoint SAX](<Lecture 15 - Adjoint SAX.md>)

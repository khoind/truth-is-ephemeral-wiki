---
title: Subtyping
lecture: 8
date: 2023-09-21
pdf_pages: 88-101
printed_pages: L8.1-L8.14
tags:
  - session-types
  - subtyping
  - coinduction
  - variance
prerequisites:
  - Preservation and Progress
  - Linear Message Passing I-II
---

# Lecture 8: Subtyping

## 1. Why this lecture exists

Exact equality between the provider’s and client’s session types is sufficient for safe communication, but it is unnecessarily rigid. A provider that promises fewer possible output labels than its client is prepared to receive remains safe; similarly, a service that accepts more requests than a particular client may send is safe for that client. Session subtyping identifies the largest compatibility relation justified by a simple operational criterion: every message that can cross a channel must be understood by its receiver.

This flexibility supports more precise protocols, such as binary numbers without leading zeroes or stores that enter a deletion-only phase. It also exposes two technically important ideas: variance follows the direction in which a message or channel travels, and recursive session types require a coinductive rather than finite inductive reading of subtyping proofs.

## 2. Learning objectives

After studying this page, you should be able to:

- read $A\le B$ as safe connection of an $A$-provider to a $B$-client;
- derive the rules for internal choice, external choice, tensor, unit, and linear implication from message flow;
- explain covariance and contravariance without importing unsuitable object-oriented intuitions;
- construct and check a finite cyclic representation of a coinductive proof;
- extract a finite “message not understood” counterexample from a failed derivation;
- distinguish admissible reflexivity, transitivity, and subsumption from primitive object-language rules;
- use forwarding as a practical subtyping test and understand the subtyping-aware process rules.

## 3. Dependency map

The argument proceeds from the safety results of [Lecture 7](Lecture%2007%20-%20Preservation%20and%20Progress.md):

$$
\text{progress and preservation}
\longrightarrow
\text{messages must be understood}
\longrightarrow
\text{connective-wise variance rules}
\longrightarrow
\text{coinductive recursive checking}
\longrightarrow
\text{subsumption-aware process typing}.
$$

The semantic criterion determines both the successful rules and the shape of counterexamples. See [Session Subtyping](../Concepts/Session%20Subtyping.md) for a compact standalone development.

## 4. Section-by-section reconstruction

### 1. Introduction

Suppose

$$
\mathsf{nat}=\oplus\{\mathsf{zero}:\mathbf 1,\mathsf{succ}:\mathsf{nat}\},
\qquad
\mathsf{pos}=\oplus\{\mathsf{succ}:\mathsf{nat}\}.
$$

A provider of $\mathsf{pos}$ can safely be connected to a client expecting $\mathsf{nat}$: its only first label, `succ`, is among the client’s branches. The reverse connection is unsafe because a $\mathsf{nat}$ provider may send `zero` to a client that has no such continuation. Subtyping records this direction as $\mathsf{pos}\le\mathsf{nat}$, not conversely.

The relation is behavioral compatibility, not set inclusion applied uniformly to syntax. Who sends next matters. Provider-selected and client-selected choices consequently have opposite width directions.

### 2. Message Understood

The intended meaning of

$$A\le B$$

is: whenever a process provides channel $a$ at $A$ and another process uses $a$ at $B$, every message on $a$ has a continuation at the receiving endpoint. In the refactored dynamics,

$$
\mathsf{proc}(\mathsf{send}\;a\;m;P),
\mathsf{proc}(\mathsf{recv}\;a\;K)
\longrightarrow
\mathsf{proc}(P),\mathsf{proc}(m\triangleright K),
$$

this requires $m\triangleright K$ to be defined. The desired relation is as large as possible subject to that condition. When $A\nleq B$, a finite interaction prefix should expose a message the receiver cannot handle.

Here $m$ ranges over unit, label, or channel messages; $K$ is a receiver continuation; and $m\triangleright K$ means delivery of $m$ to $K$. The operation selects the matching continuation branch or substitutes a received channel, and is undefined when message forms or labels disagree.

Four structural properties are expected to be **admissible**, meaning derivable metatheoretically without adding them as primitive rules:

- reflexivity: $A\le A$;
- transitivity: $A\le B$ and $B\le C$ imply $A\le C$;
- right subsumption: from $\Delta\vdash P::(a:A)$ and $A\le B$, infer $\Delta\vdash P::(a:B)$;
- left subsumption: from $A\le B$ and $\Delta,b:B\vdash P::(c:C)$, infer $\Delta,b:A\vdash P::(c:C)$.

Subtyping has no rule between unlike outer constructors. A unit sender cannot satisfy a receiver expecting a channel; an implication cannot satisfy a receiver waiting for a choice label. Such mismatches make $m\triangleright K$ undefined immediately.

### 3. Internal Choice and Unit

For internal choice, the provider sends the label. Therefore every label the subtype might emit must be accepted by the supertype client:

$$
\frac{L\subseteq K
\qquad A_\ell\le B_\ell\quad(\forall\ell\in L)}
{\oplus\{\ell:A_\ell\}_{\ell\in L}
\le
\oplus\{k:B_k\}_{k\in K}}.
$$

$L$ and $K$ are finite label sets. $A_\ell$ and $B_\ell$ are continuation types for the shared label $\ell$. Only branches the provider can select, those in $L$, need continuation comparisons. Unit has only the closing message, so

$$\mathbf 1\le\mathbf 1$$

has no premises.

Recursive types make these rules coinductive. Unfolding $\mathsf{pos}\le\mathsf{nat}$ reaches $\mathsf{nat}\le\mathsf{nat}$; unfolding that judgment recreates itself. A valid proof may therefore be infinite, provided every branch can always be extended. A finite cyclic derivation represents that infinite proof by closing a branch when the same ordered pair of types reappears on its ancestry.

This is not mere “assume the goal.” The cycle is valid because it is **guarded** by unfolding and a structural rule: every finite observation is checked before the pair recurs. If a counterexample existed, a shortest one would not need to traverse the same pair twice.

Recursive refinements may require cycles involving different names. With the source’s natural/even/odd family, checking even numbers against naturals alternates through continuation pairs before returning to the initial pair. Conversely, attempting the unsafe direction produces a finite label sequence whose last label is absent. The failed branch is operational evidence, not just a failed proof search.

### 4. Example: Binary Numbers in Standard Form

The binary-number example uses session types to refine representation invariants. Its three interfaces are

$$
\begin{aligned}
\mathsf{bin}&=\oplus\{\mathsf{b0}:\mathsf{bin},\mathsf{b1}:\mathsf{bin},\mathsf e:\mathbf1\},\\
\mathsf{std}&=\oplus\{\mathsf{b0}:\mathsf{pos},\mathsf{b1}:\mathsf{std},\mathsf e:\mathbf1\},\\
\mathsf{pos}&=\oplus\{\mathsf{b0}:\mathsf{pos},\mathsf{b1}:\mathsf{std}\}.
\end{aligned}
$$

The unrestricted protocol permits either bit or termination at every stage. The standard-form protocol uses $\mathsf{pos}$ after a low-order zero so that a leading zero cannot finish the number, and the positive protocol excludes the empty representation. Coinductive width checking establishes

$$\mathsf{pos}\le\mathsf{std}\le\mathsf{bin}.$$

The example also reveals an algorithmic issue: a tree-shaped circular proof can reconsider the same type pair on separate branches. A forward saturation algorithm can memoize known pairs and reuse them. For a finite signature containing $n$ syntactically distinct type expressions, at most $n^2$ ordered pairs can occur on one search branch. Consequently a depth-first checker that records ancestor pairs either encounters a finite failure or closes a finite cycle, once rules for all constructors are included.

### 5. Tensor

At $A_1\otimes A_2$, the provider sends a channel of type $A_1$ and then continues along the original channel at $A_2$. Both components are covariant:

$$
\frac{A_1\le B_1\qquad A_2\le B_2}
{A_1\otimes A_2\le B_1\otimes B_2}.
$$

Why is the payload covariant? If the sent channel’s actual provider has type $C_1$, the sending process may know it at some $A'_1$ with

$$C_1\le A'_1\le A_1.$$

After handoff, the receiving client will use it at $B_1$. Requiring $A_1\le B_1$ completes the safe chain $C_1\le A'_1\le A_1\le B_1$. The original channel independently continues under $A_2\le B_2$.

This reasoning permits a generalized send rule:

$$
\frac{A'_1\le A_1\qquad\Delta\vdash P::(x:A_2)}
{\Delta,y:A'_1\vdash\mathsf{send}\;x\;y;P::(x:A_1\otimes A_2)}
\;\otimes R^*.
$$

The process owns $y$ as a client at the more precise type $A'_1$ and may transmit it where $A_1$ is promised.

### 6. Negative Types

For negative external choice, written $\mathbin{\&}\{\ell:A_\ell\}_{\ell\in L}$ here (the source typesets this constructor as $N\{\ldots\}$), the **client** sends a label and the provider receives it. A subtype provider must therefore accept every label that a supertype client may select:

$$
\frac{L\supseteq K
\qquad A_k\le B_k\quad(\forall k\in K)}
{\mathbin{\&}\{\ell:A_\ell\}_{\ell\in L}
\le
\mathbin{\&}\{k:B_k\}_{k\in K}}.
$$

Width reverses relative to $\oplus$, but continuation types remain in provider-to-client order.

For linear implication $A_1\multimap A_2$, the client sends an argument channel and the provider receives it. The argument is contravariant; the continuation is covariant:

$$
\frac{B_1\le A_1\qquad A_2\le B_2}
{A_1\multimap A_2\le B_1\multimap B_2}.
$$

If the client passes an actual channel through types $C_1\le B'_1\le B_1$, requiring $B_1\le A_1$ ensures that the receiving provider may safely use it at $A_1$. On the result channel, provider and client keep their roles, hence $A_2\le B_2$.

Three subtyping-aware process rules follow:

$$
\frac{A'\le A}{y:A'\vdash\mathsf{fwd}\;x\;y::(x:A)}\;\mathsf{id}
$$

$$
\frac{p(x:A')(y_i:B'_i)=P\in\Sigma
\qquad B_i\le B'_i\;(\forall i)
\qquad A'\le A}
{y_i:B_i\vdash\mathsf{call}\;p\;x\;y_i::(x:A)}\;\mathsf{call}
$$

$$
\frac{A'_1\le A_1\qquad\Delta,x:A_2\vdash P::(z:C)}
{\Delta,y:A'_1,x:A_1\multimap A_2
\vdash\mathsf{send}\;x\;y;P::(z:C)}\;\multimap L^*.
$$

The call’s actual arguments $B_i$ must be safe where the definition expects $B'_i$, while the defined result $A'$ may be exposed as $A$. Cut syntax need not be generalized: admissible left and right subsumption already permit the same programs, so a more elaborate cut rule would add notation without expressiveness.

In these rules a prime distinguishes a more precise or declared type from the type exposed at the call or send site; $i$ ranges over all formal parameters; $\forall i$ means that the stated premise holds for each of them; and $p(\ldots)=P\in\Sigma$ means the process definition is a member of the global signature.

### 7. Example: Subtyping of Stores

The store protocol is a negative choice because the client chooses an operation. Factor out the deletion result as

$$\mathsf{reply}(S)=\oplus\{\mathsf{none}:\mathbf1,\mathsf{some}:\mathsf{bin}\otimes S\}.$$

Then the unrestricted and phase-specific interfaces are

$$
\begin{aligned}
\mathsf{store}&=\&\{\mathsf{ins}:\mathsf{bin}\multimap\mathsf{store},
                       \mathsf{del}:\mathsf{reply}(\mathsf{store})\},\\
\mathsf{store1}&=\&\{\mathsf{ins}:\mathsf{bin}\multimap\mathsf{store1},
                        \mathsf{del}:\mathsf{reply}(\mathsf{store2})\},\\
\mathsf{store2}&=\&\{\mathsf{del}:\mathsf{reply}(\mathsf{store2})\}.
\end{aligned}
$$

The unrestricted store accepts `ins` and `del`. A phase-one store accepts both, but after its first deletion its continuation becomes a phase-two store that accepts only `del`. The useful relations are

$$\mathsf{store}\le\mathsf{store1}\le\mathsf{store2}.$$

The direction can look surprising until sender roles are restored. A provider of `store1` accepts at least the sole operation a `store2` client may send, so $\mathsf{store1}\le\mathsf{store2}$. The reverse fails: a client typed at `store1` may send `ins`, which a `store2` provider does not accept. Recursive continuation comparisons establish the remaining branches, including covariance through the positive result of deletion and contravariance at inserted arguments.

These types express a temporal usage protocol, closely related to typestate: the legal operations depend on the current phase, and communication changes that phase.

### 8. Subtyping in MPASS

MPASS enables subtyping with `--subtyping`, abbreviated `-s`. Since forwarding has type

$$x:A\vdash\mathsf{fwd}\;y\;x::(y:B)$$

exactly when $A\le B$, a tiny forwarding declaration acts as a subtyping query. Prefixing a declaration with `fail` tests that a proposed relation does *not* hold; running with `-d` still displays the diagnostic for that expected failure. This operational interface exercises the same relation used by process typing; it is not a separate nominal hierarchy.

The phase-specific store example illustrates why subtyping matters beyond isolated type comparisons. A producer that only inserts can expose the phase-one interface; after the transition, a consumer that only deletes uses the phase-two interface. The unrestricted implementation remains reusable because the derived subtype relations mediate the narrower views.

### 9. Summary

The complete relation for the lecture consists of the five coinductive type rules:

$$
\begin{array}{c@{\qquad}c}
\dfrac{L\subseteq K\quad A_\ell\le B_\ell\;(\ell\in L)}
{\oplus\{\ell:A_\ell\}_{\ell\in L}\le\oplus\{k:B_k\}_{k\in K}}
&
\dfrac{}{\mathbf1\le\mathbf1}\\[5mm]
\dfrac{A_1\le B_1\quad A_2\le B_2}
{A_1\otimes A_2\le B_1\otimes B_2}
&
\dfrac{L\supseteq K\quad A_k\le B_k\;(k\in K)}
{\mathbin{\&}\{\ell:A_\ell\}_{\ell\in L}\le\mathbin{\&}\{k:B_k\}_{k\in K}}\\[5mm]
\multicolumn{2}{c}{
\dfrac{B_1\le A_1\quad A_2\le B_2}
{A_1\multimap A_2\le B_1\multimap B_2}}
\end{array}
$$

They are interpreted coinductively, and they support the generalized identity, call, tensor-send, and implication-send rules above. Reflexivity, transitivity, and subsumption remain admissible metatheorems rather than additional syntax.

## 5. Formal core

The judgment $A\le B$ relates **structural session behavior**: an $A$-provider may replace a $B$-provider without causing the $B$-typed client to receive an unrecognized message. It is directional, even though both endpoints continue after most communications.

Symbols used throughout:

| Symbol | Meaning |
| --- | --- |
| $A,B,A_i,B_i$ | Session types and their component types. |
| $\mathbf 1$ | Positive unit: the provider sends the closing unit message. |
| $\oplus\{\ell:A_\ell\}_{\ell\in L}$ | Positive internal choice; the provider selects a label in $L$. |
| $A_1\otimes A_2$ | Positive channel output; provider sends an $A_1$ channel, then continues as $A_2$. |
| $\&\{\ell:A_\ell\}_{\ell\in L}$ | Negative external choice; client selects a label, provider handles it. |
| $A_1\multimap A_2$ | Negative channel input; client sends an $A_1$ channel, session continues as $A_2$. |
| $L,K$ | Finite sets of distinct labels. |
| $\ell,k$ | Individual labels; subscripts select continuation types. |
| $\le$, $\nleq$ | Safe-substitution relation and its failure. |
| $\Delta$ | A linear context of used channels. |
| $P$ | A process term; $x,y,z$ are channels. |
| $\Sigma$ | The global signature of recursive type and process definitions. |

“Covariant” means a premise preserves the direction $A_i\le B_i$; “contravariant” means it reverses it to $B_i\le A_i$. Width inclusion is determined by the set of messages the sender may choose, not by the words “subtype” and “supertype.”

The symbols $\subseteq$ and $\supseteq$ are subset and superset inclusion; $\forall$ means “for every”; $\in$ means membership; a prime marks a distinct related type rather than a derivative; and the subscripts $1,2,i,k,\ell$ identify components, parameters, or label-indexed branches. Rule names such as $\otimes R^*$ and $\multimap L^*$ indicate subtyping-generalized right and left process-typing rules, not additional type constructors.

Algorithmically, a checker unfolds equirecursive names and explores rule premises. It maintains the ordered pairs already encountered on the current branch. A constructor mismatch or failed width condition yields a finite counterexample. Repetition of a guarded pair closes a cyclic branch. All branches must succeed.

## 6. Operational/computational reading

Read $A\le B$ by placing an $A$ process on the provider side and a $B$ process on the client side, then ask who controls the next send:

- If the provider sends, the client’s accepted message set must cover the provider’s possible messages.
- If the client sends, the provider’s accepted message set must cover the client’s possible messages.
- After the message, compare continuation types with the provider still on the left.
- When a channel is handed off, trace its old provider to its new client; this reveals tensor covariance and implication-argument contravariance.

This reading is exactly the local condition needed to extend preservation and progress. It does not claim that subtype and supertype implement the same protocol, only that the more precise provider cannot surprise the less precise client.

## 7. Worked derivation or trace in original notation and prose

Use a fresh recursive example:

$$
\begin{aligned}
\mathsf{event}&=\oplus\{\mathsf{ping}:\mathsf{event},\;\mathsf{done}:\mathbf1\},\\
\mathsf{heartbeat}&=\oplus\{\mathsf{ping}:\mathsf{heartbeat}\}.
\end{aligned}
$$

We show $\mathsf{heartbeat}\le\mathsf{event}$ coinductively.

1. Unfold both names. The provider-side label set is $\{\mathsf{ping}\}$ and the client-side set is $\{\mathsf{ping},\mathsf{done}\}$, so width succeeds.
2. The only continuation obligation is again $\mathsf{heartbeat}\le\mathsf{event}$.
3. That ordered pair is the guarded ancestor goal. Close the branch cyclically.

Written compactly:

$$
\frac{
  \mathsf{heartbeat}\le\mathsf{event}\;\text{(cycle)}
}{
  \oplus\{\mathsf{ping}:\mathsf{heartbeat}\}
  \le
  \oplus\{\mathsf{ping}:\mathsf{event},\mathsf{done}:\mathbf1\}
}
$$

Every finite trace emitted by a `heartbeat` provider consists only of `ping` labels, so an `event` client always has the needed branch. The fact that the client also knows `done` causes no obligation because the provider controls internal choice and never emits it.

The reverse fails immediately:

$$
\{\mathsf{ping},\mathsf{done}\}\nsubseteq\{\mathsf{ping}\}.
$$

The one-message counterexample is `done`: an `event` provider may send it, but a `heartbeat` client has no `done` continuation. This finite witness refutes the reverse relation without reasoning about infinite traces.

## 8. Conceptual synthesis

Session subtyping is the proof-relevant boundary between precision and compatibility. A narrow output type tells us more about what a provider will do; a wide input type tells us more about what a provider is prepared to accept. Both can be subtypes because provider replacement is judged against the client’s possible actions.

Coinduction matches the property being established: there is no finite interaction prefix ending in an unrecognized message. Cyclic proofs are finite certificates of this potentially infinite safety argument. Process subsumption then turns the behavioral relation into usable flexibility while the original preservation/progress discipline continues to enforce linear ownership and compatible evolution.

## 9. Common confusions and failure modes

- **Fewer labels always means subtype.** Only for provider-selected internal choice. Client-selected external choice reverses width.
- **Every component is covariant.** The argument of $\multimap$ is contravariant because it travels from client to provider.
- **A cycle proves any recursive judgment.** Only a repeated, structurally guarded ordered pair closes a branch; constructor and label checks before the cycle must succeed.
- **Reflexivity and transitivity are syntax rules.** In this presentation they are admissible metatheorems.
- **Subtyping permits different outer constructors.** It does not: the first message forms would disagree.
- **$A\le B$ means an $A$ client accepts a $B$ provider.** The convention is an $A$ provider connected to a $B$ client.
- **The phase-two store is below the phase-one store.** A phase-two provider cannot accept an `ins` that a phase-one client may send, so the safe direction is phase one below phase two.
- **Generalized cut is required.** Left and right subsumption make it redundant.

## 10. Self-test questions with concise answers

1. **What operational event witnesses $A\nleq B$?** A finite message sequence ending in a message the receiver’s continuation cannot accept.
2. **Why is $\oplus$ width covariant by subset?** Its provider chooses, so every subtype label must occur at the supertype client.
3. **Why is $\&$ width reversed?** Its client chooses, so the subtype provider must accept every supertype-client label.
4. **What is the tensor payload premise?** $A_1\le B_1$, because the sent channel ultimately connects its provider to the supertype client.
5. **What is the implication argument premise?** $B_1\le A_1$, because the client-supplied channel is consumed by the subtype provider.
6. **Why can a recursive checker terminate?** With finitely many type expressions, only finitely many ordered pairs exist; a branch must fail or repeat one.
7. **How can forwarding test subtyping?** The generalized identity rule types a forwarder from $A$ to $B$ exactly when $A\le B$.
8. **Does a successful cyclic proof prove termination of sessions?** No; it proves communication compatibility through every finite prefix.

## 11. Related concept pages

- [Session Subtyping](../Concepts/Session%20Subtyping.md) presents the relation as a reusable concept with a fresh worked protocol.
- [Preservation and Progress](../Concepts/Preservation%20and%20Progress.md) states the safety properties subtyping must retain.
- [Configuration Typing and Observation](../Concepts/Configuration%20Typing%20and%20Observation.md) explains the runtime interfaces on which provider/client compatibility is observed.

## 12. Source trail

- Frank Pfenning, *15-836 Substructural Logics*, Lecture 8, “Subtyping,” September 21, 2023.
- Numbered sections: 1 “Introduction”; 2 “Message Understood”; 3 “Internal Choice and Unit”; 4 “Example: Binary Numbers in Standard Form”; 5 “Tensor”; 6 “Negative Types”; 7 “Example: Subtyping of Stores”; 8 “Subtyping in MPASS”; 9 “Summary.”
- Printed pages: L8.1–L8.14.
- PDF pages: 88–101.

## 13. Previous/next navigation

Previous: [Lecture 7: Preservation and Progress](Lecture%2007%20-%20Preservation%20and%20Progress.md).

Next: [Lecture 9: Validity](Lecture%2009%20-%20Validity.md).

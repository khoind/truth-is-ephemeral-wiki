---
title: "Lecture 6: Linear Message Passing II"
lecture: 6
date: 2023-09-14
pdf_pages: "66-77"
printed_pages: "L6.1-L6.12"
tags:
  - linear-logic
  - session-types
  - channel-passing
  - mpass
prerequisites:
  - "Lecture 5: Linear Message Passing I"
---

# Lecture 6: Linear Message Passing II

## 1. Why this lecture exists

Lecture 5 obtained label and close communication from internal choice and unit. That fragment can describe streams and recursive control, but it cannot transmit a channel as data or let the client choose a service operation. Lecture 6 completes the basic session vocabulary: tensor sends a channel, linear implication receives one, and external choice lets the client select a label. It also turns the pairwise reductions into multiset rewriting, making independent communication steps genuinely unordered.

These additions make the communication graph mobile. Passing a channel transfers a linear capability and changes which processes can interact. The typing rules guarantee that the old owner gives up that capability and the new owner receives exactly one endpoint. See [Session Connectives and Channel Passing](../Concepts/Session%20Connectives%20and%20Channel%20Passing.md) for a connective-by-connective account.

## 2. Learning objectives

After this lecture, a reader should be able to:

- represent a running process network as a multiset configuration;
- state the finite internal- and external-choice typing rules;
- explain how $A\otimes B$ sends an $A$-channel before continuing as $B$;
- explain how $A\multimap B$ receives an $A$-channel before continuing as $B$;
- distinguish standard sequent rules from the single-continuation variants used by MPASS;
- trace channel ownership through a communication step;
- read list and storage-server protocols as session types; and
- state what linear parametricity strengthens beyond ordinary structural parametricity.

## 3. Dependency map

Lecture 5 contributes cut/spawn, identity/forward, $\oplus$, $1$, and recursion. Lecture 6 extends that core in two directions:

$$
\begin{array}{c@{\qquad}c}
\text{provider-driven}&\text{client-driven}\\
\oplus\{\ell:A_\ell\}&\&\{\ell:A_\ell\}\\
A\otimes B&A\multimap B
\end{array}
$$

The horizontal distinction is polarity and message direction; the vertical distinction is whether the message is a label or a channel. All communications execute within configurations by linear multiset rewriting. Lists exercise positive protocols; the storage server alternates negative requests with positive replies.

## 4. Section-by-section reconstruction covering every numbered heading

### 1. Introduction

The starting process language has spawn from cut, forwarding from identity, label send/receive from $\oplus$, unit send/receive from $1$, and named process calls. Actions are described from the provider's perspective. Thus “send label” for $\oplus R$ means that the provider sends; the corresponding client uses $\oplus L$ and receives. A process call is type-independent and is the mechanism by which named recursive definitions unfold.

The lecture's first reformulation observes that the operational rules themselves are linear inferences. This matters because a concurrent execution is not fundamentally a list of commands: it is a collection of independently matchable resources.

### 2. Dynamics as Linear Inference

A semantic object $\mathsf{proc}(P)$ represents one running process in state $P$. Runtime channels are written $a,b,c$ to distinguish concrete fresh names from source variables such as $x,y,z$. A configuration $\mathcal C$ is an unordered multiset of such objects.

For unit synchronization:

$$
\mathsf{proc}(\mathsf{send}\ a\ ()),
\mathsf{proc}(\mathsf{recv}\ a(()\Rightarrow Q))
\longrightarrow \mathsf{proc}(Q).
$$

For labels:

$$
\mathsf{proc}(\mathsf{send}\ a\ k;P),
\mathsf{proc}(\mathsf{recv}\ a(\ell\Rightarrow Q_\ell)_{\ell\in L})
\longrightarrow
\mathsf{proc}(P),\mathsf{proc}(Q_k),
$$

provided $k\in L$. A rule selects just the matching objects and leaves every other object unchanged. Therefore two redexes on disjoint channels can fire in either order without imposing a false global schedule.

Spawn rewrites one object into two:

$$
\mathsf{proc}(x^A\leftarrow P(x);Q(x))
\longrightarrow
\mathsf{proc}(P(a)),\mathsf{proc}(Q(a)),
$$

where $a$ is fresh in the *whole* configuration. This global side condition is stronger than checking only the matched premise; technically it has the flavor of existential name generation. The transition notation is $\mathcal C\longrightarrow\mathcal C'$. These configuration metavariables must not be confused with the type $C$ or with a channel context $\Delta$.

### 3. Typing Finite Internal Choice

Finite internal choice is

$$
\oplus\{\ell:A_\ell\}_{\ell\in L}.
$$

The provider selects one $k\in L$ and continues according to $A_k$; the client supplies a continuation for every $\ell\in L$. The left rule is finitary because $L$ is finite. MPASS conveniently assumes $L$ nonempty, although logic also admits the empty internal choice $0=\oplus\{\}$, for which there is no right rule and the left rule has no premises.

### 4. Sending Channels Along Channels

The tensor protocol $A\otimes B$ means: the provider sends a channel of type $A$ along the offered channel, then continues to provide that same offered channel at type $B$. Channel transmission changes connectivity, as in the $\pi$-calculus, but linear typing also transfers ownership.

Standard tensor right introduction has two premises, one proving $A$ and one proving $B$. MPASS instead uses a single-continuation rule $\otimes R^*$:

$$
\frac{\Delta\vdash P::(x:B)}
     {\Delta,w:A\vdash \mathsf{send}\ x\ w;P::(x:A\otimes B)}.
$$

Here the process already owns $w:A$ and sends that channel. In the continuation $P$, $w$ is absent from $\Delta$: the sender no longer owns it. The client receives the transmitted channel under a fresh local variable:

$$
\frac{\Delta',y:A,x:B\vdash Q(y)::(z:C)}
     {\Delta',x:A\otimes B\vdash
      \mathsf{recv}\ x(y\Rightarrow Q(y))::(z:C)}.
$$

The communication substitutes the concrete channel being sent:

$$
\mathsf{proc}(\mathsf{send}\ a\ b;P),
\mathsf{proc}(\mathsf{recv}\ a(y\Rightarrow Q(y)))
\longrightarrow
\mathsf{proc}(P),\mathsf{proc}(Q(b)).
$$

The alternative right rule is proof-theoretically justified in both directions: $\otimes R^*$ is derivable from standard $\otimes R$ using identity, while standard $\otimes R$ is recoverable from $\otimes R^*$ using cut. Consequently, wholesale replacement changes the literal cut-elimination theorem: the translation may retain subformula-respecting, or analytic, cuts. This is a calculus-design fact, not an additional runtime communication.

### 5. Example: Sequences

A list of channels of element protocol $A$ is

$$
\mathsf{list}_A=
\oplus\{\mathsf{nil}:1,\ \mathsf{cons}:A\otimes\mathsf{list}_A\}.
$$

The provider sends either $\mathsf{nil}$ and closes, or $\mathsf{cons}$, an element channel, and the remaining list. Because the type is positive, every message flows from provider to client. An append process receives the shape of its first input list. In the nil case it consumes the close and forwards the second list as the result. In the cons case it relays the label and head channel, then tail-calls append on the remaining first list and the unchanged second list. Linear contexts at each program point expose mistakes immediately: once the head is sent, its channel cannot appear in the continuation.

### 6. External Choice

External choice, written $\&\{\ell:A_\ell\}_{\ell\in L}$, reverses label ownership. The provider must receive and handle every label; the client selects and sends one label. It is negative because its right rule is invertible and contains no choice by the provider.

The same runtime label rule used for internal choice suffices. Syntax does not determine whether a sender is provider or client; the typing derivation and the polarity of the current protocol do. This is why “send always means provider action” is false once negative connectives enter the language.

### 7. Linear Implication

Linear implication $A\multimap B$ is the channel-passing counterpart of external choice. Its provider first receives a channel of type $A$, then continues as $B$:

$$
\frac{\Delta,y:A\vdash P(y)::(x:B)}
     {\Delta\vdash \mathsf{recv}\ x(y\Rightarrow P(y))::(x:A\multimap B)}.
$$

The client owns a channel $w:A$, sends it to the provider, relinquishes $w$, and continues to use $x:B$:

$$
\frac{\Delta',x:B\vdash Q::(z:C)}
     {\Delta',w:A,x:A\multimap B\vdash
      \mathsf{send}\ x\ w;Q::(z:C)}.
$$

This is the one-continuation $\multimap L^*$ formulation. Its runtime step is the same channel-substitution rule as for tensor, with the sender now being the client. Tensor and implication are not “output” and “input” in the abstract; they are provider-output and provider-input, respectively.

### 8. Example: A Storage Server

A polymorphic storage interface can be expressed as

$$
\mathsf{store}_A=
\&\{\mathsf{ins}:A\multimap\mathsf{store}_A,
\ \mathsf{del}:\oplus\{\mathsf{none}:1,
\mathsf{some}:A\otimes\mathsf{store}_A\}\}.
$$

The outer $\&$ says the client requests insertion or deletion. After $\mathsf{ins}$, the provider receives an $A$-channel and resumes the service. After $\mathsf{del}$, control switches: the provider chooses $\mathsf{none}$ and closes, or chooses $\mathsf{some}$, sends an element, and resumes the residual store.

One implementation represents a stack as a chain of node processes ending in an empty process. An empty node receiving insertion spawns a fresh empty tail and becomes a nonempty node; receiving deletion reports none. A nonempty node receiving insertion preserves the old head in a spawned node and takes ownership of the new element. Receiving deletion reports some, sends its owned head channel, and forwards the tail as the continuing store. Each program step is type-directed: the outer connective says which side can act and the residual type says what action is legal next.

The empty-case design also exposes a boundary decision. If deletion from an empty store closed the service, clients can terminate cleanly. If it instead recurred forever, the protocol would need an explicit deallocation option; linearity prevents a client from simply forgetting a live store.

### 9. A Brief Note on Parametricity

For a structural polymorphic store, parametricity says returned values originated among inserted values, but contraction and weakening still permit duplication or loss. With the linear interface, neither is legal: every inserted $A$-channel must be transferred exactly once. Subject to terminating, complete interaction, the outputs must therefore be a permutation of the inputs. The order is not determined by the linear type alone; stack, queue, or some other permutation policy requires additional structure or a stronger specification. The lecture presents the prospective ordered-logic strengthening as a conjecture, not as an established theorem.

### 10. Summary

The complete MPASS core now has typing rules for cut, identity, $1$, finite $\oplus$, $\otimes$, finite $\&$, and $\multimap$, plus named calls. Its dynamics consists of fresh-name spawning, two forwarding orientations, label synchronization, unit synchronization, and channel synchronization. Positive and negative connectives share runtime forms, but their typing rules reverse provider/client responsibility.

## 5. Formal core (rules/judgments/theorems, with each symbol explained)

The typing judgment remains $\Delta\vdash P::(x:A)$. $\Delta$ is an unordered linear context of used channels; $P$ is the process; and $(x:A)$ is the one provided channel. $L$ is a finite label set, $k$ is one chosen label, $A_\ell$ is the continuation indexed by $\ell$, and $C$ is an arbitrary result protocol.

The inherited structural core remains explicit in the complete language:

$$
\frac{\Delta\vdash P(x)::(x:A)\qquad
      \Delta',x:A\vdash Q(x)::(z:C)}
{\Delta,\Delta'\vdash x^A\leftarrow P(x);Q(x)::(z:C)}\;\mathsf{cut}
$$

$$
x:A\vdash\mathsf{fwd}\ y\ x::(y:A)\;\mathsf{id}
$$

$$
\frac{}{\cdot\vdash\mathsf{send}\ x\ ()::(x:1)}\;1R
\qquad
\frac{\Delta\vdash Q::(z:C)}
{\Delta,x:1\vdash\mathsf{recv}\ x(()\Rightarrow Q)::(z:C)}\;1L.
$$

$x^A\leftarrow P(x);Q(x)$ binds the newly connected source channel $x$ at type $A$; $\mathsf{fwd}\ y\ x$ provides $y$ by forwarding to used channel $x$; $\cdot$ is the empty context; and $()$ is the unique unit message.

The finite choice rules are:

$$
\frac{\Delta\vdash P::(x:A_k)\quad k\in L}
{\Delta\vdash\mathsf{send}\ x\ k;P::(x:\oplus\{\ell:A_\ell\}_{\ell\in L})}
\;\oplus R
$$

$$
\frac{\Delta,x:A_\ell\vdash Q_\ell::(z:C)\quad(\forall\ell\in L)}
{\Delta,x:\oplus\{\ell:A_\ell\}_{\ell\in L}\vdash
\mathsf{recv}\ x(\ell\Rightarrow Q_\ell)_{\ell\in L}::(z:C)}
\;\oplus L,
$$

$$
\frac{\Delta\vdash P_\ell::(x:A_\ell)\quad(\forall\ell\in L)}
{\Delta\vdash\mathsf{recv}\ x(\ell\Rightarrow P_\ell)_{\ell\in L}::
(x:\&\{\ell:A_\ell\}_{\ell\in L})}
\;\&R
$$

$$
\frac{\Delta,x:A_k\vdash Q::(z:C)\quad k\in L}
{\Delta,x:\&\{\ell:A_\ell\}_{\ell\in L}\vdash
\mathsf{send}\ x\ k;Q::(z:C)}
\;\&L.
$$

The tensor and implication rules used operationally are:

$$
\frac{\Delta\vdash P::(x:B)}
{\Delta,w:A\vdash\mathsf{send}\ x\ w;P::(x:A\otimes B)}\;\otimes R^*
$$

$$
\frac{\Delta',y:A,x:B\vdash Q(y)::(z:C)}
{\Delta',x:A\otimes B\vdash\mathsf{recv}\ x(y\Rightarrow Q(y))::(z:C)}\;\otimes L
$$

$$
\frac{\Delta,y:A\vdash P(y)::(x:B)}
{\Delta\vdash\mathsf{recv}\ x(y\Rightarrow P(y))::(x:A\multimap B)}\;\multimap R
$$

$$
\frac{\Delta',x:B\vdash Q::(z:C)}
{\Delta',w:A,x:A\multimap B\vdash\mathsf{send}\ x\ w;Q::(z:C)}\;\multimap L^*.
$$

The star marks the single-continuation alternative to a standard sequent rule. It is not polarity, Kleene iteration, or an exponent. In every channel-passing rule, $y$ is a binder local to the receiver; at runtime $Q(b)$ or $P(b)$ is capture-avoiding substitution of concrete channel $b$ for $y$.

For completeness, the runtime rules can be collected in one configuration-level summary:

$$
\begin{aligned}
\mathsf{proc}(x^A\leftarrow P(x);Q(x))
&\longrightarrow \mathsf{proc}(P(a)),\mathsf{proc}(Q(a))
&& (a\text{ fresh}),\\
\mathsf{proc}(P(b)),\mathsf{proc}(\mathsf{fwd}\ a\ b)
&\longrightarrow \mathsf{proc}(P(a)),\\
\mathsf{proc}(\mathsf{fwd}\ a\ b),\mathsf{proc}(Q(a))
&\longrightarrow \mathsf{proc}(Q(b)),\\
\mathsf{proc}(\mathsf{send}\ a\ k;P),
\mathsf{proc}(\mathsf{recv}\ a(\ell\Rightarrow Q_\ell)_{\ell\in L})
&\longrightarrow \mathsf{proc}(P),\mathsf{proc}(Q_k)
&& (k\in L),\\
\mathsf{proc}(\mathsf{send}\ a\ ()),
\mathsf{proc}(\mathsf{recv}\ a(()\Rightarrow Q))
&\longrightarrow \mathsf{proc}(Q),\\
\mathsf{proc}(\mathsf{send}\ a\ b;P),
\mathsf{proc}(\mathsf{recv}\ a(y\Rightarrow Q(y)))
&\longrightarrow \mathsf{proc}(P),\mathsf{proc}(Q(b)).
\end{aligned}
$$

$\mathsf{proc}(P)$ is a running-process object; commas form a multiset; $a$ is a runtime carrier channel; $b$ is a forwarded or transmitted channel; and freshness is global to the configuration. Label synchronization covers both $\oplus$ and $\&$, while channel synchronization covers both $\otimes$ and $\multimap$; typing determines which endpoint is provider.

## 6. Operational/computational reading

Configurations are multisets, so rule application is local and closed under unrelated parallel context:

$$
\mathcal C\longrightarrow\mathcal C'
\quad\Longrightarrow\quad
\mathcal C,\mathcal D\longrightarrow\mathcal C',\mathcal D.
$$

$\mathcal D$ is any disjoint remainder of the configuration. Label and unit steps exchange control information. Channel steps move connectivity: after $b$ is sent, the receiver owns the capability represented by $b$, and the sender's continuation cannot mention it. Forwarding replaces an intermediate endpoint, while spawn creates a fresh private edge. These rules permit concurrency but do not prescribe fairness or a unique interleaving.

Polarity gives a compact reading discipline:

- at $\oplus$ or $\otimes$, the provider sends;
- at $\&$ or $\multimap$, the provider receives;
- after the event, both parties continue at the selected or trailing protocol.

## 7. Worked derivation or trace in original notation and prose

Define a one-use dispatch service:

$$
\mathsf{dispatch}_A=
\&\{\mathsf{drop}:1,\ \mathsf{deliver}:A\multimap1\}.
$$

The provider waits for the client's label. Suppose a client owns $b:A$, selects $\mathsf{deliver}$ on runtime channel $a$, sends $b$, and then waits for close. A provider receives the label, receives an element channel into variable $y$, passes $y$ to an internal worker, and closes $a$.

Ignoring the independent worker after it gains ownership, the relevant configuration evolves as follows:

$$
\begin{aligned}
&\mathsf{proc}(\mathsf{recv}\ a(
 \mathsf{drop}\Rightarrow P_d\mid
 \mathsf{deliver}\Rightarrow P_v)),\ 
 \mathsf{proc}(\mathsf{send}\ a\ \mathsf{deliver};
 \mathsf{send}\ a\ b;Q)\\
&\longrightarrow
 \mathsf{proc}(P_v),\mathsf{proc}(\mathsf{send}\ a\ b;Q)\\
&=
 \mathsf{proc}(\mathsf{recv}\ a(y\Rightarrow P(y))),
 \mathsf{proc}(\mathsf{send}\ a\ b;Q)\\
&\longrightarrow
 \mathsf{proc}(P(b)),\mathsf{proc}(Q).
\end{aligned}
$$

Initially the provider sees $a:\mathsf{dispatch}_A$. After the label, its residual type is $a:A\multimap1$. After the channel transfer, the provider owns $b:A$ and $a:1$, while the client no longer owns $b$ and uses $a:1$. A final unit synchronization removes $a$. Choosing $\mathsf{drop}$ while also retaining $b:A$ would fail typing unless the client uses $b$ elsewhere: linear channels cannot be abandoned merely because another branch was selected.

Two independent dispatch pairs on $a$ and $c$ may take their first steps in either order. The multiset semantics records both executions without assigning a causal order between them.

## 8. Conceptual synthesis

Session types combine local protocol state with ownership. Choice transmits control; tensor and implication transmit capabilities; recursion repeats the state machine; cut supplies private connectivity; and configurations provide the concurrent world in which these local interactions occur. The connective does more than classify a payload: it fixes the sender, receiver, continuation, and linear ownership update.

The alternative single-continuation rules make each source construct operationally small: only cut spawns, each send or receive has one continuation, and unit send terminates. Their proof-theoretic justification is by translation, so one must not silently claim the unmodified cut-elimination theorem for the alternative calculus.

## 9. Common confusions and failure modes

- **Using syntax alone to identify the provider.** The same send/receive forms serve positive and negative protocols; typing determines the role.
- **Reading $A\otimes B$ as a pair of ordinary values.** It is a temporal protocol: send an $A$-channel, then continue on the same offered channel as $B$.
- **Retaining a sent channel.** Linear ownership transfers; the sender's continuation cannot still use that channel.
- **Confusing $A\multimap B$ with unrestricted function space.** It is a one-use session action in which the provider receives an $A$-channel.
- **Treating configurations as ordered lists.** They are multisets; independent objects do not acquire an artificial order.
- **Checking freshness only locally.** A spawned runtime name must be fresh in the entire configuration.
- **Claiming linearity fixes list/store order.** It fixes exact use, not whether a service is FIFO, LIFO, or another permutation.
- **Promoting a conjecture to a theorem.** The ordered-connective queue/stack guarantee is only suggested in the lecture.

## 10. Self-test questions with concise answers

1. **What does $\mathsf{proc}(P)$ denote?** One running process object in state $P$.
2. **Why is multiset rewriting concurrent?** Disjoint redexes can reduce independently without a specified global order.
3. **Who selects a branch of $\&\{\ell:A_\ell\}$?** The client; the provider must accept every advertised label.
4. **What does the provider do first at $A\otimes B$?** Sends an $A$-channel, then continues as $B$.
5. **What does the provider do first at $A\multimap B$?** Receives an $A$-channel, then continues as $B$.
6. **Why does a sent channel disappear from the sender's context?** Sending transfers its unique linear ownership.
7. **What justifies $\otimes R^*$?** Translation to standard $\otimes R$ using identity, and recovery of standard $\otimes R$ using cut.
8. **What extra claim does linear parametricity support for a store?** Under complete terminating use, returned elements form a permutation of inserted elements rather than allowing loss or duplication.

## 11. Related concept pages

- [Session Connectives and Channel Passing](../Concepts/Session%20Connectives%20and%20Channel%20Passing.md)
- [Linear Message Passing and Session Types](../Concepts/Linear%20Message%20Passing%20and%20Session%20Types.md)
- [Cut Reduction as Process Execution](../Concepts/Cut%20Reduction%20as%20Process%20Execution.md)
- [Lecture 5: Linear Message Passing I](Lecture%2005%20-%20Linear%20Message%20Passing%20I.md)

## 12. Source trail (lecture, numbered sections, printed-page range, PDF-page range)

- Frank Pfenning, *Linear Message Passing II*, Lecture 6, September 14, 2023.
- Numbered sections covered: 1 “Introduction”; 2 “Dynamics as Linear Inference”; 3 “Typing Finite Internal Choice”; 4 “Sending Channels Along Channels”; 5 “Example: Sequences”; 6 “External Choice”; 7 “Linear Implication”; 8 “Example: A Storage Server”; 9 “A Brief Note on Parametricity”; 10 “Summary.”
- Printed pages: L6.1-L6.12.
- PDF pages: 66-77.

## 13. Previous/next navigation

Previous: [Lecture 5: Linear Message Passing I](Lecture%2005%20-%20Linear%20Message%20Passing%20I.md).

Next: Lecture 7, *Preservation and Progress* (not yet authored in this repository).

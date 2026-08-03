---
title: Preservation and Progress
lecture: 7
date: 2023-09-19
pdf_pages: 78-87
printed_pages: L7.1-L7.10
tags:
  - session-types
  - type-safety
  - operational-semantics
  - recursion
prerequisites:
  - Linear Message Passing I-II
  - Cut and Identity Elimination
---

# Lecture 7: Preservation and Progress

## 1. Why this lecture exists

The logical origin of the message-passing language explains its process constructs, but it does not by itself state the runtime guarantee a programmer needs. Cut elimination says how a proof can be normalized and, in the fragment without recursion, that normalization terminates. A running program is different: recursive definitions may compute forever, and users observe only behavior at an interface rather than inspecting the whole proof term. This lecture therefore recasts the proof-theoretic ideas as programming-language metatheory.

The central result is type safety for configurations of concurrent processes. **Preservation** says that a computation step does not damage the externally promised session interface. **Progress** says that a closed, well-typed configuration is either able to step or is legitimately waiting at its external channels. The lecture also makes explicit what an external observation can reveal and refactors the operational semantics so every message exchange has one uniform rule.

## 2. Learning objectives

After studying this page, you should be able to:

- distinguish recursive type unfolding from recursive process calls;
- read the configuration judgment $\Delta \vdash C :: \Delta'$ as a transformation of channel interfaces;
- apply the `proc`, `join`, and `empty` rules and explain why a typing order need not be the runtime order;
- state preservation and progress with their exact hypotheses;
- explain why progress is neither termination nor “every process always steps”;
- trace spawning, forwarding, calls, and synchronized communication;
- describe which positive behavior can be observed and why observation stops at a negative type.

## 3. Dependency map

The development follows this chain:

$$
\text{cut and identity reduction}
\longrightarrow
\text{process reductions}
\longrightarrow
\text{typed configurations}
\longrightarrow
\begin{cases}
\text{preservation}\\
\text{progress}
\end{cases}
\longrightarrow
\text{safe external observation}.
$$

Recursive signatures sit beside this chain: they enlarge the language enough that normalization need not terminate, which is precisely why preservation and progress replace termination as the relevant guarantees. For fuller treatments of the two endpoints of the chain, see [Preservation and Progress](../Concepts/Preservation%20and%20Progress.md) and [Configuration Typing and Observation](../Concepts/Configuration%20Typing%20and%20Observation.md).

## 4. Section-by-section reconstruction

### 1. Introduction

Linear propositions correspond closely to session types, sequent proofs to communicating processes, and principal cut reductions to communications. The correspondence is explanatory, not an identification of logic with execution. Proofs are objects meant to be inspected in full. Programs are commonly judged through the behavior visible at their inputs and outputs, so an implementation may be refactored without changing what a client can observe.

Two differences force a new metatheory. First, general process recursion permits infinite computation even though pure cut elimination terminates. Second, program equivalence is mediated by observation: proof permutations and identity expansions suggest equations between processes, but not necessarily computation steps. Constructive type theory supplies a broader setting in which proofs can be data and programs can carry specifications, but this lecture stays with the concrete safety questions for linear message passing.

### 2. Integrating Recursion

Recursion enters at two distinct levels. A recursive type name is **equirecursive**: a name and its defining body are interchangeable during type checking without sending a runtime message. For example, an independently chosen type

$$
\mathsf{stream} = \oplus\{\mathsf{stop}:\mathbf 1,\;\mathsf{more}:\mathsf{stream}\}
$$

may be unfolded whenever its outer constructor must be inspected. A recursive process definition, by contrast, executes: a call reduces by replacing the call with the definition instantiated at actual channels.

Both kinds of definition live in a global signature:

$$
\Sigma ::= \cdot
\mid \Sigma,\;t=A
\mid \Sigma,\;p(x:A)(\vec y:\vec B)=P.
$$

Here $\Sigma$ is a finite signature; $\cdot$ is empty; $t$ is a type name; $A$ is a session type; $p$ is a process name; $x$ is the channel provided by $P$; and $\vec y:\vec B$ abbreviates parameters $y_i:B_i$. Declarations may be mutually recursive, so each is checked against the whole fixed signature rather than only against earlier declarations. All type and process names must nevertheless be distinct.

The judgment $\vdash_\Sigma A\;\mathsf{type}$ says that unfolding names from $\Sigma$ makes $A$ a well-formed type and that every type name appearing in it is defined. The judgment $\vdash \Sigma\;\mathsf{sig}$ says the entire signature is valid. Once a valid global $\Sigma$ has been fixed, its subscript is normally suppressed.

Mutual recursion is captured by checking a declaration list $\Sigma'$ against that fixed global signature $\Sigma$:

$$
\frac{}{\vdash_\Sigma\cdot\;\mathsf{sig}}
\qquad
\frac{\vdash_\Sigma\Sigma'\;\mathsf{sig}\qquad
      \vdash_\Sigma A\;\mathsf{type}}
     {\vdash_\Sigma(\Sigma',t=A)\;\mathsf{sig}}
$$

$$
\frac{\vdash_\Sigma\Sigma'\;\mathsf{sig}\qquad
      (\vec y:\vec B)\vdash_\Sigma P(x,\vec y)::(x:A)}
     {\vdash_\Sigma(\Sigma',p(x:A)(\vec y:\vec B)=P(x,\vec y))\;\mathsf{sig}}.
$$

In these rules $\Sigma'$ is the declaration list being validated, while the subscript $\Sigma$ never changes and may contain the very mutually recursive names under examination.

At runtime, if $p(x:A)(\vec y:\vec B)=P$ belongs to $\Sigma$, then

$$
\mathsf{proc}(\mathsf{call}\;p\;a\;\vec b)
\longrightarrow
\mathsf{proc}(P[a/x,\vec b/\vec y]).
$$

The bracket notation is capture-avoiding substitution of actual channel names for formal parameters. The call step is computational; equirecursive type unfolding is not.

### 3. Typing Configurations of Processes

A process may spawn more processes, so runtime states are configurations:

$$
C ::= \mathsf{proc}(P) \mid C_1,C_2 \mid \cdot.
$$

The comma is associative and commutative at runtime, and $\cdot$ is its unit. Thus a configuration is a multiset of process objects. Configuration typing uses a directed judgment

$$
\Delta \vdash C :: \Delta',
$$

meaning that $C$ uses every channel in the linear context $\Delta$ and makes every channel in $\Delta'$ available to later clients. A context is a finite collection of distinct assignments such as $a:A$; linearity requires exactly the prescribed provider/client usage.

The three structural rules are

$$
\frac{\Delta \vdash P::(a:A)}
     {\Delta',\Delta\vdash\mathsf{proc}(P)::(\Delta',a:A)}
\;\mathsf{proc}
$$

$$
\frac{\Delta_0\vdash C_1::\Delta_1
\qquad
\Delta_1\vdash C_2::\Delta_2}
{\Delta_0\vdash C_1,C_2::\Delta_2}
\;\mathsf{join}
\qquad
\frac{}{\Delta\vdash\cdot::\Delta}
\;\mathsf{empty}.
$$

The pass-through context $\Delta'$ in `proc` is essential: channels made available before $P$ but unused by $P$ remain available afterward. The tempting rule that concludes only $(a:A)$ would incorrectly discard them. The `join` rule composes interfaces; it requires a provider to appear before a client in the *typing derivation*. This derivation order is not a runtime sequence, because configurations themselves are commutative multisets.

For each internal channel, a well-formed configuration has exactly one provider and one client. A channel at the left interface has its provider outside the configuration; a channel at the right interface has its client outside. Fresh channels created by spawn preserve this ownership condition.

The exchange lemma reconciles multiset execution with directed typing: if $P$ provides $a$ and the following process $Q$ does not use $a$, their process objects can be swapped in the typing derivation. Repeating exchange moves a provider next to its actual client, or to the right edge if the channel is external. Crucially, one may not exchange a provider past a process that uses its channel.

### 4. Preservation

Internal session types evolve after communication: after a label is exchanged, both endpoints continue at the selected branch type. Preservation therefore does **not** say that every internal channel keeps one unchanging type. It says that both endpoints evolve consistently while the external interfaces remain fixed.

**Preservation theorem.** If $\Delta\vdash C::\Delta'$ and $C\longrightarrow D$, then $\Delta\vdash D::\Delta'$.

The proof is by cases on the reduction: spawn (the operational form of cut), forwarding (identity), call expansion, and connective-specific interaction. In a spawn case, inversion of the process typing separates the spawned provider and its client; global freshness permits the same new name to replace the bound formal channel in both derivations. In an interaction case, exchange first places the provider beside its client in the typing derivation. Inversion then exposes dual send/receive rules with matching message and continuation types. After communication, the two continuation derivations compose with the same surrounding interfaces.

For a channel-passing interaction, suppose the adjacent processes are

$$
\mathsf{proc}(\mathsf{send}\;a\;b;P),
\mathsf{proc}(\mathsf{recv}\;a\;(y\Rightarrow Q(y))).
$$

They reduce to $\mathsf{proc}(P),\mathsf{proc}(Q(b))$. Typing inversion tells us that the first continuation and the substituted second continuation agree on the evolved type of $a$, while ownership of $b$ is transferred to the receiver. The bureaucratic rearrangement of contexts implements the same invariant as preservation of the conclusion in principal cut reduction.

### 5. Progress

Because calls may unfold forever, safety cannot promise termination. It instead excludes internal communication mismatch and internal deadlock for configurations closed on the left.

**Progress theorem.** If $\cdot\vdash C::\Delta$, then either $C$ is final or there exists $D$ such that $C\longrightarrow D$.

“Closed on the left” means $C$ has no dependencies on providers outside itself. A final configuration is one in which every process is poised to communicate along a channel in the external interface $\Delta$. Since an external channel has no peer inside $C$, blocking there is legitimate.

The proof is a right-to-left induction over configuration typing. If the prefix can step, the whole configuration can step. If the prefix is final, inspect the last process. Spawn, forwarding, and call forms step directly. If the last process uses a channel $a$, typing and left-closedness ensure that some earlier process provides $a$. Because that prefix is final, its provider is poised on $a$; inversion guarantees complementary actions, so the pair reduces. If instead the last process is poised on a channel it provides to $\Delta$, it contributes to finality. Each communication case echoes a principal cut reduction.

### 6. Observation

A final state is not necessarily a fully materialized value. If $a$ has a positive type, the environment can receive the message waiting on $a$, after which the provider resumes until it reaches the next observable action. Observation is therefore interactive and may evolve the *observed* external type. Receiving label $\mathsf{stop}$ from $a:\mathsf{stream}$ changes the interface entry to $a:\mathbf 1$; receiving $\mathsf{more}$ leaves it at $a:\mathsf{stream}$.

Positive constructors—internal choice $\oplus$, tensor $\otimes$, and unit $\mathbf 1$—put the next send under the provider’s control, so an observer can record that send. At a negative constructor—external choice or linear implication—the provider is waiting for input. No single passive observation reveals its behavior. External choice could be probed once per label, but a received-channel argument may itself have unboundedly many behaviors. The chosen observation procedure consequently stops at negative types, just as an evaluator normally treats a function value as opaque until an argument is supplied.

### 7. Refactoring the Dynamics

The syntax can factor connective-specific actions into generic messages and continuations:

$$
\begin{aligned}
P,Q ::= {}& x^A\leftarrow P(x);Q(x)
\mid \mathsf{fwd}\;x\;y
\mid \mathsf{send}\;x\;m;P\\
&\mid \mathsf{recv}\;x\;K
\mid \mathsf{call}\;p\;x\;\vec y,\\[2mm]
m ::= {}& () \mid k \mid y,\\
K ::= {}& (()\Rightarrow P)
\mid (\ell\Rightarrow P_\ell)_{\ell\in L}
\mid (y\Rightarrow P(y)).
\end{aligned}
$$

The message $m$ is respectively unit, a label, or a channel. A continuation $K$ expects the matching form. Application $m\mathbin{\triangleright}K$ is defined by

$$
()\triangleright(()\Rightarrow P)=P,
\qquad
k\triangleright(\ell\Rightarrow P_\ell)_{\ell\in L}=P_k\;(k\in L),
\qquad
b\triangleright(y\Rightarrow P(y))=P(b).
$$

It is undefined when the forms disagree or a label is absent. All principal communications then share one rule:

$$
\mathsf{proc}(\mathsf{send}\;a\;m;P),
\mathsf{proc}(\mathsf{recv}\;a\;K)
\longrightarrow
\mathsf{proc}(P),\mathsf{proc}(m\triangleright K).
$$

Spawn creates a fresh shared channel, forwarding renames a provider endpoint into the forwarded name, and call unfolds a signature definition. Reasonable implementations may specialize when forwarding fires or add the symmetric forwarding direction; those are design variations consistent with the underlying identity reductions.

## 5. Formal core

The judgments and objects can be summarized as follows:

| Form | Reading |
| --- | --- |
| $\vdash\Sigma\;\mathsf{sig}$ | $\Sigma$ is a valid mutually recursive signature. |
| $\vdash_\Sigma A\;\mathsf{type}$ | $A$ is a well-formed type using names defined in $\Sigma$. |
| $\Delta\vdash P::(x:A)$ | $P$ uses exactly the channels in $\Delta$ and provides $x$ according to $A$. |
| $\Delta\vdash C::\Delta'$ | $C$ transforms the available interface $\Delta$ into $\Delta'$. |
| $C\longrightarrow D$ | Configuration $C$ takes one computation step to $D$. |
| $m\triangleright K$ | Deliver message $m$ to continuation $K$. |

In these forms, $A,B,C$ range over session types (the letter $C$ is also conventionally used for configurations when its syntactic role is clear); $P,Q$ over processes; $C,D$ over configurations; $a,b,x,y$ over channel names; $p$ over process names; $m$ over messages; $K$ over continuations; $\Delta,\Delta',\Delta_i$ over linear channel contexts; $L$ over finite label sets; $k,\ell$ over labels; and $\Sigma$ over signatures. The turnstile $\vdash$ separates used resources from the typed object, `::` separates a process or configuration from what it provides, $\longrightarrow$ is one-step reduction, and $\cdot$ denotes an empty signature, context, or configuration according to position.

The safety invariant is the conjunction of:

1. **Interface preservation:** reduction keeps the left and right boundaries of a configuration typing fixed.
2. **Internal compatibility:** every internally connected provider/client pair has matching current session structure.
3. **Ownership:** every internal linear channel has one provider and one client.
4. **No unexplained stuck state:** a left-closed well-typed configuration either reduces or waits only at its right boundary.

Progress depends on the typing discipline and the left-closed hypothesis; preservation applies to open configurations as long as the initial configuration is typed.

## 6. Operational/computational reading

Configuration typing is best read as a pipeline of ownership rather than as a sequential scheduler. A derivation orders providers before their clients so the output context of one fragment can become the input context of the next. Runtime may choose any enabled adjacent communication after harmless exchanges.

Each reduction has a proof-theoretic shadow:

- spawn exposes the two sides of a cut on a globally fresh channel;
- forwarding eliminates an identity link by renaming the remaining endpoint;
- call expands a process definition and may repeat forever;
- send/receive applies a message to the receiver’s continuation, corresponding to a principal connective reduction.

The theorems jointly guarantee communication safety, not fairness. They do not say which enabled pair the runtime selects, that every process eventually runs, that recursion terminates, or that an external environment will respond.

## 7. Worked derivation or trace in original notation and prose

Consider an original protocol

$$
\mathsf{signal}=\oplus\{\mathsf{ready}:\mathbf 1,\;\mathsf{retry}:\mathsf{signal}\}.
$$

Let $\mathsf{announce}(x)$ provide $x:\mathsf{signal}$ by sending `ready` and then offering unit on $x$. Let $\mathsf{relay}(x,z)$ use $x:\mathsf{signal}$, accept either label, and provide $z:\mathsf{signal}$; on `ready` it sends `ready` on $z$ and relays the final unit, while on `retry` it calls itself. The composite main process is

$$
M(z)=x^{\mathsf{signal}}\leftarrow
\mathsf{announce}(x);\mathsf{relay}(x,z).
$$

Its process typing has the cut shape

$$
\frac{\cdot\vdash\mathsf{announce}(x)::(x:\mathsf{signal})
\qquad
x:\mathsf{signal}\vdash\mathsf{relay}(x,z)::(z:\mathsf{signal})}
{\cdot\vdash M(z)::(z:\mathsf{signal})}.
$$

The initial configuration therefore satisfies

$$
\cdot\vdash\mathsf{proc}(M(a))::(a:\mathsf{signal}).
$$

Now trace it:

1. **Spawn.** Choose globally fresh $b$:
   $$
   \mathsf{proc}(M(a))
   \longrightarrow
   \mathsf{proc}(\mathsf{announce}(b)),
   \mathsf{proc}(\mathsf{relay}(b,a)).
   $$
   The new $b$ is internal, with one provider and one client. The external interface remains $(a:\mathsf{signal})$.
2. **Label interaction.** The provider sends `ready`; the client has a `ready` branch:
   $$
   \longrightarrow
   \mathsf{proc}(\mathsf{close}(b)),
   \mathsf{proc}(\mathsf{readyThenRelayClose}(b,a)).
   $$
   Both sides now treat $b$ at $\mathbf 1$.
3. **Unit interaction.** The unit on $b$ is consumed, eliminating the private session:
   $$
   \longrightarrow
   \mathsf{proc}(\mathsf{readyThenClose}(a)).
   $$
4. **Finality.** The remaining process is poised to send `ready` on external $a$. It cannot reduce internally, so the configuration is final—not stuck.
5. **Observation.** An external observer receives `ready`. The observed interface evolves from $a:\mathsf{signal}$ to $a:\mathbf 1$; receiving the final unit completes the observation.

At every internal step preservation re-establishes $\cdot\vdash C_i::(a:\mathsf{signal})$. The interface changes only when the external observer is deliberately composed with the configuration.

## 8. Conceptual synthesis

Cut elimination supplies the local reason communication is type correct; configuration typing turns that local fact into a global runtime invariant. Recursion removes the termination conclusion but not the compatibility of each step. Progress then converts the absence of an internal mismatch into a structural claim about the whole configuration: any inability to move is accounted for by an exposed service boundary.

Observation completes the programming-language view. A session-typed result is not an inert value but a protocol. Positive structure can be consumed as emitted data, one message at a time. Negative structure is an awaiting capability whose behavior is meaningful only under interaction. This distinction prepares the “message understood” interpretation of [Lecture 8](Lecture%2008%20-%20Subtyping.md).

## 9. Common confusions and failure modes

- **Preservation freezes every channel type.** It freezes the external interfaces of an internal step. An internal session advances in lockstep at both endpoints.
- **Progress implies termination.** A recursive call can always take another step, so an infinite computation can satisfy progress forever.
- **Final means all processes have disappeared.** A final synchronous configuration can contain processes blocked on external channels.
- **Any blocked configuration is final.** Finality requires every blocked action to be on the provided external interface; an internal mismatch is not final.
- **Configuration comma and `join` are both commutative.** Runtime comma is commutative. Directed composition of typing derivations is not, although exchange validates swaps that do not cross a dependency.
- **The naive `proc` rule is enough.** It loses pass-through channels and prevents later clients from using them.
- **Type unfolding is a runtime event.** Equirecursive unfolding is silent during typing; process-call unfolding is a reduction.
- **A negative value can be completely printed.** A negative provider is waiting for input; passive observation cannot enumerate arbitrary argument behavior.

## 10. Self-test questions with concise answers

1. **Why must a spawned name be globally fresh?** So it has exactly the newly created provider and client and cannot capture or alias an existing channel.
2. **What does $\Delta\vdash C::\Delta'$ assert?** $C$ uses the linear channels in $\Delta$ and provides the channels in $\Delta'$.
3. **Why does `proc` carry a context $\Delta'$ unchanged?** Those channels are available before the process and unused by it, so they remain available to later clients.
4. **What changes during a label communication?** The internal channel advances from the choice type to the selected continuation type at both endpoints.
5. **Why is left-closedness used in progress?** It guarantees that a channel used by the last process has its provider inside the preceding configuration.
6. **Can preservation hold for a diverging program?** Yes. It is a per-step invariant and makes no termination claim.
7. **When is $m\triangleright K$ undefined?** When message and continuation forms disagree or a sent label has no corresponding branch.
8. **Why stop observation at linear implication?** The provider awaits a channel whose possible behaviors cannot generally be exhausted by passive probing.

## 11. Related concept pages

- [Preservation and Progress](../Concepts/Preservation%20and%20Progress.md) isolates the two safety theorems and their proof obligations.
- [Configuration Typing and Observation](../Concepts/Configuration%20Typing%20and%20Observation.md) develops directed configuration composition, finality, and observable behavior.
- [Session Subtyping](../Concepts/Session%20Subtyping.md) relaxes exact endpoint equality while retaining the “message understood” invariant.

## 12. Source trail

- Frank Pfenning, *15-836 Substructural Logics*, Lecture 7, “Preservation and Progress,” September 19, 2023.
- Numbered sections: 1 “Introduction”; 2 “Integrating Recursion”; 3 “Typing Configurations of Processes”; 4 “Preservation”; 5 “Progress”; 6 “Observation”; 7 “Refactoring the Dynamics.”
- Printed pages: L7.1–L7.10.
- PDF pages: 78–87.

## 13. Previous/next navigation

Previous: [Lecture 6: Linear Message Passing II](Lecture%2006%20-%20Linear%20Message%20Passing%20II.md).

Next: [Lecture 8: Subtyping](Lecture%2008%20-%20Subtyping.md).

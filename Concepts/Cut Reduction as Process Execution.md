---
title: "Cut Reduction as Process Execution"
aliases:
  - "Operational Cut Reduction"
  - "Proof Reduction as Communication"
tags:
  - cut-reduction
  - operational-semantics
  - concurrency
source_lectures:
  - 5
  - 6
prerequisites:
  - "Cut and identity elimination"
  - "Linear Message Passing and Session Types"
related:
  - "Linear Message Passing and Session Types"
  - "Session Connectives and Channel Passing"
---

# Cut Reduction as Process Execution

## 1. One-sentence definition

**Cut reduction becomes process execution when a cut is read as a provider and client running in parallel on a private channel and the proof's principal or identity reductions are read as their communication or rewiring steps.**

## 2. Why the concept is needed

The slogan “proofs are programs” is incomplete until proof transformation explains computation. In a sequent calculus, cut is the constructor that connects a proof of $A$ to a proof that uses $A$. Under the process interpretation, it is exactly the place where a provider and client meet. Reducing the cut therefore supplies an operational semantics grounded in logical normalization.

This view also distinguishes three phenomena often conflated in process calculi: allocating a fresh private connection, exchanging a message over an existing connection, and removing a forwarding indirection. All descend from cut and its reductions, but they are different runtime events.

## 3. Intuitive model

**Intuition.** Picture cut as plugging a device's output socket into another device's matching input socket. A principal reduction is a compatible handshake at that socket. An identity reduction removes a perfect extension cable. A permuting reduction merely redraws independent internal wiring so the handshake is visible; it need not count as a user-observable event.

The analogy should not be pushed into shared buses: the cut channel is private and linear, so precisely two endpoints participate.

## 4. Formal core

The typed cut is

$$
\frac{\Delta\vdash P::(x:A)\qquad
      \Delta',x:A\vdash Q::(z:C)}
     {\Delta,\Delta'\vdash P\parallel_xQ::(z:C)}\;\mathsf{cut}.
$$

$P$ is the provider of channel $x$ at protocol $A$. $Q$ is its client and provides some external channel $z:C$. $\Delta$ and $\Delta'$ are disjoint linear contexts of other channels used by the two processes. $P\parallel_xQ$ is parallel composition with $x$ bound privately. The conclusion hides $x$ because it is internal to the composition.

For internal choice $\oplus\{\ell:A_\ell\}_{\ell\in L}$, a principal cut meets $\oplus R$ with $\oplus L$:

$$
(\mathsf{send}\ x\ k;P)\parallel_x
\mathsf{recv}\ x(\ell\Rightarrow Q_\ell)_{\ell\in L}
\longrightarrow
P\parallel_xQ_k
\qquad(k\in L).
$$

$L$ is the finite legal-label set, $k$ is the chosen label, $P$ is the provider continuation at $A_k$, and $Q_k$ is the matching client continuation. The private channel $x$ remains connected but its residual type changes from the whole choice to $A_k$.

For unit, principal reduction removes the completed private session:

$$
\mathsf{send}\ x\ ()\parallel_x
\mathsf{recv}\ x(()\Rightarrow Q)
\longrightarrow Q.
$$

$()$ is the unique unit message. There is no provider continuation because $1$ is finished.

Identity is forwarding:

$$
x:A\vdash\mathsf{fwd}\ y\ x::(y:A).
$$

Its two cut orientations reduce by capture-avoiding renaming:

$$
P(x)\parallel_x\mathsf{fwd}\ y\ x\longrightarrow P(y),
\qquad
\mathsf{fwd}\ x\ y\parallel_xQ(x)\longrightarrow Q(y).
$$

The notation $P(y)$ means the former occurrences of connected endpoint $x$ have been renamed to $y$ so the external interface is preserved. This is not message copying.

At runtime, a configuration $\mathcal C$ is an unordered multiset of objects $\mathsf{proc}(P)$. A transition $\mathcal C\longrightarrow\mathcal C'$ consumes the objects named in one rule and inserts their continuations. For example:

$$
\mathsf{proc}(\mathsf{send}\ a\ k;P),
\mathsf{proc}(\mathsf{recv}\ a(\ell\Rightarrow Q_\ell)_{\ell\in L})
\longrightarrow
\mathsf{proc}(P),\mathsf{proc}(Q_k).
$$

$a$ is a concrete runtime channel; it corresponds to a source variable after fresh-name allocation.

## 5. How to use/read it

To derive an execution step, first locate two process objects whose outer actions are complementary on the same channel. Verify that their current session types arise from the matching right and left rules. Consume both prefixes, select or substitute the appropriate continuations, and leave unrelated configuration objects untouched.

Spawn is the operational reading of source-level cut construction:

$$
\mathsf{proc}(x^A\leftarrow P(x);Q(x))
\longrightarrow
\mathsf{proc}(P(a)),\mathsf{proc}(Q(a)),
$$

where $a$ is globally fresh. This step creates connectivity but exchanges no message. Subsequent complementary actions on $a$ perform principal reductions. If one side is a forwarder, an identity reduction rewires instead.

Permuting cut reductions are different. They commute a cut past a rule unrelated to the cut formula. Operationally they justify rearranging independent process structure or treating terms as equal; Lectures 5-6 do not count them as message steps.

## 6. Worked example

Let

$$
\mathsf{gate}=\oplus\{\mathsf{open}:1,\mathsf{closed}:1\}.
$$

A source term spawns a provider that chooses $\mathsf{open}$ and a client that maps either state to a result protocol

$$
\mathsf{result}=\oplus\{\mathsf{pass}:1,\mathsf{wait}:1\}.
$$

Write the source composition abstractly as

$$
g^{\mathsf{gate}}\leftarrow
(\mathsf{send}\ g\ \mathsf{open};\mathsf{send}\ g\ ());Q(g).
$$

Step 1, allocation: choose a name $a$ absent from the entire current configuration.

$$
\mathsf{proc}(g^{\mathsf{gate}}\leftarrow P(g);Q(g))
\longrightarrow
\mathsf{proc}(P(a)),\mathsf{proc}(Q(a)).
$$

Step 2, label synchronization: $P(a)$ sends $\mathsf{open}$ and $Q(a)$ branches. The two objects become the provider's close action and the client's open continuation. Channel $a$ now has residual type $1$ on both sides.

$$
\mathsf{proc}(\mathsf{send}\ a\ \mathsf{open};\mathsf{send}\ a\ ()),
\mathsf{proc}(\mathsf{recv}\ a(\mathsf{open}\Rightarrow Q_o\mid
\mathsf{closed}\Rightarrow Q_c))
\longrightarrow
\mathsf{proc}(\mathsf{send}\ a\ ()),\mathsf{proc}(Q_o).
$$

Step 3, unit synchronization: if $Q_o=\mathsf{recv}\ a(()\Rightarrow \mathsf{send}\ r\ \mathsf{pass};\mathsf{send}\ r\ ())$, then

$$
\mathsf{proc}(\mathsf{send}\ a\ ()),\mathsf{proc}(Q_o)
\longrightarrow
\mathsf{proc}(\mathsf{send}\ r\ \mathsf{pass};\mathsf{send}\ r\ ()).
$$

The private name $a$ vanishes at protocol completion. The external channel $r:\mathsf{result}$ is unchanged by the internal steps. If the surrounding configuration also contains a complementary pair on unrelated channel $b$, that pair may reduce before, after, or between these steps.

## 7. Non-example or boundary case

Two sends on the same channel do not form a principal redex:

$$
\mathsf{proc}(\mathsf{send}\ a\ k;P),
\mathsf{proc}(\mathsf{send}\ a\ j;Q).
$$

They are not complementary right/left actions and should not be assigned an invented collision rule. A well-typed closed configuration built from the session rules should not connect such endpoints at the same protocol state.

Likewise, fresh-name allocation is not allowed to choose an $a$ already occurring in an unrelated object. Local freshness relative only to $P$ and $Q$ could capture a third endpoint and destroy privacy.

Finally, process execution is not identical to full proof normalization. Principal and identity reductions are operational; permuting conversions may represent equality; recursive calls may unfold forever, so execution need not reach a cut-free normal form.

## 8. Key consequences

- Communication rules can be read directly from matching left/right introductions.
- The residual cut type records the remaining protocol after a message.
- The conclusion's external interface stays fixed across internal reductions.
- Identity has computational content as endpoint forwarding.
- Multiset closure exposes concurrency: unrelated processes survive a local step unchanged.
- Fresh-name generation preserves the privacy and binary ownership of cut channels.

These observations motivate, but do not themselves prove, later preservation and progress theorems for configurations.

## 9. Relations to nearby concepts

[Linear Message Passing and Session Types](Linear%20Message%20Passing%20and%20Session%20Types.md) supplies the broader propositions/protocols and proofs/processes correspondence. Cut reduction is its dynamic component.

[Session Connectives and Channel Passing](Session%20Connectives%20and%20Channel%20Passing.md) determines which principal redexes exist for labels and channels. Its focus is protocol vocabulary and ownership transfer; this page focuses on the reduction mechanism, configurations, freshness, and forwarding.

Proof normalization aims to transform derivations, often eliminating all cuts. Process execution preserves strategically placed cuts because they are active private connections, includes recursive unfolding beyond finite proofs, and distinguishes observable communication from equality-like permutations.

See [Lecture 5](../Lectures/Lecture%2005%20-%20Linear%20Message%20Passing%20I.md) for the proof reductions and [Lecture 6](../Lectures/Lecture%2006%20-%20Linear%20Message%20Passing%20II.md) for their multiset formulation.

## 10. Common mistakes

- Calling every cut reduction a message event.
- Forgetting that spawn needs a name fresh in the whole configuration.
- Dropping the unchanged configuration around a local multiset rewrite.
- Failing to update the private channel's residual type after a label or channel action.
- Treating forwarding as a process that reads and copies each message.
- Confusing source variables $x,y$ with allocated runtime names $a,b$.
- Assuming that the existence of cut elimination proves termination of recursive process execution.
- Renaming endpoints without avoiding variable capture.

## 11. What to remember

- Cut is a private provider-client connection, not merely a proof artifact.
- Principal reductions are synchronizations; identity reductions are rewiring.
- Spawn allocates, while send/receive communicates.
- Configurations are multisets, so independent redexes have no forced order.
- External types remain stable even while private residual protocols advance.

## 12. Source trail

- Lecture 5, sections 2-4 and 6-8; printed pages L5.2-L5.10; PDF pages 55-63.
- Lecture 6, section 2 and the dynamics summary in section 10/Figure 2; printed pages L6.1-L6.2 and L6.10-L6.12; PDF pages 66-67 and 75-77.

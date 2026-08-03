---
title: Preservation and Progress
aliases:
  - Type Safety
  - Session Fidelity and Deadlock Freedom
tags:
  - type-safety
  - session-types
  - metatheory
source_lectures:
  - 7
prerequisites:
  - Configuration typing
  - Process reduction
related:
  - Configuration Typing and Observation
  - Session Subtyping
---

# Preservation and Progress

## 1. One-sentence definition

**Preservation and progress are the paired type-safety properties saying that a typed configuration retains its external interface after every internal reduction and, when closed on the left, can either reduce or is legitimately waiting only at that interface.**

## 2. Why the concept is needed

The proof/process correspondence explains individual communication rules, but a programmer needs a statement about arbitrary runtime configurations. Spawning creates many concurrent processes; forwarding changes names; recursion may unfold forever; and communication advances internal session types. Without a global invariant, a well-typed starting process might conceivably evolve into a state where one endpoint sends a label and the other expects a channel, or into an unexplained internal deadlock.

Cut elimination cannot simply be reused as “the program terminates.” General recursion invalidates that conclusion. The appropriate safety decomposition is therefore:

- preservation excludes type corruption from each step;
- progress classifies every well-typed, left-closed state as reducible or observably final.

## 3. Intuitive model

**Intuition.** Imagine a network of one-use contracts. Each internal wire joins exactly one supplier to one customer. A communication consumes the current clause of the wire’s contract and reveals its continuation clause to both parties. Preservation says the two copies of every internal contract advance together and the contracts advertised at the boundary do not change. Progress says a sealed network cannot be silently jammed inside: if it does not move, all remaining workers are waiting at sockets deliberately exposed to the environment.

The model is only intuition. The actual statements concern typing derivations and one-step reduction, not physical wires, scheduling fairness, or elapsed time.

## 4. Formal core

A process judgment

$$\Delta\vdash P::(x:A)$$

says that process $P$ uses exactly the channels assigned types by the linear context $\Delta$ and provides channel $x$ according to session type $A$. A configuration judgment

$$\Delta\vdash C::\Delta'$$

says configuration $C$ uses the input interface $\Delta$ and provides the output interface $\Delta'$. Here $C,D$ range over configurations; $P$ over processes; $x$ over channels; $A$ over session types; and $\Delta,\Delta'$ over finite linear contexts of distinct channel/type assignments. The symbol $\vdash$ separates required resources from the typed object, `::` introduces what is provided, and $C\longrightarrow D$ denotes one internal computation step.

**Preservation theorem.**

$$
\text{If }\Delta\vdash C::\Delta'\text{ and }C\longrightarrow D,
\text{ then }\Delta\vdash D::\Delta'.
$$

The fixed boundary does not imply that internal channel types are textually fixed. If two endpoints communicate along $a:A_1\otimes A_2$, the channel $a$ advances to $A_2$ on both sides. Because $a$ is internal, it appears in neither outer interface.

A configuration is **left-closed** when its input context is empty: $\cdot\vdash C::\Delta$. It is **final** when every resident process is poised to communicate on a channel in the provided external interface $\Delta$.

**Progress theorem.**

$$
\text{If }\cdot\vdash C::\Delta,
\text{ then either $C$ is final or }C\longrightarrow D\text{ for some }D.
$$

Preservation is proved by cases on spawn, forward, call, and communication reductions. Progress is proved by induction over configuration typing, using inversion to show that a process blocked on an internal channel has a complementary typed peer.

## 5. How to use/read it

Use preservation as an invariant when following a trace: after each internal arrow, re-establish the same external judgment. Internal assignments may disappear or evolve, but ownership and endpoint compatibility must remain derivable.

Use progress only after checking the hypotheses. The left context must be empty. If the configuration cannot step, inspect every poised action: its subject must be a right-interface channel. Such a state is waiting for an observer or client, not suffering an internal type error.

Together the theorems justify the phrase “well typed programs do not get stuck,” where “stuck” is carefully restricted to an unaccounted-for internal blockage.

## 6. Worked example

Define a fresh protocol

$$\mathsf{answer}=\oplus\{\mathsf{yes}:\mathbf1,\mathsf{no}:\mathbf1\}.$$

Let $V(b)$ provide $b:\mathsf{answer}$ by selecting `yes` and then sending unit. Let $R(b,a)$ use $b:\mathsf{answer}$ and provide $a:\mathsf{answer}$ by relaying the selected label and closing handshake. Start from a cut process that privately connects them:

$$
C_0=\mathsf{proc}(b^{\mathsf{answer}}\leftarrow V(b);R(b,a)).
$$

Assume its derivation concludes $\cdot\vdash C_0::(a:\mathsf{answer})$.

1. Spawn chooses a globally fresh $c$:
   $$
   C_0\longrightarrow
   C_1=\mathsf{proc}(V(c)),\mathsf{proc}(R(c,a)).
   $$
   Inversion of the cut typing gives a $c$-provider and a $c$-client, so $\cdot\vdash C_1::(a:\mathsf{answer})$.
2. The `yes` send meets the receiver’s `yes` branch. Both sides advance $c$ to $\mathbf1$:
   $$C_1\longrightarrow C_2.$$
   The external judgment is again $\cdot\vdash C_2::(a:\mathsf{answer})$.
3. The private unit handshake removes the remaining work on $c$. The relay becomes poised to send `yes` on $a$, giving $C_2\longrightarrow C_3$ with the same external typing.
4. No internal peer exists for $a$, so $C_3$ cannot reduce alone. It is final because its sole poised action is on the external channel $a$.

Preservation accounts for every arrow; progress accounts for both the enabled internal arrows and the final endpoint.

## 7. Non-example or boundary case

Consider a recursive process whose only action is to call itself with the same channels. Each call expansion produces another well-typed configuration. Preservation holds at every step, and progress holds because a next step always exists, yet the computation never becomes final. Thus neither theorem implies termination.

Also, progress does not apply to $a:A\vdash C::\Delta$. If $C$ waits to receive along the left-interface channel $a$, its provider lies outside the configuration. The wait may be legitimate, but the left-closed theorem cannot classify it using only $C$.

## 8. Key consequences

- No reduction from a typed configuration introduces an endpoint type disagreement.
- Fresh-name creation preserves one-provider/one-client linear ownership.
- A closed typed configuration has no unaccounted internal stuck state.
- Recursive divergence is compatible with safety.
- Finality exposes the runtime boundary at which observation or further client interaction must occur.
- The local principal cases of cut reduction become the central cases of runtime safety proofs.

## 9. Relations to nearby concepts

[Configuration Typing and Observation](Configuration%20Typing%20and%20Observation.md) supplies the directed judgment, final-state definition, and external interaction used in both theorems. It is machinery and semantics; preservation/progress are metatheorems about that machinery.

[Session Subtyping](Session%20Subtyping.md) weakens exact endpoint equality. It must be designed so that the receiver still understands every message; under that condition, preservation and progress can be retained. Subtyping is a compatibility relation, not itself a reduction theorem.

Proof normalization is stronger than these safety properties in one direction and less directly operational in another. Normalization includes termination for the recursion-free proof system; preservation/progress permit infinite execution and classify observable blocking.

## 10. Common mistakes

- Treating preservation as equality of every internal context before and after a step.
- Quoting progress without the empty left context.
- Calling an externally waiting final state “stuck.”
- Inferring termination, fairness, or eventual response from progress.
- Forgetting that global freshness is needed in the spawn case.
- Treating preservation or progress as object-language typing rules rather than metatheorems proved about the rules.

## 11. What to remember

- Preservation fixes external interfaces while internal sessions evolve consistently.
- Progress means “step or wait at the boundary,” not “terminate.”
- Progress requires a left-closed configuration.
- Recursion can diverge safely.
- The two theorems together exclude internal communication errors for typed executions.

## 12. Source trail

- Lecture 7, sections 3 “Typing Configurations of Processes,” 4 “Preservation,” and 5 “Progress.”
- Supporting material: section 2 “Integrating Recursion” and section 6 “Observation.”
- Printed pages: L7.2–L7.9.
- PDF pages: 79–86.
- Full lecture reconstruction: [Lecture 7: Preservation and Progress](../Lectures/Lecture%2007%20-%20Preservation%20and%20Progress.md).

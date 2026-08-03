---
title: "CBA Diagrams and True Concurrency"
aliases:
  - "CBA diagrams"
  - "causal proof diagrams"
  - "true concurrency"
tags:
  - concept
  - proofs
  - concurrency
source_lectures:
  - 2
prerequisites:
  - "Structural, linear, and ordered inference"
related:
  - "Linear Inference"
  - "Ordered Inference"
  - "Nondeterminism Dont-Care vs Dont-Know"
---

# CBA Diagrams and True Concurrency

## 1. One-sentence definition

**A CBA diagram represents proposition occurrences as nodes and rule instances as connecting events, so causal resource flow is explicit and independent events form one truly concurrent proof rather than several order-sensitive interleavings.**

## 2. Why the concept is needed

Tree-shaped proof terms fit single-conclusion inference but become awkward when a rule produces several propositions or none. A sequential trace has the opposite problem: it forces every event into an order, even when two events are independent. CBA diagrams accommodate multiple inputs and outputs while recording only causal constraints.

They also let a reader recover intermediate states as slices through a proof. This ties proof identity to resource flow rather than to an arbitrary scheduler, a perspective useful for later reasoning about parallel and concurrent programs.

## 3. Intuitive model

**Intuition.** Picture a factory diagram. Circles are individual parts, boxes are machines, and wires show which parts each machine consumes and produces. A horizontal cut lists the parts currently available. Machines on disjoint wires can run in either order—or simultaneously—without changing the causal diagram. This is an intuition; structural and ordered systems require additional slice conditions beyond ordinary factory flow.

## 4. Formal core

A CBA diagram contains:

- **proposition nodes** $v$, each labeled by a proposition and representing one occurrence;
- **event boxes** $e$, each labeled by an instantiated inference rule;
- incoming edges $v\to e$ from the event’s premise occurrences;
- outgoing edges $e\to v'$ to the event’s conclusion occurrences.

The transitive closure of these edges defines causal precedence, written $e_1<e_2$, when an output or enabling consequence of $e_1$ is required by $e_2$. Two events are concurrent when neither $e_1<e_2$ nor $e_2<e_1$, subject to the structural discipline.

For a **linear** diagram, a slice is a frontier containing the live nodes after some causally closed set of events. Moving the slice across an enabled event removes its input nodes and adds its output nodes.

For an **ordered** diagram, slice nodes inherit left-to-right order. Inputs must be adjacent, and wires cannot be freely crossed. If deleting an intervening segment enables a later zero-output cancellation, the diagram must record that adjacency dependency even though there is no ordinary produced proposition to connect.

For a **structural** diagram, facts persist. A slice is therefore upward/ancestor closed rather than a frontier that forgets consumed inputs. Multiple proofs of one fact and contraction make complete formalization subtler; Lecture 2 presents the structural version as an informative construction, not a finished definition.

Different topological sorts of the same causal partial order are interleavings of one true-concurrent proof. A diagram with an extra consume-produce detour is a different proof even if its initial and final slices coincide.

## 5. How to use/read it

Read from causes toward effects. For each box, identify its exact input occurrences and output occurrences. To find a state, draw a cut that respects causality and the relevant context discipline. To compare two sequential traces, ask whether swapping adjacent independent events leaves the same nodes, boxes, and dependencies. If so, the traces are two linearizations of one diagram.

Do not quotient choices that compete for the same occurrence. Those are alternative proofs, not independent schedules. Likewise, in ordered inference check adjacency, not merely direct data flow.

## 6. Worked example

Suppose two independent preparation rules feed one assembly rule:

$$
\frac{a}{x}\;e_x
\qquad
\frac{b}{y}\;e_y
\qquad
\frac{x\quad y}{z}\;e_z.
$$

From the linear state $[a,b]$, the causal picture is:

```text
a       b
|       |
[e_x] [e_y]
|       |
x       y
 \     /
  [e_z]
    |
    z
```

1. The initial slice is `[a,b]`.
2. Moving past only $e_x$ gives `[x,b]`; moving past only $e_y$ gives `[a,y]`.
3. Moving past both, in either order, gives `[x,y]`.
4. Only then is $e_z$ enabled, yielding `[z]`.

$e_x$ and $e_y$ are concurrent because neither consumes or produces a node needed by the other. $e_z$ causally follows both. The sequential traces $e_x;e_y;e_z$ and $e_y;e_x;e_z$ are not two causally different proofs.

## 7. Non-example or boundary case

From a single occurrence `[a]`, suppose both $a\to x$ and $a\to y$ are enabled. The two events compete for the same node. They cannot both appear as independent events in one execution diagram; choosing one removes the input required by the other. This is don’t-know branching unless the specification deliberately identifies the outcomes.

For ordered inference, two cancellations may appear to have disjoint labels but still be dependent if the second pair becomes adjacent only after the first deletion. Absence of a producer-consumer wire is not sufficient evidence of independence.

## 8. Key consequences

- Multiple- and zero-conclusion rules receive a natural proof representation.
- Slices recover legal intermediate states from one proof diagram.
- Causality is a partial order, not necessarily a total schedule.
- Independent interleavings can be identified as one proof.
- Resource competition remains a real alternative.
- Ordered adjacency and structural persistence require specialized slice conditions.

## 9. Relations to nearby concepts

[Linear Inference](Linear%20Inference.md) supplies the clearest node-consumption and production reading. [Ordered Inference](Ordered%20Inference.md) adds noncrossing order and adjacency causality. [Structural Inference](Structural%20Inference.md) requires persistent, ancestor-closed slices. [Nondeterminism Dont-Care vs Dont-Know](Nondeterminism%20Dont-Care%20vs%20Dont-Know.md) distinguishes reorderings of independent events from genuine choice. [State Saturation and Quiescence](State%20Saturation%20and%20Quiescence.md) describes closure or terminality, while a CBA diagram describes one proof’s internal causal structure.

## 10. Common mistakes

- Treating every sequential ordering as a distinct proof.
- Calling events independent when they compete for one occurrence.
- Drawing one node for a proposition label that actually occurs twice linearly.
- Reading a slice as an arbitrary horizontal set of nodes without causal closure.
- Ignoring ordered adjacency dependencies created by deletion.
- Treating the informal structural-diagram account as a completed formal theory.

## 11. What to remember

- Nodes are proposition occurrences; boxes are rule instances.
- Wires record consumption, production, and causal dependence.
- A slice represents a state compatible with the diagram.
- True concurrency forgets the order of independent events, not genuine choices.
- Linear, ordered, and structural diagrams need different slice disciplines.

## 12. Source trail

- Lecture 2, §1 “Introduction,” printed p. L2.1, PDF p. 13.
- Lecture 2, §2 “CBA Diagrams for Substructural Proofs,” printed pp. L2.2–L2.3, PDF pp. 14–15.
- Lecture 2, §3 “CBA Diagrams and True Concurrency,” printed pp. L2.3–L2.5, PDF pp. 15–17.
- Lecture 2, §4 “CBA Diagrams for Structural Inference,” printed pp. L2.5–L2.6, PDF pp. 17–18.


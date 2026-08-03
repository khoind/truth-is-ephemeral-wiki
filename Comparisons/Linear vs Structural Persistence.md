---
title: Linear vs Structural Persistence
aliases: [persistence comparison, reusable versus ephemeral resources]
tags: [comparison, persistence, linearity, structural-logic, operational-semantics]
source_lectures: ["Lecture 09 - Validity", "Lecture 10 - A Mixed Linear/Nonlinear Logic", "Lecture 15 - Adjoint SAX"]
prerequisites: [Validity, contexts, multiset rewriting]
related: [Mixed Linear-Nonlinear Logic, Adjoint Logic, Adjoint SAX Message Sequences and Pattern Matching]
---

# Linear vs Structural Persistence

## One-sentence definition

**Linear persistence means an item remains only until its unique use consumes or transforms it, while structural persistence means it may remain available across zero, one, or many uses because weakening and contraction are permitted.**

## Why the concept is needed

“Persistent” is overloaded. It may describe a logical assumption that can be reused, a runtime object retained after a transition, or a channel whose name stays stable while its protocol advances. These are not equivalent. Linear logic can model a long-lived process that must nevertheless have exactly one client; structural logic can model a service used many times even when each spawned session is short. Keeping the axes distinct prevents unsound operational rules and misleading implementation claims.

## Intuitive model

**Intuition.** A linear subscription card may last for years but can be transferred or closed exactly once at each protocol step. A structural service directory may be consulted by any number of clients. Duration concerns time; structural persistence concerns admissible multiplicity.

## Formal core

For a linear context $\Delta$, a judgment $\Gamma;\Delta\vdash A$ must account for each occurrence of $B\in\Delta$ exactly once. For structural $\Gamma$, weakening and contraction are admissible:

$$
\frac{\Gamma\vdash C}{\Gamma,B\vdash C}\;W
\qquad
\frac{\Gamma,B,B\vdash C}{\Gamma,B\vdash C}\;C.
$$

Bottom-up, weakening permits ignoring $B$ and contraction permits using it in multiple branches. In multiset rewriting, a linear fact is consumed by a matching transition, while a persistent fact is copied unchanged to the result. If an upshifted structural provider receives a request, the intended transition is schematically

$$
\underline{\mathsf{proc}(a_S,P)},\;\mathsf{request}(a_S,b_L)
\longrightarrow
\underline{\mathsf{proc}(a_S,P)},\;\mathsf{proc}(b_L,P_b),
$$

where the underline marks a persistent semantic object, $a_S$ is a structural channel, and fresh $b_L$ begins one linear session. The provider remains; the request is consumed.

| Dimension | Linear persistence | Structural persistence |
|---|---|---|
| Logical location | Linear multiset $\Delta$ | Structural set/context $\Gamma$ |
| Allowed uses | Exactly one | Zero, one, or many |
| Runtime rewrite | Consumed or replaced | May remain after matching |
| Typical channel | One client/session | Shared provider/server |
| Duplication | Forbidden for the resource | Authorized by contraction |
| Dropping | Forbidden for the resource | Authorized by weakening |
| Longevity | May be arbitrarily long | May also be short or long |

## How to use/read it

Ask two separate questions. First, what structural rules does the type’s mode allow? Second, what does this operational transition retain? A linear process can persist through many transitions by being replaced with its continuation exactly once. A structural provider can be retained while spawning a fresh linear continuation for each client. Persistence annotations in a runtime semantics must follow the mode discipline established by typing.

## Worked example

Consider a structural doubling service $d_S:\uparrow(A\multimap A)$ and two linear clients $x_1:A$ and $x_2:A$.

1. Client 1 sends a request on $d_S$ and supplies fresh linear continuation $f_1:A\multimap A$.
2. The request is consumed; the provider for $d_S$ remains because its mode admits contraction.
3. A fresh process offers $f_1$ and consumes $x_1$ exactly once.
4. Independently, client 2 requests $f_2$ from the same $d_S$.
5. The structural provider again remains, while $f_2$ and $x_2$ are linear.

No single linear session was duplicated. Sharing occurred at the structural service boundary, and each use generated a distinct linear interaction.

## Non-example or boundary case

Keeping every `proc` fact after every rewrite does not implement structural persistence; it duplicates linear behavior and can let two receivers consume the same session action. Conversely, consuming a structural provider after its first request gives it linear runtime behavior and can strand other well-typed clients. A stable channel name in synchronous MPASS also does not by itself prove structurality: one linear channel may retain its name while its type changes.

## Key consequences

Structural persistence supports multicast and shared servers; linear persistence supports deterministic ownership and protocol fidelity. Mixed semantics require both sets and multisets, or an equivalent device, because a single consumption policy cannot model both. The monotonicity constraint in adjoint logic ensures that dependencies at higher modes have at least the structural permissions required below.

## Relations to nearby concepts

[Validity](../Concepts/Validity.md) explains why a proof independent of linear resources may be structurally reused. [Mixed Linear-Nonlinear Logic](../Concepts/Mixed%20Linear-Nonlinear%20Logic.md) places the two regimes in separate strata. [Adjoint Logic](../Concepts/Adjoint%20Logic.md) assigns structural properties mode by mode. [Adjoint SAX, Message Sequences, and Pattern Matching](../Concepts/Adjoint%20SAX%2C%20Message%20Sequences%2C%20and%20Pattern%20Matching.md) carries the distinction into asynchronous communication.

## Common mistakes

- Equating “not yet consumed” with “duplicable.”
- Treating a persistent runtime fact as automatically well typed.
- Reusing a continuation channel because its provider is shared.
- Assuming contraction implies weakening; adjoint modes may permit either independently.

## What to remember

- Multiplicity and lifetime are different axes.
- Linear continuations may live long but have one owner.
- Structural providers may serve many fresh linear sessions.
- Runtime persistence must reflect the mode’s structural permissions.

## Source trail

Lecture 9, §§2–3, printed pages L9.1–L9.3, PDF pages 102–104; Lecture 10, §§8–10, printed pages L10.6–L10.9, PDF pages 118–121; Lecture 15, §§1–2, printed pages L15.1–L15.3, PDF pages 159–161. See [Lecture 09 - Validity](../Lectures/Lecture%2009%20-%20Validity.md), [Lecture 10 - A Mixed Linear-Nonlinear Logic](../Lectures/Lecture%2010%20-%20A%20Mixed%20Linear-Nonlinear%20Logic.md), and [Lecture 15 - Adjoint SAX](../Lectures/Lecture%2015%20-%20Adjoint%20SAX.md).

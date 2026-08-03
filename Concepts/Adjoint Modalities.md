---
title: Adjoint Modalities
aliases: [indexed shifts, adjoint shifts]
tags: [modalities, shifts, adjoint-logic, modes, lecture-11]
source_lectures: ["Lecture 11 - Adjoint Logic", "Lecture 15 - Adjoint SAX"]
prerequisites: [Modes and the Dependence Preorder, Shifts Between Logics]
related: [Adjoint Logic, Positive vs Negative Polarity, Adjoint SAX Message Sequences and Pattern Matching]
---

# Adjoint Modalities

## One-sentence definition

**Adjoint modalities are indexed upshifts $\uparrow^m_k$ and downshifts $\downarrow^\ell_m$ that transport propositions between comparable modes under precisely the dependency conditions required by the sequent judgment.**

## Why the concept is needed

Native connectives live at one mode, yet programs and proofs must communicate across usage regimes. A plain coercion would let a reusable proof depend on a linear resource or erase which structural rules are available. Indexed modalities record both endpoints and expose the necessary side conditions. Their adjoint relationship also explains familiar modal operators as composites.

## Intuitive model

**Intuition.** An upshift wraps a lower-mode session behind a higher-mode request interface. A downshift sends a higher-mode object through a lower-mode interaction. The indices are customs checkpoints: a crossing exists only along an allowed edge of the dependency preorder.

## Formal core

Let $m\ge k$ and $\ell\ge m$. $A_k$ is a proposition at mode $k$, $A_\ell$ at mode $\ell$, $C_r$ a conclusion at mode $r$, and $\Delta$ a multiset of mode-annotated assumptions. The upshift rules are

$$
\frac{\Delta\vdash A_k}{\Delta\vdash\uparrow^m_k A_k}\;\uparrow R
\qquad
\frac{k\ge r\quad\Delta,A_k\vdash C_r}
{\Delta,\uparrow^m_k A_k\vdash C_r}\;\uparrow L.
$$

The right rule has no added side condition: well-formedness of the conclusion gives $\Delta\ge m$, and $m\ge k$ implies $\Delta\ge k$. The left rule needs $k\ge r$ because exposing $A_k$ must remain a legal dependency of $C_r$.

The downshift rules are

$$
\frac{\Delta\ge\ell\quad\Delta\vdash A_\ell}
{\Delta\vdash\downarrow^\ell_m A_\ell}\;\downarrow R
\qquad
\frac{\Delta,A_\ell\vdash C_r}
{\Delta,\downarrow^\ell_m A_\ell\vdash C_r}\;\downarrow L.
$$

$\downarrow R$ explicitly prevents a proof at the lower mode from capturing dependencies that cannot support $A_\ell$. Upshift is negative; downshift is positive.

## How to use/read it

Read the superscript/subscript as the source and destination modes specified by the notation: $\uparrow^m_k A_k$ is a proposition at $m$ built from $A_k$, and $\downarrow^\ell_m A_\ell$ is at $m$ built from $A_\ell$. Check comparability before applying a rule. Operationally, a shift message contains a continuation channel at the other mode, so the type-and-mode transition is observable.

## Worked example

Recover the linear exponential in a two-mode signature.

1. Choose $S>L$, $\sigma(S)=\{W,C\}$, and $\sigma(L)=\varnothing$.
2. Start with a linear proposition $A_L$.
3. Form $\uparrow^S_L A_L$, a structural proposition describing a shared interface for fresh $A_L$ sessions.
4. Form $\downarrow^S_L(\uparrow^S_L A_L)$, which is again linear.
5. Define $!A_L\equiv\downarrow^S_L\uparrow^S_L A_L$.
6. A client consumes the outer linear package once to obtain a structural endpoint, then may request arbitrarily many fresh linear $A_L$ sessions through that endpoint.

The composite has the comonadic “derelict, duplicate, extend” behavior associated with $!$, but each step respects the mode boundary.

## Non-example or boundary case

If $m$ and $k$ are incomparable, $\uparrow^m_k A_k$ is not well formed. Nor can $\downarrow R$ use a context that is merely $\ge m$ when some assumption is not $\ge\ell$: the resulting lower-mode package would conceal an illegal higher-mode dependency. Same-mode shifts may also be deliberately ruled out in a particular instance; the general grammar does not force an application to admit them.

## Key consequences

Modal composites recover linear $!$, S4 necessity, and lax logic’s strong monad under different mode signatures. Polarity follows from which side is invertible, improving focused proof search. In SAX, noninvertible shift rules become message axioms while invertible rules remain receives, so modality has a direct session interpretation.

## Relations to nearby concepts

[Modes and the Dependence Preorder](Modes%20and%20the%20Dependence%20Preorder.md) defines legal crossings. [Shifts Between Logics](Shifts%20Between%20Logics.md) is the unindexed LNL special case. [Positive vs Negative Polarity](../Comparisons/Positive%20vs%20Negative%20Polarity.md) explains their asymmetric rules. [Adjoint SAX, Message Sequences, and Pattern Matching](Adjoint%20SAX%2C%20Message%20Sequences%2C%20and%20Pattern%20Matching.md) gives their asynchronous process form.

## Common mistakes

- Dropping indices when more than two modes are present.
- Treating shifts as inverse isomorphisms; an adjunction does not make both composites identities.
- Forgetting $\Delta\ge\ell$ on $\downarrow R$.
- Calling $!$ itself simply positive or negative despite its two opposite shifts.

## What to remember

- Indexed shifts cross only comparable modes.
- Upshift is negative; downshift is positive.
- Side conditions enforce independence, not cosmetic typing.
- Familiar monads and comonads arise from composites.

## Source trail

Lecture 11, §§4–5, printed lecture pages L11.4–L11.6, PDF pages 126–128; Lecture 15, §2, printed pages L15.1–L15.3, PDF pages 159–161. See [Lecture 11 - Adjoint Logic](../Lectures/Lecture%2011%20-%20Adjoint%20Logic.md) and [Lecture 15 - Adjoint SAX](../Lectures/Lecture%2015%20-%20Adjoint%20SAX.md).

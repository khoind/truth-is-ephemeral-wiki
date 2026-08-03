---
title: Session Subtyping
aliases:
  - Behavioral Subtyping for Sessions
  - Message-Understood Subtyping
tags:
  - session-types
  - subtyping
  - coinduction
  - variance
source_lectures:
  - 8
prerequisites:
  - Preservation and Progress
  - Positive and negative session types
related:
  - Preservation and Progress
  - Configuration Typing and Observation
---

# Session Subtyping

## 1. One-sentence definition

**Session subtyping $A\le B$ holds when any provider following $A$ can safely serve a client written for $B$, because every message either side may send is understood by its receiver and the resulting continuations remain similarly related.**

## 2. Why the concept is needed

Requiring both endpoints to use textually equal session types rejects safe, useful refinements. A provider may emit only one of several labels a client accepts. A service may accept more requests than a particular client ever sends. A data-structure protocol may enter a phase with fewer legal operations, and recursive types may encode representation invariants such as positivity or standard form.

Subtyping admits those connections without sacrificing communication safety. It is structural and behavioral: the direction comes from provider/client roles and message flow, not from names or an inheritance declaration.

## 3. Intuitive model

**Intuition.** Treat $B$ as the client’s expectation envelope. An $A$ provider fits inside that envelope if it never produces an output outside the envelope and can accept every input the envelope permits the client to send. After each exchange, the same condition must hold for what remains.

The image is deliberately two-sided. “Fewer cases” is not universally smaller: fewer *outputs* may be safer, while accepting fewer *inputs* may be unsafe.

## 4. Formal core

The judgment $A\le B$ places the provider type $A$ on the left and the client’s view $B$ on the right. $A,B,A_i,B_i$ range over session types; $L,K$ over finite label sets; and $\ell,k$ over labels. The rules are interpreted **coinductively**.

$$
\frac{L\subseteq K\quad A_\ell\le B_\ell\;(\forall\ell\in L)}
{\oplus\{\ell:A_\ell\}_{\ell\in L}\le
 \oplus\{k:B_k\}_{k\in K}}
\qquad
\frac{}{\mathbf1\le\mathbf1}
$$

In internal choice $\oplus$, the provider selects a label, so all provider labels $L$ must be accepted by the client’s set $K$. Unit $\mathbf1$ has only the closing message.

$$
\frac{A_1\le B_1\quad A_2\le B_2}
{A_1\otimes A_2\le B_1\otimes B_2}
$$

In tensor, the provider sends an $A_1$ channel and continues as $A_2$; payload and continuation are covariant.

$$
\frac{L\supseteq K\quad A_k\le B_k\;(\forall k\in K)}
{\&\{\ell:A_\ell\}_{\ell\in L}\le
 \&\{k:B_k\}_{k\in K}}
$$

In external choice $\&$ (printed as $N\{\ldots\}$ in the source lecture), the client selects a label. The provider on the left must accept every label $K$ the right-hand client may send, so width reverses.

$$
\frac{B_1\le A_1\quad A_2\le B_2}
{A_1\multimap A_2\le B_1\multimap B_2}.
$$

In linear implication, the client sends the argument channel. Hence the argument is contravariant, while the continuing session is covariant.

There is no rule when outer constructors differ. Reflexivity $A\le A$, transitivity, and left/right subsumption are admissible metatheorems, not primitive clauses above.

For recursive names, proof search unfolds definitions. If a guarded branch reaches an ordered pair already occurring on that branch, the repeated pair may close a finite cycle representing an infinite proof. “Guarded” means that constructor and message-compatibility checks occur before the recurrence.

## 5. How to use/read it

To decide a proposed $A\le B$:

1. Unfold type names until both outer constructors are visible.
2. Reject immediately if the constructors differ.
3. Identify who sends next.
4. Check that the receiver covers every label or message the sender may choose.
5. Generate continuation obligations with the variance shown above.
6. Accept only if every branch reaches an axiom or a guarded repeated pair; reject a failed branch and record its message path as a counterexample.

Operationally, the rules guarantee that message application $m\triangleright K$ is defined whenever an $A$-provider communicates with a $B$-client.

## 6. Worked example

Define an original pair of recursive output protocols:

$$
\begin{aligned}
\mathsf{log}&=\oplus\{\mathsf{item}:\mathsf{log},\;\mathsf{end}:\mathbf1\},\\
\mathsf{live}&=\oplus\{\mathsf{item}:\mathsf{live}\}.
\end{aligned}
$$

Check $\mathsf{live}\le\mathsf{log}$.

1. Unfold both definitions.
2. Internal-choice width holds because $\{\mathsf{item}\}\subseteq\{\mathsf{item},\mathsf{end}\}$.
3. The `live` provider can choose only `item`, so the sole continuation obligation is $\mathsf{live}\le\mathsf{log}$.
4. This is the guarded ancestor pair. Close it as a cycle.

The finite cyclic certificate denotes an infinite derivation that checks every finite prefix of `item` messages. A `log` client always understands those messages, even though its unused `end` branch is never selected by this provider.

Now reverse the judgment. Internal-choice width would require

$$\{\mathsf{item},\mathsf{end}\}\subseteq\{\mathsf{item}\},$$

which is false. The one-step counterexample is the label `end`: a `log` provider may send it, but a `live` client cannot receive it.

## 7. Non-example or boundary case

The judgment

$$\mathbf1\le A\otimes B$$

does not hold for any $A,B$. The unit provider sends `()`, while the tensor client is prepared to receive a channel. No amount of recursive unfolding or subsumption repairs a mismatch of outer message forms.

A repeated unguarded assumption is also not a proof. Writing $A\le B$ above itself without first exposing compatible constructors would accept unsafe relations and destroy the counterexample interpretation of failure.

## 8. Key consequences

- Output refinements may safely reduce provider-selected alternatives.
- Input-capable services may safely accept more client-selected alternatives.
- Tensor is covariant in both components; implication is contravariant in its argument and covariant in its continuation.
- Recursive compatibility is an absence-of-finite-counterexample property and is naturally coinductive.
- Forwarding can witness a subtype relation through the generalized identity rule.
- Subsumption increases reuse while retaining the message-understood invariant required by type safety.

## 9. Relations to nearby concepts

[Preservation and Progress](Preservation%20and%20Progress.md) are properties of execution. Session subtyping is a relation used inside the typing system; its rules are chosen so those execution properties continue to hold.

[Configuration Typing and Observation](Configuration%20Typing%20and%20Observation.md) fixes the provider-on-left/client-on-right interpretation and explains why compatibility is judged at connected endpoints. Observation concerns what an external environment can reveal; subtyping concerns whether connecting two possibly different interface descriptions is safe.

Ordinary function subtyping is a useful special analogy for $\multimap$ variance, but it does not explain choice width by itself. The decisive fact is always who sends the next message.

## 10. Common mistakes

- Reversing the meaning of $A\le B$: $A$ is the provider’s type, $B$ the client’s view.
- Applying subset width to both $\oplus$ and $\&$.
- Making the argument of $\multimap$ covariant.
- Checking only first labels and ignoring continuation types.
- Closing a cycle without a guarded repetition of the same ordered pair.
- Adding a rule between different outer constructors.
- Calling reflexivity and transitivity primitive when the presentation establishes them as admissible.

## 11. What to remember

- “Every message is understood” determines all rule directions.
- Provider-selected choice uses $L\subseteq K$; client-selected choice uses $L\supseteq K$.
- $\otimes$ is covariant/covariant; $\multimap$ is contravariant/covariant.
- Recursive subtyping uses guarded cyclic proofs.
- A failed branch should yield a finite bad-message trace.

## 12. Source trail

- Lecture 8, sections 1–3 for the semantic criterion, admissible properties, choice/unit rules, and coinduction.
- Lecture 8, sections 4–7 for recursive examples, tensor, negative types, variance, and phase-sensitive stores.
- Lecture 8, sections 8–9 and Figures 1–2 for MPASS use and the collected type/process rules.
- Printed pages: L8.1–L8.14.
- PDF pages: 88–101.
- Full lecture reconstruction: [Lecture 8: Subtyping](../Lectures/Lecture%2008%20-%20Subtyping.md).

---
title: Formula and Rule Sheet
tags: [reference, rules]
---

# Formula and Rule Sheet

This is a memory aid, not a substitute for the linked concept explanations.

## Structural laws

- Exchange: $\Delta_1,A,B,\Delta_2 \equiv \Delta_1,B,A,\Delta_2$.
- Weakening: assumptions may be added without use.
- Contraction: duplicate assumptions may be merged/reused.

Structural contexts admit exchange, weakening, and contraction; linear contexts normally admit exchange only; ordered contexts deny exchange as well.

## Linear rewriting

$$
\Delta=R\uplus[P_1,\ldots,P_m]
\quad\Longrightarrow\quad
\Delta'=R\uplus[Q_1,\ldots,Q_n].
$$

The matched premises are consumed, conclusions are produced, and frame $R$ is preserved.

## Identity and cut

$$A\vdash A$$

$$
\frac{\Delta\vdash A\qquad \Delta',A\vdash C}{\Delta,\Delta'\vdash C}\;\mathsf{cut}
$$

Identity expresses direct use; cut composes evidence/processes. Cut elimination shows composition introduces no new provability and drives computation.

## Representative connective rules

$$
\frac{\Delta\vdash A\qquad\Delta'\vdash B}{\Delta,\Delta'\vdash A\otimes B}\;\otimes R
$$

$$
\frac{\Delta,A,B\vdash C}{\Delta,A\otimes B\vdash C}\;\otimes L
$$

$$
\frac{\Delta,A\vdash B}{\Delta\vdash A\multimap B}\;\multimap R
$$

$$
\frac{\Delta\vdash A\qquad\Delta',B\vdash C}{\Delta,\Delta',A\multimap B\vdash C}\;\multimap L
$$

Additive rules share a context across alternatives; multiplicative rules partition resources across simultaneous obligations.

## Safety

- Preservation: well-typed configurations remain well typed after a step.
- Progress: a well-typed closed configuration is final/observable or can step.

## Focusing
Invertible rules run eagerly during asynchronous inversion. Noninvertible rules require a choice of one focus and remain synchronous until focus is released.

## Quantifier side conditions
Universal-right and existential-left introduce fresh eigenvariables. Freshness prevents dependency on a special witness/name.

## Futures
A future address has single-assignment discipline: one computation writes a value; dependent computations may read when available. Linear/structural modes govern ownership and reuse.

## Bidirectional typing
Checking judgments validate a term against a known type; synthesis judgments infer a type from an eliminative form. Annotations mediate between directions.

[Notation Guide](02%20Notation%20Guide.md) · [Concept Index](03%20Concept%20Index.md)

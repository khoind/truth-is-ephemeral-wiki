---
title: Partial Focusing
aliases:
  - focused compound values
  - partial positive phase
tags:
  - focusing
  - data-layout
  - proof-theory
source_lectures:
  - 17
prerequisites:
  - "[Data layout and compound values](Data-Layout-and-Compound-Values.md)"
related:
  - "[Forward proof search and inverse method](Forward-Proof-Search-and-Inverse-Method.md)"
  - "[Canonical forms and hereditary substitution](Canonical-Forms-and-Hereditary-Substitution.md)"
---

# Partial Focusing

## One-sentence definition

Partial focusing performs a positive focused phase deeply enough to build or inspect a compound value, but deliberately stops at downshifts and negative types where an address becomes the boundary.

## Why the concept is needed

Ordinary focusing maximizes a phase to remove inessential proof permutations. Data layout needs a controlled notion of partiality: positive fields should be fused into one compound cell, while recursion and latent behavior must remain behind addresses. On reads, the same discipline must generate nested, exhaustive patterns rather than only shallow constructor tests.

## Intuitive model

**Intuition.** Follow a recipe through every “open now” constructor, but stop at every “reference this later” marker. On output this builds one nested value; on input it destructures exactly the same visible shape. The stopping rule is logical, not an arbitrary parser depth.

## Formal core

The focused value judgment $\Delta\vdash V:\lceil A\rceil$ means $V$ is a positive observation of $A$. Representative right rules are:

$$
\frac{\Delta\vdash V:\lceil A_k\rceil}{\Delta\vdash k(V):\lceil\oplus\{\ell:A_\ell\}_{\ell\in L}\rceil}
\quad
\frac{\Delta_1\vdash V_1:\lceil A\rceil\quad\Delta_2\vdash V_2:\lceil B\rceil}
{\Delta_1,\Delta_2\vdash(V_1,V_2):\lceil A\otimes B\rceil}.
$$

The phase stops through

$$
x:A\vdash\langle x\rangle:\lceil\downarrow A\rceil
\qquad
x:A^-\vdash x:\lceil A^-\rceil,
$$

where $A^-$ is negative. Reading uses a pattern sequence $\mathcal V$ and continuation $K$:

$$
\mathcal V ::= \mathcal V\cdot\mathcal V\mid(\cdot),
\qquad K::=(\mathcal V\Rightarrow P\mid K)\mid\cdot.
$$

The judgment $\Delta;\Omega\vdash K::\delta$ matches the ordered sequence $\Omega$ of focused components. Tensor replaces one expected item $A\otimes B$ by adjacent expectations $A,B$; a sum creates one premise per label; a downshift or negative type transfers a bound address into $\Delta$. $\delta$ is the process result judgment.

## How to use/read it

For a write, repeatedly apply positive right rules until every leaf is unit, shifted, or negative. For a read, expand the expected positive type into nested patterns and ensure every sum tag has a branch. The continuation application operation projects and filters branches as each constructor is encountered.

## Worked example

Take $T=\oplus\{\mathsf{leaf}:1,\mathsf{node}:B\otimes\downarrow T\}$ with positive $B=\oplus\{\mathsf{off}:1,\mathsf{on}:1\}$.

1. To write a node with `on` and tail address $a$, focus on $T$ and choose `node`.
2. Focus through $\otimes$, producing two adjacent obligations $B$ and $\downarrow T$.
3. Focus on $B$, choose `on`, and close its unit.
4. Stop at $\downarrow T$ with $\langle a\rangle$.
5. The compound value is $\mathsf{node}(\mathsf{on}(),\langle a\rangle)$.
6. A complete reader has a `leaf()` branch plus `node(off(),⟨t⟩)` and `node(on(),⟨t⟩)` branches. Each binds only the address $t$ beyond the focused frontier.

## Non-example or boundary case

A reader with only the `node(on(),⟨t⟩)` pattern is not exhaustive for $T$. Conversely, decomposing the cell at $t$ in the same phase crosses a downshift boundary and defeats the finite layout discipline.

## Key consequences

Partial focusing explains why compound values and nested patterns are dual. It makes visible layout finite, permits unboxed fields, and leaves latent or recursive parts behind addresses. It also exposes where a richer language could permit partial patterns that bind a still-positive subvalue rather than fully enumerating it.

## Relations to nearby concepts

[Data layout and compound values](Data-Layout-and-Compound-Values.md) is the principal application. [Forward proof search and inverse method](Forward-Proof-Search-and-Inverse-Method.md) uses full focused phases to generate big-step inference rules instead. [Canonical forms and hereditary substitution](Canonical-Forms-and-Hereditary-Substitution.md) uses focusing to define normal LF syntax.

## Common mistakes

- Equating partial focusing with an incomplete proof search.
- Stopping at an arbitrary positive connective.
- Continuing through a shift and thereby inlining recursive data indefinitely.
- Forgetting that tensor patterns expand both components.
- Omitting a sum branch without explicitly extending the language with partial matches.

## What to remember

- Positive structure is followed deeply.
- Downshifts and negative types are address boundaries.
- Writes build compound values; reads use dual nested patterns.
- Exhaustiveness remains a typing condition.

## Source trail

Lecture 17, §3 “Partial Focusing Revisited,” printed pp. L17.4–L17.5, PDF pp. 183–184; examples and the proposed partial-pattern extension are in §4, printed pp. L17.5–L17.6, PDF pp. 184–185.


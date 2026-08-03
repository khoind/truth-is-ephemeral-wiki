---
title: Data Layout and Compound Values
aliases:
  - compound values
  - boxed and unboxed data
  - SNAX data layout
tags:
  - data-layout
  - snax
  - focusing
source_lectures:
  - 17
prerequisites:
  - "[Partial focusing](Partial-Focusing.md)"
related:
  - "[Futures and single assignment](Futures-and-Single-Assignment.md)"
  - "[Positive and negative futures](../Comparisons/Positive-and-Negative-Futures.md)"
---

# Data Layout and Compound Values

## One-sentence definition

Data layout is the type-directed in-memory shape obtained by composing positive constructors into compound values until a shift or negative type forces a fixed-size address indirection.

## Why the concept is needed

If every pair component is stored through a pointer, programs lose control over locality; if recursive positive data is always inlined, values may require unbounded space. SNAX connects high-level layout choices to semi-axiomatic proof structure: a cut allocates a cell, while a restricted cut or snip can denote an address relative to already allocated storage. Compound values expose safe inlining without fixing machine-level byte offsets.

## Intuitive model

**Intuition.** Lay out a value by opening positive constructors like nested boxes. Tags and fields sit inline. Stop opening when a field is deliberately boxed by a shift or is negative; place a fixed-width address there. This is a schematic layout, not a promise about exact bytes, alignment, garbage collection, or calling conventions.

## Formal core

Positive compound values are:

$$
V ::= k(V)\mid(V_1,V_2)\mid()\mid\langle x\rangle\mid x.
$$

$k$ is a sum tag; $V_1,V_2$ are nested values; $()$ is unit; $\langle x\rangle$ is a downshifted address; bare $x$ is an address at a negative boundary such as $A\multimap B$, $N\{\ell:A_\ell\}$, or $\uparrow A$. A write has the typing shape

$$
\frac{\Delta\vdash V:\lceil A\rceil}{\Delta\vdash\operatorname{write}\ x\,V::(x:A)}.
$$

$\lceil A\rceil$ means that $A$ is under a positive value-construction focus. For example:

$$
\frac{\Delta_1\vdash V_1:\lceil A\rceil\quad \Delta_2\vdash V_2:\lceil B\rceil}
{\Delta_1,\Delta_2\vdash(V_1,V_2):\lceil A\otimes B\rceil}.
$$

Recursive types require a stopping point. The type
$\mathsf{nat}=\oplus\{\mathsf{zero}:1,\mathsf{succ}:\mathsf{nat}\}$ has unbounded inline size. Replacing the recursive occurrence by $\downarrow\mathsf{nat}$ gives a fixed-width pointer at each successor.

## How to use/read it

Follow the type top-down. Allocate room for a tag at $\oplus$, concatenate layouts at $\otimes$, allocate no payload for $1$, and insert an address at $\downarrow$ or a negative type. “Boxed” means the field is behind such an address; “unboxed” means its positive representation sits inline.

## Worked example

Define

$$
\mathsf{bool}=\oplus\{\mathsf{false}:1,\mathsf{true}:1\},\quad
\mathsf{blist}=\oplus\{\mathsf{nil}:1,\mathsf{cons}:\mathsf{bool}\otimes\downarrow\mathsf{blist}\}.
$$

For the value `cons true tail`:

1. Reserve the outer tag and choose `cons`.
2. Expand the tensor inline.
3. Expand `bool` inline and choose the `true` tag; its unit payload needs no data field.
4. Stop at $\downarrow\mathsf{blist}$ and store tail address $a$.
5. The schematic record is therefore `[cons | true | a]`.

For `nil`, the representation is `[nil | unused | unused]` if all alternatives use one fixed width. The unused region is padding, not hidden data.

## Non-example or boundary case

A purely positive recursive definition does not describe a finite statically allocated cell. Nor does this logical layout determine exact word sizes or permit reading a prefix that the pattern judgment has not justified.

## Key consequences

Type definitions expose the box/unbox choice. Inlining can improve locality but expands fixed cell size; boxing bounds cell width and adds indirection. Negative values are represented by addresses because their behavior is not directly inspected as positive data. Partial focusing provides the proof-theoretic criterion for stopping.

## Relations to nearby concepts

[Partial focusing](Partial-Focusing.md) derives compound values and exhaustive nested patterns. [Positive and negative futures](../Comparisons/Positive-and-Negative-Futures.md) explains why negative cells store behavior. [Mixed linear and structural futures](Mixed-Linear-and-Structural-Futures.md) distinguishes a shift's mode role from its use as layout indirection.

## Common mistakes

- Assuming all recursive data must be boxed at every field.
- Calling unboxed recursion finite without a shift or negative boundary.
- Confusing logical layout with exact ABI layout.
- Forgetting padding needed for alternatives of unequal width.
- Treating a negative continuation as directly observable inline data.

## What to remember

- Positive constructors compose inline.
- Shifts and negative types stop inlining with an address.
- Recursive positive types need indirection for bounded cells.
- Boxing is explicit in the type; low-level details remain compiler choices.

## Source trail

Lecture 17, §§1–2 and §4, printed pp. L17.1–L17.7, PDF pp. 180–186; the formal value rules are in §3, printed pp. L17.4–L17.5, PDF pp. 183–184.


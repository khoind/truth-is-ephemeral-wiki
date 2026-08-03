---
title: "Lecture 17 — Data Layout"
lecture: 17
date: 2023-11-09
pdf_pages: "180–186"
printed_pages: "L17.1–L17.7"
tags:
  - lecture-guide
  - data-layout
  - snax
prerequisites:
  - "[Lecture 16 — Futures](Lecture-16-Futures.md)"
  - "[Data layout and compound values](../Concepts/Data-Layout-and-Compound-Values.md)"
---

# Lecture 17 — Data Layout

## 1. Why this lecture exists

The future interpretation says types describe cell contents but has so far used addresses for most components. This lecture asks which positive data can be stored inline, where recursive structures require indirection, and how the type system exposes that choice. Partial focusing and SNAX connect proof shape to compound memory layout without prescribing byte-level compiler details.

## 2. Learning objectives

- construct compound values for sums, tensors, unit, shifts, and negative boundaries;
- distinguish boxed from unboxed fields;
- diagnose unbounded purely positive recursive layouts;
- explain how partial focusing determines layout and nested patterns;
- read the generalized continuation judgment; and
- compare three append representations.

## 3. Dependency map

[Futures](Lecture-16-Futures.md) gives cells and addresses. Positive focusing $\rightarrow$ [compound values and layout](../Concepts/Data-Layout-and-Compound-Values.md). Stopping at shifts/negative types $\rightarrow$ bounded recursion. Dual pattern inversion $\rightarrow$ [partial focusing](../Concepts/Partial-Focusing.md). SNAX snips $\rightarrow$ relative addresses rather than fresh allocation.

## 4. Section-by-section reconstruction covering every numbered heading

### 1 Introduction

Functional compilers normally choose layouts implicitly. SNAX exposes selected high-level choices in types. Semi-axiomatic cut elimination permits restricted cuts called snips; under shared memory, a full cut allocates a cell while a snip identifies storage relative to an existing address. The lecture concentrates on the connection between partial focusing and source-language compound values.

### 2 Data Layout: Compound Values

A positive field need not be an address: tags, pairs, and unit can nest directly. The grammar $V::=k(V)\mid(V_1,V_2)\mid()\mid\langle x\rangle\mid x$ stops at downshifts or negative types. Purely positive recursion has unbounded inline size, so types insert an address boundary. A `listbool` may inline its Boolean but store a pointer to the tail. Different sum alternatives use a common cell width, leaving padding in smaller variants.

### 3 Partial Focusing Revisited

Writing focuses through positive right rules until a shift or negative identity ends the phase. Reading is dual but must handle nested patterns, so the continuation judgment uses an ordered sequence of pending types. Tensor expands both fields; sum requires all tags; shift/negative boundaries bind addresses into the ordinary context. Continuation projection successively filters and expands patterns.

### 4 Example: Append with Three Types

The first append consumes inline list cells whose element and tail are shifted pointers. The second makes the list itself a pointer and must match through the pointer to expose a constructor, awkwardly decomposing and recomposing tails. The third inlines Booleans, forcing separate `false` and `true` branches under full matching. Allowing a variable at a positive subvalue would support more convenient partial matches.

## 5. Formal core

The write boundary is

$$
\frac{\Delta\vdash V:\lceil A\rceil}{\Delta\vdash\operatorname{write}\ x\,V::(x:A)}.
$$

$V$ is a compound value, $\lceil A\rceil$ a positive focused type, and $\Delta$ its address resources. Key terminal rules are $x:A\vdash\langle x\rangle:\lceil\downarrow A\rceil$ and $x:A^-\vdash x:\lceil A^-\rceil$. Reading begins from $\Delta;\lceil A\rceil\vdash K::\delta$, where the semicolon separates stable bound addresses $\Delta$ from the ordered pattern worklist. The final empty pattern selects a process $P::\delta$.

## 6. Operational/computational reading

Inline constructors are observed by one cell read and pattern match. Address boundaries defer another read or invocation. Boxing yields fixed-size references and more indirection; unboxing increases the current record's fixed footprint but can improve locality. The type constrains this strategy while a compiler still decides word sizes and offsets.

## 7. Worked derivation or trace in original notation and prose

For

$$
\mathsf{blist}=\oplus\{\mathsf{nil}:1,\mathsf{cons}:\mathsf{bool}\otimes\downarrow\mathsf{blist}\},
$$

derive $\mathsf{cons}(\mathsf{true}(),\langle a\rangle)$:

1. $\cdot\vdash():\lceil1\rceil$.
2. Hence $\cdot\vdash\mathsf{true}():\lceil\mathsf{bool}\rceil$.
3. $a:\mathsf{blist}\vdash\langle a\rangle:\lceil\downarrow\mathsf{blist}\rceil$ ends focusing at the pointer.
4. Tensor combines the disjoint resources to obtain $(\mathsf{true}(),\langle a\rangle)$.
5. Sum introduction tags it `cons`.
6. `write x` stores the whole visible structure in one cell at $x$.

### Extended reconstruction: from proof phase to representation

**Section 1** connects a proof-theoretic restriction to a memory decision. Ordinary cut allocates an independently named cell. A snip is permitted only where the semi-axiomatic derivation already identifies storage inside a surrounding result; operationally it can use a relative location rather than allocate another future. SNAX therefore does not claim that proofs determine machine bytes. It exposes a typed boundary between contiguous representation and separately addressed representation, leaving alignment, word size, and garbage collection to later compilation.

**Section 2** can be read as a size calculation. Associate a schematic width $|A|$ with focused positive layout. A unit contributes no payload, a finite sum contributes a tag plus the maximum payload width of its alternatives, and tensor contributes both component widths. A downshift or negative boundary contributes one address-sized field and stops recursive expansion. Hence

$$
|1|=0,\qquad |\oplus\{k_i:A_i\}|=|\mathsf{tag}|+\max_i|A_i|,
\qquad |A\otimes B|=|A|+|B|,
$$

while $|\downarrow A|=|\mathsf{addr}|$. These equations are explanatory, not byte-level definitions. They clarify why $X=1\oplus(A\otimes X)$ is not a finite inline layout: unfolding $X$ keeps adding fields. Replacing the recursive occurrence by $\downarrow X$ gives every constructor a bounded width. Padding in a short sum alternative follows from reserving enough room for the largest alternative; it is not extra logical data.

**Section 3** explains why the value grammar and continuation grammar are dual. Positive right focusing eagerly builds tags, pairs, and unit until it reaches a boundary. A read continuation must be prepared to invert every possible constructor at the same depth. The worklist in $\Delta;\lceil A_1\rceil,\ldots,\lceil A_n\rceil\vdash K::\delta$ records positive pieces still to be matched in order. Here $\Delta$ contains already bound address variables, the semicolon is a phase boundary rather than context union, and $\delta$ is the eventual process conclusion. For tensor the head work item is replaced by two component items. For a sum, one continuation branch is checked for every tag. At a shift or negative atom, decomposition stops and an address is bound in $\Delta$.

**Section 4** uses append to reveal costs that are hidden in an ordinary algebraic datatype. If both element and tail are pointers, each constructor read reveals only addresses and subsequent work incurs more reads. If the whole list is boxed, append must first dereference the list pointer before seeing `nil` or `cons`, and rebuilding can require another layer. If Boolean elements are inline, one read reveals both the list constructor and Boolean tag, but a fully decomposing continuation duplicates the `cons` branch into `false` and `true` cases. The proposed extension—allowing a variable pattern for a positive subvalue—would retain that field without splitting all of its constructors. This is representation-polymorphic matching, not weakening: the captured subvalue remains present and typed.

For a more explicit read trace, suppose

$$
\operatorname{cell}(x,\mathsf{cons}(\mathsf{false}(),\langle t\rangle))
$$

is matched against a continuation with `nil`, `cons(true(),<q>)`, and `cons(false(),<q>)` branches. The outer tag chooses `cons`; tensor decomposition places the Boolean and tail pattern on the worklist; Boolean decomposition chooses `false`; the shift boundary binds $t$ to $q$ without reading the tail. The selected branch may now write a result using $q$. Exactly one cell has been read. Following $q$ would be a distinct read, showing operationally where indirection occurs.

This also refines the earlier construction example. The derivation of `cons(true(),<a>)` proves that the inline Boolean and tail pointer use disjoint address resources. The write rule then commits the compound storable atomically at $x$. It does not mean that the recursively pointed-to list at $a$ has already been evaluated; $a$ may still be an unfulfilled future.

The key boundary cases are useful design tests. An empty variant still occupies the common sum representation. A deeply nested but nonrecursive positive type is large yet statically bounded. A recursive type is acceptable when every cycle crosses an address boundary. Negative fields are represented by addresses/continuations rather than inlined positive constructors. Finally, changing a field from boxed to unboxed can preserve extensional source values while changing which programs can observe readiness and locality; layout is therefore semantically disciplined, not merely cosmetic.

Additional checks: **Does focusing force one global layout?** No, shifts and polarity choices in the type select boundaries. **Can a compiler unbox through a declared shift?** Not without proving that it preserves the exposed operational interface. **Why require exhaustive sum patterns?** A cell may legally contain any declared tag. **What does a snip save?** A fresh allocation, by reusing a statically justified sublocation.

Layout comparison should therefore count both space and synchronization. Inlining can remove a pointer and a future read, but it may delay publication until the entire compound storable is ready. Boxing can publish an outer constructor while a pointed component is still being computed. The types make this readiness boundary visible. Two extensionally equal lists may consequently expose different intermediate availability even though complete values decode to the same mathematical sequence. This is why an optimization that moves a shift needs an operational preservation argument, not just a size argument.

## 8. Conceptual synthesis

Layout is the spatial face of focusing: contiguous positive construction becomes a compound cell, while polarity/shift boundaries become pointers. Recursive types are safe because the programmer makes finite-size boundaries explicit. The matching rules certify that a reader covers every representation admitted by the type.

## 9. Common confusions and failure modes

- Pure positive recursion is not a bounded layout.
- A shift may express same-mode indirection in general adjoint logic; it need not always cross linear/structural modes.
- “Unboxed” does not mean dynamically untyped.
- The layout calculus does not fix byte alignment.
- Omitting a sum case is not allowed by the presented full-pattern system.

## 10. Self-test questions with concise answers

1. **Where does partial focusing stop?** At a downshift or negative type.
2. **Why box a recursive tail?** To keep each cell's layout bounded.
3. **What does tensor do to layout?** Places both component layouts inline and adjacent schematically.
4. **Why can `nil` contain padding?** All variants of one type use a common width.
5. **What would partial matching add?** A variable could stand for an undecomposed positive subvalue.

## 11. Related concept pages

- [Data layout and compound values](../Concepts/Data-Layout-and-Compound-Values.md)
- [Partial focusing](../Concepts/Partial-Focusing.md)
- [Positive versus negative futures](../Comparisons/Positive-and-Negative-Futures.md)

## 12. Source trail

Lecture 17 “Data Layout”: §1, printed pp. L17.1–L17.2, PDF pp. 180–181; §2, L17.2–L17.4, PDF pp. 181–183; §3, L17.4–L17.5, PDF pp. 183–184; §4, L17.5–L17.6, PDF pp. 184–185; references, L17.6–L17.7, PDF pp. 185–186.

## 13. Previous/next navigation

Previous: [Lecture 16 — Futures](Lecture-16-Futures.md). Next: [Lecture 18 — The Inverse Method](Lecture-18-The-Inverse-Method.md).


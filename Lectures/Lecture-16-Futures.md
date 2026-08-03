---
title: "Lecture 16 — Futures"
lecture: 16
date: 2023-11-02
pdf_pages: "171–179"
printed_pages: "L16.1–L16.9"
tags:
  - lecture-guide
  - futures
  - sax
prerequisites:
  - "Lecture 15: Adjoint SAX"
  - "[Futures, addresses, and single assignment](../Concepts/Futures-and-Single-Assignment.md)"
---

# Lecture 16 — Futures

## 1. Why this lecture exists

Earlier lectures read linear proofs as message-passing processes. This lecture gives the same SAX proof terms a write-once shared-memory interpretation. The bridge is a future: cut allocates a promised result cell, the producer and consumer run concurrently, and the consumer blocks only when it reads before fulfillment. Extending the interpretation from positive to negative and then mixed-mode types shows precisely what a cell must store and when reads persist.

## 2. Learning objectives

After this lecture, a reader should be able to:

- interpret sequent variables as addresses and types as cell-content specifications;
- explain single assignment and distinguish a cell, address, storable, and process;
- translate positive and negative SAX actions to reads and writes without reversing polarity;
- step the future operational semantics;
- distinguish linear cells from persistent structural cells; and
- use shifts to move between linear and structural modes.

## 3. Dependency map

SAX right rules $\rightarrow$ writes to the succedent address $\rightarrow$ [positive/negative interpretation](../Comparisons/Positive-and-Negative-Futures.md). Cut $\rightarrow$ fresh allocation and parallelism $\rightarrow$ [single-assignment futures](../Concepts/Futures-and-Single-Assignment.md). Adjoint modes and shifts $\rightarrow$ [mixed linear/structural futures](../Concepts/Mixed-Linear-and-Structural-Futures.md). Compound values introduced at the end $\rightarrow$ [Lecture 17](Lecture-17-Data-Layout.md).

## 4. Section-by-section reconstruction covering every numbered heading

### 1 Introduction

`let x = future e1 in e2(x)` immediately returns a promise to `e2`, evaluates producer `e1` concurrently, and synchronizes only when `e2` demands the promised value. The model is shared memory but not arbitrary mutable memory: a designated address is filled once. The channel/promise analogy retains proofs-as-programs and admits sequential implementations without changing the logical interface. Linear futures are studied first; structural reuse is added later.

### 2 Reinterpreting SAX: Positive Types

In $x_1:A_1,\ldots,x_n:A_n\vdash P::(x:A)$, every variable is an address. $P$ reads the antecedent addresses and writes $x$. Positive sum, tensor, and unit values are respectively $k(a)$, $(a_1,a_2)$, and $()$. Their left rules read and pattern-match. Cut allocates fresh storage; identity moves contents. Runtime syntax separates $\operatorname{proc}(P)$ from $\operatorname{cell}(a,V)$ so a quiescent result can be characterized as cells only.

### 3 Reinterpreting SAX: Negative Types

The uniform memory rule is “right writes, left reads.” For negative connectives, a right rule offers future interaction, so it writes a continuation rather than ordinary positive data. A cell for $A\multimap B$ contains $(x,r)\Rightarrow P(x,r)$; a client reads it with actual argument address $a:A$ and result address $b:B$. Therefore storables are $S::=V\mid K$. Relative to message passing, send/receive becomes read/write for positive types but flips for negative types.

### 4 Mixed Linear/Structural Futures

Shifts carry addresses between modes. $\downarrow A_S$ is positive and stores a structural address in a linear value; $\uparrow A_L$ is negative and stores a continuation behind a structural address. Linear cell reads consume the cell capability. A structural write produces $!\operatorname{cell}(a_S,S)$, and a read leaves that persistent cell available. The symmetric matching operation accepts value/continuation in either order. A linear list may consequently contain shared binary numbers without duplicating its linear spine.

## 5. Formal core

The central judgment and syntax are

$$
\Delta\vdash P::(x:A),\qquad
P::=x\leftarrow P;Q\mid\operatorname{move}\ x\ y\mid
\operatorname{write}\ x\,S\mid\operatorname{read}\ x\,S'.
$$

$\Delta$ is a context of typed input addresses; $x:A$ is the output address; $P,Q$ are processes; $S,S'$ are values or continuations. The key transitions are

$$
\begin{aligned}
\operatorname{proc}(x\leftarrow P;Q)&\to\operatorname{proc}(P(a)),\operatorname{proc}(Q(a)) && a\text{ fresh},\\
\operatorname{proc}(\operatorname{write}\ a\,S)&\to\operatorname{cell}(a,S),\\
\operatorname{cell}(a,S),\operatorname{proc}(\operatorname{read}\ a\,S')&\to\operatorname{proc}(S\triangleright S').
\end{aligned}
$$

For structural $a_S$, replace `cell` by persistent `!cell` and retain it after reading. Every symbol is operational: `proc` marks runnable code, `cell` marks fulfilled storage, $a$ is an address, freshness prohibits collision, and $\triangleright$ performs pattern/continuation application.

## 6. Operational/computational reading

Allocation enables producer and consumer to interleave. `write` commits once; `read` blocks until a matching cell exists; `move` relocates an already produced storable to a demanded destination. Positive clients select a branch by inspecting data. Negative clients supply a request to stored behavior. Structural persistence duplicates read access, not the right to update.

## 7. Worked derivation or trace in original notation and prose

Let $b$ contain $\mathsf{left}(u)$ and let $K$ negate the tag:

$$
K=(\mathsf{left}(z)\Rightarrow\operatorname{write}\ r\,\mathsf{right}(z)
\mid\mathsf{right}(z)\Rightarrow\operatorname{write}\ r\,\mathsf{left}(z)).
$$

Then

$$
\operatorname{cell}(b,\mathsf{left}(u)),\operatorname{proc}(\operatorname{read}\ b\,K)
\to\operatorname{proc}(\operatorname{write}\ r\,\mathsf{right}(u))
\to\operatorname{cell}(r,\mathsf{right}(u)).
$$

The first step matches the stored tag against $K$; the second fulfills $r$. If $b$ is linear, its cell is consumed. If $b_S$ is structural, $!\operatorname{cell}(b_S,\mathsf{left}(u))$ remains beside the new process.

### Extended reconstruction and second trace

The four source sections form one argument rather than four disconnected implementation recipes. **Section 1** fixes the semantic contract: allocation may expose an address before its contents exist, but fulfillment happens at most once. Consequently, determinacy does not require a fixed scheduler. Two enabled producers for unrelated addresses may run in either order, while a reader of an unfilled address simply has no transition. This is blocking synchronization, not polling and not failure.

**Section 2** obtains the positive interpretation directly from right introduction. A proof of a sum chooses a tag, so the corresponding writer stores a tagged payload. A proof of tensor constructs both components, so the storable is a pair of addresses or focused subvalues. Unit carries no payload. On the left, case analysis and pair elimination become patterns consumed by `read`. Identity is special: it does not calculate a new constructor; it forwards the unique storable from an input address to the required output. Cut is also special because its logical intermediate formula becomes a physical fresh address hidden from the surrounding configuration.

**Section 3** prevents a common but serious polarity error. A negative right rule waits for information supplied by a client. To preserve the invariant “right writes the offered address,” the writer deposits suspended behavior. For $A\multimap B$, the stored continuation expects an address for an $A$ and an address at which to produce $B$. A left use reads that behavior and supplies those addresses. Thus “data versus code” is not an extra dynamic type test: the type of the address already determines the admissible storable and matching rule.

**Section 4** adds modes without abandoning single assignment. Let $a_L$ denote a linear address and $a_S$ a structural address. Reading `cell(a_L,S)` transfers the sole capability and removes that cell from the configuration. Reading $!\operatorname{cell}(a_S,S)$ leaves the persistent fact behind, allowing many clients to obtain the same already-fixed storable. Persistence therefore concerns observation, not repeated mutation. A downshift packages a reusable structural address as positive data, while an upshift exposes linear behavior through the structural side according to the adjoint discipline.

The matching operator $S\triangleright S'$ is symmetric notation for joining complementary halves. If $S$ is a tagged value and $S'$ is a case continuation, matching selects a branch and substitutes the payload. If one side is a stored function continuation and the other is a request, matching performs continuation application. It is not an arbitrary comparison: typing guarantees that the two forms are dual at the same address type.

Consider a cut that creates $a$, a producer that writes a pair, and a consumer that projects its second field:

$$
\operatorname{proc}(a\leftarrow \operatorname{write}\ a\,(u,v);\
                    \operatorname{read}\ a\,((x,y)\Rightarrow\operatorname{move}\ r\ y)).
$$

Fresh allocation first yields two processes sharing only $a$. If the consumer is scheduled first, it blocks because no `cell(a,_)` exists. The producer then steps to $\operatorname{cell}(a,(u,v))$. The read joins the pair with its pattern, substitutes $u$ for $x$ and $v$ for $y$, and produces `move r v`. Finally forwarding fulfills $r$ with the storable available at $v$. This trace shows three distinct events—name generation, fulfillment, and demand—and explains why saying merely “cut substitutes a term” loses the concurrency exposed by SAX.

The safety invariant behind all these steps is ownership of destinations: a well-typed process offers exactly one output address, cuts choose fresh destinations, and no reduction creates a competing writer. Progress is more qualified. A well-typed open configuration may wait for an environment-owned address, and cyclic networks may deadlock. The logic rules establish shape and resource safety; they should not be overread as a blanket termination or deadlock-freedom theorem.

Additional checks: **Why can readers race safely?** Only structural readers can coexist, and they all observe the identical committed storable. **Why not erase polarity?** Positive and negative addresses reverse which participant supplies the observable constructor or request. **What survives a linear read?** The continuation process survives, but the consumed cell capability does not. **Can scheduling alter the stored value?** Not in a typed single-writer configuration; it can alter only when independent steps occur.

A final diagnostic is to ask who owns each address. An antecedent address is available for reading according to its mode; the succedent is the unique destination this process must eventually fulfill. Fresh cut addresses are internal, whereas free addresses describe the configuration's interface. This ownership reading connects the static sequent directly to the dynamic no-double-write invariant without identifying an address with the process that currently mentions it.

## 8. Conceptual synthesis

The future interpretation is not a new logic but a new computational reading of SAX. Polarity determines the shape of storage; mode determines persistence. Single assignment connects proof uniqueness of production with race-free memory, while shifts allow controlled sharing. This prepares Lecture 17's question: how much positive structure should be stored inline in one cell?

## 9. Common confusions and failure modes

- A future is not a mutable reference; no rule overwrites a cell.
- An address is not its stored value.
- Negative types do not follow the positive send/write mnemonic.
- A persistent cell remains single-assignment.
- Recursive typing does not itself guarantee a process eventually reads and writes all promised cells.

## 10. Self-test questions with concise answers

1. **What does cut do at runtime?** It allocates a fresh address and spawns producer and consumer processes.
2. **Why can a negative cell hold code?** A negative right rule offers a continuation, so right-as-write stores that continuation.
3. **When does a read block?** When no cell at the requested address is present.
4. **What changes for a structural read?** The persistent cell is retained.
5. **Does persistence permit a second writer?** No.

## 11. Related concept pages

- [Futures, addresses, and single assignment](../Concepts/Futures-and-Single-Assignment.md)
- [Positive versus negative future interpretation](../Comparisons/Positive-and-Negative-Futures.md)
- [Mixed linear and structural futures](../Concepts/Mixed-Linear-and-Structural-Futures.md)

## 12. Source trail

Lecture 16 “Futures”: §1, printed pp. L16.1–L16.2, PDF pp. 171–172; §2, L16.2–L16.4, PDF pp. 172–174; §3, L16.4–L16.6, PDF pp. 174–176; §4, L16.6–L16.8, PDF pp. 176–178; references continue on L16.8–L16.9, PDF pp. 178–179.

## 13. Previous/next navigation

Previous: Lecture 15 — Adjoint SAX (guide outside this requested tranche). Next: [Lecture 17 — Data Layout](Lecture-17-Data-Layout.md).


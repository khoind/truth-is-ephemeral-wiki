---
title: "Lecture 22 — The Concurrent Logical Framework"
lecture: 22
date: 2023-12-05
pdf_pages: "229–236 (source map lists 229–248; 237–248 are headed Lecture 23)"
printed_pages: "L22.1–L22.8"
tags:
  - lecture-guide
  - clf
  - concurrency
prerequisites:
  - "[Lecture 21 — Substructural Frameworks](Lecture-21-Substructural-Frameworks.md)"
  - "[CLF and monadic concurrency](../Concepts/CLF-and-Monadic-Concurrency.md)"
---

# Lecture 22 — The Concurrent Logical Framework

## 1. Why this lecture exists

LLF represents linear single-conclusion rules but handles forward rules with multiple conclusions only through continuation-passing encodings that impose nested order. CLF adds positive types and monadic expressions so transitions can directly consume and generate resources. Its equality swaps independent lets, retaining causality while erasing scheduler artifacts. Futures dynamics then becomes a compact executable signature.

## 2. Learning objectives

- explain why multi-conclusion forward rules strain LLF;
- perform the continuation-passing workaround;
- read CLF positive types, monadic braces, terms, patterns, and lets;
- determine when two let steps commute;
- encode futures transitions with `proc`, `cell`, `pass`, and existential addresses; and
- distinguish don't-care execution from nonterminating generative search.

## 3. Dependency map

[LLF](../Concepts/Linear-Logical-Frameworks-and-Metatheory.md) limitation $\rightarrow$ continuation passing. Positive results $\rightarrow$ [CLF monadic concurrency](../Concepts/CLF-and-Monadic-Concurrency.md). Commuting lets $\rightarrow$ [trace equivalence](../Concepts/Generative-Grammars-Trace-Equivalence-and-Adequacy.md). [Future dynamics](../Concepts/Futures-and-Single-Assignment.md) $\rightarrow$ executable CLF rules and queries.

## 4. Section-by-section reconstruction covering every numbered heading

### 1 Introduction

Simple linear systems can have several conclusions, as in resource-generation rules. CLF carefully adds positive types to LLF, enabling both their representation and concurrent computation. The lecture's main application is a direct encoding of linear futures dynamics.

### 2 Coin Exchange Revisited

Coin rules consume one multiset and produce another. Linear implications with tensor conclusions are not directly representable in negative-only LLF. Moving transitions into antecedents and reversing direction yields continuation-passing types with arbitrary result `c`. A proof that a quarter plus nickel becomes three dimes is representable, but the term nests constructors and distinguishes irrelevant coin identities/orderings. This motivates positive framework results.

### 3 CLF

CLF adds positive $1$, tensor, existential, and embedded negative types, plus negative $\{A^+\}$. Forward clauses such as `fromQ : q -o {d*d*n}` become direct. Expressions use `let {p}=M in E` to bind generated resources. Two adjacent lets are definitionally equal when neither pattern captures a free variable of the other computation. Hence independent interleavings denote one concurrent trace, while dependent steps remain ordered. The historical presentation omits sums and has shift/atom limitations later repaired in Celf.

### 4 Representing the Dynamics of Futures

The signature declares syntactic categories for values, expressions, continuations, and addresses; state facts `cell` and `proc`; and a `pass` relation implementing value/continuation matching. Execution rules consume state facts and monadically generate replacements. `exec/cut` existentially creates a fresh address; `exec/write` creates a cell; `exec/read` consumes a process, cell, and matching proof to generate the continuation process. Boolean-negation queries demonstrate concrete traces and existential result discovery.

### Source-map boundary note

The supplied `LECTURE-MAP.md` assigns PDF pp. 229–248 to Lecture 22. The extracted file at PDF p. 237 begins a separately titled **Lecture 23, “Linear Natural Deduction,” dated December 7, 2023**, and pp. 237–248 use printed labels L23.1–L23.12 with numbered §§1–7. Those pages were read as requested but are not silently reconstructed as Lecture 22. Lecture 22 itself ends with references on PDF p. 236 / printed p. L22.8.

#### Mapped supplement: Lecture 23 §§1–7 on PDF pp. 237–248

For completeness of the supplied page range, the separately headed material contains these numbered sections. **§1 Introduction** contrasts the single bottom-up direction of sequent calculi with natural deduction's introduction and elimination directions. **§2 The Base Rules** derives tensor pairing/matching and linear function abstraction/application while splitting resources. **§3 Bidirectional Type Checking** separates checking $M\Leftarrow A$ from synthesis $M\Rightarrow A$ and assigns introduction rules to checking and eliminations/hypotheses mainly to synthesis. **§4 An Example** derives currying and identifies the synthesis-to-checking conversion, whose implementation must compare the synthesized and expected types. **§5 System Correctness**, including **§5.1 Harmony**, relates local completeness to identity and local soundness to normalization using admissible substitution; **§5.2 Soundness/Completeness with respect to Sequent Calculus** states translations among ordinary natural deduction, bidirectional natural deduction, and sequent calculus, with an explicit context-substitution judgment. **§6 Curry–Howard Correspondence** identifies local proof reductions such as $(\lambda x.M)N\to[N/x]M$ with computation. **§7 Full Bidirectional Rules** collects checking and synthesis rules for implication, negative choice, tensor, unit, and positive sums. These are Lecture 23 topics, not prerequisites or hidden subsections of CLF.

## 5. Formal core

A transition has type

$$
A_1\multimap\cdots\multimap A_m\multimap\{\exists\vec x.B_1\otimes\cdots\otimes B_n\}.
$$

$A_i$ are consumed linear facts, $B_j$ generated facts, and $\vec x$ fresh names. For futures:

```text
exec/cut   : proc (cut (\x. P x) (\x. Q x))
             -o {Exists a:addr. proc (P a) * proc (Q a)}
exec/write : proc (write A V) -o {cell A V}
exec/read  : proc (read A K) -o cell A V -o pass V K P
             -o {proc P}
```

`proc`, `cell`, and `pass` are linear predicates; capital identifiers are framework variables; braces suspend a positive result; `Exists` binds a fresh output; `*` is positive tensor.

## 6. Operational/computational reading

A CLF query is forward execution over a multiset of linear state facts. Applying a clause consumes its arguments and exposes generated facts through `let`. For futures, nondeterministic scheduling is don't-care when independent steps commute and all choices represent the same causal computation. Coin exchange can run forever because reversible rules prevent quiescence; terminating future programs reach cell-only states.

## 7. Worked derivation or trace in original notation and prose

Start with cells encoding false and a negation process:

```text
cell c0 unit * cell c1 (pi2 c0) *
proc (read c1 (plus_cont <(\u. write c2 (pi2 u)),
                           (\u. write c2 (pi1 u))>))
```

1. `pass/plus2` selects the second continuation because the value is `pi2 c0`.
2. `exec/read` consumes `cell c1 ...`, the read process, and the `pass` proof; it generates `proc (write c2 (pi1 c0))`.
3. `exec/write` consumes that process and generates `cell c2 (pi1 c0)`.
4. `cell c0 unit` remains untouched.
5. The final state therefore represents true at `c2`; the two lets in the printed trace record exactly these causally ordered steps.

### Extended reconstruction: positive results as concurrent traces

**Section 1** starts from a representation mismatch. A forward transition naturally has several outputs that coexist, such as replacing one coin by three coins or replacing one process fact by two spawned processes. Negative-only LLF types end in one atomic conclusion. Continuation passing can encode the transition, but the continuation decides an artificial nesting order among outputs. CLF adds a positive layer so the framework type can state directly which multiset of resources is generated.

**Section 2** makes the mismatch concrete. In a continuation-passing coin rule, produced coins are passed to a continuation of arbitrary result type $c$. The encoding preserves reachability, yet a proof term records which particular dime was fed to which later rule and in what syntactic order continuations were called. The object system regards equal-valued coins as multiset resources and independent exchanges as unordered. A direct positive result such as $\{d\otimes d\otimes n\}$ represents simultaneous availability more faithfully.

**Section 3** divides types by phase. Positive types include unit $1$, tensor $A^+\otimes B^+$, existential $\exists x:A.B^+(x)$, and an embedding of negative atoms/types. The negative monadic type $\{A^+\}$ packages a computation that will generate a positive result. In an expression

$$\mathsf{let}\ \{p\}=M\ \mathsf{in}\ E,$$

$M$ performs a generative step, pattern $p$ names its positive outputs, and $E$ continues with those outputs as linear resources. Existential patterns reveal fresh names without letting the surrounding signature choose them in advance.

The commuting conversion is a causal criterion, not unrestricted reordering. Adjacent lets may swap when the computation in either step does not use variables bound by the other's output pattern. Linear typing also prevents two swapped steps from secretly consuming the same fact. If the second step reads a resource generated by the first, its free-variable dependency fixes the order. If two rules compete for one coin or cell, only one can occur in a particular trace; they are alternatives, not commuting events.

This equality turns expressions into traces modulo independent permutations. It removes scheduler artifacts while retaining causal order. Adequacy for a concurrent encoding therefore needs more than a bijection between raw rule sequences and raw terms. It should relate object executions modulo permutation of independent transitions to CLF expressions modulo commuting lets.

**Section 4** maps futures state directly. `proc P` says process expression $P$ is runnable, and `cell A V` says address $A$ contains value $V$. Both are linear state facts. `pass V K P` is not persistent machine state; it is an auxiliary judgment proving that matching value $V$ with continuation $K$ yields process $P$. `exec/cut` consumes one cut process and generates two processes plus existentially fresh address $a$. `exec/write` replaces a write process by a cell. `exec/read` consumes a read process and matching linear cell, consults a `pass` proof, and generates the continuation process.

Read the transition type

$$A_1\multimap\cdots\multimap A_m\multimap
\{\exists\vec x.B_1\otimes\cdots\otimes B_n\}$$

from left to right: the $A_i$ are required facts consumed exactly once; braces suspend generation until the clause is applied; $\vec x$ are fresh names scoped over the outputs; tensor says all $B_j$ become jointly available. It does not mean a sequential function returns a heap tuple, though an implementation may realize it that way.

Consider two independent writes in state

$$\mathsf{proc}(\mathsf{write}\ a\ V)\otimes
  \mathsf{proc}(\mathsf{write}\ b\ W),\qquad a\ne b.$$

Applying `exec/write` at $a$ and then $b$ gives an expression with two nested lets and final state $\mathsf{cell}\ a\ V\otimes\mathsf{cell}\ b\ W$. Applying them in the opposite order gives the reversed lets and the same multiset. Neither step mentions an output of the other, so the commuting equality identifies them. Add instead `proc(read a K)`. Its `exec/read` step depends on `cell a V`, so the write at $a$ cannot commute past that read as if causality were absent. The write at $b$ may still commute with both if no process mentions $b$.

Freshness is equally observable. For a cut, existential output prevents collision with every existing address; both spawned processes receive the same fresh witness. Two unrelated cuts can commute, but each one's pair of children remains causally downstream of its own allocation. This is the CLF counterpart of the future trace in Lecture 16.

Queries execute the signature as a generative grammar. Don't-care nondeterminism means independent schedules represent one trace class or otherwise all permitted choices are acceptable for execution. It is distinct from don't-know search, where the engine explores alternatives to find a requested existential result. Reversible coin rules can generate an infinite search even though every transition is well typed. Futures examples often terminate in cell-only states, but that property belongs to the encoded program/theorem, not to CLF typing itself.

Additional checks: **Why not use tensor alone in LLF?** The negative-only canonical discipline cannot directly expose an arbitrary positive multi-conclusion result. **What does a monadic let record?** One generative event and dependencies on its outputs. **Are all reorderings equal?** Only permutations of independent events. **Is `pass` a runtime cell?** No, it is the matching relation used to justify a read transition. **What must concurrency adequacy respect?** Resource-state correspondence, fresh names, and trace equivalence on both sides.

## 8. Conceptual synthesis

CLF is a logical framework whose type theory itself exposes concurrency. Positive monadic results make forward rules native, linear hypotheses represent state, existentials represent name generation, and commuting conversions represent independence. Adequacy must compare object traces and CLF expressions modulo their respective independence equalities.

## 9. Common confusions and failure modes

- LLF continuation passing is a valid encoding but obscures direct concurrency.
- Independent lets commute; dependent or competing steps do not.
- Positive tensor outputs are generated resources, not duplicated inputs.
- A well-typed generative system need not terminate.
- The source-map pages 237–248 belong to the separately headed Lecture 23.

## 10. Self-test questions with concise answers

1. **Why braces?** They embed a positive multi-result computation in a negative type eligible for forward chaining.
2. **What makes two lets independent?** Neither uses variables bound by the other's pattern, and they do not share linear inputs.
3. **How does cut allocate?** `exec/cut` produces an existentially fresh address.
4. **What does `pass` encode?** Pattern-directed application of a stored value to a continuation.
5. **Why can coin exchange diverge?** Reversible rules keep generating applicable transitions.

## 11. Related concept pages

- [CLF and monadic concurrency](../Concepts/CLF-and-Monadic-Concurrency.md)
- [Generative grammars, trace equivalence, and adequacy](../Concepts/Generative-Grammars-Trace-Equivalence-and-Adequacy.md)
- [Futures, addresses, and single assignment](../Concepts/Futures-and-Single-Assignment.md)

## 12. Source trail

Lecture 22 “The Concurrent Logical Framework”: §1 and §2, printed pp. L22.1–L22.4, PDF pp. 229–232; §3, L22.4–L22.5, PDF pp. 232–233; §4, L22.6–L22.8, PDF pp. 234–236. Mapping anomaly: PDF pp. 237–248 are explicitly Lecture 23, §§1–7, printed pp. L23.1–L23.12, and are excluded from Lecture 22 attribution.

## 13. Previous/next navigation

Previous: [Lecture 21 — Substructural Frameworks](Lecture-21-Substructural-Frameworks.md). Next: Lecture 23 — Linear Natural Deduction (source present, guide outside the requested Lectures 16–22 scope).

---
title: CLF and Monadic Concurrency
aliases:
  - Concurrent Logical Framework
  - CLF
  - monadic concurrency
tags:
  - clf
  - concurrency
  - logical-frameworks
source_lectures:
  - 22
prerequisites:
  - "[Linear logical frameworks and metatheory](Linear-Logical-Frameworks-and-Metatheory.md)"
related:
  - "[Generative grammars, trace equivalence, and adequacy](Generative-Grammars-Trace-Equivalence-and-Adequacy.md)"
  - "[Futures and single assignment](Futures-and-Single-Assignment.md)"
---

# CLF and Monadic Concurrency

## One-sentence definition

CLF extends a linear logical framework with positive types and a monadic form $\{A^+\}$ whose let-bound computations perform linear forward steps and identify independent orderings as the same concurrent trace.

## Why the concept is needed

LLF can encode rules with one negative conclusion naturally, but a forward rule such as $q\to d,d,n$ has multiple produced resources. Continuation-passing style can force it into LLF, at the cost of deeply nested proof terms and artificial ordering. CLF gives positive collections of results first-class representation and preserves the concurrency of independent rule applications.

## Intuitive model

**Intuition.** A CLF monadic computation is a transaction that consumes some uniquely named tokens and emits a package of fresh tokens. `let` opens that package for later steps. Independent transactions may be written in either order because the framework remembers causal dependence, not an arbitrary scheduler order.

## Formal core

CLF adds positive types and a negative monadic suspension:

$$
A^+,B^+::=1\mid A^+\otimes B^+\mid\exists x:A.B^+(x)\mid A,
\qquad A^-::=\cdots\mid\{A^+\}.
$$

Expressions and patterns have the schematic forms

$$
E::=\mathbf{let}\ \{p\}=M\ \mathbf{in}\ E\mid T,
$$

where $T$ packages unit, pairs, dependent witnesses, or a negative object, and $p$ binds the matching outputs. A coin rule is direct:

```text
fromQ : q -o { d * d * n }
toD   : n -o n -o { d }
```

Independent lets commute:

$$
\mathbf{let}\ p=M\ \mathbf{in}\mathbf{let}\ q=N\ \mathbf{in}\ T
=
\mathbf{let}\ q=N\ \mathbf{in}\mathbf{let}\ p=M\ \mathbf{in}\ T
$$

when $FV(p)\cap FV(N)=\varnothing=FV(q)\cap FV(M)$. This equation says neither step consumes an output of the other.

The term **monadic concurrency** highlights that effects are isolated inside $\{A^+\}$ and sequenced by `let`, while the definitional equality quotients away independent sequencing.

## How to use/read it

Represent consumable state facts as linear atomic types. Give each transition a reusable signature constant whose linear arguments are consumed and whose monadic positive result lists generated facts. Use existential output to allocate fresh names. Read data dependency between bound variables as causality; do not assign meaning to the textual order of independent lets.

## Worked example

From a quarter $q_1$ and nickel $n_1$, produce three dimes:

```text
\q1. \n1. {
  let {[d1, [d2, n2]]} = fromQ q1 in
  let {d3} = toD n1 n2 in
  [d1, d2, d3]
}
```

1. `fromQ` consumes $q_1$ and generates $d_1,d_2,n_2$.
2. `toD` consumes $n_1,n_2$ and generates $d_3$.
3. The second step is causally after the first because $n_2$ is bound by it.
4. The final positive tensor packages $d_1,d_2,d_3$.
5. Swapping the two lets is forbidden: $n_2$ would become free in `toD`.

## Non-example or boundary case

CLF does not identify steps that compete for the same linear resource or where one consumes the other's output. Nor does every forward system terminate: reversible coin exchange can run forever even though the representation is well typed.

## Key consequences

Positive outputs eliminate the continuation-passing detour. Linear types make consumption explicit. Existentials model fresh name generation. Equality by commuting independent lets represents true concurrency up to scheduling. CLF can encode futures dynamics as rules over `proc`, `cell`, and auxiliary `pass` facts.

## Relations to nearby concepts

[Linear logical frameworks and metatheory](Linear-Logical-Frameworks-and-Metatheory.md) explains the LLF limitation. [Generative grammars, trace equivalence, and adequacy](Generative-Grammars-Trace-Equivalence-and-Adequacy.md) develops the semantic view of CLF signatures and traces. [Futures and single assignment](Futures-and-Single-Assignment.md) provides the transition system encoded in Lecture 22.

## Common mistakes

- Calling monadic braces mere punctuation around a tensor.
- Swapping dependent lets.
- Treating signature rules as one-use resources.
- Assuming type correctness implies quiescence.
- Confusing textual order with causal order.

## What to remember

- CLF adds positive multi-result computations to LLF.
- Linear inputs are consumed; positive outputs are generated.
- `let` exposes generated resources.
- Independent lets commute; dependent lets do not.
- Existentials create fresh names.

## Source trail

Lecture 22, §§1–2, printed pp. L22.1–L22.4, PDF pp. 229–232; §3 “CLF,” printed pp. L22.4–L22.5, PDF pp. 232–233. The phrase “monadic concurrent linear logic programming” occurs in the cited line of work; the lecture's braces-and-let presentation supplies the monadic mechanism.


---
title: Generative Grammars, Trace Equivalence, and Adequacy
aliases:
  - CLF generative grammar
  - concurrent traces
  - representation adequacy
tags:
  - clf
  - traces
  - adequacy
source_lectures:
  - 20
  - 21
  - 22
prerequisites:
  - "[CLF and monadic concurrency](CLF-and-Monadic-Concurrency.md)"
related:
  - "[Logical frameworks and judgments as types](Logical-Frameworks-and-Judgments-as-Types.md)"
  - "[Forward proof search and inverse method](Forward-Proof-Search-and-Inverse-Method.md)"
---

# Generative Grammars, Trace Equivalence, and Adequacy

## One-sentence definition

A CLF signature acts as a generative grammar for reachable linear states, its expressions denote traces modulo permutation of independent steps, and adequacy asserts a precise two-way correspondence between object executions and those typed trace classes.

## Why the concept is needed

A transition signature is useful only if its proof objects mean the executions one intends. Raw interleaving sequences over-distinguish concurrent runs, while quotienting too aggressively can identify causally different computations. Generative-grammar and trace views state what configurations and runs are produced; adequacy proves the representation neither invents nor loses them.

## Intuitive model

**Intuition.** Transition declarations are grammar productions. A multiset of linear facts is the current sentential form, and applying a production consumes symbols and generates replacements. A trace is a derivation history, except that independent production applications are considered the same history. This analogy does not imply context-free parsing or guarantee termination.

## Formal core

Let a rule constant have type

$$
r:A_1\multimap\cdots\multimap A_m\multimap\{\exists\vec x.\,B_1\otimes\cdots\otimes B_n\}.
$$

Operationally it consumes linear facts $A_1,\ldots,A_m$, generates fresh names $\vec x$, and produces $B_1,\ldots,B_n$. A signature $\Sigma$ is therefore a **generative grammar** for states reachable from an initial multiset.

A trace is a sequence/partial order of instantiated rules. Adjacent steps $r_1,r_2$ are equivalent when neither uses a name or linear fact produced by the other and they do not compete for an input. CLF realizes this by commuting-let equality with free-variable side conditions. Trace equivalence is the reflexive, symmetric, transitive closure of these permitted swaps plus alpha-renaming of bound fresh names.

An adequacy statement must identify domains and equality explicitly. A typical form is:

> Object executions from state $S$ to $S'$, modulo exchange of independent transitions and fresh-name renaming, are in bijection with canonical CLF expressions of the encoded type, modulo CLF definitional equality.

Soundness is the left-to-right claim that encoded traces are legal; completeness/reflection is the reverse claim that every legal object trace has a representation.

## How to use/read it

Define the representation of states, transition instances, and fresh names. Specify the object trace equivalence before claiming concurrency adequacy. Prove one constructor/rule case at a time, then prove injectivity and surjectivity only up to the declared equalities. For nondeterministic execution, distinguish existential reachability from universal outcomes.

## Worked example

Suppose independent rules $r:a\multimap\{b\}$ and $s:c\multimap\{d\}$ act on initial state $a,c$.

1. Trace $t_1$ applies $r$ then $s$, reaching $b,d$.
2. Trace $t_2$ applies $s$ then $r$, reaching the same multiset.
3. In CLF, $t_1$ is `let {b}=r a in let {d}=s c in [b,d]`.
4. $t_2$ reverses the lets.
5. Each pattern binds a variable absent from the other rule call, so the commuting condition holds; $t_1=t_2$.
6. Add $u:b\multimap\{e\}$. `u b` cannot commute before `r a` because it depends on generated $b$; the causal distinction remains.

## Non-example or boundary case

Two steps both consuming $a$ are alternatives, not independent interleavings, even if they happen to produce isomorphic final states. Final-state equality alone is therefore too coarse for trace equivalence. Likewise, a one-way encoding that maps each run to some term is not yet adequate.

## Key consequences

The grammar view explains forward execution and reachability queries. Trace equivalence removes scheduler noise while preserving causality. Adequacy justifies using framework type checking and proof search as reasoning about the object transition system. For futures, terminating processes may reach quiescent cell configurations; reversible coin systems may generate infinite traces.

## Relations to nearby concepts

[CLF and monadic concurrency](CLF-and-Monadic-Concurrency.md) gives the syntax and commuting law. [Forward proof search and inverse method](Forward-Proof-Search-and-Inverse-Method.md) also saturates forward rules, but as a goal-specialized theorem prover rather than a typed trace representation. [Logical frameworks and judgments as types](Logical-Frameworks-and-Judgments-as-Types.md) gives the general adequacy obligation.

## Common mistakes

- Equating traces solely because they have the same final state.
- Commuting causally dependent or competing steps.
- Omitting alpha-equivalence for generated names.
- Calling soundness alone adequacy.
- Assuming a generative grammar is terminating or confluent.

## What to remember

- CLF rules consume and generate linear facts.
- The signature is a grammar of reachable states and traces.
- Independent scheduling order is quotiented away.
- Causality and resource conflict remain observable.
- Adequacy is a two-way correspondence modulo stated equality.

## Source trail

Lecture 22, §3, printed pp. L22.4–L22.5, PDF pp. 232–233, for positive generations and commuting independent lets; §4, printed pp. L22.6–L22.8, PDF pp. 234–236, for encoded futures traces and reachability queries. The general framework adequacy methodology is in Lecture 20, §3, printed p. L20.4, PDF p. 213, and Lecture 21, §2, printed pp. L21.2–L21.4, PDF pp. 221–223.


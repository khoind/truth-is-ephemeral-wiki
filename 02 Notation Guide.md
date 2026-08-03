---
title: Notation Guide
tags: [reference, notation]
---

# Notation Guide

## Judgments and contexts

- $\Gamma \vdash A$: $A$ follows from structural assumptions $\Gamma$; assumptions may generally be copied or discarded.
- $\Delta \vdash A$: $A$ follows from linear assumptions $\Delta$; each occurrence must be accounted for exactly once.
- Ordered contexts are sequences rather than multisets; exchange is unavailable.
- $\Gamma;\Delta\vdash A$: a mixed structural/linear judgment.
- $\Gamma\vdash A\;\mathsf{valid}$: $A$ is stable under future extensions of the ephemeral context.
- $\Delta\longrightarrow\Delta'$: one state transition; $\longrightarrow^*$ is zero or more transitions.

A context is not just punctuation: comma behavior is determined by its structural laws. Exchange permits reordering, weakening permits unused assumptions, and contraction permits reuse/duplication.

## Core linear connectives

| Form | Informal reading | Polarity tendency |
|---|---|---|
| $A\otimes B$ | provide both resources | positive |
| $1$ | provide no further resource | positive |
| $A\oplus B$ | provider selects a branch | positive |
| $0$ | impossible positive choice | positive |
| $A\mathbin{\&}B$ | client selects a branch | negative |
| $\top$ | trivially offer any external observation | negative |
| $A\multimap B$ | receive/use $A$, then behave as $B$ | negative |

The course sometimes uses presentation-specific symbols such as $\times$, $+$, $\to$, or message/process notation. Always read a connective through its introduction rules rather than typography alone.

## Modes and shifts
A mode $m$ carries structural properties $\sigma(m)\subseteq\{W,C\}$. A preorder $m\ge k$ controls which assumptions may depend on which modes. Shifts $\uparrow^m_k A_k$ and $\downarrow^k_m A_m$ move propositions across mode boundaries subject to the dependence relation.

## Polarity and focusing
Positive types are introduced by noninvertible right rules; negative types by invertible right rules. Focused judgments use brackets to mark the one formula undergoing synchronous decomposition. Phase markers are metasyntax, not object-language connectives.

## Processes, channels, and futures
A typing judgment such as $\Delta\vdash P::(x:A)$ says that process $P$ uses channels in $\Delta$ and provides behavior $A$ along $x$. Cut composes a provider and client over a fresh channel. In the futures interpretation, an address is written once and may be read by dependent computations; linearity controls ownership and use.

## Quantifiers
$\forall x. A(x)$ offers behavior uniformly for a fresh/eigenvariable; $\exists x. A(x)$ packages a witness with evidence. Side conditions on freshness prevent a proof from depending on an accidentally chosen name.

[Home](00%20Home.md) · [Formula and Rule Sheet](07%20Formula%20and%20Rule%20Sheet.md)

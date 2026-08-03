---
title: Cut Elimination for SAX
aliases: [SAX normalization, snip elimination]
tags: [cut-elimination, sax, analytic-cut, snip, lecture-14]
source_lectures: ["Lecture 14 - Semi-Axiomatic Sequent Calculus"]
prerequisites: [Semi-Axiomatic Sequent Calculus and SAX, ordinary cut elimination]
related: [Cut Elimination Across Modes, Continuation Channels, Focusing]
---

# Cut Elimination for SAX

## One-sentence definition

**Cut elimination for SAX removes all nonanalytic compositions but generally retains restricted analytic cuts called snips, because message axioms need composition to build nested positive or negative structure.**

## Why the concept is needed

SAX has the same provability as ordinary sequent calculus, yet its information rules are axioms. Consequently some cut-free ordinary proofs translate to SAX proofs containing cuts. Demanding traditional cut elimination would falsely declare valid sequents unprovable. A refined normalization theorem must identify the irreducible cuts and still connect proof reduction to process execution.

## Intuitive model

**Intuition.** Ordinary cut elimination can inline every intermediate function. SAX messages are intentionally tiny constructors, so composing constructors is normal. A snip is a local splice that builds a larger message from an immediate submessage; arbitrary hidden intermediates can still be eliminated.

## Formal core

SAX retains

$$
\frac{\Delta\vdash A\quad\Delta',A\vdash C}
{\Delta,\Delta'\vdash C}\;\mathsf{cut}.
$$

An **analytic cut** has a cut formula that is a subformula of the endsequent. A **snip** is a more restricted analytic cut in which one premise is a SAX axiom or is itself constructed by snips. The lecture intentionally leaves the exact inductive definition for later work; one should not invent a stronger formal clause here.

Soundness/completeness translations yield a normalization argument:

1. Translate a SAX derivation to ordinary sequent calculus, expanding message axioms using identity.
2. Eliminate all ordinary cuts.
3. Translate the cut-free sequent derivation back to SAX.
4. The back-translation inserts only the local analytic compositions needed to simulate ordinary information rules—snips.

A direct SAX reduction algorithm can likewise reduce general cuts while leaving snips, more closely reflecting computation.

## How to use/read it

When a SAX proof contains cut, ask whether the cut composes a message axiom with its immediate continuation structure. If yes, it may be an intended snip. If the cut formula introduces a non-subformula intermediate, normalization should remove it. At runtime, a cut connecting `send` and `recv` reduces by message matching; a cut allocating the continuation chain may persist as construction structure.

## Worked example

Consider distinct atoms $P,Q,R$ and the derivable sequent

$$Q\vdash(P\oplus Q)\oplus R.$$

1. Use SAX axiom $Q\vdash P\oplus Q$ for the right injection of the inner sum.
2. Use SAX axiom $P\oplus Q\vdash(P\oplus Q)\oplus R$ for the left injection of the outer sum.
3. Cut the two derivations on $P\oplus Q$.
4. The cut formula is a subformula of the conclusion and the second premise is an axiom, so this is the characteristic snip shape.
5. No invertible rule or single SAX axiom derives the endsequent directly, so erasing this cut would get stuck.

The retained composition corresponds to two linked messages.

## Non-example or boundary case

A cut through an unrelated proposition $D$ not occurring in either the assumptions or conclusion is not analytic and cannot be justified as a snip merely because one premise is short. It should disappear under normalization. Conversely, “cut is not eliminable” does not mean every cut is irreducible; message-receipt cuts reduce immediately, and nonanalytic intermediates can be removed.

## Key consequences

SAX has a weaker but computationally meaningful normalization theorem. It preserves the subformula discipline up to tightly controlled composition, explains explicit continuation-channel allocation, and separates proof-theoretic normality from the absence of every cut symbol. This is different from adjoint multicut, which generalizes multiplicity rather than retaining analytic constructors.

## Relations to nearby concepts

[Semi-Axiomatic Sequent Calculus and SAX](Semi-Axiomatic%20Sequent%20Calculus%20and%20SAX.md) explains why the axioms require cut. [Continuation Channels](Continuation%20Channels.md) gives snips an operational linked-message reading. [Cut Elimination Across Modes](Cut%20Elimination%20Across%20Modes.md) solves explicit contraction by multicut, a separate issue.

## Common mistakes

- Claiming SAX enjoys traditional cut elimination.
- Claiming no SAX cuts reduce.
- Calling every analytic cut a snip without the premise restriction.
- Presenting an exact snip definition absent from the source.
- Confusing proof normalization with process quiescence.

## What to remember

- Full cut-freeness is too strong for SAX.
- Normal SAX proofs may contain snips.
- Snips are restricted analytic compositions.
- Translation through cut-free sequent calculus removes all other cuts.
- Direct reductions connect the theorem to execution.

## Source trail

Lecture 14, §§6–8, printed lecture pages L14.5–L14.8, PDF pages 152–155. See [Lecture 14 - Semi-Axiomatic Sequent Calculus](../Lectures/Lecture%2014%20-%20Semi-Axiomatic%20Sequent%20Calculus.md).

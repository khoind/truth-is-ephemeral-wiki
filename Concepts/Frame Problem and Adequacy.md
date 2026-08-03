---
title: "Frame Problem and Adequacy"
aliases:
  - "local state change and adequacy"
  - "frame preservation"
tags:
  - concept
  - state-change
  - metatheory
source_lectures:
  - 1
prerequisites:
  - "Linear and ordered inference"
related:
  - "Linear Inference"
  - "Ordered Inference"
  - "State Saturation and Quiescence"
---

# Frame Problem and Adequacy

## 1. One-sentence definition

**Substructural framing makes every rule preserve its unmatched context automatically, while adequacy is the metalevel proof that the resulting formal states and executions correspond exactly to the intended domain states and behaviors.**

## 2. Why the concept is needed

A state-changing specification faces two separate risks. First, a local action may require an ever-growing list of facts that it does *not* change; this is the frame problem. Second, even elegant rules may manipulate malformed encodings or reach formal states with no intended meaning; this is the adequacy problem.

Linear and ordered inference address the first risk by construction. They do not automatically solve the second. A specification still needs legal-input conditions, an execution policy, an interpretation of outputs, and a soundness/completeness argument.

## 3. Intuitive model

**Intuition.** Editing one cell in a spreadsheet should not require a sentence saying that every other cell stays fixed. The untouched cells form a frame. But a syntactically valid spreadsheet file could still encode nonsense for a particular accounting task. Adequacy is the audit that valid encodings and permitted edits mean exactly what the domain claims they mean.

## 4. Formal core

For linear inference, suppose a rule instance consumes multiset $P$ and produces multiset $Q$. If the whole state decomposes as

$$\Delta=R\uplus P,$$

then the transition is

$$R\uplus P\longrightarrow R\uplus Q.$$

$R$ is the unmatched **frame** and $\uplus$ is multiset union. For ordered inference the analogous decomposition is

$$\Omega=\Omega_L P\Omega_R
\longrightarrow
\Omega_L Q\Omega_R,$$

where $P$ and $Q$ are sequences and the prefix $\Omega_L$ and suffix $\Omega_R$ are preserved.

An adequacy statement needs an encoding $\llbracket d\rrbracket$ from domain configurations $d$ to formal states, a domain transition relation $d\Rightarrow d'$, and a formal relation $\longrightarrow$. A typical one-step correspondence has two directions:

- **soundness:** if $\llbracket d\rrbracket\longrightarrow X$, then there is a valid $d'$ with $d\Rightarrow d'$ and $X=\llbracket d'\rrbracket$;
- **completeness:** if $d\Rightarrow d'$, then $\llbracket d\rrbracket\longrightarrow\llbracket d'\rrbracket$.

For planning or normalization, the theorem may instead concern $\Rightarrow^*$ and $\longrightarrow^*$, final states, or acceptance. It must quantify over well-formed domain configurations or a formally defined invariant $\mathrm{Valid}(X)$.

## 5. How to use/read it

Design local rules by listing precisely the facts that cease and begin to hold. Conditions needed for locality should often be represented positively as maintained resources, rather than as negative searches through the entire frame.

Then state three metalevel clauses:

1. the class of valid initial encodings;
2. the execution discipline, such as exhaustive reachability or don’t-care normalization;
3. the exact meaning of a reachable or quiescent formal state.

Prove preservation of validity and both directions of the chosen correspondence. Calling a representation “adequate” without these clauses hides the most important modeling assumptions.

## 6. Worked example

Model a single-slot locker. Domain configurations are `empty` or `full(p)` for one parcel identifier $p$. Use linear propositions `vacant` and $\mathit{stored}(p)$, with actions represented by rules

$$
\frac{\mathit{vacant}\quad\mathit{arrives}(p)}{\mathit{stored}(p)}\;\mathsf{deposit}
\qquad
\frac{\mathit{stored}(p)\quad\mathit{code}(p)}{\mathit{vacant}}\;\mathsf{collect}.
$$

Suppose the full system state also contains an unrelated token `camera-on`.

1. From `[vacant, arrives(k), camera-on]`, `deposit` yields `[stored(k), camera-on]`.
2. The camera token is the frame; no rule needs a special premise and conclusion saying it remains on.
3. Encode `empty` as `[vacant]` and `full(k)` as `[stored(k)]`, with transient arrival/code tokens treated as action inputs.
4. A validity invariant requires exactly one of `vacant` or `stored(p)` for exactly one $p$.
5. Soundness says each formal locker step corresponds to the matching deposit or collection action. Completeness says every legal domain action has the displayed formal step.

The local frame behavior is automatic, but the “exactly one locker status” invariant and the status/action distinction are adequacy work.

## 7. Non-example or boundary case

Consider a pickup rule with a premise “there exists no object above $x$.” If that premise is checked by scanning the entire unmatched state, adding an unrelated new proposition can alter applicability. The rule is no longer local in the intended substructural sense. A maintained positive token such as $\mathit{clear}(x)$ makes the enabling condition part of the matched footprint.

Also, a rule set that preserves an invariant on valid inputs is not automatically adequate if it omits a legal domain action; that would be sound but incomplete.

## 8. Key consequences

- Local rules are modular under extension by unrelated resources.
- Positive state tokens can replace nonlocal absence tests.
- Frame preservation is built into substructural matching, not added by separate axioms.
- Adequacy includes representation, strategy, and interpretation, not just transition syntax.
- Soundness excludes spurious formal behavior; completeness excludes missing intended behavior.
- Validity of initial and intermediate states is a metatheoretic invariant.

## 9. Relations to nearby concepts

[Linear Inference](Linear%20Inference.md) carries an unordered remainder; [Ordered Inference](Ordered%20Inference.md) carries an ordered prefix and suffix. [State Saturation and Quiescence](State%20Saturation%20and%20Quiescence.md) tells when exploration or a run stops, while adequacy tells what stopping means. [Nondeterminism Dont-Care vs Dont-Know](Nondeterminism%20Dont-Care%20vs%20Dont-Know.md) is part of the execution clause of an adequacy statement. [CBA Diagrams and True Concurrency](CBA%20Diagrams%20and%20True%20Concurrency.md) makes matched resources and preserved independence visible in proofs.

## 10. Common mistakes

- Claiming the frame problem is solved while using global negative side conditions.
- Listing every unchanged fact in every rule, making extensions nonmodular.
- Stating only soundness and calling it exact correspondence.
- Omitting the definition of valid initial states.
- Letting quiescence stand in for an output specification.
- Treating the scheduler as if it were encoded by the inference rules.

## 11. What to remember

- The frame is the unmatched state preserved by a local rewrite.
- Linear frames are multisets; ordered frames are prefix/suffix sequences.
- Rules alone do not define legal inputs, search strategy, or successful outputs.
- Adequacy normally needs soundness and completeness.
- State well-formedness must be stated and preserved.

## 12. Source trail

- Lecture 1, §3 “Linear Inference,” printed pp. L1.4–L1.5, PDF pp. 4–5, especially the frame-problem discussion on L1.5/PDF 5.
- Lecture 1, §4 “Ordered Inference,” printed pp. L1.5–L1.7, PDF pp. 5–7, especially the adequacy template on L1.6–L1.7/PDF 6–7.
- Lecture 1, §5 “Binary Increment as Ordered Inference,” printed p. L1.7, PDF p. 7.
- Lecture 1, §6 “Blocks World as Linear Inference,” printed pp. L1.8–L1.9, PDF pp. 8–9.


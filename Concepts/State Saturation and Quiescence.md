---
title: "State Saturation and Quiescence"
aliases:
  - "closure and stuckness"
  - "saturated states"
  - "quiescent states"
tags:
  - concept
  - operational-semantics
  - inference
source_lectures:
  - 1
prerequisites:
  - "One-step and multi-step inference"
related:
  - "Structural Inference"
  - "Linear Inference"
  - "Nondeterminism Dont-Care vs Dont-Know"
---

# State Saturation and Quiescence

## 1. One-sentence definition

**Saturation is closure under every possible inference consequence, whereas quiescence is the local condition that one particular state has no enabled inference step.**

## 2. Why the concept is needed

“Nothing more happens” can mean two different things. In a monotone fact database, it means every consequence is already present. In a rewriting system, it means the current resources match no rule. A third situation arises when analyzing nondeterministic rewriting: the *collection* of discovered states is saturated once every successor of every discovered state has also been discovered.

Conflating these conditions leads to incorrect algorithms. Stopping at one quiescent branch can miss other reachable states. Conversely, trying to make one linear state contain every alternative misunderstands state change.

## 3. Intuitive model

**Intuition.** Saturation resembles completing a map: every road leaving a mapped location ends at another mapped location. Quiescence resembles standing at a location with no outgoing road. A completed map may contain many locations with outgoing roads, and a dead end can be encountered long before the map is complete.

## 4. Formal core

Let $X\longrightarrow Y$ mean that one instantiated inference rule transforms state $X$ into state $Y$. Let $\longrightarrow^*$ be its reflexive-transitive closure, so $X\longrightarrow^*X$ and any finite chain is included.

A state $Q$ is **quiescent** when

$$\neg\exists Q'.\;Q\longrightarrow Q'.$$

For structural inference, let $S$ be a set of facts and $T(S)$ the set of all conclusions of rule instances whose premises lie in $S$. Because structural firing only adds facts, $S$ is **saturated** when

$$T(S)\subseteq S.$$

The least saturated extension of initial facts $S_0$ is the least fixed point of $F(S)=S\cup T(S)$, when understood mathematically even if iterative computation does not terminate.

For linear or ordered inference, define the reachable collection

$$\mathrm{Reach}(X_0)=\{X\mid X_0\longrightarrow^*X\}.$$

A candidate collection $R$ is reachability-saturated relative to $X_0$ when $X_0\in R$ and

$$X\in R\land X\longrightarrow Y\;\Rightarrow\;Y\in R.$$

This closure property belongs to $R$, not generally to an individual rewriting state. A finite saturated reachable set may contain cycles and nonquiescent states.

## 5. How to use/read it

For structural bottom-up evaluation, repeatedly add genuinely new facts. Stop when a complete pass produces none; the database is saturated. Proof novelty does not count as fact novelty.

For don’t-know linear or ordered exploration, maintain a worklist of discovered but unexpanded states. Remove a state, generate every successor, and add unseen successors. Stop when the worklist is empty; the discovered collection is saturated.

For don’t-care normalization, follow one enabled transition at a time until no step exists. Stop at quiescence—but call the result successful only if a separate adequacy condition identifies that normal form as an answer.

## 6. Worked example

Consider a linear two-color toggle:

$$
\frac{\mathit{red}}{\mathit{green}}\;r_g
\qquad
\frac{\mathit{green}}{\mathit{red}}\;g_r.
$$

Start from $X_0=[\mathit{red}]$.

1. The first rule gives $[\mathit{red}]\longrightarrow[\mathit{green}]$.
2. The second gives $[\mathit{green}]\longrightarrow[\mathit{red}]$.
3. The reachable collection is therefore $R=\{[\mathit{red}],[\mathit{green}]\}$.
4. Every successor of a state in $R$ is already in $R$, so $R$ is saturated.
5. Neither member is quiescent, because each enables one rule.

Now add a one-way rule $\mathit{green}\to\mathit{off}$ and remove $g_r$. The state `[off]` is quiescent, and the finite reachable set `{[red], [green], [off]}` is saturated. These are two different claims about two different objects.

## 7. Non-example or boundary case

A quiescent ordered word is not automatically an accepted word. With only the deletion rule $a\,b\to\cdot$, the word $b\,a$ is quiescent but does not reduce to empty. Acceptance must say “quiescent *and empty*,” or otherwise specify the desired terminal language.

Likewise, a structural generator such as $p(n)\to p(n+1)$ never reaches a finite saturated database from $p(0)$, although each finite stage is a valid partial result.

## 8. Key consequences

- Structural saturation is a fixed-point property of a fact set.
- Reachability saturation is a closure property of a collection of changing states.
- Quiescence is a no-successor property of one state.
- Saturation does not imply that all contained states are quiescent.
- Quiescence does not imply success, uniqueness, or global exploration.
- Termination must be established separately in every regime.

## 9. Relations to nearby concepts

[Structural Inference](Structural%20Inference.md) naturally computes one monotone saturated fact set. [Linear Inference](Linear%20Inference.md) and [Ordered Inference](Ordered%20Inference.md) instead rewrite states, so saturation normally applies to their reachability graph. [Nondeterminism Dont-Care vs Dont-Know](Nondeterminism%20Dont-Care%20vs%20Dont-Know.md) determines whether reaching one quiescent state is enough or exhaustive closure is required. [Frame Problem and Adequacy](Frame%20Problem%20and%20Adequacy.md) supplies the statement that tells us what a quiescent or reachable result means.

## 10. Common mistakes

- Calling any state with no *newly printed* facts quiescent when rules are still enabled.
- Saturating proof terms rather than propositions in a structural database.
- Calling one linear multiset saturated because a chosen run stopped.
- Assuming a finite reachable set must contain a quiescent state.
- Assuming a quiescent state is a valid answer.
- Claiming termination from closure definitions alone.

## 11. What to remember

- Saturation means closure; quiescence means no enabled step.
- Always identify whether the subject is one state or a collection of states.
- Structural saturation adds facts to one set.
- Substructural reachability saturation completes a state graph.
- A success criterion and a termination argument are separate obligations.

## 12. Source trail

- Lecture 1, §2 “Structural Inference,” printed pp. L1.2–L1.3, PDF pp. 2–3.
- Lecture 1, §3 “Linear Inference,” printed pp. L1.4–L1.5, PDF pp. 4–5.
- Lecture 1, §§4–5 “Ordered Inference” and “Binary Increment as Ordered Inference,” printed pp. L1.5–L1.7, PDF pp. 5–7.
- Lecture 1, §7 “Summary,” printed pp. L1.9–L1.10, PDF pp. 9–10.


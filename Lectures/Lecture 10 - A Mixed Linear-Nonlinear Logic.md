---
title: "Lecture 10 - A Mixed Linear-Nonlinear Logic"
lecture: 10
date: 2023-09-28
pdf_pages: "113-122"
printed_pages: "L10.1-L10.10"
tags:
  - lecture
  - lnl
  - linear-logic
  - structural-logic
  - shifts
  - session-types
prerequisites:
  - validity
  - Girard's exponential
  - linear and intuitionistic sequent calculi
  - process interpretation of proofs
---

# Lecture 10 - A Mixed Linear-Nonlinear Logic

## 1. Why this lecture exists

The validity account of $!A$ controls reuse, but it combines two logically different transitions in one connective. Promotion may have to wait for the linear context to empty, so $!$ is not right-invertible; using a banged assumption also involves a staged move through validity, so it is not left-invertible either. Worse, translating all structural logic into linear logic may preserve provability while obscuring native functional meaning or changing observable behavior.

Mixed linear/nonlinear logic (LNL) keeps structural and linear propositions as equally native strata. Two shifts connect them: $\uparrow$ moves a linear proposition into the structural language, while $\downarrow$ moves a structural proposition into the linear language. Their composition recovers $!A=\downarrow\uparrow A$, but the separate shifts have clean polarities and direct process behavior. LNL is therefore both a better account of mixed functional/message-passing programs and the two-mode prototype for [adjoint logic](../Concepts/Adjoint%20Logic.md).

## 2. Learning objectives

After this lecture, a reader should be able to:

- read LNL's two proposition grammars and two judgment forms;
- explain the independence of structural conclusions from linear assumptions;
- apply all implication, shift, identity, and cut rules with the correct context discipline;
- derive $!A$ as $\downarrow\uparrow A$ and determine the polarity of each shift;
- state identity, cut, and conservative-extension metatheorems without confusing them with primitive rules;
- trace the operational interaction of structural and linear channels;
- explain why recursive `mapreduce` needs structurally reusable function services and where parallelism arises.

## 3. Dependency map

[Validity](../Concepts/Validity.md) explains why structural conclusions must not depend on live linear resources. [Girard vs Andreoli exponentials](../Comparisons/Girard%20vs%20Andreoli%20Exponentials.md) supplies the compound behavior later factored as $\downarrow\uparrow$. Native [Structural inference](../Concepts/Structural%20Inference.md) and [Linear inference](../Concepts/Linear%20Inference.md) become separate modes, joined by [Shifts between logics](../Concepts/Shifts%20Between%20Logics.md). Their proof terms extend the process reading of [Linear message passing and session types](../Concepts/Linear%20Message%20Passing%20and%20Session%20Types.md), and the mode-parametric pattern is generalized in [Lecture 11](Lecture%2011%20-%20Adjoint%20Logic.md).

## 4. Section-by-section reconstruction

### 1. Introduction

Lecture 9 established a compositional embedding of structural logic into linear logic, but two problems remain. First, $!$ has mixed polarity: neither its right nor its left rule is always invertible. Second, a derivability-preserving translation need not preserve the intended observations of a functional program, so it is not automatically a satisfactory compiler.

LNL answers by combining two logics directly. Structural logic continues to describe reusable functional values; linear logic continues to describe one-use resources and message-passing channels. The system is a variant of Benton's mixed linear/nonlinear logic and a stepping stone to the general mode discipline of adjoint logic.

### 2. Shifting Between Logics

LNL has two mutually related grammars:

$$
\begin{aligned}
A_S &::= P_S \mid A_S\supset B_S \mid A_S\land B_S \mid \top_S
       \mid A_S\lor B_S \mid \bot_S \mid \uparrow A_L,\\
A_L &::= P_L \mid A_L\multimap B_L \mid A_L\otimes B_L \mid 1
       \mid A_L\mathbin{\&}B_L \mid \top_L \mid A_L\oplus B_L \mid 0
       \mid \downarrow A_S.
\end{aligned}
$$

Subscripts $S$ and $L$ are **modes**, not truth values: they indicate structural or linear propositions. $P_S,P_L$ are atoms. Structural implication, product, sum, truth, and falsehood are $\supset,\land,\lor,\top_S,\bot_S$. Their linear relatives are $\multimap,\otimes,\oplus,1,0$, with additive conjunction $\mathbin{\&}$ and its unit $\top_L$. The extraction renders $\mathbin{\&}$ as “N”; this guide uses the conventional symbol.

The two judgment forms are

$$
\Gamma_S;\Delta_L\vdash A_L
\qquad\text{and}\qquad
\Gamma_S\vdash A_S.
$$

$\Gamma$ is structural and may weaken or contract; $\Delta$ is a linear multiset that must be consumed exactly once. A structural conclusion has no $\Delta$ at all. This is the independence principle inherited from validity: persistent truth cannot capture ephemeral dependencies.

The intended combination must eliminate cut and expand identity. It must also be conservative: a shift-free structural proof should be essentially a proof of intuitionistic logic, and a shift-free linear proof with empty $\Gamma$ should be essentially a proof of linear logic—not merely have the same yes/no provability result.

### 3. Rules for Implication

Right introduction is native in each mode:

$$
\frac{\Gamma,A_S\vdash B_S}{\Gamma\vdash A_S\supset B_S}\;\supset R
\qquad
\frac{\Gamma;\Delta,A_L\vdash B_L}{\Gamma;\Delta\vdash A_L\multimap B_L}\;\multimap R.
$$

A linear implication can occur only in a linear judgment, so it has one left rule:

$$
\frac{\Gamma;\Delta_1\vdash A_L\qquad
      \Gamma;\Delta_2,B_L\vdash C_L}
     {\Gamma;\Delta_1,\Delta_2,A_L\multimap B_L\vdash C_L}\;\multimap L.
$$

The linear contexts are partitioned between the premises; the same structural $\Gamma$ is shared.

A structural implication may be used while proving either a structural or a linear conclusion. It therefore has two left rules:

$$
\frac{\Gamma,A_S\supset B_S\vdash A_S\qquad
      \Gamma,A_S\supset B_S,B_S;\Delta\vdash C_L}
     {\Gamma,A_S\supset B_S;\Delta\vdash C_L}\;\supset L_{SL}
$$

$$
\frac{\Gamma,A_S\supset B_S\vdash A_S\qquad
      \Gamma,A_S\supset B_S,B_S\vdash C_S}
     {\Gamma,A_S\supset B_S\vdash C_S}\;\supset L_{SS}.
$$

The first subscript identifies the implication's structural mode; the second identifies the conclusion mode. Both premises proving $A_S$ must use the structural judgment, and the structural result $B_S$ belongs in $\Gamma$. LNL's five implication rules are correct but repetitive; Lecture 11 replaces them with one mode-indexed right rule and one mode-indexed left rule.

### 4. Rules for Shifts

The four shift rules are

$$
\frac{\Gamma;\cdot\vdash A_L}{\Gamma\vdash\uparrow A_L}\;\uparrow R
\qquad
\frac{\Gamma,\uparrow A_L;\Delta,A_L\vdash C_L}
     {\Gamma,\uparrow A_L;\Delta\vdash C_L}\;\uparrow L,
$$

$$
\frac{\Gamma\vdash A_S}{\Gamma;\cdot\vdash\downarrow A_S}\;\downarrow R
\qquad
\frac{\Gamma,A_S;\Delta\vdash C_L}
     {\Gamma;\Delta,\downarrow A_S\vdash C_L}\;\downarrow L.
$$

$\uparrow R$ is the former validity rule: a linear proposition enters the structural layer only when it has no linear dependencies. $\uparrow L$ spawns one fresh linear use from a reusable structural service. $\downarrow R$ packages a structural value as a linear proposition, again with no linear residue. $\downarrow L$ opens such a package and places its structural payload in $\Gamma$.

The decomposition

$$
!A_L\;\overset{\mathrm{def}}{=}\;\downarrow\uparrow A_L
$$

explains the old polarity anomaly. $\uparrow$ is negative because its right rule is invertible: any proof ending at $\uparrow A_L$ can be reduced to the premise without making a choice. $\downarrow$ is positive because its left rule is invertible. Their composition is positive outside and negative inside, so $!$ is not uniformly one polarity. See [Positive versus negative polarity](../Comparisons/Positive%20vs%20Negative%20Polarity.md).

### 5. Identity and Cut

There is one identity schema per judgment:

$$
\frac{}{\Gamma,A_S\vdash A_S}\;\mathsf{id}_S
\qquad
\frac{}{\Gamma;A_L\vdash A_L}\;\mathsf{id}_L.
$$

There are three mode-correct cuts:

$$
\frac{\Gamma\vdash A_S\qquad\Gamma,A_S\vdash C_S}
     {\Gamma\vdash C_S}\;\mathsf{cut}_{SS},
$$

$$
\frac{\Gamma\vdash A_S\qquad\Gamma,A_S;\Delta'\vdash C_L}
     {\Gamma;\Delta'\vdash C_L}\;\mathsf{cut}_{SL},
$$

$$
\frac{\Gamma;\Delta\vdash A_L\qquad\Gamma;\Delta',A_L\vdash C_L}
     {\Gamma;\Delta,\Delta'\vdash C_L}\;\mathsf{cut}_{LL}.
$$

There is no $\mathsf{cut}_{LS}$: a proof of a structural conclusion may not depend on a linear proposition. Expanded identities are admissible by simultaneous induction on $A_S$ and $A_L$. All three cuts are admissible by a simultaneous nested induction on the cut formula and the two premise derivations. Structural weakening may be needed to align the shared $\Gamma$ in the premises.

Cut elimination yields strong conservativity. If $\Gamma,A_S$ contain no $\uparrow$, then $\Gamma\vdash A_S$ in LNL exactly when the same sequent is derivable in intuitionistic logic. If $\Delta,A_L$ contain no $\downarrow$, then $\cdot;\Delta\vdash A_L$ exactly when $\Delta\vdash A_L$ in pure linear logic. In a cut-free proof, the subformula property prevents shifts from appearing out of nowhere, leaving precisely the native fragment's rules.

### 6. Examples

The upshift preserves implication with the appropriate change of mode:

$$
\vdash \uparrow(A_L\multimap B_L)\supset
       (\uparrow A_L\supset\uparrow B_L).
$$

To use the two structural upshifts, $\uparrow L$ obtains linear instances of the function and argument; $\multimap L$ applies one to the other; $\uparrow R$ returns the result to the structural mode.

Downshift likewise preserves structural implication as a linear implication:

$$
\cdot;\cdot\vdash
\downarrow(A_S\supset B_S)\multimap
(\downarrow A_S\multimap\downarrow B_S).
$$

$\downarrow L$ opens the two linear packages into structural assumptions, $\supset L$ performs structural application, and $\downarrow R$ repackages $B_S$. The inherited laws of $!$ follow by replacing it with $\downarrow\uparrow$; the extra shift steps are administrative but now each has a definite polarity.

### 7. A Programming Example

The example folds a binary tree with data at leaves:

$$
\mathsf{tree}_A=\oplus\{\mathsf{leaf}:A,\;\mathsf{node}:\mathsf{tree}_A\otimes\mathsf{tree}_A\}.
$$

`mapreduce` receives a result channel $r:B$, a leaf function $h:A\multimap B$, a combining function $f:B\multimap(B\multimap B)$, and a tree channel. A recursive traversal uses $h$ once for every leaf and $f$ once for every internal node. Linear channels for $h$ and $f$ cannot support an input-dependent number of calls. Their correct types are therefore

$$
h_S:\uparrow(A\multimap B),\qquad
f_S:\uparrow(B\multimap(B\multimap B)).
$$

Each recursive branch requests a fresh linear instance from the same structural service. The tree itself remains linear: the traversal consumes each node exactly once. The alternative uncurried combiner $\uparrow((B\otimes B)\multimap B)$ requires constructing an explicit pair channel before invoking the function, but expresses the same resource behavior.

### 8. Dynamics of the Shifts

Channel annotations turn the rules into processes. For $\uparrow R$, a provider on structural channel $x_S:\uparrow A_L$ receives a fresh linear channel $y_L$ and continues as a provider of $A_L$ on $y_L$:

$$
\mathsf{recv}\;x_S(\langle y_L\rangle\Rightarrow P(y_L)).
$$

The $\uparrow L$ client sends such a fresh channel:

$$
\mathsf{send}\;x_S(\langle y_L\rangle\Rightarrow Q(y_L)).
$$

A naive reduction that consumes both endpoints is wrong because $x_S$ may have several clients. The structural provider must persist, like a server that spawns one private connection per request. Operationally, interaction on $a_S$ creates a fresh $b_L$, spawns $P(b_L)$ for that request, continues $Q(b_L)$ for the client, **and retains** the provider on $a_S$ for later requests. The runtime state therefore contains persistent objects (set-like) and ephemeral processes (multiset-like).

The persistent provider originates from $\mathsf{cut}_{SL}$. A cut creates a fresh structural channel $a_S$ joining a structural provider $P$ to a linear client $Q$; the provider remains available as $Q$ and possibly other clients request instances.

For $\downarrow$, roles reverse. A provider of $x_L:\downarrow A_S$ sends a fresh structural channel $y_S$; a client receives it. Their interaction consumes the one-shot wrapper $x_L$ but creates a structural service/value at fresh $b_S$. Thus $\uparrow$ crosses from a reusable interface to a fresh linear session, while $\downarrow$ crosses from a linear package to a structural payload.

### 9. Example Continued

In the leaf branch, `mapreduce` requests a fresh $h':A\multimap B$ from $h_S$, sends the leaf channel to $h'$, and forwards the result to $r$. In the node branch it splits the tree channel, launches two recursive calls producing $x:B$ and $y:B$, requests a fresh $f'$ from $f_S$, sends $x$ and $y$, then forwards $f'$ to $r$.

The structural status of $h_S$ and $f_S$ is not incidental: the leaf branch uses $h_S$ once and $f_S$ zero times; the node branch may lead to arbitrarily many uses of both. The two recursive calls are independent and can run concurrently. Moreover, the combining process may be started before both recursive results finish; channel communication synchronizes only when their values are actually demanded. This producer/consumer overlap is pipelining, not merely tree-level fork/join parallelism.

### 10. Summary

LNL directly combines native structural and linear fragments. It factors $!$ into a negative upshift and a positive downshift, preserves each pure fragment by cut elimination, and gives the shifts a persistent/ephemeral message-passing semantics. Categorically, $\uparrow$ and $\downarrow$ form an adjunction: $\downarrow\uparrow$ is a comonad on the linear side, while $\uparrow\downarrow$ is a monad on the structural side. The next lecture abstracts the two fixed modes into a preorder of modes with configurable structural properties.

## 5. Formal core

The notation has four context/proposition roles:

- $A_S,B_S,C_S$ range over structural propositions; $A_L,B_L,C_L$ over linear propositions.
- $\Gamma$ is a structural context, shared unchanged across premises and admitting weakening/contraction.
- $\Delta,\Delta_1,\Delta_2$ are linear multisets. Writing $\Delta_1,\Delta_2$ means disjoint resource partition, not duplication.
- $\cdot$ denotes an empty context; $x_S,x_L$ distinguish channel modes; a fresh channel is absent from the current configuration.

The independence invariant can be stated syntactically: the only judgment concluding $A_S$ is $\Gamma\vdash A_S$. There is no well-formed sequent $\Gamma;\Delta\vdash A_S$. Consequently no rule, cut, or proof term can smuggle a live linear dependency into a persistent result.

The shifts are the formal bridge:

| Shift | Source and target | Invertible side | Computational interface |
|---|---|---|---|
| $\uparrow A_L$ | linear proposition represented structurally | right | reusable server spawning a fresh linear session |
| $\downarrow A_S$ | structural proposition packaged linearly | left | one-shot wrapper transmitting a structural channel |

The main metatheorems are:

1. **Identity admissibility:** compound identities can be expanded from atomic identities, simultaneously across both modes.
2. **Cut admissibility:** all $SS$, $SL$, and $LL$ cuts can be eliminated.
3. **Conservative extension:** shift-free proofs in either fragment contain only that fragment's rules after cut elimination.

These theorems establish proof-theoretic compatibility. They do not alone prove contextual equivalence, cost preservation, or compiler correctness for a chosen programming semantics.

## 6. Operational/computational reading

An LNL configuration has two kinds of inhabitants. Linear processes and messages form a multiset: consuming a matching item removes it. Structural providers form a persistent set-like component: matching a request may spawn work without consuming the provider. The distinction mirrors the two antecedent zones exactly.

The web-server intuition is accurate only as intuition. Formally, persistence comes from structural proof rules and the dynamics corresponding to $\mathsf{cut}_{SL}$; it is not an untyped implementation trick. Fresh cross-mode channels make each spawned linear session independent, preserving linear ownership even when the factory that creates sessions is reusable.

For `mapreduce`, this yields three layers of behavior: the tree channel enforces exactly-once traversal; the shifted functions allow demand-dependent reuse; futures/channels let recursive producers overlap with the combining consumer. [Futures and single assignment](../Concepts/Futures-and-Single-Assignment.md) develops the synchronization mechanism further.

## 7. Worked derivation or trace in original notation and prose

Here is an original proof showing that a linearly received package of a structural pair can be separated into two linearly packaged components:

$$
\cdot;\downarrow(A_S\land B_S)
\vdash \downarrow A_S\otimes\downarrow B_S.
$$

Read bottom-up:

1. Apply $\downarrow L$ to open the input. The goal becomes $A_S\land B_S;\cdot\vdash\downarrow A_S\otimes\downarrow B_S$.
2. Structural $\land L$ exposes $A_S$ and $B_S$ in $\Gamma$. Unlike a linear tensor, this structural pair is reusable and its components may be weakened where unneeded.
3. Apply $\otimes R$, splitting the empty linear context into two empty contexts while sharing $A_S,B_S$ structurally.
4. In the left branch derive $A_S,B_S\vdash A_S$ by structural identity plus weakening, then apply $\downarrow R$ to get $A_S,B_S;\cdot\vdash\downarrow A_S$.
5. Symmetrically derive $A_S,B_S;\cdot\vdash\downarrow B_S$ in the right branch.

Schematically:

$$
\frac{
 \frac{A_S,B_S\vdash A_S}{A_S,B_S;\cdot\vdash\downarrow A_S}\;\downarrow R
 \qquad
 \frac{A_S,B_S\vdash B_S}{A_S,B_S;\cdot\vdash\downarrow B_S}\;\downarrow R
}{A_S,B_S;\cdot\vdash\downarrow A_S\otimes\downarrow B_S}\;\otimes R,
$$

followed upward by structural $\land L$ and $\downarrow L$.

Boundary case: replacing $\land$ with structural disjunction does not work:

$$
\downarrow(A_S\lor B_S)\nvdash\downarrow A_S\otimes\downarrow B_S.
$$

Opening the package reveals only one unknown alternative. Structural reuse can repeat the same available proof, but it cannot manufacture the missing disjunct. Reusability and information content are separate properties.

## 8. Conceptual synthesis

LNL makes the border between persistent and ephemeral computation explicit and typed. The old exponential is no longer primitive mystery: it is a round trip from linear to structural and back. Separating the trip reveals polarity, gives each crossing a direct operational protocol, and allows full structural formulas to retain their own introduction and elimination rules.

The price is duplicated rules: connectives such as implication need mode-specific variants, and structural propositions may be used in conclusions of either mode. Adjoint logic keeps LNL's independence and shifts while parameterizing the rules by modes, eliminating this duplication.

## 9. Common confusions and failure modes

- **$S$ means “server” and $L$ means “client.”** They are proposition modes: structural and linear. Either side of a communication can provide or use a channel.
- **$\uparrow$ and $\downarrow$ are inverses.** They form an adjoint pair, not generally an isomorphism; round trips create monadic/comonadic structure.
- **$\uparrow A_L$ contains an existing linear channel that clients share.** It offers a repeatable way to spawn fresh linear instances.
- **$\downarrow A_S$ is itself reusable.** Its outer proposition is linear; opening the wrapper once reveals a structural payload.
- **A structural conclusion may temporarily depend on $\Delta$ if the final step removes it.** Such a sequent is never well formed, so the dependency cannot be introduced.
- **The two $\supset L$ rules arbitrarily duplicate syntax.** They correspond to the two possible conclusion judgments; their premise modes are forced.
- **A naive $\uparrow$ reduction consumes the server.** That strands additional structural clients. The provider must persist and spawn a fresh linear process.
- **Two recursive calls imply all of `mapreduce` is synchronized fork/join.** The channel graph permits additional pipeline overlap with the combiner.

## 10. Self-test questions with concise answers

1. **Why are there two judgments?** To keep native structural and linear conclusions while enforcing that structural truth has no linear dependency.
2. **What is the type of the linear exponential in LNL?** $!A_L=\downarrow\uparrow A_L$, again a linear proposition.
3. **Which shift is negative?** $\uparrow$, because its right rule is invertible.
4. **Which shift is positive?** $\downarrow$, because its left rule is invertible.
5. **Why is there no $\mathsf{cut}_{LS}$?** A structural result cannot depend on a linear cut formula.
6. **What proves conservativity?** Cut elimination plus the subformula property for cut-free rules.
7. **Why must `mapreduce` shift $h$ and $f$ upward?** Their number of uses depends on the input tree, so one linear channel for each is insufficient.
8. **What survives an interaction on a structural upshifted channel?** The structural provider; a fresh linear service instance and client continuation are spawned.

## 11. Related concept pages

- [Mixed linear-nonlinear logic](../Concepts/Mixed%20Linear-Nonlinear%20Logic.md)
- [Shifts between logics](../Concepts/Shifts%20Between%20Logics.md)
- [Modes and the dependence preorder](../Concepts/Modes%20and%20the%20Dependence%20Preorder.md)
- [Identity and cut admissibility](../Concepts/Identity%20and%20Cut%20Admissibility.md)
- [Linear message passing and session types](../Concepts/Linear%20Message%20Passing%20and%20Session%20Types.md)
- [Futures and single assignment](../Concepts/Futures-and-Single-Assignment.md)
- [Positive versus negative polarity](../Comparisons/Positive%20vs%20Negative%20Polarity.md)
- [Linear versus structural persistence](../Comparisons/Linear%20vs%20Structural%20Persistence.md)

## 12. Source trail

- **Lecture:** 10, “A Mixed Linear/Nonlinear Logic,” September 28, 2023.
- **Numbered sections:** §1 Introduction; §2 Shifting Between Logics; §3 Rules for Implication; §4 Rules for Shifts; §5 Identity and Cut; §6 Examples; §7 A Programming Example; §8 Dynamics of the Shifts; §9 Example Continued; §10 Summary.
- **Printed pages:** L10.1–L10.10.
- **PDF pages:** 113–122.

## 13. Previous/next navigation

[← Lecture 09 - Validity](Lecture%2009%20-%20Validity.md) · [Lecture 11 - Adjoint Logic →](Lecture%2011%20-%20Adjoint%20Logic.md)

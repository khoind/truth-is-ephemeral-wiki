---
title: "Lecture 15 - Adjoint SAX"
lecture: 15
date: 2023-10-31
pdf_pages: "159-170"
printed_pages: "L15.1-L15.12"
tags:
  - lecture
  - adjoint-sax
  - message-sequences
  - pattern-matching
  - partial-focusing
prerequisites:
  - "Lecture 11 - Adjoint Logic"
  - "Lecture 12 - Focusing"
  - "Lecture 14 - Semi-Axiomatic Sequent Calculus"
---

# Lecture 15 - Adjoint SAX

## 1. Why this lecture exists

Linear SAX gives a clean asynchronous account of session-typed communication, but many programs need reusable functions and shared services. This lecture combines SAX with adjoint shifts between a structural mode and a linear mode. The result supports multicast-like persistence and multiple clients while keeping individual linear data under single-use discipline.

The lecture also attacks the implementation cost of continuation channels. Core SAX allocates a fresh address for nearly every message. **Message sequences** compact several logical messages into one syntax tree, and nested **pattern matching** consumes those sequences. Their typing rules reveal a proof-theoretic structure: message construction is partial focusing, while pattern decomposition is partial inversion. Rather than define a second runtime, the extended language is elaborated type-directedly into core SAX.

These two threads answer a common question: can a protocol have a stable, practical channel representation while its proof theory uses a new continuation channel at each step? Adjoint modes explain which services may persist; message sequences explain how chains of logical steps may be represented compactly and later compiled back into explicit addresses.

## 2. Learning objectives

After this lecture, you should be able to:

1. state the SAX rules for upshift and downshift between structural and linear modes;
2. explain the mode side condition on adjoint cut and why structural assumptions may be shared;
3. type the essential stages of a mixed linear/nonlinear `mapreduce`;
4. explain the negative unit $\bot$ and the meaning of an empty succedent;
5. relate message sequences to partial left/right focus;
6. calculate continuation projection for products, units, and labeled choices;
7. state the four type-preservation obligations for elaborating extended send/receive syntax; and
8. expand a nested message and pattern into core SAX operations.

## 3. Dependency map

$$
\text{adjoint modes}
\longrightarrow \uparrow,\downarrow
\longrightarrow \text{mixed linear/structural SAX}
\longrightarrow \text{reusable services},
$$

and independently,

$$
\text{core SAX continuation channels}
\longrightarrow \text{message sequences}
\longrightarrow \text{partial focusing}
\longrightarrow \text{nested pattern matching / partial inversion}
\longrightarrow \text{type-directed elaboration to core SAX}.
$$

The first line depends on [adjoint logic](<../Concepts/Adjoint Logic.md>); the second depends on [the SAX comparison](<../Comparisons/Sequent-Calculus-SAX-and-Explicit-Resources.md>) and [focusing](<../Concepts/Focusing.md>). Their meeting point is operational: structural services can be invoked many times, while each invocation exposes a fresh linear continuation.

## 4. Section-by-section reconstruction

### 1 Introduction

Purely linear SAX cannot directly express a function used at every internal node of a tree or a server with multiple clients. Adjoint logic supplies modes and shifts so linear and nonlinear propositions coexist. In the two-mode presentation, structural mode $S$ is above linear mode $L$. Structural resources admit weakening and contraction; linear resources do not.

Asynchrony is crucial. A persistent message may be observed by multiple recipients, and a shared service may accept multiple clients. Requiring all of them to synchronize in one atomic rendezvous would need a global notion of simultaneous delivery. SAX instead represents each interaction by messages and continuations.

The second concern is representation. Explicitly fresh continuation addresses are theoretically clean but implementation-heavy. Message sequences allow several message constructors on the same apparent channel, support compact surface programs, and can be implemented as queues. Their types can sometimes bound maximum queue size.

### 2 Adding Adjoint Modalities to SAX

Core SAX has messages $k(x')$, $(y,x')$, and $()$; matching continuations; cut, forwarding, send, receive, and process calls. A message/continuation form is shared by a pair of dual types. To add mixed linear/nonlinear behavior, introduce

$$
A_S ::= \cdots\mid\uparrow A_L,
\qquad
A_L ::= \cdots\mid\downarrow A_S.
$$

The upshift $\uparrow A_L$ is a structural type packaging a linear behavior. It is negative, so its right rule remains an inference and its left rule becomes a SAX axiom:

$$
\frac{\Delta\vdash A_L}{\Delta\vdash\uparrow A_L}\;\uparrow R,
\qquad
\Delta_S,\uparrow A_L\vdash A_L\;\uparrow X.
$$

The annotated rules exchange a continuation channel in a shift message $\langle x'_L\rangle$:

$$
\frac{\Delta\vdash P(x'_L)::(x'_L:A_L)}
     {\Delta\vdash
      \mathsf{recv}\ x_S\ (\langle x'_L\rangle\Rightarrow P(x'_L))
      ::(x_S:\uparrow A_L)}\;\uparrow R,
$$

$$
\Delta_S,x_S:\uparrow A_L\vdash
\mathsf{send}\ x_S\langle x'_L\rangle::(x'_L:A_L)
\;\uparrow X.
$$

Because $x_S$ is structural, a client may request an underlying linear continuation more than once. Each returned $x'_L$ is a separate linear session.

The downshift $\downarrow A_S$ is a linear positive type packaging a structural channel. Its right rule becomes a send axiom and its invertible left rule remains a receive:

$$
\Delta_S,A_S\vdash\downarrow A_S\;\downarrow X,
\qquad
\frac{\Delta,A_S\vdash C_r}{\Delta,\downarrow A_S\vdash C_r}\;\downarrow L.
$$

With processes:

$$
\Delta_S,x'_S:A_S\vdash
\mathsf{send}\ x_L\langle x'_S\rangle::(x_L:\downarrow A_S),
$$

$$
\frac{\Delta,x'_S:A_S\vdash Q(x'_S)::(z_r:C_r)}
     {\Delta,x_L:\downarrow A_S\vdash
      \mathsf{recv}\ x_L(\langle x'_S\rangle\Rightarrow Q(x'_S))
      ::(z_r:C_r)}.
$$

Adjoint cut has the mode condition $\Delta\ge m\ge r$:

$$
\frac{\Delta_S,\Delta\vdash A_m
      \qquad
      \Delta_S,\Delta',A_m\vdash C_r}
     {\Delta_S,\Delta,\Delta'\vdash C_r}.
$$

The shared structural context $\Delta_S$ occurs in both premises; contraction at $S$ justifies the sharing. With $S>L$, there are three meaningful mode combinations for cut: produce and consume structural at $S$; produce structural for a linear conclusion; or produce and consume linear for a linear conclusion. There is no cut that makes a linear proposition available to a structural conclusion, because $L\not\ge S$. Identity has one instance at each mode.

The full dynamics must distinguish ephemeral linear processes/messages from persistent structural ones. The source deliberately refers this development to later work rather than presenting rules, so no unsupported persistence dynamics is invented here.

### 3 An Example: mapreduce

Let

$$
\mathsf{tree}_A=
\oplus\{\mathsf{node}:\mathsf{tree}_A\otimes\mathsf{tree}_A,
         \mathsf{leaf}:A\}.
$$

For linear element type $A$ and result type $B$, `mapreduce` uses two structural services:

$$
f_S:\uparrow(B\otimes B\multimap B),
\qquad
h_S:\uparrow(A\multimap B).
$$

$f_S$ is reused at every internal node, and $h_S$ at every leaf. Their underlying arguments and results remain linear.

At a node, receiving the tree exposes linear subtrees $l$ and $r$. Two recursive calls create result futures/channels $y_1:B$ and $y_2:B$. Form the pair $p:B\otimes B$, request a fresh linear continuation $f_L$ from the structural service $f_S$, then send $p$ and the overall destination $y$ to $f_L$. At a leaf with data $x:A$, request $h_L:A\multimap B$ from $h_S$ and send it $x$ with destination $y$.

The sharing is disciplined: $f_S$ and $h_S$ may occur in every recursive call because they are structural; $l,r,x,y_1,y_2,p,f_L,h_L$, and $y$ are linear and each follows one session.

The computation has more parallelism than fork/join. The reducer can be spawned with channels $y_1$ and $y_2$ before those recursive results exist. It blocks only when it actually receives from them. The pair of destination references does not itself force a join.

### 4 Bottom

The negative unit dual to positive $1$ is bottom $\bot$. Flipping the sequent orientation of unit gives

$$
\frac{\Delta\vdash\cdot}{\Delta\vdash\bot}\;\bot R,
\qquad
\bot\vdash\cdot\;\bot L.
$$

The dot in the succedent means there is no offered channel. Local harmony holds: cutting a $\bot R$ proof against $\bot L$ returns the premise $\Delta\vdash\cdot$, and identity for $\bot$ expands through these two rules.

In SAX, the negative left rule is renamed as the message axiom $\bot X$ but remains premise-free:

$$
\frac{\Delta\vdash P::\cdot}
     {\Delta\vdash\mathsf{recv}\ x\ (()\Rightarrow P)::(x:\bot)}
\;\bot R,
$$

$$
x:\bot\vdash\mathsf{send}\ x\ ()::\cdot
\;\bot X.
$$

A process with judgment $\Delta\vdash P::\cdot$ computes without serving a client. In the intuitionistic orientation used here, a closed process $\cdot\vdash P::\cdot$ is not derivable in the ordinary finite system, so $\bot$ has limited direct application. Unrestricted recursion could obscure this boundary but would not change the logical rules.

### 5 Message Sequences

Instead of requiring every constructor to end immediately in a continuation channel, an extended message may continue with another message:

$$
M::=k(M)\mid(y,M)\mid()\mid x'.
$$

Here $k(M)$ is a choice label followed by a message, $(y,M)$ is a payload channel followed by a message, $()$ ends a unit protocol, and $x'$ explicitly stops the sequence at a core continuation channel. A continuation is a finite list of pattern branches $M\Rightarrow P$, and sends/receives use these extended objects.

This syntax makes compact programs possible. A list append receiver can match `cons(x,L')` directly rather than first receiving `cons(p)` and then receiving pair $(x,L')$ from $p$. A unary halving process can use nested patterns for zero, one successor, and two successors rather than manually naming every intermediate continuation channel.

The statics exposes partial focusing. For positive $A$,

$$
\frac{\Delta\vdash M:\lfloor A\rfloor}
     {\Delta\vdash\mathsf{send}\ x\ M::(x:A)}
\;\mathsf{send}^+.
$$

$\lfloor A\rfloor$ means that $A$ is being constructed by a partially focused message sequence. The positive rules are

$$
\frac{\Delta\vdash M:\lfloor A_k\rfloor}
     {\Delta\vdash k(M):\lfloor\oplus\{\ell:A_\ell\}_{\ell\in L}\rfloor},
$$

$$
\frac{\Delta\vdash M:\lfloor B\rfloor}
     {\Delta,y:A\vdash(y,M):\lfloor A\otimes B\rfloor},
\qquad
\cdot\vdash():\lfloor1\rfloor,
$$

and the stopping rule

$$
x':A\vdash x':\lfloor A\rfloor.
$$

These resemble right focus, but identity may stop at **any** type $A$, not only an atom or polarity boundary. Also, the $y:A$ in the tensor rule is supplied directly rather than recursively focused. The sequence may therefore be as short or long as the programmer wants. This is partial rather than full focusing.

For negative types, message sequences correspond to partial left focus. Let $\delta$ abbreviate a singleton succedent $(z:C)$. Then

$$
\frac{\Delta,\lfloor A\rfloor\vdash M::\delta}
     {\Delta,x:A\vdash\mathsf{send}\ x\ M::\delta}
\;\mathsf{send}_L,
$$

The two information-carrying cases are

$$
\frac{\Delta,\lfloor A_k\rfloor\vdash M::\delta}
     {\Delta,\lfloor\mathbin{\&}\{\ell:A_\ell\}_{\ell\in L}\rfloor
      \vdash k(M)::\delta},
$$

$$
\frac{\Delta,\lfloor B\rfloor\vdash M::\delta}
     {\Delta,y:A,\lfloor A\multimap B\rfloor\vdash(y,M)::\delta},
$$

together with a left identity that stops at any $A$. The displayed floor marker identifies the negative antecedent being partially focused; it is not an object-language type constructor.

### 6 Pattern Matching

Receivers match whole sequences. Their typing uses **projection** $K@p$, which filters and peels a layer of pattern $p$ from a continuation set $K$. This corresponds to partial inversion.

For a positive antecedent consumed by a client,

$$
\frac{\Delta;A\vdash K::\delta}
     {\Delta,x:A\vdash\mathsf{recv}\ x\ K::\delta}
\;\mathsf{recv}_L.
$$

The semicolon separates ordinary antecedents $\Delta$ from the single type currently being inverted. $K$ must be nonempty.

For product:

$$
\frac{\Delta,y:A;B\vdash K@(y,\_)::\delta}
     {\Delta;A\otimes B\vdash K::\delta}
\;\otimes L.
$$

Projection is defined only if every remaining branch begins with a pair. It removes that pair layer and consistently renames the branch-bound payload to the rule's $y$. Importantly, $y:A$ enters $\Delta$, not the semicolon zone. Only the tail $B$ continues to be matched, ensuring sequences rather than branching message trees.

For unit:

$$
\frac{\Delta\vdash K@()::\delta}{\Delta;1\vdash K::\delta}\;1L,
$$

where projection is defined only for exactly one branch $()\Rightarrow P$, and returns $P$. Multiple unit branches would make matching nondeterministic.

For internal choice:

$$
\frac{\Delta;A_\ell\vdash K@\ell(\_)::\delta
      \quad(\forall\ell\in L)}
     {\Delta;\oplus\{\ell:A_\ell\}_{\ell\in L}\vdash K::\delta}
\;\oplus L.
$$

Projection retains matching $\ell$ branches, skips other labels $k\in L$, and is undefined for malformed outer patterns. Every protocol label must project to a nonempty continuation, so pattern matching is exhaustive. Requiring every supplied label to belong to $L$ is stronger than progress alone needs, but preserves the exact logical correspondence.

A single variable pattern stops inversion at any type:

$$
\frac{\Delta,x':A\vdash P(x')::\delta}
     {\Delta;A\vdash(x'\Rightarrow P(x'))::\delta}
\;\mathsf{cont/var}^+.
$$

The negative/right side is symmetric. A provider receives a continuation $K$ for a negative type. Implication projection peels $(y,\_)$ and negative-choice projection peels labels. The rule $\mathsf{cont/var}^-$ likewise stops at any type. This freedom to stop before a polarity boundary is the defining difference from full inversion.

### 7 Dynamics for Message Sequences

Rather than add direct reductions for nested syntax, define a type-directed elaboration into core SAX. The metafunctions

$$
\mathsf{send}^*(x:A)M=P
\qquad\text{and}\qquad
\mathsf{recv}^*(x:A)K=P
$$

allocate intermediate continuation channels and turn nested patterns into nested one-step receives.

The intended preservation obligations are:

1. a positive extended send providing $x:A$ elaborates to a core SAX process providing $x:A$;
2. a negative extended send using $x:A$ elaborates to a core SAX process with the same singleton succedent $\delta$;
3. a left/client extended receive using $x:A$ elaborates with the same typing; and
4. a right/provider extended receive offering $x:A$ elaborates with the same typing.

The source notes that fully formal statements must be generalized to the partial-focus judgments; this is left as an exercise and should not be mistaken for a completed theorem in the lecture.

For a positive sum, elaboration builds the tail first on fresh $x'$ and then sends the outer label:

$$
\mathsf{send}^*(x:\oplus\{\ell:A_\ell\})\ k(M)
=x'\leftarrow\mathsf{send}^*(x':A_k)M;
\mathsf{send}\ x\ k(x').
$$

For positive tensor, it elaborates the tail at $B$ and sends $(y,x')$; unit is already core syntax; ending in $x'$ elaborates to forwarding $x$ to $x'$. Negative choice and implication reverse the order: send the outer request to obtain $x'$, then elaborate the remaining message at the continuation. Their terminal forwarding has the opposite orientation because the original channel is used rather than provided.

Receive elaboration is structurally the same for positive-left and negative-right cases. It receives one core message, projects the continuation set by the observed constructor, and recursively elaborates the tail. A variable-only continuation elaborates by substituting the actual channel $x$ into its process body.

## 5. Formal core

### Modes, contexts, and sequents

- $S$ is structural mode and $L$ linear mode, with $S>L$.
- $A_S$ and $A_L$ are propositions at their respective modes.
- $\Delta_S$ contains structural channels and may be shared, weakened, or contracted.
- $\Delta,\Delta'$ contain mode-compatible resources; linear entries must be used exactly once.
- $A_m$ is the cut formula at mode $m$; $C_r$ is the conclusion at mode $r$.
- $\Delta\ge m\ge r$ is the adjoint dependence condition.
- $\delta$ denotes a singleton offered channel $z:C$, while $\cdot$ denotes no succedent.

### Extended syntax

- $M$ is a message sequence; $k(M)$ and $(y,M)$ add one constructor, $()$ terminates unit, and $x'$ terminates at a continuation channel.
- $K$ is a finite ordered collection of pattern branches or $\cdot$.
- $K@p$ is a partial metafunction. “Undefined” means the pattern shapes are inconsistent; $\cdot$ can be a defined projection result for a missing label, but the typing rules then prevent completion.
- $\lfloor A\rfloor$ is a judgmental partial-focus marker, not a connective in session types.
- $\Delta;A\vdash K::\delta$ is partial left inversion on a singleton ordered inversion type.
- $\Delta\vdash K:A$ is partial right inversion for a negative offered type.

### Projection equations

Representative equations are:

$$
((z,M)\Rightarrow P(z)\mid K)@(y,\_)
=M\Rightarrow P(y)\mid(K@(y,\_)),
$$

$$
(\ell(M)\Rightarrow P\mid K)@\ell(\_)
=M\Rightarrow P\mid(K@\ell(\_)),
$$

$$
(k(M)\Rightarrow P\mid K)@\ell(\_)
=K@\ell(\_)
\quad(k\ne\ell,\ k\in L).
$$

The equations are type-directed filters, not runtime nondeterministic pattern selection.

### Elaboration boundary

$\mathsf{send}^*$ and $\mathsf{recv}^*$ are metalevel compilation functions. Their equations define extended-language behavior by translation to core SAX; they are not source-level recursive processes. Fresh intermediate variables in those equations must be chosen capture-avoidably.

## 6. Operational/computational reading

An upshifted structural service is a reusable handle that dispenses fresh linear sessions. A downshifted linear message transfers access to a structural channel. Persistence applies to the handle or structural service, not to the linear result channel returned by one request.

A message sequence is a compact description of several linked SAX messages. It may be represented as queue content on one apparent channel, but elaboration proves what that intuition means: each nested constructor becomes a core message with a fresh continuation address. A nested receive is compiled into a sequence of blocking receives and projections.

Partial focusing is important operationally. Full focusing would force the longest possible logical message, reducing where programmers may place process boundaries. Partial focusing lets a message stop at any type by naming a continuation channel, so queue chunks can be chosen for implementation convenience without losing typing.

## 7. Worked derivation or trace in original notation and prose

Define

$$
\mathsf{nat}=\oplus\{\mathsf{zero}:1,\mathsf{succ}:\mathsf{nat}\}.
$$

Consider the extended positive message

$$
\mathsf{succ}(\mathsf{zero}(())),
$$

which represents unary one and contains no explicit continuation channel.

Its partial-focus typing is bottom-up:

1. $\cdot\vdash():\lfloor1\rfloor$ by $1R$.
2. $\cdot\vdash\mathsf{zero}(()):\lfloor\mathsf{nat}\rfloor$ by the sum rule for label `zero`.
3. $\cdot\vdash\mathsf{succ}(\mathsf{zero}(())):\lfloor\mathsf{nat}\rfloor$ by the sum rule for `succ`.
4. Therefore $\cdot\vdash\mathsf{send}\ x\ \mathsf{succ}(\mathsf{zero}(()))::(x:\mathsf{nat})$.

Elaboration creates two fresh continuation channels:

$$
\begin{aligned}
\mathsf{send}^*(x:\mathsf{nat})\ \mathsf{succ}(\mathsf{zero}(()))
= {}&x_1\leftarrow
   \mathsf{send}^*(x_1:\mathsf{nat})\ \mathsf{zero}(());\\
 &\mathsf{send}\ x\ \mathsf{succ}(x_1),\\
\mathsf{send}^*(x_1:\mathsf{nat})\ \mathsf{zero}(())
= {}&x_2\leftarrow\mathsf{send}\ x_2\ ();\\
 &\mathsf{send}\ x_1\ \mathsf{zero}(x_2).
\end{aligned}
$$

After cut allocation, the core configuration contains a linked chain

$$
\mathsf{send}\ x\ \mathsf{succ}(a_1),
\quad
\mathsf{send}\ a_1\ \mathsf{zero}(a_2),
\quad
\mathsf{send}\ a_2\ ().
$$

Now use this exhaustive extended continuation:

```text
succ(zero()) => P_one
zero()       => P_zero
succ(succ(y)) => P_many(y)
```

Projection at the outer `succ` drops the `zero` branch and peels one constructor from the other two branches. Projecting the result at `zero` selects `P_one`; projecting at `succ` would bind $y$ and select `P_many(y)`. The elaborated receiver performs exactly these decisions one core receive at a time.

Boundary cases:

- Omitting the outer `zero()` branch makes projection at label `zero` empty, so the typing derivation cannot close; the match is nonexhaustive.
- Adding two branches both equal to `()` violates the unit projection rule; unit matching must have one deterministic branch.
- Writing a pair pattern in one branch and a label pattern in another makes product or choice projection undefined; the patterns disagree about the channel's type.

## 8. Conceptual synthesis

Adjoint SAX separates reuse from consumption at the type level. Structural channels may be shared, but each interaction can expose linear data or a linear continuation. Message sequences then separate logical granularity from representational granularity: the core calculus keeps one constructor per address, while the surface language groups an arbitrary number of constructors.

The bridge is proof theory. Shifts follow polarity and mode adjunction; sequences follow partial focus; patterns follow partial inversion; elaboration reifies every compressed phase as explicit SAX messages and receives. The extended syntax is therefore not an untyped convenience layered over the calculus—it is a typed, conservative interface to the core.

## 9. Common confusions and failure modes

- **“Structural means all data beneath a shift may be duplicated.”** The structural handle may be reused; each linear continuation it returns remains linear.
- **“$\uparrow$ and $\downarrow$ are logical negations.”** They move propositions between modes and have opposite polarities; they do not negate truth.
- **“Any cut may feed a linear value into a structural result.”** The condition $m\ge r$ forbids dependence of a structural conclusion on a linear cut formula.
- **“The lecture defines the full persistence dynamics.”** It does not; it notes that persistent structural messages/services complicate dynamics and refers elsewhere.
- **“$\bot$ is the same as $0$.”** $0$ is positive and has no right rule; $\bot$ is negative and has an empty-succedent right rule.
- **“$\cdot\vdash P::\cdot$ is an ordinary closed server.”** It offers no client channel and is not derivable in the finite intuitionistic system.
- **“$\lfloor A\rfloor$ is a new session type.”** It is a judgmental marker for partial focus.
- **“Partial focus must continue to an atom.”** Identity may stop a sequence at any proposition by supplying a continuation channel.
- **“Projection chooses one of several matching unit branches.”** More than one unit branch is rejected to preserve determinism.
- **“A missing label is a runtime failure only.”** Exhaustiveness is enforced statically because its empty projection cannot complete a typing derivation.
- **“Message sequences have their own unrelated dynamics.”** Their behavior is defined by type-directed elaboration to core SAX.
- **“The four elaboration properties are fully proved here.”** The source states the intended properties and notes that they require generalization to partial-focus judgments.

## 10. Self-test questions with concise answers

1. **What does $x_S:\uparrow A_L$ provide operationally?**  
   A reusable structural handle from which clients can request fresh linear sessions of type $A_L$.

2. **Why may $\Delta_S$ appear in both cut premises?**  
   Structural mode admits contraction, so those assumptions may be shared.

3. **Why are `mapreduce`'s $f_S$ and $h_S$ structural?**  
   They are reused at every internal node and leaf, respectively.

4. **What does an empty succedent mean?**  
   The process offers no channel to a client and computes only for its own effect.

5. **What is the base case of a message sequence besides unit?**  
   An explicit continuation channel $x'$, typed by partial identity.

6. **Why is sequence typing only partially focused?**  
   It may stop at any type instead of being forced to a polarity boundary or atom.

7. **What does $K@(y,\_)$ do?**  
   It requires pair-shaped branches, removes their first component, and consistently binds that component as $y$.

8. **How is label exhaustiveness checked?**  
   The choice rule requires a nonempty, typable projection for every label in the type.

9. **Why is elaboration type-directed?**  
   The type determines whether a constructor is positive or negative and therefore the order and orientation of core sends, receives, and forwarding.

10. **What becomes of a terminal variable pattern $x'\Rightarrow P(x')$?**  
    Elaboration substitutes the actual channel $x$ into $P$.

## 11. Related concept pages

- [Adjoint SAX, message sequences, and pattern matching](<../Concepts/Adjoint SAX, Message Sequences, and Pattern Matching.md>)
- [Adjoint modalities](<../Concepts/Adjoint Modalities.md>)
- [Modes and the dependence preorder](<../Concepts/Modes and the Dependence Preorder.md>)
- [Inversion, chaining, and proof phases](<../Concepts/Inversion, Chaining, and Proof Phases.md>)
- [Partial focusing](<../Concepts/Partial-Focusing.md>)
- [Bottom, the empty succedent, and type-directed elaboration](<../Concepts/Adjoint SAX, Message Sequences, and Pattern Matching.md>)
- [Futures and single assignment](<../Concepts/Futures-and-Single-Assignment.md>)
- [Linear vs structural persistence](<../Comparisons/Linear vs Structural Persistence.md>)
- [Sequent calculus, SAX, and explicit resources](<../Comparisons/Sequent-Calculus-SAX-and-Explicit-Resources.md>)

## 12. Source trail

- Frank Pfenning, *Adjoint SAX*, 15-836 Substructural Logics, Lecture 15, October 31, 2023.
- Numbered sections covered exactly: §1 **Introduction**; §2 **Adding Adjoint Modalities to SAX**; §3 **An Example: mapreduce**; §4 **Bottom**; §5 **Message Sequences**; §6 **Pattern Matching**; §7 **Dynamics for Message Sequences**.
- Printed pages: L15.1-L15.12.
- PDF pages: 159-170.
- This guide retains the source's open proof obligations and omitted persistence dynamics as explicit boundaries. The unary-message trace is original.

## 13. Previous/next navigation

- Previous: [Lecture 14 - Semi-Axiomatic Sequent Calculus](<Lecture 14 - Semi-Axiomatic Sequent Calculus.md>)
- Next: [Lecture 16 - Futures](<Lecture-16-Futures.md>)

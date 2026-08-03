---
title: "Lecture 13 - Quantifiers"
lecture: 13
date: 2023-10-10
pdf_pages: "142-147"
printed_pages: "L13.1-L13.6"
tags:
  - lecture
  - quantifiers
  - first-order-logic
  - eigenvariables
  - substitution
prerequisites:
  - "Ordered sequent calculus"
  - "Cut elimination"
  - "Identity expansion"
---

# Lecture 13 - Quantifiers

## 1. Why this lecture exists

Inference rules routinely contain schematic variables, but a schematic variable in the metalanguage is not yet a quantifier inside the logic. This matters when a rule itself is represented as a proposition. The transitivity rule

$$
\frac{\mathsf{path}(x,y)\qquad\mathsf{path}(y,z)}{\mathsf{path}(x,z)}
$$

becomes reusable logical data only after its parameters are internalized, for example as

$$
\forall x.\forall y.\forall z.
(\mathsf{path}(x,y)\land\mathsf{path}(y,z))\supset\mathsf{path}(x,z).
$$

This lecture adds first-order universal and existential quantification to an ordered sequent calculus. Its central issue is variable hygiene: universal right and existential left must introduce genuinely arbitrary, fresh individuals. An explicit structural context $\Gamma$ records which individual variables are in scope, and an individual-substitution theorem supplies the principal cut reductions. Existentials then explain why “allocate a globally fresh channel” is a logical operation rather than an informal side condition.

## 2. Learning objectives

After this lecture, you should be able to:

1. distinguish metalanguage schemata from object-language quantification;
2. state $\forall R$, $\forall L$, $\exists R$, and $\exists L$ with their freshness and well-formedness conditions;
3. explain why individual variables live in a structural context even when propositions live in an ordered or linear context;
4. apply the individual-substitution principle in a principal cut reduction;
5. explain how $\exists$ internalizes global freshness in process dynamics; and
6. derive the negative polarity of $\forall$ and positive polarity of $\exists$ from rule orientation.

## 3. Dependency map

$$
\text{first-order terms and predicates}
\longrightarrow \text{individual context }\Gamma
\longrightarrow \text{quantifier rules}
\longrightarrow \text{substitution}
\longrightarrow \text{cut reduction}.
$$

The operational line is

$$
\text{fresh-name generation}
\longrightarrow \exists\text{-introduction in a rewrite rule}
\longrightarrow \exists L\text{ chooses a fresh eigenvariable}.
$$

This lecture relies on [ordered inference](<../Concepts/Ordered Inference.md>) for its propositional contexts, [identity and cut admissibility](<../Concepts/Identity and Cut Admissibility.md>) for harmony, and [polarity](<../Comparisons/Positive vs Negative Polarity.md>) for classifying the new connectives.

## 4. Section-by-section reconstruction

### 1 Introduction

Schematic variables in an inference rule are implicitly universally quantified by the person reading the rule. That convention is sufficient while the rule remains in the metalanguage. It fails when the rule must become a proposition that can be assumed, copied according to its mode, and used through logical inference. Explicit quantifiers bridge the two levels.

The lecture stays in predicate calculus rather than dependent type theory. Individuals and propositions remain separate syntactic categories: terms may occur inside propositions, but terms do not contain proofs or propositions. Ordered logic is used as the base because its cut-elimination machinery is already familiar, though the quantifier principles carry over to linear, structural, and adjoint systems.

### 2 Universal Quantification

Predicate calculus abstracts from the domain. The domain might later be graph nodes, natural numbers, trees, or channels, but the logical rules depend only on a judgment saying that a term denotes an individual.

To prove $\forall i.A(i)$, prove $A(i)$ for a fresh, arbitrary $i$. Freshness is expressed by adding $i$ only in the premise's individual context:

$$
\frac{\Gamma,i\,\mathsf{ind};\Omega\vdash A(i)}
     {\Gamma;\Omega\vdash\forall i.A(i)}
\;\forall R.
$$

$\Gamma$ is a structural context of distinct declarations $i_1\,\mathsf{ind},\ldots,i_k\,\mathsf{ind}$. The presupposition is that every free individual variable occurring in $\Omega$ and the succedent is declared in $\Gamma$. Bound variables may be alpha-renamed so the displayed $i$ is fresh.

To use a universal antecedent, instantiate it with any well-formed term:

$$
\frac{\Gamma\vdash t\,\mathsf{ind}
      \qquad
      \Gamma;\Omega_L\,A(t)\,\Omega_R\vdash C}
     {\Gamma;\Omega_L\,(\forall i.A(i))\,\Omega_R\vdash C}
\;\forall L.
$$

Here $\Omega_L$ and $\Omega_R$ are the ordered context on the left and right of the principal formula. The term judgment ensures that every variable in $t$ is declared in $\Gamma$. In the smallest term language, $t$ is just a declared variable; richer theories may add constructors such as $0$ and $\mathsf{succ}(t)$.

The individual context is structural because terms are mentioned, not consumed. A linear proposition can contain the same name several times without using the corresponding individual as a linear resource. This is a separation between syntactic scope and propositional resource use.

The principal $\forall$ cut exposes why freshness matters. A $\forall R$ derivation provides $A(i)$ for a fresh $i$, while $\forall L$ asks for $A(t)$. They match only after substituting $t$ for $i$ throughout the left derivation:

$$
\frac{\Gamma\vdash t\,\mathsf{ind}
      \qquad
      \Gamma,i\,\mathsf{ind};\Omega(i)\vdash A(i)}
     {\Gamma;\Omega(t)\vdash A(t)}
\;\mathsf{subst}.
$$

The resulting cut is on $A(t)$, a proper subformula of $\forall i.A(i)$. The size of $t$ does not invalidate the measure: first-order terms contain no logical connectives or quantifiers, so logical formula size strictly decreases.

The source also checks rule internalization. A universally quantified transitivity proposition can be instantiated with $a$, $b$, and $c$ by three $\forall L$ steps. Its implication left rule turns proofs of $\mathsf{path}(a,b)$ and $\mathsf{path}(b,c)$ into the new assumption $\mathsf{path}(a,c)$ needed downstream. Top-down rule application has thus become bottom-up use of an antecedent.

### 3 Existential Quantification

Existential rules reverse the universal pattern:

$$
\frac{\Gamma\vdash t\,\mathsf{ind}
      \qquad \Gamma;\Omega\vdash A(t)}
     {\Gamma;\Omega\vdash\exists i.A(i)}
\;\exists R,
$$

$$
\frac{\Gamma,i\,\mathsf{ind};\Omega_L\,A(i)\,\Omega_R\vdash C}
     {\Gamma;\Omega_L\,(\exists i.A(i))\,\Omega_R\vdash C}
\;\exists L.
$$

$\exists R$ supplies a witness $t$ already meaningful in $\Gamma$. $\exists L$ opens an unknown witness as a fresh eigenvariable $i$; the client must work parametrically and may not assume which witness was chosen.

In the principal cut, the provider chooses $t$ with $\exists R$, while the client opens the existential with a fresh $i$ using $\exists L$. Substitution replaces $i$ by $t$ in the client derivation, after which a smaller cut on $A(t)$ remains.

Existential quantification also internalizes freshness in multiset-rewriting dynamics. Informally, cut allocation has the step

$$
\mathsf{proc}(x\leftarrow P(x);Q(x))
\longrightarrow
\mathsf{proc}(P(a))\;\mathsf{proc}(Q(a))
\quad(a\text{ globally fresh}).
$$

As a proposition, its essential shape is

$$
\forall P.\forall Q.
\mathsf{proc}(x\leftarrow P(x);Q(x))
\multimap
\exists a.\mathsf{proc}(P(a))\otimes\mathsf{proc}(Q(a)).
$$

When the existential appears on the left of a sequent, $\exists L$ extends the complete channel-name context $\Gamma$ with a new $a$. Because $\Gamma$ already lists every free channel in the rest of the configuration, that eigenvariable is globally fresh, not merely absent from $P$ and $Q$.

### 4 Polarities

Identity expansion gives a quick polarity test. To expand identity for $\forall i.A(i)$, the first outer rule is $\forall R$: introduce a fresh $i$ on the right, then use $\forall L$ on the antecedent with that same declared individual, and finally appeal to identity for $A(i)$. Right-first identity expansion indicates a negative connective.

Moreover, $\forall L$ is not invertible in general: using it requires choosing a term $t$, and a suitable term may not yet be available. Therefore $\forall$ is negative.

Existential quantification is symmetric. $\exists L$ introduces a fresh eigenvariable without choosing a witness, so it is invertible; $\exists R$ must choose a witness. Therefore $\exists$ is positive.

The identity theorem must be stated with $\Gamma$:

$$
\Gamma;A\vdash A,
$$

subject to all free individual variables of $A$ being declared in $\Gamma$. Omitting $\Gamma$ would silently restrict identity to closed propositions.

## 5. Formal core

### Syntax and contexts

- $i,j,a,b,c$ are individual variables.
- $t$ is a first-order term. Its constructors depend on the chosen domain theory.
- $A(i)$ is a proposition with zero or more free occurrences of $i$; $A(t)$ is capture-avoiding substitution of $t$ for those occurrences.
- $\Gamma$ is an exchangeable, weakenable, contractible context of individual declarations.
- $\Omega,\Omega_L,\Omega_R$ are ordered contexts of propositions. Their inhabitants remain subject to the substructural discipline.
- $C$ is a succedent proposition.
- $\Gamma\vdash t\,\mathsf{ind}$ is a well-formedness judgment, not a proof that $t$ has a proposition as a type.

### Eigenvariable conditions

The displayed rules encode freshness by scope:

- in $\forall R$, the eigenvariable occurs in the premise context but not the conclusion;
- in $\exists L$, the eigenvariable occurs in the premise context but not the conclusion.

Alpha-renaming a bound variable is allowed before applying either rule. What is forbidden is letting the eigenvariable depend on an assumption or conclusion outside its scope.

### Substitution theorem

**Individual substitution.** If $\Gamma\vdash t\,\mathsf{ind}$ and
$\Gamma,i\,\mathsf{ind};\Omega(i)\vdash A(i)$, then
$\Gamma;\Omega(t)\vdash A(t)$.

This is an admissible metatheorem proved by induction on the second derivation. It must act capture-avoidably on the whole derivation, including every formula, term, and eigenvariable side condition.

### Principal cut reductions

For $\forall$, substitute the eliminator's term into the $\forall R$ premise and cut on $A(t)$. For $\exists$, substitute the introducer's witness into the $\exists L$ premise and cut on $A(t)$. Both reductions lower formula complexity.

## 6. Operational/computational reading

Read $\forall i.A(i)$ as a provider that works uniformly for an arbitrary individual supplied by its client. Using it chooses an instantiation term. Read $\exists i.A(i)$ as a provider that chooses and hides a witness; using it reveals a fresh local name standing for that witness.

This is a logical reading, not automatically a full programming-language interpretation. In a propositions-as-types setting, several computational interpretations of quantification are possible, especially under substructural constraints. The lecture intentionally remains at the level of logical inference.

For concurrency, $\exists$ has a particularly concrete role: it scopes a freshly allocated address. The structural context of names is the static record that lets “fresh” mean fresh with respect to the whole configuration.

## 7. Worked derivation or trace in original notation and prose

Let the domain contain terms $0$ and $\mathsf{succ}(t)$, and suppose the ordered context contains

$$
\forall i.\mathsf{even}(i)\to\mathsf{odd}(\mathsf{succ}(i))
\qquad\text{and}\qquad
\mathsf{even}(0).
$$

We derive $\mathsf{odd}(\mathsf{succ}(0))$.

1. The term judgment gives $\Gamma\vdash 0\,\mathsf{ind}$; no free variables are needed in $\Gamma$.
2. Apply $\forall L$ with $t=0$. The quantified antecedent becomes
   $\mathsf{even}(0)\to\mathsf{odd}(\mathsf{succ}(0))$.
3. Apply implication left. Its first premise is the identity derivation
   $\mathsf{even}(0)\vdash\mathsf{even}(0)$.
4. Its second premise is the identity derivation
   $\mathsf{odd}(\mathsf{succ}(0))\vdash
   \mathsf{odd}(\mathsf{succ}(0))$.
5. The conclusion is the desired ordered sequent, with the quantified rule and the even fact used in their permitted order.

Now package a witness:

$$
\frac{\Gamma\vdash \mathsf{succ}(0)\,\mathsf{ind}
      \qquad
      \Gamma;\Omega\vdash\mathsf{odd}(\mathsf{succ}(0))}
     {\Gamma;\Omega\vdash\exists j.\mathsf{odd}(j)}
\;\exists R.
$$

Boundary case: from $\Gamma;\Omega\vdash A(n)$ one may not infer
$\Gamma;\Omega\vdash\forall i.A(i)$ when $n$ is already declared in $\Gamma$ or appears in $\Omega$. That would confuse “this particular $n$” with “an arbitrary individual.” For instance, knowing $\mathsf{even}(0)$ does not prove $\forall i.\mathsf{even}(i)$.

## 8. Conceptual synthesis

Quantifier rules are controlled movement between two levels. $\Gamma$ governs names and term formation; $\Omega$ governs propositional resources. Universal right and existential left move from a bound variable to a fresh parameter. Universal left and existential right move from a binder to a chosen term.

Substitution is the bridge that makes these movements harmonious. Without it, the principal cuts stop at the mismatch between $A(i)$ and $A(t)$. With it, quantifier interaction reduces to interaction at the body $A(t)$, exactly as connective harmony demands.

## 9. Common confusions and failure modes

- **“A schematic rule variable is already an object-language $\forall$.”** Schematic generality belongs to the metalanguage; it must be internalized explicitly to be used as a proposition.
- **“Fresh means absent only from $A$.”** An eigenvariable must be fresh for the entire conclusion, including $\Gamma$, all antecedents, and the succedent.
- **“$\Gamma$ should be linear because the surrounding logic is linear.”** Names are mentioned in formulas, not consumed as propositional resources, so the individual context is structural.
- **“Any expression can instantiate $\forall$.”** Only a term satisfying $\Gamma\vdash t\,\mathsf{ind}$ may be used.
- **“Substitution changes only the conclusion formula.”** It acts throughout the derivation and must preserve all scopes and side conditions.
- **“A large witness prevents the cut measure from decreasing.”** Formula size counts logical structure; first-order terms contain no propositions.
- **“$\exists L$ chooses the witness.”** The provider chose it via $\exists R$; $\exists L$ opens it using a fresh parameter.
- **“$\forall$ is positive because it has many instances.”** Polarity is determined by invertibility and rule orientation; $\forall$ is negative.

## 10. Self-test questions with concise answers

1. **What is an eigenvariable?**  
   A fresh parameter introduced in a rule premise to represent an arbitrary bound individual.

2. **Which rules introduce eigenvariables?**  
   $\forall R$ and $\exists L$.

3. **Which rules choose terms?**  
   $\forall L$ and $\exists R$.

4. **Why is $\Gamma$ explicit?**  
   It enforces scope, freshness, and the presupposition that every free individual variable is declared.

5. **What theorem reduces a principal quantifier cut?**  
   Capture-avoiding substitution for individuals.

6. **Why is $\forall$ negative?**  
   Its right rule is invertible, while its left rule requires choosing an instantiation.

7. **Why is $\exists$ positive?**  
   Its left rule is invertible, while its right rule requires choosing a witness.

8. **How does $\exists$ express fresh channel allocation?**  
   Opening it on the left introduces an eigenvariable fresh for the complete channel context.

## 11. Related concept pages

- [Quantifiers in substructural logic](<../Concepts/Quantifiers in Substructural Logic.md>)
- [Eigenvariables and individual substitution](<../Concepts/Quantifiers in Substructural Logic.md>)
- [Ordered inference](<../Concepts/Ordered Inference.md>)
- [Fresh names and existential quantification](<../Concepts/Quantifiers in Substructural Logic.md>)
- [Positive vs negative polarity](<../Comparisons/Positive vs Negative Polarity.md>)
- [Structural inference](<../Concepts/Structural Inference.md>), [linear inference](<../Concepts/Linear Inference.md>), and [ordered inference](<../Concepts/Ordered Inference.md>)
- [Forward proof search and the inverse method](<../Concepts/Forward-Proof-Search-and-Inverse-Method.md>)

## 12. Source trail

- Frank Pfenning, *Quantifiers*, 15-836 Substructural Logics, Lecture 13, October 10, 2023.
- Numbered sections covered exactly: §1 **Introduction**; §2 **Universal Quantification**; §3 **Existential Quantification**; §4 **Polarities**.
- Printed pages: L13.1-L13.6.
- PDF pages: 142-147.
- The examples and prose in this guide are original; the guide follows the source's judgments and metatheoretic claims.

## 13. Previous/next navigation

- Previous: [Lecture 12 - Focusing](<Lecture 12 - Focusing.md>)
- Next: [Lecture 14 - Semi-Axiomatic Sequent Calculus](<Lecture 14 - Semi-Axiomatic Sequent Calculus.md>)

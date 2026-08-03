#!/usr/bin/env python3
from pathlib import Path
from urllib.parse import quote
import re

root=Path(__file__).resolve().parents[1]

def link(p,label=None,base=root):
    rel=p.relative_to(base).as_posix()
    return f'[{label or p.stem}]({quote(rel, safe="/")})'

def title_of(p):
    t=p.read_text(errors='replace')
    m=re.search(r'^title:\s*["\']?(.+?)["\']?\s*$',t,re.M)
    return m.group(1).strip('"\'') if m else p.stem

def lecture_no(p):
    m=re.search(r'Lecture[- ](\d+)',p.name)
    return int(m.group(1)) if m else 999

lectures=sorted((root/'Lectures').glob('*.md'),key=lecture_no)
concepts=sorted((root/'Concepts').glob('*.md'),key=lambda p:title_of(p).lower())
comparisons=sorted((root/'Comparisons').glob('*.md'),key=lambda p:title_of(p).lower())

home='''---
title: Truth Is Ephemeral Wiki
tags: [home, substructural-logic]
---

# Truth Is Ephemeral Wiki

A self-contained, concept-first companion to the 2023 **15-836: Substructural Logics** lecture notes. The principal lecturer is Frank Pfenning; Lecture 23, on linear natural deduction, is by Sophia Roshal.

The wiki explains the formal systems, computational readings, proof theory, and conceptual relationships in original prose. Concept pages are designed to stand on their own: each supplies motivation, notation, formal rules, an original worked example, a boundary case, consequences, mistakes, and a source trail.

## Begin

- [Reading Map](01%20Reading%20Map.md) — choose a route through the material.
- [Notation Guide](02%20Notation%20Guide.md) — decode contexts, sequents, modes, polarity, and process notation.
- [Concept Index](03%20Concept%20Index.md) — standalone explanations.
- [Lecture Index](04%20Lecture%20Index.md) — all 23 lectures.
- [Study Guide](05%20Study%20Guide.md) — active-learning sequence and checkpoints.
- [Source and Citation](06%20Source%20and%20Citation.md) — provenance and rights boundary.
- [Formula and Rule Sheet](07%20Formula%20and%20Rule%20Sheet.md) — compact reference after concepts are understood.
- [Dependency Map](08%20Dependency%20Map.md) — conceptual prerequisites and cross-cutting themes.

## The course arc

1. **Resource-sensitive inference:** structural, linear, and ordered states.
2. **Proof theory:** connectives, identity, cut, proof terms, and polarity.
3. **Logic as concurrent computation:** session types, message passing, safety, and subtyping.
4. **Multiple resource regimes:** validity, exponentials, mixed and adjoint logics.
5. **Canonical proof search:** focusing, quantifiers, SAX, and adjoint SAX.
6. **Futures and representation:** single assignment, messages, and data layout.
7. **Automation and semantics:** inverse method and resource semantics.
8. **Metalogical representation:** LF, linear LF, CLF, and linear natural deduction.
'''
(root/'00 Home.md').write_text(home)

reading='''---
title: Reading Map
tags: [navigation, study]
---

# Reading Map

## Complete route
Read Lectures 1–23 in order. The sequence is cumulative: structural discipline motivates connectives; cut reduction motivates processes; modes and polarity motivate focusing and SAX; the final lectures turn the accumulated machinery into proof search, semantics, and logical frameworks.

## Concept-first route
1. Structural, linear, and ordered inference.
2. Structural rules and resource regimes.
3. Identity, cut, polarity, and focusing.
4. Session types and process execution.
5. Adjoint logic and shifts.
6. SAX, futures, and data layout.
7. Inverse method and resource semantics.
8. Logical frameworks, CLF, and natural deduction.

## Concurrency route
Start with Lectures 1–2, then 5–7, 14–17, and 22. Use the concept pages on CBA diagrams, session types, cut-as-execution, continuation channels, futures, and CLF to connect operational models.

## Proof-search route
Read Lectures 3–4, 9–13, 18–19, then 23. The central chain is identity/cut → polarity → focusing → inverse method → resource semantics → bidirectional natural deduction.

## Type-systems route
Read Lectures 5–8, 10–17, and 23. Focus on session types, preservation/progress, subtyping, modes, focusing, SAX, futures, and bidirectional type checking.

[Home](00%20Home.md) · [Dependency Map](08%20Dependency%20Map.md)
'''
(root/'01 Reading Map.md').write_text(reading)

notation=r'''---
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
'''
(root/'02 Notation Guide.md').write_text(notation)

ci=['---','title: Concept Index','tags: [navigation, concepts]','---','','# Concept Index','',f'{len(concepts)} standalone concept pages and {len(comparisons)} focused comparisons. Each page is written to be understandable without reopening the source PDF.','', '## Concepts','']
for p in concepts: ci.append(f'- {link(p,title_of(p))}')
ci += ['','## Comparisons','']
for p in comparisons: ci.append(f'- {link(p,title_of(p))}')
ci += ['','[Home](00%20Home.md) · [Dependency Map](08%20Dependency%20Map.md)']
(root/'03 Concept Index.md').write_text('\n'.join(ci)+'\n')

li=['---','title: Lecture Index','tags: [navigation, lectures]','---','','# Lecture Index','']
for p in lectures: li.append(f'{lecture_no(p)}. {link(p,title_of(p))}')
li += ['','[Home](00%20Home.md) · [Reading Map](01%20Reading%20Map.md)']
(root/'04 Lecture Index.md').write_text('\n'.join(li)+'\n')

study='''---
title: Study Guide
tags: [study, exercises]
---

# Study Guide

## How to study a formal concept
For each concept, complete five passes:
1. State the motivating problem without notation.
2. Reconstruct the central judgment or rules and name every metavariable.
3. Run the worked example by hand.
4. Modify one assumption and predict what fails.
5. Explain the concept’s boundary against its nearest comparison page.

## Milestones

### I — State discipline
You should be able to classify a state as a set, multiset, or sequence from its structural laws, and explain saturation, quiescence, frames, and adequacy.

### II — Proof theory
Derive representative left/right rules, distinguish admissibility from derivability, and explain why cut elimination is both a normalization theorem and a computational semantics.

### III — Sessions and safety
Read each connective as provider/client behavior. Trace a cut reduction and explain why preservation and progress jointly express session fidelity.

### IV — Modes and focusing
Given structural properties and a mode preorder, determine legal dependencies and shifts. Classify rules by invertibility and trace inversion, choice, and focus phases.

### V — SAX and futures
Translate between sequent rules, continuation-channel processes, message sequences, and single-assignment futures. Explain what data layout changes and what typing preserves.

### VI — Search, semantics, frameworks
Run a small inverse-method saturation, interpret resource annotations, and explain judgments-as-types, hereditary substitution, LLF/CLF, and adequacy.

### VII — Natural deduction
Relate introduction/elimination rules to right/left sequent rules, explain harmony, and use bidirectional typing to separate checking from synthesis.

## Mastery test
You have mastered a page when you can teach its formal core, reproduce an original example, identify a tempting invalid rule, and connect it to two other concepts without consulting the source.

[Home](00%20Home.md) · [Concept Index](03%20Concept%20Index.md)
'''
(root/'05 Study Guide.md').write_text(study)

source='''---
title: Source and Citation
tags: [reference, citation, rights]
---

# Source and Citation

## Supplied source
*Lecture Notes on Truth is Ephemeral*, 15-836: Substructural Logics, Fall 2023. Lectures 1–22 are principally attributed in the notes to Frank Pfenning. Lecture 23, “Linear Natural Deduction,” is attributed to Sophia Roshal.

PDF verification basis: 248 pages; generated with LaTeX/pdfTeX; source-file SHA-256 `66de62c3c2a5cc534dd4fba2d7b249d097c0e8b6bd4ae737c601625245d06302`.

## Citation practice
Each lecture and concept page includes a source trail with lecture, section, printed lecture pages, and/or PDF pages. Cite the original lecture notes for scholarly claims and verify exact theorem/rule wording there.

## Rights boundary
No explicit license or redistribution notice was found in the supplied PDF. Copyright therefore remains reserved by default. This wiki is an independently worded personal study companion. The PDF, extracted text, diagrams, assignments, and long source passages are excluded. Keep the GitHub repository private unless publication rights are established.

## Scope
The wiki aims for conceptual self-sufficiency but does not pretend to replace every derivation, implementation detail, bibliography entry, or classroom discussion in the lectures. Source-dependent uncertainty is labeled rather than silently repaired.

[Home](00%20Home.md)
'''
(root/'06 Source and Citation.md').write_text(source)

rules=r'''---
title: Formula and Rule Sheet
tags: [reference, rules]
---

# Formula and Rule Sheet

This is a memory aid, not a substitute for the linked concept explanations.

## Structural laws

- Exchange: $\Delta_1,A,B,\Delta_2 \equiv \Delta_1,B,A,\Delta_2$.
- Weakening: assumptions may be added without use.
- Contraction: duplicate assumptions may be merged/reused.

Structural contexts admit exchange, weakening, and contraction; linear contexts normally admit exchange only; ordered contexts deny exchange as well.

## Linear rewriting

$$
\Delta=R\uplus[P_1,\ldots,P_m]
\quad\Longrightarrow\quad
\Delta'=R\uplus[Q_1,\ldots,Q_n].
$$

The matched premises are consumed, conclusions are produced, and frame $R$ is preserved.

## Identity and cut

$$A\vdash A$$

$$
\frac{\Delta\vdash A\qquad \Delta',A\vdash C}{\Delta,\Delta'\vdash C}\;\mathsf{cut}
$$

Identity expresses direct use; cut composes evidence/processes. Cut elimination shows composition introduces no new provability and drives computation.

## Representative connective rules

$$
\frac{\Delta\vdash A\qquad\Delta'\vdash B}{\Delta,\Delta'\vdash A\otimes B}\;\otimes R
$$

$$
\frac{\Delta,A,B\vdash C}{\Delta,A\otimes B\vdash C}\;\otimes L
$$

$$
\frac{\Delta,A\vdash B}{\Delta\vdash A\multimap B}\;\multimap R
$$

$$
\frac{\Delta\vdash A\qquad\Delta',B\vdash C}{\Delta,\Delta',A\multimap B\vdash C}\;\multimap L
$$

Additive rules share a context across alternatives; multiplicative rules partition resources across simultaneous obligations.

## Safety

- Preservation: well-typed configurations remain well typed after a step.
- Progress: a well-typed closed configuration is final/observable or can step.

## Focusing
Invertible rules run eagerly during asynchronous inversion. Noninvertible rules require a choice of one focus and remain synchronous until focus is released.

## Quantifier side conditions
Universal-right and existential-left introduce fresh eigenvariables. Freshness prevents dependency on a special witness/name.

## Futures
A future address has single-assignment discipline: one computation writes a value; dependent computations may read when available. Linear/structural modes govern ownership and reuse.

## Bidirectional typing
Checking judgments validate a term against a known type; synthesis judgments infer a type from an eliminative form. Annotations mediate between directions.

[Notation Guide](02%20Notation%20Guide.md) · [Concept Index](03%20Concept%20Index.md)
'''
(root/'07 Formula and Rule Sheet.md').write_text(rules)

dep='''---
title: Dependency Map
tags: [navigation, prerequisites]
---

# Dependency Map

## Main spine

```text
state representations
  → structural laws
  → logical connectives
  → identity and cut
  → proof terms / cut reduction
  → session processes
  → preservation and progress
  → validity and persistence
  → adjoint modes and shifts
  → polarity and focusing
  → SAX and futures
  → data layout
  → inverse method / resource semantics
  → LF / LLF / CLF
  → linear natural deduction
```

## Cross-cutting dependencies

- **Adequacy** begins with inference encodings and returns in logical frameworks.
- **Polarity** organizes cut reduction, sessions, focusing, messages, futures, and data layout.
- **Structural rules** control state representations, exponentials, modes, resource semantics, and framework contexts.
- **Cut** appears as substitution, process composition, communication, and future synchronization.
- **Focusing** reduces proof-search redundancy and later determines canonical message/value forms.
- **Resource semantics** connects proof search with explicit counting of assumption use.
- **Harmony** reconnects introduction/elimination natural deduction with sequent-calculus cut/identity principles.

## Recommended prerequisite checks
Before sessions, understand identity/cut and polarity. Before adjoint logic, understand mixed linear/nonlinear logic. Before SAX, understand focusing and cut-as-process. Before inverse method, understand forward proof search and polarity. Before CLF, understand judgments-as-types and linear contexts.

[Home](00%20Home.md) · [Reading Map](01%20Reading%20Map.md)
'''
(root/'08 Dependency Map.md').write_text(dep)

readme='''# Truth Is Ephemeral Wiki

A concept-first, self-contained Markdown companion to the Fall 2023 **15-836: Substructural Logics** lecture notes.

Start with [`00 Home.md`](00%20Home.md). The repository contains guides for every supplied lecture plus standalone concept and comparison pages. Pages use portable relative Markdown links and TeX math, and work in Obsidian or other capable Markdown readers.

## Design standard
Every central concept explains its motivation, notation, formal core, operational interpretation, original worked example, boundary case, consequences, common mistakes, and source trail. The goal is to minimize the need to reopen the source merely to understand a concept listed here.

## Validation
Run:

```sh
python3 _tools/validate_wiki.py
```

## Rights
No explicit license was found in the supplied PDF. This repository is an independently worded personal study companion and is kept private. It excludes the source PDF, extracted corpus, assignments, diagrams, and long quotations.
'''
(root/'README.md').write_text(readme)
print(f'Navigation built: {len(lectures)} lectures, {len(concepts)} concepts, {len(comparisons)} comparisons')

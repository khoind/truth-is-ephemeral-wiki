#!/usr/bin/env python3
"""Validate the Lecture 16–22 tranche without requiring third-party packages."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]

LECTURES = [
    ROOT / "Lectures" / "Lecture-16-Futures.md",
    ROOT / "Lectures" / "Lecture-17-Data-Layout.md",
    ROOT / "Lectures" / "Lecture-18-The-Inverse-Method.md",
    ROOT / "Lectures" / "Lecture-19-Resource-Semantics.md",
    ROOT / "Lectures" / "Lecture-20-Logical-Frameworks.md",
    ROOT / "Lectures" / "Lecture-21-Substructural-Frameworks.md",
    ROOT / "Lectures" / "Lecture-22-The-Concurrent-Logical-Framework.md",
]

TOPIC_PAGES = [
    ROOT / "Concepts" / "Futures-and-Single-Assignment.md",
    ROOT / "Comparisons" / "Positive-and-Negative-Futures.md",
    ROOT / "Concepts" / "Mixed-Linear-and-Structural-Futures.md",
    ROOT / "Concepts" / "Data-Layout-and-Compound-Values.md",
    ROOT / "Concepts" / "Partial-Focusing.md",
    ROOT / "Concepts" / "Forward-Proof-Search-and-Inverse-Method.md",
    ROOT / "Comparisons" / "Resource-Regimes.md",
    ROOT / "Concepts" / "Resource-Semantics.md",
    ROOT / "Comparisons" / "Sequent-Calculus-SAX-and-Explicit-Resources.md",
    ROOT / "Concepts" / "Validity-and-Untethering.md",
    ROOT / "Concepts" / "Logical-Frameworks-and-Judgments-as-Types.md",
    ROOT / "Concepts" / "Canonical-Forms-and-Hereditary-Substitution.md",
    ROOT / "Concepts" / "Representing-Sequent-Derivations.md",
    ROOT / "Concepts" / "Linear-Logical-Frameworks-and-Metatheory.md",
    ROOT / "Concepts" / "CLF-and-Monadic-Concurrency.md",
    ROOT / "Concepts" / "Generative-Grammars-Trace-Equivalence-and-Adequacy.md",
]

LECTURE_KEYS = {
    "title", "lecture", "date", "pdf_pages", "printed_pages", "tags", "prerequisites"
}
CONCEPT_KEYS = {
    "title", "aliases", "tags", "source_lectures", "prerequisites", "related"
}

LECTURE_SECTIONS = [
    "Why this lecture exists",
    "Learning objectives",
    "Dependency map",
    "Section-by-section reconstruction covering every numbered heading",
    "Formal core",
    "Operational/computational reading",
    "Worked derivation or trace in original notation and prose",
    "Conceptual synthesis",
    "Common confusions and failure modes",
    "Self-test questions with concise answers",
    "Related concept pages",
    "Source trail",
    "Previous/next navigation",
]

CONCEPT_SECTIONS = [
    "One-sentence definition",
    "Why the concept is needed",
    "Intuitive model",
    "Formal core",
    "How to use/read it",
    "Worked example",
    "Non-example or boundary case",
    "Key consequences",
    "Relations to nearby concepts",
    "Common mistakes",
    "What to remember",
    "Source trail",
]

NUMBERED_SOURCE_HEADINGS = {
    16: [
        "1 Introduction",
        "2 Reinterpreting SAX: Positive Types",
        "3 Reinterpreting SAX: Negative Types",
        "4 Mixed Linear/Structural Futures",
    ],
    17: [
        "1 Introduction",
        "2 Data Layout: Compound Values",
        "3 Partial Focusing Revisited",
        "4 Example: Append with Three Types",
    ],
    18: [
        "1 Introduction",
        "2 The Basic Idea",
        "3 The Inverse Method with Focusing",
        "4 Strict, Affine, and Structural Logic",
        "5 $\\top$ and $0$ Revisited",
    ],
    19: [
        "1 Introduction",
        "2 A Sequent Calculus with Explicit Resources",
        "3 Adding Validity",
        "4 Untethering",
    ],
    20: [
        "1 Introduction",
        "2 Judgments as Types",
        "3 The Formal Metalanguage",
        "4 Hereditary Substitution",
    ],
    21: [
        "1 Introduction",
        "2 Representing Sequent Derivations",
        "3 A Linear Logical Framework",
        "4 Metatheoretic Reasoning",
    ],
    22: [
        "1 Introduction",
        "2 Coin Exchange Revisited",
        "3 CLF",
        "4 Representing the Dynamics of Futures",
    ],
}

REQUESTED_TOPICS = [
    "futures",
    "cells",
    "addresses",
    "single assignment",
    "positive",
    "negative",
    "mixed linear",
    "structural futures",
    "data layout",
    "compound values",
    "partial focusing",
    "forward proof search",
    "inverse method",
    "strict",
    "affine",
    "linear",
    "structural",
    "resource semantics",
    "explicit-resource",
    "validity",
    "untethering",
    "logical frameworks",
    "judgments as types",
    "canonical forms",
    "hereditary substitution",
    "representing sequent derivations",
    "linear logical frameworks",
    "metatheoretic reasoning",
    "CLF",
    "monadic concurrency",
    "generative grammars",
    "trace equivalence",
    "adequacy",
]

LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def frontmatter_and_body(path: Path) -> tuple[set[str], str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("missing opening YAML delimiter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("missing closing YAML delimiter")
    yaml_text = text[4:end]
    keys = {
        match.group(1)
        for line in yaml_text.splitlines()
        if (match := re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):(?:\s|$)", line))
    }
    return keys, text[end + 5 :]


def word_count(body: str) -> int:
    without_code = re.sub(r"```.*?```", " ", body, flags=re.S)
    return len(re.findall(r"\b[\w'-]+\b", without_code))


def local_link_target(source: Path, raw: str) -> Path | None:
    target = raw.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    target = unquote(target.split("#", 1)[0])
    if not target or re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", target):
        return None
    return (source.parent / target).resolve()


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    targets = LECTURES + TOPIC_PAGES

    if len(TOPIC_PAGES) not in range(14, 19):
        errors.append(f"expected 14–18 topic pages, found {len(TOPIC_PAGES)}")

    bodies: dict[Path, str] = {}
    for path in targets:
        if not path.is_file():
            errors.append(f"missing file: {path.relative_to(ROOT)}")
            continue
        try:
            keys, body = frontmatter_and_body(path)
        except ValueError as exc:
            errors.append(f"{path.relative_to(ROOT)}: {exc}")
            continue
        bodies[path] = body
        required_keys = LECTURE_KEYS if path in LECTURES else CONCEPT_KEYS
        missing_keys = sorted(required_keys - keys)
        if missing_keys:
            errors.append(f"{path.relative_to(ROOT)}: missing YAML keys {missing_keys}")

        required_sections = LECTURE_SECTIONS if path in LECTURES else CONCEPT_SECTIONS
        for section in required_sections:
            if not re.search(rf"^## (?:\d+\. )?{re.escape(section)}\s*$", body, re.M):
                errors.append(f"{path.relative_to(ROOT)}: missing section '{section}'")

        if path in TOPIC_PAGES and word_count(body) < 600:
            warnings.append(f"{path.relative_to(ROOT)}: only {word_count(body)} prose words")
        if path.parent.name == "Comparisons" and "\n|" not in body:
            errors.append(f"{path.relative_to(ROOT)}: comparison page has no Markdown table")

        local_links = 0
        for raw in LINK_RE.findall(body):
            resolved = local_link_target(path, raw)
            if resolved is None:
                continue
            local_links += 1
            if not resolved.is_file():
                errors.append(
                    f"{path.relative_to(ROOT)}: broken link '{raw}' -> "
                    f"{resolved.relative_to(ROOT) if resolved.is_relative_to(ROOT) else resolved}"
                )
        if local_links < 2:
            errors.append(f"{path.relative_to(ROOT)}: fewer than two local Markdown links")

    for lecture, path in zip(range(16, 23), LECTURES):
        body = bodies.get(path, "")
        for heading in NUMBERED_SOURCE_HEADINGS[lecture]:
            if f"### {heading}" not in body:
                errors.append(f"{path.relative_to(ROOT)}: missing source heading '{heading}'")

    topic_corpus = "\n".join(bodies.get(path, "") for path in TOPIC_PAGES).casefold()
    for topic in REQUESTED_TOPICS:
        if topic.casefold() not in topic_corpus:
            errors.append(f"requested topic absent from standalone-page corpus: {topic}")

    # The tranche links into the surrounding wiki, so also verify every ordinary
    # Markdown link in all non-source content rather than checking only this manifest.
    checked_global_links = 0
    for path in ROOT.rglob("*.md"):
        if "_source" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        for raw in LINK_RE.findall(text):
            resolved = local_link_target(path, raw)
            if resolved is None:
                continue
            checked_global_links += 1
            if not resolved.is_file() and path not in targets:
                errors.append(f"{path.relative_to(ROOT)}: broken global link '{raw}'")

    if any(path.name in {"README.md", "00 Home.md"} for path in ROOT.glob("*.md")):
        errors.append("request forbids creating root README/navigation in this tranche")

    print(f"Validated {len(LECTURES)} lecture guides and {len(TOPIC_PAGES)} topic pages.")
    print(f"Checked {checked_global_links} local Markdown links across the wiki.")
    print(f"Errors: {len(errors)}")
    for item in errors:
        print(f"ERROR: {item}")
    print(f"Warnings: {len(warnings)}")
    for item in warnings:
        print(f"WARNING: {item}")
    return 1 if errors or warnings else 0


if __name__ == "__main__":
    sys.exit(main())

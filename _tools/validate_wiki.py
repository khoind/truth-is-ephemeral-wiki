#!/usr/bin/env python3
from pathlib import Path
from urllib.parse import unquote
import re, sys

root = Path(__file__).resolve().parents[1]
content_dirs = [root / "Lectures", root / "Concepts", root / "Comparisons"]
files = sorted(p for d in content_dirs if d.exists() for p in d.glob("*.md"))
errors, warnings = [], []
required_concept = [
    "One-sentence definition", "Why the concept is needed", "Intuitive model",
    "Formal core", "How to use/read it", "Worked example",
    "Non-example or boundary case", "Key consequences",
    "Relations to nearby concepts", "Common mistakes", "What to remember", "Source trail"
]
required_lecture = [
    "Why this lecture exists", "Learning objectives", "Dependency map",
    "Section-by-section reconstruction", "Formal core",
    "Operational/computational reading", "Worked derivation or trace",
    "Conceptual synthesis", "Common confusions and failure modes",
    "Self-test questions", "Related concept pages", "Source trail"
]
all_md = sorted(p for p in root.rglob("*.md") if "_source" not in p.parts and "dist" not in p.parts)
for p in all_md:
    text = p.read_text(errors="replace")
    if not text.startswith("---\n") and p.name not in {"README.md"}:
        errors.append(f"missing YAML: {p.relative_to(root)}")
    # Portable relative Markdown links only; ignore images and external/anchor/mail links.
    for target in re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", text):
        raw = target.split("#", 1)[0].strip()
        if raw.startswith("<") and raw.endswith(">"):
            raw = raw[1:-1]
        if not raw or re.match(r"^(https?://|mailto:)", raw):
            continue
        q = (p.parent / unquote(raw)).resolve()
        if not q.exists():
            errors.append(f"broken link: {p.relative_to(root)} -> {target}")
    words = len(re.findall(r"\b[\w’'-]+\b", re.sub(r"^---.*?---", "", text, flags=re.S)))
    if p.parent.name in {"Concepts", "Comparisons"}:
        for h in required_concept:
            if not re.search(rf"^##\s+(?:\d+\.\s+)?{re.escape(h)}(?:\s+.*)?$", text, re.M | re.I):
                errors.append(f"missing section `{h}`: {p.relative_to(root)}")
        if words < 650:
            warnings.append(f"short concept ({words} words): {p.relative_to(root)}")
        links = len(re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", text))
        if links < 2:
            errors.append(f"fewer than 2 links: {p.relative_to(root)}")
    elif p.parent.name == "Lectures":
        for h in required_lecture:
            if not re.search(rf"^##\s+(?:\d+\.\s+)?{re.escape(h)}(?:\s+.*)?$", text, re.M | re.I):
                errors.append(f"missing section `{h}`: {p.relative_to(root)}")
        if words < 1800:
            warnings.append(f"short lecture ({words} words): {p.relative_to(root)}")

lecture_nums=[]
for p in (root/"Lectures").glob("*.md"):
    m=re.search(r"Lecture[- ](\d+)",p.name)
    if m: lecture_nums.append(int(m.group(1)))
missing=sorted(set(range(1,24))-set(lecture_nums))
duplicates=sorted(n for n in set(lecture_nums) if lecture_nums.count(n)>1)
if missing: errors.append(f"missing lectures: {missing}")
if duplicates: errors.append(f"duplicate lectures: {duplicates}")

print("SELF-CONTAINED WIKI AUDIT")
print(f"Markdown content files: {len(files)}")
print(f"Lecture guides: {len(list((root/'Lectures').glob('*.md')))}")
print(f"Concept pages: {len(list((root/'Concepts').glob('*.md')))}")
print(f"Comparison pages: {len(list((root/'Comparisons').glob('*.md')))}")
print(f"Links and schemas checked across: {len(all_md)} files")
print(f"Errors: {len(errors)}")
print(f"Warnings: {len(warnings)}")
for x in errors: print("ERROR:",x)
for x in warnings: print("WARNING:",x)
if errors or warnings:
    sys.exit(1)
print("RESULT: PASS")

#!/usr/bin/env python3
from pathlib import Path
import json, re, sys

ROOT = Path(__file__).resolve().parents[1]
REG = json.loads((ROOT / "registry.json").read_text(encoding="utf-8"))
errors = []

skills = REG.get("skills", [])
if len(skills) != 100:
    errors.append(f"registry must contain exactly 100 skills; got {len(skills)}")

ids = [s.get("id") for s in skills]
if ids != list(range(1, 101)):
    errors.append("skill IDs must be exactly 1..100 in order")

slugs = [s.get("slug") for s in skills]
if len(slugs) != len(set(slugs)):
    errors.append("duplicate skill slugs detected")

valid_name = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")

counts = {"production":0, "integration":0, "experimental":0}
for s in skills:
    slug = s["slug"]
    if not valid_name.fullmatch(slug):
        errors.append(f"{slug}: invalid Agent Skills-style name")
    counts[s["status"]] = counts.get(s["status"], 0) + 1

    skill_dir = ROOT / "skills" / slug
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.exists():
        errors.append(f"{slug}: missing SKILL.md")
        continue
    txt = skill_file.read_text(encoding="utf-8")
    if not txt.startswith("---\n"):
        errors.append(f"{slug}: SKILL.md missing YAML frontmatter")
    m = re.search(r"^name:\s*([^\n]+)$", txt, re.M)
    if not m or m.group(1).strip() != slug:
        errors.append(f"{slug}: frontmatter name must match directory")
    m = re.search(r"^description:\s*(.+)$", txt, re.M)
    if not m:
        errors.append(f"{slug}: missing description")
    if len(txt.splitlines()) > 500:
        errors.append(f"{slug}: SKILL.md exceeds 500 lines")
    if not (skill_dir / "references" / "QUALITY.md").exists():
        errors.append(f"{slug}: missing references/QUALITY.md")
    if not (skill_dir / "tests" / "cases.yaml").exists():
        errors.append(f"{slug}: missing tests/cases.yaml")

expected = REG.get("summary", {})
for k in ("production","integration","experimental"):
    if counts.get(k,0) != expected.get(k):
        errors.append(f"summary mismatch for {k}: registry={expected.get(k)} actual={counts.get(k,0)}")

if errors:
    print("Validation FAILED")
    for e in errors:
        print(" -", e)
    sys.exit(1)

print("Validation OK")
print(f" - total: {len(skills)}")
print(f" - production: {counts['production']}")
print(f" - integration: {counts['integration']}")
print(f" - experimental: {counts['experimental']}")

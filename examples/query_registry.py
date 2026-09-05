#!/usr/bin/env python3
import json
from pathlib import Path

registry = json.loads((Path(__file__).parents[1] / "registry.json").read_text())

for skill in registry["skills"]:
    if skill["status"] == "production" and skill["quality_score"] >= 4.5:
        print(f"{skill['id']:02d} {skill['slug']}: {skill['name_zh']}")

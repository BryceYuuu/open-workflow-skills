#!/usr/bin/env bash
set -euo pipefail
python3 scripts/validate_registry.py
python3 -m open_workflow_skills.cli --version
python3 -m open_workflow_skills.cli list --implemented >/dev/null
python3 -m open_workflow_skills.cli test

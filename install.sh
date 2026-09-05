#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if [[ ${1:-} == "list" ]]; then
  python3 -m open_workflow_skills.cli list
  exit 0
fi
if [[ $# -lt 1 ]]; then echo "Usage: ./install.sh list | ./install.sh <skill> [target-dir]"; exit 2; fi
SKILL="$1"
TARGET="${2:-$HOME/.local/share/open-workflow-skills}"
python3 -m open_workflow_skills.cli install "$SKILL" --target "$TARGET"

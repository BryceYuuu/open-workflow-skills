#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Open Workflow Skills installer

Usage:
  ./install.sh list
  ./install.sh <skill> [--agent <agent>] [--global] [--yes]
  ./install.sh doctor

Examples:
  ./install.sh video-bilingual-subtitles
  ./install.sh spreadsheet-merge --agent codex
  ./install.sh image-watermark --agent cursor --global

Notes:
- Uses the community `npx skills` CLI.
- Project-level install is the default.
- `--yes` skips confirmation; avoid it for untrusted third-party skills.
EOF
}

if [[ $# -lt 1 ]]; then
  usage
  exit 1
fi

cmd="$1"
shift || true

case "$cmd" in
  list)
    if ! command -v npx >/dev/null 2>&1; then
      echo "ERROR: npx is required. Install Node.js/npm first." >&2
      exit 1
    fi
    exec npx skills add . --list
    ;;
  doctor)
    exec "$(dirname "$0")/scripts/doctor.sh"
    ;;
  -h|--help|help)
    usage
    exit 0
    ;;
esac

skill="$cmd"
if [[ ! -f "skills/$skill/SKILL.md" ]]; then
  echo "ERROR: Unknown skill: $skill" >&2
  echo "Run: ./install.sh list" >&2
  exit 1
fi

if ! command -v npx >/dev/null 2>&1; then
  echo "ERROR: npx is required. Install Node.js/npm first." >&2
  exit 1
fi

args=(skills add . --skill "$skill")
while [[ $# -gt 0 ]]; do
  case "$1" in
    --agent)
      [[ $# -ge 2 ]] || { echo "ERROR: --agent requires a value" >&2; exit 1; }
      args+=(--agent "$2")
      shift 2
      ;;
    --global|-g)
      args+=(--global)
      shift
      ;;
    --yes|-y)
      args+=(--yes)
      shift
      ;;
    *)
      echo "ERROR: Unknown option: $1" >&2
      usage
      exit 1
      ;;
  esac
done

echo "About to install: $skill"
echo "Source: local repository"
echo "Review first: skills/$skill/SKILL.md"
exec npx "${args[@]}"

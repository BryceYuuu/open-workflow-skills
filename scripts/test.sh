#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."

echo "[1/3] Registry + folder validation"
python3 scripts/validate_registry.py

echo
echo "[2/3] JSON syntax"
python3 -m json.tool registry.json >/dev/null
python3 -m json.tool schemas/registry.schema.json >/dev/null
echo "JSON OK"

echo
echo "[3/3] Optional community CLI discovery"
if command -v npx >/dev/null 2>&1; then
  if npx skills add . --list >/dev/null 2>&1; then
    echo "npx skills discovery OK"
  else
    echo "WARNING: npx skills discovery check failed or CLI behavior changed."
    echo "         Registry validation still passed."
  fi
else
  echo "SKIP: npx not installed"
fi

echo
echo "All required local checks passed."

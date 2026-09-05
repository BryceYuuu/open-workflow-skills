#!/usr/bin/env bash
set -u

echo "Open Workflow Skills — environment doctor"
echo

check() {
  local name="$1"
  local cmd="$2"
  if command -v "$cmd" >/dev/null 2>&1; then
    printf "✓ %-18s %s\n" "$name" "$(command -v "$cmd")"
  else
    printf "· %-18s not found (only required by some skills)\n" "$name"
  fi
}

check "git" git
check "node" node
check "npm" npm
check "npx" npx
check "python3" python3
check "pip3" pip3
check "ffmpeg" ffmpeg
check "ImageMagick" magick
check "docker" docker
check "jq" jq
check "curl" curl
check "gitleaks" gitleaks
check "certbot" certbot

echo
echo "Installing a SKILL.md does not install every runtime dependency."
echo "Open the target skill's SKILL.md and review Core stack + Permissions."

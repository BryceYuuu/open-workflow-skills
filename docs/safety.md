# Safety model / 安全模型

## Default rules

1. Preserve source files unless in-place edits are explicitly requested.
2. Do not install privileged packages silently.
3. Do not store API keys, passwords, tokens, or private keys in SKILL.md or committed files.
4. Do not claim an external action happened unless it can be verified.
5. Approval-gate high-impact writes.
6. Use least privilege.
7. For unfamiliar third-party skills, inspect SKILL.md and scripts before execution.

## High-impact actions

Examples that should normally require explicit approval:

- sending external messages at scale
- signing or dispatching contracts
- production deployment
- deleting data
- modifying firewall/security configuration
- payments
- live financial trading
- privileged server changes

## Third-party skill risk

Skills may contain executable code. Treat installation similarly to adding a software dependency.

Do not make `curl | bash` the only installation path. This repository favors reviewable Git/npx flows.

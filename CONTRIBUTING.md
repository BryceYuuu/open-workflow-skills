# Contributing to Open Workflow Skills

Contributions are welcome, but v2 distinguishes **workflow definitions** from **runnable implementations**. Do not label a workflow runnable unless the repository contains code and a smoke test that CI can execute.

## Contribution types

### 1. Definition-only Skill
Required:
- `SKILL.md`
- bilingual explanation
- truthful dependencies and permissions
- `references/QUALITY.md`
- `tests/cases.yaml`
- registry entry with `implementation_status: definition-only`

### 2. Tested reference implementation
In addition to the above:
- `runtime.json`
- `scripts/run.py` (or another declared entrypoint)
- `tests/smoke.py`
- deterministic validation of at least one valid path
- clear handling of missing optional dependencies
- registry entry with `implementation_status: tested-reference`

## Principles
1. One clear, repeatable capability per Skill.
2. No fake one-click claims.
3. Preserve source data by default.
4. Declare shell/network/account/credential requirements.
5. Approval-gate consequential writes.
6. Never commit real secrets or personal data as fixtures.
7. Prefer deterministic checks over model self-grading.
8. Chinese and English descriptions should both be understandable, not literal machine translations.

## Before opening a PR

```bash
python3 scripts/validate_registry.py
pip install -e '.[all]'
ows test
```

If your implementation requires a heavy or paid external service, provide an offline smoke path where possible and document the live integration separately.

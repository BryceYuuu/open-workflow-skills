# Contributing

Thanks for improving Open Workflow Skills.

## Before adding a skill

A proposed skill should describe a repeatable workflow, not merely a generic prompt.

Ask:

- Does it have a clear trigger?
- Are inputs and outputs explicit?
- Can success be evaluated?
- Are dependencies declared?
- Are permissions visible?
- Are external writes approval-gated where appropriate?
- Is the description truthful about limitations?

## Folder format

```text
skills/<slug>/
├── SKILL.md
├── references/
│   └── QUALITY.md
└── tests/
    └── cases.yaml
```

`<slug>` must use lowercase letters/numbers and single hyphens, and should match the `name` in `SKILL.md`.

## Status labels

Choose one:

- `production`
- `integration`
- `experimental`

Do not upgrade status based on a single demo.

## Pull request checklist

- [ ] English and Chinese descriptions are present.
- [ ] Permissions are declared.
- [ ] Dependencies are declared.
- [ ] Failure behavior is defined.
- [ ] Eval cases are included.
- [ ] No secret or credential is committed.
- [ ] `python3 scripts/validate_registry.py` passes.
- [ ] High-impact actions require explicit authorization.

## Scripts

Scripts should:

- fail loudly with useful error messages
- avoid silent destructive behavior
- support dry-run where practical
- use non-zero exit codes on failure
- validate inputs
- quote shell variables
- document runtime dependencies

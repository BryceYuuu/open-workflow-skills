# Quality Guide — Personalized Mail Merge / 个性化批量邮件

## Current status

- Status: Integration Required / 需要外部集成
- Audit grade: B
- Quality score: 4.0/5
- Automation level: L3-L4

## What “good” means

A successful run must produce the requested artifact **and** evidence that the result was checked.

### Required checks

- Input scope is explicit.
- Output format matches the request.
- Deterministic values are computed by code/tooling where practical.
- Missing data is surfaced instead of invented.
- External actions are verified from the external system when applicable.
- Source files and credentials are not exposed or silently modified.
- Consequential actions are approval-gated.

## Status-specific expectations

The core workflow is real and useful, but quality depends on connected services, authentication, API behavior, current external data, or infrastructure. Tests should mock or sandbox external writes whenever possible.

## Core stack

CSV/Excel / LLM / Gmail or SMTP

## Suggested eval dimensions

1. **Correctness** — factual/structural accuracy.
2. **Completeness** — requested fields or artifacts are present.
3. **Reproducibility** — deterministic steps can be rerun.
4. **Safety** — permissions and destructive actions are controlled.
5. **Usability** — output is directly usable or clearly reviewable.

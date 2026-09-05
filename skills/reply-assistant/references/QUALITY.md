# Quality Guide — Reply Assistant / 智能回复助手

## Current status

- Status: Production Ready / 成熟可落地
- Audit grade: A
- Quality score: 4.5/5
- Automation level: L1-L2

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

This workflow is considered mature enough for repeatable use **when its declared dependencies are present**. Prefer deterministic tooling and automated checks. Human review may still be appropriate for subjective content or high-impact contexts.

## Core stack

LLM

## Suggested eval dimensions

1. **Correctness** — factual/structural accuracy.
2. **Completeness** — requested fields or artifacts are present.
3. **Reproducibility** — deterministic steps can be rerun.
4. **Safety** — permissions and destructive actions are controlled.
5. **Usability** — output is directly usable or clearly reviewable.

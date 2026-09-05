# Quality Guide — Market Technical Analysis / 市场技术指标分析

## Current status

- Status: Verified Workflow / 已验证工作流
- Audit grade: A
- Quality score: 4.0/5
- Automation level: L2-L3

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

This workflow definition has been reviewed as a mature pattern. Runtime implementation status is tracked separately; a verified workflow may still be definition-only.

## Core stack

Market data / Python

## Suggested eval dimensions

1. **Correctness** — factual/structural accuracy.
2. **Completeness** — requested fields or artifacts are present.
3. **Reproducibility** — deterministic steps can be rerun.
4. **Safety** — permissions and destructive actions are controlled.
5. **Usability** — output is directly usable or clearly reviewable.

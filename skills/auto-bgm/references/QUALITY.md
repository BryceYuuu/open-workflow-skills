# Quality Guide — Auto BGM / 视频自动配乐

## Current status

- Status: Experimental / Assisted / 实验性 / 辅助完成
- Audit grade: C
- Quality score: 2.5/5
- Automation level: L3

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

This workflow is technically feasible but has subjective quality, real-time constraints, generative uncertainty, or domain limitations. Present outputs as candidates/assistance and require review before consequential use.

## Core stack

Audio analysis / music source / FFmpeg

## Suggested eval dimensions

1. **Correctness** — factual/structural accuracy.
2. **Completeness** — requested fields or artifacts are present.
3. **Reproducibility** — deterministic steps can be rerun.
4. **Safety** — permissions and destructive actions are controlled.
5. **Usability** — output is directly usable or clearly reviewable.

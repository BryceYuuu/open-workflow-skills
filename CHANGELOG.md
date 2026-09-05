# Changelog

## 2.0.0

Open Workflow Skills v2 separates **workflow maturity** from **implementation status** and adds a real local runtime.

### Added
- `ows` CLI: `list`, `info`, `doctor`, `run`, `test`, `install`.
- 15 runnable, smoke-tested reference implementations.
- Per-skill `runtime.json` manifests for runnable skills.
- Deterministic smoke tests and fixtures generated at test time.
- CI validation for registry integrity, Agent Skills structure, CLI, and runnable references.
- `implementation_status` metadata (`tested-reference` or `definition-only`).

### Changed
- Replaced the ambiguous `Production Ready` label with `Verified Workflow`.
- Registry version bumped to `2.0.0`.
- README now distinguishes installing a Skill definition from satisfying runtime dependencies.
- Core runnable skills use task-specific workflows instead of a generic seven-step template.

### Compatibility
- Agent Skills folder structure remains unchanged.
- `npx skills add ...` remains supported as a community installer for Skill definitions.
- The `ows` CLI is an additional local runtime, not a replacement for Agent-specific installers.

# Architecture / 架构

## Principle

A skill is a reusable workflow definition, not a magical capability bundle.

```text
User intent
  ↓
Skill metadata discovery
  ↓
SKILL.md instructions
  ↓
Preflight: input + dependency + permission checks
  ↓
Deterministic tools / model calls / Apps / APIs
  ↓
Validation
  ↓
Approval gate when needed
  ↓
Output + audit trail
```

## Skill directory

The Agent Skills specification requires at minimum:

```text
skill-name/
└── SKILL.md
```

This repository extends that convention with:

```text
skill-name/
├── SKILL.md
├── references/
│   └── QUALITY.md
└── tests/
    └── cases.yaml
```

Implementations may additionally add:

```text
scripts/
assets/
examples/
```

## Why not put everything in SKILL.md?

Agent Skills supports progressive disclosure. Keep the activation instructions concise and move detailed technical references, long schemas, fixtures, and deterministic code into supporting files.

## Skill vs integration

A skill can describe how to use Gmail, Calendar, Figma, a CRM, a database, or cloud infrastructure. It does not automatically provide those credentials or connections.

External access must be separately authorized.

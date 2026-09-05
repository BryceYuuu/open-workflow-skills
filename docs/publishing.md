# Publishing checklist / 发布清单

Before the first GitHub release:

1. Replace `YOUR_GITHUB_USERNAME` in README and all SKILL.md files.
2. Review repository name and project branding.
3. Run:
   ```bash
   python3 scripts/validate_registry.py
   ./scripts/test.sh
   ```
4. Optionally run the Agent Skills reference validator.
5. Review LICENSE.
6. Review SECURITY.md.
7. Create a signed/tagged release if desired.
8. Do not mark a skill as implemented merely because it has a SKILL.md. If you add runtime scripts, document and test them.
9. Add screenshots/demos only after the corresponding implementation is reproducible.

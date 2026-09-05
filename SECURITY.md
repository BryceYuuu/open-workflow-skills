# Security Policy

## Reporting a vulnerability

Please do not publish exploitable vulnerabilities, leaked credentials, or private infrastructure details in a public issue.

Open a private security advisory in GitHub if the repository has that feature enabled.

## Security boundaries

This repository contains executable workflow instructions and may eventually include scripts. Treat skills as software dependencies.

The project will not intentionally:

- embed secrets in skills
- require blanket administrator/root privileges when narrower permissions work
- enable live trading by default
- bypass authentication or access controls
- auto-approve production deployment, payment, signing, or destructive data operations

## Installing third-party forks

Review the skill source and scripts before execution. Forks are not automatically trusted by this project.

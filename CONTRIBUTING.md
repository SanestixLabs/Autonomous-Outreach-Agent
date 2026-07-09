# Contributing to Autonomous Outreach Agent

Thank you for contributing to the Autonomous Outreach Agent project.

This repository is maintained by Sanestix Labs. To ensure high code quality and maintainability, please follow the contribution guidelines below.

---

## Development Workflow

All development must follow the Git workflow below:

```text
main
│
└── develop
    ├── feature/lead-finder
    ├── feature/research-agent
    ├── feature/qualification-agent
    ├── feature/email-agent
    ├── feature/scheduler-agent
    └── feature/crm-agent
```

### Rules

- Never commit directly to `main`.
- Never commit directly to `develop`.
- Every task should be completed in its own feature branch.
- Submit a Pull Request for review before merging.

---

## Branch Naming Convention

### Feature

```text
feature/lead-finder
feature/email-generator
feature/calendar-integration
```

### Bug Fix

```text
bugfix/fix-email-validation
bugfix/crm-sync
```

### Documentation

```text
docs/update-readme
docs/architecture
```

---

## Getting Started

### Clone Repository

```bash
git clone https://github.com/SanestixLabs/autonomous-outreach-agent.git
cd autonomous-outreach-agent
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Project Structure

```text
autonomous-outreach-agent/
│
├── agents/
│   ├── master_agent/
│   ├── lead_finder/
│   ├── research_agent/
│   ├── qualification_agent/
│   ├── email_agent/
│   ├── scheduler_agent/
│   └── crm_agent/
│
├── tools/
├── prompts/
├── workflows/
├── integrations/
├── database/
├── config/
├── tests/
├── docs/
│
├── requirements.txt
├── README.md
├── CONTRIBUTING.md
└── .env.example
```

---

## Coding Standards

- Follow PEP 8 style guidelines.
- Write modular and reusable code.
- Keep agent responsibilities isolated.
- Add docstrings to public functions and classes.
- Avoid hardcoding configuration values.

---

## Commit Message Convention

```text
feat: add lead qualification agent
fix: resolve calendar sync issue
docs: update architecture diagram
refactor: optimize research workflow
test: add email generation tests
chore: update dependencies
```

---

## Pull Request Checklist

Before opening a Pull Request:

- [ ] Code builds successfully
- [ ] Feature has been tested
- [ ] Documentation updated (if required)
- [ ] No secrets or credentials committed
- [ ] Branch is up to date with `develop`

---

## Testing

Run all tests before submitting a Pull Request.

```bash
pytest
```

For agent-specific testing:

```bash
pytest tests/
```

---

## Security

Never commit:

```text
.env
API Keys
OAuth Tokens
Database Credentials
Service Account Keys
SMTP Passwords
```

Only commit:

```text
.env.example
```

---

## Agent Design Principles

Each agent should have a single responsibility.

Examples:

- Lead Finder Agent → Finds potential leads
- Research Agent → Collects company information
- Qualification Agent → Scores leads
- Email Agent → Generates personalized emails
- Scheduler Agent → Handles meeting booking
- CRM Agent → Updates CRM records

The Master Agent coordinates all sub-agents and manages workflow execution.

---

## Code Review Policy

Every Pull Request must be reviewed before merging.

Review focuses on:

- Code quality
- Agent modularity
- Performance
- Prompt design
- Security
- Documentation

---

## Communication

If you encounter blockers:

1. Comment on the assigned GitHub Issue.
2. Describe the problem clearly.
3. Attach relevant logs or screenshots.
4. Request assistance before the deadline if needed.

---

## Ownership

This repository is the intellectual property of **Sanestix Labs**.

All contributions made to this repository become part of the company's codebase and may be modified, distributed, or used by Sanestix Labs in accordance with company policies.

---

Thank you for contributing to the Autonomous Outreach Agent.

Together, we're building intelligent systems that automate modern sales workflows.

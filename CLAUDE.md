# Claude Code Project Guidelines

## Project Overview
`bioinformatics-agent-skills` is an open-source library of scientific agent skills for computational biology, multi-omics, and drug discovery.

## Development & Validation Commands
- Validate skill metadata: `python scan_skills.py`
- Run test suite: `pytest`
- Format code: `black scan_skills.py tests/`

## Skill Conventions
- Every skill lives under `skills/<skill-name>/SKILL.md`.
- All `SKILL.md` files must pass schema validation via `scan_skills.py`.
- Include input/output contracts and code examples in every skill.

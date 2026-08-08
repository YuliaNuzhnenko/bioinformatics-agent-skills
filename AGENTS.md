# Agent Integration & Specification Guide 🤖

This document provides technical guidance for integrating **Bioinformatics & Scientific AI Agent Skills** with autonomous coding agents (Cursor, Claude Code, Google Antigravity, OpenAI Codex, Gemini CLI, LangChain).

---

## 📌 Supported Agent Host Architectures

| Agent Host | Recommended Skill Directory | Configuration Hook |
| :--- | :--- | :--- |
| **Cursor** | `.cursor/skills/` or `.cursorrules` | Automatic discovery via `.cursorrules` |
| **Claude Code CLI** | `~/.agents/skills/` | `claude --prompt` or global config |
| **Google Antigravity** | `.agents/skills/` | Agent Tools registry |
| **LangChain / AutoGPT** | `skills/` | Custom Tool Loader (`scan_skills.py`) |

---

## 🧪 Skill Frontmatter Specification

Every `SKILL.md` file MUST conform to the YAML frontmatter schema:

```yaml
---
name: skill-name-slug
description: Clear, 1-line description of the skill capability.
version: "1.0.0"
metadata:
  author: Yulia Nuzhnenko
  domain: Scientific Domain Name
  frameworks: [Framework1, Framework2]
---
```

---

## 🔒 Security & Sandboxing

Skills execute code within the host agent's environment. Ensure network permissions and local file access are appropriately scoped before running tasks against production datasets.

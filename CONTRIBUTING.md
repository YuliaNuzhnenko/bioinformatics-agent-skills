# Contributing to Bioinformatics Agent Skills 🧬

Thank you for your interest in contributing to `bioinformatics-agent-skills`!

---

## 🚀 How to Add a New Skill

1. **Fork the Repository**: Create a new branch `feat/add-my-skill`.
2. **Create Skill Directory**: Create `skills/<your-skill-name>/SKILL.md`.
3. **Follow the Frontmatter Schema**:
   ```yaml
   ---
   name: your-skill-name
   description: Brief description of the skill.
   version: "1.0.0"
   metadata:
     author: Your Name
     domain: Domain Name
     frameworks: [Tool1, Tool2]
   ---
   ```
4. **Validate Your Skill**:
   Run the local validator script:
   ```bash
   python scan_skills.py
   pytest
   ```
5. **Submit a Pull Request**: Describe the scientific utility and test coverage of your skill.

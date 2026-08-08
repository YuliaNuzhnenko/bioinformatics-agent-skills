import os
import yaml
import pytest

def test_skills_frontmatter_schema():
    skills_dir = "skills"
    assert os.path.exists(skills_dir), "skills directory must exist"
    
    skill_count = 0
    for root, dirs, files in os.walk(skills_dir):
        for file in files:
            if file == "SKILL.md":
                filepath = os.path.join(root, file)
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                
                assert content.startswith("---"), f"{filepath} must start with '---'"
                parts = content.split("---", 2)
                assert len(parts) >= 3, f"{filepath} must have valid YAML frontmatter"
                
                data = yaml.safe_load(parts[1])
                assert "name" in data, f"{filepath} missing 'name'"
                assert "description" in data, f"{filepath} missing 'description'"
                assert "version" in data, f"{filepath} missing 'version'"
                skill_count += 1
                
    assert skill_count >= 12, "Must contain at least 12 valid skills"

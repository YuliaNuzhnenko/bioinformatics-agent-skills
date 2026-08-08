#!/usr/bin/env python3
"""
Bioinformatics Agent Skills Validator & Indexer CLI
Author: Yulia Nuzhnenko
"""

import os
import sys
import yaml

def scan_skills(skills_dir="skills"):
    if not os.path.exists(skills_dir):
        print(f"Error: {skills_dir} directory not found.")
        sys.exit(1)
        
    valid_count = 0
    errors = []
    
    print("==================================================")
    print(" Bioinformatics Agent Skills Validator")
    print("==================================================\n")
    
    for root, dirs, files in os.walk(skills_dir):
        for file in files:
            if file == "SKILL.md":
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, "r", encoding="utf-8") as f:
                        content = f.read()
                    
                    if not content.startswith("---"):
                        errors.append(f"{filepath}: Missing YAML frontmatter marker '---'")
                        continue
                        
                    parts = content.split("---", 2)
                    if len(parts) < 3:
                        errors.append(f"{filepath}: Invalid frontmatter structure")
                        continue
                        
                    frontmatter = yaml.safe_load(parts[1])
                    name = frontmatter.get("name")
                    desc = frontmatter.get("description")
                    version = frontmatter.get("version")
                    
                    if not name or not desc:
                        errors.append(f"{filepath}: Missing 'name' or 'description' in frontmatter")
                        continue
                        
                    print(f"  [VALID] {name:<30} (v{version}) - {root}")
                    valid_count += 1
                    
                except Exception as e:
                    errors.append(f"{filepath}: Exception parsing YAML - {e}")
                    
    print(f"\nTotal Valid Skills Processed: {valid_count}")
    if errors:
        print(f"Encountered {len(errors)} Errors:")
        for err in errors:
            print(f"  [ERROR] {err}")
        sys.exit(1)
    else:
        print(" All skills passed schema validation successfully!")

def main():
    scan_skills()

if __name__ == "__main__":
    main()

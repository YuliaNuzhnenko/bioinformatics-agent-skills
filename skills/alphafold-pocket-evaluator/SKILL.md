---
name: alphafold-pocket-evaluator
description: Parses AlphaFold2 PDB files, computes per-residue pLDDT confidence scores, and evaluates Solvent Accessible Surface Area (SASA) of active site pockets.
version: "1.0.0"
metadata:
  author: Yulia Nuzhnenko
  domain: Structural Biology & Docking
  frameworks: [Biopython, Py3Dmol, FreeSASA, SciPy]
---

# Agent Skill: AlphaFold2 3D Binding Pocket & SASA Evaluator Skill

[![Domain](https://img.shields.io/badge/Domain-Structural%20Biology%20&%20Docking-00f0ff?style=flat-square)](#)
[![Version](https://img.shields.io/badge/Version-1.0.0-green?style=flat-square)](#)

## 📌 Description
Parses AlphaFold2 PDB files, computes per-residue pLDDT confidence scores, and evaluates Solvent Accessible Surface Area (SASA) of active site pockets.

---

## 🤖 Agent Execution Protocol

When an AI Agent is tasked with `alphafold-pocket-evaluator`:
1. **Input Validation**: Verify that the required input files or coordinates are supplied.
2. **Environment Check**: Ensure dependencies (`Biopython, Py3Dmol, FreeSASA, SciPy`) are installed.
3. **Execution**: Run the protocol pipeline snippet below.
4. **Output Generation**: Produce actionable Markdown/JSON summaries with publication figures.

---

## 💻 Protocol Code Snippet

```python
def evaluate_pocket(pdb_file, pocket_residues):
    plddt_list = []
    with open(pdb_file, 'r') as f:
        for line in f:
            if line.startswith("ATOM") and line[12:16].strip() == "CA":
                res_id = int(line[22:26].strip())
                if res_id in pocket_residues:
                    plddt_list.append(float(line[60:66].strip()))
    return sum(plddt_list) / len(plddt_list) if plddt_list else 0.0

```

---

## 📥 Input & Output Specifications

### Input Contract
* **Target Files**: Valid input data matching domain formats.
* **Parameters**: Quality thresholds and cutoffs.

### Output Contract
* **Results Table**: Structured summary dataframe or matrix.
* **Visualization**: Rendered SVG/PNG figures.

---

## 📄 License
Distributed under the MIT License. See `LICENSE` for details.

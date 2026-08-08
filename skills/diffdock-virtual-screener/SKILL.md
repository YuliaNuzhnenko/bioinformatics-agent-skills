---
name: diffdock-virtual-screener
description: Runs DiffDock generative diffusion models for blind protein-ligand docking against AlphaFold structures and ranks candidates by confidence scores.
version: "1.0.0"
metadata:
  author: Yulia Nuzhnenko
  domain: AI Drug Discovery
  frameworks: [DiffDock, PyTorch, RDKit, OpenBabel]
---

# Agent Skill: DiffDock AI Molecular Docking & Screening Skill

[![Domain](https://img.shields.io/badge/Domain-AI%20Drug%20Discovery-00f0ff?style=flat-square)](#)
[![Version](https://img.shields.io/badge/Version-1.0.0-green?style=flat-square)](#)

## 📌 Description
Runs DiffDock generative diffusion models for blind protein-ligand docking against AlphaFold structures and ranks candidates by confidence scores.

---

## 🤖 Agent Execution Protocol

When an AI Agent is tasked with `diffdock-virtual-screener`:
1. **Input Validation**: Verify that the required input files or coordinates are supplied.
2. **Environment Check**: Ensure dependencies (`DiffDock, PyTorch, RDKit, OpenBabel`) are installed.
3. **Execution**: Run the protocol pipeline snippet below.
4. **Output Generation**: Produce actionable Markdown/JSON summaries with publication figures.

---

## 💻 Protocol Code Snippet

```python
# DiffDock Screening Protocol
python -m inference --protein_path protein.pdb --ligand_description ligand.sdf --out_dir docking_results/

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

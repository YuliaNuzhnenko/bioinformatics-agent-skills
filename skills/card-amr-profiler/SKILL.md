---
name: card-amr-profiler
description: Scans bacterial genome assemblies against CARD (Comprehensive Antibiotic Resistance Database) and ResFinder to map drug-class resistance heatmaps.
version: "1.0.0"
metadata:
  author: Yulia Nuzhnenko
  domain: Microbiology & AMR
  frameworks: [RGI (Resistance Gene Identifier), ResFinder, Seaborn]
---

# Agent Skill: CARD & ResFinder Antimicrobial Resistance Skill

[![Domain](https://img.shields.io/badge/Domain-Microbiology%20&%20AMR-00f0ff?style=flat-square)](#)
[![Version](https://img.shields.io/badge/Version-1.0.0-green?style=flat-square)](#)

## 📌 Description
Scans bacterial genome assemblies against CARD (Comprehensive Antibiotic Resistance Database) and ResFinder to map drug-class resistance heatmaps.

---

## 🤖 Agent Execution Protocol

When an AI Agent is tasked with `card-amr-profiler`:
1. **Input Validation**: Verify that the required input files or coordinates are supplied.
2. **Environment Check**: Ensure dependencies (`RGI (Resistance Gene Identifier), ResFinder, Seaborn`) are installed.
3. **Execution**: Run the protocol pipeline snippet below.
4. **Output Generation**: Produce actionable Markdown/JSON summaries with publication figures.

---

## 💻 Protocol Code Snippet

```python
rgi main --input_sequence genome.fasta --output_file amr_results --input_type contig --local

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

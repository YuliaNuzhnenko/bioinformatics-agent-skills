---
name: qiime2-16s-microbiome
description: DADA2 amplicon sequence variant (ASV) dereplication, Alpha/Beta diversity index calculation, SILVA taxonomy classification, and 3D PCoA projections.
version: "1.0.0"
metadata:
  author: Yulia Nuzhnenko
  domain: Metagenomics
  frameworks: [QIIME2, DADA2, scikit-bio, phyloseq]
---

# Agent Skill: QIIME2 16S Microbiome & Dysbiosis Skill

[![Domain](https://img.shields.io/badge/Domain-Metagenomics-00f0ff?style=flat-square)](#)
[![Version](https://img.shields.io/badge/Version-1.0.0-green?style=flat-square)](#)

## 📌 Description
DADA2 amplicon sequence variant (ASV) dereplication, Alpha/Beta diversity index calculation, SILVA taxonomy classification, and 3D PCoA projections.

---

## 🤖 Agent Execution Protocol

When an AI Agent is tasked with `qiime2-16s-microbiome`:
1. **Input Validation**: Verify that the required input files or coordinates are supplied.
2. **Environment Check**: Ensure dependencies (`QIIME2, DADA2, scikit-bio, phyloseq`) are installed.
3. **Execution**: Run the protocol pipeline snippet below.
4. **Output Generation**: Produce actionable Markdown/JSON summaries with publication figures.

---

## 💻 Protocol Code Snippet

```python
# QIIME2 Diversity Protocol
qiime diversity core-metrics-phylogenetic --i-phylogeny tree.qza --i-table table.qza --p-sampling-depth 10000 --output-dir core-metrics-results

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

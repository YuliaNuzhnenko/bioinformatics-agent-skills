---
name: tcga-cibersort-deconv
description: Downloads TCGA RNA-Seq datasets via TCGAbiolinks, normalizes log2(TPM+1) counts, and calculates tumor-infiltrating immune cell fractions (CIBERSORT).
version: "1.0.0"
metadata:
  author: Yulia Nuzhnenko
  domain: Cancer Genomics
  frameworks: [TCGAbiolinks, limma, CIBERSORT, ggplot2]
---

# Agent Skill: TCGA Immune Microenvironment Deconvolution Skill

[![Domain](https://img.shields.io/badge/Domain-Cancer%20Genomics-00f0ff?style=flat-square)](#)
[![Version](https://img.shields.io/badge/Version-1.0.0-green?style=flat-square)](#)

## 📌 Description
Downloads TCGA RNA-Seq datasets via TCGAbiolinks, normalizes log2(TPM+1) counts, and calculates tumor-infiltrating immune cell fractions (CIBERSORT).

---

## 🤖 Agent Execution Protocol

When an AI Agent is tasked with `tcga-cibersort-deconv`:
1. **Input Validation**: Verify that the required input files or coordinates are supplied.
2. **Environment Check**: Ensure dependencies (`TCGAbiolinks, limma, CIBERSORT, ggplot2`) are installed.
3. **Execution**: Run the protocol pipeline snippet below.
4. **Output Generation**: Produce actionable Markdown/JSON summaries with publication figures.

---

## 💻 Protocol Code Snippet

```python
library(TCGAbiolinks)
query <- GDCquery(project="TCGA-LUAD", data.category="Transcriptome Profiling", data.type="Gene Expression Quantification")

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

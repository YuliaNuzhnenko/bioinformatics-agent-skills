---
name: gatk4-somatic-variant-caller
description: Executes GATK4 Mutect2 tumor-normal paired variant calling, applies LearnReadOrientationModel, and runs FilterMutectCalls for somatic SNV filtering.
version: "1.0.0"
metadata:
  author: Yulia Nuzhnenko
  domain: Somatic Genomics
  frameworks: [GATK4, SAMtools, Picard, BCFtools]
---

# Agent Skill: GATK4 Mutect2 Somatic Variant Calling Skill

[![Domain](https://img.shields.io/badge/Domain-Somatic%20Genomics-00f0ff?style=flat-square)](#)
[![Version](https://img.shields.io/badge/Version-1.0.0-green?style=flat-square)](#)

## 📌 Description
Executes GATK4 Mutect2 tumor-normal paired variant calling, applies LearnReadOrientationModel, and runs FilterMutectCalls for somatic SNV filtering.

---

## 🤖 Agent Execution Protocol

When an AI Agent is tasked with `gatk4-somatic-variant-caller`:
1. **Input Validation**: Verify that the required input files or coordinates are supplied.
2. **Environment Check**: Ensure dependencies (`GATK4, SAMtools, Picard, BCFtools`) are installed.
3. **Execution**: Run the protocol pipeline snippet below.
4. **Output Generation**: Produce actionable Markdown/JSON summaries with publication figures.

---

## 💻 Protocol Code Snippet

```python
# GATK Mutect2 Shell Protocol
gatk Mutect2 -R reference.fasta -I tumor.bam -I normal.bam -O raw_somatic.vcf.gz

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

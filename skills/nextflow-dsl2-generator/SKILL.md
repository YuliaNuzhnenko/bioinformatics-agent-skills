---
name: nextflow-dsl2-generator
description: Generates production Nextflow DSL2 process modules, handles tuple channel mapping, pins Docker containers, and configures AWS Batch / SLURM profiles.
version: "1.0.0"
metadata:
  author: Yulia Nuzhnenko
  domain: Cloud HPC & Workflows
  frameworks: [Nextflow DSL2, Docker, AWS Batch, SLURM]
---

# Agent Skill: Nextflow DSL2 Cloud Pipeline Generator Skill

[![Domain](https://img.shields.io/badge/Domain-Cloud%20HPC%20&%20Workflows-00f0ff?style=flat-square)](#)
[![Version](https://img.shields.io/badge/Version-1.0.0-green?style=flat-square)](#)

## 📌 Description
Generates production Nextflow DSL2 process modules, handles tuple channel mapping, pins Docker containers, and configures AWS Batch / SLURM profiles.

---

## 🤖 Agent Execution Protocol

When an AI Agent is tasked with `nextflow-dsl2-generator`:
1. **Input Validation**: Verify that the required input files or coordinates are supplied.
2. **Environment Check**: Ensure dependencies (`Nextflow DSL2, Docker, AWS Batch, SLURM`) are installed.
3. **Execution**: Run the protocol pipeline snippet below.
4. **Output Generation**: Produce actionable Markdown/JSON summaries with publication figures.

---

## 💻 Protocol Code Snippet

```python
// Nextflow DSL2 Agent Template
process FASTQC {
    container 'biocontainers/fastqc:v0.11.9_cv8'
    input: tuple val(id), path(reads)
    output: path "*.html", emit: html
    script: "fastqc ${reads}"
}

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

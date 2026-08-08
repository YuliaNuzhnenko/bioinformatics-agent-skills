---
name: ensembl-vep-variant-annotator
description: Parses multi-sample VCF files, queries Ensembl VEP REST API, filters ClinVar pathogenicity ratings, and maps driver mutations to FDA targeted drugs.
version: "1.0.0"
metadata:
  author: Yulia Nuzhnenko
  domain: Clinical Genomics
  frameworks: [PyVCF, Ensembl VEP API, ClinVar, Open Targets]
---

# Agent Skill: Clinical VCF Variant Prioritization & VEP Skill

[![Domain](https://img.shields.io/badge/Domain-Clinical%20Genomics-00f0ff?style=flat-square)](#)
[![Version](https://img.shields.io/badge/Version-1.0.0-green?style=flat-square)](#)

## 📌 Description
Parses multi-sample VCF files, queries Ensembl VEP REST API, filters ClinVar pathogenicity ratings, and maps driver mutations to FDA targeted drugs.

---

## 🤖 Agent Execution Protocol

When an AI Agent is tasked with `ensembl-vep-variant-annotator`:
1. **Input Validation**: Verify that the required input files or coordinates are supplied.
2. **Environment Check**: Ensure dependencies (`PyVCF, Ensembl VEP API, ClinVar, Open Targets`) are installed.
3. **Execution**: Run the protocol pipeline snippet below.
4. **Output Generation**: Produce actionable Markdown/JSON summaries with publication figures.

---

## 💻 Protocol Code Snippet

```python
import requests

def query_vep_variant(chrom, pos, ref, alt):
    url = f"https://rest.ensembl.org/vep/human/region/{chrom}:{pos}-{pos}:1/{alt}?content-type=application/json"
    r = requests.get(url)
    return r.json() if r.status_code == 200 else {}

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

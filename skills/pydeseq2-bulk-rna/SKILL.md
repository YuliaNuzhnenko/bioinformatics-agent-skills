---
name: pydeseq2-bulk-rna
description: Automated negative binomial differential gene expression analysis, log2 fold-change calculation, p-value adjustment (FDR), and Volcano plot generation.
version: "1.0.0"
metadata:
  author: Yulia Nuzhnenko
  domain: Transcriptomics
  frameworks: [PyDESeq2, DESeq2, Pandas, Plotly]
---

# Agent Skill: PyDESeq2 Bulk RNA-Seq Differential Expression Skill

[![Domain](https://img.shields.io/badge/Domain-Transcriptomics-00f0ff?style=flat-square)](#)
[![Version](https://img.shields.io/badge/Version-1.0.0-green?style=flat-square)](#)

## 📌 Description
Automated negative binomial differential gene expression analysis, log2 fold-change calculation, p-value adjustment (FDR), and Volcano plot generation.

---

## 🤖 Agent Execution Protocol

When an AI Agent is tasked with `pydeseq2-bulk-rna`:
1. **Input Validation**: Verify that the required input files or coordinates are supplied.
2. **Environment Check**: Ensure dependencies (`PyDESeq2, DESeq2, Pandas, Plotly`) are installed.
3. **Execution**: Run the protocol pipeline snippet below.
4. **Output Generation**: Produce actionable Markdown/JSON summaries with publication figures.

---

## 💻 Protocol Code Snippet

```python
import pandas as pd
from pydeseq2.dds import DeseqDataSet
from pydeseq2.ds import DeseqStats

def run_dge(counts_df, metadata_df, design_factors="condition"):
    # Real PyDESeq2 Differential Expression Pipeline
    dds = DeseqDataSet(
        counts=counts_df,
        metadata=metadata_df,
        design_factors=design_factors
    )
    dds.deseq2()
    
    stat_res = DeseqStats(dds, contrast=["condition", "treated", "control"])
    stat_res.summary()
    return stat_res.results_df
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

---
name: scanpy-sc-analyzer
description: Autonomous single-cell RNA-seq quality control filtering, Harmony batch-effect correction, Leiden clustering, UMAP visualization, and marker gene annotation.
version: "1.0.0"
metadata:
  author: Yulia Nuzhnenko
  domain: Single-Cell Genomics
  frameworks: [Scanpy, Harmony, AnnData, Plotly]
---

# Agent Skill: Single-Cell RNA-Seq & Harmony Integration Skill

[![Domain](https://img.shields.io/badge/Domain-Single-Cell%20Genomics-00f0ff?style=flat-square)](#)
[![Version](https://img.shields.io/badge/Version-1.0.0-green?style=flat-square)](#)

## 📌 Description
Autonomous single-cell RNA-seq quality control filtering, Harmony batch-effect correction, Leiden clustering, UMAP visualization, and marker gene annotation.

---

## 🤖 Agent Execution Protocol

When an AI Agent is tasked with `scanpy-sc-analyzer`:
1. **Input Validation**: Verify that the required input files or coordinates are supplied.
2. **Environment Check**: Ensure dependencies (`Scanpy, Harmony, AnnData, Plotly`) are installed.
3. **Execution**: Run the protocol pipeline snippet below.
4. **Output Generation**: Produce actionable Markdown/JSON summaries with publication figures.

---

## 💻 Protocol Code Snippet

```python
import scanpy as sc
import numpy as np

def run_sc_pipeline(h5ad_path):
    adata = sc.read_h5ad(h5ad_path)
    sc.pp.filter_cells(adata, min_genes=200)
    sc.pp.filter_genes(adata, min_cells=3)
    sc.pp.normalize_total(adata, target_sum=1e4)
    sc.pp.log1p(adata)
    sc.pp.highly_variable_genes(adata, n_top_genes=2000)
    sc.pp.pca(adata, n_comps=30)
    sc.pp.neighbors(adata, n_neighbors=15)
    sc.tl.umap(adata)
    sc.tl.leiden(adata, resolution=0.5)
    return adata

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

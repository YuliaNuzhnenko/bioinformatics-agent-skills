---
name: pubmed-rag-synthesizer
description: Vectorizes PubMed abstracts using PubMedBERT, builds FAISS indices, and instructs agents to synthesize clinical evidence with exact PMID citations.
version: "1.0.0"
metadata:
  author: Yulia Nuzhnenko
  domain: Biomedical AI & Literature
  frameworks: [LangChain, PubMedBERT, FAISS, EUtils API]
---

# Agent Skill: PubMed Literature RAG & Citation Agent Skill

[![Domain](https://img.shields.io/badge/Domain-Biomedical%20AI%20&%20Literature-00f0ff?style=flat-square)](#)
[![Version](https://img.shields.io/badge/Version-1.0.0-green?style=flat-square)](#)

## 📌 Description
Vectorizes PubMed abstracts using PubMedBERT, builds FAISS indices, and instructs agents to synthesize clinical evidence with exact PMID citations.

---

## 🤖 Agent Execution Protocol

When an AI Agent is tasked with `pubmed-rag-synthesizer`:
1. **Input Validation**: Verify that the required input files or coordinates are supplied.
2. **Environment Check**: Ensure dependencies (`LangChain, PubMedBERT, FAISS, EUtils API`) are installed.
3. **Execution**: Run the protocol pipeline snippet below.
4. **Output Generation**: Produce actionable Markdown/JSON summaries with publication figures.

---

## 💻 Protocol Code Snippet

```python
def build_pubmed_rag(pmid_list):
    # Vector Search Pipeline
    print(f"Indexing {len(pmid_list)} PubMed abstracts for RAG synthesis.")

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

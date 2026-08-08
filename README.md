# Bioinformatics & Scientific AI Agent Skills 🤖🧬

[![AI Agent Skills](https://img.shields.io/badge/Agent_Skills-Bioinformatics-00f0ff?style=flat-square)](#)
[![Compatibility](https://img.shields.io/badge/Compatible-Cursor%20%2F%20Claude%20Code%20%2F%20Antigravity-0d1117?style=flat-square)](#)
[![License](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](LICENSE)

An open-source library of ready-to-use **AI Agent Skills, System Prompts, and Workflow Protocols** for transforming LLM agents (Cursor, Claude Code, Antigravity, LangChain, CrewAI) into autonomous **AI Scientists** for Bioinformatics, Genomics, Structural Biology, and Drug Discovery.

---

## 📑 Table of Agent Skills

| Category | Agent Skill | Target Tools / APIs | File Path |
| :--- | :--- | :--- | :--- |
| **Transcriptomics** | `rna-seq-dge-analyzer` | DESeq2, limma, Volcano Plots | `skills/rna_seq_dge.md` |
| **Single-Cell Omics** | `scrna-scanpy-cluster` | Scanpy, Harmony, UMAP | `skills/scrna_scanpy.md` |
| **Structural Biology** | `alphafold-pocket-evaluator` | AlphaFold DB, py3Dmol, PDB | `skills/alphafold_pocket.md` |
| **Clinical Genomics** | `vcf-variant-annotator` | Ensembl VEP, ClinVar, Open Targets | `skills/vcf_annotation.md` |
| **Biomedical RAG** | `pubmed-literature-synthesizer` | PubMed API, BioBERT, FAISS | `skills/pubmed_rag.md` |
| **Cheminformatics** | `rdkit-qsar-ic50-predictor` | RDKit, ECFP4, LightGBM | `skills/qsar_ic50.md` |

---

## 🚀 How to Use Skills in AI Coding Agents

### 1. For Cursor / Antigravity Agents
Copy any skill markdown block from `skills/` into your project `.cursorrules` or Agent configuration file.

### 2. For Claude Code CLI
```bash
claude --prompt "$(cat skills/vcf_annotation.md) Analyze sample.vcf.gz"
```

---

## 🧬 Sample Skill: Clinical VCF Variant Annotator

```yaml
skill_name: vcf-variant-annotator
description: Instructs AI agents to parse VCF variant data, query ClinVar/Ensembl VEP, and format precision oncology summaries.
input_spec: VCF variant coordinates (CHROM, POS, REF, ALT)
output_spec: JSON & Markdown report with ClinVar pathogenicity and FDA targeted drug mappings.
```

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

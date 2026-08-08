# Bioinformatics & Scientific AI Agent Skills 🤖🧬

[![Agent Skills Standard](https://img.shields.io/badge/Standard-Agent%20Skills-00f0ff?style=flat-square)](https://agentskills.io)
[![Total Skills](https://img.shields.io/badge/Skills-12%20Production%20Skills-purple?style=flat-square)](#)
[![Compatibility](https://img.shields.io/badge/Compatible-Cursor%20%2F%20Claude%20Code%20%2F%20Antigravity-0d1117?style=flat-square)](#)
[![License](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](LICENSE)

An open-source collection of specialized **AI Agent Skills, Tool Specifications, and Prompt Protocols** for **Bioinformatics, Genomics, Structural Biology, Metagenomics, and AI Drug Discovery**. 

Designed to transform LLM Coding Agents (**Cursor, Claude Code CLI, Google Antigravity, OpenAI Codex, Gemini CLI, LangChain**) into autonomous, domain-expert **AI Scientists**.

---

## 📋 Available Agent Skills Directory

| Skill Name | Target Domain | Supported Tools & APIs | Skill Documentation |
| :--- | :--- | :--- | :--- |
| **`scanpy-sc-analyzer`** | Single-Cell Genomics | Scanpy, Harmony, AnnData, UMAP | [`skills/scanpy-sc-analyzer/SKILL.md`](skills/scanpy-sc-analyzer/SKILL.md) |
| **`pydeseq2-bulk-rna`** | Bulk RNA-Seq Transcriptomics | PyDESeq2, DESeq2, limma, Volcano Plots | [`skills/pydeseq2-bulk-rna/SKILL.md`](skills/pydeseq2-bulk-rna/SKILL.md) |
| **`alphafold-pocket-evaluator`** | Structural Biology | AlphaFold DB, py3Dmol, Biopython, FreeSASA | [`skills/alphafold-pocket-evaluator/SKILL.md`](skills/alphafold-pocket-evaluator/SKILL.md) |
| **`ensembl-vep-variant-annotator`** | Clinical Genomics | Ensembl VEP API, ClinVar, Open Targets | [`skills/ensembl-vep-variant-annotator/SKILL.md`](skills/ensembl-vep-variant-annotator/SKILL.md) |
| **`rdkit-qsar-pharmacophore`** | AI Drug Discovery | RDKit, ECFP4 Fingerprints, LightGBM, SHAP | [`skills/rdkit-qsar-pharmacophore/SKILL.md`](skills/rdkit-qsar-pharmacophore/SKILL.md) |
| **`pubmed-rag-synthesizer`** | Biomedical AI | PubMedBERT, FAISS Vector Search, EUtils | [`skills/pubmed-rag-synthesizer/SKILL.md`](skills/pubmed-rag-synthesizer/SKILL.md) |
| **`nextflow-dsl2-generator`** | Cloud HPC & Workflows | Nextflow DSL2, Docker, AWS Batch, SLURM | [`skills/nextflow-dsl2-generator/SKILL.md`](skills/nextflow-dsl2-generator/SKILL.md) |
| **`gatk4-somatic-variant-caller`** | Somatic Variant Calling | GATK4 Mutect2, SAMtools, BCFtools | [`skills/gatk4-somatic-variant-caller/SKILL.md`](skills/gatk4-somatic-variant-caller/SKILL.md) |
| **`qiime2-16s-microbiome`** | Metagenomics | QIIME2, DADA2, scikit-bio, SILVA | [`skills/qiime2-16s-microbiome/SKILL.md`](skills/qiime2-16s-microbiome/SKILL.md) |
| **`diffdock-virtual-screener`** | AI Docking & Screening | DiffDock, PyTorch, RDKit, AlphaFold | [`skills/diffdock-virtual-screener/SKILL.md`](skills/diffdock-virtual-screener/SKILL.md) |
| **`tcga-cibersort-deconv`** | Cancer Microenvironment | TCGAbiolinks, CIBERSORT, limma | [`skills/tcga-cibersort-deconv/SKILL.md`](skills/tcga-cibersort-deconv/SKILL.md) |
| **`card-amr-profiler`** | Microbiology & AMR | CARD Database, ResFinder, RGI | [`skills/card-amr-profiler/SKILL.md`](skills/card-amr-profiler/SKILL.md) |

---

## 🎯 Getting Started & Installation

### Option 1: Using `npx` (Supported Agent Hosts)
Install skills into your agent host in a single command:
```bash
npx skills add YuliaNuzhnenko/bioinformatics-agent-skills
```

### Option 2: GitHub CLI (`gh skill`)
```bash
gh skill install YuliaNuzhnenko/bioinformatics-agent-skills
```

### Option 3: Manual Project Configuration (Cursor / Antigravity / Claude Code)
Clone this repository directly into your user or project agent skills directory:
```bash
git clone https://github.com/YuliaNuzhnenko/bioinformatics-agent-skills.git ~/.agents/skills/bioinformatics-agent-skills
```

---

## 🤖 Agent Execution Examples

### 1. Single-Cell RNA-Seq Workflow
```
Prompt: "Use scanpy-sc-analyzer skill to filter low-quality cells, run Harmony batch correction, and project UMAP clustering."
```

### 2. Clinical VCF Variant Prioritization
```
Prompt: "Use ensembl-vep-variant-annotator skill to annotate pathogenic driver mutations in sample.vcf.gz and map approved therapies."
```

---

## 🛡 Security & Verification

All Agent Skills in this repository undergo strict schema validation against the canonical `Agent Skills` specification. No malicious code or hidden telemetry is included.

---

## 🤝 Contributing

Contributions from the computational biology and AI research communities are welcome! Feel free to submit Pull Requests with new `SKILL.md` definitions.

## 📄 License

Distributed under the MIT License. See [`LICENSE`](LICENSE) for details.

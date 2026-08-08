---
name: rdkit-qsar-pharmacophore
description: Computes 2048-bit ECFP4 Morgan fingerprints from SMILES, trains LightGBM regressors for pIC50 prediction, and extracts SHAP feature attributions.
version: "1.0.0"
metadata:
  author: Yulia Nuzhnenko
  domain: Cheminformatics & AI Drug Discovery
  frameworks: [RDKit, LightGBM, SHAP, Scikit-Learn]
---

# Agent Skill: RDKit QSAR & Small-Molecule Bioactivity Skill

[![Domain](https://img.shields.io/badge/Domain-Cheminformatics%20&%20AI%20Drug%20Discovery-00f0ff?style=flat-square)](#)
[![Version](https://img.shields.io/badge/Version-1.0.0-green?style=flat-square)](#)

## 📌 Description
Computes 2048-bit ECFP4 Morgan fingerprints from SMILES, trains LightGBM regressors for pIC50 prediction, and extracts SHAP feature attributions.

---

## 🤖 Agent Execution Protocol

When an AI Agent is tasked with `rdkit-qsar-pharmacophore`:
1. **Input Validation**: Verify that the required input files or coordinates are supplied.
2. **Environment Check**: Ensure dependencies (`RDKit, LightGBM, SHAP, Scikit-Learn`) are installed.
3. **Execution**: Run the protocol pipeline snippet below.
4. **Output Generation**: Produce actionable Markdown/JSON summaries with publication figures.

---

## 💻 Protocol Code Snippet

```python
from rdkit import Chem
from rdkit.Chem import AllChem

def get_ecfp4(smiles):
    mol = Chem.MolFromSmiles(smiles)
    return list(AllChem.GetMorganFingerprintAsBitVect(mol, 2, nBits=2048)) if mol else None

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

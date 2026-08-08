# Agent Skill: AlphaFold 3D Pocket Evaluator

```yaml
name: alphafold-pocket-evaluator
version: 1.0.0
domain: Structural Biology & Drug Discovery
```

## Agent Protocol
When evaluating protein structures:
1. Fetch 3D PDB coordinates from AlphaFold DB using UniProt Accession.
2. Parse B-factor column to extract per-residue pLDDT confidence scores.
3. Calculate Solvent Accessible Surface Area (SASA) of active site residues.

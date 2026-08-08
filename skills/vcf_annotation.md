# Agent Skill: Clinical VCF Variant Annotator

```yaml
name: vcf-variant-annotator
version: 1.0.0
domain: Clinical Genomics & Precision Oncology
```

## Agent Protocol
When a user provides a VCF variant entry or coordinates:
1. Extract Chromosome, Position, Reference, and Alternate alleles.
2. Query NCBI ClinVar REST API for clinical significance classification (Pathogenic, VUS, Benign).
3. Retrieve Ensembl VEP REST API functional consequences (SIFT/PolyPhen-2 scores).
4. Map detected driver mutations (e.g. BRAF V600E, BRCA1) to approved targeted therapies on Open Targets.

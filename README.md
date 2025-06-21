# Protein Sequence Analysis of Hemoglobin Alpha Subunit

## Overview

This project focuses on analyzing the **alpha subunit of hemoglobin**, a critical oxygen-transport protein in red blood cells. The goal is to identify and annotate functional domains, motifs, and structural features using bioinformatics tools.

## Objectives

- Annotate protein domains and motifs using **InterProScan**.
- Interpret associated **Gene Ontology (GO)** terms for biological function.
- Identify secondary structural elements using **PSIPRED** with **DSSP** notation.
- Relate structure to function through combined annotation.

## Data Sources and tools

- **Protein Sequence**: Retrieved from UniProt (e.g., [P69905](https://www.uniprot.org/uniprot/P69905)).
- **PSIPRED**: Used for assigning secondary structures (e.g., helix, loop).
- **InterProScan**: Used for predicting motifs and domains.
- **GO terms & Reactome**: Provided in InterProScan output.

## Workflow

1. Retrieve the hemoglobin alpha sequence.
2. Assign secondary sturcutre using PSIPRED
3. Run InterProScan and collect `.tsv` results.
4. Parse and filter annotations based on significance (e.g., E-values).
5. Add GO term and Reactome pathway interpretations.
6. Combine sequence and structure features in one annotation table.

## 📊 Results

composotion of the protein in terms of the amino acid shows that protein subunit has higer level of Alanine amino acid.
<img src="images\amino-acid-comp.png" alt="composition of the protein" style="width:50%;"/>

The following alignment shows the relative positions of the aamino acid and the secondary of which the amino acid is a part of. The Protein majorly comprises of alpha helices.

<img src="images\annotated pred.webp" alt="composition of the protein"/>
<img src="images\structure-comp.png" alt="composition of the protein" style="width:50%;"/>

### The table shows the domans and motifs in the protien subunit. Amino acid from position 4-29 act as the iron ion binding and comprise of only alpha helices.

|     | interpro_id | interpro_desc          | analysis | start | end | significance                           |
| --: | :---------- | :--------------------- | :------- | ----: | --: | :------------------------------------- |
|   0 | IPR002338   | Hemoglobin, alpha-type | CDD      |     3 | 142 | hamoglobin complex, oxygen transporter |
|   1 | IPR000971   | Globin                 | Pfam     |    27 | 137 | heme binding                           |
|   2 | IPR002339   | Hemoglobin, pi         | PRINTS   |     4 |  29 | Iron ion biniding                      |

## 🧠 Biological Interpretation

- Hemoglobin alpha subunit is essential for **oxygen binding and transport**.
- Identified motifs **globin domain**, **heme-binding site** which support the protien.

## 💭 Limitations and Future Work

- Some annotations may overlap or be redundant.
- Structural annotations depend on quality of the input PDB file.
- Future steps could include:
  - Comparative analysis with beta subunit.
  - Multiple sequence alignment across species.

## 📚 References

- [InterProScan Documentation](https://interproscan-docs.readthedocs.io/en/latest/)
- [Biopython Documentation](https://biopython.org/)
- [UniProt: Hemoglobin Subunit Alpha (P69905)](https://www.uniprot.org/uniprot/P69905)
- Reactome and Gene Ontology databases

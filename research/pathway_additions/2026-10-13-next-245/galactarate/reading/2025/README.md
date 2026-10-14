# 2025 primary evidence: galactarate utilization

This independent appraisal covers Levy et al., *Convergent evolution of oxidized sugar metabolism in commensal and pathogenic microbes in the inflamed gut* ([PMID39875389](https://pubmed.ncbi.nlm.nih.gov/39875389/), [DOI10.1038/s41467-025-56332-9](https://doi.org/10.1038/s41467-025-56332-9)). It is a primary-source appraisal, not a native pathway-record review or validation receipt.

The paper provides genetic and physiological corroboration for E. coli galactarate utilization. The canonical four-step GarD→GarL→GarR→GarK chemistry remains background in this paper; separate primary biochemistry and issuing chemical/reaction authorities must support its formal equations.

## Strongest applicable evidence

| Claim | Exact inspected locators | Required scope |
|---|---|---|
| GarP contributes to galactarate utilization: deletion attenuates fermentation and its native-gene plasmid restores it. | XML Par15–18,35,43,45,47; Fig3B; Supplementary Table2; Source Data `Figure 3B-G!A2:B47` | Functional transport context, not directly measured uptake or proton stoichiometry. |
| GarL deletion diminishes galactarate fermentation and native-gene expression rescues it. | Par15,18,43,45,47; Fig3A,C; Supplementary Fig2/Table2; Source Data `Figure 3B-G!F2:G38` | Pathway participation, not direct product identification. |
| GarR deletion attenuates galactarate fermentation and native-gene expression rescues it. | Par15,18,43,45,47; Fig3D; Supplementary Table2; Source Data `Figure 3B-G!K2:L50` | No inference of NADH versus NADPH specificity or assembly. |
| E. coli 5α grows with galactarate supplementation. | Par11,42; Fig2F; Source Data `Figure 2A-F!R82:AG120` | Separate 5α experiment in anaerobic, supplemented BHI; not MG1655 or chemically sole-carbon growth. |

The GarP/L/R mutants are **BW25113 Keio** strains. Native inserts were amplified from BW25113 and expressed in pCW-lic under inducible **tac**, with 100 µM IPTG. Figure3 and Supplementary Fig2 identify **BL21** as the positive control, so it must not be described as an isogenic BW25113 comparator. The endpoint was pH-dependent A460−A620 after 48 h at 25°C in **10 g/L peptone plus 10 g/L sugar**. It was not a direct growth, transport, flux or purified-enzyme assay. Anaerobiosis was explicit for the separate growth screen, not the fermentation-plate protocol. Plasmid maps and primers were inspected; complete verified construct sequences were not obtained.

## Deliberate exclusions and source defects

- Figure1A draws the named tartronate semialdehyde with two carboxyl termini. Do not use this schematic for exact chemistry; it also omits relevant co-substrates.
- The Fig3 legend says n=9 for each galactarate panel; source-data deletion/rescue groups contain **9 for GarP, 6 for GarL and 10 for GarR**. These are numerical observations, not independently established biological-replicate counts. Preserve qualitative rescue without repeating uniform n or claiming reproduced significance.
- Fig3D/F have apparent construct-name typos; graph labels, workbook and Methods resolve the intended backgrounds/genes. Exact observations are in `appraisal.json`.
- Enterocloster GarABC/GudL and Fusobacterium constructs are alternative heterologous systems. GudL direct aldolase chemistry was not demonstrated, explicitly acknowledged in peer-review pp8–9,16–17. Its mutation results cannot be transferred to E. coli GarL.
- GarK omission from the computational minimum-gene screen reflects phylogenetic search design, not dispensability of the canonical fourth reaction. Par35's possible GudP-mediated galactarate import remains hypothetical.
- No new direct GarD/GarK enzymology or CdaR regulation experiment is supplied. Par39 explicitly leaves changes in transcriptional regulation unresolved; IBD associations do not establish causation.

## Acquisition and reading scope

The complete article XML, eight main figure images and all six supplements were obtained; all six publisher supplements match their EuropePMC ZIP members byte-for-byte. All main text/Methods/captions and main figures were inspected; the principal supplement's eight pages were read and viewed. Reporting-summary text was read, with its design page viewed. Peer-review inspection was bounded to relevant pp7–9,16–17; workbook inspection covered all sheet headers, the indicated Fig2F/3B–D regions and selected Escherichia inventory rows, not every sequence or metadata row. `reading-coverage.json` records the precise boundaries.

An additional complete issuing UniProt P0AA80 response establishes GarP identity (garP/yhaU, b3127/JW3096, 444 aa, K12, RefSeq NP_417596.1, GeneID947642). It does not prove exact identity of the experimental construct or direct transport chemistry. Error HTML and a raw NCBI reCAPTCHA response were retained as rejected responses.

`source-manifest.json` binds each original to public URL/time/status/hash and a member of the external deterministic archive `oxidized-sugars-2025-originals.tar.gz`. Every archived member was read back and hash-verified. Complete source bodies, workbooks, images and acquisition receipts remain external; temporary paths are acquisition history, not public or permanent hosting. `artifact-manifest.json` inventories the compact retained appraisal files. No maintained record, native review bundle or GitHub state was modified by this appraisal.

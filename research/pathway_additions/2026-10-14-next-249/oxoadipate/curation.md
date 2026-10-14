# Pathway mechanism research: 3-oxoadipate degradation

## Pathway scope

`MetaCyc:PWY-2361` defines the complete two-reaction terminal module converting
3-oxoadipate through 3-oxoadipyl-CoA to acetyl-CoA and succinate, with succinyl-CoA
regenerated. The record retains native *Pseudomonas putida* catalyst identities
and distinguishes the PRS2000 experimental lineage from other strains. The
upstream catechol and protocatechuate branches remain separate pathways.

All 246 baseline records were inventoried. Forty-two exact searches included
hidden and ignored files. PWY-2361 appeared as an interface in the catechol
record, but not as a record of its own. Searches excluded Git metadata and the
virtual environment, did not decode compressed archives or follow symlink
directories, and did not exhaust external caches. These bounds do not establish
source exhaustion. Protocatechuate ortho cleavage remains a subsequent lead;
the separate galactitol stereochemistry problem remains unresolved.

The pinned GO term GO:0042952 includes both upstream branches and this terminal
module. Its broader scope cannot replace PWY-2361. The two relevant molecular
function terms each describe one enzyme activity, rather than the pathway.

## Mechanistic summary

RHEA:12049 transfers CoA from succinyl-CoA to 3-oxoadipate. RHEA:19483 consumes
the resulting 3-oxoadipyl-CoA and free CoA, producing acetyl-CoA and succinyl-CoA.
Both complete equations balance atoms and charge. Every chemical-side
coefficient is one. The native reaction objects are reversible; the pathway
selects their forward and reverse traversals, respectively. RHEA:19483 retains
its right-to-left family direction even though its displayed directional
equation puts the consumed compounds first.

All six native complete InChIs, formulas and charges agree with ChEBI 255 and
current issuing records. Two native SMILES fields are incomplete. InChI
reconstruction can redistribute mobile proton and charge sites in CoA species;
the original CML and ChEBI SMILES agree. KEGG structures represent neutral
forms, so their route cross-references are not exact charged-equation synonyms.
Adipate(2-) is an experimental inducer analog, not a substrate of this module.

The native transferase model contains two copies each of MONOMER-3190 and
MONOMER-3191. Historical mass measurements support that model, while current
UniProt subunit entries say heterodimer. Both observations remain explicit.
The native thiolase model has four MONOMER-3207 copies; its cited P. putida
genetic experiment does not directly measure oligomerization. Measurements
from *Pseudomonas* strain B13 are not transferred to these proteins.

## Evidence table

| Source | Supported assertion | Boundary retained |
| --- | --- | --- |
| Complete META 27.0 pathway, reactions, complexes, monomers and activity objects | Two-step boundary, order, catalyst identities, native assembly and evidence annotations | Layout primaries are not complete equations; native comments include identified errors |
| Rhea 142 RDF and directional table; ChEBI 255 and current issuing structures | Complete chemical sides, charges, identities and source orientation | Pinned Rhea 139 continues to supply canonical authority labels |
| Parales 1992 and 1993, PMID:1624453 and PMID:8376330 | PRS2000 pcaIJ identity, complementation and PcaR-dependent promoter induction | Reporter expression does not establish direct enzyme activation |
| Romero-Steiner 1994, PMID:8083169 | PRS2000 PcaR identity and promoter binding in recombinant crude extracts | Initiating methionine remains uncertain; no direct inducer-binding claim |
| Harwood 1994, PMID:7961399 | PcaF mutant phenotype and adipate-dependent cell-extract activity | No P. putida thiolase oligomer measurement; paper leaves PcaR-to-pcaF regulation unresolved |
| Nichols 1995, PMID:8522507 | Later report of PcaR requirement and 3-oxoadipate induction for pcaF | Author abstract inspected; full paper inaccessible |
| Yeh 1981, PMID:6780551 | Historical transferase mass and inferred alpha2beta2 assembly | Rendered discussion and Table VI inspected; miniprint and original figures unread |
| Kaschabek 2002, PMID:11741862 | Independent purified-enzyme route chemistry in strain B13 | Intermediate assignment has stated analytical limits; no P. putida protein equivalence |

Four complete older papers were read from all 39 original archived page scans.
The B13 paper's complete HTML, two figures and three tables were inspected.
The primary manifest distinguishes original scans, landing pages, metadata,
failed downloads and inaccessible material. References for quoted scans bind
the specific page bytes; those hashes do not purport to cover a complete paper.

## Gaps

The native Chan79 citation resolves to an unrelated amniotic-fluid paper
(PMID:761399); it is rejected without guessing a replacement. The native
transferase comment saying it was not purified conflicts with its experimental
annotation and the 1981 primary report. The original 1966 paper was inaccessible
and is not quoted or claimed read.

The deposited ENA translations match the current issuing UniProt sequences for
PcaI, PcaJ, PcaF and PcaR. The PcaR paper prints 292 residues, whereas L33795 and
Q52154 encode 291; the discrepancy and possible initiating Met-1/23/45 remain
documented. ENA L33795 labels its source PRS1/ATCC12633, while the UniProt sequence
reference names PRS2000. Original 1994 pages 5771–5773 describe PRS2000 as a
PRS1 derivative and trace cloning/PCR to PRS2000. The deposited translation
match is separate from that lineage interpretation; neither establishes
complete-genome identity or universal strain synonymy. See
`native/sequence-lineage-reconciliation.json` for page-specific hashes.
No modern KT2440 homolog replaces a PRS2000 protein. iModulonDB's positive
KT2440 PcaR module is separate computational expression context.

No direct 3-oxoadipate-to-PcaR binding, physiological magnesium cofactor,
upstream PcaK transport, ATP-dependent alternative activation, or B13-specific
inhibition is inferred. Magnesium was used to detect an assay-product chelate.
Expression induction is modeled as regulation, rather than catalytic activation.

## Candidate YAML

The maintained record is `data/pathways/3-oxoadipate-degradation.yaml`.
It contains 13 participants, two reactions, 22 edges and 18 references. Exact
identifiers are listed in `identifiers.json`. All ten new authority terms were
produced from original source bytes by unchanged canonical builders; all
4,776 previous terms and 752 previous source-owner objects are retained.

Full scientific downloads, paper scans, HTTP responses and acquisition helpers
remain external. This dossier retains compact projections, digest manifests,
and review and validation receipts. Independent scientific review and the
required gates are recorded separately after execution.

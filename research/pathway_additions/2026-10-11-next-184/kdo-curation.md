# CMP-Kdo biosynthesis curation

Target: `data/pathways/cmp-kdo-biosynthesis.yaml`, GO:0033468, **CMP-keto-3-deoxy-D-manno-octulosonic acid biosynthetic process**. This is a complete, source-defined pathway with an explicit stereochemical limitation. It is not downstream Kdo transfer to lipid IVA (`KDOSYN-PWY`) or general LPS assembly.

The pinned GO term explicitly cross-references MetaCyc:PWY-1269. The native MetaCyc 22.5 XML defines **five**, not four, reaction-list members: the four enzyme conversions plus spontaneous arabinose-5-phosphate ring equilibrium. All five are retained. The initial cohort planning phrase “ring opening” is corrected here: the native displayed left-to-right orientation closes the aldehydo sugar into its furanose form, and the reaction itself is reversible.

## Complete boundary and chemical source conflicts

| Native member | Maintained activity | Disposition |
|---|---|---|
| DARAB5PISOM-RXN | RHEA:23106 | D-ribulose 5-phosphate to aldehydo-D-arabinose 5-phosphate; selected biosynthetic direction of a reversible enzyme. Native RHEA:23107 is bidirectional; the full RDF independently links both variants to master 23104. |
| RXN-16804 | MetaCyc:RXN-16804 | Native spontaneous reversible aldehydo/furanose equilibrium; no molecular-activity category or invented catalyst. Displayed consume/produce links follow native closure orientation. |
| KDO-8PSYNTH-RXN | RHEA:14054 | Current open-chain A5P + PEP + water to alpha-Kdo8P + phosphate. Native 22.5 instead names the furanose substrate. Primary PMID:1521535 supports the acyclic substrate; its enzyme work concerns E. coli B per native provenance, not a direct K-12 assay. |
| KDO-8PPHOSPHAT-RXN | RHEA:11501 | Current Kdo8P hydrolysis to free alpha-Kdo + phosphate. K-12 protein assignment is explicitly by similarity. |
| CPM-KDOSYNTH-RXN | RHEA:23449 | Current formal alpha-Kdo + CTP to CMP-beta-Kdo + diphosphate, with unresolved experimental substrate-anomer conflict described below. |

The selected graph preserves current Rhea 142 formula, charge, coefficients and reaction-family direction links. Its chemistry does not use neutral-acid names as substitutes for charged ChEBI entities. Fifteen exact Rhea sides and two native equilibrium sides are replayed. The four Rhea reactions and native isomerization balance independently against full ChEBI 255 formula/charge statements. Chemical balance cannot resolve a stereochemical conflict.

The ring equilibrium is retained as a pool equilibrium, not used to force an unsupported furanose-to-KdsA transition. Current Rhea consumes the open-chain form supplied by the API step. All native members and original ordering are preserved in the source projection, with this explicit adjudication. There is no duplicated net reaction, decomposition, or invented ring-opening enzyme.

### KdsB stereochemistry: explicit independent-review question

PMID:2997221 directly reports beta-pyranose Kdo as the preferred substrate and retention of beta configuration in CMP-Kdo. Full primary PMC2790981 (PMID:19815542), Results and Discussion / Kinetic Characterization of KdsB, independently reiterates that the approximately 2% beta-pyranose fraction is accepted. This is not merely a naming assertion inferred from an inhibitor.

Current Rhea:23448/23449, reviewed UniProt P04951 and the native MetaCyc KDO compound instead specify **alpha** free Kdo. ChEBI:85986 has an explicit alpha stereochemical structure; ChEBI:85987 is the CMP-beta product. These are not silently declared equivalent. A full pinned ChEBI label/synonym query and live exact-name primary-registry search did not verify a suitable free-beta Kdo identifier. ChEBI:16064 is acyclic, and ChEBI:65335 is a generic class; neither was substituted as an exact beta structure. This is a bounded search result, not a claim that no identifier exists anywhere.

The record retains the exact current formal Rhea reaction. Every edge involving RHEA:23449 explicitly says that it follows the database convention and does not establish experimental alpha catalysis; the beta primary evidence is attached to the substrate edge and the gene-product role and is prominent in the pathway description. No alpha-to-beta anomerase is inferred. The independent reviewer should adjudicate whether this clearly qualified source-defined graph is an acceptable representation; it must not be read as a resolved stereochemical mechanism. A concrete follow-up is to resolve the Rhea/ChEBI annotation against the NMR and structural sources and obtain a verified beta entity before replacing this convention.

## Organism, assemblies and cofactors

The record scope is E. coli K-12 (NCBITaxon:83333), the taxon of all five reviewed UniProt entries. Native assemblies and full-pathway annotation include MG1655. The GutQ primary paper uses MG1655 genomic DNA but BW30270-derived K-12 deletion strains; it is not relabeled as one uniform MG1655 flux experiment. Expression in BL21 is distinguished from the donor protein's origin.

* **KdsD P45395** and **GutQ P17115** have exact native tetramers CPLX0-1262 and CPLX0-3929, each with four explicitly cross-referenced subunits. Reviewed subunit/catalysis annotations carry ECO:0000269. PMID:12805358 and full PMID:16199563 support the API role; the latter directly establishes GutQ compensation for KdsD loss in K-12. The proposed A5P regulatory role is not promoted to a regulation edge.
* **KdsA P0A715** maps through its exact native monomer to KDO-8PSYNTH-CPLX with four subunits. Primary PMID:10926505 discusses tetrameric structural contacts. Current UniProt instead says “Homotrimer” without an evidence code; this disagreement is retained without inventing a condition that explains it. Catalysis is attached to the verified native tetramer, with current open-chain chemistry explicitly distinguished from the old native substrate form.
* **KdsC P0ABZ4** catalysis, Mg binding and tetramer statements all carry ECO:0000250 to A0A140N5J7. The independently inspected native complex CPLXCQ7-1 is BL21(DE3), not K-12. Full PMC2781614 shows active sites at tetramer interfaces and catalytic Mg; its earlier cloned enzyme is sourced through PMID:12639950, which characterizes strain B enzyme. It is not relabeled as a direct K-12 assay. A qualified gene-product `enables` edge retains the K-12 assignment without implying monomer sufficiency or inventing a K-12 complex accession.
* **KdsB P04951** is assigned current chemistry by HAMAP MF_00057 (ECO:0000255). Native CPM-KDOSYNTH-MONOMER explicitly unifies P04951 but its frame name is not evidence of a catalytically sufficient monomer. Full PMC2790981 shows dimers and an opposite-subunit CTP contact. The record uses a qualified functional role and preserves the dimer context. Its Mg evidence separates one observed site from a second site proposed by modeling and Mn-substituted EPR; it does not claim crystallographic observation of two Mg ions.

No API zinc cofactor is inferred from zinc binding: the inspected sources describe inhibition and lack of a cofactor requirement. KdsA metal-inhibitor annotations do not establish an obligatory metal. KdsC inefficient Ca substitution is not a Ca requirement. Optional assay inhibitors, proposed GutQ regulation, capsule-specific KpsF/KpsU and downstream Kdo transfer/LPS assembly are outside this complete pathway's core graph.

## Novelty and contextual evidence

Fresh searches included hidden and ignored files throughout both the current 184-record worktree and the now-readable original Documents checkout, excluding only `.git` and `.venv` internals. The latter is an older clean main at dbf399e. Its ignored DRAM `M00063` source rows 650–653 define the four enzyme steps; they were read and are reusable source leads, not a maintained pathway duplicate. Current-cohort planning and iModulon receipts account for the other hits. Adjacent lipid-IVA and peptidoglycan records do not cover CMP-Kdo synthesis. Exact queries, outputs and limitations are in `kdo-search-ledger.json`.

Root's shared iModulonDB context searched the five genes and their aliases/loci/accessions with the unchanged client after the console runner was unavailable. Two returned modules were inspected without matching queried Kdo members. Expression context establishes neither catalytic function nor biological absence; no iModulon edges are added.

## Evidence and verification receipt

Current UniProt full bodies are release 2026_03. Native XML explicitly declares MetaCyc 22.5. Full primary HTML was retrieved for PMIDs:16199563, 19815542 and 19726684. PMIDs:12805358, 10926505, 1521535 and 2997221 remain indexed abstract evidence. Three Europe PMC fullTextXML attempts returned HTTP 500; three BioC requests returned HTTP 200 no-result bodies that were rejected. Successful public PMC HTML is independently retained and hashed. No unavailable article is claimed to have been read.

All reference hashes cover the exact complete retained response body specified in the manifest. Rhea hashes cover the full compressed RDF, not the parsed subset. The manifest retains no session, cookie or authentication headers. The root-fetched HTML pages are independent identity inputs; native XML remains the mechanism source.

`kdo-replay.py` performs native and closed schema validation, body-hash checks, complete native membership and direction replay, two-pass full-RDF extraction with side-level coefficients, formula/charge balances, exact native assembly/UniProt bridges, reviewed identity checks, scientific-limit guards and actual KGX evidence/category preservation. `kdo-validation.json` records its actual terminal result. Root owns corpus-wide identifier integration, history, rendering, full validation/tests and the separate independent scientific review.

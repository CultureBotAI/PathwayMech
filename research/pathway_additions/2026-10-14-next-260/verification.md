# Gallate degradation II: final local verification

## Pathway scope

Added **MetaCyc:GALLATE-DEGRADATION-I-PWY — gallate degradation II** in [the maintained YAML](../../../data/pathways/gallate-degradation-ii.yaml), with its [generated pathway graph](../../../pages/records/MetaCyc_GALLATE-DEGRADATION-I-PWY.html). The accession suffix I and display name II are intentionally different in the issuing source.

The record contains 169 evidence-backed edges, 90 participants, 11 reaction/interface nodes, 1 taxon and 65 references. Five reactions are formal route members; adjacent assay activities do not extend that boundary. The duplicate assessment searched the entire repository including ignored/hidden files, with root Git/dependency metadata exclusions recorded, and inspected all 256 predecessor records. Prior research mentions and shared downstream modules were retained and distinguished from an exact duplicate.

Two predecessor records receive bounded corrections: six issuing Rhea member directions and 15 connected source-direction descriptions. Their other parsed content is unchanged. [Issue #558](https://github.com/CultureBotAI/PathwayMech/issues/558) tracks those corrections. [Issue #559](https://github.com/CultureBotAI/PathwayMech/issues/559) tracks an independently found retained-ledger locator typo, corrected by an append-only clarification. Both fixes are prepared for this pull request.

## Mechanistic summary

The five-step route connects gallate through pyrone dicarboxylate, keto oxalomesaconate, formal E,E enol and carboxyhydroxyoxoadipate to pyruvate plus oxaloacetate. The selected members are MetaCyc:RXN-11861, RHEA:10645, RHEA:28932, RHEA:17403 and RHEA:28936. All 17 formal material relations and the net elemental/charge balance were replayed. Rhea member direction and native reversibility remain separate assertions; RHEA:17403 describes hydration by the right-to-left member. Adjacent optical-HG assay context uses forward cleavage member RHEA:18170 without converting measured equilibrium into a whole-pathway claim.

## Evidence table

| Evidence | What it supports |
| --- | --- |
| [Source and author ledger](README.md) | Complete native pathway closure, 179 primary fact dispositions, exact preparations, source conflicts and deliberate exclusions. |
| [Entry primary papers](sources/primary/HANDOFF.md) | Original 1975 and 1982 text/tables, distinguishing gifted enzyme, purified product-identifying preparations and PDC-isolate extracts. |
| [Preparation follow-up](sources/preparation-successor/HANDOFF.md) | Scoped LigJ/PmdE/ProH/ProA/GalB assays, constructs, optical substrates and conditional metal/nucleotide effects. |
| [Authority union](authority/HANDOFF.md) | Exactly 34 selected additions; all 4,989 prior terms and their owners preserved. Final total 5,023 terms; no parser/schema/policy change. |
| [Technical proof package](reviews/independent-technical/HANDOFF.md) | Source integration, KGX, authority, rendered SVG/DOM/evidence links, and unchanged production/governance files. |

## Gaps

The detailed 1985 ProH source and 2018 LigJ main text/thesis remain unavailable in the recorded attempts. Historical protein identities, sample provenance, some construct termini and the E6 cleavage scar remain unresolved. Formal E,E chemistry is not interchangeable with the source narrative Z,Z link or unassigned historical mixtures. Formal CHA is stereochemistry-unspecified, which does not establish a racemic sample. Exact LigJ/BR6020PmdE formal E,E catalysis is deferred. Component evidence does not establish complete-route occurrence in every enzyme-source or expression-host taxon.

Browser preview was unavailable because no browser surface was available. The technical reviewer checked generated SVG/DOM data, local anchors, evidence, qualifiers and downloads directly; this report does not claim a visual or interactive browser inspection. The optional structured iModulonDB adapter was unavailable to the scientific reviewer, and no transcriptomic evidence was inferred.

## Completed checks and saved reviews

`just render-pages`, `just validate`, `just test`, `just lint`, `just vendored-check`, working `git diff --check` and staged `git diff --cached --check` passed. Full validation covers 257 records, 457 history entries and 18,925 evidence blocks. Tests: **5,255 passed, 3 skipped, 7 warnings**. The initial vendored attempt failed solely on sandbox DNS; its bounded network retry passed. All 8 actual attempts and their logs are [retained](reviews/verification/retention-manifest.json). All 2,026 tested core input files stayed unchanged; only final reports, saved reviews and verification evidence were appended afterward.

All three saved canonical reviews are completed and pass with explicit limitations, with no unresolved findings. Required checks were shared actual executions; independent source review is documented separately from deterministic validation.

- `20261015T013756Z-next260-gallate-degradation-ii-science`: [Markdown](../../../reviews/structured/20261015T013756Z-next260-gallate-degradation-ii-science/review.md), [YAML](../../../reviews/structured/20261015T013756Z-next260-gallate-degradation-ii-science/review.yaml).
- `20261015T013807Z-next260-shared-rhea-direction-context`: [Markdown](../../../reviews/structured/20261015T013807Z-next260-shared-rhea-direction-context/review.md), [YAML](../../../reviews/structured/20261015T013807Z-next260-shared-rhea-direction-context/review.yaml).
- `20261015T013924Z-next260-independent-technical`: [Markdown](../../../reviews/structured/20261015T013924Z-next260-independent-technical/review.md), [YAML](../../../reviews/structured/20261015T013924Z-next260-independent-technical/review.yaml).

Canonical `record_review.py check --base b2590dfd2385c83fe4f028ecd5309a0407739838 --require-reviews` passed after saving all three bundles. The [persistence receipt](reviews/root-completion/canonical-review-persistence.json) preserves actual commands and results. Publication and merge are subsequent operations and are not claimed by this local verification report.

## Selected identifiers

The [machine-readable selection](identifier-selection.json) lists all 103 pathway/node identifiers, all 65 local reference identifiers and the 34 authority additions separately. Existing identifiers reused in this record are not mislabeled as new corpus terms.

### Pathway and local nodes

| Identifier | Label | Role |
| --- | --- | --- |
| `CHEBI:15356` | cysteine | participants |
| `CHEBI:15361` | pyruvate | participants |
| `CHEBI:15377` | water | participants |
| `CHEBI:15378` | hydron | participants |
| `CHEBI:15379` | dioxygen | participants |
| `CHEBI:15422` | ATP | participants |
| `CHEBI:16382` | iodide | participants |
| `CHEBI:16452` | oxaloacetate(2-) | participants |
| `CHEBI:16526` | carbon dioxide | participants |
| `CHEBI:16761` | ADP | participants |
| `CHEBI:16763` | 2-oxobutanoate | participants |
| `CHEBI:16793` | mercury(2+) | participants |
| `CHEBI:16810` | 2-oxoglutarate(2-) | participants |
| `CHEBI:16856` | glutathione | participants |
| `CHEBI:16918` | gallate | participants |
| `CHEBI:16947` | citrate(3-) | participants |
| `CHEBI:17051` | fluoride | participants |
| `CHEBI:173437` | 4-Hydroxy-2-oxobutanoic acid | participants |
| `CHEBI:17742` | 4-hydroxy-2-oxoglutarate(2-) | participants |
| `CHEBI:17996` | chloride | participants |
| `CHEBI:18320` | 1,4-dithiothreitol | participants |
| `CHEBI:18420` | magnesium(2+) | participants |
| `CHEBI:22629` | arsenate ion | participants |
| `CHEBI:23414` | copper(II) sulfate | participants |
| `CHEBI:29033` | iron(2+) | participants |
| `CHEBI:29034` | iron(3+) | participants |
| `CHEBI:29035` | manganese(2+) | participants |
| `CHEBI:29036` | copper(2+) | participants |
| `CHEBI:29105` | zinc(2+) | participants |
| `CHEBI:29108` | calcium(2+) | participants |
| `CHEBI:29888` | diphosphoric acid | participants |
| `CHEBI:30089` | acetate | participants |
| `CHEBI:30808` | iron trichloride | participants |
| `CHEBI:31823` | mercury dichloride | participants |
| `CHEBI:32139` | sodium hydrogencarbonate | participants |
| `CHEBI:32588` | potassium chloride | participants |
| `CHEBI:3312` | calcium dichloride | participants |
| `CHEBI:34887` | nickel dichloride | participants |
| `CHEBI:35780` | phosphate ion | participants |
| `CHEBI:36655` | glyoxylate | participants |
| `CHEBI:44485` | N-ethylmaleimide | participants |
| `CHEBI:44976` | phosphonic acid | participants |
| `CHEBI:4735` | ethylenediaminetetraacetic acid | participants |
| `CHEBI:48775` | cadmium(2+) | participants |
| `CHEBI:48828` | cobalt(2+) | participants |
| `CHEBI:49786` | nickel(2+) | participants |
| `CHEBI:53351` | chromium(3+) trichloride | participants |
| `CHEBI:57471` | (1E)-4-oxobut-1-ene-1,2,4-tricarboxylate | participants |
| `CHEBI:57499` | 2-oxoadipate(2-) | participants |
| `CHEBI:58075` | 2-hydroxy-4-oxobutane-1,2,4-tricarboxylate | participants |
| `CHEBI:58142` | 4-carboxy-2-hydroxy-cis,cis-muconate(3-) | participants |
| `CHEBI:58222` | 4-hydroxy-2-oxopentanoate | participants |
| `CHEBI:58276` | 4-hydroxy-4-methyl-2-oxoglutarate(2-) | participants |
| `CHEBI:58304` | 2-oxo-2H-pyran-4,6-dicarboxylate | participants |
| `CHEBI:59051` | diethyl pyrocarbonate | participants |
| `CHEBI:62843` | beryllium dichloride | participants |
| `CHEBI:63317` | barium chloride | participants |
| `CHEBI:747199` | strontium sulfate | participants |
| `CHEBI:86228` | dithionitrobenzoic acid | participants |
| `CHEBI:9532` | thiamine(1+) diphosphate | participants |
| `GO:0005829` | cytosol | participants |
| `MetaCyc:4.1.3.17-RXN` | 4-hydroxy-4-methyl-2-oxoglutarate aldolase | reactions |
| `MetaCyc:CPD-29` | p-chloromercuribenzoate | participants |
| `MetaCyc:CPLX-2721` | protocatechuate 3,4-dioxygenase | participants |
| `MetaCyc:CPLX-2781` | 4-oxalomesaconate hydratase | participants |
| `MetaCyc:CPLX-2782` | HMG aldolase | participants |
| `MetaCyc:CPLX-2864` | 4-oxalomesaconate hydratase | participants |
| `MetaCyc:CPLX-2865` | 4-carboxy-4-hydroxy-2-oxoadipate aldolase | participants |
| `MetaCyc:CPLX-2881` | HMG aldolase | participants |
| `MetaCyc:CPLX-7917` | HMG aldolase | participants |
| `MetaCyc:CPLX-8178` | 4-oxalmesaconate hydratase | participants |
| `MetaCyc:CPLX1G01-155` | 4-hydroxy-4-methyl-2-oxoglutarate aldolase | participants |
| `MetaCyc:DITHIO-NITROBENZOATE` | 5,5'-dithio-bis-2-nitrobenzoate | participants |
| `MetaCyc:G1G01-2697-MONOMER` | 4-oxalomesaconate tautomerase | participants |
| `MetaCyc:G1G01-2698-MONOMER` | 4-hydroxy-4-methyl-2-oxoglutarate aldolase aldolase | participants |
| `MetaCyc:G1G01-2699-MONOMER` | 4-oxalmesaconate hydratase monomer | participants |
| `MetaCyc:GALLATE-DEGRADATION-I-PWY` | gallate degradation II | pathway |
| `MetaCyc:MONOMER-10723` | 2-pyrone-4,6-dicarboxylate hydrolase | participants |
| `MetaCyc:MONOMER-3182` | 2-pyrone-4,6-dicarboxylate hydrolase | participants |
| `MetaCyc:MONOMER-3183` | 4-carboxy-2-hydroxymuconate hydratase | participants |
| `MetaCyc:MONOMER-3184` | HMG aldolase monomer | participants |
| `MetaCyc:MONOMER-3185` | protocatechuate 3,4-dioxygenase β subunit | participants |
| `MetaCyc:MONOMER-3186` | protocatechuate 3,4-dioxygenase α subunit | participants |
| `MetaCyc:MONOMER-3243` | subunit of 4-oxalomesaconate hydratase | participants |
| `MetaCyc:MONOMER-3244` | 4-oxalocitramalate aldolase subunit | participants |
| `MetaCyc:MONOMER-3463` | 2-pyrone-4,6-dicarboxylate hydrolase | participants |
| `MetaCyc:MONOMER-3467` | 2-pyrone-4,6-dicarboxylate hydrolase | participants |
| `MetaCyc:MONOMER-3468` | 4-oxalomesaconate hydratase monomer | participants |
| `MetaCyc:MONOMER-3469` | LigK | participants |
| `MetaCyc:MONOMER-3481` | subunit of 4-hydroxy-4-methyl-2-oxoglutarate aldolase | participants |
| `MetaCyc:OXALODECARB-RXN` | EC 4.1.1.112 | reactions |
| `MetaCyc:PROTOCATECHUATE-34-DIOXYGENASE-RXN` | EC 1.13.11.3 | reactions |
| `MetaCyc:RXN-11861` | gallate 3,4-dioxygenation to PDC | reactions |
| `MetaCyc:RXN-12074` | EC 4.1.3.17 | reactions |
| `MetaCyc:TCA` | TCA cycle I (prokaryotic) | reactions |
| `NCBIProtein:BAI50711.1` | 4-oxalomesaconate hydratase [Comamonas sp. E6] | participants |
| `NCBITaxon:303` | Pseudomonas putida | taxa |
| `PubChem:6098323` | Lithium potassium acetyl phosphate (1/1/1) | participants |
| `RHEA:10645` | PDC hydrolysis | reactions |
| `RHEA:17403` | formal E,E enol hydration to CHA | reactions |
| `RHEA:18170` | 4-hydroxy-2-oxoglutarate => glyoxylate + pyruvate | reactions |
| `RHEA:28932` | keto OMA to formal E,E enol | reactions |
| `RHEA:28936` | CHA aldol cleavage | reactions |

### Local reference identifiers

**MetaCyc**: `MetaCyc:4.1.3.17-RXN`, `MetaCyc:CPLX-2721`, `MetaCyc:CPLX-2781`, `MetaCyc:CPLX-2782`, `MetaCyc:CPLX-2864`, `MetaCyc:CPLX-2865`, `MetaCyc:CPLX-2881`, `MetaCyc:CPLX-7917`, `MetaCyc:CPLX-8178`, `MetaCyc:CPLX1G01-155`, `MetaCyc:ENZRXN-11003`, `MetaCyc:ENZRXN-11041`, `MetaCyc:ENZRXN-16933`, `MetaCyc:ENZRXN-16934`, `MetaCyc:ENZRXN-18362`, `MetaCyc:ENZRXN-18372`, `MetaCyc:ENZRXN-18373`, `MetaCyc:ENZRXN-18617`, `MetaCyc:ENZRXN-3343`, `MetaCyc:ENZRXN-3363`, `MetaCyc:ENZRXN-3364`, `MetaCyc:ENZRXN-3365`, `MetaCyc:ENZRXN-3623`, `MetaCyc:ENZRXN-3625`, `MetaCyc:ENZRXN-3627`, `MetaCyc:ENZRXN-3641`, `MetaCyc:ENZRXN1G01-1112`, `MetaCyc:G1G01-2699-MONOMER`, `MetaCyc:GALLATE-DEGRADATION-I-PWY`, `MetaCyc:OXALODECARB-RXN`, `MetaCyc:REG-10400`, `MetaCyc:REG-10401`, `MetaCyc:REG-10724`, `MetaCyc:REG-12626`, `MetaCyc:REG-12629`, `MetaCyc:REG-12637`, `MetaCyc:REG-12669`, `MetaCyc:REG-8378`, `MetaCyc:REG-8379`, `MetaCyc:REG-8380`, `MetaCyc:REG-8394`, `MetaCyc:REG-8395`, `MetaCyc:REG-8396`, `MetaCyc:REG-8397`, `MetaCyc:REG-8398`, `MetaCyc:REG-8402`, `MetaCyc:REG-8403`, `MetaCyc:REG-8404`, `MetaCyc:REG-8405`, `MetaCyc:REG-9531`, `MetaCyc:REG-9532`, `MetaCyc:RXN-11861`, `MetaCyc:RXN-2462`, `MetaCyc:RXN-2463`, `MetaCyc:RXN-2464`, `MetaCyc:RXN-9983`.
**PMID**: `PMID:11092855`, `PMID:1194238`, `PMID:21219457`, `PMID:2229032`, `PMID:2229033`, `PMID:26867578`, `PMID:6841354`, `PMID:7142106`.
**RHEA**: `RHEA:18170`.

### Identifiers added to the authority union

`CHEBI:15356`, `CHEBI:16382`, `CHEBI:17051`, `CHEBI:173437`, `CHEBI:17742`, `CHEBI:17996`, `CHEBI:22629`, `CHEBI:23414`, `CHEBI:30808`, `CHEBI:32139`, `CHEBI:32588`, `CHEBI:3312`, `CHEBI:34887`, `CHEBI:35780`, `CHEBI:44976`, `CHEBI:53351`, `CHEBI:58222`, `CHEBI:58276`, `CHEBI:62843`, `CHEBI:63317`, `CHEBI:747199`, `CHEBI:86228`, `CHEBI:9532`, `MetaCyc:4.1.3.17-RXN`, `MetaCyc:CPLX-2864`, `MetaCyc:GALLATE-DEGRADATION-I-PWY`, `MetaCyc:MONOMER-3183`, `MetaCyc:MONOMER-3468`, `MetaCyc:OXALODECARB-RXN`, `MetaCyc:PROTOCATECHUATE-34-DIOXYGENASE-RXN`, `MetaCyc:RXN-11861`, `MetaCyc:RXN-12074`, `PubChem:6098323`, `RHEA:18170`.

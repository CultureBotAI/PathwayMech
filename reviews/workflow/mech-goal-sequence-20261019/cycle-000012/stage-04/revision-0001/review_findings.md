# Cycle 12 Stage 4 (`record_review`) Findings & Stage 5 Carry-Forward Register

- **Run ID**: `mech-goal-sequence-20261019`
- **Repository**: `CultureBotAI/PathwayMech` (`pathwaymech`)
- **Cycle / Stage / Revision**: Cycle `12`, Stage `4` (`record_review`), Revision `1` (`revision-0001`)
- **Stage Action ID**: `ca56939ca2d904840a8dcf04` / `e7089a79d28f75ad8ddc9a2f`
- **Frozen Inventory Snapshot**: `main` at commit `b3ce30812ac7cf1bb39965a9073a225f5736ee93` (`281` eligible records)
- **Structured Review Bundle**: `reviews/structured/20261105T145000Z-cycle12-stage4-frozen-corpus-cohort-review/review.yaml`
- **Carry-Forward Finding IDs**: `["F-C12S4-001", "F-C12S4-002"]`

---

## 1. Summary of Open Findings (`2` Findings across `10` Distinct Pathway Records)

| Finding ID | Issue Key | Category | Severity | Certainty | Status | Target Records (`10` distinct total) | Affected Field Count | Assigned Follow-Up |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `F-C12S4-001` | `missing-reference-urls-10-records` | `representation` | `minor` | `confirmed` | `open` | `Reactome:R-MTU-868688`, `Reactome:R-MTU-879299`, `Reactome:R-MTU-936721`, `Reactome:R-MTU-936635`, `Reactome:R-MTU-936654`, `Reactome:R-MTU-879325`, `WikiPathways:WP5060`, `WikiPathways:WP5587`, `MIBiG:BGC0002072`, `WikiPathways:WP296` | `47` `references[].url` entries (`12 + 12 + 8 + 5 + 3 + 2 + 2 + 1 + 1 + 1`) | `A-C12S4-001` (Cycle 12 Stage 5 `resolve_review_findings`) |
| `F-C12S4-002` | `placeholder-reactome-and-mibig-reference-titles-4-records` | `representation` | `minor` | `confirmed` | `open` | `Reactome:R-MTU-879299`, `Reactome:R-MTU-868688`, `Reactome:R-MTU-879325`, `MIBiG:BGC0002072` | `13` `references[].title` entries (`6 + 5 + 1 + 1`) | `A-C12S4-002` (Cycle 12 Stage 5 `resolve_review_findings`) |

---

## 2. Detailed Finding Specifications

### `F-C12S4-001` — Missing resolvable `url` on `references[]` entries (`10` records, `47` entries)

- **Issue Key**: `missing-reference-urls-10-records`
- **Category / Severity / Certainty / Status**: `representation` / `minor` / `confirmed` / `open`
- **Assessment ID**: `ASSESS-C12-MISSING-REF-URLS-AND-PLACEHOLDER-TITLES-10`
- **Rule ID**: `CURATION:reference-entries-include-resolvable-url`
- **Evidence IDs**:
  - `EV-C12-MISSING-REF-URLS-10` (`data/pathways/mycobacterium-trehalose-biosynthesis.yaml`, `data/pathways/mycothiol-biosynthesis.yaml`, `data/pathways/mycobacterium-cysteine-synthesis-from-o-acetylserine.yaml`, `data/pathways/mycobacterium-sulfate-assimilation.yaml`, `data/pathways/mycobacterium-cysteine-synthesis-from-o-phosphoserine.yaml`, `data/pathways/mycothiol-catabolism.yaml`, `data/pathways/peptidoglycan-cytoplasmic-synthesis-and-recycling-pathways.yaml`, `data/pathways/2-phenylethanol-biosynthesis.yaml`, `data/pathways/linearmycin-biosynthetic-gene-cluster.yaml`, and `data/pathways/tca-cycle-detailed.yaml`)
- **Affected Records & Exact Field Paths**:
  1. `Reactome:R-MTU-868688` (`data/pathways/mycobacterium-trehalose-biosynthesis.yaml`, `12` entries):
     - `references[0].url` (`id: Reactome:R-MTU-868622`, `title: Reactome reaction R-MTU-868622`)
     - `references[1].url` (`id: Reactome:R-MTU-868608`, `title: Reactome reaction R-MTU-868608`)
     - `references[2].url` (`id: Reactome:R-MTU-868709`, `title: Reactome reaction R-MTU-868709`)
     - `references[3].url` (`id: Reactome:R-MTU-868658`, `title: Reactome reaction R-MTU-868658`)
     - `references[4].url` (`id: Reactome:R-MTU-868657`, `title: Reactome reaction R-MTU-868657`)
     - `references[5].url` (`id: PMID:10658666`, `title: Three pathways for trehalose biosynthesis in mycobacteria`)
     - `references[6].url` (`id: PMID:12473104`, `title: Trehalose-phosphate synthase of Mycobacterium tuberculosis. Cloning, expression and properties of the recombinant enzyme`)
     - `references[7].url` (`id: PMID:15158675`, `title: Cloning and expression of the trehalose-phosphate phosphatase of Mycobacterium tuberculosis: comparison to the enzyme from Mycobacterium smegmatis`)
     - `references[8].url` (`id: PMID:19177348`, `title: Effect of trehalose on protein structure`)
     - `references[9].url` (`id: PMID:15703182`, `title: The OtsAB pathway is essential for trehalose biosynthesis in Mycobacterium tuberculosis`)
     - `references[10].url` (`id: PMID:12626396`, `title: New insights on trehalose: a multifunctional molecule`)
     - `references[11].url` (`id: PMID:15901732`, `title: The crucial role of trehalose and structurally related oligosaccharides in the biosynthesis and transfer of mycolic acids in Corynebacterineae`)
  2. `Reactome:R-MTU-879299` (`data/pathways/mycothiol-biosynthesis.yaml`, `12` entries):
     - `references[0].url` (`id: Reactome:R-MTU-879331`, `title: Reactome reaction R-MTU-879331`)
     - `references[1].url` (`id: Reactome:R-MTU-879298`, `title: Reactome reaction R-MTU-879298`)
     - `references[2].url` (`id: Reactome:R-MTU-879274`, `title: Reactome reaction R-MTU-879274`)
     - `references[3].url` (`id: Reactome:R-MTU-879327`, `title: Reactome reaction R-MTU-879327`)
     - `references[4].url` (`id: Reactome:R-MTU-879319`, `title: Reactome reaction R-MTU-879319`)
     - `references[5].url` (`id: Reactome:R-MTU-879248`, `title: Reactome reaction R-MTU-879248`)
     - `references[6].url` (`id: PMID:14763976`, `title: The Mycobacterium tuberculosis ino1 gene is essential for growth and virulence`)
     - `references[7].url` (`id: PMID:18390549`, `title: Structural and enzymatic analysis of MshA from Corynebacterium glutamicum: substrate-assisted catalysis`)
     - `references[8].url` (`id: PMID:20167072`, `title: Inositol monophosphate phosphatase genes of Mycobacterium tuberculosis`)
     - `references[9].url` (`id: PMID:14556638`, `title: Characterization of Mycobacterium tuberculosis mycothiol S-conjugate amidase`)
     - `references[10].url` (`id: PMID:12033919`, `title: ATP-dependent L-cysteine:1D-myo-inosityl 2-amino-2-deoxy-alpha-D-glucopyranoside ligase, mycothiol biosynthesis enzyme MshC, is related to class I cysteinyl-tRNA synthetases`)
     - `references[11].url` (`id: PMID:12375100`, `title: Identification of the mycothiol synthase gene (mshD) encoding the acetyltransferase producing mycothiol in actinomycetes`)
  3. `Reactome:R-MTU-936721` (`data/pathways/mycobacterium-cysteine-synthesis-from-o-acetylserine.yaml`, `8` entries):
     - `references[0].url` (`id: PMID:12072441`, `title: 5'-adenosinephosphosulfate lies at a metabolic branch point in mycobacteria`)
     - `references[1].url` (`id: PMID:16008502`, `title: A conserved mechanism for sulfonucleotide reduction`)
     - `references[2].url` (`id: PMID:17644602`, `title: Sulfite reduction in mycobacteria`)
     - `references[3].url` (`id: PMID:15917234`, `title: Siroheme- and [Fe4-S4]-dependent NirA from Mycobacterium tuberculosis is a sulfite reductase with a covalent Cys-Tyr bond in the active site`)
     - `references[4].url` (`id: PMID:17567578`, `title: Structural insights into catalysis and inhibition of O-acetylserine sulfhydrylase from Mycobacterium tuberculosis. Crystal structures of the enzyme alpha-aminoacrylate intermediate and an enzyme-inhibitor complex`)
     - `references[5].url` (`id: PMID:16436075`, `title: Functional analysis of L-serine O-acetyltransferase from Corynebacterium glutamicum`)
     - `references[6].url` (`id: PMID:19376862`, `title: Functional genomics reveals extended roles of the Mycobacterium tuberculosis stress response factor sigmaH`)
     - `references[7].url` (`id: PMID:17970225`, `title: Drug targets in mycobacterial sulfur metabolism`)
  4. `Reactome:R-MTU-936635` (`data/pathways/mycobacterium-sulfate-assimilation.yaml`, `5` entries):
     - `references[0].url` (`id: PMID:11929522`, `title: Functional genomics reveals the sole sulphate transporter of the Mycobacterium tuberculosis complex and its relevance to the acquisition of sulphur in vivo`)
     - `references[1].url` (`id: PMID:15184554`, `title: The Mycobacterium tuberculosis cysD and cysNC genes form a stress-induced operon that encodes a tri-functional sulfate-activating complex`)
     - `references[2].url` (`id: PMID:15615729`, `title: The trifunctional sulfate-activating complex (SAC) of Mycobacterium tuberculosis`)
     - `references[3].url` (`id: PMID:18454554`, `title: Rv2131c from Mycobacterium tuberculosis is a CysQ 3'-phosphoadenosine-5'-phosphatase`)
     - `references[4].url` (`id: PMID:17970225`, `title: Drug targets in mycobacterial sulfur metabolism`)
  5. `Reactome:R-MTU-936654` (`data/pathways/mycobacterium-cysteine-synthesis-from-o-phosphoserine.yaml`, `3` entries):
     - `references[0].url` (`id: PMID:16104727`, `title: Reconstitution of a new cysteine biosynthetic pathway in Mycobacterium tuberculosis`)
     - `references[1].url` (`id: PMID:18842002`, `title: O-phospho-L-serine and the thiocarboxylated sulfur carrier protein CysO-COSH are substrates for CysM, a cysteine synthase from Mycobacterium tuberculosis`)
     - `references[2].url` (`id: PMID:18799456`, `title: Cysteine synthase (CysM) of Mycobacterium tuberculosis is an O-phosphoserine sulfhydrylase: evidence for an alternative cysteine biosynthesis pathway in mycobacteria`)
  6. `Reactome:R-MTU-879325` (`data/pathways/mycothiol-catabolism.yaml`, `2` entries):
     - `references[0].url` (`id: Reactome:R-MTU-879281`, `title: Reactome reaction R-MTU-879281`)
     - `references[1].url` (`id: PMID:14556638`, `title: Characterization of Mycobacterium tuberculosis mycothiol S-conjugate amidase`)
  7. `WikiPathways:WP5060` (`data/pathways/peptidoglycan-cytoplasmic-synthesis-and-recycling-pathways.yaml`, `2` entries):
     - `references[0].url` (`id: PMID:31296364`, `title: Bacteria's different ways to recycle their own cell wall`)
     - `references[1].url` (`id: PMID:18266853`, `title: Cytoplasmic steps of peptidoglycan biosynthesis`)
  8. `WikiPathways:WP5587` (`data/pathways/2-phenylethanol-biosynthesis.yaml`, `1` entry):
     - `references[0].url` (`id: PMID:40724265`, `title: Screening of High-Yield 2-Phenylethanol Producing Strain from Wild-Type Saccharomyces cerevisiae and Optimization of Fermentation Parameters`)
  9. `MIBiG:BGC0002072` (`data/pathways/linearmycin-biosynthetic-gene-cluster.yaml`, `1` entry):
     - `references[0].url` (`id: PMID:29348524`, `title: MIBiG literature reference PMID:29348524`)
  10. `WikiPathways:WP296` (`data/pathways/tca-cycle-detailed.yaml`, `1` entry):
     - `references[0].url` (`id: CHEBI:30744`, `title: ChEBI oxaloacetic acid JSON API record`)
- **Proposed Remediation (`A-C12S4-001` for Cycle 12 Stage 5)**:
  - Populate canonical resolvable `url` values across all `47` `references[]` entries (`https://pubmed.ncbi.nlm.nih.gov/<pmid>/` for `34` `PMID:*` entries, `https://reactome.org/content/detail/<id>` for `12` `Reactome:*` entries, and `https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:30744` for `CHEBI:30744`), record curation history entries under `history/records/<slug>/`, and refresh rendered pages (`pathwaymech-render-pages`).

---

### `F-C12S4-002` — Generic placeholder `references[].title` strings on Reactome reaction and MIBiG literature references (`4` records, `13` entries)

- **Issue Key**: `placeholder-reactome-and-mibig-reference-titles-4-records`
- **Category / Severity / Certainty / Status**: `representation` / `minor` / `confirmed` / `open`
- **Assessment ID**: `ASSESS-C12-MISSING-REF-URLS-AND-PLACEHOLDER-TITLES-10`
- **Rule ID**: `CURATION:no-placeholder-reference-titles`
- **Evidence IDs**:
  - `EV-C12-PLACEHOLDER-REF-TITLES-4` (`data/pathways/mycothiol-biosynthesis.yaml`, `data/pathways/mycobacterium-trehalose-biosynthesis.yaml`, `data/pathways/mycothiol-catabolism.yaml`, and `data/pathways/linearmycin-biosynthetic-gene-cluster.yaml`)
- **Affected Records & Exact Field Paths**:
  1. `Reactome:R-MTU-879299` (`data/pathways/mycothiol-biosynthesis.yaml`, `6` entries):
     - `references[0].title` (`id: Reactome:R-MTU-879331`, current `title: Reactome reaction R-MTU-879331`)
     - `references[1].title` (`id: Reactome:R-MTU-879298`, current `title: Reactome reaction R-MTU-879298`)
     - `references[2].title` (`id: Reactome:R-MTU-879274`, current `title: Reactome reaction R-MTU-879274`)
     - `references[3].title` (`id: Reactome:R-MTU-879327`, current `title: Reactome reaction R-MTU-879327`)
     - `references[4].title` (`id: Reactome:R-MTU-879319`, current `title: Reactome reaction R-MTU-879319`)
     - `references[5].title` (`id: Reactome:R-MTU-879248`, current `title: Reactome reaction R-MTU-879248`)
  2. `Reactome:R-MTU-868688` (`data/pathways/mycobacterium-trehalose-biosynthesis.yaml`, `5` entries):
     - `references[0].title` (`id: Reactome:R-MTU-868622`, current `title: Reactome reaction R-MTU-868622`)
     - `references[1].title` (`id: Reactome:R-MTU-868608`, current `title: Reactome reaction R-MTU-868608`)
     - `references[2].title` (`id: Reactome:R-MTU-868709`, current `title: Reactome reaction R-MTU-868709`)
     - `references[3].title` (`id: Reactome:R-MTU-868658`, current `title: Reactome reaction R-MTU-868658`)
     - `references[4].title` (`id: Reactome:R-MTU-868657`, current `title: Reactome reaction R-MTU-868657`)
  3. `Reactome:R-MTU-879325` (`data/pathways/mycothiol-catabolism.yaml`, `1` entry):
     - `references[0].title` (`id: Reactome:R-MTU-879281`, current `title: Reactome reaction R-MTU-879281`)
  4. `MIBiG:BGC0002072` (`data/pathways/linearmycin-biosynthetic-gene-cluster.yaml`, `1` entry):
     - `references[0].title` (`id: PMID:29348524`, current `title: MIBiG literature reference PMID:29348524`)
- **Proposed Remediation (`A-C12S4-002` for Cycle 12 Stage 5)**:
  - Replace the `13` generic placeholder `references[].title` strings across `Reactome:R-MTU-879299`, `Reactome:R-MTU-868688`, `Reactome:R-MTU-879325`, and `MIBiG:BGC0002072` with descriptive Reactome reaction titles (`<reaction label> (<reference_id>)`) and the verified PubMed article title for `PMID:29348524`, record curation history entries under `history/records/<slug>/`, and refresh rendered pages (`pathwaymech-render-pages`).

---

## 3. Prior Findings Verified Resolved in Cycle 11 Stage 5 (`#792` / `#791`)

- **`F-C11S4-001`** (`raw-local-id-structured-metacyc-reference-titles-4-records`, `4` records: `MetaCyc:BIOTIN-BIOSYNTHESIS-PWY`, `MetaCyc:PWY-6823`, `MetaCyc:CALVIN-PWY`, and `MetaCyc:THISYN-PWY`, `79` `references[].title` entries): Verified `resolved` (`0` remaining raw `local_id` reference titles across all `7,132` references in the 281-record corpus).
- **`F-C11S4-002`** (`raw-local-id-metacyc-reaction-labels-7-metacyc-records`, `7` records: `MetaCyc:PWY0-321`, `MetaCyc:P321-PWY`, `MetaCyc:CENTBENZCOA-PWY`, `MetaCyc:PWY0-1477`, `MetaCyc:METH-ACETATE-PWY`, `MetaCyc:METHANOGENESIS-PWY`, and `MetaCyc:PWY-5177`, `49` `reactions[].label` entries): Verified `resolved` (`16` `source_context`-eligible reaction labels updated in YAML + `33` `native_roles` reaction labels verified as authority-locked frame-only fallbacks in `20261105T054000Z-cycle11-stage5-resolve-review-findings`).

# L-carnitine degradation I: curation receipt

The maintained record is [l-carnitine-degradation-i.yaml](../../../data/pathways/l-carnitine-degradation-i.yaml), identified by **PathBank:SMP0002051**. It represents the four-reaction anaerobic CoA-linked route in native `PW002037.owl`, with current reviewed E. coli K-12 CaiC, CaiD, CaiA and CaiB protein identities. It contains 19 participants, four directed reactions and 32 edges. This receipt records author research and narrow checks; an independent scientific review and the integrated repository gates are separate.

## Novelty and boundary

Before authoring, both the new worktree and the original repository were searched with `rg -uu -n -i`, including hidden and ignored content. The search excluded `.git`, `.venv`, and generated `pages`, `output` and `build` trees; it included research and ignored source material. Original repository: `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/PathwayMech`. New worktree: `/private/tmp/pathwaymech-carnitine-putrescine-20261010`, base `5766cf2fe227afc248a72e455f74f4c5ddda9d97`.

The first exact pattern was `SMP0002051|PW002037|L-carnitine degradation I|carnitine catabol|carnitine degradation|P31552|P31572|P31551|P60584|11551212|15518548`. Each repository returned 11 lines, entirely in the previous candidate inventory, archive screening ledger and next-lead notes. Those records were read. They identified this route as pending investigation, especially its generic redox carriers, rather than a rejected or already maintained pathway. Raw search receipts are `/private/tmp/pathwaymech-carnitine-novelty-{worktree,original}.txt`.

The second pattern was `CARNMET-PWY|carnitine metabolism, CoA-linked|GO:0019254|GO:0042413|RHEA:(28514|28515|28338|28339|51584|51586|28418|28419)|PMID:(18266698|10209289|8060125|12081978)|10\.1021/bi0108812|10\.1021/bi048481c|10\.1111/j\.1365-2672\.2008\.03740`. Both searches returned zero matches within the stated ignored-inclusive scope. Receipts are `/private/tmp/pathwaymech-carnitine-secondary-novelty-{worktree,original}.txt`. This establishes absence of a maintained exact route before this addition; it is not a claim that carnitine biology is absent from every external source.

GO:0019254 denotes CoA-linked carnitine metabolism, which also covers reverse biosynthesis, and GO:0042413 denotes broader carnitine catabolism across routes. The native pathway identity is more exact. The prior Pseudomonas `PW123534.owl` lead describes a distinct aerobic assimilation context with unresolved catalyst assignment and is not merged here.

## Native identity and chemical conflicts

The official primary BioPAX archive is the preserved 2019 Last-Modified artifact downloaded on 2026-10-08, not a claim about the current portal release. Its exact member has one Pathway whose SMPDB URI and xref independently identify SMP0002051, plus the distinct PathWhiz PW002037 xref. All four BiochemicalReaction nodes (`5950–5953`) and their Catalysis nodes are explicit pathway components. Four BiochemicalPathwayStep objects are linked through pathwayOrder, but no nextStep relation is present. The array order is not treated as biochemical chronology.

Each native controller resolves to a reviewed protein accession, or the native CaiB complex and its protein component. Current UniProt reaction annotations independently connect these enzymes to the selected Rhea families. This is a manually justified pathway correspondence, **not a native Rhea cross-reference or an exact chemical mapping**. The complete native graph objects and all dispositions are preserved in [carnitine-source-projection.json](carnitine-source-projection.json).

| Native object | Finding | Maintained treatment |
|---|---|---|
| PW_C040813, displayed as diphosphate | PubChem:3315, formula C34H28N6O14S4 and native structure describe an azo dye. Official PubChem independently confirms the mismatch. | Reject native chemical identity. Rhea28515 and reviewed CaiC independently support CHEBI:33019 diphosphate(3-). |
| PW_C001099, CoA | CHEBI:1146900 was absent as a subject or referenced alternative/replacement in the complete pinned ChEBI255 SQL lookup; native formula is neutral CoA. | Reject this xref; use independently supported Rhea CHEBI:57287 CoA(4-). |
| Three acyl-CoAs, PubChem591/605/726 | Official PubChem records omit stereochemical layers and use different protonation from selected Rhea compounds. Native structure representations also require care rather than an assumed exact match. | Retain native transformation/catalyst context, but independently ground R-carnitinyl-CoA, E-crotonobetainyl-CoA and gamma-butyrobetainyl-CoA in exact Rhea/ChEBI forms. |
| Native ATP and AMP | Neutral source forms differ from Rhea ATP(4-) and AMP(2-). | Preserve difference explicitly, without exactMatch. |
| Generic237/227 | Native SmallMolecule objects named reduced/oxidized electron acceptor have no identity xrefs. | Do not equate those source objects to an ETF. Independently retain exact whole Rhea ETF state identifiers. |

Native water, R-carnitine and gamma-butyrobetaine ChEBI identities agree with the selected forms. The graph contains every selected Rhea side, including water, hydron and the two carrier states. All 18 side occurrences have native Rhea `contains1`; no coefficient is inferred merely from an identifier in the participant list.

## Mechanism and evidence limits

| Native step | Maintained directed Rhea | Interpretation |
|---|---|---|
| 5950 / CaiC P31552 | 28515, left to right | ATP-dependent initial carnitinyl-CoA formation from L-carnitine and CoA. |
| 5951 / CaiD P31551 | 28339, left to right | Carnitinyl-CoA dehydration to crotonobetainyl-CoA and water. |
| 5952 / CaiA P60584 | 51586, right to left relative to master51584 | Reduction to gamma-butyrobetainyl-CoA with the generic reduced ETF state; oxidized ETF and hydron are products. |
| 5953 / CaiB P31572 homodimer | 28419, left to right | CoA transfer to a fresh carnitine molecule, releasing gamma-butyrobetaine and regenerating carnitinyl-CoA. |

CaiC supplies an initial activated pool; CaiB closes the recycling loop. The material-flow edge from CaiB back to CaiD prevents the four listed reactions from being read as one ATP-consuming linear pathway for every turnover. CaiD and CaiB are characterized as reversible; the selected directed IDs express the catabolic presentation, not irreversibility. The primary CaiB/CaiD paper studied the reversible synthesis direction, and the current curated enzyme annotations explicitly support the reverse chemistry.

Rhea release142 defines `RHEA-COMP:10685` and `10686` as **whole generic electron-transfer flavoprotein states**. Their reactive flavin parts are not substituted for the carrier. Current UniProt P60584 explicitly cross-references both component identifiers. The FAD cofactor of CaiA is separately supported by its COFACTOR annotation and the original CaiA component-II study: one bound FAD per subunit. The record does not identify the generic ETF with an exact FixA/FixB protein complex. The [fixA/fixB mutant study](https://pubmed.ncbi.nlm.nih.gov/12081978/) establishes genetic necessity for anaerobic carnitine reduction and proposes electron provision; it does not establish direct transfer by a precisely identified stoichiometric donor complex.

The native CaiB complex `PathBank:SMP0002051/ProteinComplex/4010` contains two copies of P31572. The original [CaiB crystal structure](https://pubmed.ncbi.nlm.nih.gov/15518548/) and reviewed SUBUNIT annotation independently support a homodimer. The CaiD homotrimer and CaiA homotetramer annotations are retained in catalytic descriptions without inventing new native complex IDs. The historical 1999 assay association of a CaiB dimer with a CaiA tetramer is not promoted into an independently identified complex for the precise modern thioester reaction. Its “unknown low-molecular-mass cofactor” was subsequently identified as gamma-butyrobetainyl-CoA, an intermediate already represented, not a second prosthetic cofactor.

All four reviewed protein records have K-12 taxon83333. Several older primary experiments instead used O44 K74 or overexpression strains. Thus K-12 is the curated protein provenance, not a claim that all cited experiments used K-12, that every K-12 strain expresses the pathway, or that carnitine supports universal growth. The CaiF paper describes a laboratory-strain regulatory defect. The earlier free-carnitine dehydratase/racemase assignments were superseded by direct CoA-thioester chemistry and are not imported. Neither induction changes nor historical coupled-assay inhibitor data become generalized direct inhibition edges.

Nine original article abstracts were inspected through Europe PMC core records: PMID18266698,11551212,15518548,10209289,12081978,10978161,8060125,8631699,7815937. Four short verbatim excerpts support narrow enzyme/assembly/cofactor claims; the remaining evidence preserves current structured database assertions, exact locators and source evidence codes. The PMC135185 BioC response was HTML help/error content despite HTTP200, and the Europe PMC full-text request failed with HTTP500. Both are recorded as rejected/failed retrievals. **No full-text figure, table or methods inspection is claimed.** The exact reaction chemistry rests on inspected current authoritative records with primary abstract support.

## Context deliberately excluded

Other CaiC substrates, CaiD crotonyl-CoA activity and CaiB crotonobetaine transfer lie outside this exact four-reaction route. Transport by CaiT, CaiF regulation, CaiE function, expression regulation and alternative aerobic assimilation are not added. CaiB-bound crystallization buffer is not a cofactor. No free-magnesium cofactor edge is inferred from ATP chemistry or an assay condition. No compartment node is guessed from a subcellular-location code.

The root's canonical iModulonDB query `imodulondb search --organism e_coli --dataset precise_mg1655 --query cai` succeeded and returned nine gene hits, zero iModulons. CaiA/B/C/D match the target enzymes; CaiE/F/T are adjacent context, while **ycaI and wcaI are substring false positives**. No coexpression module or regulatory edge is inferred. Raw output: `/private/tmp/pathwaymech-carnitine-putrescine-imodulondb-cai.md`.

## Reproduction and verification

[carnitine-source-manifest.json](carnitine-source-manifest.json) preserves URLs, retrieval timestamps, release metadata and exact byte/hash scopes. Native member hashes are uncompressed XML member bytes; the Rhea source hash is the downloaded compressed gzip; UniProt/Europe PMC/PubChem hashes are exact response-body bytes. No session or cookie headers are retained. Mechanistic Rhea142 is distinct from the previously pinned Rhea139 identity ontology. The existing ChEBI255, GO2026-07-26 and NCBITaxon2026-07-12 Semantic SQL authorities were used for identity and scope checks; root owns the reproducible additive authority refresh.

All 25 named identifiers, local reference identifiers and paper DOIs are listed in [carnitine-identifiers.json](carnitine-identifiers.json). Raw sources and narrow scripts are retained externally at `/private/tmp/pathwaymech-carnitine-putrescine-evidence/carnitine`. [carnitine-validation.json](carnitine-validation.json) records native/closed schema, all Rhea directions/sides/coefficients, raw native membership/controller/assembly checks, literal abstract quotes, protein provenance, source-body hashes and actual target KGX export. Integrated rendering, identifier snapshots, full tests/lint and immutable independent review remain root-owned steps; this author receipt does not substitute for them.

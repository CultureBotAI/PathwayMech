# Next251 primary handoff

Use `proposed-edges.json` with `claim-ledger.json`, `primary-metadata.json`, `reading-coverage.json`, and `source-artifacts.json`. These are external research proposals; no repository files were edited.

The complete U2 route is the strongest anchor. Keep the C.glutamicum and NyZ101 thiol variants separate and carry their N-terminal His6 construct qualifiers on every assay endpoint. BagL accepts cysteine, Cys-Gly, and glutathione in vitro. Preserve Table2 concentration/kinetic distinctions instead of asserting cysteine exclusivity.

Metal activity changes support explicitly qualified perturbation edges. They do not establish physiological metal-cofactor identity. Leave EDTA in descriptive evidence. Assembly claims require the separate tagged/deposited construct limits in the ledger.

Identity closure from the native agent is in `/private/tmp/pathwaymech-next-251-native-20261014/variant-protein-identity.json`: H6TG59 = ADZ54051.1 = HQ897158.1 bagL (162aa,tax980079); Q8NLC1 = NP_602215.1 = BAC00415.1 (241aa,tax196627). The latter exact241aa occurs after the20aa tag in PDB2NSF. Do not impose that2007 full tag on the2006 construct.

No complete paper PDF/HTML was successfully saved as a raw original. Full publisher HTML was actually read for U2 and NyZ101, and author-uploaded full-paper parsed text for Feng2006; the manifest distinguishes these from saved figure/deposition/abstract artifacts. All twelve U2/NyZ101 figure images were downloaded, hashed, and visually inspected. Feng2006 figure legends/tables were read but figure images were not visually inspected. Other reading and supplement limits are explicit in `reading-coverage.json`.

Four misleading `.pdf`/`.html` responses were browser challenges, now quarantined under `failed-responses/` and marked invalid source documents. BioC JSON retry also returned429; do not represent it as full text.

Four additional explicitly typed web-tool extracted-text artifacts are saved under `derived/`, each with URL/request, retrieval time, byte count and SHA256 in its metadata sidecar and source manifest. They preserve inspected evidence sections; they are not raw article originals or necessarily full paper text. Claim bindings distinguish them from PubMed abstracts.

Native agent independently confirmed PDB2JL4 contains exactly N-terminal Lys + full212aa O86043; PDB2V6K instead contains N-terminal Ala-Lys + full212aa. Both are deposited dimeric assemblies; qualify any such edge as the corresponding deposited construct. See native `u2-nagl-assembly-identity.json`.

Metadata correction: the PMID-to-PMC mappings in `primary-metadata.json` were rebuilt from each record’s direct `PubmedData/ArticleIdList/ArticleId`, excluding cited-reference identifiers. Five PMCIDs and all twelve previously truncated page ranges were corrected; all DOI, title, author, date, journal, volume, and issue fields match the saved original. See `metadata-correction-audit.json`.

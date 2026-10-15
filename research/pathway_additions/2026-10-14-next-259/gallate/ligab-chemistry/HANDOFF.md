# LigAB five-inhibitor chemical identity supplement

This is new external author research, not an independent review, maintained edit or authority promotion. Every earlier frozen package is unchanged.

All five organic inhibitors in the 2013 LigAB Table2 PCA assay have exact issuing ChEBI identities matching the paper's FigureS2 structures:

| Primary compound / canonical ChEBI label | Proposed endpoint | Formula | Net charge | Table2 inhibition |
|---|---|---|---|---|
| 2,3,4-trihydroxybenzoic acid | CHEBI:88714 | C7H6O5 | 0 | 95% |
| 2,3-dihydroxybenzoic acid | CHEBI:18026 | C7H6O4 | 0 | 36% |
| 4-nitrocatechol | CHEBI:16318 | C6H5NO4 | 0 | 31% |
| 4-methylcatechol | CHEBI:17254 | C7H8O2 | 0 | 28% |
| 3-methoxycatechol | CHEBI:141700 | C7H8O3 | 0 | 26% |

The original ACS supplement PDF was copied after rehashing, together with its original FigureS2 page render. All five red structures were visually inspected. The ring positions and substituents were independently reconstructed as atom/bond graphs; they were not copied from issuing SMILES. The primary drawing explicitly uses CO2H for both benzoic acids. Phenolic hydroxyls and the methoxy/methyl groups are also explicit. The nitro group uses the conventional N+/O− resonance representation in the reconstructed graph, with net charge zero; this is not a nitrocatecholate assignment.

Five fresh ChEBI public compound JSON originals were downloaded before parsing. The four new IDs were discovered through public source links and then verified against their own issuing records; the already-known 4-nitrocatechol original was separately reused/hash-bound and freshly reacquired. Current JSON, the complete pinned ChEBI255 database and independently reconstructed primary graphs agree in canonical name, full InChI, InChIKey, formula, net charge and canonical graph connectivity. Current and pinned issuing SMILES both round-trip to the same graph. Each graph is one component with no unresolved stereocentre. `chemical-identity-closure.json` retains the complete checks, graph arrays, precise figure positions and source bindings; individual reconstructed MOL files are under `projections/`.

These endpoints identify the named and drawn neutral parent compounds. They do **not** establish a supplied salt, the predominant solution or bound microspecies at pH7.5, or inhibition of gallate flux. The assays measured PCA-dependent oxygen consumption with500micromolarPCA,1mM inhibitor,3–7nMLigAB,air-saturated50mMTris,pH7.5,25C. Preserve the synthetic construct, thrombin-cleaved preparation and all assay conditions from the source-author proposals. No competitive Ki or physiological regulatory mechanism is inferred.

The 2,3,4-trihydroxybenzoic acid drawing labels94.7% whereas Table2 rounds to95%; this is retained and does not change identity. Do not substitute gallate, another positional hydroxybenzoic acid isomer, a conjugate base or a salt. In particular, the issuing 2,3-dihydroxybenzoic acid record distinguishes conjugate-base CHEBI:36654; that anion is not the neutral acid drawn in this paper.

`participant-proposals.json` supplies the five exact IDs, canonical labels and small-molecule categories. `five-regulatory-edge-proposals.json` is an identity-completed **replacement view** of R11–R15 from the existing author package. It adds chemical subjects and the neutral-parent boundary, and adapts the citation key to PMID:23977959. It does not add duplicate edges or a new quotation allocation: these are the same five edges already included in the 2013 package's25-word total. `issuing-reference-proposals.json` supplies optional independent identity citations; it does not replace the primary inhibition evidence.

The pinned ChEBI255 original remains at `/private/tmp/pathwaymech-curation-authorities/chebi.db`; its full byte digest was independently checked against the existing provenance: `26ad4890cdcf6ee357760d815dfee8f5ba81e0873e62cb379369b04205722b0f`. `pinned-original-binding.json` records that shared original without duplicating the large database. `projections/pinned-five-compound-triples.json` retains every direct statement for the five selected compounds. The current maintained authority exact-key inventory is recorded separately; normal root-owned extraction and review remain required. No missing-ID exception or authority edit was made.

The initial network attempt had sandbox DNS failures. A normal public retry retrieved all five records with HTTP200; both acquisition receipts are retained. No challenge bypass or authenticated source access was used. `verification.json`, `proposal-shape-verification.json`, the original/reuse receipts and `manifest.json` provide technical checks and final hashes. Those checks are not scientific approval.

# Complete protocatechuate ortho branch chemistry

Author support, not independent final review. No maintained files edited.

`draft-chemistry.json` contains ready record fields: nine canonical-label chemicals, four complete reactions, 22 edges (15 sides, four memberships, three material joins), and 11 references. Parent is GO:0019618. Root must retain the independently established GO/native scope bridge and add supported catalyst/taxon context and downstream interface. The draft does not invent a fifth step.

Selected reactions:

1. RHEA:10085, left_to_right: protocatechuate(-1) + O2 → 3-carboxy-cis,cis-muconate(3-) + **2 H+**.
2. **MetaCyc:5.5.1.2-RXN**, right_to_left: 3-carboxy-cis,cis-muconate(3-) + H+ → (R)-carboxymuconolactone(2-).
3. RHEA:23349, left_to_right: (R)-carboxymuconolactone(2-) + H+ → 3-oxoadipate enol-lactone(-1) + CO2.
4. RHEA:10185, left_to_right: 3-oxoadipate enol-lactone(-1) + H2O → 3-oxoadipate(2-) + H+.

Each complete equation conserves atoms and charge. All coefficients are one except the two protons produced by reaction 1. Calculated net: protocatechuate(-1) + O2 + H2O → 3-oxoadipate(2-) + CO2 + H+; not an extra elementary reaction.

Critical resolved mismatch: native 5.5.1.2-RXN outputs CPD-7737 = CHEBI:58771, the R lactone. Native RHEA:23658 cross-reference uses generic stereochemically unspecified CHEBI:57979. Entire Rhea142 reverse object graph from CHEBI:58771 reaches only the decarboxylase family23348, proving no exact R-lactone cycloisomerase in that release. Use the existing exact native reaction identifier and the native RIGHT-TO-LEFT direction. Do not replace the intermediate or use the generic Rhea identity. All four native steps remain complete.

All nine native full InChIs, formulas, charges and complete CML atom/bond graphs agree with pinned ChEBI255 and freshly acquired issuing JSON. Native protocatechuate, 3-carboxymuconate and 3-oxoadipate SMILES are generic placeholders; complete CML and InChI close them. Pinned CHEBI:57496 SMILES loses defined double-bond stereo, while pinned full InChI and current issuing SMILES retain the complete cis,cis identity. R lactone CHEBI:58771 has full /t7-/m0/s1 stereo. Native CML coordinates are not interpreted as an independent absolute stereo assignment.

KEGG C00230/C01163/C03586/C00846 are neutral forms matching the complete InChI except protonation. KEGG C01278 is neutral **and stereo-unspecified**; it is not exact R lactone identity. Do not promote these route cross-references to exact charged chemistry.

New core authority terms relative to inspected base: RHEA:10085, MetaCyc:5.5.1.2-RXN, RHEA:23349, CHEBI:57496, CHEBI:58771. CHEBI:36241 already exists. Canonical labels in required-identifiers.tsv.

Full chemical-identity-closure.json, author-handoff.json, original Rhea traversal, stereospecific search proof, and artifact-manifest.json retain reproducible locators and digests. All raw XML/JSON/MOL/flatfile originals remain external in originals/. Full Rhea142 RDF/TSV are reused from /private/tmp/pathwaymech-curation-authorities; their hashes were freshly calculated. Pinned multi-GB SQL stores were opened read-only, and existing provenance hashes inspected rather than freshly recomputed. Current ChEBI/Rhea142 evidence does not upgrade canonical ChEBI255/Rhea139 authority provenance.

The native pathway miscites unrelated PMID:916393 and PMID:761399. No scientific claim here relies on them. Catalyst, cofactor, taxon/strain and complete primary-paper stereochemistry reading remain separate author/reviewer tasks.

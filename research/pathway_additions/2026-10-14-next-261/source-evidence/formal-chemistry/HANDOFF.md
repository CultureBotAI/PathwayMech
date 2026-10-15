# Catechol degradation I: formal chemistry author handoff

Candidate **MetaCyc:PWY-5415** is the five-step catechol meta-cleavage route. This is root-authored source chemistry, not a final independent review or a maintained pathway addition.

All **16 complete META27.0 compounds** (14 formal compounds plus the distinct E-enol and keto comparators) match issuing ChEBI full InChI, full InChIKey, atom counts, charge and complete native CML connectivity versus issuing SMILES. Stereo is compared through exact full source-issued identifiers; it is not inferred from labels, CML connectivity alone, or historical assay preparations. The complete pinned 4,137,340,928-byte ChEBI SQL file was hashed before and after read-only queries and remained unchanged. Seven common-compound originals were freshly retrieved; NAD/NADH/FORMATE and six intake originals were reused by exact hashes. Earlier inspected META22.5 common-compound files were excluded from the selected calculation.

| Native step | Proposed exact formal ID | Selected traversal |
|---|---|---|
| CATECHOL-23-DIOXYGENASE-RXN | RHEA:17338 | left to right |
| 3.7.1.9-RXN | MetaCyc:3.7.1.9-RXN | left to right |
| 2-OXOPENT-4-ENOATE-HYDRATASE-RXN | RHEA:22582 | right to left relative to its master equation |
| MHPELY-RXN | RHEA:22625 | left to right; native reversible annotation retained |
| ACETALD-DEHYDROG-RXN | RHEA:23289 | left to right; native reversible annotation retained |

The original Rhea142 RDF and direction table were fully hash-bound. All20 family members and their complete sides/participants/compound nodes were traversed, preserving repeated subject fragments. Four selected directional equations exactly match the formal native material sets. **The hydrolase cross-reference does not match**: MetaCyc3.7.1.9-RXN produces CPD14447/CHEBI67152 (2Z enol), whereas linked Rhea14552/family14549 produces CHEBI11641 (keto). Both are balanced but are distinct compounds. Retain the native reaction ID for the formal enol route; keep the Rhea keto definition as explicitly conflicting context. This is not a license to infer initial-product stereochemistry from the historical assay literature.

All **21 material-side facts**, five reactions and the summed route balance. The calculated net is catechol + O2 +2H2O +CoA(4−) +NAD(1−) → formate +pyruvate +acetyl-CoA(4−) +NADH(2−) +3H+. Each side has C48H68N14O36P5S and charge−5. This is a bookkeeping calculation, not an added elementary reaction or measured flux.

The three-carbon/terminal intermediates preserve their exact forms: native CPD14447 is CHEBI67152 2Z enol; CPD6761 is CHEBI60886 2E enol; OXOPENTENOATE is CHEBI11641 keto. Ring-cleavage product is CHEBI71198 (2Z,4E), and formal hydroxyketopentanoate is CHEBI73143 S. Primary authoring must preserve unresolved preparation-specific stereo/product forms. The oxidative sibling PWY5420 remains separate.

`formal-chemistry-verification.json` contains the complete structural and balance calculations; `formal-source-projection.json` retains exact issuing RDF fragments and full native reaction slots; `material-facts.json` gives21 source-located statements under400characters. No verbatim paper quotation was used. `current-compound-acquisition.json` retains all fresh original response metadata. The failed first calculation attempt was an incomplete external RDKit environment, before any science output; the successful isolated pinned runtime and original failure log are both preserved.

This package closes formal-route chemistry only. Native biology/assemblies/evidence, primary preparations and chemical regulators/additional assay substrates are separate scopes. The complete22 native chemical-endpoint handoff still requires selection-specific issuing identity checks for any additional graph nodes. No whole-route taxon assignment, catalytic preparation equivalence, physiological irreversibility or equilibrium is inferred here. Full integration, record authorities, gates, saved reviews and publication remain future work.

# Additional enzyme-context chemicals for PWY-5417

This root-authored supplement verifies eight chemical identities needed by the full catechol ortho-cleavage record. It is not an independent review or an approval of an inhibitor target, effect sign, or assay interpretation.

| Native chemical | Exact selected identity |
| --- | --- |
| MN+2 | CHEBI:29035 manganese(2+) |
| ZN+2 | CHEBI:29105 zinc(2+) |
| CU+2 | CHEBI:29036 copper(2+) |
| NADH | CHEBI:57945 NADH(2-) |
| CPD-621 | CHEBI:57712 2-hydroxy-3-oxoadipate(2-) |
| CPD-8827 | CHEBI:149587 2-chloro-3-oxoadipate |
| EDTA | CHEBI:64755 EDTA(2-) |
| CPD-8828 | PubChem:25240959 5-chloro-4-oxopentanoate |

Six ChEBI bodies and the PubChem property response were acquired successfully from the exact issuing APIs. The complete NADH ChEBI and native XML originals were reused byte-for-byte from the frozen262 chemistry package. Seven other native XML originals are exact copies of frozen263 native inputs. `acquisition.json`, `native-input-bindings.json` and the complete input manifests preserve original acquisition and reuse provenance.

`verification.json` records full native/issuing InChI and InChIKey equality for every chemical, reconstruction of every native CML connectivity/formula/charge, and issuing structure replay with RDKit 2026.03.5. CML is not used to infer stereochemistry. The two substituted oxoadipates retain unspecified stereocenters. RDKit's proton-normalization and undefined-stereochemistry messages are expected for these explicitly represented InChIs; no stereoisomer is invented.

These are enzyme-context chemicals, not extra formal route reactions. Ion endpoints retain the actual CuSO4 or ZnCl2 reagent in the primary assay description. Defined chemical protonation does not establish measured solution speciation. NADH(2-) is the exact native/ChEBI formal entity, whereas the assay reports NADH without determining charge. EDTA is the native dianion, not an interchangeable neutral acid. The native HCN versus primary NaCN discrepancy is not repaired by adding an HCN inhibition edge.

The three organic analogs belong to the primary transferase inhibition results; their native thiolase assignments are rejected separately in record curation. CcaC EDTA annotations remain native-only where the accessible primary abstract supports metal reactivation but does not mention EDTA. Identity checks alone do not establish these scientific claims.

The compact manifest binds actual original and stored bytes. All XML/request originals are retained losslessly compressed; helpers are inert text. Original absolute paths identify inspected artifacts, while the repository retention map supplies the stored destinations. This package is immutable after its artifact manifest is written.

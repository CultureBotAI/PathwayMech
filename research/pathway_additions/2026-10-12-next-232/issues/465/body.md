Stable finding key: `nad-pnt-topology-locator`

The independent scientific review of the unsealed NAD phosphorylation/dephosphorylation pathway draft (`MetaCyc:NADPHOS-DEPHOS-PWY`, SHA-256 `7631c5290ee2f86d24bac0ab137f5e3ea619492db15cce6b3553cf599fa526da`) found a minor evidence-locator defect in edges `nad-051` and `nad-052`. Their assertions describe cytoplasmic nucleotide-binding domains, but their sole selector addresses the UniProt SUBCELLULAR LOCATION comment, which states only inner-membrane and multi-pass location.

Root independently checked the retained whole issuing originals for [P07001](https://rest.uniprot.org/uniprotkb/P07001.json) (SHA-256 `c1a07fc32905f32101ef2796eabed6bf1f513c52873c924177bbff17a5038633`) and [P0AB67](https://rest.uniprot.org/uniprotkb/P0AB67.json) (`136fea7ee43efb6aad747ba16a85675f19cfb573b83ac625bfcb24cc492a63c7`). Their Topological domain features support cytoplasmic regions 1–401 and 330–462, respectively, with ECO:0000255 inference. This is a provenance-completeness defect; the biological topology is not being rejected.

Acceptance criteria:
- Narrow the location-only evidence assertion to what its selector supports.
- Add exact topological-feature and primary domain-context locators for the additional claim, retaining inference and structural-model limits.
- Preserve the initial target and explicit correction lineage, then independently verify the final sealed target and rendered evidence.

The author reports a correction in progress. Final scientific acceptance, maintained integration, and publication remain pending. This issue does not represent a defect in an already published NAD record.

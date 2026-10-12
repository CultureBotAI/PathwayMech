Independent scientific review of candidate MetaCyc:PWY-8178 found a minor defect in `data/pathways/pentose-phosphate-pathway-non-oxidative-branch-ii.yaml`. The candidate is awaiting integration.

Stable finding key: `pwy8178-ammonium-assay-preparation`

The qualifier says auxiliary-enzyme ammonium sulfate was removed by ultrafiltration. The 2020 Methods instead specify lyophilized rabbit aldolase/GPDH and explain that the earlier ammonium-sulfate suspensions could not be used with S7P barium salt. Ultrafiltration in the neighboring paragraph applies to the purified PFK buffer exchange. The qualifier cites 2019 preparation paragraphs, which do not establish the 2020 added-ammonium condition.

Correction: State that the 2020 assay used lyophilized auxiliary enzymes in place of the earlier ammonium-sulfate suspensions, retaining BaSO4 precipitation and the source NH4Cl2 inconsistency. Cite the actual 2020 Methods in the qualifier; preserve the separate 2019 His6/TEV construct evidence.

Acceptance: No claim that auxiliary enzymes were ultrafiltered remains. The qualifier includes the 2020 assay paragraph and keeps CDQ83_07225/F6P/ATP scope; no PPi-S7P catalytic edge is added.

Affected fields: `mechanistic_edges[ppi-048].description`, `mechanistic_edges[ppi-048].endpoint_qualifiers[0]`, `description paragraph 4`

Primary evidence: PMID:31871051, PMID:31178853

Source locations: /article/body/sec[5]/sec[7]/p[1]; /article/body/sec[5]/sec[7]/p[2]

Review packet SHA256: `d7749e954e7cd7a823fa5f7bb0ed2ded90394e48b9a51f8313eab37c3ae9fa8c`. Preserve the complete six-event pathway, all biological edge identities, and negative/conflicting controls.

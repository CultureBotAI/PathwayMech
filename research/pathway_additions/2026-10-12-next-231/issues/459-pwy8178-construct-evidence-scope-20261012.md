Independent scientific review of candidate MetaCyc:PWY-8178 found a minor defect in `data/pathways/pentose-phosphate-pathway-non-oxidative-branch-ii.yaml`. The candidate is awaiting integration.

Stable finding key: `pwy8178-construct-evidence-scope`

ppi-034 asserts the His6/TEV construct but cites only the 2020 Methods and issuing native sequence; the retained 2019 Methods directly establish that feature. Aldoa linker wording is supported by the 2023 Results, but those Results are omitted from the qualifier locators. For Pfp, the inspected 2023 Methods explicitly call PfkA, PfkB and Aldoa codon optimized, then refer Pfp to an earlier study; the Pfp-specific text and thesis establish His6 but do not explicitly establish its linker or codon optimization. Those features should not be transferred from neighboring proteins.

Correction: Add the retained 2019 direct construct citation to ppi-034. Add the actual Aldoa linker Results locator to the four Aldoa qualifiers. For Pfp, keep the supported pAHCT0347/pRSET-A, His6, host, strain and assay distinctions, while making the linker/codon-optimization uncertainty explicit or supplying an inspected Pfp-specific construct source before retaining those extra features.

Acceptance: Every retained construct feature is entailed by its cited exact passage for that enzyme. No unsupported Pfp linker/codon-optimization assertion remains; all biological endpoints, catalytic activities, signs, strains and negative controls are preserved.

Affected fields: `mechanistic_edges[ppi-034].endpoint_qualifiers[0].evidence`, `mechanistic_edges[ppi-036,ppi-037,ppi-038,ppi-039].endpoint_qualifiers[0]`, `mechanistic_edges[ppi-040,ppi-041,ppi-042,ppi-043].endpoint_qualifiers[0].evidence`, `description paragraphs 6 and 7`

Primary evidence: PMID:31178853, PMID:31871051, PMID:37438781, hdl:1993/32279

Source locations: /article/body/sec[2]/sec[1]/p (2019 His6/TEV); /article/body/sec[5]/sec[2]/p (2023 cloning); /article/body/sec[2]/sec[1]/p (2023 PFK masses); /article/body/sec[2]/sec[7]/p (2023 Aldoa linker); Thesis PDF pp.111–113 and 117

Review packet SHA256: `d7749e954e7cd7a823fa5f7bb0ed2ded90394e48b9a51f8313eab37c3ae9fa8c`. Preserve the complete six-event pathway, all biological edge identities, and negative/conflicting controls.

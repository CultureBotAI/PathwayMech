The proposed complete amino-sugar superpathway draft omits two source-supported controls of its ManXYZ uptake branch. This finding concerns the external next-record draft, before maintained adoption.

Affected draft: `/private/tmp/pathwaymech-next-223-author-20261011/draft/amino-sugar-superpathway.future-schema.yaml`, SHA256 `a6c42b952683c9b3b69b11b800ea6b9b32f9d2380e8e851e4328c3091581cb0c` (109 edges, 77 named nodes).

Evidence:

- The intact native `CPLX-165.xml` Protein/comment paragraph about manXYZ expression explicitly identifies CRP–cAMP, Mlc and SgrS regulation. It links the issuing ECOLI frames `CPLX0-226` and `RNA0-241`, and primary papers PMID:9484892 and PMID:22988087.
- Native source: https://bf2i-artsymbiocyc.insa-lyon.fr/getxml?id=META:CPLX-165
- The current draft represents Mlc and NagC regulation of ManXYZ, and cAMP-bound CRP regulation of the separate GLUAMCAT context. Those edges do not represent the omitted ManXYZ controls.
- The author confirmed there was no evidence-based exclusion of these controls from the intended complete regulatory scope. Root independently read the entire native comment; independent scientific review is assessing the exact primary and identifier boundaries.

Requested correction:

1. Inspect the primary evidence and exact issuing CRP–cAMP and SgrS records, preserving strain, promoter/translation, sign and experimental limits. An ECOLI link alone must not be relabeled as an asserted META record.
2. Add the supported ManXYZ regulatory assertions and their narrow evidence. Verify whether an exact issuing CRP–cAMP state ID should also replace the currently qualified generic CRP endpoint, following the existing preference for exact state IDs.
3. Resolve any newly required RNA/state authority support through a bounded native adapter; do not invent a CURIE, add a label-policy waiver or discard the supported branch to satisfy current tooling.
4. Preserve the sealed author draft and review evidence, produce an explicit corrected successor, and rerun source-specific completeness controls, schema/identifier gates, graph/KGX qualification preservation and independent scientific review.

Acceptance: the full intended uptake/regulatory scope is represented with verified identities and source limits, the original omission is retained as review history, and the corrected successor passes the required checks.

Finding key: `amino-sugar-manxyz-crp-sgrs-regulation-completeness`.

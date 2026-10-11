# Four complete microbial pathway additions

This cohort adds four source-defined pathways to the 180-record baseline at
`e3bceba7613eb0525af3ff76ef32520201ae9f33`. Each author dossier records the
native boundary, exact identifier decisions, independently inspected evidence,
source conflicts and excluded near-matches. The resulting records contain 241
mechanistic edges and 419 edge-level evidence blocks.

| Record | Native scope | Author dossier |
| --- | --- | --- |
| MetaCyc:PWY-6993 | Eleven-step nicotine degradation II, including spontaneous hydration and the terminal succinate-semialdehyde branch | [Nicotine](nicotine-curation.md) |
| MetaCyc:PWY-6823 | Eight-step molybdenum-cofactor biosynthesis with whole sulfur-carrier states and the activation cycle | [Molybdenum cofactor](moco-curation.md) |
| MetaCyc:PWY0-1241 | Five-step ADP-L-glycero-beta-D-manno-heptose biosynthesis from sedoheptulose 7-phosphate | [ADP-heptose](adhp-curation.md) |
| MetaCyc:PWY0-501 | Two-step lipoate biosynthesis and incorporation I through protein-bound octanoyl and dihydrolipoyl states | [Lipoate](lipoate-curation.md) |

The [identifier ledger](identifiers-added.json) compares every declared identifier
slot in the four records with all baseline records. Authority integration
preserves earlier source objects and adds independently fetched source bodies;
its receipts retain source hashes and exact labels. Source-body manifests refer
to external raw evidence files, which are not committed here. The four replay
scripts are reproducible when those retained source bodies and the stated
ontology/Rhea snapshots are available.

The author replay receipts are distinct from scientific review. Each pathway
received a full independent assessment by a reviewer who did not author it;
immutable YAML and Markdown review bundles are under `reviews/structured/`.
The independent audit receipts in this directory retain source-level checks.

Four confirmed defects were filed and corrected before publication:

- [#341](https://github.com/CultureBotAI/PathwayMech/issues/341): a retired nicotine chemical identifier was removed from an active mapping slot while its source-version discrepancy was preserved in provenance.
- [#342](https://github.com/CultureBotAI/PathwayMech/issues/342): the MoaA intermediate cross-reference was attributed to the actual ChEBI reverse cross-reference, rather than a nonexistent native database link.
- [#343](https://github.com/CultureBotAI/PathwayMech/issues/343): nicotine catalyst and sequence edges now separate native pathway assertions from independently verified reaction-side chemistry.
- [#344](https://github.com/CultureBotAI/PathwayMech/issues/344): a LipA redox caveat was removed from the LipB evidence and retained on the correct LipA reaction.

The integrated [validation receipt](integration-validation.json),
[graph/export audit](generated-graph-kgx-audit.json) and
[baseline preservation audit](baseline-preservation.json) report final check
results. The initial validation detected pages rendered before the last nicotine
and lipoate edits; final checks follow regeneration. Diagram checks are
structural: the enabled-browser inventory was empty, so there is no visual or
interaction inspection claim.

Source conflicts remain explicit, including formal GmhA anomer stoichiometry,
legacy versus current LipA redox equations, and native versus modern molybdenum
cofactor states. Strain-specific experiments and inferred annotation do not
become broader experimental claims. iModulonDB supplies expression context only;
the missing console dependency and unchanged-client fallback are documented.
No source-exhaustion claim is made. The original Documents checkout remains
OS-inaccessible and is outside the scope of absence and cleanup claims.

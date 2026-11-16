# MIBiG actinorhodin source and bounded cluster addition

Checked 2026-11-16. Scope: one known-source update and one net-new cluster,
MIBiG:BGC0000194. This is not a whole-source or whole-fleet survey.

The [prior MIBiG canary](2026-10-07-mibig-ectoine-canary.md), current source
inventory and identifier manifest supplied the local baseline. A fresh download
of [MIBiG 4.0](https://dl.secondarymetabolites.org/mibig/mibig_json_4.0.tar.gz)
has SHA-256 `986f1a69fb5eeb84fd7c0175ae921304c22fd5f8ed04c96d8c1c0c95a145837b`,
identical to the existing pinned artifact. No release-wide update is claimed.
The inspected [entry JSON](https://mibig.secondarymetabolites.org/repository/BGC0000194.5/annotations.json)
has identical non-changelog content to archive member
`mibig_json_4.0/BGC0000194.json`, but its last changelog entry says `next`
with a null release date, versus release 5 dated 2024-11-15 in the archive.
The committed record follows the reproducible archive, not that mutable date.

The native record is active, questionable quality, and complete according to
MIBiG. These are source labels, not a new scientific review. Its locus is
AL645882.2:5513809..5535091 in NCBITaxon:100226. The JSON has one annotated
gene (CAC37459.1); its annotation list is not the full locus gene inventory.
The record preserves that annotation and adds three independently resolved
GenBank actI proteins. It never claims four genes exhaust the cluster.

The [primary abstract](https://doi.org/10.1016/S0021-9258(18)41772-3)
links sequenced genes to act mutations by complementation and interprets the
discrete PKS components using genetic, biochemical and similarity evidence.
The full paper was not retrieved. GenBank CAC44200.1, CAC44201.1 and CAC44202.1
explicitly identify actIORF1, actIORF2 and actIORF3. The alpha-subunit annotation
notes an extended N terminus relative to the earlier sequence; gene-role
correspondence is not historical assay-construct identity. The three enabling
edges express this limited evidence, not independent catalysis or sufficiency.

No reaction order, intermediate, catalyst sufficiency, product equivalence or
chemical output edge is inferred. The product name remains native metadata.
The inspected [ChEBI entry](https://www.ebi.ac.uk/chebi/CHEBI:2448) reports
InChIKey `VTIKDEXOEJDMJP-WYUUTHIRSA-N`; the native PubChem CID 5280985 property
response reports `FXTIILIJTTYSLT-WYUUTHIRSA-N` and omitted the requested Title.
These representations require reconciliation before a chemical endpoint or
crosswalk is added. They were excluded from the authority projection.

MIBiG data are [CC BY 4.0](https://doi.org/10.1093/nar/gkae1115);
MIBiG is the attributed source of the cluster facts. Database terms do not
establish a paper's redistribution terms. Only original summaries, identifiers,
hashes and locators are committed; raw paper metadata and downloaded inputs
remain in the durable private session evidence directory. No paid or
authenticated service, account creation or terms-acceptance step was used.

Duplicate searches included ignored and hidden files in the canonical checkout,
excluding Git internals, virtual environments and dotenv files. Matches were a
DRAM support row and unrelated styrene-paper text, not a maintained cluster or
rejection. The isolated current-main corpus was also checked for the exact ID.
Other source caches outside the repository were not searched. Four new authority
terms were projected by the existing native source builder: MIBiG:BGC0000194
and the three versioned NCBIProtein identifiers. Existing authorities and the
already-pinned taxon were preserved. No schema, importer, prefix or policy
waiver was added. Generic YAML emission was unavailable; the user-authorized
native create-one-record workflow exclusively installed validated new bytes.

Next: reconcile the compound structures and inspect primary full text before
extending the reaction graph. Keep source quality and evidence scope explicit.
Validation receipts are retained in the fleet-ops report directory and the PR.

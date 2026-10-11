# Three complete microbial pathway networks

This cohort extends the 192-record baseline at `0919419d95f65d097e867c6d8452f1ca552f550b` to 195 records. It adds 12 reaction nodes and 115 directed assertions across three source-defined pathways. Discovery remains active; the coverage hints and prior-assessment index are navigation aids, not evidence of source exhaustion.

| Pathway | Maintained record | Boundary |
| --- | --- | --- |
| MetaCyc:P121-PWY — adenine and adenosine salvage I | [YAML](../../../data/pathways/adenine-and-adenosine-salvage-i.yaml) | Both DeoD/Apt reactions from adenosine through adenine to AMP |
| MetaCyc:PWY-5705 — allantoin degradation to glyoxylate III | [YAML](../../../data/pathways/allantoin-degradation-to-glyoxylate-iii.yaml) | All four AllB/AllC/AllE/AllA reactions, including the nested PWY-5698 route |
| MetaCyc:PWY-6151 — S-adenosyl-L-methionine cycle I | [YAML](../../../data/pathways/s-adenosyl-l-methionine-cycle-i.yaml) | The native five transformations, with the supported MetH alternative represented as a sixth reaction node |

Per-pathway curation reports, identifier ledgers, original-source manifests, source projections and replay receipts retain the exact decisions. Original source bodies remain in the external caches named by each manifest, with source URLs, retrieval dates and SHA-256 hashes. `cohort-records.json` enumerates every added named node and reference; `integration-receipt.json` records the final commands and results.

Salvage I is distinct from the previously curated four-step salvage III route to IMP. The native pathway's species list does not include E. coli; the record grounds the K-12 enzyme implementation independently in the inspected salvage scheme, Apt experiments and DeoD kinetics. It does not establish dominant in vivo flux. The Apt dimer, DeoD hexamer, conditional metal use and preparation-dependent Apt location retain their source limits.

Allantoin III retains all four native reactions to glyoxylate, including the three-step AllB/AllC/AllE module. It differs from the existing anaerobic oxamate route and the yeast allantoicase route. The AllA urea-release and Ni-rescue experiment is direct primary evidence; its dimer observation remains structural annotation without an invented whole-complex identifier. The record makes no essential-route claim from the K-12 nitrogen-growth experiments.

SAM cycle I retains native generic methylation, Pfs/LuxS recycling and MetE/MetH regeneration. The generic methyl-acceptor classes preserve the source's literal donor labels and explain their reaction roles. The new `chemical_entity` category represents their broad molecular scope without inventing a specific structure. PathBank's unsupported dimethylglycine specialization, obsolete chemical mappings and autoinducer naming were not promoted. LuxS metal and assembly annotations retain their similarity evidence tier. No compartment is inferred for the entire cycle.

[Issue #354](https://github.com/CultureBotAI/PathwayMech/issues/354) tracks the generic chemical representation gap. The category is implemented in both validators, graph rendering and KGX export, with an end-to-end regression and a cofactor-subject guard. The independent code audit verifies identical graph output and KGX exports for all 192 baseline records. Scientific review outcomes and any additional findings are recorded in `review-index.json` and `issue-tracking.json`.

The initial allantoin/oxamate candidate was an existing-record duplicate. The glutathione PathBank map is a collage of biosynthesis, redox cycling, transport and xenobiotic reactions with a conflicting chemical identity; its disposition is retained without promoting an artificial single pathway. Duplicate searches include ignored and hidden files, with explicit scope and exclusions in the ledgers.

Fresh iModulonDB queries provide bounded computational expression context. They do not establish reaction chemistry or catalysis, and missing module hits are not negative biological evidence. The source bodies were replayed through the unchanged structured parser after the console runner proved unavailable.

The unchanged authority builders re-read original source inputs and preserve all baseline authority facts. Baseline preservation checks cover prior records, histories, reviews, record pages and exported assertions. Generated graph checks cover all nodes, edges, evidence links, directions and geometry, with parity against a separate KGX export. These are programmatic checks; no browser visual inspection is claimed.

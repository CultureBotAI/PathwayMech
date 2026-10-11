# Three complete microbial pathway networks

This cohort extends the 189-record baseline at `7bab6407d811db928abe049854ccb6107e591a3e` to 192 records. It adds all nine reactions and 93 directed assertions across three source-defined pathways. Discovery remains active; the lexical coverage inventory is a lead list, not evidence of source exhaustion.

| Pathway | Maintained record | Boundary |
| --- | --- | --- |
| MetaCyc:PWY-6609 — adenine and adenosine salvage III | [YAML](../../../data/pathways/adenine-and-adenosine-salvage-iii.yaml) | Four reactions from adenine through adenosine, inosine and hypoxanthine to IMP |
| MetaCyc:GALACTCAT-PWY — D-galactonate degradation | [YAML](../../../data/pathways/d-galactonate-degradation.yaml) | Three DgoD/DgoK/DgoA reactions to glyceraldehyde 3-phosphate and pyruvate |
| MetaCyc:PWY-6534 — phenylethylamine degradation II | [YAML](../../../data/pathways/phenylethylamine-degradation-ii.yaml) | Both native catabolic steps in Pseudomonas putida strain U |

The per-pathway curation reports, identifier ledgers, source manifests, source projections and replay receipts retain the exact identity and evidence decisions. Original bodies remain in the external caches named by each manifest, with source URLs, access dates and SHA-256 hashes. Exact record counts and identifiers are in `cohort-records.json`; final command results are in `integration-receipt.json`.

Salvage III is distinct from the current salvage I and inosine-kinase alternatives. The record preserves E. coli K-12 experimental scope, primary versus annotation evidence tiers, Hpt/Gpt catalyst differences, and the historical Gpt assembly discrepancy. It does not infer a membrane-localized pathway or include transport beyond the native metabolic boundary.

D-galactonate degradation retains the three-reaction native boundary rather than the broader glycolytic module. It preserves corrected DgoA/DgoD locus identities and conditional DgoR effector and metal observations. The record does not assert a fixed DgoA complex composition or an exclusive physiological metal.

Phenylethylamine degradation II retains the strain-U native boundary and exact ENA sequence bridges. The PeaA/D/C complex composition remains explicitly inferred; PeaB is an accessory requirement. The physiological electron carrier is unresolved, so the reaction uses the source's generic acceptor pair. Azurin observations from another strain and PeaEFG composition claims are not silently transferred to strain U. The 2008 primary abstract, original structured database tables and accessible comparison papers are distinguished from the unavailable full 2008 article.

Independent adversarial review found minor source-attribution and figure-locator defects, tracked in [issue #351](https://github.com/CultureBotAI/PathwayMech/issues/351) and [issue #352](https://github.com/CultureBotAI/PathwayMech/issues/352). Immutable initial observations and successor dispositions are indexed in `review-index.json`; exact pre-fix inputs are preserved under `historical-drafts/`. The issue ledger distinguishes a supported correction from subsequent GitHub closure.

Duplicate searches include ignored and hidden files, with explicit scope and exclusions recorded in the search ledgers. Fresh iModulonDB queries provide computational expression context only. The P. putida dataset is KT2440 and is not applicable to the strain-U mechanism; lack of a module-name hit is not negative biological evidence.

Authority snapshots are extracted from original source bodies using the unchanged canonical builders. The baseline preservation audit verifies that all prior records, histories, reviews, rendered record pages and KGX assertions are retained. The generated graph audit checks node and edge coverage, direction, evidence links, geometry and independent KGX export parity. No browser surface was available, so these checks do not claim visual browser inspection.

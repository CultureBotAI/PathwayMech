# Next264 bounded candidate discovery: aerobic benzoate entry pathway

Recommend **MetaCyc:PWY-2503, benzoate degradation I (aerobic)** for the next source-preparation task. This is a discovery-author handoff, not a pathway draft, final scientific review, or approval to curate against an unmerged baseline.

The complete native definition has two enzyme-mediated transformations:

1. BENZOATE-12-DIOXYGENASE-RXN: benzoate + NADH + proton + oxygen → the cis-dihydrodiol CPD-290 + NAD+.
2. 1.3.1.25-RXN: CPD-290 + NAD+ → catechol + carbon dioxide + NADH.

The native ordering joins the two reactions through CPD-290. There are 11 material-side entries and one primary-material join. Native Rhea references belong to families 12633–12636 and 11560–11563, respectively; the KEGG reaction leads are R05621 and R00813. These source cross-references support duplicate comparison; a full issuing-structure, charge, stoichiometry, and reaction-equivalence audit remains to be done.

Neither defining reaction family appears in any of the **260 current working records**, nor in the **258 original-checkout records**. The three maintained catechol degradation routes begin at this candidate's endpoint and contain neither of its transformations. This is a complete named upstream entry pathway, not an alias for a maintained catechol route.

## Baseline and bounded search

The current comparison root is `/private/tmp/pathwaymech-next-263-20261014`, based on commit `46ee133770039e8b21d1563166dec50eecd2c411`, tree `6dc181ad99e020fb3dade28304a31ba1a3177adc`. Its 260-record working corpus includes unmerged catechol degradation III, SHA256 `b30573a380b358a9b0228f8e3e2689943ecf828aa01ae790f281ba3fe617e603`. This is not a committed 260-record baseline.

The untouched original checkout is `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/PathwayMech`, commit `fbccbdc027f2a86ad4919e9dbbb16a736cc0746a`, tree `72737d598ca6c7d18861f8c3612f50c265a30e08`, with 258 records. Complete parsed inventories, exact YAML hashes, and compressed record snapshots are retained.

The final search uses 91 fixed-string, case-insensitive patterns: candidate IDs, names, aliases, both native/Rhea/KEGG reaction families, compound and native protein leads, native cited PMIDs, four assessed primary DOI/PMID sets, finite 2025 gene/protein leads, and three additional module aliases. `rg --no-ignore --hidden` includes ignored and hidden files. Root `.git` and `.venv` directories are excluded; normal binary handling applies, compressed archive interiors and directory symlinks are not traversed, and no global cache or world/database exhaustion is claimed.

The dispositioned union contains **18 current-root files / 38 matched lines** and **10 original-root files / 27 matched lines**. All matched files have retained complete byte snapshots. Mentions include an obsolete GO term from earlier broad searches, native links at the upstream catechol interface, species-level publication metadata, ubiquitous oxygen/proton reaction backlinks, unrelated dihydroxybenzoate substrings, broader native superpathways, and ignored DRAM support rows for KEGG M00551. None establishes an existing maintained record for the complete selected route. Exact reaction fields were checked where substrings could mislead.

**After 263 merges, rebind the complete corpus and ignored-inclusive searches to that verified merged commit before authoring.** The frozen evidence and snapshots permit comparison even after the temporary 263 checkout is removed. A later rebind must inspect new or changed matched contexts rather than automatically reuse this absence conclusion.

## Authoritative boundary and alternatives

Complete native META 27.0 originals are retained for PWY-2503, both defining reactions, CPD-290, benzoate, the Benzoate-Degradation class, PWY-2504, and PWY-283. The complete PWY-5430 original and Rhea directions table were reused from frozen predecessor packages with exact hash/manifest bindings.

The Benzoate-Degradation class has three direct pathway members. PWY-283 has only a benzoate-CoA ligase reaction and is excluded from this multi-step task. PWY-5430 combines upstream benzoate conversion with alternative catechol meta routes; PWY-2504 is a broader aromatic-source superpathway with 12 module members. Both are excluded as umbrellas. GO:0043639 is broader benzoate catabolism; the former hydroxylation-specific GO:0043640 is obsolete and replaced by that generic term. The exact complete KEGG M00551 response covers benzoate **or methylbenzoate**, so it is a broader mapping lead, not the selected native boundary. EAWAG `benz2` is only a native PART-OF link here.

## Primary scope and source conflicts

The primary reading ledger distinguishes actual content from access attempts:

- PMID:4399343 (Reiner, 1971): complete issuing metadata and abstract read. Benzoate-induced extracts support the cis-dihydrodiol intermediate and NAD+-coupled dehydrogenation/decarboxylation to catechol. Full XML failed; PMC HTML was a browser-check page, and the PDF attempt returned HTML with HTTP 403. No historical full methods, figures, or tables were read.
- PMID:4326771 and PMID:4341530: exact issuing metadata and titles retained; no abstracts or readable full text acquired. The latter publisher response was HTTP 403. Purified-enzyme constants and preparations are not accepted from titles alone.
- PMID:40405529 (2025): complete issuing JATS read, including body text, two tables, and seven figure captions. Actual figure graphics and a PDF were not viewed. RW1 knockout/complementation and heterologous assays support the first benzoate-to-cis-diol step and electron-transfer alternatives. BenD remains putative in this paper; the second step and a unique physiological ferredoxin must not be inferred from those results.

The complete native pathway prose incorrectly says the cis-dihydrodiol is “reduced” to catechol. Its own reaction and the 1971 primary abstract instead support substrate dehydrogenation/oxidative decarboxylation while NAD+ is reduced. Preserve this disagreement explicitly. A native JMP222 taxon parent/comment mismatch, an unrelated L-rhamnose citation nested under species metadata, and a 2025 helper-host preparation inconsistency are also retained in `known-source-conflicts-and-limits.json`.

## Next source tasks

1. Rebind to the post263 merged baseline and fresh corpus/search inventory.
2. Retrieve and read all five complete activity definitions: ENZRXN-15650, ENZRXN-3124, ENZRXN-15651, ENZRXN-3125, and ENZRXN-12384. Close their four enzyme frames CPLX-7698, CPLX-2541, CPLX-7701, and MONOMER-2964, including components, genes, cofactors, regulators, and preparation-specific evidence. The eight native UniProt cross-references remain related-to leads until issuing identity/sequence verification.
3. Verify exact CPD-290 stereochemistry and all benzoate/catechol/cofactor/small-molecule structures, charge, stoichiometry, and reaction-family orientation using issuing originals. Native chemical cross-references alone are not this verification.
4. Pursue readable historical primary methods through available public routes, preserving failures and access limits. Resolve strain lineage and exact 2025 protein/taxon identities; keep organism, preparation, activity, and regulation contexts distinct.
5. Only then curate, integrate authorities/history, render and inspect graph/KGX outputs, run gates, and obtain independent scientific and technical review.

This finite discovery supports choosing the next candidate. It does not establish source exhaustion, final scientific completeness, licensing clearance, or readiness to merge a new record. All task output is external; no maintained files, Git state, or GitHub objects were changed.

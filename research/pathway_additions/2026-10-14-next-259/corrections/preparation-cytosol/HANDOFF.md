# External author correction proposal

This package proposes two review-driven corrections against record SHA256 `9fb56b4694243c675aa1227a443dd46a8012d8ebeb0e8665e4de6f68520ed665`. It does not modify maintained files, frozen research packages, or authority snapshots. Independent successor review and root acceptance remain pending.

Proposed record: `gallate-degradation-i.yaml`, SHA256 `2fe675db8c090057dbf2cddedf313ea133278b7895dd7a4d68ec787e6e91fcd6` (156,292 bytes). The proposed record has 130 edges, 78 participants, nine reaction/context nodes, and no whole-pathway taxa. `proposed.patch` applies to the exact reviewed input; `field-change-acceptance.json` accounts for all 29 field changes or additions.

## F1: local preparation citations

The three native-022/026/037 preparation qualifiers now cite the inspected Kasai 2005 or Nogales 2011 primary text. The existing catalytic assertions remain intact. Four DesB treatment qualifiers now distinguish the actual Table 1 plasmid and strain rows from the host–construct assignment in Methods prose. Source assertions describe only inspected structured table rows. The short primary excerpts carry exact source locators; no paper prose is relabeled as structured evidence.

The complete preparation and mechanism descriptions are preserved. The existing GalT effect excerpt is shortened to allocate words to the GalD and GalC preparation citations; its less-efficient protocatechuate uptake statement and original locator remain unchanged. Kasai 2005 has 25 quoted words and Nogales 2011 has 24, counting every repeated qualifier placement. Every other paper remains within 25 words. Whole-record exact quotation replay rehashed all original files and passed, using only whitespace normalization. `quotation-replay.json` retains source paths and hashes, without copying another set of quotations.

The 2011 evidence remains a retained publisher web transcription. Original spectra, Table S1, and Figure S7 were inaccessible; this patch does not claim new visual inspection. The DesB retained PMC HTML was read directly, including the actual Table 1 cells and relevant Methods/Results paragraphs. `source-element-replay.json` binds their precise DOM paths and text hashes.

## F2: omitted computational location

The native G1G01-2699-MONOMER XML has both an explicit CCO-CYTOSOL location and GO:0005829 with EV-COMP-AINF and PSORTdb citation PUB-26602691. The proposal adds only that native GalB monomer's located_in edge. The description explicitly distinguishes the computational annotation from direct localization and from the recombinant preparations.

GO:0005829 is already in the maintained ontology authority and the external union as cytosol. `go-cytosol-authority.json` verifies its exact pinned cellular-component triples and rehashes the full 1,701,474,304-byte GO database to the existing owner digest. No new authority owner or snapshot change is proposed.

`append-only-disposition-corrections.json` supersedes the false absence statement in the frozen native compartments fact and HANDOFF, plus the generic dispositions for the native location and sixth GO slot. It identifies prior files, hashes, and exact fact/slot keys; the frozen originals and ledgers remain unchanged.

## Validation and application boundary

Local schema and closed LinkML schema both pass. All 129 existing subject/predicate/object triples and every existing edge/qualifier description remain unchanged. The one new selected identifier is GO:0005829; the existing monomer becomes an additional locally declared reference. `validation.json` records commands, current input hashes, source hashes, counts, and rubric bindings. The initial strict-schema invocation used a nonexistent worktree virtualenv path; `first-attempt-receipt.json` records that failure and the corrected invocation uses the existing main virtualenv with the next259 code and working directory.

The final frozen predecessor package was rehashed unchanged. The patch was checked with `git apply --check` against the task worktree without applying it. Root owns issue creation, maintained application, history, generated artifacts, full gates, successor reviews, and all GitHub actions. Complete source originals remain external; this package contains only the proposal, compact proof ledgers, hash bindings, and a replay helper.

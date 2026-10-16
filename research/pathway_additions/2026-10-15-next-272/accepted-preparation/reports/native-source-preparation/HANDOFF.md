# Frozen native source-preparation handoff: MetaCyc PWY0-1477

Owner: `/root/next272_native_source_preparation`.
Owner directory: `/private/tmp/pathwaymech-next-272-native-source-preparation`.
Scope: complete native source originals for every one of the five reactions' 71 activity leads, selected protein/complex/component/cofactor/regulation/location closure, and bounded author semantic dispositions. This is a source-preparation packet, not an accepted maintained record, independent scientific review or completed cited-literature survey.

## Result

- 268 exact original response files: 204 META full XML objects, 24 ECOLI full XML objects, 34 canonical UniProt JSON proteins, five bounded keyword/protein search responses, and one QuickGO response containing GO:0031471 and GO:0031469.
- All 228 native objects and all 3,689 native own slots preserved. The 34 proteins have 298 retained comment statements; full original sequence/reference/crossreference content remains in the source JSON and projections.
- All 71 activities have full enzyme originals and individual dispositions: seven selected native Eut activities, eight same-taxon/adjacent contexts, 56 unrelated contexts. All five members, both branches, root21 slots, four ordering links, 22 material occurrences and 14 materials preserved.
- Nineteen explicit source-conflict groups with original statement content, source hashes and exact locators.
- Offline raw-identity/slot/activity/receipt/reuse coverage verification passes. Six projection/disposition generators replay byte-identically; helper syntax checks pass. All acquisition jobs are terminal.

The initial 69-object enzyme acquisition plan contains **68 distinct enzyme objects directly linked by the 71 activity leads plus G7288-MONOMER**, the separately selected EutD component. The directly linked EutD enzyme is CPLX0-7912. Earlier shorthand describing “69 linked enzyme objects” conflated activity enzymes with component closure; it was not a duplicate or missing activity. `results/enzyme-count-reconciliation.json` supplies the exact 68-object set and the one-object difference; the original acquisition plan is preserved.

## Read order

1. `SOURCE_ASSESSMENT.md`: biological scope, selection and unresolved distinctions.
2. `results/all71-activity-dispositions.json`: every source activity and enzyme disposition, evidence, taxa, cofactor/alternative/kinetic/component/location content.
3. `results/all34-protein-semantic-dispositions.json` and `results/all-uniprot-comment-dispositions.json`: protein and comment-level biological interpretation.
4. `results/source-conflicts.json`: 19 consequential claim groups including source label/EC/direction/class/location/assembly/microstate contradictions.
5. `results/all-native-projections.json`, `results/ecoli-native-projections.json`, `results/complete-native-slot-interpretations.json`: complete native source projections and all-own-slot accounting. The slot ledger is machine completeness plus slot-type interpretation, not 3,689 independent scientific validations.
6. `results/verification.json`, `results/replay-proof.json`, `results/enzyme-count-reconciliation.json`: reproducibility and exact coverage.
7. `originals/`, `receipts/`, reuse bindings and `inputs/`: immutable body bytes and provenance chain.

## Provenance and access

Fresh XML uses the retained MetaCyc/EcoCyc 27.0 issuing source service, with exact requested/final URL, timestamps, status, headers, bytes, SHA256 and identity validation in receipts. This does not claim a newly released BioCyc dataset. Fresh canonical UniProt entries retain exact release/entry/sequence versions and source evidence codes. Search responses are bounded discovery leads; their strings are not separate proof of mechanisms.

The six root/reaction originals are exact copies from the accepted frozen discovery packet, bound in `results/reused-input-bindings.json`. The 16 core material/taxon originals are exact copies from `/private/tmp/pathwaymech-next-272-core-identity-preparation`, manifest SHA256 `67f29b62064d86886bfc0767a42c2ee08a8b444045242ed7e4d1b4e398dc8e57`, bound in `results/core-original-copy-bindings.json`. Its handoff, manifest, freeze proof, reuse binding and available receipt chain are copied under `inputs/core/`. ACETALD and Pi were supplied with exact older-owner provenance/raw envelopes but without their original HTTP receipts; no fresh retrieval timestamp is asserted for them. Source/receipt copy hashes are enumerated in `results/additional-input-bindings.json`.

Discovery and independent-preflight handoffs, root intake and product guidance are copied into `inputs/` and `guidance/`; no later process depends on the next271 worktree. Their acceptance is limited to source preparation.

Primary evidence is separately owned at `/private/tmp/pathwaymech-next-272-primary-evidence-preparation`. Its frozen manifest is `86974c5ce2562d549755f18b30fa27a14ac6c6d5007b476aaeefe105eaa36ada` (250 listed / 252 physical files). Its handoff, manifest, freeze proof, 24 source reading scopes, 32 claim dispositions and open limits are bound under `inputs/primary/`. The conflict ledger marks the parallel primary owner's reports as such; root intake is separate and this packet does not claim independent reading of those papers. Root also owns the separate iModulonDB expression-context packet. Those outputs must not become unsourced enzyme/flux/localization assertions.

## Required downstream care

Native MG1655 association and K12 UniProt scope/CPZ-55 caution do not demonstrate intact MG1655 flux. EutBC source prose conflicts with explicit six-plus-six composition. EutN crystal/native hexamer and solution pentamer have distinct scopes. EutT has an omitted native component coefficient, separate UniProt dimer evidence, unresolved cobinamide specificity and reaction proton-count/EC differences. The native acetate-kinase EC anomaly is preserved. EutH neutral transport must not be equated with native +1 ethanolaminium. Whole-route lumen assignment, shell detoxification, donor identity and direct cofactor/cargo handoff are not uniformly established. EutP/Q, EutE/D/G and cargo experiments retain their strain, construct, assay-direction and access tiers.

No new CURIE, schema slot, accepted alias, source-equivalent graph node or maintained causal edge was manufactured. No external issuer verification is claimed for every ancillary compound/protein xref. Unrelated/shared reaction enzymes and chemical/class/regulation backlinks remain explicit context. This is the completed bounded source phase; further literature/identity review and exact merged-baseline rebind remain required before maintained curation.

## Offline reproduction and freeze

Run `python -B scripts/verify_packet.py` from this owner to verify source/projection/coverage consistency without network or writes. `results/replay-proof.json` records six generator commands that reproduced the twelve derived outputs byte-for-byte. Acquisition scripts are retained for provenance but must not be rerun into this frozen owner; their source files are immutable. For a new acquisition, use a new owner and new receipts.

Two initial helper failures are preserved under `results/`: an explicit slot-coverage assertion caught missing reverse-link interpretation, and the verification helper initially treated an integer material-occurrence count as a list. Both were corrected without source changes and followed by passing replay. Earlier plain-comment extraction was refined to an HTML parser so tooltip attributes cannot leak into readable prose; exact XML originals were always retained.

`artifact-manifest.json` inventories every physical file except itself and `freeze-proof.json`, with byte count and SHA256. `freeze-proof.json` binds the manifest and this handoff, states all jobs terminal and records counts. No file in this owner is to be edited after freezing. Any follow-up is a new packet.

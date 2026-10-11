# Carbon-fixation pathway additions after the 206-record baseline

This cohort starts at merge `a3a31179b0533cacbf59559a3151c8ebcaac4f97`
(PR #372). The preceding cohort's publication was checked against that exact
merged tree before its feature branch was deleted. This work is on a separate
branch based on that merge.

The three candidate scopes are distinct:

| Identifier | Pathway boundary | Evidence scope under curation |
| --- | --- | --- |
| MetaCyc:PWY-5789 | Complete 3-hydroxypropionate/4-hydroxybutyrate cycle, with net acetyl-CoA formation. | Metallosphaera sedula TH2 / DSM 5348; original protein sequences and biochemical preparations are checked separately from native cross-references. |
| GO:0043427 | Complete first 3-hydroxypropionate cycle, producing glyoxylate and regenerating acetyl-CoA. | Chloroflexus aurantiacus; OK-70-fl and J-10-fl experiments and protein sequences remain distinct. The two experimentally supported regeneration activities omitted from native PWY-5743 are retained. |
| MetaCyc:PWY-5744 | Complete glyoxylate-assimilation cycle, producing pyruvate and regenerating propionyl-CoA. | Chloroflexus aurantiacus; all thirteen native activity objects are assessed, including the shared acetyl-CoA-to-propionyl-CoA branch. |

These boundaries do not make the separate native whole-bicycle parent a fourth
addition. Shared reactions do not establish pathway equivalence. Native object
counts, physiological reaction counts, and chemical half-reaction conventions
are recorded separately.

All three author dossiers and record bytes are frozen. The initial repository
checks passed, including 1,059 tests. Independent scientific reviews found three
bounded provenance defects, tracked in issues #373, #374, and #375: one primary
article title, three claim locators, and one native reaction attribution. The
supported corrections preserve every other parsed scientific field. Corrected
author replays and independent source reassessments passed; final repository
checks and successor review dispositions are recorded separately.

The immutable initial reviews and their inspected inputs remain in the review
bundles and `initial-review-inputs/`. The initial integration observation is
preserved in `initial-integration-receipt.json` and `initial-checks/`.
`review-correction-audit.json` records the exact parsed changes. Whole original
source bodies remain outside the repository; this dossier retains selected
facts, exact source manifests, replay helpers, and receipts.

`authority-source-inspection.json` and
`authority-source-inspection-additional.json` record twenty acquired native
MetaCyc HTML bodies. Their current scope is identifier and title extraction.
Acquisition does not establish assembly composition, organism-specific catalytic
activity. The integrated manifest selects seventeen of these bodies and fourteen
original UniProt responses, with all existing authority entries preserved.
`authority-integration.json` records the canonical rebuild commands and exact
input/output hashes: forty-three ontology terms and fifty-two source terms were
added. The existing identifier policy is unchanged.

The iModulonDB console entrypoint was unavailable, as recorded in
`imodulondb-runner-availability.json`. The unchanged source client retrieved the
twenty-organism, twenty-eight-dataset inventory. `imodulondb-replay.py` re-parses
the retained original bodies without network access; its result is recorded in
`imodulondb-offline-replay.json`. The selected Metallosphaera and Chloroflexus
scopes have no matching dataset in that inventory. The listed Sulfolobus
acidocaldarius dataset does not establish expression evidence for M. sedula.
This is an availability assessment, not negative biological evidence.

Additional candidates and source coverage remain to be assessed. Source
exhaustion has not been established.

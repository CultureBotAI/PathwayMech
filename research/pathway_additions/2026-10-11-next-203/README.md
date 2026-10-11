# Three pathway additions after the 203-record baseline

This cohort follows merge `7c555ecacc2b2708b246a68dcc9b64444791f526` (PR #370).
Each candidate is a complete, separately identified native pathway.

| Native pathway | Maintained record | Biological scope |
| --- | --- | --- |
| MetaCyc:PWY-6048 | `data/pathways/methylthiopropanoate-degradation-i.yaml` | Three-step cleavage route in Ruegeria pomeroyi DSS-3; generic electron-transfer carrier evidence is qualified. |
| MetaCyc:PWY-7255 | `data/pathways/ergothioneine-biosynthesis-i.yaml` | Seven native bacterial biosynthesis steps; strain-specific experiments and thiol/thione states remain distinct. |
| MetaCyc:PWY-7722 | `data/pathways/sulfoquinovose-degradation-ii.yaml` | Five sulfo-ED steps in Pseudomonas putida SQ1; the final native NAD(P) step becomes two cofactor-specific activities. |

The source-specific `*-curation.md`, `*-source-manifest.json`, projections,
identifier decisions, executable `*-replay.py`, and `*-validation.json` retain
the authors' evidence and reproducibility work. Raw source bodies stay in the
external cache identified by the manifests. A passed author replay verifies
source projections and artifact correspondence; it is separate from the
independent scientific reviews and full repository gates.

`authority-acquisition-integration.json` identifies the five native MetaCyc
objects and thirteen original UniProt records added as source inputs.
`authority-integration.json` records the canonical builders, original-body
hashes and exact preservation of all baseline terms and source metadata.
The unused acquired native aldolase identifier is not added to the manifest.

`imodulondb-runner-availability.json` records the unavailable console entrypoint.
The unchanged native client provided the current dataset inventory, and
`imodulondb-offline-replay.json` independently reproduces it from preserved
original bodies. `imodulondb-applicability.json` records why none of the three
selected organism/strain scopes has a matching dataset; KT2440 is not SQ1.
Dataset availability is not negative biological evidence.

`current-coverage-hints.json` refreshes bounded lexical hints for the frozen
528-document PathBank screen against the 203-record baseline. It does not
establish pathway equivalence. `carbon-fixation-scout-assessment.json` retains
two further native cycle leads, prior mentions, ignored/hidden-file searches,
newly inspected primary evidence and specific prerequisites for future curation.
Those leads are not approved records. Sources are not exhausted.

The full staphyloxanthin, coproheme and CMP-Kdo candidates previously withheld
under issues #369, #348 and #346 remain outside this cohort.

Independent review of ergothioneine identified an overly specific attribution
of the EgtD product-inhibition experiment (issue #371). The assayed engineered
ATCC607/DSM43465 preparation differs at residue 2 from the selected current
mc(2)155 protein entry. The exact-protein inhibitory edge was removed, while
the experimentally observed inhibition remains explicitly qualified context.
No inhibition-only evidence was moved onto an activity edge, and the seven
native transformations remain intact. The correction does not imply that the
sequence difference changes enzyme behavior.

The initial review is immutable, and `initial-review-inputs/` preserves all
21 of its formal inputs at their reviewed hashes. `initial-checks/` preserves
the earlier integration checks, including the corrected lint failure. The
independent successor audit distinguishes the failed initial wrapper from
its successful test child. Final cohort totals are 131 mechanistic edges and
250 evidence entries across the three new records. Source replay, scientific
review, repository validation and eventual live publication have distinct
receipts and scopes.

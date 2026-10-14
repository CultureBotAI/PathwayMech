# Acceptance record

The complete MetaCyc:PWY-6223 record contains 24 participants, three molecular
activities, three taxon contexts and 35 evidence-backed edges. Its final YAML
SHA-256 is `272e475b3bb872475bba938c5e5016b52b63e21dc8c9dea772e25ba78524c064`.

All 248 baseline pathway YAMLs, 4,799 prior authority terms and 766 source owners
are preserved. Independent canonical rebuilds reproduce the final 4,814 terms,
772 owners and 948 source entries byte for byte. The full prior manifest prefix,
KGX edges and per-record node contexts remain intact.

Independent scientific review found the NagI primer/start-position conflict,
tracked in #528. Its protein subject now has an experimental-construct qualifier
retaining the conflicting reports and uncertainty about the expressed sequence.
Independent integration review found six reproduction helpers entering executable
lint scope, tracked in #529. Their bytes and hashes are preserved as text artifacts
with explicit path mappings. Both initial findings have linked successor
dispositions; the original observations are unchanged.

All six final local gates passed: `just render-pages`, `just validate`,
`just test`, `just lint`, `just vendored-check`, and `git diff --check`.
Test summary: 4882 passed, 3 skipped, 7 warnings in 515.89s (0:08:35).
The captured core inputs remained unchanged throughout the gates. Actual receipts
and lossless logs are under `validation/final/`; the earlier focused helper-lint
failure remains in the integration review evidence.

Independent page and KGX audits retain all 35 edges, full evidence/reference
metadata and all 14 qualified endpoints. The static SVG has 42 display nodes;
arrow directions, evidence anchors, bounds and label/node geometry pass. Raster
and native-size crops were inspected. This is static SVG verification, not browser
interaction testing. Taxa remain record/KGX context rather than invented network
edges.

Completed independent successor observations:

- [Independent successor scientific review of gentisate degradation I](../../../../reviews/structured/20261014T123411Z-next251-gentisate-science-final/review.md) ([YAML](../../../../reviews/structured/20261014T123411Z-next251-gentisate-science-final/review.yaml)): pass_with_limitations.
- [Gentisate integration accepted; retained-helper lint finding resolved](../../../../reviews/structured/20261014T123445Z-gentisate251-integration-resolved/review.md) ([YAML](../../../../reviews/structured/20261014T123445Z-gentisate251-integration-resolved/review.yaml)): pass_with_limitations.

Scientific limitations remain explicit: the NagI expressed N terminus is unresolved,
some full papers or supplementary material were unavailable, Cgl Figure 5 was
assessed through its legend, and metal effects are bounded tagged-protein assays.
These limits do not become unqualified physiological claims. Raw downloads stay
external. Exact committed-head acceptance and remote CI are recorded separately
in the subsequent PR lifecycle.

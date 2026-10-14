# Acceptance record

MetaCyc:PWY-6336, protocatechuate degradation III (para-cleavage pathway), now
contains 25 participants, five molecular activities, one downstream pathway
interface, one taxon, 46 evidence-backed edges, 30 references and nine qualified
endpoints. Final record SHA-256: `2a5e42e39a4e8eadb77eabf6f95896ecc7f001bafba04dec6eb74e7251169d89`. The complete identifier inventory is
in `identifiers.json`, and original reference bindings are in `reference-bindings.json`.

All 249 baseline pathway records and 4,814 baseline authority terms are preserved.
The final authority snapshot contains 4,835 terms and 784 source owners; the prior
948-entry source manifest prefix is preserved before 12 additions. The second
ontology extraction adds the two redox chemical terms to the initial addition
without changing its source owners or earlier terms. Initial evidence and output
bindings remain immutable, with separate successor evidence documenting the fix.

Independent scientific review identified an omitted native dioxygenase redox
mechanism, tracked in issue #531. Four added edges now represent hydrogen peroxide
and potassium ferricyanide inactivation and ascorbate recovery of two distinct
inactive-enzyme states. The exact potassium salt and generic ascorbate identity
preserve the primary abstract's scope. The original 42 edges, 22 participants and
29 references remain unchanged. A linked scientific successor resolves the
original finding; the initial observation is preserved.

The first commit omitted three retained authority build logs because the existing
ignore rule excludes log files. This commit-packaging defect is tracked in #532.
The exact files were explicitly added, preserving their original paths, bytes
and retention manifests. Independent committed-tree verification and a linked
integration successor document the correction; the first commit is preserved.

All six final local gates passed: `just render-pages`, `just validate`, `just test`,
`just lint`, `just vendored-check` and `git diff --check`.
Test result: 4882 passed, 3 skipped, 7 warnings in 536.51s (0:08:56).
The captured core inputs remained unchanged throughout execution. Actual receipts
and lossless logs are retained in `validation/final/`. Independent integration
review checks the canonical authority reproduction, generated graph, KGX data,
reference evidence and retained artifact bindings; its exact scope is recorded below.

Completed independent observations:

- [Protocatechuate para-cleavage integration accepted](../../../../reviews/structured/20261014T133634Z-next252-para-integration-final/review.md) ([YAML](../../../../reviews/structured/20261014T133634Z-next252-para-integration-final/review.yaml)): pass_with_limitations.
- [Independent successor scientific review of protocatechuate para-cleavage](../../../../reviews/structured/20261014T133636Z-next252-para-science-final/review.md) ([YAML](../../../../reviews/structured/20261014T133636Z-next252-para-science-final/review.yaml)): pass_with_limitations.
- [Committed protocatechuate evidence retention resolved](../../../../reviews/structured/20261014T134804Z-next252-retention-resolved/review.md) ([YAML](../../../../reviews/structured/20261014T134804Z-next252-retention-resolved/review.yaml)): pass_with_limitations.

Scientific limits remain explicit: the 1993 full article and 2009 supplementary
material were unavailable, recombinant terminal/tag details are unresolved, and
historical native-enzyme effects are not physiological regulatory claims. The PraR
reporter result lacks an exact identified target and remains an evidence gap.
The five-step route and downstream interface are distinct. Ignored and hidden files
were included in duplicate and review-lineage searches within their stated bounds.
No source-exhaustion conclusion is drawn. Raw downloads remain external; public
release licensing is deferred under the user's direction. Exact committed-head
acceptance and remote CI are documented in the subsequent PR lifecycle.

# Integration gate evidence

`gate-results.json` records the terminal full validation, test, lint, existing review-bundle and unstaged whitespace checks. The exact stdout/stderr bytes are retained as deterministic gzip files under `logs/`; receipts are unchanged byte copies, including failed attempts and their passing successors. The index records original and stored sizes and hashes.

The full suite passed 8,014 tests, with three empty custom-command parametrizations skipped and seven dependency warnings. Full validation passed 269 pathways, 21,950 evidence blocks, 518 history records, identifier policies, the closed schema and generated-page freshness. The existing review check passed 196 saved bundles. The separate vendored-file gate passed all 22 pinned artifacts.

This is a finite root-receipt subset, distinct from complete frozen scientific and adversarial packets. The product-input inventory was captured after the gates; it does not claim to be a gate-start snapshot. The final canonical review, later support packaging, staged whitespace, PR checks and actual merge verification remain separate publication steps. No browser/pixel test or source exhaustion is claimed.

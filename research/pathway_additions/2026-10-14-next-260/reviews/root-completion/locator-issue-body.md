Independent technical review of the gallate degradation II addition found a provenance-navigation typo in the supporting S75-003 successor erratum. Its `affected_frozen_context` names `entry-primary/author/claim-ledger.json`, while the retained claim ledger is `sources/primary/author/claim-ledger.json` within `research/pathway_additions/2026-10-14-next-260/`.

The scientific erratum remains valid: the original 1975 page reports induction at absorbancy 0.3 at 540 nm. No maintained graph edge used the earlier transcription of 0.4. This issue concerns the retained artifact locator, not a new scientific correction.

The fix is already prepared locally as an append-only `integration/erratum-locator-clarification.json`, preserving the earlier frozen erratum and binding the correct ledger by SHA-256 `bf554cf6e9903976d4522112534abbd3f46b8f8c7b167b0d4816e3e8b806d989`. The research README points readers to the clarification.

Acceptance: verify the corrected retained path and hash, keep the original frozen source package unchanged, and include the clarification and independent technical review in the gallate II pull request. Close this issue when that reviewed change is merged.

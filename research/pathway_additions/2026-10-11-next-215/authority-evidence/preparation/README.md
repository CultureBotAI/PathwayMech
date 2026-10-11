# Staphyloferrin B authority preparation

`selection.json` binds the corrected current B record (`742930db…`), 44 named identifiers and exact original authority bytes. It preserves the historical author proposal and its earlier target hashes. The selection began against reviewed A commit `775e7166…`; `actual-baseline-equivalence.json` separately verifies its full tree equality with actual merge `6bdd43b7…` and all seven unchanged authority/parser inputs in the current 215 checkout.

The proposed delta is five original source inputs, 12 source terms and 14 ontology terms. Prospective totals are 524 manifest inputs, 2,134 source terms and 1,821 ontology terms. The native UniProt response has nine entries, but only Q2G1M5 and Q2G1N2 are graph participants. The complete response remains the hashed source. No labels come from the curated record, no namespace or policy changes are proposed, and no original body is copied into the repository.

`prepare-selection.py` used the unchanged native parsers and issuing ontology extraction functions. `integrate-authorities.py` defaults to an external canonical dry run: it links the original cache files beneath a fresh output directory, rebuilds both snapshots, preserves every prior term and source metadata object, checks the exact planned additions and runs the current one-record identifier gate. It writes neither shared cache nor maintained snapshots in this mode.

The optional `--apply` mode is proposed for root only after independent acceptance. It requires `--acceptance` plus its exact `--acceptance-sha256`, and the acceptance JSON must contain:

- `status`: `passed_independent_root_authority_selection_review`
- `selection_sha256`: the accepted selection digest
- `integration_helper_sha256`: the accepted helper digest
- `target_sha256`: the accepted current B record digest
- `base_commit`: actual A merge `6bdd43b77ade4ceb6ffa4e4b486d1f42e096e9aa`

The apply mode repeats the canonical build and preservation guards before copying verified new source bytes into the external shared cache and updating only the three authority owners plus three new integration dossier files. The output directory must be fresh and external. This preparer has not executed apply and does not independently approve this helper or its selection.

Scientific eligibility, full corpus gates, history, rendering, publication and a final canonical scientific successor remain separate work. Identity labels do not establish catalytic activity, strain transfer, oligomerization or chemical equivalence.

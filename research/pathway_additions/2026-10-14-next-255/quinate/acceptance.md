# Quinate degradation I acceptance

The complete three-step `MetaCyc:QUINATEDEG-PWY` record has 37 edges, 17 participants and two organism contexts. All 251 baseline pathway records are unchanged. Its generated network page and KGX exports preserve the evidence and six qualified endpoint instances.

## Verification

- `just render-pages`: 252 records.
- `just validate`: 252 records, 18,151 evidence blocks, identifiers, closed schema, provenance, source records and page consistency passed.
- `just test`: 4960 passed, 3 skipped, 7 warnings.
- `just lint`, `just vendored-check`, and `git diff --check`: passed.
- Saved structured reviews passed the repository review-contract check.
- Independent authority replay reproduced both snapshots exactly, preserving all 4,891 prior terms, 821 owners and the 997-entry manifest prefix.
- All 12,574 existing KGX edges and 4,544 prior nodes are preserved; shared nodes only add this pathway context.

The complete gate output is retained in `validation/` as lossless wrappers bound to their external originals. Tested core inputs remained unchanged. Record SHA256: `a0c21af8e01b7a2653b226656b405fc197b0376b2d9ea4a6dbb6d003a3cc36cb`.

## Independent reviews

- [Independent integration review of quinate degradation I](../../../../reviews/structured/20261014T164250Z-next255-independent-integration/review.yaml): `pass_with_limitations`; codex independent integration reviewer /root/next255_integration_review.
- [Independent scientific review of quinate degradation I](../../../../reviews/structured/20261014T164250Z-next255-quinate-scientific/review.yaml): `pass_with_limitations`; codex:/root/next255_science_review.

Both reviewers assessed the final record independently of its authors. Their source inspections, exact input bindings, limitations and full assessment are in the immutable YAML/Markdown bundles. Exact committed Git-object verification follows the commit before publication; merge-queue and merge tree verification is retained externally with lifecycle receipts.

## Issue disposition

[Issue #540](https://github.com/CultureBotAI/PathwayMech/issues/540) is resolved: the primary claims, preparation ledger and handoff explicitly distinguish Acinetobacter sp. SA1 and A. calcoaceticus AC3 from ADP1 and Gluconobacter IFO3244. This corrected an author-session attribution before any erroneous maintained pathway record existed. No unqualified strain transfer enters the final graph.

## Evidence limits and remaining candidates

The 1995 figure images and 1988/2004 full bodies were unavailable; precise access bounds are recorded. Native broad quinone classes are preserved without a false exact Rhea mapping. Periplasmic topology, sequence equivalence across strains, and purified same-strain full-route reconstitution are not inferred. Canonical source protein names do not override the scoped location evidence.

Every declared node/reference ID and the 16 added authority terms are listed in `identifiers.json`. The chemical, native, primary and preflight ledgers record supported facts and exclusions. Shikimate I, quinate II and shikimate II remain genuine next candidates; the ongoing discovery goal is not exhausted.

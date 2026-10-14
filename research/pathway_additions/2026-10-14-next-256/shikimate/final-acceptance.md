# Shikimate degradation I acceptance

The complete two-step `MetaCyc:SHIKIMATEDEG-PWY` record has 31 evidence-linked edges, 16 participants and three scoped taxon contexts. All 252 baseline pathway records are unchanged. Its generated network and KGX exports preserve the full evidence, reference metadata and six qualified endpoint instances.

## Validation

- `just render-pages`: 253 pathway records.
- `just validate`: records, closed schema, identifiers, provenance, source records, history and page consistency passed.
- `just test`: 4960 passed, 3 skipped, 7 warnings.
- `just lint`, `just vendored-check`, and `git diff --check`: passed.
- The saved structured reviews passed the repository archive contract check.
- Independent execution of both unchanged authority builders reproduced the promoted bytes, preserving all 4,907 prior terms, 832 prior owners and 1,008 prior manifest entries.
- All 12,611 baseline KGX edges and 4,560 baseline nodes are preserved; existing nodes only acquire this pathway context. The final exports have 12,642 edges and 4,566 nodes.

Complete gate output, environment and tested-input hashes are retained in `validation/`. Record SHA256: `ae4b0f56055956fcfe86d0d887fa4d1654efaad87a77d46bb2922335e66e4808`.

The initial full suite caught the page becoming stale when the append-only history correction was added after rendering (4,959 passed, one failed, three skipped). Exact original receipts and logs are preserved in `validation-observations/`. The final run regenerated pages, included history in the frozen input set, and reran all required gates successfully.

## Independent adversarial reviews

- [Independent integration review of shikimate degradation I](../../../../reviews/structured/20261014T180931Z-next256-independent-integration/review.yaml): `pass_with_limitations`; codex independent integration reviewer /root/next256_integration_review.
- [Independent scientific review of shikimate degradation I](../../../../reviews/structured/20261014T181132Z-next256-shikimate-scientific/review.yaml): `pass_with_limitations`; codex:/root/next256_scientific_review.

Both independent reviewers assessed the corrected final record. Their source and graph audits are retained alongside their immutable review bundles. Exact committed Git-blob verification occurs after commit and before publication; remote CI, native merge-queue tree equality, merge-integrity and branch cleanup are recorded externally in the next-256 lifecycle receipts.

## Issue disposition

[Issue #542](https://github.com/CultureBotAI/PathwayMech/issues/542) is addressed. The draft incorrectly presented historical Gluconobacter observations discussed in the 1988 paper as experiments performed in that study. The unnecessary sentence was removed; the final graph still explicitly distinguishes enzyme activity from shikimate-supported growth, mineralization and complete route reconstruction. The independent scientific reviewer verified the correction before acceptance.

[Issue #543](https://github.com/CultureBotAI/PathwayMech/issues/543) is addressed by an append-only history correction. The original scaffold default incorrectly named claude-code; its supported successor identifies Codex explicitly, preserves the original timestamp and event, and documents the correction. A subsequent `just validate-history` passed without changing tested pathway or production inputs.

## Evidence boundaries

The record preserves generic quinone classes rather than asserting an exact mapping to narrower Rhea classes. PQQ remains a separate cofactor. Native enzyme identities retain their strain, preparation and inference limits; the four PcaU/protocatechuate regulation edges preserve direct quiA versus shared quiC–quiX probe scope. The 1988 author reprint and 2005 article were read; the 2004 full body and 1995 figure images remain unavailable. The first reaction uses the native curated shikimate activity with its evidence limitations.

Ignored and hidden files were included in the bounded duplicate searches. `identifiers.json` lists all node/reference identifiers and the six added authority terms. `curation.md` and the native, primary, chemical and preflight ledgers document the strongest sources and deliberate exclusions. Quinate degradation II and shikimate degradation II remain genuine leads; the ongoing discovery goal is not exhausted.

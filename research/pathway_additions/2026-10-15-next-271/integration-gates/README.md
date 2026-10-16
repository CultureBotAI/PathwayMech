# Integration gate evidence

`gate-results.json` records the actual full test and validation results, passing lint/whitespace corrections, exact input states and every retained artifact hash. The initial failing checks are preserved alongside their verified successors. The full suite passed 7,591 tests with three empty custom-command parametrizations skipped and seven dependency warnings. Full validation passed all 268 records, 21,683 evidence blocks, 516 history records and generated-page freshness.

Raw stdout/stderr bytes are stored individually as deterministic gzip files under `logs/`; `gzip -cd logs/NAME.stdout.gz` reads a log without changing it. The index supplies both original and stored hashes and sizes. All other listed receipts are exact byte copies. This finite root-check subset does not claim to contain every scratch file or replace the separately retained complete scientific packets.

The full suite began against the 236-file candidate. The explicit successor ledger accounts for eight changed support inputs and 15 additions; product code, tests, pathway records and authority snapshots are unchanged. The affected lint, archive, attribute, generated-page and full validation checks passed on the reviewed 251-file successor. Later support retention, canonical review persistence and final PR/merge checks remain separate steps.

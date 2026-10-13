## Finding

Stable issue key: `thio-integration-history-default-actor` (P3 / provenance).

The three new, uncommitted THIO integration history records identify their actor as `claude-code` while recording `model: gpt-6` and `agent_tool: codex`. The actual work was performed by Codex. The prepared native history commands omitted `--actor-name`, so `scripts/new_history_record.py` used its documented default. The helper itself supports an explicit actor correctly.

Affected scope: the new thioredoxin CREATE event, two-label desferrioxamine EDIT event, and carrier-authority infrastructure EDIT event. No previously committed history record needs rewriting.

The original native outputs and command receipts are retained. Finish the currently running checks without changing their inputs; then replace only these three uncommitted scaffolds through the native CLI with `--actor-name codex` and truthful corrective details. Rerender and validate the corrected histories and generated pages. Preserve the earlier check inputs and results as historical evidence rather than claiming they ran against corrected history bytes.

## Acceptance checks

- All three corrected histories identify Codex consistently and use actual native timestamps/filenames.
- Original provisional histories and receipts remain retained; every committed history byte is unchanged.
- Corrected history validation, regenerated-page checks, and final staged whitespace pass.
- Native review inputs bind the corrected maintained history and exact evidence for the earlier and corrective checks.

Evidence: `/private/tmp/pathwaymech-next-233-history-actor-finding-20261012/finding.json`, SHA256 `32cbd3eea70524850e22065e95b7fa3df5290381ba693a7e156cd1ae0a6c6c1b`; full native history read `4984b1/0`.

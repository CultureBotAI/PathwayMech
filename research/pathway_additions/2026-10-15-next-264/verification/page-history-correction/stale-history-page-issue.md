PR #575's first GitHub QC run fails `tests/test_render_pages.py::test_the_committed_site_is_current` for `pages/records/MetaCyc_PWY-2503.html`.

Independent reproduction identifies an omitted regeneration step, not a renderer defect. The final record-history entry `history/records/benzoate-degradation-i-aerobic/2026-10-15T102211Z-Codex-c5acee.yaml` was added after the initial full render/validation run. `load_site_history` feeds that entry into `_record_page`, but the later documentation checks did not rerun the page check.

- Committed page SHA256: `98e5b35bd640e5292c70a7ea05412078e321ba0e19451a66e8c6e118f853544e` (336,400 bytes).
- Native rendering with the current complete history: `4e637a583fc5bbccb0b2b25ccac95b1b2b03b0dfedaff2b267068f7c9c2d37fe` (337,699 bytes).
- Omitting only the late history entry in an isolated read-only reproduction gives the exact committed page. No maintained input was removed in that experiment.
- The pathway YAML, graph relationships, evidence, authorities and renderer code remain unchanged.

Severity: minor publication/provenance defect. The existing page test correctly detects it; no new test or renderer-code change is needed.

Acceptance: retain the failed CI observation and independent diagnosis; run the native renderer after all record-history changes; prove only the expected history block changes and graph/data/KGX stay exact; run required checks against the refreshed page; save a bounded successor review that includes history among generated-input owners; update PR #575 and require green protected CI before merge. Keep prior frozen proof and canonical reviews immutable.

CI run: https://github.com/CultureBotAI/PathwayMech/actions/runs/38720895009

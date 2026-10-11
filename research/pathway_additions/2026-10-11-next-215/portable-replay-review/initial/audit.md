# Independent B portable replay review

The original helper needs correction for **#396**. A real concurrent copied-target edit during startup was accepted: the helper exited 0, reported target SHA `891ce5a5…`, but its captured target and the YAML it later validated had SHA `394ff752…`. The pre-probe cached digest and post-probe snapshot refer to different versions. Exact commands, original hashes, logs and receipts are preserved in `finding.json` and `pre-capture-race/`.

The full positive replay checked 62 original bodies, seven native reactions, 40 reaction sides, seven balances and actual 44-node/72-edge/129-evidence KGX. Sixteen independent invalid-input controls rejected correctly. A real concurrent final-output creation was rejected while preserving its sentinel. Those successes do not remove the startup provenance defect or approve the initial record’s two known sequence-locator errors.

The same target-edit probe against A helper `0b669333…` rejected with `Stale source projection target` and emitted no receipt. A captures and hashes its target after the probe, unlike B. This establishes a narrow distinction; it is not an exhaustive safety claim about A or other helpers.

All sealed handoff files were rehashed unchanged. Only external test copies and evidence were written. Root filed https://github.com/CultureBotAI/PathwayMech/issues/396. The corrected B successor will be assessed separately.

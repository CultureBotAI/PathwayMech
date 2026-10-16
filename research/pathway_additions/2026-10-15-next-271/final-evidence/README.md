# Final evidence retention for next271

This is mechanical preservation of four explicitly released frozen packets: the authority implementation, its independent review, the canonical pre-save evidence subset, and the integration adversary. It supplies no new scientific verdict, gate result, issue closure or publication acceptance. Each original report preserves its authorship, independence, baseline and limits.

`retention.json` inventories every outer member and archive, including hidden/ignored files, original manifests/freezes, and failed attempts. Tar members are sorted regular files with fixed metadata; gzip uses an empty filename and mtime 0. Every compressed artifact is below 40 MiB. Every archive was fully decoded, every member checked against the frozen source and manifest, and a second independent serialization reproduced each compressed hash exactly. Source trees were read directly without duplicating whole raw trees. Nested containers remain opaque byte-exact payloads; no inner scientific rereading is asserted.

`readable/` contains 15 whole-report byte copies taken from the indexed originals, with their original filenames and hierarchy. These are not rewritten summaries. The authority author has no top-level REVIEW/RESULT pair, so its HANDOFF/OPERATIONS/REPRODUCE/check receipts are exposed. The canonical subset has no final verdict pair: its HANDOFF, SCIENTIFIC-ASSESSMENT, OPERATIONS and pre-save result retain the pending-gate qualification. The independent authority and integration packets expose their actual REVIEW/HANDOFF/RESULT. Each readable copy is checked against its corresponding archived member.

Root's separate final gate logs and the final saved canonical review pair are deliberately excluded, avoiding provenance cycles. The original authority release and its independently reviewed single-file attribute successor remain distinct inside their original packets. Later helper formatting, page freshness, full gates and publication scopes are not inferred from this packaging.

Portable verification with the existing runtime:

```sh
python -B retain.py verify --output .
python -B check_archived_manifests.py .
```

An optional `--sources-root /private/tmp` also rechecks all original frozen owners against `packets.json`; source paths are relative to that root, including the canonical pre-save subdirectory. A complete deterministic rebuild uses `retain.py build --output NEW_DIRECTORY --sources-root /private/tmp` and requires a fresh destination. Never rebuild into this retained owner. No network, dependency installation or external cache is needed.

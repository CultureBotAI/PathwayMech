# Local execution receipts

`execution-index.json` describes the exact scope and environment of these native
commands. Each receipt retains its actual command, start/finish time, starting
input hashes, exit code, and stdout digest.

The repository stores native command logs losslessly as `.log.gz`. Decompress
the file named in `stdout-retention.json` to obtain the corresponding `.log`
named in each execution receipt and review evidence locator. Both compressed
and uncompressed hashes are recorded and every stream was verified after
compression. This preserves the original test warning's whitespace. Uncompressed
local copies remain ignored; no log content was edited.

The local full test suite started before the final ten membership-evidence text
values changed. Its original starting hash is retained. Stable final QC and
independent source/delta review cover those edits; exact final-head GitHub checks
remain required before merge.

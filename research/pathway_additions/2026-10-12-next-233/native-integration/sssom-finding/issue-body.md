## Finding

Stable issue key: `thio-integration-stale-sssom-export` (P3 / generated artifact).

The actual maintained test suite finished with 3,209 passed, three skipped and one failure: `tests/test_sssom_export.py::test_committed_sssom_output_is_current`. The integration plan rendered pages and scheduled KGX export but omitted the native SSSOM export.

The accepted thioredoxin record already contains three exact source mappings, for native NADP, NADPH and PROTON identifiers. The committed `output/sssom/source_mappings.sssom.tsv` therefore lacks precisely three new THIO rows. The test-generated expectation retains every old line and row in order. No scientific record, source mapping, export code or test waiver is needed.

Run the native SSSOM exporter, retain the failed suite and its exact original/expected files, and rerun the full maintained checks against the corrected export and history. Add the generated SSSOM file to the explicit integration change plan.

## Acceptance checks

- The native export matches the actual test-generated expectation exactly.
- All old mapping rows and metadata are preserved, with only the three THIO rows added.
- The full test suite and remaining maintained gates pass on the corrected files.
- The failed first attempt remains recorded and is not relabeled as successful.

Evidence: `/private/tmp/pathwaymech-next-233-sssom-export-finding-20261012/finding.json`; actual full-suite terminal `19c910/1`, exact export difference `8f15a8/0`.

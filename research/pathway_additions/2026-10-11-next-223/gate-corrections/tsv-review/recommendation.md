# Narrow review of the trailing empty TSV-field remedy

**Recommend option A: encode an empty terminal field as the CSV-quoted empty string `""`.** The parsed `endpoint_qualifiers` value remains the empty string. Do not replace it with JSON `[]`, omit the column, or exempt the generated file from whitespace checks.

The current `_tsv` function in `src/pathwaymech/kgx.py:289` uses a fixed tab delimiter and LF record terminator. Every data cell first passes through `_cell`, which replaces literal tabs/CR/LF and strips surrounding whitespace. Its `csv.DictWriter` therefore produces `\t\n` only for an empty last cell. After CSV serialization, the bounded replacement below quotes that structural empty field without touching any populated cell or its CSV escaping:

```python
return stream.getvalue().replace("\t\n", '\t""\n')
```

Add a brief comment connecting this operation to normalized single-line cells and Git's trailing-whitespace check. Both `write_kgx` and `render_kgx` already use this one serializer, so no second export implementation is needed. The fixed production column names contain no tabs or newlines. This recommendation relies on the existing cell normalization and LF terminator; retain those invariants rather than generalizing the substitution to arbitrary unnormalized CSV.

The reviewer made no maintained edits. `assessment-probes.py` applied the proposal externally to the actual generated files and adversarial synthetic values (terminal `28c1cc`, exit 0):

- All 10,922 parsed edge rows remain exactly equal, including IDs, empty strings and the three populated qualifier payloads. Exactly 10,919 terminal empty cells become quoted.
- All 3,845 node rows and the complete node-file bytes remain unchanged.
- Eight synthetic cases retain empty/None values, a literal pair of quote characters, a lone quote, quoted text, Unicode, JSON with escaped controls and quotation marks, and normalized whitespace. Earlier cell values are preserved.
- The proposed full edge TSV contains no physical line ending in a tab or space. `git diff --no-index --check /dev/null <external-proposed-file>` emitted no diagnostics. Its exit 1 is the normal no-index difference status for a newly supplied file, not an observed whitespace-check diagnostic.

Minimal meaningful regression coverage: extend `test_write_kgx_uses_lf_tsv_with_stable_headers` to assert a normal unqualified edge ends in the quoted empty cell, no TSV line has trailing tabs/spaces, and `csv.DictReader` recovers `endpoint_qualifiers == ""` with the complete column set. Add one small serializer round-trip test containing the synthetic empty/literal-quote/Unicode/JSON cases. Existing `test_kgx_roundtrip_retains_qualifier_payload_and_qualifier_only_citations` already compares disk and render output and protects populated JSON qualifications; keep it in the focused run. Finally re-render and perform the real staged `git diff --cached --check`, plus parsed full-export preservation, after adopting the fix.

The previous successful checks did not include this whole staged edge-file whitespace check. This new finding does not retroactively invalidate their narrower scopes, nor does it justify treating the still-running full suite as failed or timed out. This assessment is scoped to serialization and read-only proposed-output equivalence, not final maintained gates, PR or merge acceptance.

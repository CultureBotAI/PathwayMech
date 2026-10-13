# Final artifact preservation review

Against reviewed HEAD `70903536191206d2586cd23e46f7d70c32fef92e`, the completed generators pass **35 targeted preservation checks**. The checker only reads the checkout and writes an external report.

- All 242 pathway YAML paths were inventoried including hidden/ignored files; the sole record change is acetoacetate's RHEA:21038 direction scalar.
- All 12,125 KGX edges remain byte-exact. Node identities/order are unchanged. Only RHEA:21038 changes: global direction is restored from blank to `right_to_left`, and its aceto source context has the same single corrected direction. All other fields and contexts are exact, with expected deterministic context sorting.
- Both download TSVs equal their corresponding output files. All manifest checksums/counts and the concatenated graph version are valid; other manifest metadata is unchanged. The homepage changes only its graph-version checksum.
- All 70 SSSOM rows and their column header remain byte-exact.
- The aceto page's complete parsed DOM is identical after accounting for the two accessible graph-direction strings, the component table's direction cell, the dependent SVG digest/reference substitution, and one new curation-history entry. The new entry's path, record target, timestamp, actor, event summary and event details agree with the maintained history source; the old history entry is exact. No other record page, graph edge, label, evidence table, reference, style or script content changes.
- The complete tracked generated-artifact delta is precisely the aceto page, node TSV counterparts, download manifest, homepage version and the SSSOM header, plus the single YAML scalar.

New history source: `history/records/acetoacetate-degradation/2026-10-13T043250Z-codex-01bcaa.yaml`.

The checker was prepared before inspecting final outputs and run only after root reported both generators complete. Three preparatory checker defects were corrected without product edits: the initial YAML inventory incorrectly included tracked `.gitkeep`; the first component-row XPath also matched mechanism-table rows; and the initial history accessor expected a top-level timestamp instead of `session.timestamp`. The final 35 checks all pass. These failures concern the external checker, not the generated artifacts. No broad suite, builder, or generator was run by this reviewer.

Checker: `/private/tmp/pathwaymech-publish243-final-preservation-check-20261013.py` — SHA-256 `b16d36dc0557601eb1d9e7468e6d4834f98fe8d3f038f58b5a80dee4704e4bf2`.

Result: `/private/tmp/pathwaymech-publish243-final-preservation-result-20261013.json` — SHA-256 `c5f701e559a0c45909ba007aa35236adde02b44c2840511de571897a3e389722`.

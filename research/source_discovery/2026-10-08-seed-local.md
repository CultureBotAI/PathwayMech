# Native SEED subsystem local ingestion — 2026-10-08

**Result:** ingested the native `Glyoxylate bypass` subsystem as local support,
including 13 ordered role definitions and 4,445 genome-specific variant rows
(27,207 role cells, 31,933 feature memberships representing 31,926 unique native
feature IDs). This adds native role abbreviations, variant codes and curator
metadata beyond downstream BV-BRC pathway calls. It creates no maintained pathway
record, taxon assertion, biochemical reaction ordering or experimental evidence.

The data bytes and derived TSV remain in the local bundle. Source requests,
response digests and counts are committed in
[the metadata directory](2026-10-08-seed-local/). Public-release licensing review
is deferred under the user's instruction; source attribution is retained. The
SEED software license is not treated as a verified license for these data.

## Access and exact source

The official [SEED download tutorial](https://blog.theseed.org/servers/2010/08/downloading-a-subsystem.html)
and [live Sapling API documentation](https://pubseed.theseed.org/sapling/server.cgi?pod=SAP)
describe subsystem role and genome/variant retrieval. Ordinary unauthenticated
HTTPS requests worked on 2026-10-08 despite web-fetch failure and timeout of the
interactive per-subsystem HTML views. The public selector listed 1,364 completed
subsystems; this is a web-view count, not a claim about the full API catalogue.
Only two named subsystems were acquired, not the whole catalogue.

Endpoint: `https://pubseed.theseed.org/sapling/server.cgi`. Each response was
requested by URL-encoded POST fields `function`, `encoding=json`, and `args`
containing the JSON parameters. The successful canary used exactly:

| Function | JSON parameters |
| --- | --- |
| `subsystem_roles` | `{"-ids":["Glyoxylate bypass"],"-aux":1,"-abbr":1}` |
| `pegs_in_variants` | `{"-subsystems":["Glyoxylate bypass"]}` |
| `subsystem_data` | `{"-ids":["Glyoxylate bypass"],"-field":"version"}` |
| `subsystem_data` | `{"-ids":["Glyoxylate bypass"],"-field":"curator"}` |
| `subsystem_data` | `{"-ids":["Glyoxylate bypass"],"-field":"description"}` |

The native source reports version `140` and curator `SvetaG`. This version is
not a source modification timestamp. Each request's UTC acquisition timestamp is
recorded separately; these five requests are not a transactional database snapshot.
Requests include auxiliary roles, so feature cells are joined against the entire
returned role list. No genome filter is applied to the admitted bundle.

[The pinned official client](https://github.com/TheSEED/seed_svr/blob/b620c74e0bc90ae508eaf29dae79334a7dd4aeaf/scripts/svr_subsystem_spreadsheet.pl)
confirms the pair orientation and spreadsheet semantics. The raw API role tuple
is `[full role name, abbreviation]`; the tutorial's display TSV reverses those
columns. The adapter consumes the raw API orientation.

## Data contract and limitations

- `subsystem_roles` is an ordered list of role/abbreviation pairs. Position is
  spreadsheet alignment, not temporal or causal reaction order. Repeated pairs
  are retained as repeated positions.
- `pegs_in_variants` maps native genome IDs to `[variant, [role, feature, ...], ...]`.
  Genome IDs may carry region strings. They remain opaque SEED IDs; decimal
  prefixes are not promoted to NCBI taxonomy identifiers.
- Feature IDs, role strings and variant codes remain unchanged. Empty or negative
  variants are supported. Empty cells and absent roles do not imply verified
  biological absence; no native variant is translated to an experimental claim.
- The successful canary contains only variant `"1"`, including all 4,445 returned
  genome rows. Its nontransactional source responses have complete role joins.
- One TSV row is emitted per native role occurrence, per genome row, and per
  metadata field. `native_value_json` preserves the entire native value, including
  feature multiplicity and source cell order. The output has 4,461 data rows.
- Every output row retains source filename, SHA-256, endpoint, function,
  parameters, acquisition timestamp, subsystem version and manifest SHA-256.
  The manifest records acquisition provenance; it is not remote authentication.
- Full input is validated before output. Wrong subsystem scope, incomplete
  auxiliary roles, unknown role joins, duplicate JSON keys, repeated role cells,
  invalid payloads and hash mismatches fail. Raw snapshots remain available for
  review rather than being silently repaired or dropped.

## Rejected alanine canary

`Alanine biosynthesis` version `267`, curator `OlgaZ`, returned 6,690 genome rows
and 13 role positions representing 12 distinct role names. Its duplicate `AvtA`
pair is preserved by the native representation, but the full bundle fails a
separate role-join check: the role dictionary names AlaB `Alanine transaminase
(EC 2.6.1.2)` while genome cells use `Glutamate-pyruvate aminotransferase
(EC 2.6.1.2)`. Equal EC numbers do not authorize an inferred synonym join.

These 6,690 rows are **acquired but rejected**, not included in the ingestion
count. Their source responses and manifest are retained locally. Counts and the
unmapped role are recorded in `audit.json`; this offers a concrete next step if
upstream reconciliation is later requested. The actual alanine snapshot also
contains seven native `"-1"` variants; the importer tests preserve negative and
empty variants without assigning biological interpretations.

## Reproduce and verify

Place the five hash-matched `glyoxylate_*.json` responses beside the committed
`glyoxylate-manifest.json`, then run:

```bash
uv run pathwaymech-import-seed-subsystems /path/to/glyoxylate-manifest.json > glyoxylate-native.tsv
```

The source manifest pins the 1,961,308-byte variant response to
`e74fb0e37dc47273bd4b45bad49746da05df97ea44b43c922752853a0c092cac`.
The initial successful TSV is 3,582,562 bytes, SHA-256
`941bfe6dee78ea96de85fb4f010eeca537a7d5a3f4cfb584283f9b2554c335e0`.
These values are also in `audit.json`. API responses may change on reacquisition;
new bytes require a new manifest, not replacing the old digest.

Verification: the synthetic adapter tests exercise lossless JSON-in-TSV
roundtrips, duplicate role positions, negative/empty variant codes, empty genome
rows, native region IDs, malformed data, traversal, request scope and digest
binding. A separate independent check round-trips every real genome/role value
against the acquired JSON. Alanine's unmapped role is refused before output.

The durable local bundle and batch boundaries are recorded in the
[DRAM/SEED batch report](2026-10-08-dram-seed-ingestion.md).

# Curation history

Append-only provenance for curation sessions. **One record per change**: per
pathway for hand curation, per *migration* for a bulk edit. A record is written
once and **never edited afterwards**; a correction is a new record that names
the old one in its `details`.

```
history/<kind-dir>/<slug>/<TIMESTAMP>-<actor>-<shortid>.yaml
```

The schema (`src/pathwaymech/schema/history.yaml`) is vendored from
culturebotai-claw. The scaffolder and validator in `scripts/` are this
repository's and need no claw checkout.

This is a different layer from a record's own optional `curation_history` slot.
That slot says what changed inside one pathway record. A history record can
also say that a source was re-read, that a gate was adopted and what it found,
or that a review deliberately changed nothing, and which tool or model did it,
under which issue.

## Writing a record

Do not hand-write the filename or timestamp; scaffold it:

```bash
just new-history --kind record --slug arginine-biosynthesis \
  --target-root data/pathways \
  --event REVIEW --outcome no_change \
  --summary "Checked every edge's quote against its reference" \
  --model claude-opus-5-5 --agent-tool claude-code \
  --issue https://github.com/CultureBotAI/PathwayMech/issues/1 \
  --details "What was done, what evidence was used, how it was validated."
```

Omit `--details` and you get a TODO placeholder, and `just validate-history`
**fails** while it is still there. The command prints the record path as its
final stdout line.

`--kind record` and `--kind schema` derive the target path from `--slug` plus
`--target-root`. Every other kind should pass an explicit `--path`.

Then validate and stage:

```bash
just validate-history history/records/arginine-biosynthesis/<file>.yaml
git add history/
```

## The vocabulary

`event`: `CREATE` · `EDIT` · `REVIEW` · `AUDIT` · `GENERAL`

`outcome`: `changed` · `no_change` · `needs_followup` · `blocked`

`kind`: `record` · `schema` · `mapping` · `report` · `infrastructure` · `other`
(`other` requires an explicit `--path`).

## One record per change, not per file

| What happened | `--kind` | Target |
|---|---|---|
| one pathway, curated | `record` | that pathway's YAML under `data/pathways/` |
| an import, re-seed or bulk edit | `infrastructure` | the script that made it |
| a schema change | `schema` | the schema file |
| a source-inventory change | `other` | `conf/sources.yaml` |
| a research note | `other` | the note under `research/` |

## What is checked

`just validate-history`, and `just validate` through `pathwaymech-run-qc`,
validates every record against the vendored schema and checks that its links
resolve. CI runs the same gate. Records are append-only by convention, not by
a gate.

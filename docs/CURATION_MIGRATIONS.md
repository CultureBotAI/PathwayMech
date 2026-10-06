# Reproducing bounded curation migrations

The October 2026 migrations are historical curation stages. Replaying an early
stage over the final corpus would restore rejected source assertions or remove
later enrichment. GO-CAM native, diagram and MetaCyc reconstruction therefore
require every target to match the reviewed Git baseline,
`88744403c934a84828d373cfccb8cdaa7507ad77`. The MetaCyc `--baseline-ref` option
selects an explicit alternative baseline; it also checks the destination records
against that revision. It does not authorize overwriting a different state.

Use current migration code with records in an isolated baseline checkout. For
example, from the current repository:

```bash
git worktree add --detach /tmp/pathwaymech-reproduction \
  88744403c934a84828d373cfccb8cdaa7507ad77

PYTHONPATH=src .venv/bin/python scripts/curate_diagram_causal_graphs.py \
  --root /tmp/pathwaymech-reproduction \
  --cache "$CACHE" --chebi-db "$CHEBI_DB" \
  --report /tmp/pathwaymech-preview/diagram-review.json
```

This previews the changes without writing pathway records. Inspect the new
report, then repeat with `--apply` to apply to that isolated checkout. GO-CAM
native, complex and location scripts use the existing `--write` spelling;
all other mutators use `--apply`. The chemical supplement now also defaults to
preview and requires `--apply` for record writes. Baseline and source checks
remain active under `python -O`.

Pass `--records /tmp/pathwaymech-reproduction/data/pathways` to scripts that
accept a records directory. For MetaCyc, pass `--root` and use a fresh
`--report-dir`. Later targeted chemistry migrations operate on the intermediate
state produced by their prerequisite stages and check their exact record/source
preconditions. They are not a supported way to refresh the final corpus.

All mutators validate the complete proposed cohort with the semantic and closed
LinkML validators before publication. They serialize and stage every output
before replacing a record or report, so a late record error, source failure or
unwritable report destination does not publish earlier candidates. Replacements
are atomic per file; this does not promise crash-atomic publication of an entire
multi-file cohort.

Applied reports and historical reports without an `applied` flag are immutable.
A no-op replay preserves them byte for byte. A changed candidate needs a new
report path; dry runs cannot replace applied evidence ledgers. Preview reports
carry `applied: false` and may be replaced by a subsequent preview or application.
Supplemental source ledgers are preserved unless their bytes already match the
proposed output; use a new report directory for different supplemental outputs.

Do not replace committed source-exclusion ledgers to document a later audit.
Create a separate report and an append-only history record identifying the
earlier curation and the new evidence or implementation change.

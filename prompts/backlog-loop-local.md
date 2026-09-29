# PathwayMech backlog loop: local rules

The canonical `prompts/backlog-loop-goal.md` owns the loop; this file adds
PathwayMech's gates and data rules to it.

## Gates

- `just validate` runs the skills check and `pathwaymech-run-qc`: record
  validation, the closed LinkML schema, provenance, sources, docs, the
  research report contract and `pages/` drift. `just test` and `just lint` are
  the rest of CI.
- `just vendored-check` confirms the claw-governed files match the pin.

## Data rules

- One pathway per YAML file under `data/pathways/`. Every causal edge cites a
  reference declared in the same record, with a short verbatim quote.
- After any record change, run `just render-pages` and commit `pages/` with it.
- `conf/sources.yaml` ranks source families. A missing pathway family is a
  candidate to *recommend*, not to pick: drafting or editing a curated record
  needs the user's explicit go-ahead, as the canonical loop says.

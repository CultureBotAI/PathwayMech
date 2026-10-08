set dotenv-load := true

validate: validate-skills
    uv run pathwaymech-run-qc

# Every record against the closed LinkML schema (also run by `validate`).
validate-strict *args:
    uv run pathwaymech-validate-strict {{args}}

check-identifiers *args:
    uv run pathwaymech-check-identifiers {{args}}

validate-skills:
    uv run python scripts/validate_claude_skills.py

test:
    uv run --extra dev pytest

lint:
    uv run --extra dev ruff check .

render-pages:
    uv run pathwaymech-render-pages

kgx-export *args:
    uv run pathwaymech-export-kgx {{args}}

# Inventory UniProt proteins in sibling Mech checkouts against PathwayMech
# participants and check sibling PathwayMech links (conf/sibling_mechs.yaml).
# Local files only unless --fetch-sgd-map / --fetch-annotations is passed.
# See .claude/skills/cross-mech-protein-links/SKILL.md for pinned audit inputs.
cross-mech-proteins *args:
    uv run pathwaymech-cross-mech-proteins {{args}}

sssom-export *args:
    uv run pathwaymech-export-sssom {{args}}

backfill-source-mappings *args:
    uv run python scripts/backfill_source_mappings.py {{args}}

# Fails if pages/ is not what the records render to (also run by `validate`).
check-pages:
    uv run pathwaymech-check-pages

# Verify every claw-governed vendored file matches the pinned canonical
# revision in scripts/.vendored_canon_ref (the check the vendored-sync workflow
# runs). Needs network access to fetch the pinned claw revision.
vendored-check:
    bash scripts/check_vendored_sync.sh

seed:
    uv run pathwaymech-seed-from-sources

# Scaffold an append-only curation-history record (history/<kind>/<slug>/...).
# See history/README.md. Needs no claw checkout.
new-history *args:
    uv run python scripts/new_history_record.py {{args}}

# Validate history records (default: all of history/) against the vendored
# schema. `just validate` runs this too, through pathwaymech-run-qc.
validate-history *args:
    #!/usr/bin/env bash
    set -euo pipefail
    targets=({{args}})
    if [ "${#targets[@]}" -eq 0 ]; then targets=(history); fi
    for target in "${targets[@]}"; do
      uv run python scripts/validate_history.py "$target"
    done

stage-imodulondb *args:
    uv run python scripts/stage_imodulondb_pathway_contexts.py {{args}}

[positional-arguments]
import-biopax *args:
    uv run pathwaymech-import-biopax "$@"

import-bigg *paths:
    uv run pathwaymech-import-bigg {{paths}}

import-brenda *args:
    uv run pathwaymech-import-brenda {{args}}

import-bvbrc *paths:
    uv run pathwaymech-import-bvbrc {{paths}}

[positional-arguments]
import-dbcan-pul *args:
    uv run pathwaymech-import-dbcan-pul "$@"

import-gapmind *paths:
    uv run pathwaymech-import-gapmind {{paths}}

import-gocam *paths:
    uv run pathwaymech-import-gocam {{paths}}

import-go *paths:
    uv run pathwaymech-import-go {{paths}}

import-hadeg *args:
    uv run pathwaymech-import-hadeg {{args}}

import-kegg *paths:
    uv run pathwaymech-import-kegg {{paths}}

import-mibig *paths:
    uv run pathwaymech-import-mibig {{paths}}

import-metacyc *paths:
    uv run pathwaymech-import-metacyc {{paths}}

import-modelseed *paths:
    uv run pathwaymech-import-modelseed {{paths}}

import-pmn *paths:
    uv run pathwaymech-import-pmn {{paths}}

import-rhea *paths:
    uv run pathwaymech-import-rhea {{paths}}

import-unipathway *paths:
    uv run pathwaymech-import-unipathway {{paths}}

import-veupathdb *paths:
    uv run pathwaymech-import-veupathdb {{paths}}

import-wikipathways *paths:
    uv run pathwaymech-import-wikipathways {{paths}}

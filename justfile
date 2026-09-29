set dotenv-load := true

validate: validate-skills
    uv run pathwaymech-run-qc

# Every record against the closed LinkML schema (also run by `validate`).
validate-strict *args:
    uv run pathwaymech-validate-strict {{args}}

validate-skills:
    uv run python scripts/validate_claude_skills.py

test:
    uv run --extra dev pytest

lint:
    uv run --extra dev ruff check .

render-pages:
    uv run pathwaymech-render-pages

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

stage-imodulondb *args:
    uv run python scripts/stage_imodulondb_pathway_contexts.py {{args}}

import-biopax *args:
    uv run pathwaymech-import-biopax {{args}}

import-bigg *paths:
    uv run pathwaymech-import-bigg {{paths}}

import-bvbrc *paths:
    uv run pathwaymech-import-bvbrc {{paths}}

import-gocam *paths:
    uv run pathwaymech-import-gocam {{paths}}

import-go *paths:
    uv run pathwaymech-import-go {{paths}}

import-kegg *paths:
    uv run pathwaymech-import-kegg {{paths}}

import-mibig *paths:
    uv run pathwaymech-import-mibig {{paths}}

import-metacyc *paths:
    uv run pathwaymech-import-metacyc {{paths}}

import-modelseed *paths:
    uv run pathwaymech-import-modelseed {{paths}}

import-rhea *paths:
    uv run pathwaymech-import-rhea {{paths}}

import-wikipathways *paths:
    uv run pathwaymech-import-wikipathways {{paths}}

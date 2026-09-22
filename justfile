set dotenv-load := true

validate: validate-skills
    uv run pathwaymech-run-qc

validate-skills:
    uv run python scripts/validate_claude_skills.py

test:
    uv run --extra dev pytest

lint:
    uv run --extra dev ruff check .

render-pages:
    uv run pathwaymech-render-pages

seed:
    uv run pathwaymech-seed-from-sources

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

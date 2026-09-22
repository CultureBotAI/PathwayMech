set dotenv-load := true

validate:
    uv run pathwaymech-run-qc

test:
    uv run --extra dev pytest

lint:
    uv run --extra dev ruff check .

render-pages:
    uv run pathwaymech-render-pages

seed:
    uv run pathwaymech-seed-from-sources

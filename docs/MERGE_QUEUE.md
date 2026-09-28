# Merge Queue

Before merging a curation pull request:

1. Confirm that `just validate` passes.
2. Confirm that every mechanistic edge has reference-backed evidence.
3. Confirm that generated pages were refreshed when curated YAML changed
   (`just check-pages`, also part of `just validate` and of CI).

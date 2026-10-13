# Issue 504 implementation handoff

Issue: https://github.com/CultureBotAI/PathwayMech/issues/504
Checkout: `/private/tmp/pathwaymech-next-243-local-20261012`.

Changed only `src/pathwaymech/identifiers.py` and new `tests/test_typed_authority_consumer_integrity.py`.

The consumer now inventories retained typed identities before selected terms choose an owner. It compares full retained projections and native release for BioCyc kinds, includes both protein-state originals and every retained Rhea Polymer member, rejects cross-kind collisions, and binds selected terms to the established native kind. Ordinary reaction IDs are included despite their older reduced metadata. Rhea Polymer duplicate comparison retains the producer's cross-release compatibility for identical facts. Existing aceto original/provenance checks, compatible companion owners, first-owner output, and the native-pathway/SGD compatibility branch are preserved. No schema, producer, authority, scientific record, or generated output changes.

The 87 dedicated regressions cover legacy term rebinding, complete-owner producer/consumer parity in both orders and selected/unselected cases, identical duplicates, state counterparts, unselected polymer members, cross-kind owners, release conflicts, aceto compatibility, end-to-end identifier failure, and exact current authority terms. The original pre-fix reproduction now rejects every previously accepted corruption; its post-fix stdout is `/private/tmp/pathwaymech-publish243-runtime-repro-fixed-20261013.stdout`.

Commands were run from the checkout with:

```bash
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src:tests:. /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/PathwayMech/.venv/bin/python -m pytest -q tests/test_typed_authority_consumer_integrity.py
```

Result: **87 passed in 4.77 s**. Captured at `/private/tmp/pathwaymech-publish243-runtime-focused-tests-20261013.stdout`.

```bash
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src:tests:. /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/PathwayMech/.venv/bin/python -m pytest -q tests/test_biocyc_carrier_authority.py tests/test_electron_transfer_authority.py tests/test_nitrate_native_authority.py tests/test_named_complex_consumer_conflicts.py tests/test_aceto_authority.py tests/test_aceto_legacy_cycles.py tests/test_protein_carrier_reaction_authority.py tests/test_protein_carrier_preselection.py tests/test_pathbank_context_authority.py tests/test_identifier_snapshot_builders.py
```

Result: **2,148 passed in 108.18 s**. Captured at `/private/tmp/pathwaymech-publish243-runtime-affected-tests-20261013.stdout`.

```bash
/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/PathwayMech/.venv/bin/ruff check src/pathwaymech/identifiers.py tests/test_typed_authority_consumer_integrity.py
/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/PathwayMech/.venv/bin/ruff format --check src/pathwaymech/identifiers.py tests/test_typed_authority_consumer_integrity.py
```

Results: **All checks passed; 2 files already formatted**. No commits, staging, branch changes, or external actions. Root owns independent review, final combined gates, history, and publication.

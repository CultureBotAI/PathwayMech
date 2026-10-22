# Stage 6 Infrastructure Implementation Plan (`mech-goal-sequence-20261019` / Cycle 1 / Stage 6)

## 1. Frozen Scope & Provenance

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `1`
- **Stage**: `6` (`infrastructure`)
- **Revision**: `1`
- **Source revision (`main` base)**: `e8f3fcc82ab9de3aa8d47f5e41b07c07a09159a9`
- **Supervisor-frozen `INFRA_TASKS.md` cutoff**: `2026-10-22T04:59:06Z`
- **Frozen snapshot artifact**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-06/revision-0001/infra_snapshot.md` (`sha256: 842d392d3e6a1dcec5507c958d4add01b8a1f270943c5d0788f88d151dd08c94`, `14811` bytes)
- **Frozen task inventory**: 5 tasks (`pathwaymech-infra-0001`, `pathwaymech-infra-0002`, `pathwaymech-infra-0003`, `pathwaymech-infra-0004`, `pathwaymech-infra-0005`)

## 2. Issue Intake & Dependency Graph

Every frozen task in `INFRA_TASKS.md` was deduplicated against open and closed issues in `CultureBotAI/PathwayMech` and linked to a real GitHub issue:

| Task ID | Originating Stage | GitHub Issue | Priority | Dependencies | Stage 6 Disposition |
| --- | --- | --- | --- | --- | --- |
| `pathwaymech-infra-0001` | Cycle 1 Stage 1 (`add_records`) | [#673](https://github.com/CultureBotAI/PathwayMech/issues/673) | medium | Per-slice upstream `UniProtKB` / `RHEA` / `PMID` authority inspection during Stage 1 (`add_records`) | `deferred` (carried forward to Cycle 2 Stage 1) |
| `pathwaymech-infra-0002` | Cycle 1 Stage 2 (`causal_graphs`) | [#674](https://github.com/CultureBotAI/PathwayMech/issues/674) | medium | None (`src/pathwaymech/curation.py`) | `resolved` |
| `pathwaymech-infra-0003` | Cycle 1 Stage 2 (`causal_graphs`) | [#675](https://github.com/CultureBotAI/PathwayMech/issues/675) | low | None (`src/pathwaymech/schema/pathwaymech.yaml`, `src/pathwaymech/schema.py`, `src/pathwaymech/kgx.py`) | `resolved` |
| `pathwaymech-infra-0004` | Cycle 1 Stage 3 (`protein_examples`) | [#676](https://github.com/CultureBotAI/PathwayMech/issues/676) | medium | None (`src/pathwaymech/sssom.py`, `output/sssom/source_mappings.sssom.tsv`) | `resolved` |
| `pathwaymech-infra-0005` | Cycle 1 Stage 4 (`record_review`) | [#677](https://github.com/CultureBotAI/PathwayMech/issues/677) | medium | Coordinates with `pathwaymech-infra-0003` in `src/pathwaymech/schema.py`, `src/pathwaymech/kgx.py`, and `tests/test_linkml_schema.py` | `resolved` |

### Dependency Analysis & Execution Order

1. **`pathwaymech-infra-0002` ([#674](https://github.com/CultureBotAI/PathwayMech/issues/674)) — Independent writer upgrade (`src/pathwaymech/curation.py`)**:
   - Can execute first with zero coupling to schema or export modules.
   - Ensures any future `publish_curation` runs preserve per-file YAML line-wrap widths (`80`, `88`, `100`, `120`, `4096`) and YAML anchor/alias structure (`&id001`/`*id001`).
2. **`pathwaymech-infra-0004` ([#676](https://github.com/CultureBotAI/PathwayMech/issues/676)) — Independent SSSOM export upgrade (`src/pathwaymech/sssom.py`)**:
   - Can execute independently of schema and curation modules.
   - Adds `Entrez`, `gomodel`, `NCBIProtein`, `Reactome`, and `SGD` prefix declarations to `CURIE_MAP` in `src/pathwaymech/sssom.py` and updates `output/sssom/source_mappings.sssom.tsv`.
3. **`pathwaymech-infra-0003` ([#675](https://github.com/CultureBotAI/PathwayMech/issues/675)) & `pathwaymech-infra-0005` ([#677](https://github.com/CultureBotAI/PathwayMech/issues/677)) — Co-located schema & KGX export upgrades (`src/pathwaymech/schema/pathwaymech.yaml`, `src/pathwaymech/schema.py`, `src/pathwaymech/kgx.py`)**:
   - Both tasks modify `src/pathwaymech/schema.py`, `src/pathwaymech/kgx.py`, and `tests/test_linkml_schema.py`; implementing them together ensures open (`validate_record`) and closed (`strict_errors` / `SchemaView`) LinkML validators and `LOCAL_PREDICATE_CURIES` / `_PREFIX_CATEGORIES` stay strictly synchronized.
4. **`pathwaymech-infra-0001` ([#673](https://github.com/CultureBotAI/PathwayMech/issues/673)) — Deferred to Cycle 2 Stage 1 (`add_records`)**:
   - Under `CLAUDE.md` and `conf/identifier_policy.yaml`, `conf/identifier_sources.json` and `data/identifier_authorities/sources.json` must only register authority entries whose labels and accessions have been verified against inspected upstream sources (`UniProtKB`, `Rhea 142 RDF`, `PubMed`, and `pathbank_primary_biopax.zip`) during bounded pathway curation rather than bulk-seeding uncurated records. Explicitly deferred to Cycle 2 Stage 1 (`add_records`) and kept open in [#673](https://github.com/CultureBotAI/PathwayMech/issues/673).

## 3. Detailed Implementation Specifications & Acceptance Criteria

### 3.1 `pathwaymech-infra-0002` ([#674](https://github.com/CultureBotAI/PathwayMech/issues/674))

- **Target files**: `src/pathwaymech/curation.py`, `tests/test_curation_publication.py`
- **Implementation**:
  - Add `_detect_yaml_width(raw_text, parsed_record)` in `src/pathwaymech/curation.py` to test candidate `yaml.safe_dump` widths (`100`, `88`, `80`, `120`, `4096`) against the existing file text and select the width that minimizes diff lines (returning an exact match immediately).
  - Add `_collect_anchored_subtrees(raw_text)` and `_restore_yaml_anchors(record, anchored_subtrees)` in `src/pathwaymech/curation.py` so that when an existing YAML file contains YAML anchors/aliases (`&id001`/`*id001`), repeated subtrees matching an anchored structure are re-linked to share the same Python object reference before `yaml.safe_dump` runs—even if the caller deep-copied or JSON-round-tripped the record.
- **Acceptance criteria**:
  - `test_publish_curation_preserves_existing_line_wrap_width` verifies that an `88`-column YAML file updated via `publish_curation` retains `88`-column wrapping on unchanged lines.
  - `test_publish_curation_preserves_yaml_anchor_aliases_across_deep_copies` verifies that a YAML file using `&id001`/`*id001` aliases retains `&id001` and `*id001` after `copy.deepcopy` + `publish_curation`.

### 3.2 `pathwaymech-infra-0003` ([#675](https://github.com/CultureBotAI/PathwayMech/issues/675))

- **Target files**: `src/pathwaymech/schema/pathwaymech.yaml`, `src/pathwaymech/schema.py`, `src/pathwaymech/kgx.py`, `tests/test_linkml_schema.py`
- **Implementation**:
  - Add optional `coefficient` (`range: integer`, `minimum_value: 1`) on `MechanisticEdge` in `src/pathwaymech/schema/pathwaymech.yaml` and enforce positive integer validation in `_validate_edges` in `src/pathwaymech/schema.py`.
  - Add `encodes` to `EdgePredicateEnum` in `src/pathwaymech/schema/pathwaymech.yaml`, `ALLOWED_EDGE_PREDICATES` in `src/pathwaymech/schema.py`, and `LOCAL_PREDICATE_CURIES` (`"encodes": "pathwaymech:encodes"`) in `src/pathwaymech/kgx.py`, with endpoint validation in `_validate_edge_endpoint_types` requiring participant endpoints (`gene`/`dna`/`rna` subject when typed; `protein`/`rna`/`complex` object when typed).
  - Add optional `assay_taxon` (`^NCBITaxon:[0-9]+(?![\s\S])`) and `eco_code` (`^ECO:[0-9]{7}(?![\s\S])`) on `EvidenceItem` in `src/pathwaymech/schema/pathwaymech.yaml` and `_validate_evidence` in `src/pathwaymech/schema.py`.
- **Acceptance criteria**:
  - All 270 existing records in `data/pathways/*.yaml` continue to pass both open (`pathwaymech-validate`) and closed (`validate_strict.py`) LinkML validation.
  - Positive and negative unit tests in `tests/test_linkml_schema.py` verify that both open and closed validators accept valid `coefficient`, `encodes`, `assay_taxon`, and `eco_code` values and reject invalid ones.

### 3.3 `pathwaymech-infra-0004` ([#676](https://github.com/CultureBotAI/PathwayMech/issues/676))

- **Target files**: `src/pathwaymech/sssom.py`, `output/sssom/source_mappings.sssom.tsv`, `tests/test_sssom_export.py`
- **Implementation**:
  - Add `Entrez` (`https://identifiers.org/ncbigene:`), `gomodel` (`http://model.geneontology.org/`), `NCBIProtein` (`https://identifiers.org/ncbiprotein:`), `Reactome` (`https://identifiers.org/reactome:`), and `SGD` (`https://identifiers.org/sgd:`) to `CURIE_MAP` in `src/pathwaymech/sssom.py`.
  - Regenerate the `# curie_map:` header in `output/sssom/source_mappings.sssom.tsv`.
- **Acceptance criteria**:
  - `tests/test_sssom_export.py` verifies that `write_sssom` accepts and expands `Entrez`, `gomodel`, `NCBIProtein`, `Reactome`, and `SGD` CURIEs in `source_mappings` and matches the committed `output/sssom/source_mappings.sssom.tsv`.

### 3.4 `pathwaymech-infra-0005` ([#677](https://github.com/CultureBotAI/PathwayMech/issues/677))

- **Target files**: `src/pathwaymech/kgx.py`, `src/pathwaymech/schema.py`, `tests/test_kgx_export.py`, `tests/test_linkml_schema.py`
- **Implementation**:
  - Add `"BiGG": "biolink:BiochemicalReaction"` to `_PREFIX_CATEGORIES` in `src/pathwaymech/kgx.py` so untyped `BiGG:*` reactions default to `biolink:BiochemicalReaction` while untyped `BiGG:*` participants fall back to `biolink:NamedThing`.
  - In `_validate_named_nodes` in `src/pathwaymech/schema.py`, reject `reactions` lists that mix entries with an explicit `category` and entries without `category`.
- **Acceptance criteria**:
  - `test_native_participant_fallback_retains_reaction_defaults[BiGG]` in `tests/test_kgx_export.py` and `test_reactions_mixing_explicit_and_omitted_categories_are_rejected` in `tests/test_linkml_schema.py` pass.

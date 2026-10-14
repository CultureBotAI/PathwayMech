# Quinate degradation II acceptance

The maintained `MetaCyc:PWY-6416` record has 60 evidence-backed relationships, 41 participants, four reaction nodes (three formal steps plus one NAD-specific realization), and five native taxon contexts. All 253 previous pathway records and all 4,913 previous authority terms remain unchanged. The authority union adds exactly 34 verified terms.

## Validation

- `just render-pages` and `just validate`: all 254 records passed, including identifiers, closed schema, evidence, history and generated-page checks.
- `just test`: 4960 passed, 3 skipped, 7 warnings.
- `just lint`, `just vendored-check`, `git diff --check`: passed.
- Structured review contract: 161 valid bundles; the five finding heads are resolved.
- Independent graph replay preserves all 60 SVG/KGX edges, 12 qualified endpoints and 51 local node contexts.

Complete final gate output and exact tested-input hashes are retained in `validation/`. The initial validation failure on four participant labels remains in the immutable initial reviews and their evidence. Final record SHA256: `83445c4f5cedd104d29cd065771b384f0ea277ed74291e3569315a9d42b01d97`.

## Review dispositions

The scientific and integration reviewers saved independent initial observations, then independently reassessed the corrected inputs. The initial bundles were not rewritten. Issues #545–547 track five findings: QutB NAD scope, QsuD specificity evidence placement, QsuB inspected-sequence wording and inhibition locator, and four canonical MetaCyc participant labels.

- Scientific successor resolving quinate degradation II review findings: `pass_with_limitations` ([YAML](../../../../reviews/structured/20261014T193002Z-quinate-ii-scientific-successor/review.yaml), [Markdown](../../../../reviews/structured/20261014T193002Z-quinate-ii-scientific-successor/review.md)).
- Integration resolution of quinate degradation II: `pass_with_limitations` ([YAML](../../../../reviews/structured/20261014T193035Z-quinate-ii-integration-resolution/review.yaml), [Markdown](../../../../reviews/structured/20261014T193035Z-quinate-ii-integration-resolution/review.md)).

## Evidence limits

The graph retains strain and experimental-construct distinctions, alternative in-vitro metals, inferred enzyme roles, and conflicting primary-source descriptions. Several primary sources were available only as abstracts or selected scans; the QsuR paper was inspected through a retained publisher transcript. No separately deposited full QsuB assay-clone sequence was inspected. Complete downloads remain external and hash-bound. These limitations are explicit in the record and final scientific review.

Ignored and hidden files were included in the duplicate searches. `identifiers.json` lists every named and referenced identifier and every new authority term. The source packages and README describe the strongest evidence and deliberate exclusions. Shikimate degradation II remains queued; source discovery is not exhausted.

Exact committed Git-blob verification, remote CI, native merge-queue tree equality, merge integrity and branch cleanup are subsequent lifecycle checks retained externally in `/private/tmp/pathwaymech-next-257-ci/`.

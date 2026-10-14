# Shikimate degradation II acceptance

The final record is `MetaCyc:PWY-6419`, shikimate degradation II, at `data/pathways/shikimate-degradation-ii.yaml`. It contains 32 evidence-backed edges, two formal reactions and the distinct downstream `GO:0019618` pathway interface. The complete named/reference identifier inventory is retained in `identifier-inventory.json`.

Three findings from the independent initial reviews were corrected in seven scalar fields: the downstream node category (#549) and six readable source-version values (#550). Mechanistic evidence, source hashes, identifiers, URLs and endpoint qualifiers are unchanged. The independent successor observations below retain each stable issue key and its exact predecessor.

- Scientific: `reviews/structured/20261014T212535Z-shikimate-ii-final-independent-scientific-review/review.yaml` and `reviews/structured/20261014T212535Z-shikimate-ii-final-independent-scientific-review/review.md`; `pass_with_limitations`, `completed`.
- Integration: `reviews/structured/20261014T212758Z-shikimate-ii-integration-successor/review.yaml` and `reviews/structured/20261014T212758Z-shikimate-ii-integration-successor/review.md`; `pass`, `completed`.

| Required command | Result | Seconds |
| --- | --- | --- |
| `just render-pages` | exit 0 | 68.14 |
| `just validate` | exit 0 | 226.66 |
| `just test` | exit 0 | 864.33 |
| `just lint` | exit 0 | 0.27 |
| `just vendored-check` | exit 0 | 3.13 |
| `git diff --check` | exit 0 | 1.32 |

The complete command output, environment, 1,248-file tested inventory and unchanged-input receipt are retained under `validation/final/`. The explicit baseline review-contract check uses `495de27ec09f99367d1cdd5c457a5e54a93c9a0b`; its actual output and save receipts are under `validation/review-contract-final/`.

All 254 baseline records, 4,947 authority terms, 865 owners and the 1,041-entry manifest prefix were independently preserved. The seven new authority identities and strict KEGG CDS adapter are documented in `authorities/` and `adapter/`; reviewed scientific and integration evidence remains distinct from software validation.

The initial failed vendored fetch, its successful scoped network retry, original author packages and initial review bundles remain intact. Final gates passed separately after correction. Abstract-only evidence, inaccessible full text, construct/strain boundaries and unsupported mechanistic extensions remain explicit in the record and scientific review. Public-release licensing is deferred as requested.

Missing-pathway searches included ignored and hidden files within the documented roots and exclusions. This record acceptance does not establish source exhaustion. Git commit, publication, queue/merge verification and cleanup have their own subsequent execution receipts.

# MG PathBank identity adapter implementation

This external candidate adds the native primary-owned Interaction attachment needed to identify the two PathBank pathways in the unchanged MG archive member. It is ready for independent code review; no full canonical build or scientific acceptance is claimed.

## Base and change boundary

The candidate copies committed ribose `b70ed36907b4c434d967f4456456be3b480415ae` (tree `428c9ff0ab1294c2e4b5d6059d45a40ddf096974`) and overlays the exact accepted six-file lyxose adapter. `baseline-code-bindings.json` binds all 222 files. The three changed files are the source snapshot builder, its PathBank tests, and `docs/IDENTIFIERS.md`; 219 copied files are byte-identical. The identifier consumer and typed archive provenance validator remain unchanged. `code-delta.json`, `implementation.patch`, and `code-copy-plan.json` define the exact incremental adoption boundary.

Both earlier packets remain sealed: all 280 lyxose implementation artifacts and all 229 MG authority-preparation artifacts were rehashed successfully during final verification. This packet does not alter their claims or prior gap ledgers.

## Behavior

The new branch resolves an Interaction owned by the requested primary Pathway through a direct component, an ordered PathwayStep, or both redundant paths. It requires the observed literal source marker, exactly one resolved local SmallMolecule and one different native Pathway participant, the compound's native reference, and an empty child with its exact marker, native accession/URI agreement, and direct title. It validates pointer shape, object types, local identities, namespace/base, literal cardinalities, and duplicate or dangling attachment paths. It does not scan arbitrary descendants or hardcode the MG accessions, member filename, or numeric fragments.

The existing direct/ordered SubPathway branch remains supported. Generic source markers are excluded from pathway synonyms. These structural names establish source identity only: no inhibition predicate, inhibitor mechanism, directed dependency, chemical equivalence, or child chemistry is inferred.

## Original-derived output

`two-term-build.json` is produced by the native source builder from the whole unchanged official ZIP, selecting `PW002096.owl`. It contains:

- `PathBank:SMP0002108`: `2-O-alpha-Mannosyl-D-glycerate Degradation`.
- `PathBank:SMP0000839`: `Gluconeogenesis from L-Malic Acid`.

Both labels come from the source, with empty synonyms. Typed metadata independently binds the 27,782,843-byte ZIP (`b3a9b9557d4147fac0159d178a27c13cc1180729eae9ccb4fb32abebb1656f44`) and 42,234-byte member (`473c3b61e69910e3ff52bbfff79daf3e9d1939f4ccf9c2cb8bb8ea96e08b2bb8`). Root-first `pathway_accessions` contains exactly the proven two accessions. The existing consumer accepts this bounded output. `new-originals-copy-plan.json` directs reuse of the exact complete ZIP; no source bytes were rewritten.

## Validation

The final focused suite passed **500 tests**, and Ruff passed. Actual commands, start/end times, exit codes, and output hashes are in `check-executions.json`. The first attempt's 500 passing tests and one E501 lint failure are retained under `retained-attempts/focused-attempt1`; the test line wrap was corrected before the final passing run.

`real-source-replay.json` records exact before/after parsing of all 11 previously supported PathBank originals, followed by bounded production builds preserving all 368 native terms and all 11 complete source metadata objects. Original-derived lyxose direct-only, ordered-only and redundant paths all retain the same output. The three corresponding MG modes pass. Fifty-three actual-original malformed member/archive/provenance controls are rejected, including owner paths, types, markers, pointer/cardinality errors, conflicting identity, expanded child, foreign namespace/base, unrelated pathways, changed original hashes/lengths/root and duplicate member names. Synthetic tests use different local identities and accessions. The malformed ZIPs are explicitly derivatives, never source authority.

## Prospective proposal composition and remaining root-owned work

The optional complete source proposal appends these two native terms and one typed source entry to the previously sealed MG helper proposal. It preserves exactly **2,432 source terms, 584 source metadata objects, and 737 manifest entries**, yielding **2,434 / 585 / 738**. These are **prospective proposal-composition counts, not merged canonical counts**. They include the helper's prospective lyxose composition.

Root has separately approved following the native ordered lyxose builder even when the existing frozen P76268 original is selected before a fresh UniProt source, producing 563 rather than the earlier proposed 564 source metadata objects. This implementation changes no source ordering. The full MG canonical build must start from the exact accepted lyxose canonical outputs, preserve all adopted terms/metadata/provenance, and add MG originals through the native builder. Do not overwrite that accepted output with these prospective totals.

Independent root review, adoption, a full original-backed canonical build, whole-corpus gates, final scientific record review, and any Git/GitHub work remain pending. No maintained files, shared cache, Git state, GitHub state, or environments were changed by this implementation task; no package installation or synchronization occurred. Public-release licensing remains deferred as instructed.

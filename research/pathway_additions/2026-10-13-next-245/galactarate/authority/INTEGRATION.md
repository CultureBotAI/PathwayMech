# Next245 canonical authority proposal

This folder is external staging only. Root approved the existing builders and the 914-entry proposed manifest, subject to final output/diff review. No maintained configuration, snapshot, record, or GitHub state was changed by this work.

Baseline: `3ead64024e50c06206aaa959cdf89d896f1cdbac` in `/private/tmp/pathwaymech-next-245-20261013`.

## Intended maintained artifacts after root review

| Complete canonical artifact | Maintained destination |
| --- | --- |
| `identifier_sources.json` | `conf/identifier_sources.json` |
| `sources.union.json` | `data/identifier_authorities/sources.json` |
| `ontology.union.json` | `data/identifier_authorities/ontology.json` |

Do not hand-merge terms or owner metadata. Copy only the complete successful canonical outputs after `canonical-build-receipt.json` and `canonical-union-comparison.json` establish the final GarP-inclusive build, and root reviews the diff.

The twelve new source owners are one pathway HTML identity/name object, two native reaction XML objects, three native compound HTML objects, two protein-complex XML objects, and four NCBI Gene XML objects. The four newly selected UniProt terms retain their first existing source owner, `uniprot-ecoli-reviewed-cofactors`; no new protein owner is introduced. The pinned ontology SQL supplies the new forward reaction RHEA16006.

## Source and scope decisions

`proposed-source-additions.json` is the exact append-only source manifest addition. `provenance-manifest.json` binds every entry to its actual whole original, request, retrieval timestamp, byte count, and digest. `gene-identity-projection.json` retains native garD/garL/garR/garP symbols, locus tags, taxon511145 and native update dates. Status omission remains omission.

The whole MetaCyc27.0 GALACTARDEG-PWY XML was rejected by the typed pathway adapter because its direct `super-pathways`, `in-pathway`, and `evidence` slots are outside the existing closed grammar. `pathway-adapter-gap.json` and `initial-typed-adapter-probes.json` preserve that rejection and the actual native slots. No original or parser was changed. Root approved the existing HTML adapter's exact native pathway identity/title as the authority owner. The unaltered whole XML independently supports biology, EV-EXP, super-pathway memberships, native direction, and complete pathway scope. **No typed-pathway validation is claimed.**

The reactions retain `source_context` frame-token names and molecular-activity type. The compound HTML titles are `(2R)-tartronate semialdehyde`, `NAD(P)+`, and `NAD(P)H`; complete XML chemistry/class evidence remains in the scientific dossier. Original layout primaries are not substituted for reaction equations.

GarP's retained first-owner label is `Probable galactarate/D-glucarate transporter GarP`. Existing authority ownership and labels are preserved even when newer scientific evidence provides additional function information.

## Reproduction

`canonical-build-commands.json` supplies the exact unchanged canonical builder argument arrays, environment, input hashes, and baseline. Run from the named worktree with the existing Python environment. Source originals are staged through explicit aliases to retained unmodified files, including recursive companion paths; `staging-original-bindings.json` and the manifest bind these aliases. The old complete cache is `/private/tmp/pathwaymech-next-244-authority-staging/originals`.

For a fresh reproduction, stage the complete baseline corpus and a copy of the real accepted-scope author draft, append the twelve source entries to the unchanged baseline manifest, and supply every original at its exact relative manifest path. Add an external selector reconstructed from the sorted union of `retained-authority-identifiers.json` and `planned-identifiers.json`, using the documented `yaml.safe_dump` serialization. It contains IDs only and is **not a scientific record**. Its purpose is to retain all earlier authority IDs, including those not used by the current corpus. No label comes from this selector.

The copied first draft has SHA-256 `09ff77ad5137f6ca7630a4c82380863d5d72e27abad5ffdcadf04948140fc177`; the final selection also explicitly includes UniProtKB:P0AA80 and Entrez:947642. Root states that subsequent evidence/locator fixes introduce no further IDs. Before integration, confirm every final candidate identifier belongs to the completed union outputs. That check is about identity coverage, not approval of the scientific graph.

The preliminary successful build without GarP is retained in `preliminary-without-garp/`; it preserved every earlier term and owner. Final receipts must refer to the subsequent GarP-inclusive build. Temporary environment-bound helpers remain external; no helper script belongs in the maintained dossier. Full original bodies likewise remain outside the repository.

## Final observed result

Both final canonical builders exited 0. `canonical-build-receipt.json` binds their logs, complete outputs and comparison. All 2,710 old source terms and 721 source owner objects, all 2,020 old ontology terms and five ontology owners, and all 902 ordered baseline manifest entries are exactly unchanged. Final outputs contain 2,726 source terms / 733 owners, 2,021 ontology terms / five owners, and 914 manifest entries. The final candidate has 38 selected identifiers, all resolved; its only additions to the copied first draft are GarP protein and gene.

`first-draft-origin-supplement.json` binds the historical `candidate.yaml` input to the now-immutable `first-draft-09ff77.yaml` without rewriting execution history. `final-candidate-identity-coverage.json` records the current revised candidate hash and exact identity-set comparison. The canonical ontology log retains existing corpus label-difference diagnostics; these are not silent label edits. No prior term or source object was altered. Root must still review the complete artifact diff before copying maintained files.

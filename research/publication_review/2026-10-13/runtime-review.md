# Fresh runtime adversarial review

Reviewed checkout: `/private/tmp/pathwaymech-next-243-local-20261012`.
Base: `e1c66917e753105c4bf5b7b026193fcefa2b000f`.
Head: `70903536191206d2586cd23e46f7d70c32fef92e`.

## Finding: P2 — register every typed native identity before dispatching selected terms

Location: `src/pathwaymech/identifiers.py:351–361` (selected-owner guard), with incomplete all-owner registration at lines 283–319.

The loader individually validates the new typed source objects but protects selected ownership only for PathBank context, protein-carrier reactions, pathways and the separate aceto validation. The expected projection checks at lines 392–428 depend on the term's chosen source kind. Consequently, retaining an entirely valid typed owner while changing its selected term to an additional ordinary legacy source bypasses its type and canonical-name constraints. Removing `entity_type` and using an arbitrary label makes `identifier_errors` accept a protein class, protein state, electron-transfer reaction, native chemical class, named complex or Rhea polymer as a `small_molecule` participant. The same records correctly raise `ENTITY_TYPE_MISMATCH` with their original typed terms.

The missing global registration also allows internally contradictory retained owners: two independently well-formed carrier classes/states with different native canonical names, two electron-transfer reactions with coefficients 4 versus 9, or two native chemical classes with different names load successfully. The snapshot producer rejects each identical pair before selection. This is the same producer/consumer integrity boundary enforced for named complexes by the new issue-500 tests, but the other new modes are omitted.

Trigger: a hand-edited, combined or merged authority JSON retains a typed native source while rebinding its term to a legacy owner, or includes contradictory duplicate typed owners. The checked-in corpus is not asserted to contain these corruptions; this is a blocking-validator coverage defect, not evidence of current scientific-record corruption.

Requested correction: register complete typed identity assertions, including state counterparts and polymer members, before reading selected terms; check same-identity conflicts and require each selected term to retain its compatible typed owner. Preserve existing compatible companion exceptions and first-owner behavior. Add producer/consumer parity regressions for both source orders, selected/unselected conflicts, legacy rebinding, and identical duplicates.

Reproduction: `/private/tmp/pathwaymech-publish243-runtime-repro-20261013.py` and captured output `/private/tmp/pathwaymech-publish243-runtime-repro-20261013.stdout`. Run from the reviewed checkout with `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src:tests:.` and the repository Python environment. It uses existing fixture builders; all generated inputs are confined to fresh temporary directories. The six downgrade cases return `errors=[]`; the four conflicting-owner cases are rejected by the producer and accepted by the consumer.

## Scope and limits

Read shared runtime dispatch, the new BioCyc carrier/state/native-context/pathway/electron-transfer/named-complex/protein-carrier modules, PathBank context and Rhea polymer readers, aceto assertion/companion integration, and relevant adversarial tests and identifier contracts. Inspected producer dispatch/conflict code to compare guarantees. No broad suite repeated; the parent supplied final-head native results of 4,773 passed, 3 skipped, 3 warnings. No worktree edits or remote actions. No binary evidence audit or independent scientific reassessment. Local instruction-file discovery included hidden and ignored files (excluding `.git`, virtual environments and node modules); no repository-local AGENTS.md was returned. No further actionable runtime defect was established in this pass.

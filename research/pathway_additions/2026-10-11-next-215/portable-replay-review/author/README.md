# Portable staphyloferrin B replay preparation

This external candidate preserves the complete frozen seven-transformation author replay. It is a preparation for later maintained integration and independent review. It does not approve the scientific record, a maintained authority snapshot, or the whole corpus.

The scientific target remains SHA256 `891ce5a5ba08bfae8fdedbd7709f14097f4bd04749c7755fce6d6a51841c840a`. The independently reported sequence locators on `sbn-edge-056` and `sbn-edge-058` are still unresolved in those frozen bytes. The helper receipt explicitly retains that limitation. A corrected target, matching projections and locator regression would be a separately reviewed successor; this handoff does not silently substitute it.

## Interface

`staphyloferrin-b-replay.py` requires `--repo-root`, `--record`, `--source-manifest`, `--source-projection`, `--authority-root`, `--output`, `--pdf-python`, and `--stereo-python`.

The PDF and RDKit dependencies require two explicit interpreter arguments. Their paths are made absolute but deliberately are not resolved through virtualenv symlinks. The chosen environments must import `pypdfium2` and `rdkit`, respectively. No dependency installation or network acquisition occurs. The exact successful command and runtime paths are in `positive-final-execution.json`.

The command imports the selected repository's unchanged canonical schema, strict validation, identifier validation and KGX implementation. It checks full policy equality with the explicitly supplied authority root. Only policy-referenced snapshots are copied into a new one-record companion sandbox. That scope is distinct from current or future whole-corpus integration.

The new external receipt and its `.artifacts` companion must not exist, including as dangling symlinks. Paths inside the repository, authority root, original-source directories or record/manifest/projection directories are rejected. `python -O`, stale projection/manifest digests, duplicate original paths, ambiguous basenames and undeclared role/reference sources are rejected. All scientific/source assertions remain active. Inputs and 62 original bodies are checked again immediately before exclusive final receipt creation. `open('x')` provides final no-overwrite semantics even after the startup check. Independent real-race review remains pending; no race result is claimed here.

## Observed validation

- Final relocated positive CLI execution exited 0: 62 original bodies, all seven native transformations, 40 Rhea sides, seven balances, 44 KGX nodes, 72 edges, 129 evidence blocks and 53 references.
- Fresh explicit-interpreter PDF checks passed all seven original locator guard groups. Fresh RDKit checks retain the original cyclic PubChem structure, linear ChEBI distinction and prior SI drawing transcription scope; they do not establish a physiological molecular-state distribution.
- Seventeen real negative CLI invocations failed as required and retained protected sentinel bytes. `negative-controls-final.json` lists the exact commands and actual failure locations. The stale original digest case is rejected early by reference/manifest digest consistency.
- Ruff passed on the final helper. AST comparison confirms 71 original assertions are unchanged; the other two original digest checks are strengthened by manifest binding and fresh rehashes. The complete original seven-group PDF guard loop is unchanged.
- All 25 artifacts in the frozen author completion manifest, the completion file itself, and both original helper copies were rehashed unchanged.

`helper.diff` is the exact original-to-candidate implementation diff. `guard-preservation.json` records the comparison and immutable author inputs. `positive-final.json` binds the final helper, canonical code and snapshot hashes, original bytes, runtime probes, schema/identifier results and actual KGX evidence parity.

The first preparation formatter failed before writing the candidate because it attempted to wrap f-string child constants. Excluding those AST nodes fixed formatting without changing the scientific AST. An intermediate retry used the just-removed `213/.venv` link and exited 127 before any check; final commands use the retained 195 environment explicitly. These preparation failures and earlier successful trial outputs are preserved separately. No frozen author file, raw source, maintained owner, shared cache, Git state or GitHub state was changed.

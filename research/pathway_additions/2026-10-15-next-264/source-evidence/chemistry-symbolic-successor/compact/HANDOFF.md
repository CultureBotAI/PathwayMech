# Next264 chemistry symbolic-coefficient successor

Issue: [572](https://github.com/CultureBotAI/PathwayMech/issues/572), `next264-rhea-symbolic-participant-truncation`.

The correction-author replay passed: 37,222 directional equations were examined, 37,068 complete fixed-coefficient equations were compared, and 154 entire symbolic equations were excluded. All 148 previously truncated comparisons are explicitly accounted for. Both selected reactions and all 11 material entries remain correct. Read [CORRECTIONS.md](CORRECTIONS.md) for the bounded supersession and preserved limitations.

Preferred evidence:

- `replay-summary.json` and `execution-receipt.v2.json`: actual successful command, counts, Python version and output hashes.
- `helpers/replay_symbolic_comparison.v2.py.txt`: corrected executable source retained with an inert filename. It uses only Python's standard library and reads external frozen inputs. The filename without `.v2` is the preserved failed successor attempt.
- `corrected-rhea-equivalence-exclusions.json`: all 154 excluded equations with every material term, predicate, participant identity and legacy diagnostic disposition.
- `excluded-complete-source-closure.json`: 809 exact source URIs and 1,225 complete parsed RDF Description elements.
- `fixed-equation-signatures.json`: all 37,068 accepted complete side signatures; no excluded fragment appears in this population.
- `corrected-selected-route-replay.json`: both oriented equations, all 11 material entries, formulas/charges, exact family matches, native ordering, primary material join and net calculation.
- `selected-complete-source-closure.json`: 31 selected family/side/participant/compound URIs and 43 complete parsed RDF Description elements.
- `frozen-package-preservation.json`: all 136 original frozen artifacts and the complete hidden/ignored-inclusive inventory verified before and after the replay.
- `correction.json`, `input-retention-map.json` and `replay-input-bindings.json`: original evidence, superseded claims, artifact hashes and retained copies.
- `helper-attempt-disposition.json`, `execution-receipt.json` and the first trace: the failed new-parser attempt remains disclosed separately from the successful v2 result.

The original RDF hash is `8ee48d7044cf3eef1001fa730dae2a491902ab25b259b519d6826796bb8acedf`. The original frozen helper hash is `2359e7be56ed23008db677bfe0716046e670112974262263ba46cf1b1c1ae4d8`. The independent counterexample inventory hash is `8ef1ed6c0ce2960708ce96a4164e4f292da5e47356c8d2b59316173227f626b6`. The successful v2 helper hash is `6e594df753a38246fab661bf872c9649224290be572454c0cf32034ce213b752`.

The helper writes outputs with exclusive creation and must not be rerun in this frozen package. For independent reproduction, copy it to a new owned scratch location and change only its `OUT` constant to a fresh output directory; retain that bounded transformation and actual execution receipt. Keep all frozen inputs unchanged. No 263 worktree or shared Python environment is needed.

`compact/` contains lossless copies for retention, with original/stored hashes in `compact-retention-manifest.json`. The complete original RDF remains in the original external source package rather than being duplicated here. Its bytes, source path and frozen artifact manifest remain bound. No maintained record, authority, Git/GitHub mutation or canonical review was made. This correction is authored evidence, awaiting separate independent assessment; it does not close issue 572.

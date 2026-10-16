# Ethanolamine utilization: bounded iModulonDB context

This source-preparation packet adds computational expression-module context for prospective `MetaCyc:PWY0-1477`. It does not establish pathway identity, reaction membership, catalysis, transport, reaction direction, or native strain flux. No maintained record, shared adapter, runtime, or Git/GitHub state was changed.

The existing installed `kg-microbe-sources` runner was used directly. Fresh dataset discovery returned 28 dataset keys across 20 organism entries, including five E. coli keys (`modulome`, `precise1k`, `precise278`, `precise815`, `precise_mg1655`) and `s_enterica/core`. Both `ethanolamine` and `eut` were searched in each of those six keys. These are finite returned search results, not a complete gene or component inventory. Every successful search returned ten gene rows; no inference about additional omitted or unmatched genes follows.

Eleven of twelve searches succeeded through the installed adapter. The E. coli `modulome`/`ethanolamine` search exited 2 because the actual component row has `regulator: null` and the shared parser expects a list. The original failed stdout/stderr and receipt are retained. Direct inspection of the unmodified public API response succeeds and identifies `e_coli/modulome/76`, named Fermentation, with a function annotation covering hydrogenase, ethanolamine and lactate catabolism. Null regulator is not a claim of no regulation. The adapter was not repaired or bypassed by rewriting its input. Its ordinary summarize command for component 76 succeeds.

The exact component-gene API response contains 13 rows, all marked `in_imodulon: true`, with threshold 0.105120952. This is the complete returned table, not a claim that only 13 genes were scored in the underlying transcriptomic study. The corresponding adapter summary rounds display values. The most relevant rows are:

| Dataset-local gene | Name | Signed component weight | Issuer annotation in this response |
|---|---|---:|---|
| `e_coli/modulome/b2454` | eutJ | 0.205927273 | UniProt P77277; STRING 511145.b2454 |
| `e_coli/modulome/b2453` | eutG | 0.200325 | UniProt P76553; STRING 511145.b2453 |
| `e_coli/modulome/b2452` | eutH | 0.156945 | UniProt P76552; STRING 511145.b2452 |
| `e_coli/modulome/b2451` | eutA | 0.155497 | UniProt P76551; STRING 511145.b2451 |
| `e_coli/modulome/b2296` | ackA | -0.17111 | UniProt P0A6A3; STRING 511145.b2296 |

Only the first weight above is shown at the original response precision; the other displayed weights follow the adapter's rounded summary. Exact numbers for all 13 rows remain in `raw-e_coli-modulome-76-genes.body.json` and the generated assessment JSON. Positive and negative component weights are not biochemical reaction directions. The component also contains unrelated hydrogenase, fumarate, lactate and other functions, so it is not an exact ethanolamine pathway definition.

The returned E. coli gene keys are compatible with an MG1655 reference annotation and one dataset key explicitly names MG1655; the inspected inventory does not establish the culture, genetic background, or activity conditions of every contributing sample. The Salmonella search has STM locus keys but supplies no experiment-level LT2 strain confirmation. Therefore none of this evidence resolves the native MG1655 CPZ-55 interruption, substitutes K12 protein scope for an MG1655 experiment, or transfers a Salmonella mechanism to E. coli. Search product strings are historical annotations: for example, `s_enterica/core/STM2461` calls EutG a putative transport protein. They must not replace the separately inspected enzyme and primary evidence.

All successful rendered search tables, the complete component summary, and all three exact HTTP response bodies were read at their stated scope. The eleven other searches returned no component rows for those terms; that is not evidence that Eut genes belong to no other modules. No exhaustive transcriptome, organism, pathway, archive, or source search is claimed. The evidence can support a qualified review note about the returned fermentation module and selected genes; it does not justify adding a mechanistic edge.

Raw HTTP bodies and their response metadata are distinguished from adapter-rendered stdout. Runner source files are copied and hash-bound for reproducibility, with no installation or dependency change. Every owned acquisition is terminal. Later curation still requires the actual verified PR #633 merged baseline and independent review of the full biological source preparation.

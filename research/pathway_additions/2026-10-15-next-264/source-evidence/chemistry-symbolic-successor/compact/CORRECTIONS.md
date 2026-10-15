# Issue 572: complete fixed-coefficient comparison

This append-only package corrects the source-method claim in the frozen next264 chemistry preparation for MetaCyc:PWY-2503. The original package remains unchanged. This is correction-author work; independent acceptance belongs to a separate reviewer. It is not a maintained pathway or a canonical record review.

The original helper retained numeric `contains[0-9]+` predicates while discarding symbolic coefficients. For 148 directional equations this silently removed material before comparison. Six additional symbolic equations were already excluded because the filtered side data disappeared. The original claim of 37,216 complete fixed-coefficient comparisons is therefore incorrect.

| Population | Frozen claim | Corrected result |
| --- | ---: | ---: |
| Directional equations in the complete source | 37,222 | 37,222 |
| Complete fixed-coefficient equations compared | 37,216 | 37,068 |
| Entire equations excluded | 6 | 154 |
| Previously compared truncated equations | Unaccounted | 148 |

The corrected helper retains every direct RDF predicate. It distinguishes the base `rh:contains` membership relation from its coefficient-bearing predicates, verifies that each member has exactly one coefficient predicate, and rejects the entire equation if either side contains a symbolic/nonpositive coefficient, missing material or an unresolved/nonunique participant identity. No fragment from an excluded equation enters the accepted comparison.

All 154 exclusions are symbolic in this pinned source. Their 392 directional symbolic-term occurrences use `containsN` (352), `contains2n` (22), `containsNplus1` (10), or `containsNminus1` (8). The complete side inventories retain numeric and symbolic terms, exact predicates, participant URIs and compound identities. All 809 excluded reaction/side/participant/compound URIs and all 1,225 corresponding complete RDF Description elements are retained. XML elements are parsed and serialized by ElementTree; these are complete structural extracts, not claims of lexical byte identity with an RDF substring. The complete original RDF remains unchanged and hash-bound.

The complete exclusion IDs and every material term agree with the independent counterexample inventory. That comparison is an author-side cross-check, not independent acceptance of this correction. The old numeric-only selection is reproduced solely as a diagnostic to account for all 148 previously partial comparisons and the six earlier exclusions.

The corrected comparison still finds only RHEA:12634/12635 for the first selected equation and RHEA:11561/11562 for the second. RHEA:12634 and RHEA:11561 remain the selected left-to-right members. All 11 native/Rhea material entries, coefficients, exact compound identities, formulas and charges were replayed. Each reaction balances to C28 H33 N7 O18 P2 with charge −2 on each side. The native order and CPD-290 join remain exact. NAD and NADH cancel in the calculated net sum: benzoate + H+ + O2 → catechol + CO2, with C7 H6 O4 and charge zero per side.

Only the affected whole-Rhea method and completeness claims are superseded: the comparison paragraph and six-exclusion wording in `HANDOFF.md`; `whole-route-chemistry-replay.json` comparison statistics/limit; `rhea-equivalence-search-exclusions.json` completeness claim; and those claims repeated by the old helpers and actual execution logs. The historical logs still accurately document what those old programs printed. They are preserved, not rewritten as successful corrected runs. The selected route, eight chemical identities, family orientation, context-cofactor assessment and all preparation/access caveats are not superseded by this correction.

The first new correction-author attempt also failed: it initially treated the base membership predicate as another coefficient. That helper, actual exit-1 receipt and trace remain in this package. The successful v2 helper explicitly checks membership coverage before coefficient interpretation. Its actual command exited 0, with no stderr. This implementation correction changed neither the frozen original nor a maintained record.

Fixed-coefficient comparison means equality of complete ordered multisets of declared compound IDs and positive integer coefficients. It does not infer generic/polymer algebra, identify new pathways, establish global source exhaustion, or upgrade strain, enzyme or assay claims. Independent acceptance and the merged-baseline discovery rebind remain separate prerequisites for curation.

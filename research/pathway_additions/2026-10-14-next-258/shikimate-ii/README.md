# Shikimate degradation II

This dossier supports `data/pathways/shikimate-degradation-ii.yaml`, the
MetaCyc:PWY-6419 two-reaction NAD-dependent route from shikimate through
3-dehydroshikimate to protocatechuate. Its exact reactions are RHEA:17742 and
RHEA:24849. GO:0019618 identifies the already maintained downstream
protocatechuate ortho-cleavage process; that interface adds no third formal
reaction to shikimate degradation II.

The baseline is commit `495de27ec09f99367d1cdd5c457a5e54a93c9a0b`, with 254
pathway records. Searches included ignored and hidden files in both main and
the isolated task worktree. `preflight/` and `supplemental-search/` retain the
patterns, searched boundaries, matched-file dispositions and exact baseline
comparisons. Default text-search binary handling and external-cache limits are
explicit. No claim of source exhaustion follows from this candidate audit.

`native/` accounts for 53 native objects, 853 direct slots, six linked enzyme
activities and 22 protein/gene/component references. Complete source objects
remain external and hash-bound. The source narrative's fungal qutB/G-11736
pointer is inconsistent with the bacterial second step: R-strain qsuB is
G-11737/cgR_0493. QsuD's native Cgl0424/G-11733 identity belongs to ATCC 13032,
whereas the R-strain regulatory target is cgR_0495. Those distinctions are
retained rather than combining results across strains.

`primary/` separates the R-strain genetic and expression experiments from
ATCC 13032 QsuD and ATCC 13869 QsuB biochemical assays. It includes the
directly studied ShiA shikimate transporter and ShiR control of shiA
expression, distinct from the earlier QsuA homology inference. Chorismate is
the supported QsuR effector. QsuB metal support and product/substrate
inhibition are conditional in vitro observations. Native NADP turnover and
2013 NADP nondetection retain their respective assay scope. Tags, cleavage
uncertainty and sequence-join limits are attached to the affected endpoints.
Abstract-only and unavailable primary content are identified in the reading
ledger; they are not treated as inspected full text.

`assembly/` binds the complete chemical comparison, author integration and
initial draft. Exact native compounds agree with pinned ChEBI identities,
and both complete reaction equations agree with detailed Rhea 142 evidence,
including direction, coefficients and atom/charge balance. Canonical Rhea
labels still come from pinned Rhea 139. The broader NAD(P) reaction RXN-11174
is not substituted for the NAD-specific formal member. Later review fixes,
if any, belong to separate immutable review observations and correction
receipts; they do not rewrite the initial author draft.

`adapter/` documents the strict `kegg-gene-flatfile` authority profile. It
retains a complete issuing CDS response, verifies the request and original
hash, reparses all fields in the consumer and requires gene placement with
the native locus label. Scientific sequence translation and the T00501/cgt
genome join are independently checked in `native/`. The old NCBI Gene
records are discontinued; the exact current KEGG loci provide the regulatory
gene endpoints. The adapter does not turn functional NAME annotations into
gene symbols or establish biological function by parsing an identifier.

`authorities/` preserves all 4,947 baseline terms and 865 source-owner objects,
then adds the seven explicitly selected identities. The source manifest
keeps its complete 1,041-entry prefix and appends six originals. Both builders
use complete issuing sources; the record supplies only an ID selection.
No canonical-label policy, schema or governed-file exception is required.
`identifier-inventory.json` enumerates named and reference identifiers.

Author evidence, deterministic validation and independent review are separate
artifacts. Compact retained files have exact original-to-repository mappings;
raw sources, full baseline snapshots and generated authority trial copies
remain external. Failures and corrected author-helper assumptions are retained
with their actual scope. Repository gates and saved review bundles provide the
later acceptance evidence; this dossier alone is not scientific approval.

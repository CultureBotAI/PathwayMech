# Independent MMPA source assessment

Target `data/pathways/methylthiopropanoate-degradation-i.yaml`; SHA256 `7810e21c690b17fe781fd249ea6fc0ec86220913a55947df75ec29c15cffe5dd`.

Inspection began 2026-10-11T09:04:15.408502+00:00; this source assessment finished 2026-10-11T09:09:44.730353+00:00. This is an audit supporting a forthcoming canonical review, pending shared gates.

This reviewer authored only the separate sulfoED record in this cohort; root authored MMPA. No MMPA record or author dossier was edited. Governed inspect preceded assessment; the reviewer wrote a separate replay instead of importing the author replay.

No corrective findings were identified in the 29-edge, 64-evidence target.

## Exact identity and complete boundary

Three native members are fully represented. DMSP demethylation precedes this named route; acetaldehyde oxidation and methanethiol assimilation follow it. These adjacent pathways are not silently folded into the exact boundary.

Inspected evidence: Original PWY-6048 XML reaction-list/orderings and canonical HTML; full 2011 primary printed pp.208-209.

## Native/current chemistry and direction

All17 graph sides and15 component sides independently reconstructed; seven equations balance. Four terminal component equations sum exactly to the retained two-water net. Master-to-directed triples verified. All three native compound InChIs equal current selected structures, including the trans MTA double bond.

Inspected evidence: Original Rhea142 RDF, full native reaction XML, current ChEBI255 SQL.

## Generic electron acceptor

Whole generic ETF redox states are source-issued database convention. Direct DSS-3 experiments used artificial acceptors, and free FAD/FMN/NADP alone did not support the later assay. The record explicitly does not establish physiological ETF identity. No carrier-specific strain protein or reoxidation route invented.

Inspected evidence: Original native ETF objects, UniProt Q5LLW7, Rhea52613; 2011 pp.208-209; 2022 PMC8824276 s2-3/s3-1.

## DmdD composite net and assembly

Net cleavage is experimentally observed; enzymatic hydration and thioester hydrolysis are distinct from spontaneous methanethiol release and expected spontaneous malonate-semialdehyde decarboxylation. Carbon dioxide was presumed in the original product balance, not directly measured there. The homohexamer has two trimers and intersubunit sites; enables does not assert isolated monomer activity.

Inspected evidence: 2011 pp.208-209; 2013 PMC3660561 sections s2b,s2f,s2g and Figure6.

## Exact taxon, proteins and inferred cofactors

SPO2045/DmdB2, SPO3804/DmdC1 and SPO3805/DmdD resolve to Q5LRT0/Q5LLW7/Q5LLW6 and strain taxon246200. DmdB2/DmdC1 dimer support retained. Mg requirement is directly reported; its UniProt annotation remains ECO0250. DmdC FAD occupancy is similarity-based, not a direct DSS-3 occupancy measurement. Other paralogs and cross-species 2019 findings are not transferred.

Inspected evidence: Original native ENZRXN/MONOMER chains and three reviewed UniProt JSONs; 2014 PMC3957724 sec3-1/sec3-2; 2022 PMC8824276 s2-3/s3-1.

## Conditional activity regulation

DMSP inhibits purified DmdB2. MMPA above2mM relieves that inhibition, with about80% recovery at8mM; activates is expressly conditional. ADP relief is DmdB1-specific and is not assigned to DmdB2.

Inspected evidence: 2014 original PMC3957724 sections sec3-5/sec3-6, Figures3/5B; Q5LRT0 comments3.

## Evidence locality and references

Every29edge was assessed. Structured assertions remain their original source statements; primary experiments are scoped to exact strains and conditions. All inspected UniProt pointers and primary section/figure/page locators resolve. Source hashes independently match original bytes.

Inspected evidence: Complete target read, original20 reference bodies, primary article metadata, original source objects/fields and all64 edge evidence blocks.

## Structured expression context

Inventory contains20organisms/28datasets and no Ruegeria dataset. Console runner unavailability is preserved; unchanged canonical parser fallback was used by root. No surrogate strain or negative biological claim inferred.

Inspected evidence: Current original iModulonDB /api/datasets response SHA155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693; root console/fallback/replay receipts.

## Schema and actual export

All endpoints and references remain local. Actual exported rows retain each evidence block and description byte-exactly. This narrow actual export is not a substitute for root full-corpus gates.

Inspected evidence: Independent validate_record and render_kgx execution, 25nodes/29edges/64evidence.

## Actual checks

Independent replay session80023 exited0:31original body hashes,20reference hashes,17graph sides plus15component sides,7balances,exact component-to-net sum,3InChI bridges,3protein identity chains,25node labels and actualKGX25nodes/29edges/64evidence. Initial reviewer-helper XML-selection failure was corrected before the successful rerun; no target edit resulted.

The 2011 original PDF was independently extracted in full and printed p.209 was rendered and visually inspected. Current shared gate results are not preclaimed.

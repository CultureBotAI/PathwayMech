# Pathway mechanism research: fructoselysine and psicoselysine degradation

## Pathway scope

Candidate `MetaCyc:PWY0-521` is the complete three-reaction pathway in META
PGDB 27.0. It converts psicoselysine through fructoselysine and fructoselysine
6-phosphate to glucose 6-phosphate and lysine. Fructoselysine can enter at the
kinase step. The distinguishing entry reaction is FrlC-catalyzed epimerization;
the FrlD/FrlB core overlaps the maintained `GO:1901281` record. These are
overlapping source-defined boundaries, not two disjoint metabolic capabilities
or exact GO/MetaCyc synonyms. Preserve the existing GO record unchanged.

The native reaction list contains RXN0-4841, RXN0-962 and RXN0-963, in that
order. It does not include a transport or transcriptional-regulation reaction.
Native species annotations identify E. coli K-12 MG1655; reviewed UniProt
entries have the broader K-12 taxon. Experimental organisms and constructs
must retain their own scope. The native Bacteria taxonomic range does not
establish experimental pathway demonstration throughout Bacteria.

## Mechanistic summary

The native epimerase reaction is reversible and printed fructoselysine on the
left, psicoselysine on the right. The pathway traverses it right-to-left. The
kinase consumes ATP and generates ADP and a proton; the deglycase consumes
water. Layout primaries do not replace these complete reaction sides.
The deglycase's catabolic traversal does not deny its reported in vitro
reversibility. The exact chemical audit accepts `RHEA:28391` for catabolic
epimerization and `RHEA:28379` for phosphorylation. Their L2R notation follows
Rhea's own printed orientation, not the opposite native epimerase orientation.

The final event retains `MetaCyc:RXN0-963`: its native GLC-6-P product is
`CHEBI:58247`, beta-D-glucose 6-phosphate(2-). `RHEA:28383` uses the broader,
anomer-unspecified `CHEBI:61548`. Whole InChI comparison exposes this difference;
equal formula and charge do not establish stereochemical equivalence. The
existing GO record retains its own broader Rhea product scope. All nine selected
chemical identities match native and ChEBI structures, and all three selected
equations balance atoms and charge. The beta assignment remains native database
evidence; the 2002 coupled glucose-6-phosphate assay does not independently prove
anomer identity.

## Primary evidence already appraised

The complete 2004 primary, PMID:14641112 / DOI:10.1042/BJ20031527, was acquired
from the current UCLouvain repository. Its six pages and five figures were
inspected by the independent source investigator; the reading ledger retains
that attribution. Figure 4 supports reversible conversion, and Figure 5
places epimerization before the shared phosphorylation/deglycation core.
The complete original PDF is retained externally with SHA-256
`3ff6bd0c195156ff78fd509723301a3d425d317a6ef9e0f65489faeec579556c`.

Methods on page 1048 specify BL21(DE3) genomic DNA, pET-3a cloning and
BL21(DE3)pLysS expression. Results describes the corrected region as K12.
Figure 1 presents 275 residues, matching the first 275 residues of current
UniProt P45541; the current 276-residue sequence has an additional terminal
arginine. The manually transcribed alignment is an inspection aid, not a
deposited construct sequence. Assays must not become unqualified claims about
the full-length contemporary MG1655 protein.

The approximately 260-kDa gel-filtration estimate suggests an octamer; its
underlying results are not shown. This is an assembly inference, not a solved
structure. Nickel and cobalt support in vitro activity better than iron and
manganese. The experiments include magnesium in the assay background and do
not determine physiological metal occupancy or stoichiometry. Zinc inhibition
is an assay observation; absent calcium/copper enhancement is not proof of
inhibition.

Growth on psicoselysine and Tn5 disruptions support involvement of the frl
operon. The paper identifies FB21138 (frlA), FB21140 (frlB) and FB21829
(alsE) from the Blattner collection. It does not state their genetic background
in the inspected Materials passage; BL21 culture experiments do not identify
those mutants' background. No complementation or FrlC knockout is reported.
Figure 5 labels FrlA transport presumptively; no measured transport equation,
ion coupling or transport stoichiometry is inferred.

## Evidence table

| Source | Supported scope | Limit |
| --- | --- | --- |
| Complete META PWY0-521 and three reaction XML objects | Three-member native boundary, order, layout and full chemical sides | Exact cross-database equivalence requires independent chemistry checks |
| PMID:14641112, Figures 1–5 and Methods/Results | FrlC preparation, bidirectional activity, metals and pathway interpretation | Construct/strain discrepancy, inferred assembly and conditional genetics retained |
| PMID:12147680, complete text and figure captions | FrlD/FrlB preparations, catalytic assays, product analysis and zinc inhibition | No locally retained original PDF or visual figure appraisal; product assay does not prove beta anomer |
| PMID:32979851, complete article and Figures 1–9 in the LMU thesis | FrlR repression/operator binding, RpoH reporter response and indirect CRP/cAMP context | Shared-promoter reporters and engineered preparations; supporting information unavailable |
| Existing GO:1901281 record and prior curation dossier | Narrower shared FrlD/FrlB core | Existing record has an abstract-only 2002 primary limitation |

## Gaps and acceptance work

The Rhea/ChEBI join and fresh duplicate audit are complete. The complete 2002
text and figure captions were appraised through the public author PDF in the
web reader; local PDF acquisition and visual figure inspection were unavailable.
No original PDF digest is asserted for that reference. The FrlD preparation
matches the current start-primer neighborhood, but complete experimental
sequence identity is unproved. FrlB's active first-AUG and inactive second-AUG
preparations remain distinct; the former starts at the current P0AC00 start
neighborhood. An older sequence's extended-N-terminal warning is not evidence
that this active construct extends current P0AC00. Assembly assignments remain
gel-filtration interpretations. Mg assay background and coupled NAD(P)/PEP
reporters are not promoted to indispensable enzyme cofactors or pathway chemistry.

The 2020 regulatory article (final issue 2021) was read in full, with all nine
figures, from the author's LMU thesis. Its digest binds the entire 125-page
thesis; one-based PDF pages 85–100 contain the 16-page article. Supporting
figures and exact construction/primer tables were unavailable. FrlR reporter
repression and separately tested operator binding, RpoH overexpression response,
and indirect CRP/cAMP regulatory interpretation are retained as pathway-level
expression context. The graph distinguishes the reporter FrlR preparation from
the tag-cleaved His6-SUMO preparation used for binding.

The expression assays use BW25113/JW derivatives and engineered shared-promoter
reporters. They do not measure each endogenous gene transcript separately.
The available Entrez frlABCD loci identify MG1655, and main-text methods do not
establish complete reporter-DNA equivalence. Accordingly those gene instances
are not used as direct experimental targets. Process-level regulatory context
preserves the supported mechanism without inventing promoter/operon identifiers.
The CRP attribution follows cyaA manipulation, glucose response and promoter
truncation; it is not a new direct CRP binding experiment. Frl6P recognition is
an inducer hypothesis supported genetically, not a measured ligand-binding edge.
No FrlR autoregulation or full-length dimer stoichiometry is inferred.

The original Tn5 catalog remains a separate evidence gap until inspected. Native
and reviewed annotations can support their explicit assertions but cannot be
reported as personally verified primary experiments.

No independent psicoselysine-phosphorylation bypass is asserted from FrlD's
slow side activity. No direct FrlR binding, promoter mechanism or hypothetical
cofactor-free activity is inferred from the 2004 study. No source-exhaustion
claim follows from this candidate assessment.

## Verification

The integrated draft has 23 participants, three core reactions, three taxon
scopes, 35 evidence-linked edges and 30 references. Its SHA-256 is
`3e5b25fc917a30aca70b1dbdce4c70cb7b2d69f595b1f0f13d391812b7cdcb93`.
Rendering, KGX export, lint, full `just validate` and `just test` have passed
against these unchanged bytes. The test suite reports 4,867 passed and three
skipped, with seven dependency warnings. `git diff --check` also passes.
The canonical authority union preserves all 4,747 baseline
terms and 738 owners and adds ten terms and four owners. The identifier gate
passes across all 245 records. The saved scientific review gives a qualified
pass with zero findings; its original source-reading and experimental limits
remain explicit in the [review report](../../../../reviews/structured/20261014T072939Z-fructoselysine-psicoselysine246-scientific/review.md)
and [authoritative review YAML](../../../../reviews/structured/20261014T072939Z-fructoselysine-psicoselysine246-scientific/review.yaml).
GitHub CI and publication outcomes are tracked by the associated pull request.

Compact evidence, source-to-graph assessments and external archive receipts
are retained under this dossier. Original scientific sources stay outside the
repository. Generated graph and export verification is automated and static;
an attempted interactive preview was unavailable because this session exposed
no browser. A separate SVG raster overview rendered without apparent clipping;
the dense qualified branches require zoom/scroll. The existing graph interaction
tests passed during the full suite.

The fresh duplicate audit covers the whole base-4d0546 worktree including
hidden and ignored files, with no directory exclusions. It independently
inventories all 244 existing maintained YAMLs. The only semantically overlapping
maintained record is GO:1901281, whose full bytes are unchanged. Compressed
archive interiors were not decoded, and symlink directories were not followed;
the receipt states those bounds. Prior PathBank screening and source-discovery
mentions were read as candidate dispositions, not counted as maintained records.

The initial independent draft review identified one minor source-local wording
finding, tracked by issue 514. Six assertions were narrowed to their cited
native facts; all other parsed values were unchanged at that repair checkpoint.
The independent disposition and exact before/after hashes are retained. This
precedes the later evidence additions and is not invented structured-review
lineage. The completed native scientific review independently assesses all
35 edges in the integrated record and retains the verified repair as an
assessment, without inventing a structured predecessor.

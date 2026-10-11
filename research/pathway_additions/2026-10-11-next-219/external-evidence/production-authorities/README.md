# Denitrification authority preparation

This external directory prepares production identifier authorities for the
corrected denitrification candidate. No maintained file or shared source-cache
body has been changed. It is not an independent scientific review.

The provisional lock captured committed ED head
`1129f57f9b4349acbde446065ddbf6f4f8253a10`, tree
`66033d3ab5ea79232e7e635b39568ef81939e29c`, with 219 records. Its actual parent
baseline is the earlier Myx merge, not an assertion that ED itself has merged.
All five authority/policy owners and complete local runtime/corpus inventories
are pinned. The exact five owner bodies are preserved under `baseline/`.

The original 25 proposed source bodies were parsed with the current canonical
source builder. Their native version fields and exact successful acquisition
locators are preserved in `preliminary-assessment.json`. All 216 retained
UniProt inputs were hash-checked and searched as complete native bodies; none
contains the 13 proposed proteins. No exact proposed URL or body digest occurs
in the retained manifest. Existing production metadata is preserved unchanged.

Expected changes are 25 new source inputs and 11 newly selected ChEBI terms.
GO:0016020 already has production coverage. The corrected candidate handoff is
sealed at `165488e9856288c962586a2127b1efe9cad848a1e49833fe1f76e2218ca8e860`;
its target is `7c5b3ca9714dd9968901921b54bb82f44b08f85da322cb5527453ac685568ecd`
and authority proposal is
`fbbd55cf8e0b388c711f6f8590e66f2fe8c142f48249ee238af4f36f6713110c`.
All 25 source rows are identical to the original proposal. The author's actual
successor replay is separate evidence; it does not constitute independent
production-authority acceptance.

`prepare-selection.py` requires the corrected handoff, target and proposal with
their explicit expected hashes, plus a root-observed actual ED merge receipt
and commit. It checks the actual merged tree and every baseline owner, runtime
and corpus blob against the frozen ED bytes. Only then can it produce a fresh
external selection directory. Its version metadata comes from the original
MetaCyc database/software footer or individual UniProt entryAudit. No UniProt
release is inferred from an entry annotation date.

`dry-run-authorities.py` requires the selection's exact expected digest and a
fresh external output directory. It stages source-cache links externally and
uses the unchanged canonical ontology and source builders. It selects every
prior authority ID plus the candidate IDs, verifies complete preservation of
all previous terms and source metadata, and runs the current identifier checker
against a one-record external root. All source-body identities/digests and all
four whole production SQL databases are checked at completion; shared cache
bodies are never written. Rhea139 SQL and existing Rhea142 RDF updates retain
their separate production provenance.

Neither final selection nor canonical dry-run has executed yet. The actual ED
merge receipt is pending. No source/helper/target edits, final authority seal,
full-corpus validation, GitHub action or scientific approval is claimed here.

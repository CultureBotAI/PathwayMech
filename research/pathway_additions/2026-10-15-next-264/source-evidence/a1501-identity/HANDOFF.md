# A1501 exact issuing identity supplement

This is source-author evidence for PMID:20137101, not an independent scientific
review, a final record selection, or a source-exhaustion claim. All original
responses are preserved unchanged; canonical parser copies match the maintained
baseline. No maintained files, Git state, or GitHub state were changed.

The selected handoff is BenR NCBIProtein:ABP79350.1, benA
KEGG:psa:PST_1667 (canonical label PST_1667; category gene), and
NCBITaxon:379731 (Stutzerimonas stutzeri A1501). BenB/C/D exact identities are
corroboration and do not require additional named graph nodes. The deposited
genome explicitly links benR/PST_1666 to ABP79350.1 and benA–benD/PST_1667–1670
to ABP79351.1–ABP79354.1. All five full CDS translations equal their exact
protein records. All four KEGG gene nucleotide and amino-acid sequences equal
the deposited genome and protein originals. KEGG T00511 explicitly links psa,
taxon379731, and chromosome CP000304.

Reference owners and original paths relative to this package:
- BenR protein: originals/NCBI-ben-proteins.xml (complete five-entry batch,
  SHA256 39e3046eb31036a6caf671458a285582e1bf0f3f56c2b3de7893a3a0b03437f2).
  Use its exact accession-version entry, not a generated single-entry export.
- benA gene: originals/KEGG-psa-PST_1667.txt,
  SHA256 7f6f39584b4bd5a06fdef2e3f1a55e4e2f620ddc60c25c4e5b8393002e5f3eb2.
- Strain: originals/NCBI-taxonomy-379731.xml,
  SHA256 6d765bacb6bdbb0dfb672bd2d6c0b93ece5a97a2ff1566e30640eb45281f2007.
- Genome sequence/annotations: originals/NCBI-CP000304.1.xml,
  SHA256 487a08994e58107635ffe761643d29a2a81f633084122f6037e0379159f64656.
- Genome crosswalk: originals/KEGG-genome-T00511.txt.
Exact request URLs, HTTP200 responses, retrieval times, byte sizes and hashes
are in the corresponding acquisitions/*.json. Use retrieved 2026-10-15, not an
inferred release. Taxon authority remains the pinned NCBITaxon2026-07-12 owner;
live taxonomy is corroborating evidence, not a silent snapshot refresh.

The primary Table2 benA qPCR primers map uniquely to genome positions1786665
and1786832 (reverse complement), producing the printed186bp amplicon within
PST_1667. Optional junction primer pairs RT1/RT2/RT3/RT5 map uniquely but yield
786/453/500/598bp instead of printed782/456/503/610bp. RT4 yields printed546bp.
Both observations are retained in identity-verification.replay.json. Do not
claim that all printed junction lengths reproduce; the paper's qualitative
co-transcription evidence and this sequence check have distinct evidential roles.
The initial all-length assertion failed and is retained with its exact helper
and log. Its successor explicitly records the discrepancies without changing
the paper, genome, or protein originals.

No direct BenR–DNA binding, new operon CURIE, A1601/A1608 taxon, assay construct
sequence, or catalytic function is inferred from identifier resolution.

Read-only reproduction, writing one new external JSON:
  /private/tmp/pathwaymech-next-263-verified-venv/bin/python -B \
    helpers/verify_a1501_identities.v3.py.txt \
    --source-root /absolute/path/to/this/package \
    --output /private/tmp/new-a1501-proof.json
The pinned external ncbitaxon.db is needed for one exact selected taxon query.
This identity replay does not assert a new complete database hash; the final
selected ontology CLI will hash complete pinned databases. Full originals and
gzip retention pairs are in the frozen manifests. Independent acceptance is
owned by the root/reviewer, not this correction/source author.

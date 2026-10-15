# Independent acceptance of issue 573 locator correction

The append-only successor for `NEXT264-BIO-LOC-01` is accepted. This is a minor source locator correction, not a new biological claim or canonical record review. Root owns integration and GitHub issue disposition.

The original identity metadata incorrectly names Methods 2.3. The complete original JATS labels the accession/locus paragraph as Methods 2.1, **DNA Techniques and Alignments**, at `/article/body/sec[@id="jobm70061-sec-0020"]/sec[@id="jobm70061-sec-0030"]/p[1]`. Methods 2.3 is **Heterologous Expression Constructs**.

Independent checks confirm that the successor changes exactly one JSON-encoded string, `$.primary_locator`. Every other byte, all 17 identity rows, the retained paragraph, source hashes and sequence decisions remain unchanged. The corrected paragraph contains all 17 printed locus/accession pairs. No sequence checks were repeated.

All 15 frozen successor artifacts and seven lossless compact pairs pass. Original metadata and complete JATS copies match the issuing originals exactly. The frozen biological identity package and prior independent primary review remain unchanged. P264-16 already had the correct Methods 2.1 locator. Only the nested successor package was assessed; the containing record-design directory was not assumed frozen.

Complete original and successor bodies, the exact compressed diff, independently executed checks, input hashes and preservation evidence are retained. No maintained files, Git/GitHub state, frozen predecessor package or runtime environment was modified.

# HADEG source attribution and retained terms

The four `source_row` objects and workbook fields in `finnerty-canary.json`
are a bounded selection from **HADEG: A Curated Hydrocarbon Aerobic Degradation
Enzymes and Genes Database**, by Jorge Rojas-Vargas, Hugo G. Castelán-Sánchez,
and Liliana Pardo-López. Original repository:
[jarojasva/HADEG](https://github.com/jarojasva/HADEG), pinned commit
`8f1ff8fb3b6452a0fd2667dc78686dced5cd4416`.

Citation: Rojas-Vargas J, Castelán-Sánchez HG, Pardo-López L (2023),
*Computational Biology and Chemistry*,
[doi:10.1016/j.compbiolchem.2023.107966](https://doi.org/10.1016/j.compbiolchem.2023.107966).

The upstream root `LICENSE` contains the GNU General Public License version 3.
Its exact text is retained as [GPL-3.0.txt](GPL-3.0.txt); its upstream URL and
SHA-256 appear in [acquisition-manifest.json](acquisition-manifest.json).
These source-derived fields retain the upstream terms; PathwayMech's own
repository license does not relicense them. The inspection found no distinct
table-data license in the complete pinned tree's license/readme/copyright
paths, README, or parsed cells of the five evidence workbooks. Sequence-file
contents were not exhaustively inspected for additional notices.

PathwayMech modifications, dated 2026-10-08: select the four rows assigned to
`A_Finnerty_pathway`; preserve their original fields and row/cell locators;
add separately sourced accession/taxon verification; add explicit biological
evidence assessments and an unsupported-group-membership flag. The result is
an association audit, not a corrected HADEG pathway or a reaction graph. The
full upstream tables, workbooks, and protein sequences are not redistributed
here.

UniProt and NCBI provide the independently checked accession and taxon facts.
Their URLs, access dates, entry versions where available, and artifact hashes
remain in the acquisition manifest and projection. Scientific interpretations
of the two linked primary papers are identified as PathwayMech review
assessments, separate from raw HADEG fields. No full article text is included.

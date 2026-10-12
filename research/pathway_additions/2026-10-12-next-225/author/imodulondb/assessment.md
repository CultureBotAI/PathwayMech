# Structured-source computational context

The E. coli MG1655 expression dataset is applicable as context. The exact current issuing dataset response includes `e_coli/precise_mg1655`; the author queried 16 named genes/regulators plus “threonine” and “aminoacetone”. Eighteen searches and all 13 matching module gene tables were retrieved on 2026-10-12 and replayed through the unchanged canonical client. The 32 original response bodies, exact request URLs, timestamps and hashes are retained in `attempt2/receipts.json`. The sandbox DNS failure in `attempt1` remains intact.

The console runner is absent from PATH, and the known local claw checkout has no installed `kg-microbe-sources` entry point. The approved no-install workflow uses a byte-identical copy of its existing `imodulondb.py` adapter with the explicit existing 195 Python environment and a body-recording transport. No UV command, dependency resolution or environment mutation occurred.

The bounded useful membership results are:

| Component key | Covered member genes |
| --- | --- |
| `e_coli/precise_mg1655/35` | `b3457` livH, `b3455` livG, `b3454` livF, `b3456` livM, `b3460` livJ |
| `e_coli/precise_mg1655/60` | `b3116` tdcC |
| `e_coli/precise_mg1655/78` | `b3460` livJ and `b3089` sstT |

All listed rows have native `in_imodulon=true`. The signed weights and exact thresholds are preserved in the compact replay result and original tables; their signs are not evidence for the polarity of a regulator edge. The direct searches also resolve tdh (`b3616`), yiaY (`b3589`), tynA (`b1386`), lrp (`b0889`), feaR (`b1384`), fnr (`b1334`), nsrR (`b4178`), dps (`b0812`) and mntH (`b2392`) to gene hits. An empty module list on a gene-name search does not establish absence from every expression module. The aminoacetone search had no result, which is not a biochemical negative.

These are computational expression associations. They do not establish the hypothetical TynA terminal chemistry, native reaction membership, assembly, metal occupancy, regulator binding, causal polarity, transporter stoichiometry or whole-route reconstruction. None creates a new mechanistic edge or overrides the primary/native evidence. The assessment is a bounded check of the current MG1655 dataset; it makes no statement of source exhaustion or equivalent module numbering in other datasets.

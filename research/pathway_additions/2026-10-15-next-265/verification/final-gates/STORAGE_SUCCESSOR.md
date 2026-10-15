# Archival storage successor

Issues [584](https://github.com/CultureBotAI/PathwayMech/issues/584) and [585](https://github.com/CultureBotAI/PathwayMech/issues/585) record archival whitespace and ignored evidence logs found during publication checks. Original bytes are preserved without normalization in exact gzip owners. Ignore and whitespace policies are unchanged.

`artifact-manifest.json` and any original compact manifest remain byte-identical **historical reconstruction inventories**, not current physical inventories. The original package has 18 files including its manifest; 8 original physical paths are relocated.

[storage-successor.json](storage-successor.json) lists every original file and exact original/stored hashes and sizes for each relocation. Copy unchanged original paths and decode the mapped owners into a separate directory before using the original manifests, compact maps or helpers. All other original paths remain unchanged. [physical-artifact-manifest.json](physical-artifact-manifest.json) lists every current physical file except itself. Publication must compare this entire inventory and its manifest with actual staged blobs, including files matched by ignore rules.

Saved reviews remain immutable observations of their originally inspected files. This storage change requires separate technical acceptance and actual staged checks.

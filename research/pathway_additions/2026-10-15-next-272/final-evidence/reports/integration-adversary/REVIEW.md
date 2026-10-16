# Independent next272 integration and rendering review

Qualified acceptance of the exact maintained ethanolamine record and generated artifacts below. No blocking integration or rendering defect was found. This reviewer authored the authority adapter and earlier retention package, so this review explicitly excludes acceptance of those owners. Scientific evidence and bibliography enrichment are reviewed separately.

## Bound inputs and unchanged baseline

- Baseline commit: `54e768a985d07705ea25445804c83b4758646e37`.
- Accepted graph selection: `3a5438516cb6bd82075e575dbb152eaba84337ac8371a400b8b6ce964506a29e`.
- Maintained record: `f1fd9402cab31bf3c62d53ef630abc52308c2c0e2d7b61d7ad6b9c0aaba8fb1e`.
- Maintained record page: `512da61936745f9361b21b44ce819f4fb59e4598ac29483aacf9530fbcd94127`.
- All 268 old YAML records and 268 old HTML record pages remain byte-identical. The tracked hidden `.gitkeep` is separately retained, not counted as a record.
- Current physical data/pathways and pages inventories include hidden/ignored files and reject symlinks. Exactly one record and one record page are added; there are no additional unexpected page files. Assets and renderer-contract source files remain baseline-identical.

`baseline.tar.gz` contains exact immutable Git blobs for the old records/pages, global outputs and renderer-contract sources. `reviewed-inputs.tar.gz` contains the exact adopted record, new page, changed global outputs, record history, justfile and history scaffolder. Each has a portable member/hash manifest. A final complete physical recheck confirms the reviewed maintained artifact bytes did not change during this review.

## Complete source-to-artifact preservation

The independent checker imports no renderer/exporter/adapter code. It parses maintained YAML, HTML with a separate DOM parser, standalone SVG XML and actual TSV/JSON cells. All 31,222 checks pass. The record preserves all 97 accepted edge objects, 24 complete endpoint qualifications and all participants/reactions/taxa exactly. All 275 original reference identities and their URL/version/hash provenance remain unchanged. Nine provisional reference metadata objects are enriched and 16 narrative references are added; their scientific accuracy is outside this review. Every adopted reference object cited by an exported edge survives in KGX, including qualifier-only citations.

The ordinary page shows all 127 component declarations and retains all 36 disconnected graph components. Its SVG has 150 display nodes, including 24 separate qualified endpoints, and 97 directed arrows. Each arrow resolves to the correct evidence row; each qualified node resolves to its adjacent subject/object qualification. Native identifiers remain in the table and KGX. Full qualifier descriptions, supporting assertions or quotes, source locators and references remain accessible without JavaScript. The exact short EutC reporter qualification and the separate EutA/EAL states are preserved rather than attached to unqualified native nodes. Every narrative paragraph survives in the page.

KGX gains exactly 97 edges and 101 nodes. All prior edge rows remain exact, all old node source contexts survive, and unrelated node rows remain unchanged. New source contexts preserve local labels, categories and reaction directions. Shared direction fields agree with the full context set. Standalone CLI export bytes match the published TSV files exactly. Home, browse, pathway index and download manifest independently agree with the collection: 269 records, 105 taxa, 14,260 edges and 5,868 distinct references. The new index includes all 34 protein entries and six reaction IDs. Record history attribution, timestamp, summary, details and source-session link are intact.

All 1,206 structural geometry checks pass: node boxes do not overlap or leave the viewBox, text anchors remain inside it, arrow paths start at their declared subject box and terminate at their declared object box, and arrow markers resolve. The graph viewBox is 4106 by 17203. This is a large scrollable graph, not a single-screen overview. These are structural checks, not pixel, font-glyph clipping or interactive browser tests; no browser provider was available and none is claimed.

## Adverse probes and history wrapper

Seven actual-artifact corruption classes are rejected using in-memory byte-read overlays, with no maintained mutation: dropping disconnected context; collapsing a qualified endpoint to its native node; replacing the short reporter state with an unqualified full-length claim; reversing arrow endpoints; removing KGX endpoint qualification; replacing source-reference metadata; and changing an old page by one byte. Receipts retain every failed check. The first KGX qualification probe matched a generic duplicate description and selected an already-unqualified row. That invalid probe is preserved; the successor joins exact endpoints and evidence, asserts the preexisting qualifier, and correctly detects its removal.

The issue636 justfile change is independently accepted at SHA `f504ee9a297f95a3212c04be1993380fab88f1430367a192ad7aa7ec537900d2`. Its diff only adds positional-arguments forwarding and uses "$@" for new-history. The actual just recipe was invoked with subprocess argv (no outer shell), a history root containing spaces, multiword and multiline text, quotes, semicolon, ampersand, literal $HOME, command substitution and backticks, tab, Unicode and backslash. Exact summary/details and codex attribution survive; exactly one scratch YAML is created, issue636 becomes its full URL, and three side-effect sentinel files remain absent. Ten end-to-end checks pass. This review does not claim every other just recipe has been hardened.

## Review harness corrections and limits

All initial receipts are retained. Baseline counting first included the tracked .gitkeep; the corrected count distinguishes record YAMLs. A provisional whole-reference-object equality probe exposed expected bibliography enrichment; the final graph audit requires exact original identity/provenance and exact adopted metadata in downstream artifacts while leaving enrichment accuracy to the scientific reviewer. A history probe initially required the session ID as visible text; the established page instead exposes the exact source-session link, which the corrected check verifies. These were reviewer expectation corrections and did not change maintained code or data.

All operations are terminal. No maintained, Git/GitHub, installation or runtime repair writes were performed by this review. History regression output is confined to this scratch owner. This packet becomes immutable at freeze; corrections require a separate successor.

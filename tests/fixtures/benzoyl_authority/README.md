# Complete native benzoyl authority fixtures

These eight gzip files contain exact complete MetaCyc 27.0 mirror XML originals,
not synthetic source responses. They were copied from the independently reviewed
next266 native/design preparation. The root agent separately acquired literal
`getxml?id=META:<frame>` responses on 2026-10-15; every byte equals the retained
reviewed original. `acquisition.json` preserves those eight request receipts,
including request/final URLs, timestamps, byte counts and SHA-256 digests.
`manifest.json` records exact original sizes/digests and executable test entries.

The XML is stored losslessly as `<original-name>.xml.gz`, with gzip modification
time zero and no embedded filename. This preserves source whitespace while
avoiding trailing-whitespace errors from Git's text-diff checks. `storage.json`
maps each logical XML name to its compressed path, size and SHA-256, and records
the original size and SHA-256. `manifest.json` and `acquisition.json` retain their
original bytes and describe the decoded XML. The test loader verifies compressed
and decoded sizes/hashes, checks agreement with the original manifest, and writes
the exact XML bytes under their logical names into pytest's temporary directory.

The selected six source objects exercise five independent bounded source kinds.
RXN-15012 and RXN-15013 are complete Oah constituent originals and separate
ordinary unnamed reaction owners; both roles use the same exact bytes. The
fixtures retain all comments, credits, citations, species and activity context,
ferredoxin instance/subclass and equation lists, and envelope metadata.
No scientific claim is inferred from an identifier parser accepting the source.

The native mirror source terms remain applicable. Public-release licensing is
being handled separately under the user's existing instruction.

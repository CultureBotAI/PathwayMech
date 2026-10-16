# Bounded native glutaryl authority fixtures

All 49 gzip files contain complete, unmodified issuing XML originals independently acquired before implementation. The production originals and successful acquisition receipt mappings are retained under `research/pathway_additions/2026-10-15-next-269/authority-source-originals/`; fixtures are separate copies, not production authority.

`manifest.json` carries the actual acquisition request, release and original digest. `storage.json` binds both original and compressed bytes. Tests verify hashes and lengths before decompression, then exercise producer/consumer replay, full identity/profile failures, absent embedded identities, canonical-label and role enforcement, exact request syntax, preselection downgrade rejection, generic ETF class preservation, pathway/composite membership and activity-versus-Reaction distinctions.

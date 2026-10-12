"""Produce compact selected-fact dossiers without copying complete database prose."""

import hashlib
import json
import shutil
from datetime import UTC, datetime
from pathlib import Path

B = Path(__file__).resolve().parent
D = B / "draft"
F = Path("/private/tmp/pathwaymech-staphyloferrin-a-followup-20261011")


def sha(p):
    with Path(p).open("rb") as s:
        return hashlib.file_digest(s, "sha256").hexdigest()


def save(n, v):
    (D / n).write_text(json.dumps(v, indent=2, ensure_ascii=False) + "\n")


m = json.loads((F / "source-manifest.json").read_text())
sources = []
allowed = {
    "name",
    "url",
    "path",
    "sha256",
    "bytes",
    "retrieved_at",
    "status",
    "final_url",
    "content_type",
    "version_headers",
    "accepted",
    "kind",
    "receipt",
    "acquisition_receipt",
    "reused_from",
}
for x in m["sources"]:
    assert sha(x["path"]) == x["sha256"]
    s = {k: v for k, v in x.items() if k in allowed}
    s["hash_scope"] = "complete original response body"
    sources.append(s)
for x in m["chemistry_authorities"]:
    sources.append(
        x
        | {
            "hash_scope": (
                "complete original gzip RDF, direction TSV or uncompressed Semantic SQL database"
            ),
            "role": "independent chemical/direction/ontology authority",
        }
    )
save(
    "staphyloferrin-a-source-manifest.json",
    {
        "created_at": datetime.now(UTC).isoformat(),
        "sources": sources,
        "acquisition_attempts": [
            {k: v for k, v in x.items() if k in allowed | {"error"}}
            for x in m["acquisition_attempts"]
        ],
        "web_only": [
            {
                "id": "PMID:19400778",
                "url": m["web_only"][0]["url"],
                "inspected_at": datetime.now(UTC).isoformat(),
                "scope": (
                    "Original primary Results/Table2 and Figure5; Figure3 retained "
                    "as transcriptional context. Independently reopened during auth"
                    "oring. No local full-body bytes/hash; indexed abstract is sepa"
                    "rately retained."
                ),
            }
        ],
        "prior_handoff": {"path": str(F / "handoff.json"), "sha256": sha(F / "handoff.json")},
        "license_scope": (
            "MetaCyc/KEGG database terms and primary-article terms remain s"
            "ource-specific; public retrieval is not redistribution clearan"
            "ce. Original articles and native full commentary remain outsid"
            "e proposed files."
        ),
    },
)
shutil.copyfile(B / "staphyloferrin-a-dedup.json", D / "staphyloferrin-a-dedup.json")
a = json.loads((D / "staphyloferrin-a-dedup.json").read_text())
a["conclusion"] = (
    "No maintained exact pathway in either searched checkout. Curre"
    "nt annotation Q2FW72 and original ignored DRAM M00876 support "
    "rows are leads, not curated records. SAC substring matches are"
    " unrelated sulfate/phosphatase records."
)
a["prior_mentions_read"] = [
    "research/cross_mech/2026-10-05/inputs/uniprot_annotations.json:16918-16928",
    (
        "original reports/local_source_ingestion/2026-10-08-dram-seed/d"
        "ram/module_step_form.tsv:3284-3286"
    ),
    (
        "sealed followup assessment.md, native-projection.json, protein"
        "-scope.json, chemistry.json, stereochemistry.json and source-m"
        "anifest.json"
    ),
]
save("staphyloferrin-a-dedup.json", a)
proteins = json.loads((F / "protein-scope.json").read_text())
save(
    "staphyloferrin-a-protein-projection.json",
    {
        "scope": (
            "Original versioned Newman identities; NCTC 8325 sequence compa"
            "rison, not strain or construct identity. No invented assembly."
        ),
        "comparisons": proteins,
        "raw_ncbi_xml": str(F / "originals/Newman-proteins.xml"),
        "sha256": sha(F / "originals/Newman-proteins.xml"),
    },
)
# The context remains ancillary and does not create regulatory/catalytic edges.
save(
    "staphyloferrin-a-imodulondb-context.json",
    {
        "source_context_path": str(F / "imod-context.json"),
        "source_context_sha256": sha(F / "imod-context.json"),
        "original_manifest_path": str(F / "imod-manifest.json"),
        "original_manifest_sha256": sha(F / "imod-manifest.json"),
        "interpretation": json.loads((F / "imod-interpretation.json").read_text()),
        "scope": (
            "Previously executed unchanged canonical-client searches and ta"
            "ble parsing; selected USA300HOU rows with cross-strain annotat"
            "ions are expression context only. Component55 canonical parsin"
            "g failure on unrelated null metadata is retained separately fr"
            "om native row inspection. No new API acquisition during author"
            "ing."
        ),
    },
)
(D / "staphyloferrin-a-curation.md").write_text(
    "# Staphyloferrin A: complete external author draft\n\nThe exact "
    "native pathway is MetaCyc PWY-7990, corroborated by KEGG M0087"
    "6. All three transformations are represented: reversible ornit"
    "hine racemization selected toward D-ornithine, SfaD N5-citryla"
    "tion, and SfaB terminal N2-citrylation. Neither the racemizati"
    "on nor an energetically inconvenient side species was dropped."
    " No additional net reaction double-counts the two ligations.\n\n"
    "The original Rhea 142 sides give 16 chemical incidences and ba"
    "lance all three transformations independently. Their sum consu"
    "mes one L-ornithinium, two citrate and two ATP, and produces o"
    "ne staphyloferrin A(5-), two AMP, two diphosphate and two hydr"
    "ons. This is equation bookkeeping, not a newly measured cellul"
    "ar ATP/product ratio. The native reversible racemase and its b"
    "idirectional Rhea11587 cross-reference are explicitly distingu"
    "ished from selected Rhea11585.\n\nThe represented organism is Ne"
    "wman (taxon426430), with exact versioned GenPept BAF68351.1/NW"
    "MN_2079, BAF68352.1/NWMN_2080 and BAF68354.1/NWMN_2082. Issuin"
    "g-source locus aliases are the node labels; the historical gen"
    "eric product definitions do not erase the separately supported"
    " SfaC/B/D roles. These genomic identities are not engineered c"
    "onstruct identities. The original 2010 complete article explic"
    "itly identifies Newman coding regions for the two recombinant "
    "ligases used together in product synthesis. The 2009 Cotton ab"
    "stract establishes their ordered individual chemistry; its ful"
    "l methods/supplement were unavailable, so precise RN4220 prepa"
    "ration claims are not imported from secondary accounts.\n\nSfaC "
    "is deliberately inferred. Native MONOMER-20490 says the assign"
    "ment is assumed and the enzyme was not purified. The unreviewe"
    "d Q2FW73 entry has automatic ARBA PLP evidence. Equality of it"
    "s sequence with Newman BAF68351.1 permits a qualified sequence"
    "-based annotation transfer but cannot create a direct binding "
    "or activity experiment. The analogous exact sequence equality "
    "for SfaB is retained; Newman SfaD differs from Q2FW70 at resid"
    "ue532. No native protein object is treated as an independently"
    " measured monomer or fixed biosynthetic complex. The functiona"
    "l enables relations do not claim monomer sufficiency.\n\nThe nat"
    "ive ENZRXN26283/26284 Mg2+ entries are curated cofactor annota"
    "tions citing Cotton. Their transfer to the Newman ligase roles"
    " remains explicit inference with no independently inspected me"
    "tal-dependence experiment, binding count or exclusive physiolo"
    "gical metal. Cofactors are separate relations, not consumed su"
    "bstrate substitutions. No unsupported compartment is assigned."
    "\n\nThe source-specific chemical distinction is material. Native"
    " CPD21047/CPD12589 structures leave citryl stereocenters unspe"
    "cified. Current ChEBI142972 specifies the N5-(S) intermediate;"
    " ChEBI142973 specifies N2-(R),N5-(S) product with D-ornithine "
    "alpha R. The original 2010 Figure2A was visually inspected aga"
    "in, and Results sec18 paragraph2 explains why the S,S model fi"
    "ts worse. This is ferric receptor-bound product evidence, not "
    "a free intermediate stereochemical assay or protonation measur"
    "ement. Current free ionic forms and the intermediate assignmen"
    "t remain explicit chemical-authority conventions. No SSSOM exa"
    "ctMatch is claimed across the native/current specificity gap. "
    "The old ChEBI84711 historical uncertainty and 2024 conjugate s"
    "tudy are preserved in the discovery handoff, not used to overr"
    "ide the inspected native product structure.\n\nBeasley2009 origi"
    "nal publisher Results and Table2 independently connect the thr"
    "ee Newman loci to their roles, while Figure5 supports whole-lo"
    "cus product formation. Figure3 supplies transcriptional contex"
    "t only. Public-web access succeeded but a full local article b"
    "ody was unavailable; its reference deliberately has no fabrica"
    "ted body hash. The retained indexed abstract has its own origi"
    "nal hash. iModulon context uses a different strain background "
    "and cannot establish Newman mechanism or direct regulation; na"
    "tive-table observations are separated from a canonical parser "
    "failure on unrelated null metadata.\n\nExport/uptake through Sfa"
    "A, HtsABC and FhuC, ferric loading, citrate synthesis and stap"
    "hyloferrin B are outside the exact three-member biosynthetic b"
    "oundary. The other native racemase controller CPLX7173 is not "
    "imported from another organism. No pathway-specific assembly o"
    "r regulation is invented to fill source omissions.\n\nFresh dedu"
    "plication included hidden and ignored files in both the curren"
    "t211 checkout and original Documents checkout, excluding only "
    "Git internals and Python environments. The Q2FW72 cross-Mech a"
    "nnotation and ignored DRAM module rows were read as prior lead"
    "s. Exact source identity/labels were checked in an external sa"
    "ndbox using unchanged production parsers and policy; this does"
    " not integrate authority snapshots or certify publication read"
    "iness.\n\nThe proposed files contain short selected facts, origi"
    "nal-byte manifests, locators, source-to-graph and graph-to-sou"
    "rce dispositions, and reproducibility checks. Full primary bod"
    "ies and native comments remain external. Database and article "
    "reuse terms remain source-specific; no public-release license "
    "clearance is inferred. Final corpus gates, curation history, g"
    "enerated pages, independent scientific review and publication "
    "are pending root integration. This author replay is not scient"
    "ific self-approval.\n"
)
print("Dossiers prepared", len(sources), "original inputs")

curation_path = D / "staphyloferrin-a-curation.md"
text = curation_path.read_text()
for old, new in {
    "Rhea11587": "Rhea 11587",
    "Rhea11585": "Rhea 11585",
    "taxon426430": "taxon 426430",
    "residue532": "residue 532",
    "ENZRXN26283/26284": "ENZRXN-26283 / ENZRXN-26284",
    "CPD21047/CPD12589": "CPD-21047 / CPD-12589",
    "ChEBI142972": "ChEBI 142972",
    "ChEBI142973": "ChEBI 142973",
    "ChEBI84711": "ChEBI 84711",
    "Figure2A": "Figure 2A",
    "sec18 paragraph2": "section 18 paragraph 2",
    "Beasley2009": "Beasley 2009",
    "Table2": "Table 2",
    "Figure5": "Figure 5",
    "Figure3": "Figure 3",
    "CPLX7173": "CPLX-7173",
    "current211": "current 211-record",
}.items():
    text = text.replace(old, new)
curation_path.write_text(text)

"""Synthetic Gene XML proves identity boundaries; originals remain external."""

from __future__ import annotations

import copy
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path
from xml.etree import ElementTree as ET
from xml.parsers.expat import ExpatError

import pytest
import yaml

from pathwaymech.identifiers import identifier_errors
from scripts.build_source_identifier_snapshot import build_snapshot, source_terms

URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=gene&id=948224&rettype=xml"
DOCTYPE = (
    '<!DOCTYPE Entrezgene-Set PUBLIC "-//NLM//DTD NCBI-Entrezgene, 21st January 2005//EN" '
    '"https://www.ncbi.nlm.nih.gov/data_specs/dtd/NCBI_Entrezgene.dtd">'
)
BODY = """<Entrezgene-Set><Entrezgene>
<Entrezgene_track-info><Gene-track><Gene-track_geneid>948224</Gene-track_geneid>
</Gene-track></Entrezgene_track-info>
<Entrezgene_gene><Gene-ref><Gene-ref_locus>adeP</Gene-ref_locus>
<Gene-ref_locus-tag>b3714</Gene-ref_locus-tag><Gene-ref_syn>
<Gene-ref_syn_E>purP</Gene-ref_syn_E><Gene-ref_syn_E>yieG</Gene-ref_syn_E>
</Gene-ref_syn><Gene-ref_formal-name><Gene-nomenclature>
<Gene-nomenclature_symbol>adeP</Gene-nomenclature_symbol>
</Gene-nomenclature></Gene-ref_formal-name></Gene-ref></Entrezgene_gene>
<Entrezgene_source><BioSource><BioSource_org><Org-ref>
<Org-ref_taxname>Escherichia coli str. K-12 substr. MG1655</Org-ref_taxname>
<Org-ref_db><Dbtag><Dbtag_db>taxon</Dbtag_db><Dbtag_tag><Object-id>
<Object-id_id>511145</Object-id_id></Object-id></Dbtag_tag></Dbtag></Org-ref_db>
</Org-ref></BioSource_org></BioSource></Entrezgene_source>
<Entrezgene_prot><Prot-ref><Prot-ref_name><Prot-ref_name_E>Not a gene name</Prot-ref_name_E>
</Prot-ref_name></Prot-ref></Entrezgene_prot>
</Entrezgene></Entrezgene-Set>"""
NATIVE = '<?xml version="1.0" encoding="UTF-8"?>\n' + DOCTYPE + "\n" + BODY
EXPECTED = [("Entrez:948224", "adeP", ["b3714", "purP", "yieG"])]


def parse(tmp_path, body=NATIVE, *, url=URL):
    source = tmp_path / "gene.xml"
    raw = body.encode() if isinstance(body, str) else body
    source.write_bytes(raw)
    result = list(source_terms("ncbi-entrezgene-xml", source, url=url))
    assert source.read_bytes() == raw
    return result


@pytest.mark.parametrize("encoding", ["UTF-8", "UTF-16", "UTF-16LE", "UTF-16BE"])
def test_original_external_doctype_and_status_omission_are_accepted(tmp_path, encoding):
    body = NATIVE.replace('encoding="UTF-8"', 'encoding="' + encoding + '"').encode(encoding)
    assert parse(tmp_path, body) == EXPECTED


def test_no_doctype_and_explicit_live_status_are_supported(tmp_path):
    body = BODY.replace(
        "</Gene-track>", '<Gene-track_status value="live">0</Gene-track_status></Gene-track>'
    )
    assert parse(tmp_path, body) == EXPECTED


def test_top_level_locus_is_not_overridden_by_nested_gene_or_protein_names(tmp_path):
    body = BODY.replace(
        "</Entrezgene_prot>",
        "</Entrezgene_prot><Entrezgene_comments>"
        "<Gene-ref><Gene-ref_locus>anotherGene</Gene-ref_locus>"
        "<Gene-ref_syn><Gene-ref_syn_E>alien</Gene-ref_syn_E></Gene-ref_syn>"
        "</Gene-ref></Entrezgene_comments>",
    )
    assert parse(tmp_path, body) == EXPECTED


@pytest.mark.parametrize(
    "url",
    [
        URL.replace("https:", "http:"),
        URL.replace("eutils.ncbi.nlm.nih.gov", "other.example"),
        URL.replace("eutils.ncbi.nlm.nih.gov", "eutils.ncbi.nlm.nih.gov.example.com"),
        URL.replace("eutils.ncbi.nlm.nih.gov", "user@eutils.ncbi.nlm.nih.gov"),
        URL.replace("eutils.ncbi.nlm.nih.gov", "eutils.ncbi.nlm.nih.gov:443"),
        URL.replace("db=gene", "db=protein"),
        URL.replace("id=948224", "id=948225"),
        URL.replace("id=948224", "id=0"),
        URL.replace("id=948224", "id=0948224"),
        URL.replace("id=948224", "id=948224,945851"),
        URL.replace("id=948224", "id="),
        URL.replace("rettype=xml", "rettype=json"),
        URL + "&id=948224",
        URL + "&extra=1",
        URL + "#fragment",
        URL + " ",
        URL.replace("&rettype=xml", ""),
    ],
)
def test_exact_requested_gene_identity_is_required(tmp_path, url):
    with pytest.raises(ValueError):
        parse(tmp_path, url=url)


def mutated(problem):
    root = ET.fromstring(BODY)
    gene = root[0]
    track = gene.find("Entrezgene_track-info/Gene-track")
    ref = gene.find("Entrezgene_gene/Gene-ref")
    org = gene.find("Entrezgene_source/BioSource/BioSource_org/Org-ref")
    if problem == "wrong-root":
        root.tag = "html"
    elif problem == "empty-set":
        root.remove(gene)
    elif problem == "two-genes":
        root.append(copy.deepcopy(gene))
    elif problem == "wrong-id":
        track.find("Gene-track_geneid").text = "945851"
    elif problem == "missing-id":
        track.remove(track.find("Gene-track_geneid"))
    elif problem == "duplicate-id":
        track.append(copy.deepcopy(track.find("Gene-track_geneid")))
    elif problem == "nested-id":
        ET.SubElement(track.find("Gene-track_geneid"), "extra").text = "948224"
    elif problem == "duplicate-track":
        gene.find("Entrezgene_track-info").append(copy.deepcopy(track))
    elif problem == "missing-locus":
        ref.remove(ref.find("Gene-ref_locus"))
    elif problem == "duplicate-locus":
        ref.append(copy.deepcopy(ref.find("Gene-ref_locus")))
    elif problem == "duplicate-gene-ref":
        gene.find("Entrezgene_gene").append(copy.deepcopy(ref))
    elif problem == "empty-locus":
        ref.find("Gene-ref_locus").text = " "
    elif problem == "placeholder-locus":
        ref.find("Gene-ref_locus").text = "unknown"
    elif problem == "numeric-locus":
        ref.find("Gene-ref_locus").text = "948224"
    elif problem == "nested-locus":
        ET.SubElement(ref.find("Gene-ref_locus"), "bold").text = "adeP"
    elif problem == "wrong-formal":
        ref.find("Gene-ref_formal-name/Gene-nomenclature/Gene-nomenclature_symbol").text = "add"
    elif problem == "duplicate-formal":
        ref.append(copy.deepcopy(ref.find("Gene-ref_formal-name")))
    elif problem == "missing-taxon":
        org.remove(org.find("Org-ref_db"))
    elif problem == "duplicate-taxon":
        org.find("Org-ref_db").append(copy.deepcopy(org.find("Org-ref_db/Dbtag")))
    elif problem == "invalid-taxon":
        org.find("Org-ref_db/Dbtag/Dbtag_tag/Object-id/Object-id_id").text = "taxon511145"
    elif problem == "taxon-id-and-string":
        ET.SubElement(
            org.find("Org-ref_db/Dbtag/Dbtag_tag/Object-id"), "Object-id_str"
        ).text = "511145"
    elif problem == "missing-taxon-name":
        org.remove(org.find("Org-ref_taxname"))
    elif problem == "secondary-status":
        ET.SubElement(track, "Gene-track_status", {"value": "secondary"}).text = "1"
    elif problem == "discontinued-status":
        ET.SubElement(track, "Gene-track_status", {"value": "discontinued"}).text = "2"
    elif problem == "contradictory-status":
        ET.SubElement(track, "Gene-track_status", {"value": "live"}).text = "2"
    elif problem == "duplicate-status":
        for _ in range(2):
            ET.SubElement(track, "Gene-track_status", {"value": "live"}).text = "0"
    elif problem == "redirect":
        ET.SubElement(track, "Gene-track_current-id")
    elif problem == "discontinue-date":
        ET.SubElement(track, "Gene-track_discontinue-date")
    elif problem == "bad-synonym":
        ET.SubElement(ref.find("Gene-ref_syn"), "unexpected").text = "alias"
    else:
        raise AssertionError(problem)
    return ET.tostring(root)


PROBLEMS = [
    "wrong-root",
    "empty-set",
    "two-genes",
    "wrong-id",
    "missing-id",
    "duplicate-id",
    "nested-id",
    "duplicate-track",
    "missing-locus",
    "duplicate-locus",
    "duplicate-gene-ref",
    "empty-locus",
    "placeholder-locus",
    "numeric-locus",
    "nested-locus",
    "wrong-formal",
    "duplicate-formal",
    "missing-taxon",
    "duplicate-taxon",
    "invalid-taxon",
    "taxon-id-and-string",
    "missing-taxon-name",
    "secondary-status",
    "discontinued-status",
    "contradictory-status",
    "duplicate-status",
    "redirect",
    "discontinue-date",
    "bad-synonym",
]


@pytest.mark.parametrize("problem", PROBLEMS)
def test_wrong_or_ambiguous_native_assertions_fail(tmp_path, problem):
    with pytest.raises(ValueError, match="NCBI Gene"):
        parse(tmp_path, mutated(problem))


@pytest.mark.parametrize("encoding", ["UTF-8", "UTF-16", "UTF-16LE", "UTF-16BE"])
@pytest.mark.parametrize(
    "declaration",
    [
        DOCTYPE[:-1] + ' [<!ENTITY alias "adeP">]>',
        DOCTYPE[:-1] + ' [<!ENTITY alias SYSTEM "file:///private/tmp/must-not-read">]>',
        DOCTYPE[:-1] + ' [<!ENTITY % remote SYSTEM "https://example.org/entity">%remote;]>',
        DOCTYPE.replace("https://www.ncbi.nlm.nih.gov/", "https://example.org/"),
        '<!DOCTYPE Entrezgene-Set SYSTEM "file:///private/tmp/must-not-read">',
    ],
)
def test_untrusted_declarations_fail_in_every_supported_encoding(tmp_path, encoding, declaration):
    body = '<?xml version="1.0" encoding="' + encoding + '"?>\n' + declaration + "\n" + BODY
    with pytest.raises((ValueError, ExpatError), match="NCBI Gene|entity"):
        parse(tmp_path, body.encode(encoding))


def fixture(tmp_path, body=NATIVE):
    source = tmp_path / "native.xml"
    source.write_bytes(body.encode() if isinstance(body, str) else body)
    entries = [
        {
            "key": "native",
            "kind": "ncbi-entrezgene-xml",
            "path": source.name,
            "url": URL,
            "version": "Synthetic fixture",
            "license": "Fixture",
            "sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        }
    ]
    manifest = tmp_path / "manifest.json"
    manifest.write_text(json.dumps(entries))
    records = tmp_path / "data" / "pathways"
    records.mkdir(parents=True)
    # This is an identifier-gate fixture, not a scientific pathway record.
    (records / "record.yaml").write_text(yaml.safe_dump({"id": "Entrez:948224", "label": "adeP"}))
    return manifest, records, entries


def test_native_terms_and_policy_gate_without_contextual_exemptions(tmp_path):
    manifest, records, _ = fixture(tmp_path)
    result = build_snapshot(manifest, records, tmp_path)
    assert result["terms"] == {
        "Entrez:948224": {
            "label": "adeP",
            "synonyms": ["b3714", "purP", "yieG"],
            "source": "native",
        }
    }
    (tmp_path / "conf").mkdir()
    policy = yaml.safe_load(Path("conf/identifier_policy.yaml").read_text())
    assert policy["namespaces"]["Entrez"]["policy"] == "canonical_or_synonym"
    assert not any(rule["namespace"] == "Entrez" for rule in policy["contextual_labels"])
    policy["namespaces"] = {"Entrez": policy["namespaces"]["Entrez"]}
    policy["contextual_labels"] = []
    (tmp_path / "conf" / "identifier_policy.yaml").write_text(yaml.safe_dump(policy))
    authority = tmp_path / "data" / "identifier_authorities" / "sources.json"
    authority.parent.mkdir()
    authority.write_text(json.dumps(result))
    for label in ["adeP", "yieG", "b3714"]:
        (records / "record.yaml").write_text(
            yaml.safe_dump(
                {
                    "id": "Entrez:948224",
                    "label": label,
                    "taxa": [],
                    "participants": [],
                    "reactions": [],
                }
            )
        )
        assert identifier_errors(tmp_path) == []
    (records / "record.yaml").write_text(
        yaml.safe_dump(
            {
                "id": "Entrez:948224",
                "label": "Curator name",
                "taxa": [],
                "participants": [],
                "reactions": [],
            }
        )
    )
    assert any("LABEL_MISMATCH" in e for e in identifier_errors(tmp_path))
    (records / "record.yaml").write_text(
        yaml.safe_dump(
            {
                "id": "Entrez:999999",
                "label": "adeP",
                "taxa": [],
                "participants": [],
                "reactions": [],
            }
        )
    )
    assert any("ID_NOT_FOUND" in e for e in identifier_errors(tmp_path))


@pytest.mark.parametrize(
    "mutation", [("adeP", "otherGene"), ("511145", "83333"), ("yieG", "otherAlias")]
)
@pytest.mark.parametrize("reverse", [False, True])
@pytest.mark.parametrize("selected", [False, True])
def test_conflicting_sources_fail_before_selection_in_both_orders(
    tmp_path, mutation, reverse, selected
):
    manifest, records, entries = fixture(tmp_path)
    other = tmp_path / "other.xml"
    other.write_text(NATIVE.replace(*mutation))
    entries.append(
        {
            **entries[0],
            "key": "other",
            "path": other.name,
            "sha256": hashlib.sha256(other.read_bytes()).hexdigest(),
        }
    )
    manifest.write_text(json.dumps(entries[::-1] if reverse else entries))
    if not selected:
        (records / "record.yaml").write_text("id: GO:1\nlabel: Unselected\n")
    with pytest.raises(ValueError, match="conflicting NCBI Gene"):
        build_snapshot(manifest, records, tmp_path)


@pytest.mark.parametrize("existing", [False, True])
@pytest.mark.parametrize(
    "problem", ["wrong-id", "two-genes", "redirect", "missing-locus", "missing-id"]
)
def test_real_cli_failure_preserves_existing_or_absent_output(tmp_path, existing, problem):
    manifest, records, _ = fixture(tmp_path, mutated(problem))
    output = tmp_path / "out" / "authority.json"
    if existing:
        output.parent.mkdir()
        output.write_bytes(b"previous independent authority\n")
    proc = subprocess.run(
        [
            sys.executable,
            "scripts/build_source_identifier_snapshot.py",
            "--manifest",
            str(manifest),
            "--cache-dir",
            str(tmp_path),
            "--records",
            str(records),
            "--output",
            str(output),
        ],
        capture_output=True,
        env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
    )
    assert proc.returncode != 0
    assert b"NCBI Gene" in proc.stderr
    assert (
        output.read_bytes() == b"previous independent authority\n"
        if existing
        else not output.exists()
    )


def test_unresolved_entrez_is_a_completeness_failure(tmp_path):
    manifest, records, _ = fixture(tmp_path)
    (records / "record.yaml").write_text(
        "id: Entrez:948224\nlabel: adeP\nparticipants:\n- id: Entrez:945851\n  label: add\n"
    )
    with pytest.raises(ValueError, match="unresolved source identifiers: Entrez:945851"):
        build_snapshot(manifest, records, tmp_path)

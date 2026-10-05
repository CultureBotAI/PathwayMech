from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from pathwaymech.cross_mech import (
    SlotSpec,
    build_pathway_index,
    build_report,
    fetch_sgd_uniprot_map,
    fetch_uniprot_annotations,
    load_config,
    main,
    normalize_accession,
    pathway_index_json,
    record_slug,
    record_url,
    resolve_target,
    scan_sibling,
    walk_path,
)

PATHWAY = {
    "id": "WikiPathways:WP5060",
    "label": "Peptidoglycan cytoplasmic synthesis and recycling pathways",
    "participants": [
        {"id": "UniProtKB:P0A749", "label": "murA"},
        {"id": "UniProtKB:P0A6B4", "label": "alr"},
        {"id": "EC:2.5.1.7", "label": "UDP-N-acetylglucosamine 1-carboxyvinyltransferase"},
        {"id": "EC:3.4.16.-", "label": "incomplete class"},
    ],
    "reactions": [{"id": "RHEA:18681", "label": "MurA reaction"}],
}
YEAST = {
    "id": "gomodel:YeastPathways_PWY-6074-1",
    "label": "zymosterol biosynthesis",
    "participants": [
        {"id": "SGD:S000001049", "label": "ERG11 Scer"},
        {"id": "SGD:S999999999", "label": "unmapped gene"},
    ],
    "reactions": [],
}
SGD_MAP = {"SGD:S000001049": ["P10614"]}


def write_yaml(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")


@pytest.fixture
def index():
    return build_pathway_index([PATHWAY, YEAST], SGD_MAP)


@pytest.fixture
def sibling(tmp_path: Path) -> Path:
    root = tmp_path / "AntibioticMech"
    write_yaml(root / "data" / "antibiotics" / "fosfomycin.yaml", {
        "identifier": "CHEBI:28915",
        "label": "fosfomycin",
        "molecular_targets": [
            {"target_label": "MurA", "protein_examples": [
                {"uniprot_id": "UniProtKB:P0A749-2"},
                {"uniprot_id": "UniProtKB:P00000"},
            ]},
        ],
        "related_records": [
            {"corpus": "PathwayMech", "identifier": "WikiPathways:WP5060",
             "label": "Peptidoglycan cytoplasmic synthesis and recycling pathways"},
            {"corpus": "NaturalProductMech", "identifier": "naturalproductmech:x"},
        ],
        "notes": "see https://culturebotai.github.io/PathwayMech/pages/records/"
                 "gomodel_YeastPathways_PWY-6074-1.html",
    })
    write_yaml(root / "data" / "antibiotics" / "fluconazole.yaml", {
        "identifier": "CHEBI:46081",
        "label": "fluconazole",
        "molecular_targets": [{"protein_examples": [{"uniprot_id": "UniProtKB:P10614"}]}],
        "related_records": [
            {"corpus": "PathwayMech", "identifier": "MetaCyc:NOT-A-RECORD"},
            {"corpus": "PathwayMech", "identifier": "WikiPathways:WP5060", "label": "Wrong"},
        ],
    })
    (root / "data" / "antibiotics" / "broken.yaml").write_text("a: [", encoding="utf-8")
    return root


SPEC_YAML = """
version: 1
mechs:
  AntibioticMech:
    records: data/antibiotics/**/*.yaml
    protein_slots:
      - path: molecular_targets[].protein_examples[].uniprot_id
        role: molecular target example
    link_slots:
      - path: related_records[]
        id_key: identifier
        label_key: label
        when: {corpus: PathwayMech}
"""


@pytest.fixture
def spec(tmp_path: Path):
    config = tmp_path / "sibling_mechs.yaml"
    config.write_text(SPEC_YAML, encoding="utf-8")
    return load_config(config)[0]


def test_accessions_are_normalized_and_prose_is_not_an_accession() -> None:
    assert normalize_accession("UniProtKB:P0A749") == "P0A749"
    assert normalize_accession("P0A749-2") == "P0A749"
    assert normalize_accession("UniProtKB:A0A0H3CE29") == "A0A0H3CE29"
    assert normalize_accession("MurA is P0A749") is None
    assert normalize_accession("CHEBI:28915") is None
    assert normalize_accession(None) is None


def test_slug_and_url_match_the_rendered_pages() -> None:
    assert record_slug("gomodel:YeastPathways_PWY-6074-1") == "gomodel_YeastPathways_PWY-6074-1"
    assert record_url("WikiPathways:WP5060").endswith("/pages/records/WikiPathways_WP5060.html")


def test_index_resolves_sgd_through_the_map_and_reports_unmapped_ids(index) -> None:
    assert index.records_for("P0A749") == ["WikiPathways:WP5060"]
    assert index.records_for("P10614") == ["gomodel:YeastPathways_PWY-6074-1"]
    assert index.unmapped_sgd == {"SGD:S999999999"}
    assert index.ec["WikiPathways:WP5060"] == {"2.5.1.7"}  # incomplete EC classes are dropped
    assert index.rhea["WikiPathways:WP5060"] == {"18681"}


def test_targets_resolve_by_id_slug_or_url_without_case(index) -> None:
    assert resolve_target(index, "WikiPathways:WP5060") == "WikiPathways:WP5060"
    assert resolve_target(index, "wikipathways_wp5060") == "WikiPathways:WP5060"
    url = "https://culturebotai.github.io/PathwayMech/pages/records/WikiPathways_WP5060.html"
    assert resolve_target(index, url) == "WikiPathways:WP5060"
    assert resolve_target(index, "MetaCyc:NOT-A-RECORD") is None


def test_walk_path_reports_concrete_positions() -> None:
    document = {"a": [{"b": [{"c": "x"}, {"c": "y"}]}, {"b": []}, {"z": 1}]}
    assert list(walk_path(document, "a[].b[].c")) == [("a[0].b[0].c", "x"), ("a[0].b[1].c", "y")]
    assert list(walk_path(document, "missing[].c")) == []
    with pytest.raises(ValueError):
        list(walk_path(document, "a[].b-c"))


def test_scan_finds_slot_proteins_configured_links_and_stray_urls(sibling, spec) -> None:
    proteins, links, errors = scan_sibling(sibling, spec)

    assert [(p.file, p.accession, p.slot) for p in proteins] == [
        ("data/antibiotics/fluconazole.yaml", "P10614",
         "molecular_targets[0].protein_examples[0].uniprot_id"),
        ("data/antibiotics/fosfomycin.yaml", "P0A749",
         "molecular_targets[0].protein_examples[0].uniprot_id"),
        ("data/antibiotics/fosfomycin.yaml", "P00000",
         "molecular_targets[0].protein_examples[1].uniprot_id"),
    ]
    targets = sorted((link.file.split("/")[-1], link.target) for link in links)
    assert ("fosfomycin.yaml", "WikiPathways:WP5060") in targets
    assert all("naturalproductmech" not in target for _, target in targets)
    assert any(target.endswith("gomodel_YeastPathways_PWY-6074-1.html")
               for _, target in targets)
    assert len(errors) == 1 and "broken.yaml" in errors[0]


def test_mixed_slots_ignore_other_identifiers(tmp_path: Path) -> None:
    root = tmp_path / "NaturalProductMech"
    write_yaml(root / "r.yaml", {"identifier": "x", "label": "x", "causal_graphs": [
        {"nodes": [{"identifier": "CHEBI:1"}, {"identifier": "UniProtKB:P0A749"}]}]})
    strict = SlotSpec(path="causal_graphs[].nodes[].identifier")
    mixed = SlotSpec(path="causal_graphs[].nodes[].identifier", mixed=True)
    for slot, expected_errors in ((strict, 1), (mixed, 0)):
        from pathwaymech.cross_mech import MechSpec

        found, _, errors = scan_sibling(root, MechSpec(name="NaturalProductMech",
                                                       records=["*.yaml"],
                                                       protein_slots=[slot]))
        assert [p.accession for p in found] == ["P0A749"]
        assert len(errors) == expected_errors


def test_report_marks_link_status_overlaps_and_candidates(index, sibling, spec) -> None:
    report = build_report(index, {"AntibioticMech": scan_sibling(sibling, spec)})

    statuses = sorted((row["file"].split("/")[-1], row["status"]) for row in report.link_checks)
    assert ("fluconazole.yaml", "unknown_record") in statuses
    assert ("fluconazole.yaml", "label_mismatch") in statuses
    assert statuses.count(("fosfomycin.yaml", "ok")) == 2
    assert len(report.broken_links) == 2

    overlap = {(row["file"].split("/")[-1], row["accession"], row["pathway_record"]):
               row["record_links_pathway"] for row in report.overlaps}
    assert overlap[("fosfomycin.yaml", "P0A749", "WikiPathways:WP5060")] is True
    # fluconazole holds Erg11 but does not link the zymosterol record
    assert overlap[("fluconazole.yaml", "P10614", "gomodel:YeastPathways_PWY-6074-1")] is False

    candidates = {(row["pathway_record"], row["accession"]) for row in report.example_candidates}
    assert ("WikiPathways:WP5060", "P0A6B4") in candidates  # alr: in the pathway, not held
    assert ("WikiPathways:WP5060", "P0A749") not in candidates  # already held


def test_reaction_matches_need_annotations_and_skip_direct_overlaps(index, sibling, spec) -> None:
    scans = {"AntibioticMech": scan_sibling(sibling, spec)}
    assert build_report(index, scans).reaction_matches == []
    annotations = {"P00000": {"rhea": ["RHEA:18681"], "ec": ["2.5.1.7", "3.4.16.-"]},
                   "P0A749": {"rhea": ["RHEA:18681"]}}
    rows = build_report(index, scans, annotations).reaction_matches
    assert [(row["accession"], row["basis"], row["shared_ec"]) for row in rows] == [
        ("P00000", "record_rhea", "EC:2.5.1.7")]


def test_participant_annotations_let_records_without_reactions_match(sibling, spec) -> None:
    # The yeast record states no Rhea or EC; its Erg11 participant's UniProt
    # annotation is what a sibling CYP51 ortholog can share.
    annotations = {"P10614": {"rhea": ["RHEA:25286"], "ec": ["1.14.14.154"]},
                   "P00000": {"rhea": ["RHEA:25286"], "ec": ["1.14.14.154"]}}
    index = build_pathway_index([PATHWAY, YEAST], SGD_MAP, annotations)
    assert index.participant_rhea["gomodel:YeastPathways_PWY-6074-1"] == {"25286"}
    rows = build_report(index, {"AntibioticMech": scan_sibling(sibling, spec)},
                        annotations).reaction_matches
    assert [(row["accession"], row["pathway_record"], row["basis"]) for row in rows] == [
        ("P00000", "gomodel:YeastPathways_PWY-6074-1", "participant_rhea")]


def test_cli_writes_tables_and_fails_on_broken_links(tmp_path: Path, sibling) -> None:
    # This test isolates broken links; scan failures have their own CLI test.
    (sibling / "data" / "antibiotics" / "broken.yaml").unlink()
    root = tmp_path / "PathwayMech"
    write_yaml(root / "data" / "pathways" / "wp5060.yaml", PATHWAY)
    write_yaml(root / "data" / "pathways" / "zymosterol.yaml", YEAST)
    config = tmp_path / "sibling_mechs.yaml"
    config.write_text(SPEC_YAML, encoding="utf-8")
    sgd = tmp_path / "sgd.json"
    sgd.write_text('{"SGD:S000001049": ["P10614"]}', encoding="utf-8")
    out = tmp_path / "out"

    args = ["--config", str(config), "--mech", f"AntibioticMech={sibling}",
            "--sgd-map", str(sgd), "--out", str(out)]
    assert main(args, root) == 0
    assert main([*args, "--check-links"], root) == 1
    summary = (out / "summary.md").read_text(encoding="utf-8")
    # slot values, accessions, in a pathway, pairs, unlinked pairs, links, broken links
    assert "| AntibioticMech | 3 | 3 | 2 | 2 | 1 | 4 | 2 |" in summary
    pairs = (out / "pairs.tsv").read_text(encoding="utf-8").splitlines()
    header = pairs[0].split("\t")
    assert "record_links_pathway" in header and len(pairs) == 3
    assert not (out / "overlaps.tsv").exists()
    assert main([*args, "--full-tables"], root) == 0
    assert (out / "overlaps.tsv").exists() and (out / "sibling_proteins.tsv").exists()
    assert main(["--config", str(config), "--mechs-root", str(tmp_path / "nowhere")], root) == 2


def test_summary_caps_listed_pairs_and_says_how_many_are_left(index, sibling, spec) -> None:
    from pathwaymech.cross_mech import render_summary

    report = build_report(index, {"AntibioticMech": scan_sibling(sibling, spec)})
    text = render_summary(report, list_limit=0)
    assert "AntibioticMech: 1 more pairs not listed here" in text
    assert "fluconazole" not in text.split("## Unlinked record-pathway pairs")[1].split(
        "more pairs")[0].split("AntibioticMech:")[0]


def test_glob_regex_matches_pathlib_semantics() -> None:
    from pathwaymech.cross_mech import glob_regex

    pattern = glob_regex("data/traits/**/*.yaml")
    assert pattern.match("data/traits/a.yaml")
    assert pattern.match("data/traits/x/y/a.yaml")
    assert not pattern.match("data/traits/a.yml")
    assert not pattern.match("data/other/a.yaml")
    assert not glob_regex("data/*.yaml").match("data/x/a.yaml")


def test_ref_mode_reads_committed_records_not_the_working_tree(tmp_path: Path, spec) -> None:
    import subprocess

    from pathwaymech.cross_mech import commit_of

    root = tmp_path / "AntibioticMech"
    record = root / "data" / "antibiotics" / "fosfomycin.yaml"
    write_yaml(record, {"identifier": "CHEBI:28915", "label": "fosfomycin",
                        "molecular_targets": [{"protein_examples": [
                            {"uniprot_id": "UniProtKB:P0A749"}]}]})
    git = ["git", "-C", str(root), "-c", "user.name=PathwayMech tests", "-c", "user.email=",
           "-c", "commit.gpgsign=false"]
    subprocess.run([*git, "init", "-q"], check=True)
    subprocess.run([*git, "add", "."], check=True)
    subprocess.run([*git, "commit", "-q", "-m", "seed"], check=True)
    commit = commit_of(root)
    assert len(commit) == 40
    # An uncommitted edit is visible to the working-tree scan only.
    write_yaml(record, {"identifier": "CHEBI:28915", "label": "fosfomycin",
                        "molecular_targets": [{"protein_examples": [
                            {"uniprot_id": "UniProtKB:P0A6B4"}]}]})
    working, _, _ = scan_sibling(root, spec)
    committed, _, errors = scan_sibling(root, spec, ref="HEAD")
    assert [protein.accession for protein in working] == ["P0A6B4"]
    assert [protein.accession for protein in committed] == ["P0A749"]
    assert [protein.file for protein in committed] == ["data/antibiotics/fosfomycin.yaml"]
    assert errors == []
    with pytest.raises(OSError, match="not a commit"):
        scan_sibling(root, spec, ref="no-such-branch")
    assert commit_of(tmp_path) == ""


def test_config_rejects_unknown_versions_and_bad_paths(tmp_path: Path) -> None:
    config = tmp_path / "c.yaml"
    config.write_text("version: 2\nmechs: {}\n", encoding="utf-8")
    with pytest.raises(ValueError, match="version"):
        load_config(config)
    config.write_text("version: 1\nmechs:\n  X:\n    records: a\n    protein_slots:\n"
                      "      - path: 'a..b'\n", encoding="utf-8")
    with pytest.raises(ValueError, match="invalid slot path"):
        load_config(config)


def test_uniprot_fetchers_parse_tsv_without_network() -> None:
    sgd_tsv = "Entry\tSGD\nP10614\tS000001049;\nQ00000\t\n"
    assert fetch_sgd_uniprot_map(lambda url: sgd_tsv) == {"SGD:S000001049": ["P10614"]}
    seen = []

    def fake(url: str) -> str:
        seen.append(url)
        return ("Entry\tReviewed\tOrganism (ID)\tEC number\tRhea ID\tPathway\n"
                "P0A749\treviewed\t83333\t2.5.1.7\tRHEA:18681\tPATHWAY: Cell wall biogenesis.\n")

    annotations = fetch_uniprot_annotations(["P0A749", "P0A749"], fetch=fake)
    assert annotations["P0A749"]["rhea"] == ["RHEA:18681"]
    assert annotations["P0A749"]["ec"] == ["2.5.1.7"]
    assert len(seen) == 1 and "accession%3AP0A749" in seen[0]
    assert "mailto" not in seen[0] and "@" not in seen[0]


def test_pathway_index_lists_records_pages_and_protein_participants() -> None:
    import json
    from types import SimpleNamespace

    records = [
        SimpleNamespace(id="WikiPathways:WP5060", label="PG", pathway_type="cell-wall",
                        taxa=[{"id": "NCBITaxon:562", "label": "Escherichia coli"}],
                        participants=PATHWAY["participants"] + [{"id": "CHEBI:1", "label": "x"}],
                        reactions=PATHWAY["reactions"]),
        SimpleNamespace(id="GO:42", label="minimal"),
    ]
    index = json.loads(pathway_index_json(records))
    assert index["format"] == "pathwaymech-pathway-index/1"
    assert [row["id"] for row in index["records"]] == ["GO:42", "WikiPathways:WP5060"]
    row = index["records"][1]
    assert row["page"] == "records/WikiPathways_WP5060.html"
    assert row["url"] == record_url("WikiPathways:WP5060")
    assert [protein["id"] for protein in row["proteins"]] == [
        "UniProtKB:P0A749", "UniProtKB:P0A6B4", "EC:2.5.1.7", "EC:3.4.16.-"]
    assert row["reactions"] == ["RHEA:18681"]


def test_rendered_site_publishes_the_index_and_it_is_current() -> None:
    import json

    root = Path(__file__).resolve().parents[1]
    published = root / "pages" / "pathway_index.json"
    from pathwaymech.cli import render_site
    from pathwaymech.yaml_io import load_pathway_records

    records = load_pathway_records(root / "data" / "pathways")
    rendered = render_site(records)
    assert published.read_text(encoding="utf-8") == rendered["pathway_index.json"]
    for row in json.loads(rendered["pathway_index.json"])["records"]:
        assert row["page"] in rendered, row["id"]


def test_page_gate_detects_and_renderer_repairs_a_stale_pathway_index(tmp_path: Path,
                                                                   capsys) -> None:
    from pathwaymech.cli import check_pages_main, render_pages_main

    pages = tmp_path / "pages"
    pages.mkdir()
    (pages / "style.css").write_text("", encoding="utf-8")
    (pages / ".nojekyll").write_text("", encoding="utf-8")
    assert render_pages_main([], root=tmp_path) == 0
    assert check_pages_main(root=tmp_path) == 0
    (pages / "pathway_index.json").write_text('{"records": []}', encoding="utf-8")
    assert check_pages_main(root=tmp_path) == 1
    assert "pages/pathway_index.json: not what its record renders to" in capsys.readouterr().err
    assert render_pages_main([], root=tmp_path) == 0
    assert check_pages_main(root=tmp_path) == 0


def test_repository_config_loads_and_names_real_slots() -> None:
    root = Path(__file__).resolve().parents[1]
    specs = load_config(root / "conf" / "sibling_mechs.yaml")
    assert {spec.name for spec in specs} >= {
        "TraitMech", "ProteinTraitsMech", "NaturalProductMech", "AntibioticMech",
        "CellStructureMech"}
    for spec in specs:
        assert spec.protein_slots, f"{spec.name} declares no protein slot"


def test_bad_timestamp_is_recorded_as_a_scan_error(tmp_path, spec):
    path = tmp_path / "data/antibiotics/date.yaml"
    path.parent.mkdir(parents=True)
    path.write_text("identifier: a\nretrieved: 2026-02-30\n")
    _, _, errors = scan_sibling(tmp_path, spec)
    assert len(errors) == 1 and "date.yaml" in errors[0]


def test_empty_reports_keep_headers_and_remove_stale_full_tables(tmp_path, index):
    from pathwaymech.cross_mech import write_report

    report = build_report(index, {"Mech": ([], [], [])})
    write_report(report, tmp_path, full=True)
    assert (tmp_path / "overlaps.tsv").read_text().startswith("mech\t")
    write_report(report, tmp_path)
    assert not (tmp_path / "overlaps.tsv").exists()
    assert not (tmp_path / "sibling_proteins.tsv").exists()
    assert (tmp_path / "link_checks.tsv").read_text().strip().endswith("status")


def test_unsupported_globs_cannot_diverge_between_working_and_ref_modes():
    from pathwaymech.cross_mech import glob_regex

    for pattern in ("data/[ab].yaml", "data/**.yaml", "data/**"):
        with pytest.raises(ValueError, match="unsupported record glob"):
            glob_regex(pattern)


def test_annotation_coverage_distinguishes_unknown_from_no_reactions(index, sibling, spec):
    from pathwaymech.cross_mech import ScanCoverage, render_summary

    coverage = {"AntibioticMech": ScanCoverage()}
    report = build_report(index, {"AntibioticMech": scan_sibling(sibling, spec)},
                          {"P0A749": {"rhea": []}}, coverage=coverage)
    assert coverage["AntibioticMech"].distinct_accessions == 3
    assert coverage["AntibioticMech"].annotated_accessions == 1
    assert "Missing annotation entries are unknown" in render_summary(report)


def test_when_match_only_selects_the_declared_corpus():
    slot = SlotSpec("trait_relations[]", when_match={"relation_source": r"PathwayMech\b.*"})
    assert slot.selects({"relation_source": "PathwayMech abc123"})
    assert not slot.selects({"relation_source": "Complex Portal"})
    assert not slot.selects({"relation_source": "PathwayMechExtra"})


def test_stray_urls_accept_host_case_but_still_check_the_whole_path(tmp_path, index):
    from pathwaymech.cross_mech import MechSpec

    url = "HTTPS://CultureBotAI.github.io/PathwayMech/pages/records/WikiPathways_WP5060.html"
    write_yaml(tmp_path / "record.yaml", {"identifier": "x", "notes": f"{url} {url}.bak"})
    scan = scan_sibling(tmp_path, MechSpec("Mech", ["*.yaml"]))
    report = build_report(index, {"Mech": scan})
    assert [row["status"] for row in report.link_checks] == ["ok", "unknown_record"]


def test_uniprot_batches_do_not_drop_boundary_accessions():
    import urllib.parse

    accessions = ["P0A749", "P0A6B4", "P10614", "P06115", "P06169"]
    requested = []

    def fetch(url):
        query = urllib.parse.parse_qs(urllib.parse.urlsplit(url).query)["query"][0]
        batch = [value.removeprefix("accession:") for value in query.split(" OR ")]
        requested.append(batch)
        return "Entry\tRhea ID\n" + "".join(f"{value}\t\n" for value in batch)

    assert set(fetch_uniprot_annotations(accessions, fetch=fetch, batch=2)) == set(accessions)
    assert [len(batch) for batch in requested] == [2, 2, 1]


@pytest.mark.parametrize("suffix", [".bak", "/extra"])
def test_page_urls_require_the_exact_published_path(index, suffix: str) -> None:
    url = record_url(PATHWAY["id"])
    assert resolve_target(index, url + suffix) is None
    assert resolve_target(index, url.replace("WikiPathways_WP5060", "wikipathways_wp5060")) is None
    assert resolve_target(index, url + "?source=sibling#proteins") == PATHWAY["id"]
    assert resolve_target(index, "prose " + url) is None


def test_stray_urls_report_malformed_suffixes_and_trim_prose_punctuation(tmp_path: Path) -> None:
    from pathwaymech.cross_mech import MechSpec

    url = record_url(PATHWAY["id"])
    write_yaml(tmp_path / "r.yaml", {"notes": f"See ({url}). Also {url}.bak"})
    index = build_pathway_index([PATHWAY])
    scan = scan_sibling(tmp_path, MechSpec(name="X", records=["*.yaml"]))
    report = build_report(index, {"X": scan})
    assert [(row["target"], row["status"]) for row in report.link_checks] == [
        (url, "ok"), (url + ".bak", "unknown_record")]


@pytest.mark.parametrize("option", ["--sgd-map", "--annotations", "--rhea-directions"])
def test_cli_rejects_missing_explicit_json_inputs(tmp_path: Path, option: str, capsys) -> None:
    config = tmp_path / "config.yaml"
    config.write_text(SPEC_YAML, encoding="utf-8")
    missing = tmp_path / "missing.json"
    with pytest.raises(SystemExit) as error:
        main(["--config", str(config), option, str(missing)], tmp_path)
    assert error.value.code == 2
    assert str(missing) in capsys.readouterr().err


@pytest.mark.parametrize("check_links", [False, True])
def test_cli_fails_on_unreadable_sibling_records(tmp_path: Path, check_links: bool,
                                               capsys) -> None:
    config = tmp_path / "config.yaml"
    config.write_text(SPEC_YAML, encoding="utf-8")
    sibling = tmp_path / "AntibioticMech"
    write_yaml(sibling / "data" / "antibiotics" / "valid.yaml", {"identifier": "CHEBI:1"})
    (sibling / "data" / "antibiotics" / "broken.yaml").write_text("a: [", encoding="utf-8")
    args = ["--config", str(config), "--mech", f"AntibioticMech={sibling}"]
    if check_links:
        args.append("--check-links")
    assert main(args, tmp_path) == 1
    output = capsys.readouterr()
    assert "inventory is incomplete: 1 scan error(s)" in output.err
    assert "| AntibioticMech | full | incomplete | 2 | 1 | 0 | 1 | 1 |" in output.out


def test_check_links_fails_when_only_some_configured_siblings_are_available(tmp_path: Path,
                                                                          capsys) -> None:
    config = tmp_path / "config.yaml"
    data = yaml.safe_load(SPEC_YAML)
    data["mechs"]["MissingMech"] = data["mechs"]["AntibioticMech"].copy()
    write_yaml(config, data)
    write_yaml(tmp_path / "AntibioticMech" / "data" / "antibiotics" / "r.yaml",
               {"identifier": "CHEBI:1"})
    args = ["--config", str(config), "--mechs-root", str(tmp_path)]
    assert main(args, tmp_path) == 0  # An exploratory inventory can inspect a subset.
    assert main([*args, "--check-links"], tmp_path) == 1
    output = capsys.readouterr()
    assert "MissingMech | full | missing checkout" in output.out
    assert "1 required checkout(s) unavailable" in output.err
    assert main([*args, "--check-links", "--only", "AntibioticMech"], tmp_path) == 0


def test_cli_rejects_unknown_mech_override(tmp_path: Path, capsys) -> None:
    config = tmp_path / "config.yaml"
    config.write_text(SPEC_YAML, encoding="utf-8")
    with pytest.raises(SystemExit) as error:
        main(["--config", str(config), "--mech", f"TypoMech={tmp_path}"], tmp_path)
    assert error.value.code == 2
    assert "TypoMech" in capsys.readouterr().err


def test_cli_records_prefilter_coverage_in_summary_and_tsv(tmp_path: Path) -> None:
    import csv

    config = tmp_path / "config.yaml"
    data = yaml.safe_load(SPEC_YAML)
    data["mechs"]["AntibioticMech"]["prefilter"] = True
    write_yaml(config, data)
    root = tmp_path / "PathwayMech"
    write_yaml(root / "data" / "pathways" / "p.yaml", PATHWAY)
    sibling = tmp_path / "AntibioticMech"
    for name, accession in [("matched", "P0A749"), ("filtered", "Q00000")]:
        write_yaml(sibling / "data" / "antibiotics" / f"{name}.yaml", {
            "identifier": name,
            "molecular_targets": [{"protein_examples": [{"uniprot_id": accession}]}],
        })
    out = tmp_path / "report"
    assert main(["--config", str(config), "--mech", f"AntibioticMech={sibling}",
                 "--out", str(out)], root) == 0
    summary = (out / "summary.md").read_text(encoding="utf-8")
    assert "not a complete sibling protein inventory" in summary
    assert "reaction-only matches" in summary
    assert "| AntibioticMech | accession-prefiltered | complete | 2 | 1 | 1 | 0 | 0 |" in summary
    with (out / "coverage.tsv").open(encoding="utf-8", newline="") as stream:
        row, = csv.DictReader(stream, delimiter="\t")
    assert row["scope"] == "accession-prefiltered"
    assert (row["files_seen"], row["files_parsed"], row["files_filtered"]) == ("2", "1", "1")

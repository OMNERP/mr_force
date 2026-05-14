from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def _load_fixture(name: str) -> list[dict]:
    return json.loads((ROOT / "mr_force" / "fixtures" / name).read_text())


def test_dashboard_chart_fixtures_have_valid_filters_json():
    for chart in _load_fixture("dashboard_chart.json"):
        assert chart.get("filters_json") is not None, chart.get("name")
        assert isinstance(json.loads(chart["filters_json"]), list), chart.get("name")


def test_number_card_fixtures_have_valid_filters_json():
    for card in _load_fixture("number_card.json"):
        assert card.get("filters_json") is not None, card.get("name")
        assert isinstance(json.loads(card["filters_json"]), list), card.get("name")


def test_all_fixture_documents_have_names():
    for fixture in (ROOT / "mr_force" / "fixtures").glob("*.json"):
        docs = json.loads(fixture.read_text())
        for index, doc in enumerate(docs if isinstance(docs, list) else [docs]):
            assert doc.get("name"), f"{fixture}:{index} is missing name"


def test_asset_bundle_entrypoints_exist():
    assert (ROOT / "mr_force" / "public" / "js" / "mr_force.bundle.js").is_file()
    assert (ROOT / "mr_force" / "public" / "css" / "mr_force.bundle.css").is_file()


def test_asset_bundles_are_self_contained():
    css_bundle = (ROOT / "mr_force" / "public" / "css" / "mr_force.bundle.css").read_text()
    js_bundle = (ROOT / "mr_force" / "public" / "js" / "mr_force.bundle.js").read_text()
    assert "@import" not in css_bundle
    assert 'import "./' not in js_bundle
    assert "mr_force.capture_location" in js_bundle


def test_workspace_content_references_existing_widgets():
    workspace = json.loads(
        (ROOT / "mr_force" / "mr_force" / "workspace" / "mr_force" / "mr_force.json").read_text()
    )
    content = json.loads(workspace["content"])
    shortcut_names = {row["label"] for row in workspace["shortcuts"]}
    card_names = {row["label"] for row in workspace["links"] if row.get("type") == "Card Break"}
    chart_names = {row["chart_name"] for row in workspace["charts"]}
    number_card_names = {row["number_card_name"] for row in workspace["number_cards"]}

    assert any(block["type"] == "shortcut" for block in content)
    assert any(block["type"] == "card" for block in content)
    assert any(block["type"] == "chart" for block in content)
    assert any(block["type"] == "number_card" for block in content)

    for block in content:
        data = block.get("data", {})
        if block["type"] == "shortcut":
            assert data["shortcut_name"] in shortcut_names
        elif block["type"] == "card":
            assert data["card_name"] in card_names
        elif block["type"] == "chart":
            assert data["chart_name"] in chart_names
        elif block["type"] == "number_card":
            assert data["number_card_name"] in number_card_names

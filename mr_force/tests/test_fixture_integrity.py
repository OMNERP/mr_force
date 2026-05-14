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

import frappe


def test_territory_coverage_meta_loads():
    assert frappe.get_meta("Territory Coverage")

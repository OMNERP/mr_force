import frappe


def test_geo_checkin_meta_loads():
    assert frappe.get_meta("Geo Checkin")

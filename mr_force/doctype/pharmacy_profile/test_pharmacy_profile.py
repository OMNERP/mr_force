import frappe


def test_pharmacy_profile_meta_loads():
    assert frappe.get_meta("Pharmacy Profile")

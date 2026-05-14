import frappe


def test_medical_representative_meta_loads():
    assert frappe.get_meta("Medical Representative")

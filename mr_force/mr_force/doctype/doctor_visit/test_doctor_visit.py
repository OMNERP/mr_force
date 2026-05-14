import frappe


def test_doctor_visit_meta_loads():
    assert frappe.get_meta("Doctor Visit")

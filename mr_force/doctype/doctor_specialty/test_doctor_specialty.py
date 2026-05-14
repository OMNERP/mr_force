import frappe


def test_doctor_specialty_meta_loads():
    assert frappe.get_meta("Doctor Specialty")

import frappe


def test_doctor_profile_meta_loads():
    assert frappe.get_meta("Doctor Profile")

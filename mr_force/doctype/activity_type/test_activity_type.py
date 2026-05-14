import frappe


def test_activity_type_meta_loads():
    assert frappe.get_meta("Activity Type")

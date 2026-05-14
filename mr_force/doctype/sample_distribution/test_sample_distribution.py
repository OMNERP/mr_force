import frappe


def test_sample_distribution_meta_loads():
    assert frappe.get_meta("Sample Distribution")

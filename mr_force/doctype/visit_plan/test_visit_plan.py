import frappe


def test_visit_plan_meta_loads():
    assert frappe.get_meta("Visit Plan")

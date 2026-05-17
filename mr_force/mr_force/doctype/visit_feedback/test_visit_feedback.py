import frappe


def test_visit_feedback_meta_loads():
    assert frappe.get_meta("Visit Feedback")

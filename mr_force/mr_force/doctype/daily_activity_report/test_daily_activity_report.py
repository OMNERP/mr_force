import frappe


def test_daily_activity_report_meta_loads():
    assert frappe.get_meta("Daily Activity Report")

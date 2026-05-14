import frappe


def test_kpi_target_meta_loads():
    assert frappe.get_meta("KPI Target")

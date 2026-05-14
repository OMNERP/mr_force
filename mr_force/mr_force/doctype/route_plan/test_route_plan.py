import frappe


def test_route_plan_meta_loads():
    assert frappe.get_meta("Route Plan")

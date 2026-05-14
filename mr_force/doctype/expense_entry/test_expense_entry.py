import frappe


def test_expense_entry_meta_loads():
    assert frappe.get_meta("Expense Entry")

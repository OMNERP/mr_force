import frappe


def test_field_notification_log_meta_loads():
    assert frappe.get_meta("Field Notification Log")

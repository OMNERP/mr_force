from __future__ import annotations

import frappe
from frappe.utils import add_days, getdate, nowdate


def create_follow_up_notifications() -> None:
    tomorrow = add_days(nowdate(), 1)
    visits = frappe.get_all(
        "Doctor Visit",
        filters={"next_follow_up_date": tomorrow, "status": ["!=", "Cancelled"]},
        fields=["name", "medical_representative", "doctor", "next_follow_up_date"],
    )
    for visit in visits:
        title = f"Follow up due for {visit.doctor}"
        if not frappe.db.exists("Field Notification Log", {"reference_doctype": "Doctor Visit", "reference_name": visit.name, "title": title}):
            doc = frappe.new_doc("Field Notification Log")
            doc.title = title
            doc.notification_type = "Follow Up"
            doc.reference_doctype = "Doctor Visit"
            doc.reference_name = visit.name
            doc.assigned_to = visit.medical_representative
            doc.due_date = visit.next_follow_up_date
            doc.status = "Open"
            doc.insert(ignore_permissions=True)


def refresh_daily_kpi_snapshots() -> None:
    # Reserved for future materialized KPI snapshots; current dashboards query live operational data.
    frappe.cache().hset("mr_force:last_kpi_refresh", "date", str(getdate(nowdate())))

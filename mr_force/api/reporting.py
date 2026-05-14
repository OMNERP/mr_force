from __future__ import annotations

import frappe
from frappe.utils import nowdate
from mr_force.utils.security import require_mr_force_user


@frappe.whitelist(methods=["GET"])
def dashboard_kpis() -> dict:
    require_mr_force_user()
    today = nowdate()
    total_visits = frappe.db.count("Doctor Visit")
    today_visits = frappe.db.count("Doctor Visit", {"visit_date": today})
    pending_visits = frappe.db.count("Doctor Visit", {"status": ["in", ["Planned", "In Progress"]]})
    active_doctors = frappe.db.count("Doctor Profile", {"status": "Active"})
    active_pharmacies = frappe.db.count("Pharmacy Profile", {"status": "Active"})
    return {
        "total_visits": total_visits,
        "today_visits": today_visits,
        "pending_visits": pending_visits,
        "active_doctors": active_doctors,
        "active_pharmacies": active_pharmacies,
    }


@frappe.whitelist(methods=["POST"])
def submit_daily_activity_report(report_name: str) -> str:
    require_mr_force_user()
    doc = frappe.get_doc("Daily Activity Report", report_name)
    doc.submit()
    return doc.name

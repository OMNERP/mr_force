from __future__ import annotations

import frappe
from mr_force.utils.security import require_mr_force_user


@frappe.whitelist(methods=["POST"])
def log_visit(doctor: str, medical_representative: str, visit_datetime: str, latitude: float | None = None, longitude: float | None = None, notes: str | None = None) -> str:
    require_mr_force_user()
    doc = frappe.new_doc("Doctor Visit")
    doc.doctor = doctor
    doc.medical_representative = medical_representative
    doc.visit_datetime = visit_datetime
    doc.latitude = latitude
    doc.longitude = longitude
    doc.notes = notes
    doc.status = "Completed"
    doc.insert()
    return doc.name


@frappe.whitelist(methods=["GET"])
def upcoming_visits(medical_representative: str | None = None) -> list[dict]:
    require_mr_force_user()
    filters = {"status": ["in", ["Planned", "In Progress"]]}
    if medical_representative:
        filters["medical_representative"] = medical_representative
    return frappe.get_all("Doctor Visit", filters=filters, fields=["name", "doctor", "medical_representative", "visit_datetime", "status"], order_by="visit_datetime asc", limit_page_length=100)

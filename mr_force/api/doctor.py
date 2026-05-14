from __future__ import annotations

import frappe
from frappe import _
from mr_force.utils.security import require_mr_force_user


@frappe.whitelist(methods=["GET"])
def list_doctors(territory: str | None = None, specialty: str | None = None) -> list[dict]:
    require_mr_force_user()
    filters = {}
    if territory:
        filters["territory"] = territory
    if specialty:
        filters["specialty"] = specialty
    return frappe.get_all("Doctor Profile", filters=filters, fields=["name", "doctor_name", "specialty", "territory", "mobile_no", "status"], order_by="doctor_name asc")


@frappe.whitelist(methods=["POST"])
def create_doctor(doctor_name: str, specialty: str | None = None, territory: str | None = None, mobile_no: str | None = None) -> str:
    require_mr_force_user()
    doc = frappe.new_doc("Doctor Profile")
    doc.doctor_name = doctor_name
    doc.specialty = specialty
    doc.territory = territory
    doc.mobile_no = mobile_no
    doc.status = "Active"
    doc.insert()
    return doc.name

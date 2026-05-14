from __future__ import annotations

import frappe
from frappe import _

MANAGER_ROLE = "MR Force Manager"
REP_ROLE = "Medical Representative"


def require_mr_force_user() -> None:
    if frappe.session.user == "Guest":
        frappe.throw(_("Authentication required"), frappe.PermissionError)
    if MANAGER_ROLE not in frappe.get_roles() and REP_ROLE not in frappe.get_roles() and "System Manager" not in frappe.get_roles():
        frappe.throw(_("You are not permitted to access MR Force data"), frappe.PermissionError)

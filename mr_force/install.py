from __future__ import annotations

import frappe


def after_install() -> None:
    """Seed the small amount of data required for a first usable login."""
    ensure_roles()
    ensure_seed_records()
    ensure_workspace_visible()


def after_migrate() -> None:
    """Keep navigation visible after migrations, fixture import, and upgrades."""
    ensure_roles()
    ensure_seed_records()
    ensure_workspace_visible()


def before_uninstall() -> None:
    """No destructive cleanup is needed; user data remains under normal Frappe uninstall flow."""
    return None


def ensure_roles() -> None:
    for role in ("MR Force Manager", "Medical Representative"):
        if not frappe.db.exists("Role", role):
            doc = frappe.new_doc("Role")
            doc.role_name = role
            doc.desk_access = 1
            doc.insert(ignore_permissions=True)


def ensure_seed_records() -> None:
    seeds = {
        "Activity Type": ["Doctor Call", "Pharmacy Call", "Sample Drop", "CME Follow-up", "Admin Work"],
        "Doctor Specialty": ["General Practice", "Cardiology", "Dermatology", "Pediatrics", "Internal Medicine"],
    }
    for doctype, names in seeds.items():
        for name in names:
            if not frappe.db.exists(doctype, name):
                doc = frappe.new_doc(doctype)
                field = "activity_type" if doctype == "Activity Type" else "specialty"
                setattr(doc, field, name)
                doc.insert(ignore_permissions=True)


def ensure_workspace_visible() -> None:
    if frappe.db.exists("Workspace", "MR Force"):
        frappe.db.set_value("Workspace", "MR Force", {"public": 1, "is_hidden": 0})

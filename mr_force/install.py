from __future__ import annotations

import json

import frappe


MR_FORCE_STANDARD_DOCTYPES = (
    "Activity Type",
    "Daily Activity Report",
    "Doctor Profile",
    "Doctor Specialty",
    "Doctor Visit",
    "Expense Entry",
    "Field Notification Log",
    "Geo Checkin",
    "KPI Target",
    "Medical Representative",
    "Pharmacy Profile",
    "Route Plan",
    "Sample Distribution",
    "Territory Coverage",
    "Visit Feedback",
    "Visit Plan",
    "Visit Plan Item",
)


def after_install() -> None:
    """Seed the small amount of data required for a first usable login."""
    repair_doctype_modules()
    ensure_roles()
    ensure_seed_records()
    ensure_dashboard_filters()
    ensure_workspace_layout()


def before_migrate() -> None:
    """Repair module ownership before Frappe loads standard DocType controllers."""
    repair_doctype_modules()


def after_migrate() -> None:
    """Keep navigation visible after migrations, fixture import, and upgrades."""
    repair_doctype_modules()
    ensure_roles()
    ensure_seed_records()
    ensure_dashboard_filters()
    ensure_workspace_layout()


def before_uninstall() -> None:
    """No destructive cleanup is needed; user data remains under normal Frappe uninstall flow."""
    return None


def repair_doctype_modules() -> None:
    """Keep MR Force DocTypes mapped to their standard module.

    A previous malformed scaffold placed standard DocType controllers outside
    the Frappe module package. Some failed installs can leave DocType rows
    with the fallback Core module, which makes Frappe import paths such as
    frappe.core.doctype.doctor_specialty.doctor_specialty. Use direct SQL so
    the repair does not need to load the broken DocType metadata first.
    """
    if not frappe.db.table_exists("DocType"):
        return

    frappe.db.sql(
        """
        update `tabDocType`
           set module = 'MR Force'
         where name in %(doctypes)s
           and ifnull(module, '') != 'MR Force'
        """,
        {"doctypes": MR_FORCE_STANDARD_DOCTYPES},
    )
    for doctype in MR_FORCE_STANDARD_DOCTYPES:
        frappe.clear_cache(doctype=doctype)


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


def ensure_dashboard_filters() -> None:
    if not frappe.db.table_exists("Number Card"):
        return

    today_visit_filter = json.dumps([["Doctor Visit", "visit_date", "Timespan", "today", False]], separators=(",", ":"))
    if frappe.db.exists("Number Card", "Today Visits"):
        frappe.db.set_value("Number Card", "Today Visits", "filters_json", today_visit_filter)
        frappe.clear_cache(doctype="Number Card")



def ensure_workspace_layout() -> None:
    if not frappe.db.table_exists("Workspace") or not frappe.db.exists("Workspace", "MR Force"):
        return

    with open(frappe.get_app_path("mr_force", "mr_force", "workspace", "mr_force", "mr_force.json")) as workspace_file:
        workspace = json.load(workspace_file)

    frappe.db.set_value(
        "Workspace",
        "MR Force",
        {
            "public": 1,
            "is_hidden": 0,
            "content": workspace["content"],
        },
    )
    frappe.clear_cache(doctype="Workspace")

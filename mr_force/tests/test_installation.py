import frappe


def test_workspace_exists():
    assert frappe.db.exists("Workspace", "MR Force")


def test_dashboard_kpis_api():
    from mr_force.api.reporting import dashboard_kpis
    assert isinstance(dashboard_kpis(), dict)


def test_core_doctypes_load():
    for doctype in ["Medical Representative", "Doctor Profile", "Doctor Visit", "Daily Activity Report"]:
        assert frappe.get_meta(doctype)


def test_standard_doctype_controllers_use_mr_force_module_path():
    from importlib import import_module

    for doctype in ["Doctor Specialty", "Doctor Visit", "Medical Representative"]:
        module = frappe.scrub(doctype)
        import_module(f"mr_force.mr_force.doctype.{module}.{module}")

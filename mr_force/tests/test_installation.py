import frappe


def test_workspace_exists():
    assert frappe.db.exists("Workspace", "MR Force")


def test_dashboard_kpis_api():
    from mr_force.api.reporting import dashboard_kpis
    assert isinstance(dashboard_kpis(), dict)


def test_core_doctypes_load():
    for doctype in ["Medical Representative", "Doctor Profile", "Doctor Visit", "Daily Activity Report"]:
        assert frappe.get_meta(doctype)

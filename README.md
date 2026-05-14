# MR Force

MR Force is a standalone Frappe v15 CRM and field-service app for pharmaceutical medical representative operations.

## Install

```bash
bench get-app <repo-url>
bench --site <site> install-app mr_force
bench --site <site> migrate
bench build
bench restart
bench --site <site> clear-cache
```

After installation, open Desk and select the public **MR Force** workspace.

## Verification

```bash
bench --site <site> execute mr_force.api.reporting.dashboard_kpis
bench --site <site> list-apps
bench --site <site> migrate
```

## Frappe module layout

The app uses the standard Frappe module import path `mr_force.mr_force`. Standard DocType controllers live under `mr_force/mr_force/doctype/<doctype>/<doctype>.py`, so Frappe imports `Doctor Specialty` from `mr_force.mr_force.doctype.doctor_specialty.doctor_specialty` instead of falling back to `frappe.core`.

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

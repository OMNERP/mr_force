app_name = "mr_force"
app_title = "MR Force"
app_publisher = "MR Force"
app_description = "CRM and field service operations for pharmaceutical medical representatives"
app_email = "support@example.com"
app_license = "MIT"
app_logo_url = "/assets/mr_force/icons/mr-force.svg"
app_home = "/app/mr-force"

required_apps = ["frappe"]

app_include_css = ["/assets/mr_force/css/mr_force.css"]
app_include_js = ["/assets/mr_force/js/mr_force.js"]

doctype_js = {
    "Doctor Visit": "public/js/doctor_visit.js",
    "Geo Checkin": "public/js/geo_checkin.js",
}

doctype_calendar_js = {
    "Doctor Visit": "public/js/doctor_visit_calendar.js",
    "Visit Plan": "public/js/visit_plan_calendar.js",
}

after_install = "mr_force.install.after_install"
before_migrate = "mr_force.install.before_migrate"
after_migrate = "mr_force.install.after_migrate"
before_uninstall = "mr_force.install.before_uninstall"

scheduler_events = {
    "daily": [
        "mr_force.tasks.daily.create_follow_up_notifications",
        "mr_force.tasks.daily.refresh_daily_kpi_snapshots",
    ]
}

fixtures = [
    {"dt": "Role", "filters": [["role_name", "in", ["MR Force Manager", "Medical Representative"]]]},
    {"dt": "Workspace", "filters": [["name", "=", "MR Force"]]},
    {"dt": "Number Card", "filters": [["module", "=", "MR Force"]]},
    {"dt": "Dashboard Chart", "filters": [["module", "=", "MR Force"]]},
    {"dt": "Report", "filters": [["module", "=", "MR Force"]]},
    {"dt": "Onboarding Step", "filters": [["name", "like", "MR Force%"]]},
    {"dt": "Onboarding", "filters": [["name", "=", "MR Force Onboarding"]]},
]

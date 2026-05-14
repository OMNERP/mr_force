frappe.views.calendar["Doctor Visit"] = {
  field_map: { start: "visit_datetime", end: "visit_datetime", id: "name", title: "doctor", status: "status" },
  get_events_method: "frappe.desk.calendar.get_events"
};

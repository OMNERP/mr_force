frappe.views.calendar["Visit Plan"] = {
  field_map: { start: "plan_date", end: "plan_date", id: "name", title: "medical_representative", status: "status" },
  get_events_method: "frappe.desk.calendar.get_events"
};

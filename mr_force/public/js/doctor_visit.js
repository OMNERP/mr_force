frappe.ui.form.on("Doctor Visit", {
  refresh(frm) {
    if (!frm.is_new()) return;
    frm.add_custom_button(__("Capture Location"), () => {
      mr_force.capture_location((coords) => {
        frm.set_value("latitude", coords.latitude);
        frm.set_value("longitude", coords.longitude);
      });
    });
  }
});

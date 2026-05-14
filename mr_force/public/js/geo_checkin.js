frappe.ui.form.on("Geo Checkin", {
  refresh(frm) {
    frm.add_custom_button(__("Capture GPS"), () => {
      mr_force.capture_location((coords) => {
        frm.set_value("latitude", coords.latitude);
        frm.set_value("longitude", coords.longitude);
        frm.set_value("accuracy_meters", coords.accuracy);
      });
    });
  }
});

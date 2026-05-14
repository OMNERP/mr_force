frappe.provide("mr_force");
mr_force.capture_location = function(callback) {
  if (!navigator.geolocation) {
    frappe.msgprint(__("Location capture is not supported on this device."));
    return;
  }
  navigator.geolocation.getCurrentPosition(
    (position) => callback && callback(position.coords),
    () => frappe.msgprint(__("Unable to capture location. Please check browser permissions.")),
    { enableHighAccuracy: true, timeout: 10000, maximumAge: 60000 }
  );
};

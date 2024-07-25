$(document).on("page-change", function () {
  setupPage();
});

function setupPage() {
  console.log("Page setup code running");
  var currentRoute = frappe.get_route();
  var company = frappe.defaults.get_user_defaults("company")[0];
  debugger;

  if (
    currentRoute != null &&
    currentRoute[0] === "List" &&
    currentRoute[2] === "List"
  ) {
    if (!frappe.route_options || frappe.route_options.company !== company) {
      frappe.route_options = { company: company };
      frappe.set_route("List", currentRoute[1]);
    }
  }
}

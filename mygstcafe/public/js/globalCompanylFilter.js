$(document).ready(function () {
  setupPage();
});

function setupPage() {
  var defaultCompany = frappe.defaults.get_user_defaults("company")[0];
  frappe.route_options.company = defaultCompany;
  
}

$(document).on("page-change", function () {
  setTimeout(function () {
    $('[data-fieldname="company"] input').hide();
  }, 500);
  var defaultCompany = frappe.defaults.get_user_defaults("company")[0];
  // if(frappe.route_options.company !== defaultCompany){
  //   location.reload()
  // }
});

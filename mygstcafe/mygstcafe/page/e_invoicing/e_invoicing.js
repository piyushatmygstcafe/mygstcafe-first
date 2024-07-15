frappe.pages["e-invoicing"].on_page_load = function (wrapper) {
  var page = frappe.ui.make_app_page({
    parent: wrapper,
    title: "e-invoicing",
    single_column: true,
  });
  $(frappe.render_template("e_invoicing", {})).appendTo(page.main);

  frappe.call({
    method: "mygstcafe.api.get_sales_data",
    callback: function (r) {
      if (r.message) {
        $("#data-container").html(r.message);
      }
    },
  });
};

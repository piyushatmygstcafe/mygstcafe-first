// custom_app/public/js/global_filters.js

frappe.ui.form.on("*", {
  onload: function (frm) {
    // Get the default company
    frappe.call({
      method: "mygstcafe.mygstcafe.utils.get_default_company",
      callback: function (response) {
        var default_company = response.message;

        if (frm.fields_dict["company"]) {
          frm.set_query("company", function () {
            return {
              filters: [["Company", "name", "=", default_company]],
            };
          });
        }
      },
    });
  },
});

frappe.listview_settings["*"] = {
  onload: function (listview) {
    frappe.call({
      method: "mygstcafe.mygstcafe.utils.get_default_company",
      callback: function (response) {
        var default_company = response.message;
        listview.page.add_filter("company", default_company);
      },
    });
  },
};

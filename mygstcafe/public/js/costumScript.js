frappe.ui.form.on("Item", {
  refresh: function (frm) {},

  before_save: function (frm) {
    if (frm.doc.item_defaults && frm.doc.item_defaults.length > 0) {
      return;
    }
    frappe.call({
      method: "mygstcafe.api.get_item_defaults",
      callback: function (res) {
        console.log(res);
        defaults = res.message;
        console.log(defaults);
        let row = frm.add_child("item_defaults", {
          company: defaults,
        });
        frm.refresh_field("item_defaults");
      },
    });
  },
});

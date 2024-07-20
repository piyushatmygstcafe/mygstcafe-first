frappe.pages["set-defaults"].on_page_load = function (wrapper) {
  var page = frappe.ui.make_app_page({
    parent: wrapper,
    title: "",
    single_column: true,
  });

  $(`
    <div style="display: flex; height: 200px; justify-content: center; align-items: center;">
      <div id="company-selection-container" style="display: flex; flex-direction: column; gap:10px;  align-items: center;">
        <label for="company" style="margin-right: 10px; font-weight: bold;">Select your Company</label>
        <select id="company-select" style="flex: 1; margin-right: 10px; padding: 5px; border: 1px solid #d1d8dd; border-radius: 4px;"></select>
        <button id="change-company" class="btn btn-primary" style="padding: 5px 10px;">Proceed</button>
      </div>
    </div>
  `).appendTo(page.main);

  // $(".navbar").addClass("hidden");

  // Function to change the company
  function changeCompany() {
    var selectedCompany = $("#company-select").val();
    frappe.call({
      method: "mygstcafe.api.change_default_company",
      args: {
        company_name: selectedCompany,
      },
      callback: function (res) {
        if (res.message) {
          if (res.message.error) {
            frappe.msgprint({
              title: __("Error"),
              message: __("Error: {0}"[res.error]),
              indicator: "red",
            });
          } else {
            // $(".navbar").removeClass("hidden");
            frappe.set_route("/app/home");
            location.reload();
          }
        }
      },
    });
  }

  // Bind the click event to the change button
  $("#change-company").on("click", changeCompany);

  // Fetch default company and list of companies
  frappe.call({
    method: "mygstcafe.api.get_default_company_and_list",
    callback: function (res) {
      if (res.message) {
        var data = res.message;
        var defaultCompany = data.default_company;
        var companies = data.companies;

        var companySelect = $("#company-select");
        companies.forEach(function (company) {
          companySelect.append(
            `<option value="${company.name}">${company.company_name}</option>`
          );
        });

        // If there is a default company, select it
        if (defaultCompany) {
          companySelect.val(defaultCompany);
        }

        $("#company-selection-container").show();
      }
    },
  });
};

// Copyright (c) 2024, Pinnacle Finserv Advisors Private Limited and contributors
// For license information, please see license.txt

// function to enable or diable a docfield where
// dDf = dipendend field
// cDf = want to change field
function toggleEnable(frm, dDf, cDf) {
  if (frm.doc[dDf]) {
    frm.toggle_enable(cDf, true);
  } else {
    frm.toggle_enable(cDf, false);
  }
}

function getFormattedDate() {
  const today = new Date();

  let day = today.getDate();

  let month = today.getMonth() + 1;

  let year = today.getFullYear();

  if (day < 10) {
    day = "0" + day;
  }
  if (month < 10) {
    month = "0" + month;
  }

  const formattedDate = day + "-" + month + "-" + year;

  return formattedDate;
}

frappe.ui.form.on("API Credentials", {
  refresh(frm) {
    $(
      'div[data-fieldname="mygstcafe_account_credential_section"],div[data-fieldname="e_invoicee_way_portal_credentials_section"],div[data-fieldname="enable_eway_section"],div[data-fieldname="eway_bill_sec_1"],div[data-fieldname="eway_bill_sec_2"]'
    ).css({
      border: "none",
      padding: "10px",
    });
    $(
      'div[data-fieldname="mygstcafe_account_credential_section"],div[data-fieldname="e_invoicee_way_portal_credentials_section"]'
    )
      .find(".section-head")
      .css({
        "font-weight": 350,
        "font-family": "Open Sans, sans-serif !important",
      });
    $(
      'div[data-fieldname="mygstcafe_account_credential_section"],div[data-fieldname="e_invoicee_way_portal_credentials_section"]'
    )
      .find("label")
      .css({
        "font-family": "Open Sans, sans-serif !important",
        "font-size": "14px !important",
      });

    frm.toggle_enable("application_from", false);
    
  },

  customer_id: function (frm) {
    if (frm.doc.customer_id) {
      frm.set_df_property("api_id", "reqd", 1);
    } else {
      frm.set_df_property("api_id", "reqd", 0);
    }
    // toggleEnable(frm, "customer_id", "api_id");
  },
  api_id: function (frm) {
    if (frm.doc.api_id) {
      frm.set_df_property("api_secret", "reqd", 1);
    } else {
      frm.set_df_property("api_secret", "reqd", 0);
    }
    // toggleEnable(frm, "api_id", "api_secret");
  },
  enable_eway: function (frm) {
    // if (frm.doc.enable_eway) {
    //     frm.toggle_enable('api_user_id',false)
    // } else(
    //     frm.toggle_enable('api_user_id',true)
    // )
    toggleEnable(frm, "enable_eway", [
      "application_from",
      "threshold_limit",
      "threshold_limit_includes",
      "applicable_for_intrastate",
    ]);
    
    // css using jquerry for removing section break linings eway_bill_sec_1

    // $(
    //   'div[data-fieldname="eway_bill_sec_1"], div[data-fieldname="enable_eway_section"]"]'
    // ).css({
    //   border: "none",
    //   padding: "10px",
    // });
  },
});

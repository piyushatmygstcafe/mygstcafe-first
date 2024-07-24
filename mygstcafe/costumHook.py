import frappe
from erpnext.stock.doctype.item.item import Item

def before_save(doc, method):
    pass
    # frappe.logger().info("After save method triggered")
    
    # if doc.item_defaults or not doc.item_group:
    #     frappe.logger().info("No item defaults or no item group")
    #     return

    # item_defaults = frappe.db.get_values(
    #     "Item Default",
    #     {"parent": doc.item_group},
    #     [
    #         "company",
    #         "default_warehouse",
    #         "default_price_list",
    #         "buying_cost_center",
    #         "default_supplier",
    #         "expense_account",
    #         "selling_cost_center",
    #         "income_account",
    #     ],
    #     as_dict=1,
    # )
    
    # if item_defaults:
    #     for item in item_defaults:
    #         doc.append(
    #             "item_defaults",
    #             {
    #                 "company": item["company"],
    #                 "default_warehouse": item["default_warehouse"],
    #                 "default_price_list": item["default_price_list"],
    #                 "buying_cost_center": item["buying_cost_center"],
    #                 "default_supplier": item["default_supplier"],
    #                 "expense_account": item["expense_account"],
    #                 "selling_cost_center": item["selling_cost_center"],
    #                 "income_account": item["income_account"],
    #             },
    #         )
    # else:
    #     defaults = frappe.defaults.get_defaults() or {}
    #     frappe.logger().info(f"Global defaults fetched: {defaults}")

    #     if (
    #         defaults.get("default_warehouse")
    #         and defaults.get("company")
    #         and frappe.db.exists(
    #             "Warehouse", {"name": defaults.get("default_warehouse"), "company": defaults.get("company")}
    #         )
    #     ):
    #         doc.append(
    #             "item_defaults",
    #             {"company": defaults.get("company"), "default_warehouse": defaults.get("default_warehouse")},
    #         )

    # doc.save()  # Save the doc to apply the changes
    # frappe.logger().info("Document saved with updated item defaults")

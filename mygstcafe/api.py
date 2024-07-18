import frappe
from frappe.utils import get_url

@frappe.whitelist(allow_guest=True)
def get_sales_data():
    data = frappe.db.sql("""
                         
                         SELECT * FROM `tabSales Invoice`
                         
                         """,as_dict=True)
    
    return frappe.render_template("mygstcafe/templates/includes/e_invoicing.html", {"data": data})

@frappe.whitelist(allow_guest=True)
def get_sale_invoice(id):
    invoice = frappe.get_doc('Sales Invoice', id)
    invoice_dict = invoice.as_dict()
    return invoice_dict

@frappe.whitelist(allow_guest=True)
def resume_default_settings():
    frappe.db.sql("""
                DELETE FROM `tabSingles` WHERE `doctype` = 'Default Setting'
                """)
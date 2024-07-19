import frappe
import frappe.defaults
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
def get_default_company_and_list():
    user = frappe.session.user
    
    default_company = frappe.db.get_value("DefaultValue", {"parent": user, "defkey": "company"}, "defvalue")
    
    companies = frappe.get_all("Company", fields=["name", "company_name"])
    
    return {
        "default_company": default_company,
        "companies": companies
    }
    
@frappe.whitelist(allow_guest=True)
def change_default_company(company_name):
    try:
        frappe.defaults.set_user_default("company", company_name)
        
        return { "message": "Default company set successfully."}
    except Exception as e:
      
        return {"error": str(e)}

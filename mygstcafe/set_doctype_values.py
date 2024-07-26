import frappe
from erpnext.selling.doctype.customer.customer import Customer
from erpnext.buying.doctype.supplier.supplier import Supplier
from erpnext.stock.doctype.item.item import Item

def before_save(doc, method):
    user = frappe.session.user
    default_company = frappe.db.get_value("DefaultValue", {"parent": user, "defkey": "company"}, "defvalue")
    
    if doc.doctype == "Customer":
        field_name = "credit_limits"
    elif doc.doctype == "Supplier":
        field_name = "accounts"
    elif doc.doctype == "Item":
        field_name = "item_defaults"
    else:
        return
    
    if getattr(doc, field_name) and len(getattr(doc, field_name)) > 0:
       return
        
    doc.append(field_name, {
        'company': default_company,
    })
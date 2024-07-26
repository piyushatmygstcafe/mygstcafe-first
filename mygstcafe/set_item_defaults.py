import frappe
from erpnext.stock.doctype.item.item import Item

def before_save(doc, method):

    user = frappe.session.user
    
    default_company = frappe.db.get_value("DefaultValue", {"parent": user, "defkey": "company"}, "defvalue")
    warehouse = frappe.db.get_value('Warehouse', {'company': default_company}, 'name')
    
    # chek if table exist and have some values
    if doc.item_defaults and len(doc.item_defaults) > 0:
       return
    
    # if item defaults table has no values then it will set values
    doc.append('item_defaults', {
    'company': default_company,
   })



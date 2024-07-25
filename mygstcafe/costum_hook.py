import frappe
from erpnext.stock.doctype.item.item import Item

def after_save(doc, method):
   frappe.msgprint("Working!")
import frappe


def get_custom_filters():
    
    user = frappe.session.user
    
    default_company = frappe.db.get_value("DefaultValue", {"parent": user, "defkey": "company"}, "defvalue")
    
    filters = {
        'company': default_company
    }
    return filters

def extend_sales_invoice_filters():
    custom_filters = get_custom_filters()
    invoices = frappe.get_list('Sales Invoice', filters=custom_filters, fields=['name', 'customer', 'posting_date'])
    return invoices

import frappe

def get_default_company():
    user = frappe.session.user
    
    default_company = frappe.db.get_value("DefaultValue", {"parent": user, "defkey": "company"}, "defvalue")
    return default_company

def apply_default_company_filter(doctype, filters=None, *args, **kwargs):
    if not filters:
        filters = {}

    # Apply default company filter if the doctypes include 'company' field
    if 'company' in frappe.get_meta(doctype).get_fieldnames():
        user = frappe.session.user
    
        default_company = frappe.db.get_value("DefaultValue", {"parent": user, "defkey": "company"}, "defvalue")
        # default_company = get_default_company()
        filters['company'] = default_company

    return filters
# my_custom_app/my_custom_app/auth_override.py

import frappe
from frappe.auth import LoginManager
from frappe.website.utils import get_home_page

# Store the original set_user_info method
original_set_user_info = LoginManager.set_user_info

def custom_set_user_info(self, resume=False):
    # set sid again
    frappe.local.cookie_manager.init_cookies()

    self.full_name = " ".join(filter(None, [self.info.first_name, self.info.last_name]))

    if self.info.user_type == "Website User":
        frappe.local.cookie_manager.set_cookie("system_user", "no")
        if not resume:
            frappe.local.response["message"] = "No App"
            frappe.local.response["home_page"] = "/" + get_home_page()
    else:
        frappe.local.cookie_manager.set_cookie("system_user", "yes")
        if not resume:
            frappe.local.response["message"] = "Logged In"
            frappe.local.response["home_page"] = "/app/set-defaults" 

    if not resume:
        frappe.response["full_name"] = self.full_name

    # redirect information
    redirect_to = frappe.cache.hget("redirect_after_login", self.user)
    if redirect_to:
        frappe.local.response["redirect_to"] = redirect_to
        frappe.cache.hdel("redirect_after_login", self.user)

    frappe.local.cookie_manager.set_cookie("full_name", self.full_name)
    frappe.local.cookie_manager.set_cookie("user_id", self.user)
    frappe.local.cookie_manager.set_cookie("user_image", self.info.user_image or "")

# Override the original set_user_info method with the custom method
LoginManager.set_user_info = custom_set_user_info

app_name = "mygstcafe"
app_title = "MYGSTCAFE"
app_publisher = "Pinnacle Finserv Advisors Private Limited"
app_description = "An app to manage GST"
app_email = "pinnacle@gmail.com"
app_license = "mit"

import mygstcafe.override_auth

# on_logout = "mygstcafe.api.resume_default_settings"

# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/mygstcafe/css/mygstcafe.css"

app_include_js = [
    "assets/mygstcafe/js/globaCompanylFilter.js"
]

# include js, css files in header of web template
# web_include_css = "/assets/mygstcafe/css/mygstcafe.css"
# web_include_js = "/assets/mygstcafe/js/mygstcafe.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "mygstcafe/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "mygstcafe/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "mygstcafe.utils.jinja_methods",
# 	"filters": "mygstcafe.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "mygstcafe.install.before_install"
# after_install = "mygstcafe.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "mygstcafe.uninstall.before_uninstall"
# after_uninstall = "mygstcafe.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "mygstcafe.utils.before_app_install"
# after_app_install = "mygstcafe.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "mygstcafe.utils.before_app_uninstall"
# after_app_uninstall = "mygstcafe.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "mygstcafe.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	# "*": {
    #     "get_list": "mygstcafe.mygstcafe.utils.apply_default_company_filter"
    #},
 
#   'Sales Invoice': {
#         'before_list': 'mygstcafe.mygstcafe.doctype.sales_invoice.filter_sales_invoice.extend_sales_invoice_filters'
#     }

    "Item": {
        "before_save": "mygstcafe.set_item_defaults.before_save"
    }
 
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"mygstcafe.tasks.all"
# 	],
# 	"daily": [
# 		"mygstcafe.tasks.daily"
# 	],
# 	"hourly": [
# 		"mygstcafe.tasks.hourly"
# 	],
# 	"weekly": [
# 		"mygstcafe.tasks.weekly"
# 	],
# 	"monthly": [
# 		"mygstcafe.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "mygstcafe.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "mygstcafe.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "mygstcafe.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["mygstcafe.utils.before_request"]
# after_request = ["mygstcafe.utils.after_request"]

# Job Events
# ----------
# before_job = ["mygstcafe.utils.before_job"]
# after_job = ["mygstcafe.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"mygstcafe.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }


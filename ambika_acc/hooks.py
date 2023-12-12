app_name = "ambika_acc"
app_title = "Ambika Acc"
app_publisher = "riddhi"
app_description = "for documentation"
app_email = "riddhi@sanskartechnolab.com"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/ambika_acc/css/ambika_acc.css"
# app_include_js = "/assets/ambika_acc/js/ambika_acc.js"

# include js, css files in header of web template
# web_include_css = "/assets/ambika_acc/css/ambika_acc.css"
# web_include_js = "/assets/ambika_acc/js/ambika_acc.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "ambika_acc/public/scss/website"

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
# app_include_icons = "ambika_acc/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "ambika_acc.utils.jinja_methods",
#	"filters": "ambika_acc.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "ambika_acc.install.before_install"
# after_install = "ambika_acc.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "ambika_acc.uninstall.before_uninstall"
# after_uninstall = "ambika_acc.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "ambika_acc.utils.before_app_install"
# after_app_install = "ambika_acc.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "ambika_acc.utils.before_app_uninstall"
# after_app_uninstall = "ambika_acc.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "ambika_acc.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"ambika_acc.tasks.all"
#	],
#	"daily": [
#		"ambika_acc.tasks.daily"
#	],
#	"hourly": [
#		"ambika_acc.tasks.hourly"
#	],
#	"weekly": [
#		"ambika_acc.tasks.weekly"
#	],
#	"monthly": [
#		"ambika_acc.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "ambika_acc.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "ambika_acc.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "ambika_acc.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["ambika_acc.utils.before_request"]
# after_request = ["ambika_acc.utils.after_request"]

# Job Events
# ----------
# before_job = ["ambika_acc.utils.before_job"]
# after_job = ["ambika_acc.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"ambika_acc.auth.validate"
# ]

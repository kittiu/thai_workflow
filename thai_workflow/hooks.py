app_name = "thai_workflow"
app_title = "Thai Workflow"
app_publisher = "Ecosoft"
app_description = "Workflow enhancements"
app_email = "kittiu@ecosoft.co.th"
app_license = "mit"
# required_apps = []

fixtures = [
	{
		"doctype": "Custom Field",
		"filters": [
			[
				"name",
				"in",
				(
                    "Workflow Transition-custom_use_role_formula",
                    "Workflow Transition-custom_role_formula",
                    "Workflow Transition-custom_role",
				),
			]
		],
	},
	{
		"doctype": "Property Setter",
		"filters": [
			[
				"name",
				"in",
				(
                    "Workflow Transition-allowed-fieldtype",
                    "Workflow Transition-allowed-default",
                    "Workflow Transition-allowed-is_virtual",
				),
			]
		],
	},
]



# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/thai_workflow/css/thai_workflow.css"
# app_include_js = "/assets/thai_workflow/js/thai_workflow.js"

# include js, css files in header of web template
# web_include_css = "/assets/thai_workflow/css/thai_workflow.css"
# web_include_js = "/assets/thai_workflow/js/thai_workflow.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "thai_workflow/public/scss/website"

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
# app_include_icons = "thai_workflow/public/icons.svg"

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
# 	"methods": "thai_workflow.utils.jinja_methods",
# 	"filters": "thai_workflow.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "thai_workflow.install.before_install"
# after_install = "thai_workflow.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "thai_workflow.uninstall.before_uninstall"
# after_uninstall = "thai_workflow.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "thai_workflow.utils.before_app_install"
# after_app_install = "thai_workflow.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "thai_workflow.utils.before_app_uninstall"
# after_app_uninstall = "thai_workflow.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "thai_workflow.notifications.get_notification_config"

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

override_doctype_class = {
	"Workflow Transition": "thai_workflow.custom.workflow_transition.WorkflowTransitionTH",
}

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"thai_workflow.tasks.all"
# 	],
# 	"daily": [
# 		"thai_workflow.tasks.daily"
# 	],
# 	"hourly": [
# 		"thai_workflow.tasks.hourly"
# 	],
# 	"weekly": [
# 		"thai_workflow.tasks.weekly"
# 	],
# 	"monthly": [
# 		"thai_workflow.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "thai_workflow.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "thai_workflow.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "thai_workflow.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# kittiu: This hook is not necessary if field "allowed" is type "Data" in doctype
ignore_links_on_delete = ["Workflow Transition"]

# Request Events
# ----------------
# before_request = ["thai_workflow.utils.before_request"]
# after_request = ["thai_workflow.utils.after_request"]

# Job Events
# ----------
# before_job = ["thai_workflow.utils.before_job"]
# after_job = ["thai_workflow.utils.after_job"]

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
# 	"thai_workflow.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }


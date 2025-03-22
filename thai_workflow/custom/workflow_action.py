import frappe
from frappe import _
from frappe.workflow.doctype.workflow_action.workflow_action import (
    get_doc_workflow_state,
	get_state_optional_field_value,
	is_transition_condition_satisfied,
	get_email_template_from_workflow,
	get_link_to_form,
)
from frappe.model.workflow import get_workflow


def is_workflow_action_already_created(doc):
	# Monkey patching,
    # This method has potential to get called often
	frappe.flags.wkf_role_formula_doc = doc
	# --
	return frappe.db.exists(
		{
			"doctype": "Workflow Action",
			"reference_name": doc.get("name"),
			"reference_doctype": doc.get("doctype"),
			"workflow_state": get_doc_workflow_state(doc),
		}
	)

def get_allowed_roles(user, workflow, workflow_state):
	user = user if user else frappe.session.user

	wkf_trans = frappe.get_all(  # monkey patch
		"Workflow Transition",
		filters=[["parent", "=", workflow], ["next_state", "=", workflow_state]],
		pluck="name",  # monkey patch
	)

	# monkey patch
	allowed_roles = [
		frappe.get_doc("Workflow Transition", t).allowed
		for t in wkf_trans
	]
	# --

	user_roles = set(frappe.get_roles(user))
	# monkey patch
	allowed_roles = [r for r in allowed_roles if r]
	# --
	return set(allowed_roles).intersection(user_roles)


def get_next_possible_transitions(workflow_name, state, doc=None):
	# monkey patch
	wkf_trans = frappe.get_all(
		"Workflow Transition",
		filters=[["parent", "=", workflow_name], ["state", "=", state]],
		pluck="name",
	)

	# monkey patch
	transitions = []
	for t in wkf_trans:
		tran = frappe.get_doc("Workflow Transition", t)
		transitions.append(frappe._dict({
			"allowed": tran.allowed,
			"action": tran.action,
			"state": tran.state,
			"allow_self_approval": tran.allow_self_approval,
			"next_state": tran.next_state,
			"condition": tran.condition,
		}))
	# --

	transitions_to_return = []

	for transition in transitions:
		is_next_state_optional = get_state_optional_field_value(workflow_name, transition.next_state)
		# skip transition if next state of the transition is optional
		if is_next_state_optional:
			continue
		if not is_transition_condition_satisfied(transition, doc):
			continue
		transitions_to_return.append(transition)

	return transitions_to_return


def get_common_email_args(doc):
	doctype = doc.get("doctype")
	docname = doc.get("name")

	email_template = get_email_template_from_workflow(doc)
	if email_template:
		subject = email_template.get("subject")
		response = email_template.get("message")
	else:
		subject = _("Workflow Action") + f" on {doctype}: {docname}"
		response = get_link_to_form(doctype, docname, f"{doctype}: {docname}")

	print_format = doc.meta.default_print_format
	lang = doc.get("language") or (
		frappe.get_cached_value("Print Format", print_format, "default_print_language")
		if print_format
		else None
	)

	common_args = {
		"template": "workflow_action",
		"header": "Workflow Action",
		"attachments": [
			frappe.attach_print(
				doctype,
				docname,
				file_name=docname,
				doc=doc,
				lang=lang,
				print_format=print_format,
			)
		],
		"subject": subject,
		"message": response,
	}

	# Monkey Patch
 	# Add all existing attachments from the document
	workflow = get_workflow(doctype)
	if not workflow.custom_include_all_attachments_in_email:
		attachments = frappe.get_all(
			"File",
			fields=["name", "file_url", "file_name", "is_private"],
			filters={
				"attached_to_doctype": doctype,
				"attached_to_name": docname,
			}
		)
		for attachment in attachments:
			file_path = frappe.utils.get_files_path(attachment.file_name, is_private=False)
			if attachment.is_private:
				file_path = frappe.utils.get_files_path(attachment.file_name, is_private=True)
			with open(file_path, "rb") as f:
				common_args["attachments"].append({
					"fname": attachment.file_name,
					"fcontent": f.read()
				})
	# --
	return common_args

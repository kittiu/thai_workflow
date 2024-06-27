import frappe
from frappe.workflow.doctype.workflow_action.workflow_action import (
    get_doc_workflow_state,
	get_state_optional_field_value,
	is_transition_condition_satisfied
)


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
		frappe.get_cached_doc("Workflow Transition", t).allowed
		for t in wkf_trans
	]
	# --

	user_roles = set(frappe.get_roles(user))
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
		tran = frappe.get_cached_doc("Workflow Transition", t)
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

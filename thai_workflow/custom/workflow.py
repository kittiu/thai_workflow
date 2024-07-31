import frappe
from typing import TYPE_CHECKING, Union
if TYPE_CHECKING:
	from frappe.model.document import Document
	from frappe.workflow.doctype.workflow.workflow import Workflow
from frappe.model.workflow import (
	get_workflow,
	WorkflowStateError,
	is_transition_condition_satisfied
)


@frappe.whitelist()
def get_transitions(
	doc: Union["Document", str, dict], workflow: "Workflow" = None, raise_exception: bool = False
) -> list[dict]:
	"""Return list of possible transitions for the given doc"""
	from frappe.model.document import Document

	if not isinstance(doc, Document):
		doc = frappe.get_doc(frappe.parse_json(doc))
		doc.load_from_db()

	if doc.is_new():
		return []

    # Monkey patch here
	frappe.flags.wkf_role_formula_doc = doc
	# --

	doc.check_permission("read")

	workflow = workflow or get_workflow(doc.doctype)
	current_state = doc.get(workflow.workflow_state_field)

	if not current_state:
		if raise_exception:
			raise WorkflowStateError
		else:
			frappe.throw(_("Workflow State not set"), WorkflowStateError)

	transitions = []
	roles = frappe.get_roles()

	for transition in workflow.transitions:
		if transition.state == current_state and transition.allowed in roles:
			if not is_transition_condition_satisfied(transition, doc):
				continue
		    # Monkey patch here
			transition_vals = transition.as_dict()
			transition_vals.update(allowed=transition.allowed)
			transitions.append(transition_vals)
			# ----
	return transitions

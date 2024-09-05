__version__ = "0.0.1"


# Monkey patching
# ------------------

import frappe.model.workflow as workflow
from thai_workflow.custom.workflow import get_transitions
workflow.get_transitions = get_transitions

import frappe.workflow.doctype.workflow_action.workflow_action as workflow_action
from thai_workflow.custom.workflow_action import (
    is_workflow_action_already_created,
    get_allowed_roles,
    get_next_possible_transitions
)
workflow_action.is_workflow_action_already_created = is_workflow_action_already_created
workflow_action.get_allowed_roles = get_allowed_roles
workflow_action.get_next_possible_transitions = get_next_possible_transitions

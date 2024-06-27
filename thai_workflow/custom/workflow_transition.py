import frappe
from frappe.workflow.doctype.workflow_transition.workflow_transition import WorkflowTransition
from frappe.model.workflow import get_workflow_safe_globals

class WorkflowTransitionTH(WorkflowTransition):

    @property
    def allowed(self):
        if self.custom_use_role_formula:
            doc = frappe.flags.wkf_role_formula_doc
            if doc:
                role = frappe.safe_eval(
                    self.custom_role_formula,
                    get_workflow_safe_globals(), dict(doc=doc.as_dict())
                )
                return role
            return "Role Formula"
        return self.custom_role
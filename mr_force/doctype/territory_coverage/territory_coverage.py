from __future__ import annotations

import frappe
from frappe.model.document import Document
from frappe.utils import getdate


class TerritoryCoverage(Document):
    def validate(self) -> None:
        if hasattr(self, "visit_datetime") and self.visit_datetime:
            self.visit_date = getdate(self.visit_datetime)

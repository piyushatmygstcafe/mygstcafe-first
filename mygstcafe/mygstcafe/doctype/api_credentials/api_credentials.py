# Copyright (c) 2024, Pinnacle Finserv Advisors Private Limited and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

from datetime import datetime

class APICredentials(Document):
    def onload(self):
        # Get today's date
        today = datetime.today()

        self.application_from = today.date()

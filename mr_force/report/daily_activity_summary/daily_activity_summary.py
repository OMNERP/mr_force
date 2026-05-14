from __future__ import annotations
import frappe

def execute(filters=None):
    columns=[{"label":"Date","fieldname":"report_date","fieldtype":"Date","width":120},{"label":"Representative","fieldname":"medical_representative","fieldtype":"Link","options":"Medical Representative","width":220},{"label":"Doctor Visits","fieldname":"doctor_visits","fieldtype":"Int","width":120},{"label":"Pharmacy Visits","fieldname":"pharmacy_visits","fieldtype":"Int","width":120}]
    data=frappe.get_all("Daily Activity Report", fields=["report_date","medical_representative","doctor_visits","pharmacy_visits"], order_by="report_date desc", limit_page_length=500)
    return columns, data

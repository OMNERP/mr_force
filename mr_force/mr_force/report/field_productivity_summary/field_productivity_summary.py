from __future__ import annotations
import frappe

def execute(filters=None):
    columns=[{"label":"Representative","fieldname":"medical_representative","fieldtype":"Link","options":"Medical Representative","width":220},{"label":"Visits","fieldname":"visits","fieldtype":"Int","width":100},{"label":"Completed","fieldname":"completed","fieldtype":"Int","width":100}]
    data=frappe.db.sql("""select medical_representative, count(*) visits, sum(case when status='Completed' then 1 else 0 end) completed from `tabDoctor Visit` group by medical_representative order by visits desc""", as_dict=True)
    return columns, data

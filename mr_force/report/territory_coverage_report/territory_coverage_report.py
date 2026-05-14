from __future__ import annotations
import frappe

def execute(filters=None):
    columns=[{"label":"Territory","fieldname":"territory","fieldtype":"Link","options":"Territory Coverage","width":220},{"label":"Doctors","fieldname":"doctors","fieldtype":"Int","width":100},{"label":"Visits","fieldname":"visits","fieldtype":"Int","width":100}]
    data=frappe.db.sql("""select dp.territory, count(distinct dp.name) doctors, count(dv.name) visits from `tabDoctor Profile` dp left join `tabDoctor Visit` dv on dv.doctor=dp.name group by dp.territory order by doctors desc""", as_dict=True)
    return columns, data

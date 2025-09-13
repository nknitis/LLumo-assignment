from datetime import datetime

def parse_joining_date(date_str: str) -> datetime:
    return datetime.strptime(date_str, "%Y-%m-%d")

def employee_helper(doc):
    jd = doc.get("joining_date")
    if isinstance(jd, datetime):
        jd_str = jd.strftime("%Y-%m-%d")
    else:
        jd_str = jd
    return {
        "id": str(doc.get("_id")),
        "employee_id": doc.get("employee_id"),
        "name": doc.get("name"),
        "department": doc.get("department"),
        "salary": doc.get("salary"),
        "joining_date": jd_str,
        "skills": doc.get("skills", []),
    }

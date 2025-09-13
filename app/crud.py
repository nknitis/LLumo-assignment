from .database import employees_collection
from .utils import parse_joining_date, employee_helper
from fastapi import HTTPException
from bson.objectid import ObjectId
from pymongo.errors import DuplicateKeyError

async def create_employee(data: dict):
    data["joining_date"] = parse_joining_date(data["joining_date"])
    try:
        res = await employees_collection.insert_one(data)
    except DuplicateKeyError:
        raise HTTPException(status_code=400, detail="employee_id already exists")
    doc = await employees_collection.find_one({"_id": res.inserted_id})
    return employee_helper(doc)

async def get_employee_by_empid(emp_id: str):
    doc = await employees_collection.find_one({"employee_id": emp_id})
    if not doc:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee_helper(doc)

async def update_employee(emp_id: str, update_data: dict):
    if "joining_date" in update_data:
        update_data["joining_date"] = parse_joining_date(update_data["joining_date"])
    result = await employees_collection.update_one({"employee_id": emp_id}, {"$set": update_data})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Employee not found")
    doc = await employees_collection.find_one({"employee_id": emp_id})
    return employee_helper(doc)

async def delete_employee(emp_id: str):
    result = await employees_collection.delete_one({"employee_id": emp_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"detail": "Employee deleted successfully."}

async def list_employees(query: dict, page: int, limit: int):
    skip = (page - 1) * limit
    cursor = employees_collection.find(query).sort("joining_date", -1).skip(skip).limit(limit)
    out = []
    async for doc in cursor:
        out.append(employee_helper(doc))
    return out

async def avg_salary_by_department():
    pipeline = [
        {"$group": {"_id": "$department", "avg_salary": {"$avg": "$salary"}}},
        {"$project": {"_id": 0, "department": "$_id", "avg_salary": {"$round": ["$avg_salary", 0]}}}
    ]
    cursor = employees_collection.aggregate(pipeline)
    out = []
    async for doc in cursor:
        out.append(doc)
    return out

async def search_by_skill(skill: str, page: int, limit: int):
    skip = (page - 1) * limit
    cursor = employees_collection.find({"skills": skill}).sort("joining_date", -1).skip(skip).limit(limit)
    out = []
    async for doc in cursor:
        out.append(employee_helper(doc))
    return out

from fastapi import APIRouter, Query
from typing import List, Optional
from ..schemas import EmployeeCreate, EmployeeOut, EmployeeUpdate
from .. import crud

router = APIRouter(prefix="/employees", tags=["employees"])

@router.post("", response_model=EmployeeOut)
async def create_employee(emp: EmployeeCreate):
    return await crud.create_employee(emp.dict())

@router.get("/{employee_id}", response_model=EmployeeOut)
async def get_employee(employee_id: str):
    return await crud.get_employee_by_empid(employee_id)

@router.put("/{employee_id}", response_model=EmployeeOut)
async def update_employee(employee_id: str, upd: EmployeeUpdate):
    data = {k: v for k, v in upd.dict().items() if v is not None}
    if not data:
        return await crud.get_employee_by_empid(employee_id)
    return await crud.update_employee(employee_id, data)

@router.delete("/{employee_id}")
async def delete_employee(employee_id: str):
    return await crud.delete_employee(employee_id)

@router.get("", response_model=List[EmployeeOut])
async def list_employees(department: Optional[str] = None, page: int = Query(1, ge=1), limit: int = Query(10, ge=1, le=100)):
    q = {}
    if department:
        q["department"] = department
    return await crud.list_employees(q, page, limit)

@router.get("/avg-salary")
async def avg_salary():
    return await crud.avg_salary_by_department()

@router.get("/search", response_model=List[EmployeeOut])
async def search(skill: str, page: int = 1, limit: int = 10):
    return await crud.search_by_skill(skill, page, limit)

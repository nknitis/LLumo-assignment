from pydantic import BaseModel, Field, validator
from typing import List, Optional
from datetime import datetime

class EmployeeBase(BaseModel):
    employee_id: str = Field(..., example="E123")
    name: str
    department: str
    salary: int = Field(..., ge=0)
    joining_date: str = Field(..., example="2023-01-15")
    skills: List[str] = []

    @validator("joining_date")
    def check_date(cls, v):
        datetime.strptime(v, "%Y-%m-%d")
        return v

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(BaseModel):
    name: Optional[str]
    department: Optional[str]
    salary: Optional[int]
    joining_date: Optional[str]
    skills: Optional[List[str]]

    @validator("joining_date")
    def check_date(cls, v):
        if v is None:
            return v
        datetime.strptime(v, "%Y-%m-%d")
        return v

class EmployeeOut(EmployeeBase):
    id: str

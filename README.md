📄 README.md
# Employee Management API

This is a small project built with **FastAPI** and **MongoDB**.  
It provides a set of APIs to manage employees and perform some queries like search, filter and average salary by department.  

---

## What you can do with this API
- Add a new employee  
- Get employee details by ID  
- Update employee details (partial update supported)  
- Delete an employee  
- List employees by department (sorted by joining date)  
- Search employees by skills  
- Get average salary for each department  
- Paginate employee listing (page & limit params)  

---

## Tech Used
- FastAPI (Python web framework)  
- MongoDB (database)  
- Motor (async MongoDB driver)  
- Uvicorn (server)  

---

## Getting Started

### Requirements
- Python 3.9 or higher  
- MongoDB installed and running locally  

### Setup
```bash
# Clone the repository
git clone https://github.com/<your-username>/employee-api.git
cd employee-api

# Create virtual environment
python -m venv venv
# Activate it
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

Configure

Create a .env file in the project root:

MONGO_URI=mongodb://localhost:27017
DB_NAME=assessment_db

Run the Server
uvicorn app.main:app --reload


Open API docs in your browser:
👉 http://127.0.0.1:8000/docs

Example Usage
Create Employee
POST /employees

{
  "employee_id": "E101",
  "name": "Ravi Kumar",
  "department": "Engineering",
  "salary": 85000,
  "joining_date": "2023-06-01",
  "skills": ["Python", "FastAPI"]
}

Update Employee
PUT /employees/E101

{
  "salary": 90000
}

Average Salary
GET /employees/avg-salary


Response:

[
  { "department": "Engineering", "avg_salary": 87500 },
  { "department": "HR", "avg_salary": 60000 }
]

Notes

Make sure MongoDB is running before starting the server.

Pagination works with page and limit query params. Example:

GET /employees?page=1&limit=5


employee_id is unique (index is applied).

Collection has schema validation so only valid data is stored.

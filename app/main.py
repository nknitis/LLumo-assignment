from fastapi import FastAPI
from . import database
from .routes import employees

app = FastAPI(title="Employee Management API")

@app.on_event("startup")
async def startup():
    await database.init_db()

app.include_router(employees.router)

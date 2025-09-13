from motor.motor_asyncio import AsyncIOMotorClient
from .config import settings
from pymongo import ASCENDING
from pymongo.errors import CollectionInvalid

client = AsyncIOMotorClient(settings.MONGO_URI)
db = client[settings.DB_NAME]

employees_collection = db["employees"]

async def init_db():
    # Unique index on employee_id
    await employees_collection.create_index([("employee_id", ASCENDING)], unique=True)

    # JSON Schema validator for employees
    validator = {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["employee_id", "name", "department", "salary", "joining_date", "skills"],
            "properties": {
                "employee_id": {"bsonType": "string"},
                "name": {"bsonType": "string"},
                "department": {"bsonType": "string"},
                "salary": {"bsonType": ["int", "double", "long"]},
                "joining_date": {"bsonType": "date"},
                "skills": {"bsonType": "array", "items": {"bsonType": "string"}},
            },
        }
    }

    try:
        await db.create_collection("employees", validator=validator)
    except CollectionInvalid:
        try:
            await db.command({
                "collMod": "employees",
                "validator": validator,
                "validationLevel": "moderate"
            })
        except Exception:
            pass

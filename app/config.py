from pydantic import BaseSettings

class Settings(BaseSettings):
    MONGO_URI: str = "mongodb://localhost:27017"
    DB_NAME: str = "assessment_db"

    class Config:
        env_file = ".env"

settings = Settings()

import os
from pydantic_settings import BaseSettings  # Changed this line

class Settings(BaseSettings):
    ENVIRONMENT: str
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str

    class Config:
        env_file = os.path.join(os.path.dirname(__file__), "..", ".env")  # Ensures correct location

settings = Settings()

DATABASE_URL = (
    f"postgresql://{settings.DB_USER}:{settings.DB_PASSWORD}"
    f"@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
)

# For debug
print("✅ Environment Loaded:", settings.ENVIRONMENT)

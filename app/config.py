from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    ALLOW_ORIGINS: list[str] = ["http://localhost:3000"]

    class Config:
        env_file = ".env"



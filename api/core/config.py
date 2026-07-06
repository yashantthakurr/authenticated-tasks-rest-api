
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    ALGORITHM: str
    DATABASE_URL: str
    DEBUG: bool = False
    SECRET_KEY: str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "ETL Health Microservice"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"

    model_config = SettingsConfigDict(case_sensitive=True)

settings = Settings()
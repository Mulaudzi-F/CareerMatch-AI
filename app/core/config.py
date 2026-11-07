from paydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name:str = "CareerPilot AI"
    app_env:str = "development"
    debug:bool = True
    api_v1_prefix: str = "/api/v1"

    database_url: str = "postgresql+psycopg://careerpilot:careerpilot_dev_password@localhost:5432/careerpilot"

    openai_api_key: str = ""
    openai_chat_model: str = "gpt-4.1-mini"
    openai_embedding_model: str = "text-embedding-3-small"
    embedding_dimensions: int = 1536

    max_upload_size_mb: int = 10

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


settings = Settings()

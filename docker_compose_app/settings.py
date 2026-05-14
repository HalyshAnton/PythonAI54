from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # налаштування
    host: str = "0.0.0.0"
    port: int = 8080

    text: str = ""

    # читаємо дані з .env файла
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


# створення об'єкта класу
settings = Settings()

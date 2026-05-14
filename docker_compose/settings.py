from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # налаштування
    start_range: int = 0
    end_range: int = 100

    # секретна інформація
    password: str = ""
    login: str = ""

    # читаємо дані з .env файла
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


# створення об'єкта класу
settings = Settings()

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # налаштування
    secret_text: str = "hello"
    password: str | None = None

    min_num: int = 10
    max_num: int = 100

    # читання налаштуваня з .env файла
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


# створити об'єкт цього класу
settings = Settings()

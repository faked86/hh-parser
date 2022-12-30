from pydantic import BaseSettings


class Settings(BaseSettings):
    base_url: str = "https://www.hh.ru"


settings = Settings()

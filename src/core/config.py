import os
from pathlib import Path

import dotenv
from pydantic_settings import BaseSettings


def load_env(base_dir: str) -> None:
    dotenv.load_dotenv(os.path.join(base_dir, "var/.env"), override=True)
    dotenv.load_dotenv(os.path.join(base_dir, "var/.env.dev"), override=True)


def get_db_urls():
    DATABASES: dict = {
        "default": {
            "ENGINE": str(os.getenv("POSTGRES_ENGINE")),
            "NAME": str(os.getenv("POSTGRES_DB")),
            "USER": str(os.getenv("POSTGRES_USER")),
            "PASSWORD": str(os.getenv("POSTGRES_PASSWORD")),
            "HOST": str(os.getenv("POSTGRES_HOST")),
            "PORT": str(os.getenv("POSTGRES_PORT")),
        }
    }
    d: str = DATABASES["default"]

    return f"postgresql+{d['ENGINE']}://{d['USER']}:{d['PASSWORD']}@{d['HOST']}:{d['PORT']}/{d['NAME']}"


class Settings(BaseSettings):
    BASE_DIR: str = str(Path(__file__).resolve().parent.parent.parent)
    load_env(BASE_DIR)

    DEBUG: bool = str(os.getenv("DEBUG")) == "True"

    db_url: str = get_db_urls()

    db_echo: bool = DEBUG


settings = Settings()

from pathlib import Path

from pydantic import BaseSettings


class Config(BaseSettings):
    DEBUG = True
    POSTGRES_USER = "postgres"
    POSTGRES_PASSWORD = "ali3z110"
    POSTGRES_HOST = "localhost"
    POSTGRES_PORT = 5432
    POSTGRES_DATABASE = "postgres"

    # class Config:
    #     case_sensitive = False
    #     BASE_DIR = Path(__file__).resolve().parent.parent.parent
    #     env_file = (str(BASE_DIR) + "/.env").replace("//", "/")
    #     env_file_encoding = 'utf-8'


config = Config()


class PasswordConfig:
    MIN_LENGTH = 8
    UPPERCASE_REQUIRED = False
    LOWERCASE_REQUIRED = True
    DIGIT_REQUIRED = True
    SPECIAL_CHARACTERS_REQUIRED = False
    SPECIAL_CHARACTERS = r"[!@#$%^&*()]"

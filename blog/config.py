from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.


class Settings(BaseSettings):
    database_hostname: str = "localhost"
    database_port: str = 5432
    database_password: str = "postgres"
    database_name: str = "blog_api"
    database_username: str = "postgres"
    # secret_key: str
    # algorithm: str
    # access_token_expire_minutes: int

    class Config:
        env_file = ".env"


settings = Settings()
if settings:
    print(
        f"Connecting to database........\n Database Name: {settings.database_name},\n Database Password: {settings.database_password}")

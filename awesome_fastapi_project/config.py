from pydantic import BaseSettings

class Settings(BaseSettings):
    production_database_url: str
    test_database_url: str
    database_url: str = "sqlite://:memory:"
    secret_key: str
    debug: bool = True

    class Config:
        env_file = ".env"

config = Settings()

if config.debug:
    config.database_url = config.test_database_url

else:
    config.database_url = config.production_database_url
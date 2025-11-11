from pydantic_settings import BaseSettings

# Allows us to check if an environment variable is missing
class Settings(BaseSettings):
    database_hostname: str
    database_port: str 
    database_password: str 
    database_name: str 
    database_username: str 
    secret_key: str
    algorithm: str 
    access_token_expire_minutes: int

    # Add this default for local development
    database_sslmode: str = "disable"

    class Config:
        env_file = ".env"

settings = Settings()
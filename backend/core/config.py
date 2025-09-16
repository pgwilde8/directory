"""
Application configuration settings
"""
from pydantic_settings import BaseSettings
from typing import Optional
import os


class Settings(BaseSettings):
    """Application settings"""
    
    # App Configuration
    APP_NAME: str = "Directory"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False
    HOST: str = "0.0.0.0"
    PORT: int = 9178
    
    # Database
    DATABASE_URL: str = "postgresql://adminwatch:adminwatch123@localhost/directory"
    
    # Security
    SECRET_KEY: str = "Ege4aZ0BP6JCKnBJ7OoUnLk8tW_EIDU2qSll5ntUfFE"
    
    # NewsAPI Configuration
    NEWSAPI_KEY: str = "d7a060516f7a43fa9638b44b6c570dbc"
    NEWSAPI_BASE_URL: str = "https://newsapi.org/v2"
    
    # Logging
    LOG_LEVEL: str = "INFO"
    LOG_FILE: str = "logs/app.log"
    
    # API Rate Limiting
    RATE_LIMIT_PER_MINUTE: int = 60
    RATE_LIMIT_PER_HOUR: int = 1000
    
    # Data Collection
    COLLECTION_INTERVAL_MINUTES: int = 60
    MAX_ARTICLES_PER_REQUEST: int = 100
    
    # Authentication
    ADMIN_USERNAME: str = "admin"
    ADMIN_PASSWORD: str = "admin123"
    SESSION_TIMEOUT_HOURS: int = 24
    
    # Timing Controls
    LOGIN_START_HOUR: int = 6  # 6 AM
    LOGIN_END_HOUR: int = 22   # 10 PM
    TIMEZONE: str = "US/Eastern"
    
    class Config:
        env_file = ".env"
        case_sensitive = True


# Create settings instance
settings = Settings()

"""Settings configuration using Pydantic."""

import os
from typing import Any, Dict, Optional

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings configuration."""
    
    # Server settings
    HOST: str = Field("127.0.0.1", description="Server host")
    PORT: int = Field(8000, description="Server port")
    DEBUG: bool = Field(False, description="Debug mode")
    
    # API settings
    API_PREFIX: str = Field("/api/v1", description="API prefix")
    
    # Logging settings
    LOG_LEVEL: str = Field("INFO", description="Log level")
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
    )
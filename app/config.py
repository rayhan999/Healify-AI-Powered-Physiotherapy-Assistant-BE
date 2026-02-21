from pydantic_settings import BaseSettings
from typing import List
import os

class Settings(BaseSettings):
    # App Settings
    APP_NAME: str = "Exercise Accuracy API"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True
    
    # Model Paths
    MODEL_PATH: str = "./ml_models/final_model.keras"
    THRESHOLD_PATH: str = "./ml_models/threshold.npy"
    CONFIG_PATH: str = "./ml_models/config.json"
    
    # API Settings
    API_PREFIX: str = "/api/v1"
    CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:5173"]
    
    # Server Settings
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
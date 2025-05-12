import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Centralized configuration with environment variable fallbacks"""
    DEBUG = os.getenv('DEBUG', 'False') == 'True'  # Development mode
    HOST = os.getenv('HOST', '0.0.0.0')  # Binding address
    PORT = int(os.getenv('PORT', 5000))  # Listening port

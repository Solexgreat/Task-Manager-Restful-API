import os
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

class Config:
     # Fetch environment variables, with fallback default values if necessary
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    MONGO_URI = os.getenv('MONGO_URI')

    if not MONGO_URI:
        raise Exception ("MONGO_URI not set in environment variables")

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False


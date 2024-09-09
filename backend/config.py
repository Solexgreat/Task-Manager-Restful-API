import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'secret_key')
    MONGO_URI = os.getenv('MONGO_URI', "mongodb+srv://Solexgreat:solexgreat1$@cluster0.wekq3.mongodb.net/")

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
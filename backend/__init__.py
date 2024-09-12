from flask import Flask
from flask_jwt_extended import JWTManager
from .config import Config
from pymongo import MongoClient
from .routes import user_bp, task_bp, auth_bp

def create_app():
  app = Flask(__name__)

    # Load configuration from config class
  app.config.from_object(Config)

  #Configure your secret key for encoding JWT
  app.config['JWT_SECRET_KEY'] = 'secret_key'

  #initialize JWT manger
  jwt = JWTManager(app)

  # Initialize MongoDB client using MONGO_URI from the config
  client = MongoClient(app.config['MONGO_URI'])
  db = client.flask_example_db

  # Attach the db to the app so you can access it later
  app.db = db

  # Import and register your blueprints (routes)

  app.register_blueprint(user_bp)
  app.register_blueprint(task_bp)
  app.register_blueprint(auth_bp)

  return app
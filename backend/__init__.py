from flask import Flask
import os
from flask_jwt_extended import JWTManager
from .config import Config
from pymongo import MongoClient
from mongoengine import connect
from .routes import user_bp, task_bp, auth_bp
from .column.app.v1.error import register_error_handlers


def create_app():
  app = Flask(__name__)

    # Load configuration from config class
  app.config.from_object(Config)

  #Configure your secret key for encoding JWT
  app.config['JWT_SECRET_KEY'] = app.config['JWT_SECRET']


  #initialize JWT manger
  jwt = JWTManager(app)

  # Initialize MongoDB client using MONGO_URI from the config
  #Pymongo
  client = MongoClient(app.config['MONGO_URI'])
  db = client['task-manager-project']

  #Mongoengine
  connect(db='task-manager-project', host=app.config['MONGO_URI'])

  # Attach the db to the app so you can access it later
  app.db = db

  # Import and register your blueprints (routes)

  app.register_blueprint(user_bp)
  app.register_blueprint(task_bp)
  app.register_blueprint(auth_bp)
  register_error_handlers(app)

  return app
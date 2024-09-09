from flask import Flask
from routes.users import user_bp

def create_app():
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(user_bp)

    return app
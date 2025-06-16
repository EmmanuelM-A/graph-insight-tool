from flask import Flask
from src.routes.upload_routes import upload_bp
from src.configs.upload_configs import UPLOAD_DIRECTORY
import os

def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")

    app.config["UPLOAD_FOLDER"] = UPLOAD_DIRECTORY
    app.secret_key = os.getenv("FLASK_SECRET_KEY")

    # Register Blueprints
    app.register_blueprint(upload_bp, url_prefix="/api")

    return app

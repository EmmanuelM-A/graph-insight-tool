from flask import Flask
from src.routes.upload_routes import upload_bp
from src.configs.upload_configs import UPLOAD_DIRECTORY
import os

from src.utils.logger import get_logger

logger = get_logger("app_logger")

def create_app():
    app = Flask(__name__)

    app.config["UPLOAD_FOLDER"] = UPLOAD_DIRECTORY
    app.secret_key = os.getenv("FLASK_SECRET_KEY")

    # Register Blueprints
    app.register_blueprint(upload_bp)

    logger.info("App setup and running!")

    return app

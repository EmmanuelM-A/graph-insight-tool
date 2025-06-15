from flask import Flask
from src.routes.upload_routes import upload_bp
from src.configs.upload_configs import UPLOAD_DIRECTORY

def create_app():
    app = Flask(__name__)

    app.config["UPLOAD_FOLDER"] = UPLOAD_DIRECTORY

    # Register Blueprints
    app.register_blueprint(upload_bp)

    return app

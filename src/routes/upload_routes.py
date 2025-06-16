from flask import Blueprint, request
from src.controllers.upload_controller import process_upload_request

upload_bp = Blueprint("upload_blueprint", __name__)

@upload_bp.route("/upload", methods=["POST"])
def upload_file():
    return process_upload_request(request)
from flask import Blueprint, request
from src.controllers.upload_controller import process_upload_request

upload_bp = Blueprint("upload", __name__, url_prefix="/api/uploads")

@upload_bp.route("/", methods=["POST"])
def upload_file():
    return process_upload_request(request)
from flask import Blueprint, request
from src.controllers.preprocess_controller import preprocess_data_request

preprocess_bp = Blueprint("preprocess_blueprint", __name__)

@preprocess_bp.route("/preprocess", methods=["POST"])
def preprocess_data():
    return preprocess_data_request(request)
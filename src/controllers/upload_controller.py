from flask import jsonify
from werkzeug.utils import secure_filename
import os
from src.modules.data_uploader.upload_handler import handle_upload
from src.configs.upload_configs import UPLOAD_DIRECTORY, ALLOWED_EXTENSIONS
from src.configs.http_response_codes import HTTP_BAD_REQUEST, HTTP_OK
from src.utils.logger import get_logger

logger = get_logger("upload_controller_logger")

def allowed_file(filename):
    """
    Checks if the file has an allowed extension.
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def process_upload_request(request, return_all_data=False):
    # Check if the request is a POST request
    if request.method != "POST":
        logger.error("Invalid POST request!")
        return jsonify({
            "error": "Invalid POST request!",
        }), HTTP_BAD_REQUEST

    # Check if the request has the file part
    if "file" not in request.files:
        logger.error("No file part in the request!")
        return jsonify({
            "error": "No file part in the request!"
        }), HTTP_BAD_REQUEST

    file = request.files["file"]

    # Check if the file is selected
    if file.filename == "":
        logger.error("No file selected!")
        return jsonify({
            "error": "No file selected!"
        }), HTTP_BAD_REQUEST
    
    # Check if the file extension is allowed
    if not allowed_file(file.filename):
        logger.error("Invalid file format!")
        return jsonify({
            "error": "Invalid file format!"
        }), HTTP_BAD_REQUEST

    # Secure the filename and create the full path
    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_DIRECTORY, filename)

    # Ensure upload directory exists
    os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)

    # Save the file temporarily
    file.save(filepath)

    # Process the file into a DataFrame
    data, message = handle_upload(filepath)

    # Check if the data exists
    if data is None:
        logger.error(message)
        return jsonify({
            "error": message
        }), HTTP_BAD_REQUEST

    # Delete file after processing
    os.remove(filepath)

    logger.info(f"The file: {filename} has been uploaded and processed successfully!")

    data_amount = data if return_all_data else data.heaad(10)

    # Return basic metadata
    return jsonify({
        "message": message,
        "data": data_amount.to_json()
    }), HTTP_OK
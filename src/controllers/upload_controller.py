"""upload_controller.py"""

import os
from werkzeug.utils import secure_filename
from src.modules.data_uploader.upload_handler import handle_upload
from src.configs.global_configs import UPLOAD_DIRECTORY, ALLOWED_EXTENSIONS
from src.utils import exceptions
from fastapi import status

from src.utils.custom_response import SuccessResponse
from src.utils.logger import get_logger

logger = get_logger("upload_controller_logger")


def allowed_file(filename):
    """
    Checks if the file has an allowed extension.
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


async def process_upload_request(request):
    """Processes the file upload request."""

    # Check if the request is a POST request
    if request.method != "POST":
        logger.error("Invalid POST request!")

        raise exceptions.BadRequestError(
            details="Invalid POST request!"
        )

    # Check if the request has the file part
    if "file" not in request.files:
        logger.error("No file part in the request!")

        raise exceptions.BadRequestError(
            details="No file part in the request!"
        )

    file = request.files["file"]

    # Check if the file is selected
    if file.filename == "":
        logger.error("No file selected!")

        raise exceptions.BadRequestError(
            details="No file selected!"
        )

    # Check if the file extension is allowed
    if not allowed_file(file.filename):
        logger.error("Invalid file format!")

        raise exceptions.BadRequestError(
            details="Invalid file format"
        )

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

        raise exceptions.BadRequestError(
            details=message
        )

    # Delete file after processing
    os.remove(filepath)

    logger.info("The file: %s has been uploaded and processed successfully!", filename)

    # Return basic metadata
    return SuccessResponse(
        message=f"The file: {filename} has been uploaded successfully!",
        status_code=status.HTTP_200_OK,
        data=data
    )

"""upload_controller.py"""

import os
import shutil
from werkzeug.utils import secure_filename
from fastapi import UploadFile, File

from src.services.data_uploader.upload_handler import handle_upload
from src.configs.global_configs import UPLOAD_DIRECTORY, ALLOWED_EXTENSIONS
from src.exceptions import api_exceptions as ae
from src.utils.logger import get_logger

logger = get_logger(__name__)


def allowed_file(filename):
    """
    Checks if the file has an allowed extension.
    """
    return ('.' in filename and filename.rsplit('.', 1)[1].lower()
            in ALLOWED_EXTENSIONS)


async def process_upload_request(
        file: UploadFile = File(...)
) -> object:
    """Processes the file upload request using FastAPI."""

    # Check if a file was provided
    if not file or file.filename == "":
        # logger.error("No file selected for upload")
        raise ae.BadRequestException(
            details="No file selected for upload"
        )

    # Validate file format
    if not allowed_file(file.filename):
        logger.warning("Invalid file format: %s", file.filename)
        raise ae.BadRequestException(
            details=f"Invalid file format: {file.filename}"
        )

    try:
        # Secure the filename and create the full path
        filename = secure_filename(file.filename)
        filepath = os.path.join(UPLOAD_DIRECTORY, filename)

        # Ensure upload directory exists
        os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)

        # Save the uploaded file
        with open(filepath, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Process the file into a DataFrame
        data, message = handle_upload(filepath)

        # Check if the data exists
        if data is None:
            logger.error(message)
            os.remove(filepath)
            raise ae.BadRequestException(details=message)

        # Delete the file after processing
        os.remove(filepath)

        logger.info(
            "File '%s' has been uploaded successfully!",
            filename
        )

        # Return basic metadata
        return {
            "message": f"The file '{filename}' has been uploaded "
                       f"successfully!",
            "preview": data.head(10).to_json(),
            "data": data
        }
    except Exception as e:
        logger.critical(
            "Unexpected error during file upload: %s",
            str(e),
            exc_info=True
        )

        raise ae.UploadException(
            details=f"An error occurred during file processing: {str(e)}"
        )

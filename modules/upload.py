from flask import request, current_app
from werkzeug.utils import secure_filename
import os

ALLOWED_EXTENSIONS = {'csv', 'xls', 'xlsx'}

UPLOADS_PATH = "./uploads"


def allowed_file(filename):
    """
    Checks if the file has an allowed extension.
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def upload():
    """
    Handles file uploads.

    :return: Tuple of (success_flag, message_or_filepath)
    """

    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return False, "No file part"

        file = request.files['file']

        # if user does not select file, browser also submit an empty part without filename
        if file.filename == '':
            return False, "No selected file"

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)

            os.makedirs(UPLOADS_PATH, exist_ok=True)

            filepath = os.path.join(UPLOADS_PATH, filename)
            file.save(filepath)

            return True, filepath

        return False, "Invalid file format"

    return False, "Invalid request method"

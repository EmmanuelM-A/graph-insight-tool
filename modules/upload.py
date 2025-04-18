from flask import request
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'csv', 'xls', 'xlsx'}


def allowed_file(filename):
    """
    Checks if the file has an allowed extension.
    """

    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def upload():
    """
        Handles file uploads.
        :return:
        - A success message if the file is uploaded successfully.
        - An error message if the file is not allowed or no file is selected.
    """

    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return "No file part"

        file = request.files['file']

        # if user does not select file, browser also submit an empty part without filename
        if file.filename == '':
            return "No selected file"

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)

            # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # return "File uploaded successfully"

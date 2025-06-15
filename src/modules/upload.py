from flask import request
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

    :return: Tuple of (result_msg, filepath)
    """

    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return "No file part!", None

        file = request.files['file']

        # if user does not select file, browser also submit an empty part without filename
        if file.filename == '':
            return "No selected file!", None

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)

            os.makedirs(UPLOADS_PATH, exist_ok=True)

            filepath = os.path.join(UPLOADS_PATH, filename)
            file.save(filepath)

            return "File uploaded successfully!", filepath

        return "Invalid file format!", None

    return "Invalid request method!", None

"""
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request
from src.modules import upload, data_loader, recommender, analyzer

load_dotenv(".env")

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")
app.config["UPLOAD_FOLDER"] = 'uploads'


@app.route("/", methods=["GET", "POST"])
def index():
    graph = None
    insights = []
    upload_result_msg = ""
    data_preview = []
    headings = []

    if request.method == "POST":
        # Upload the file
        result_msg, filepath = upload.upload()

        upload_result_msg = result_msg

        if filepath is not None:
            # Processes the file into a pandas DataFrame
            data, msg = data_loader.data_loader(filepath)

            if data is not None:
                data_preview = data.head(5).values.tolist()

                headings = data.columns.tolist()

                column_info = analyzer.analyze(data)

                print(column_info)

                recommended_graph = recommender.recommend_graph(data)

                print(recommended_graph)

                # TODO CREATE TEST DATA FILES FOR EACH GRAPH TYPE THAT CAN ACTUALLY BE GENERATED
                # TODO CREATE TEST DATA FILES
                # TODO CREATE TESTS FOR THE ANALYZER AND RECOMMENDER

                # Visualize/Generate Graph
                # Generate Insights

            # print(f"The file {filepath} uploaded successfully!")
            # print(msg)
            # print("First 5 rows of the data:")
            # print(data.head(5))
        else:
            print(f"File upload failed: {result_msg}")

    return render_template(
        "index.html",
        message=upload_result_msg,
        headings=headings,
        data=data_preview,
    )


if __name__ == "__main__":
    app.run(debug=True)

"""
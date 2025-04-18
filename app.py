import os
from dotenv import load_dotenv
from flask import Flask, render_template, request
from modules import upload, data_loader

load_dotenv(".env")

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")
app.config["UPLOAD_FOLDER"] = 'uploads'


@app.route("/", methods=["GET", "POST"])
def index():
    graph = None
    insights = []
    filepath = None  # FOR DEBUGGING
    data = None  # FOR DEBUGGING

    if request.method == "POST":
        # Upload the file
        success, result = upload.upload()

        filepath = result

        if success:
            # If the file upload was successful then result will be the file path otherwise it will be a message
            filepath = result

            # Processes the file into a pandas DataFrame
            data, msg = data_loader.data_loader(filepath)

            # TODO CREATE THE UNIT TESTS FOR THE DATA LOADER
            # TODO DO THE ANALYZER AND RECOMMENDER STUFF HERE

            # Analyze
            # Visualize/Generate Graph
            # Generate Insights

            print(f"File uploaded successfully: {filepath}")
            print(msg)
            print("First 5 rows of the data:")
            print(data.head(5))
        else:
            print(f"File upload failed: {result}")

    return render_template("index.html", message=filepath)


if __name__ == "__main__":
    app.run(debug=True)

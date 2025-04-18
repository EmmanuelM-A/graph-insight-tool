import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, flash
from modules.upload import upload

load_dotenv(".env")

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")
app.config["UPLOAD_FOLDER"] = 'uploads'


@app.route("/", methods=["GET", "POST"])
def index():
    graph = None
    insights = []
    filepath = None

    if request.method == "POST":
        success, result = upload()

        filepath = result

        if success:
            filepath = result

            # Process
            # Analyze
            # Visualize/Generate Graph
            # Generate Insights

            print(f"File uploaded successfully: {filepath}")
        else:
            print(f"File upload failed: {result}")

    return render_template("index.html", message=filepath)


if __name__ == "__main__":
    app.run(debug=True)

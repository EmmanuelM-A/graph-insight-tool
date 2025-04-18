from flask import Flask, render_template
from modules.upload import upload

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    # Upload
    upload()

    # Process
    # Analyze
    # Visualize/Generate Graph
    # Generate Insights


    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

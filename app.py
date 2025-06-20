from src import create_app
from dotenv import load_dotenv
from flask import render_template

load_dotenv(".env")

app = create_app()

@app.route("/", methods=["GET"])
def index():
    return render_template(
        "index.html"
    )

if __name__ == "__main__":
    app.run(debug=True)

# TODO: Figure out how to implement the upload button on the frontend, so it runs the api/upload route on the backend
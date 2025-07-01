"""
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request
from src.services import upload, data_loader, recommender, analyzer

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
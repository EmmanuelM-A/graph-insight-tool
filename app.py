from src import create_app
from dotenv import load_dotenv

# TODO: Create unit and e2e tests for the upload and preprocess controllers

load_dotenv(".env")

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
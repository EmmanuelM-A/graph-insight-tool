from src import create_app
from dotenv import load_dotenv

# TODO: OPTIMIZE EXISTING CODE
# TODO: CREATE STANDARD ERROR AND SUCCESS RESPONSES
# TODO: ADD LOGGING

load_dotenv(".env")

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)

"""
Main entry point for the application.
"""

from dotenv import load_dotenv
import uvicorn

from src import create_app

# TODO: OPTIMIZE EXISTING CODE

load_dotenv(".env")

app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True)
"""
This module initializes the FastAPI application and includes the routes for the application.
"""

from fastapi import FastAPI
from src.routes.upload_routes import router as upload_router
from src.routes.preprocess_routes import router as preprocess_router


def create_app():
    """Create and configure the FastAPI application."""

    app = FastAPI()

    # Register routes
    app.include_router(upload_router)
    app.include_router(preprocess_router)

    return app

"""
This module initializes the FastAPI application and includes the routes for the application.
"""

from fastapi import FastAPI
from src.routes.upload_routes import router as upload_router
from src.routes.preprocess_routes import router as preprocess_router
from src.middleware.exception_handler import api_error_handler
from src.utils.exceptions import ApiError


def create_app():
    """Create and configure the FastAPI application."""

    app = FastAPI()

    # Register routes
    app.include_router(upload_router)
    app.include_router(preprocess_router)

    # Add exception/error handler
    app.add_exception_handler(ApiError, api_error_handler)

    return app

"""
This module initializes the FastAPI application and includes the routes for
the application.
"""

from fastapi import FastAPI
from src.routes.upload_routes import router as upload_router
from src.routes.preprocess_routes import router as preprocess_router
from src.exceptions.exception_handler import api_exception_handler
from src.exceptions.api_exceptions import ApiException


def create_app():
    """Create and configure the FastAPI application."""

    app = FastAPI()

    # Register routes
    app.include_router(upload_router, prefix="/api")
    app.include_router(preprocess_router, prefix="/api")

    # Global error handling
    app.add_exception_handler(ApiException, api_exception_handler)

    return app

"""
This file defines the routes for the preprocess functionality in the application.
"""

from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from src.controllers.preprocess_controller import preprocess_data_request

router = APIRouter()

@router.post("/preprocess")
async def preprocess_data(request: Request):
    """Endpoint to preprocess data."""

    response = await preprocess_data_request(request)

    return JSONResponse(content=response.json_object, status_code=response.status_code)

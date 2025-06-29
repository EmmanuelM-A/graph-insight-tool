"""
This file defines the routes for the upload functionality in the application.
"""

from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from src.controllers.upload_controller import process_upload_request

router = APIRouter()

@router.post("/upload")
async def upload_file(request: Request):
    """Endpoint to handle file uploads."""

    response = await process_upload_request(request)

    return JSONResponse(content=response.json_object, status_code=response.status_code)

"""
This file defines the routes for the upload functionality in the application.
"""

from fastapi import APIRouter, UploadFile, File
from src.controllers.upload_controller import process_upload_request

router = APIRouter(
    prefix="/upload",
    tags=["upload"]
)


@router.post("/")
async def upload_file(file: UploadFile = File(...)):
    """Endpoint to handle file uploads."""

    return await process_upload_request(file)

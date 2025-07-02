"""
This file defines the routes for the upload functionality in the application.
"""

from fastapi import status

from fastapi import APIRouter, UploadFile, File
from src.controllers.upload_controller import process_upload_request
from src.utils.custom_responses import SuccessResponse, ensure_serializable

router = APIRouter(
    prefix="/upload",
    tags=["upload"]
)


@router.post("/")
async def upload_file(file: UploadFile = File(...)):
    """Endpoint to handle file uploads."""

    upload_data_response = await process_upload_request(file)

    preview = upload_data_response["preview"]

    preview = ensure_serializable(preview)

    return SuccessResponse(
        message="The file has been uploaded successfully!",
        status_code=status.HTTP_200_OK,
        data=preview
    )

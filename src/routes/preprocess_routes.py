"""
This file defines the routes for the preprocess functionality in the application.
"""

from fastapi import APIRouter, UploadFile, File, status

from src.controllers.preprocess_controller import preprocess_data_request
from src.utils.custom_responses import SuccessResponse, ensure_serializable

router = APIRouter(
    prefix="/preprocess",
    tags=["preprocess"]
)

@router.post("/")
async def preprocess_data(
        file: UploadFile = File(...)
) -> SuccessResponse:
    """Endpoint to preprocess data."""

    preprocess_data_response = await preprocess_data_request(file)

    preview = preprocess_data_response["preview"]

    preview = ensure_serializable(preview)

    return SuccessResponse(
        message=f"Data preprocessing for the file {file.filename} was"
                f"completed successfully.",
        status_code=status.HTTP_200_OK,
        data=preview
    )

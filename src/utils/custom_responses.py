"""This module defines custom responses for handling API responses."""

from typing import Any
from pydantic import BaseModel, Field
from starlette.responses import JSONResponse
from fastapi import status


# ----------------------- Pydantic Models -----------------------


class ResponseModel(BaseModel):
    """Base Pydantic model for all responses."""

    success: bool = Field(
        description="Indicates if the request was successful."
    )

    message: str = Field(
        description="Success message for the response."
    )

    status_code: int = Field(
        description="HTTP status code for the error response."
    )


class SuccessResponseModel(ResponseModel):
    """Pydantic model for successful responses."""

    success: bool = Field(
        default=True
    )

    data: Any = Field(
        default=None,
        description="Optional data to be included in the response."
    )


class ErrorDetail(BaseModel):
    """Pydantic model for detailed error information."""

    code: str = Field(
        description="Error code representing the type of error."
    )

    details: str = Field(
        description="Detailed error message."
    )

    stack_trace: str = Field(
        default=None,
        description="Optional stack trace for debugging purposes."
    )


class ErrorResponseModel(ResponseModel):
    """Pydantic model for error responses."""

    error: ErrorDetail = Field(
        description="An object containing error details."
    )

# ---------------- # Response Classes (extends JSONResponse) ----------------

class SuccessResponse(JSONResponse):
    """Custom JSON response for successful requests."""

    def __init__(
            self,
            data: Any = None,
            message: str = "Request successful",
            status_code: int = status.HTTP_200_OK
    ):
        payload = SuccessResponseModel(
            success=True,
            message=message,
            status_code=status_code,
            data=data
        )
        super().__init__(
            status_code=status_code,
            content=payload.model_dump()
        )


class ErrorResponse(JSONResponse):
    """Custom JSON response for error handling."""

    def __init__(
            self,
            error: ErrorDetail,
            message: str,
            status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR
    ):
        payload = ErrorResponseModel(
            success=False,
            message=message,
            status_code=status_code,
            error=error
        )
        super().__init__(
            status_code=status_code,
            content=payload.model_dump()
        )

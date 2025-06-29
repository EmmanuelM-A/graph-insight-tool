"""This module defines a custom response class for handling API responses."""

from pydantic import BaseModel, Field


class Response(BaseModel):
    """Response model to standardize the structure of API responses."""

    success: bool = Field(description="Indicates if the request was successful.")
    message: str = Field(description="Success message for the response.")
    status_code: int = Field(description="HTTP status code for the error response.")


class SuccessResponse(Response):
    """Represents a successful API response."""

    data: object = Field(default=None,
                         description="Optional data to be included in the response.")


class ErrorDetail(BaseModel):
    """Model for detailed error information."""

    code: str = Field(description="Error code representing the type of error.")
    details: str = Field(description="Detailed error message.")
    stack_trace: str = Field(
        default=None, description="Optional stack trace for debugging purposes.")


class ErrorResponse(Response):
    """Represents an error API response."""

    error: ErrorDetail = Field(description="An object containing error details.")

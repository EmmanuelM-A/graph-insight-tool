"""This module defines custom exceptions for the API."""

from typing import Optional

from fastapi import HTTPException, status
from src.utils.custom_responses import ErrorResponse, ErrorDetail


class ApiException(HTTPException):
    """
    Custom base error class for API errors/exceptions, providing a
    structured error response.

    Inherits from HTTPException.
    """

    def __init__(
        self,
        error_detail: ErrorDetail,
        status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR,
        message: str = "An unexpected error occurred."
    ):
        """
        Initializes the ApiError.

        Args:
            error_detail: An instance of ErrorDetail providing specific error
            information.
            status_code: The HTTP status code for the response.
            message: A high-level message for the error response.
        """
        # Create the full ErrorResponse object
        self.error_response = ErrorResponse(
            message=message,
            status_code=status_code,
            error=error_detail
        )

        super().__init__(
            status_code=status_code,
            detail=self.error_response
        )


class ValidationException(ApiException):
    """
    Custom error class for validation errors (e.g., invalid input data).
    Corresponds to HTTP 422 Unprocessable Entity.
    """
    def __init__(
        self,
        details: str,
        code: str = "VALIDATION_ERROR",
        stack_trace: Optional[str] = None
    ):
        super().__init__(
            error_detail=ErrorDetail(
                code=code,
                details=details,
                stack_trace=stack_trace
            ),
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            message="One or more input validations failed."
        )


class NotFoundException(ApiException):
    """
    Custom error class for when a requested resource is not found.
    Corresponds to HTTP 404 Not Found.
    """
    def __init__(
        self,
        details: str,
        code: str = "RESOURCE_NOT_FOUND",
        stack_trace: Optional[str] = None
    ):
        super().__init__(
            error_detail=ErrorDetail(
                code=code,
                details=details,
                stack_trace=stack_trace
            ),
            status_code=status.HTTP_404_NOT_FOUND,
            message="The requested resource could not be found."
        )


class UnauthorizedException(ApiException):
    """
    Custom error class for authentication failures.
    Corresponds to HTTP 401 Unauthorized.
    """

    def __init__(
        self,
        details: str,
        code: str = "UNAUTHORIZED_ACCESS_DETECTED",
        stack_trace: Optional[str] = None
    ):
        super().__init__(
            error_detail=ErrorDetail(
                code=code,
                details=details,
                stack_trace=stack_trace
            ),
            status_code=status.HTTP_401_UNAUTHORIZED,
            message="Authentication failed! Please provide valid credentials."
        )


class BadRequestException(ApiException):
    """
    Custom error class for HTTP 400 Bad Request errors.
    Use for invalid requests, such as malformed input or invalid HTTP methods.
    """
    def __init__(
        self,
        details: str = "The request could not be understood or was missing "
                       "required parameters.",
        code: str = "BAD_REQUEST",
        stack_trace: Optional[str] = None
    ):
        super().__init__(
            error_detail=ErrorDetail(
                code=code,
                details=details,
                stack_trace=stack_trace
            ),
            status_code=status.HTTP_400_BAD_REQUEST,
            message="Bad request! Please check your input and try again."
        )


class UploadException(ApiException):
    """
    Custom error class for errors that occurred during the upload process.
    """
    def __init__(
        self,
        details: str = "The request could not be understood or was missing "
                       "required parameters.",
        code: str = "BAD_REQUEST",
        stack_trace: Optional[str] = None
    ):
        super().__init__(
            error_detail=ErrorDetail(
                code=code,
                details=details,
                stack_trace=stack_trace
            ),
            status_code=status.HTTP_400_BAD_REQUEST,
            message="Bad request! Please check your input and try again."
        )


class ForbiddenException(ApiException):
    """
    Custom error class for authorization failures (authenticated but not
    permitted).
    Corresponds to HTTP 403 Forbidden.
    """

    def __init__(
        self,
        details: str,
        code: str = "ACCESS_FORBIDDEN",
        stack_trace: Optional[str] = None
    ):
        super().__init__(
            error_detail=ErrorDetail(
                code=code,
                details=details,
                stack_trace=stack_trace
            ),
            status_code=status.HTTP_403_FORBIDDEN,
            message="Permission denied. You do not have access to this "
                      "resource."
        )

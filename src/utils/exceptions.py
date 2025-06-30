"""This module defines custom exceptions for the API."""
from abc import ABC
from typing import Optional

from fastapi import HTTPException, status
from src.utils.custom_response import ErrorResponse, ErrorDetail


class ApiError(HTTPException, ABC):
    """
    Custom base error class for API errors, providing a structured error response.
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
            error_detail: An instance of ErrorDetail providing specific error information.
            status_code: The HTTP status code for the response.
            message: A high-level message for the error response.
        """
        # Create the full ErrorResponse object
        self._error_response = ErrorResponse(
            success=False,
            message=message,
            status_code=status_code,
            error=error_detail
        )

        # Pass the dictionary representation of the ErrorResponse as the detail to HTTPException.
        # This allows our custom exception handler to easily access the structured response.
        super().__init__(status_code=status_code, detail=self._error_response.model_dump())


class ValidationError(ApiError):
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
            error_detail=ErrorDetail(code=code, details=details, stack_trace=stack_trace),
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            message="One or more input validations failed."
        )


class NotFoundError(ApiError):
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
            error_detail=ErrorDetail(code=code, details=details, stack_trace=stack_trace),
            status_code=status.HTTP_404_NOT_FOUND,
            message="The requested resource could not be found."
        )


class UnauthorizedError(ApiError):
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
            error_detail=ErrorDetail(code=code, details=details, stack_trace=stack_trace),
            status_code=status.HTTP_401_UNAUTHORIZED,
            message="Authentication failed! Please provide valid credentials."
        )


class BadRequestError(ApiError):
    """
    Custom error class for HTTP 400 Bad Request errors.
    Use for invalid requests, such as malformed input or invalid HTTP methods.
    """
    def __init__(
        self,
        details: str = "The request could not be understood or was missing required parameters.",
        code: str = "BAD_REQUEST",
        stack_trace: Optional[str] = None
    ):
        super().__init__(
            error_detail=ErrorDetail(code=code, details=details, stack_trace=stack_trace),
            status_code=status.HTTP_400_BAD_REQUEST,
            message="Bad request! Please check your input and try again."
        )


# TODO: REFACTOR THE REST OF THE ERROR CLASSES TO MATCH STANDARD



class ForbiddenError(ApiError):
    """
    Custom error class for authorization failures (authenticated but not permitted).
    Corresponds to HTTP 403 Forbidden.
    """

    def __init__(self, detail: str = "Permission denied. You do not have access to this resource."):
        """
        Initializes the ForbiddenError.

        Args:
            detail: A detailed message about the permission denial.
        """
        super().__init__(status_code=status.HTTP_403_FORBIDDEN, detail=detail)


class FileProcessingError(ApiError):
    """
    Custom error class for issues during file upload, reading, or processing.
    Corresponds to HTTP 500 Internal Server Error by default, but can be customized.
    """

    def __init__(
            self,
            detail: str = "File processing failed. Please check the file format or content."
    ):
        """
        Initializes the FileProcessingError.

        Args:
            detail: A detailed message about the file processing issue.
        """
        super().__init__(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=detail)


class DataCleaningError(ApiError):
    """
    Custom error class for issues encountered during data cleaning or transformation.
    Corresponds to HTTP 422 Unprocessable Entity, as it often relates to data quality.
    """

    def __init__(
            self,
            detail: str = "Data cleaning failed due to inconsistencies or invalid entries."
    ):
        """
        Initializes the DataCleaningError.

        Args:
            detail: A detailed message about the data cleaning issue.
        """
        super().__init__(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=detail)


class DuplicateEntryError(ApiError):
    """
    Custom error class for when an attempt is made to create a resource that already exists.
    Corresponds to HTTP 409 Conflict.
    """

    def __init__(self, detail: str = "A resource with these unique identifiers already exists."):
        """
        Initializes the DuplicateEntryError.

        Args:
            detail: A detailed message about the duplicate entry.
        """
        super().__init__(status_code=status.HTTP_409_CONFLICT, detail=detail)


class ServiceUnavailableError(ApiError):
    """
    Custom error class for when an external service or dependency is unavailable.
    Corresponds to HTTP 503 Service Unavailable.
    """

    def __init__(self, detail: str = "Service temporarily unavailable. Please try again later."):
        """
        Initializes the ServiceUnavailableError.

        Args:
            detail: A detailed message about the service unavailability.
        """
        super().__init__(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=detail)


class TooManyRequestsError(ApiError):
    """
    Custom error class for rate limiting issues.
    Corresponds to HTTP 429 Too Many Requests.
    """

    def __init__(self, detail: str = "Too many requests. Please try again later."):
        """
        Initializes the TooManyRequestsError.

        Args:
            detail: A detailed message about the rate limiting.
        """
        super().__init__(status_code=status.HTTP_429_TOO_MANY_REQUESTS, detail=detail)

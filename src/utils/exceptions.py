"""This module defines custom exceptions for the API."""

from fastapi import HTTPException, status


class ApiError(HTTPException):
    """
    Custom base error class for API errors.
    Inherits from HTTPException to provide a consistent error response format.
    All custom API-specific exceptions should inherit from this class.
    """

    def __init__(
            self,
            status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail: str = "An unexpected API error occurred."
    ):
        """
        Initializes the ApiError.

        Args:
            status_code: The HTTP status code for the error.
            detail: A detailed message describing the error.
        """
        super().__init__(status_code=status_code, detail=detail)


class ValidationError(ApiError):
    """
    Custom error class for validation errors (e.g., invalid input data).
    Corresponds to HTTP 422 Unprocessable Entity.
    """

    def __init__(self, detail: str = "Validation error: The provided data is invalid."):
        """
        Initializes the ValidationError.

        Args:
            detail: A detailed message describing the validation issue.
        """
        super().__init__(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=detail)


class NotFoundError(ApiError):
    """
    Custom error class for when a requested resource is not found.
    Corresponds to HTTP 404 Not Found.
    """

    def __init__(self, detail: str = "Resource not found."):
        """
        Initializes the NotFoundError.

        Args:
            detail: A detailed message describing the missing resource.
        """
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)


class UnauthorizedError(ApiError):
    """
    Custom error class for authentication failures.
    Corresponds to HTTP 401 Unauthorized.
    """

    def __init__(self, detail: str = "Authentication required or failed. Invalid credentials."):
        """
        Initializes the UnauthorizedError.

        Args:
            detail: A detailed message about the authentication failure.
        """
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail=detail)


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

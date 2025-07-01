"""
Global exception handler for structured error responses and logging.
"""

from fastapi import Request
from starlette.responses import JSONResponse

from src.exceptions.api_exceptions import ApiException
from src.utils.custom_responses import ErrorDetail, ErrorResponse
from src.utils.logger import get_logger

logger = get_logger(__name__)


async def api_exception_handler(
        request: Request,
        exc: ApiException
) -> JSONResponse:
    """
    Handles all exceptions derived from ApiException and
    returns a structured JSON response, and logs the error.
    """

    # Extract the structured error detail
    error_data = exc.detail.get("error", {})
    error_detail = ErrorDetail(**error_data)

    logger.error(
        "API Error occurred | Path: %s | "
        "Status Code: %d | Code: %s | Message: %s",
        request.url.path,
        exc.status_code,
        error_detail.code,
        error_detail.details
    )

    # Return a JSONResponse with the structured error
    return ErrorResponse(
        status_code=exc.status_code,
        message=error_detail.get("details", "An error occurred"),
        error=error_detail
    )

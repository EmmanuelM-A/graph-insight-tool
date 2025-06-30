"""This file contains the global exception/error handler"""

from fastapi import FastAPI, Request

from src.utils.exceptions import ApiError

from src.utils.logger import get_logger

logger = get_logger("exc_logger")

app = FastAPI()

@app.exception_handler(ApiError)
async def api_error_handler(request: Request, error: ApiError):
    """Global error handler function"""


    logger.error(
        "Error occurred: %s | "
        "Status Code: %d | "
        "Details: %s",
        error.detail["message"],
        error.status_code,
        error.detail
    )

    # exc.detail already contains your structured error response
    return error.detail

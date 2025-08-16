"""Handles the preprocessing of data uploaded by the user."""

from fastapi import UploadFile, File

from src.api.v1.controllers.upload_controller import process_upload_request
from src.services.data_preprocessor.data_check import DataSanityCheck
from src.services.data_preprocessor.data_treatment import (
    MissingValueTreatment,
    OutlierTreatment,
    DuplicateTreatment,
    GarbageValueTreatment)
from src.services.data_preprocessor.preprocessing_handler import (
    PreprocessingHandler)
from src.logging.logger import get_logger
from src.utils import api_exceptions as ae

logger = get_logger(__name__)


async def preprocess_data_request(
        file: UploadFile = File(...)
) -> object:
    """
    Handles the preprocessing of data based on the request.
    """

    # Get the uploaded file
    data_upload_response = await process_upload_request(file)

    uploaded_data = data_upload_response["data"]
    filename = file.filename

    # Check if the file actually contains data or is empty
    if uploaded_data is None or uploaded_data.empty:
        logger.error(
            "No data found in the uploaded file: %s",
            filename
        )

        raise ae.BadRequestException(
            details=f"No data found in the uploaded file: {filename}"
        )

    # Check the sensitivity of the data
    # if check_sensitivity(uploaded_data):
    #    logger.error("Data contains sensitive information!")
    #    handle_sensitivity_checker()
    # logger.info(
    #   "Sensitivity check completed, proceeding with preprocessing."
    # )

    # Set up the data preprocessor
    preprocessor = PreprocessingHandler(
        checks=[DataSanityCheck()],
        treatments=[
            MissingValueTreatment(),
            OutlierTreatment(),
            DuplicateTreatment(),
            GarbageValueTreatment()
        ],
        encoder=None,
        normalizer=None
    )

    try:
        processed_data = preprocessor.preprocess_data(uploaded_data)

        logger.info(
            "Data preprocessing for the file: %s was completed "
            "successfully.",
            filename
        )

        return {
            "preview": processed_data.head(10).to_json(),
            "data": processed_data
        }
    except Exception as e:
        logger.critical(
            "Unexpected error during file upload: %s",
            str(e),
            exc_info=True
        )

        raise ae.PreprocessingDataException(
            details=str(e)
        )

"""Handles the preprocessing of data uploaded by the user."""

from fastapi import status

from src.controllers.upload_controller import process_upload_request
from src.modules.data_preprocessor.data_check import DataSanityCheck
from src.modules.data_preprocessor.data_treatment import (
    MissingValueTreatment,
    OutlierTreatment,
    DuplicateTreatment,
    GarbageValueTreatment)
from src.modules.data_preprocessor.preprocessing_handler import PreprocessingHandler
from src.utils.custom_response import SuccessResponse
from src.utils.logger import get_logger
from src.utils import exceptions

logger = get_logger("process_controller_logger")


def preprocess_data_request(request) -> SuccessResponse | None:
    """
    Handles the preprocessing of data based on the request.
    """

    response = process_upload_request(request)

    if response.status_code != status.HTTP_200_OK:
        return response

    uploaded_data = response.data

    if uploaded_data is None or uploaded_data.empty:
        logger.error("No data found in the uploaded file!")

        raise exceptions.BadRequestError(
            details="No data found in the uploaded file!"
        )

    # Check the sensitivity of the data
    #if check_sensitivity(uploaded_data):
    #    logger.error("Data contains sensitive information!")

    #    handle_sensitivity_checker()

    #logger.info("Sensitivity check completed, proceeding with preprocessing.")"

    # Preprocess the data
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

        logger.info("Data preprocessing completed successfully.")

        return SuccessResponse(
            message="Data preprocessing completed successfully.",
            status_code=status.HTTP_200_OK,
            data={
                "preview": processed_data.head(10),
                "all_data": processed_data
            }
        )

    except ValueError as e:
        logger.error("Data preprocessing failed: ", str(e))

        return None
        #return CustomResponse(
        #    jsonify({
        #        "error": str(e)
        #    }),
        #    HTTP_BAD_REQUEST
        #)

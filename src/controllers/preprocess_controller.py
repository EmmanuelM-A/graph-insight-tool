import pandas as pd
from io import StringIO
from src.configs.http_response_codes import HTTP_BAD_REQUEST, HTTP_OK, HTTP_LOOP_DETECTED
from src.modules.data_preprocessor.data_check import DataSanityCheck
from src.modules.data_preprocessor.data_treatment import MissingValueTreatment, OutlierTreatment, DuplicateTreatment, \
    GarbageValueTreatment
from src.utils.custom_response import CustomResponse
from src.utils.logger import get_logger
from flask import jsonify
from src.controllers.upload_controller import process_upload_request
from src.modules.data_preprocessor.preprocessing_handler import PreprocessingHandler

logger = get_logger("process_controller_logger")

def preprocess_data_request(request):
    """
    Handles the preprocessing of data based on the request.
    """

    response = process_upload_request(request)

    if response.status_code != HTTP_OK:
        return response

    uploaded_data = response.data

    if uploaded_data is None or uploaded_data.empty:
        logger.error("No data found in the uploaded file!")
        return CustomResponse(
            jsonify({
                "error": "No data found in the uploaded file!"
            }),
            HTTP_BAD_REQUEST
        )

    # Check the sensitivity of the data
    """if check_sensitivity(uploaded_data):
        logger.error("Data contains sensitive information!")

        handle_sensitivity_checker()

    logger.info("Sensitivity check completed, proceeding with preprocessing.")"""

    # Preprocess the data
    preprocessor = PreprocessingHandler(
        checks=[DataSanityCheck()],
        treatments=[MissingValueTreatment(), OutlierTreatment(), DuplicateTreatment(), GarbageValueTreatment()],
        encoder=None,
        normalizer=None
    )

    try:
        processed_data = preprocessor.preprocess_data(uploaded_data)

        logger.info("Data preprocessing completed successfully.")

        return CustomResponse(
            jsonify({
                "message": "Data preprocessing completed successfully.",
                "preview": processed_data.head(10).to_json()
            }),
            HTTP_OK,
            data=processed_data
        )

    except ValueError as e:
        logger.error(f"Data preprocessing failed: {e}")

        return CustomResponse(
            jsonify({
                "error": str(e)
            }),
            HTTP_BAD_REQUEST
        )

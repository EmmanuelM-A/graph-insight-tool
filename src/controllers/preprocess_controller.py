from src.configs.http_response_codes import HTTP_BAD_REQUEST, HTTP_OK
from src.modules.data_preprocessor.data_check import DataSanityCheck
from src.modules.data_preprocessor.data_treatment import MissingValueTreatment, OutlierTreatment, DuplicateTreatment, \
    GarbageValueTreatment
from src.utils.logger import get_logger
from flask import jsonify
from src.controllers.upload_controller import process_upload_request
from src.modules.data_preprocessor.preprocessing_handler import PreprocessingHandler

logger = get_logger("process_controller_logger")

def preprocess_data_request(request):
    """
    Handles the preprocessing of data based on the request.
    """

    json_data, http_response = process_upload_request(request, return_all_data=True)

    if http_response != HTTP_OK:
        return jsonify({
            "error": json_data.get("error")
        }), http_response

    uploaded_data = json_data.get("data")

    if not uploaded_data:
        logger.error("No data found in the uploaded file!")
        return jsonify({
            "error": "No data found in the uploaded file!"
        }), HTTP_BAD_REQUEST

    # Check the sensitivity of the data
    """if check_sensitivity(uploaded_data):
        logger.error("Data contains sensitive information!")

        handle_sensitivity_checker()

    logger.info("Sensitivity check completed, proceeding with preprocessing.")"""

    # Preprocess the data
    preprocessor = PreprocessingHandler(
        checks=[DataSanityCheck()],
        treatments=[MissingValueTreatment(), OutlierTreatment(), DuplicateTreatment, GarbageValueTreatment],
        encoder=None,
        normalizer=None
    )

    try:
        processed_data = preprocessor.preprocess_data(json_data["data"])

        logger.info("Data preprocessing completed successfully.")

        return jsonify({
            "message": "Data preprocessing completed successfully.",
            "data": processed_data
        }), HTTP_OK

    except ValueError as e:
        logger.error(f"Data preprocessing failed: {e}")
        return jsonify({
            "error": str(e)
        }), HTTP_BAD_REQUEST

from src.configs.http_response_codes import HTTP_BAD_REQUEST, HTTP_OK
from src.utils.logger import get_logger
from flask import jsonify
from src.controllers.upload_controller import process_upload_request
from src.modules.data_sensitivity.check_sensitivity import check_sensitivity, handle_sensitivity_checker

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
    if check_sensitivity(uploaded_data):
        logger.error("Data contains sensitive information!")

        handle_sensitivity_checker()

    logger.info("Sensitivity check completed, proceeding with preprocessing.")

    # Preprocess the data


    return None
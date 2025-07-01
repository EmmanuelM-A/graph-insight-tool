"""Upload Handler"""

import pandas as pd
from src.services.data_uploader.data_loader import (CSVDataLoader,
                                                    ExcelDataLoader)
from src.utils.logger import get_logger

logger = get_logger("upload_handler_logger")


def get_loader(filepath: str) -> type[CSVDataLoader | ExcelDataLoader]:
    """
    Returns the correct loader instance that corresponds to the file
    extension. If no loader can be found for the file
    then an unsupported format error is raised.
    :param filepath:
    :return:
    """

    if filepath.endswith(".csv"):
        return CSVDataLoader
    elif filepath.endswith(".xlsx") or filepath.endswith(".xls"):
        return ExcelDataLoader
    else:
        logger.warning("Unsupported file type detected!")
        raise ValueError("Unsupported file type detected!")


def handle_upload(filepath: str) -> tuple[pd.DataFrame | None, str]:
    """
    Handles the upload by using the appropriate file loader to load the
    file into a DataFrame.
    Returns the DataFrame and a status message.
    """
    try:
        # Get appropriate loader based on file extension
        file_loader = get_loader(filepath)()

        # Use loader to read the file into a DataFrame
        data, message = file_loader.load_data(filepath)

        return data, message
    except Exception as e:
        logger.error(f"Upload failed: {e}")
        return None, str(e)

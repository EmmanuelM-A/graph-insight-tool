from dataclasses import dataclass

import pandas as pd
from flask import Response


@dataclass
class CustomResponse:
    """
    Custom response class to handle API responses with a consistent structure.
    """

    def __init__(self, json_object: Response, status_code: int, data: pd.DataFrame = None) -> None:
        """
        Initializes the CustomResponse object.
        :param json_object: The JSON response object to be returned.
        :param status_code: The HTTP status code for the response.
        :param data: The data to be included in the response, if any (default is None).
        """
        self.json_object = json_object
        self.data = data
        self.status_code = status_code

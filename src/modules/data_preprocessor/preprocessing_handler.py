import pandas as pd
from abc import ABC, abstractmethod

class PreprocessingHandler:
    """
    PreprocessingHandler is responsible for managing the preprocessing of data.
    """
    
    def __init__(self, data: pd.DataFrame) -> None:
        self.data = data
        self.__data_treatments = []
        self.__data_checks = []
        self.__encoders = []
        self.__normalizers = []

    def preprocess_data(self) -> pd.DataFrame:
        pass


class DataPreprocessor(ABC):
    """
    Abstract base class for data preprocessing.
    """

    def preprocess_data(self, data: pd.DataFrame) -> pd.DataFrame:
        if not self.run_data_checks(data):
            raise ValueError("Data does not meet the required conditions.")
            
        treated_data = self.run_data_treatments(data)

        normalized_data = self.normalize_data(treated_data)

        encoded_data = self.encode_data(normalized_data)

        return encoded_data

    def run_data_treatments(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Get the list of treatments applied during preprocessing.

        :return: List of treatments.
        """
        pass

    def run_data_checks(self, data: pd.DataFrame) -> bool:
        """
        Run data checks to ensure the data meets the required conditions.

        :param data: DataFrame to check.
        :return: True if data passes all checks, False otherwise.
        """
        pass

    def encode_data(self, data: pd.DataFrame) -> pd.DataFrame:
        pass

    def normalize_data(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Run normalizers on the data.

        :param data: DataFrame to normalize.
        :return: Normalized DataFrame.
        """
        pass
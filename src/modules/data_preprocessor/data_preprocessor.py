from abc import ABC
import pandas as pd

class DataPreprocessor(ABC):
    """
    Abstract base class for data preprocessing.
    """

    def preprocess_data(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Preprocess the data by running checks, treatments, normalization, and encoding.
        :param data: DataFrame to preprocess.
        :return: Preprocessed DataFrame.
        """

        if not self.run_data_checks(data):
            raise ValueError("Data does not meet the required conditions.")

        treated_data = self.run_data_treatments(data)

        normalized_data = self.normalize_data(treated_data)

        encoded_data = self.encode_data(normalized_data)

        return encoded_data

    def run_data_treatments(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Run data treatments on the DataFrame.

        :param data: DataFrame to treat.
        :return: Treated DataFrame.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    def run_data_checks(self, data: pd.DataFrame) -> bool:
        """
        Run data checks to ensure the data meets the required conditions.

        :param data: DataFrame to check.
        :return: True if data passes all checks, False otherwise.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    def encode_data(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Run encoder on the data.

        :param data: DataFrame to encode.
        :return: Encoded DataFrame.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    def normalize_data(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Run normalizer on the data.

        :param data: DataFrame to normalize.
        :return: Normalized DataFrame.
        """
        raise NotImplementedError("Subclasses must implement this method.")
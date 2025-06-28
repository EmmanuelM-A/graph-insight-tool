from abc import ABC
import pandas as pd

from src.modules.data_preprocessor.data_check import DataCheck
from src.modules.data_preprocessor.data_encoder import DataEncoder
from src.modules.data_preprocessor.data_normalizer import DataNormalizer
from src.modules.data_preprocessor.data_treatment import DataTreatment


class DataPreprocessor(ABC):
    """
    Abstract base class for data preprocessing.
    """

    def __init__(
            self,
            checks: list[DataCheck],
            treatments: list[DataTreatment],
            encoder: DataEncoder = None,
            normalizer: DataNormalizer = None
    ) -> None:
        self.checks = checks
        self.treatments = treatments
        self.encoder = encoder
        self.normalizer = normalizer


    def preprocess_data(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Preprocess the data by running checks, treatments, normalization, and encoding.
        :param data: DataFrame to preprocess.
        :return: Preprocessed DataFrame.
        """

        encoded_data, normalized_data = None, None

        if not self.validate_data(data):
            raise ValueError("Data does not meet the required conditions.")

        treated_data = self.run_data_treatments(data)

        if self.normalizer:
            normalized_data = self.normalizer.normalize(treated_data)

        if self.encoder:
            encoded_data = self.encoder.encode(normalized_data)

        # Assuming that if normalization is not applied, we return treated data directly

        return treated_data if encoded_data is None else encoded_data


    def run_data_treatments(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Run data treatments on the DataFrame.

        :param data: DataFrame to treat.
        :return: Treated DataFrame.
        """
        raise NotImplementedError("Subclasses must implement this method.")


    def validate_data(self, data: pd.DataFrame) -> bool:
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
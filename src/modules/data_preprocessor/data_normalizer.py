from abc import ABC, abstractmethod
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler


class DataNormalizer(ABC):
    """
    Abstract base class for data normalizers.
    This class defines the interface for normalizing data.
    """

    @abstractmethod
    def normalize(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Normalize the given data.

        :param data: The DataFrame to normalize.
        :return: A normalized DataFrame.
        """
        raise NotImplementedError("Subclasses must implement this method.")


class MinMaxNormalizer(DataNormalizer):
    """
    Concrete implementation of DataNormalizer using Min-Max normalization.
    Scales numerical columns to a range between 0 and 1.
    """

    def normalize(self, data: pd.DataFrame) -> pd.DataFrame:
        scaler = MinMaxScaler()
        numeric_cols = data.select_dtypes(include=[np.number]).columns
        data[numeric_cols] = scaler.fit_transform(data[numeric_cols])
        return data

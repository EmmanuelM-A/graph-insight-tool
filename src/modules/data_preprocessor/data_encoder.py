from abc import ABC, abstractmethod
import pandas as pd
from sklearn.preprocessing import LabelEncoder


class DataEncoder(ABC):
    """
    Abstract base class for data encoders.
    This class defines the interface for encoding categorical data.
    """

    @abstractmethod
    def encode(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Encode the categorical data in the given DataFrame.

        :param data: The DataFrame containing categorical data to encode.
        :return: A DataFrame with encoded categorical data.
        """
        raise NotImplementedError("Subclasses must implement this method.")


class LabelEncodingEncoder(DataEncoder):
    """
    Concrete implementation of DataEncoder using Label Encoding.
    Applies label encoding to all object or category dtype columns.
    """

    def encode(self, data: pd.DataFrame) -> pd.DataFrame:
        label_encoder = LabelEncoder()
        for col in data.select_dtypes(include=["object", "category"]).columns:
            data[col] = label_encoder.fit_transform(data[col].astype(str))
        return data

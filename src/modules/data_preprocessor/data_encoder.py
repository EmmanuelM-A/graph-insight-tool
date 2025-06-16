from abc import ABC, abstractmethod
import pandas as pd

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
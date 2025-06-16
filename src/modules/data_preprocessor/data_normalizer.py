from abc import ABC, abstractmethod
import pandas as pd

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